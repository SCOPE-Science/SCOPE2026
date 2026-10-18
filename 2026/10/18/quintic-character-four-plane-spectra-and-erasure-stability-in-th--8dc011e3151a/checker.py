"""Exact finite certificate for the two quintic-character harmonic fusion-plane spectra.
Python 3 standard library only; no numerical floating-point tests are used.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, pi, sqrt
from cmath import exp

MOD = 11
EXPONENT = {pow(2, j, 11): j % 5 for j in range(10)}
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
# Coefficients in Z[w] with w^4+w^3+w^2+w+1 = 0.
POWERS = [tuple(int(j == k) for j in range(4)) for k in range(4)]
POWERS.append((-1, -1, -1, -1))

def plus(a, b):
    return tuple(x+y for x,y in zip(a,b))

def times_int(a, n):
    return tuple(n*x for x in a)

def mul(a,b):
    c = [0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    for d in (6,5,4):
        z = c[d]
        for j in range(1,5):
            c[d-j] -= z
    return tuple(c[:4])

def sum_ring(seq):
    out=[0]*4
    for v in seq:
        for j in range(4):
            out[j]+=v[j]
    return tuple(out)

def matmul(A,B):
    n=len(A)
    return [[sum_ring(mul(A[i][k], B[k][j]) for k in range(n))
             for j in range(n)] for i in range(n)]

def charpoly(rep):
    n=8
    M=[[ZERO for _ in range(n)] for _ in range(n)]
    for i,a in enumerate(rep):
        for j,b in enumerate(rep):
            if i==j:
                continue
            h=EXPONENT[(b-a)%MOD]
            M[2*i][2*j]=ONE
            M[2*i+1][2*j+1]=times_int(ONE,-1)
            M[2*i][2*j+1]=times_int(POWERS[h],3)
            M[2*i+1][2*j]=times_int(POWERS[-h%5],3)
    cp=[ONE]
    traces=[]
    power=[[ONE if i==j else ZERO for j in range(n)] for i in range(n)]
    for degree in range(1,n+1):
        power=matmul(power,M)
        traces.append(sum_ring(power[i][i] for i in range(n)))
        val=sum_ring(mul(cp[degree-j],traces[j-1]) for j in range(1,degree+1))
        val=times_int(val,-1)
        assert all(z%degree==0 for z in val)
        cp.append(tuple(z//degree for z in val))
    return cp

# Q_A(Y)=Y^4-120Y^3+(a+b*t)Y^2+(c+d*t)Y+(e+f*t),
# where t=w^2+w^3=(-1-sqrt(5))/2, or its conjugate.
TABLE={
  (0,1,2,3):(55, 4530,-90,-58600,1800,133650,9225),
  (0,1,2,4):(110,4350,-90,-51760,180,83250,25425),
  (0,1,2,5):(110,4170,270,-47350,-7425,130050,29025),
  (0,1,3,4):(55,4530,-270,-65080,8640,271350,-41175),
}

def affine_orbit(rep):
    return {tuple(sorted((a*x+b)%MOD for x in rep))
            for a in range(1,MOD) for b in range(MOD)}

# Pair (r,s) represents r+s*sqrt(5), with rational r,s.
def radd(u,v):
    return (u[0]+v[0],u[1]+v[1])

def rscale(u,s):
    return (s*u[0],s*u[1])

def rsign(u):
    a,b=u
    if not b: return (a>0)-(a<0)
    if a==0: return (b>0)-(b<0)
    if a>0 and b>0:return 1
    if a<0 and b<0:return -1
    if a*a==5*b*b: return 0
    if a*a>5*b*b:return (a>0)-(a<0)
    return (b>0)-(b<0)

def poly_row(row, branch):
    _,a,b,c,d,e,f=row
    # branch=-1 for t_-=(-1-sqrt5)/2; +1 for t_+
    def convert(A,B):return (Q(A)-Q(B,2), Q(branch*B,2))
    return [convert(e,f),convert(c,d),convert(a,b),(Q(-120),Q(0)),(Q(1),Q(0))]

def evaluate(coeffs,x):
    return tuple(sum(coeffs[j][i]*x**j for j in range(5)) for i in range(2))

def shifted_coeffs(coeffs,U):
    return [tuple(sum(comb(j,k)*coeffs[j][i]*U**(j-k) for j in range(k,5))
                  for i in range(2)) for k in range(5)]

# Rational root brackets chosen to separate the four largest roots in each branch.
INTERVALS={
  -1: { (0,1,2,3):(Q(51),Q(52)),(0,1,2,4):(Q(56),Q(57)),
         (0,1,2,5):(Q(77),Q(78)),(0,1,3,4):(Q(27),Q(43))},
  +1: { (0,1,2,3):(Q(62),Q(63)),(0,1,2,4):(Q(672,10),Q(673,10)),
         (0,1,2,5):(Q(65),Q(66)),(0,1,3,4):(Q(679,10),Q(68))},
}

def check_direct_harmonic_frame():
    # Independent floating-point diagnostic for the source's 11-by-2 isometries;
    # the finite spectral certificate below does not rely on floating point.
    for k in (1,2):
        chi = {x: exp(2j*pi*k*EXPONENT[x]/5) for x in range(1,11)}
        tau = sum(chi[t].conjugate()*exp(2j*pi*t/11) for t in range(1,11))
        assert abs(abs(tau)-sqrt(11))<1e-12
        phase=tau/abs(tau)
        vec=[]
        for a in range(11):
            rows=[]
            for t in range(11):
                v=(1+0j,0j) if t==0 else (3/sqrt(20),sqrt(11/20)*chi[t].conjugate())
                scale=sqrt(2/11)*exp(2j*pi*a*t/11)
                rows.append((scale*v[0],scale*v[1]))
            vec.append(rows)
        for a in range(11):
            for b in range(11):
                block=[[sum(vec[a][t][i].conjugate()*vec[b][t][j] for t in range(11))
                        for j in range(2)] for i in range(2)]
                if a==b:
                    expected=((1,0),(0,1))
                else:
                    z=chi[(b-a)%11]
                    expected=((.1,.3*z),(.3*z.conjugate(),-.1))
                    block[0][1]*=phase.conjugate()
                    block[1][0]*=phase
                assert max(abs(block[i][j]-expected[i][j])
                           for i in range(2) for j in range(2))<5e-14
    print('DIRECT_FRAME_CHECK_PASS 242 gauged Gram blocks for both character classes')

def run():
    check_direct_harmonic_frame()
    universe=set(combinations(range(11),4))
    assert len(universe)==330
    union=set()
    for rep,row in TABLE.items():
        orbit=affine_orbit(rep)
        assert len(orbit)==row[0] and not union.intersection(orbit)
        union.update(orbit)
        coeffs=charpoly(rep)
        assert coeffs[1]==coeffs[3]==coeffs[5]==coeffs[7]==ZERO
        assert coeffs[2]==times_int(ONE,-120)
        for j in range(3):
            a,b=row[1+2*j],row[2+2*j]
            assert coeffs[4+2*j]==plus(times_int(ONE,a),times_int(plus(POWERS[2],POWERS[3]),b))
        for branch in (-1,+1):
            L,U=INTERVALS[branch][rep]
            poly=poly_row(row,branch)
            assert rsign(evaluate(poly,L))<0,(branch,rep,'low')
            for v in shifted_coeffs(poly,U):
                assert rsign(v)>0,(branch,rep,'positive_shift_coeff',v)
        print('EXACT_PROFILE',rep,'quartets',row[0],'coefficients',row[1:])
    assert union==universe
    # For a monic polynomial all-positive coefficients of Q(U+z)
    # exclude all real roots at or above U, whereas Q(L)<0 and
    # Q(Y)->+infinity force a real root greater than L.
    assert INTERVALS[-1][(0,1,2,5)][0]>max(
        INTERVALS[-1][r][1] for r in TABLE if r!=(0,1,2,5))
    assert INTERVALS[+1][(0,1,3,4)][0]>max(
        INTERVALS[+1][r][1] for r in TABLE if r!=(0,1,3,4))
    for branch in (-1,+1):
        print('ROOT_CERTIFICATE',branch,[(rep,str(INTERVALS[branch][rep])) for rep in TABLE])
    print('CHECK_PASS 330 quartets, four affine orbits, eight exact quartic profiles and root-separation certificates')

if __name__=='__main__':
    run()
