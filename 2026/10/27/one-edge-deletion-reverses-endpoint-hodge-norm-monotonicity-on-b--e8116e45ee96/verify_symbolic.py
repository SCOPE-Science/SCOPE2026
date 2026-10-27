"""Self-contained polynomial certificate for the tripartite projection theorem.

All polynomials use exact integer coefficients in t=m-2. Positivity of
coefficients proves their sign for every integer m>=2. No external modules.
"""

class Poly:
    def __init__(self, coeffs):
        if isinstance(coeffs, Poly): coeffs=coeffs.c
        if isinstance(coeffs, int): coeffs=(coeffs,)
        a=list(coeffs)
        while len(a)>1 and a[-1]==0:a.pop()
        self.c=tuple(a)
    @staticmethod
    def aspoly(x):return x if isinstance(x,Poly) else Poly(x)
    def __add__(self, other):
        other=self.aspoly(other)
        return Poly([(self.c[i] if i<len(self.c) else 0)+(other.c[i] if i<len(other.c) else 0)
                     for i in range(max(len(self.c),len(other.c)))])
    __radd__=__add__
    def __neg__(self):return Poly([-x for x in self.c])
    def __sub__(self,other):return self+-self.aspoly(other)
    def __rsub__(self,other):return self.aspoly(other)+-self
    def __mul__(self,other):
        other=self.aspoly(other)
        ans=[0]*(len(self.c)+len(other.c)-1)
        for i,a in enumerate(self.c):
            for j,b in enumerate(other.c):ans[i+j]+=a*b
        return Poly(ans)
    __rmul__=__mul__
    def __pow__(self,k):
        assert isinstance(k,int) and k>=0
        ans=Poly(1)
        for _ in range(k):ans=ans*self
        return ans
    def __eq__(self,other):return self.c==self.aspoly(other).c
    def sign(self):
        if all(a>=0 for a in self.c):return 0 if self==0 else +1
        if all(a<=0 for a in self.c):return -1
        raise AssertionError('unresolved coefficient sign '+repr(self.c))
    def substitute_t_plus(self,k):
        # if input uses t=m-2, then m>=k means t=s+(k-2)
        s=Poly((0,1));d=k-2
        ans=Poly(0)
        for j,a in enumerate(self.c):ans=ans+a*(s+d)**j
        return ans

T=Poly((0,1));m=T+2
D=3*m*m-3*m+1
H=12*m*m*D
V={
 'X':[3*m*(2*m-1)*(3*m-1),-3*m*(2*m-1),-3*m*(2*m-1),
      -3*m*(m-1),-3*m*(6*m*m-8*m+3),3*m*(2*m-1),0,0],
 'Y':[-6*m*m,6*m*(3*m*m-4*m+2),-6*m*(m-1),
      6*m*m,-6*m*(3*m*m-4*m+2),6*m*(m-1),0,0],
 'Z':[(3*m-1)*(6*m*m-3*m+1),-(6*m*m-3*m+1),-(6*m*m-3*m+1),
      -(3*m-1)**2,3*m-1,3*m-1,-2*(3*m-1)*D,2*D],
 'W':[-(6*m*m-3*m+1),18*m**3-24*m*m+12*m-1,-(6*m*m-6*m+1),
      3*m-1,-1,-1,-2*(3*m-1)*D,2*D]
}
# Types: A0,A1,A*,B0,B1,B*,C0,C*; stars have multiplicities m-2,m-2,m-1.
sizes=[1,1,m-2,1,1,m-2,1,m-1]
parts=[0,0,0,1,1,1,2,2]
target={'X':(0,4),'Y':(1,4),'Z':(0,6),'W':(1,6)}
def base_potential_numerators(src,dst):
    # For K_{m,m,m}, the potential of a unit current from src to dst,
    # multiplied by 6m^2, is this eight-type vector.
    a,b=parts[src],parts[dst]
    assert a!=b
    z=[]
    for i,g in enumerate(parts):
        if i==src:z.append(3*m-1)
        elif i==dst:z.append(-(3*m-1))
        elif g==a:z.append(Poly(-1))
        elif g==b:z.append(Poly(1))
        else:z.append(Poly(0))
    return [Poly.aspoly(p) for p in z]

