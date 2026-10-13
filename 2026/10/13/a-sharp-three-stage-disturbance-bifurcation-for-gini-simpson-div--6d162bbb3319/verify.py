"""Exact-arithmetic checks for a three-stage ecological succession diversity theorem.

Run: python verify.py  (Python 3 standard library only).
The accompanying proof establishes the infinite-domain statements.
"""
from fractions import Fraction as Q
from math import comb

# Coefficients are ordered by increasing powers of their variable.
P = [Q(-1), Q(27), Q(-252), Q(918), Q(-594), Q(540), Q(135), Q(27)]
T = [Q(-1), Q(15), Q(-50), Q(51), Q(5)]

def trim(p):
    p = list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])

def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)

def evalp(p,t):
    result=Q(0)
    for c in reversed(p): result=result*t+c
    return result

def divmodp(a,b):
    a=trim(a); b=trim(b)
    q=[Q(0)]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and a != [0]:
        i=len(a)-len(b)
        c=a[-1]/b[-1]
        q[i]+=c
        for j in range(len(b)): a[i+j]-=c*b[j]
        a=trim(a)
    return trim(q),a

def det_rational(M):
    A=[[Q(x) for x in row] for row in M]
    n=len(A); s=Q(1)
    for k in range(n):
        v=next((j for j in range(k,n) if A[j][k]),None)
        if v is None: return Q(0)
        if v!=k:
            A[k],A[v]=A[v],A[k]
            s=-s
        piv=A[k][k]
        s*=piv
        for i in range(k+1,n):
            z=A[i][k]/piv
            for j in range(k+1,n): A[i][j]-=z*A[k][j]
            A[i][k]=0
    return s

def quartic_discriminant(coeff):
    # For a monic quartic, discriminant = resultant(F,F').
    a=list(reversed(coeff))
    d=[4*a[0],3*a[1],2*a[2],a[3]]
    syl=[]
    for off in range(3):
        row=[Q(0)]*7
        row[off:off+5]=a
        syl.append(row)
    for off in range(4):
        row=[Q(0)]*7
        row[off:off+4]=d
        syl.append(row)
    return det_rational(syl)

def f_coeff(r):
    return [-r*r*(r+1),r*(r-1)*(r-1),3*r*r,3*r-1,Q(1)]

# Polynomial discriminant has degree at most 18 in r: quartic discriminant
# is homogeneous of degree six in its coefficients, each of degree <=3.
# Nineteen distinct exact evaluation points therefore certify identity.
for j in range(1,20):
    r=Q(j,13)
    assert quartic_discriminant(f_coeff(r)) == -4*r**3*evalp(P,r)

# Exact Descartes certificate on r in (0, 1/10):
# (1+t)^7 P(t/[10(1+t)]) has one coefficient sign change.
q=[sum(P[j]*Q(1,10)**j*comb(7-j,k-j)
       for j in range(k+1)) for k in range(8)]
assert [v>0 for v in reversed(q)] == [True,True,False,False,False,False,False,False]
assert evalp(P,Q(0))<0<evalp(P,Q(1,10))

# Bernstein positivity on [1/10, 1/5].
c=[sum(P[j]*comb(j,k)*Q(1,10)**j for j in range(k,8))
   for k in range(8)]
bern=[sum(c[j]*Q(comb(k,j),comb(7,j)) for j in range(k+1))
      for k in range(8)]
assert all(v>0 for v in bern)
assert bern[0]==Q(441377,10000000)

# For r=1/5+t, every coefficient of P is strictly positive.
shift=[sum(P[j]*comb(j,k)*Q(1,5)**(j-k) for j in range(k,8))
       for k in range(8)]
assert all(v>0 for v in shift)

# A triple root of F would cause its derivative cubic to have a multiple root;
# its discriminant is -108*r*T(r).  The two relevant factors are coprime.
a,b=P,T
while b != [0]:
    _,rem=divmodp(a,b)
    a,b=b,rem
assert len(a)==1 and a[0]!=0

# One side has three positive roots; the other has only one.
r=Q(1,100)
assert evalp(f_coeff(r),Q(0))<0
assert evalp(f_coeff(r),Q(1,50))>0
assert evalp(f_coeff(r),Q(1,5))<0
assert evalp(f_coeff(r),Q(1))>0
assert f_coeff(Q(1))==[Q(-2),Q(0),Q(3),Q(2),Q(1)]

# Independent stationary-probability and reflection checks on rational grids.
checks=0
for a in [Q(1,3),Q(1),Q(7,2)]:
    for b in [Q(1,7),Q(2,3),Q(4)]:
        for rate in [Q(1,10),Q(1,2),Q(3),Q(8)]:
            p1=rate/(a+rate)
            p2=a*rate/((a+rate)*(b+rate))
            p3=a*b/((a+rate)*(b+rate))
            assert p1+p2+p3==1
            assert a*p1==(b+rate)*p2 and b*p2==rate*p3
            x=rate/a; r=b/a
            D=1-p1*p1-p2*p2-p3*p3
            Dformula=2*x*((x+r)**2+r)/((x+r)**2*(x+1)**2)
            assert D==Dformula
            def diversity(t):
                return 2*t*((t+r)**2+r)/((t+r)**2*(t+1)**2)
            assert diversity(r/x)-diversity(x)==2*r*x*(x*x-r)/((r+x)**2*(x+1)**2)
            checks+=1

# Rational bisection isolates the unique positive root of P.
lo=Q(0);hi=Q(1,10)
for _ in range(100):
    m=(lo+hi)/2
    if evalp(P,m)<0: lo=m
    else: hi=m
assert hi-lo<Q(1,10)**20
print('VERIFY_OK discriminant_points=19 bernstein_coefficients=8 '
      'descartes_sign_change=1 gcd_certificate=1 '
      'stationary_and_reflection_cases=%d root_bracket=[%.14f,%.14f]'%(
       checks,float(lo),float(hi)))
