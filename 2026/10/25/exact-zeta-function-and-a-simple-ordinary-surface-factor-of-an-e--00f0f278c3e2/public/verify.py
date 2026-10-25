#!/usr/bin/env python3
"""Exact finite-field verification for a genus-ten generalized Fermat curve.

The formulas hold for the smooth projective intersection
 V^3+U^3+Z^3 = W^3+U^3+omega*Z^3 = 0,
with omega^2+omega+1=0 over F4. No external packages are required.
"""
from itertools import product

# Irreducible moduli for GF(2^k), k=2,4,6,8.
MODULI={2:0b111,4:0b10011,6:0b1000011,8:0b100011101}

class Field:
    def __init__(self,k):
        self.k=k
        self.q=1<<k
        self.mod=MODULI[k]
        self.omega=next(a for a in range(2,self.q)
                        if self.mul(a,a)^a^1==0)
        self.cubes={self.mul(self.mul(a,a),a) for a in range(self.q)}
        assert len(self.cubes)==(self.q-1)//3+1
    def mul(self,a,b):
        z=0
        while b:
            if b&1:z^=a
            a<<=1
            if a&self.q:a^=self.mod
            b>>=1
        return z
    def roots3(self,a):
        return 1 if a==0 else (3 if a in self.cubes else 0)
    def pow012(self,a,j):
        if j==0:return 1
        if j==1:return a
        if j==2:return self.mul(a,a)
        raise ValueError('invalid exponent')

def projective_point_count_f4():
    f=Field(2)
    seen=set()
    for tup in product(range(4),repeat=4):
        if not any(tup):continue
        # Each projective point has 3 nonzero representatives.
        orbit=[]
        for a in (1,f.omega,f.omega^1):
            orbit.append(tuple(f.mul(a,v) for v in tup))
        rep=min(orbit)
        seen.add(rep)
    cnt=0
    for u,v,w,z in seen:
        cube=lambda a:f.mul(f.mul(a,a),a)
        if (cube(v)^cube(u)^cube(z))==0 and \
           (cube(w)^cube(u)^f.mul(f.omega,cube(z)))==0:
            cnt+=1
    assert len(seen)==85
    return cnt

def quotient_representatives():
    reps=[]
    for v in product(range(3),repeat=3):
        if v==(0,0,0):continue
        negative=tuple((-e)%3 for e in v)
        if v>negative:continue
        r=sum(e!=0 for e in v)+int(sum(v)%3!=0)
        reps.append((v,r-2))
    return reps

def quotient_count(f,v):
    a,b,c=v
    count=3 if sum(v)%3==0 else 1 # infinity
    for t in range(f.q):
        rhs=f.mul(f.mul(f.pow012(t,a),f.pow012(t^1,b)),
                  f.pow012(t^f.omega,c))
        count+=f.roots3(rhs)
    return count

def full_count(f):
    # All 9 points above infinity are rational over every F(4^n).
    count=9
    for t in range(f.q):
        count+=f.roots3(t)*f.roots3(t^1)*f.roots3(t^f.omega)
    return count

def multiply_poly(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def power_poly(a,n):
    z=[1]
    for i in range(n):z=multiply_poly(z,a)
    return z

def zeta_trace_sequence(P,nmax):
    # P(T)=exp(-sum(s_n T^n/n)), using Newton's recurrence.
    s=[]
    for n in range(1,nmax+1):
        acc=n*P[n]
        for i in range(1,n):acc+=P[n-i]*s[i-1]
        s.append(-acc)
    return s

def main():
    assert projective_point_count_f4()==9
    reps=quotient_representatives()
    assert len(reps)==13
    assert sorted(g for v,g in reps)==[0]*6+[1]*4+[2]*3
    assert sum(g for v,g in reps)==10
    f4,f16=Field(2),Field(4)
    counts={}
    for v,g in reps:
        if g==0:continue
        counts[v]=(g,quotient_count(f4,v),quotient_count(f16,v))
    expected={
       (0,1,1):(1,3,21),
       (1,0,1):(1,3,21),
       (1,1,0):(1,9,9),
       (1,1,1):(1,9,9),
       (1,1,2):(2,7,31),
       (1,2,1):(2,4,10),
       (1,2,2):(2,4,10),
    }
    assert counts==expected,(counts,expected)
    quotient_polynomials=[]
    for v,(g,N1,N2) in counts.items():
        s1=5-N1
        s2=17-N2
        if g==1:
            # Validate the second count from elliptic Frobenius relation.
            assert s2==s1*s1-8
            P=[1,-s1,4]
        else:
            b=(s1*s1-s2)//2
            assert 2*b==s1*s1-s2
            P=[1,-s1,b,-4*s1,16]
        quotient_polynomials.append(P)
    overall=[1]
    for P in quotient_polynomials:overall=multiply_poly(overall,P)
    A=[1,-2,4]
    B=[1,4,4]
    C=[1,1,4]
    D=[1,-1,-3,-4,16]
    expected_overall=[1]
    for factor in (A,B,C,D):
        expected_overall=multiply_poly(expected_overall,power_poly(factor,2))
    assert overall==expected_overall
    assert len(overall)==21 and overall[-1]==4**10
    traces=zeta_trace_sequence(overall,4)
    expected_N=[9,9,63,225]
    for i,k in enumerate((2,4,6,8),start=1):
        f=Field(k)
        direct=full_count(f)
        predicted=4**i+1-traces[i-1]
        assert direct==predicted==expected_N[i-1],(i,direct,predicted)
    # Rationality over F4 and its degree-two extension is also checked via
    # projective enumeration and the quotient point-count identities.
    assert full_count(f4)==projective_point_count_f4()
    assert sum(5-N1 for g,N1,N2 in counts.values())==5-full_count(f4)
    print('GENUS=10; QUOTIENT_GENUS_PROFILE=4x1+3x2')
    print('F4_QUOTIENT_DATA',sorted((v,)+z for v,z in counts.items()))
    print('ZETA_NUMERATOR_COEFFICIENTS',overall)
    print('POINT_COUNTS_F4_F16_F64_F256',expected_N)
    print('VERIFY_OK')

if __name__=='__main__':main()