b0=base_potential_numerators(0,3)
for name,(src,dst) in target.items():
    bf=base_potential_numerators(src,dst)
    c=b0[src]-b0[dst]
    for i in range(8):
        # Sherman-Morrison: deleted-edge voltage, multiplied by
        # 12m^2(3m^2-3m+1), has this polynomial numerator.
        assert Poly.aspoly(V[name][i])==2*D*bf[i]+(b0[src]-b0[dst])*b0[i],(name,i)
print('RANK_ONE_VOLTAGE_IDENTITIES_OK')

numQ={};numP={}
for name,v in V.items():
    assert len(v)==8
    ans=Poly(0);nonzero=0
    for i in range(8):
        for j in range(i+1,8):
            if parts[i]==parts[j] or (i,j)==(0,3):continue
            diff=Poly.aspoly(v[i])-Poly.aspoly(v[j])
            sig=diff.sign()  # proved for every integer m>=2
            ans+=sig*sizes[i]*sizes[j]*diff
            nonzero += int(sig!=0)
    numQ[name]=ans
    u,w=target[name]
    numP[name]=H+ans-2*(Poly.aspoly(v[u])-Poly.aspoly(v[w]))
    print(name,'signed edge classes',nonzero)

# Independent closed expressions; cross-multiply, no floating-point evaluation.
formulas={
 'X':((2*m-1)*(4*m*m-5*m+2),m*D,
       22*m**3-46*m*m+33*m-8,2*m*D),
 'Y':(8*m**3-14*m*m+11*m-4,m*D,
       (m-1)*(11*m*m-12*m+8),m*D),
 'Z':(16*m**4-26*m**3+16*m*m-5*m+1,2*m*m*D,
       (m-1)*(22*m**3-22*m*m+9*m-2),2*m*m*D),
 'W':(16*m**4-28*m**3+21*m*m-8*m+1,2*m*m*D,
       (2*m*m-2*m+1)*(11*m*m-12*m+2),2*m*m*D)
}
for name, (nq,dq,np,dp) in formulas.items():
    assert numQ[name]*dq==nq*H,name+' Q'
    assert numP[name]*dp==np*H,name+' P'

def gap_positive(A,B,typ,k):
    n1,d1= formulas[A][0:2] if typ=='Q' else formulas[A][2:4]
    n2,d2= formulas[B][0:2] if typ=='Q' else formulas[B][2:4]
    assert (n1*d2-n2*d1).substitute_t_plus(k).sign()==1,(A,B,typ,k)

def gap_at(A,B,typ,k):
    n1,d1=formulas[A][0:2] if typ=='Q' else formulas[A][2:4]
    n2,d2=formulas[B][0:2] if typ=='Q' else formulas[B][2:4]
    assert (n1*d2-n2*d1).substitute_t_plus(k).c[0]>0

# The only possible maximizers: Y or Z.
for typ in ('Q','P'):
    for a,b in [('Y','X'),('Y','W')]: gap_positive(a,b,typ,2)
    gap_positive('Z','W',typ,3 if typ=='Q' else 4)
gap_at('Y','Z','Q',2)
gap_positive('Z','Y','Q',3)
gap_at('Y','Z','P',2)
gap_at('Y','Z','P',3)
gap_positive('Z','Y','P',4)

# Compared with the intact graph: Q0=2(4m²-3m+1)/(3m²),
# P0=(11m²-12m+4)/(3m²).  Verify strict increase except P at m=2.
q0n=2*(4*m*m-3*m+1);p0n=11*m*m-12*m+4;d0=3*m*m
for typ,which,k in [('Q','Y',2),('Q','Z',3),('P','Y',3),('P','Z',4)]:
    n,d=formulas[which][0:2] if typ=='Q' else formulas[which][2:4]
    pn=q0n if typ=='Q' else p0n
    assert (n*d0-pn*d).substitute_t_plus(k).sign()==1,(typ,which,k)
# at m=2, cycle-projection norm unchanged.
py,pyd=formulas['Y'][2:4]
assert (py*d0-p0n*pyd).substitute_t_plus(2).sign()==1  # zero only at m=2
assert sum((py*d0-p0n*pyd).c[0:1])==0
print('SYMBOLIC_TRIPARTITE_CERTIFICATE_OK')
