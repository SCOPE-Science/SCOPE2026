#!/usr/bin/env python3
"""Exact finite-field and first-order Grassmann-chart checks for a characteristic-five cubic."""
from itertools import permutations, product
P=5

def inv(x): return pow(x%P,-1,P)

def normalize(v):
    j=next(i for i,x in enumerate(v) if x%P)
    return tuple((x*inv(v[j]))%P for x in v)

def proj(n):
    for i in range(n):
        for tail in product(range(P),repeat=n-i-1):
            yield (0,)*i+(1,)+tail

def Q(a,b,c):return (a*a+b*b+c*c+(a+b+c)**2)%P

def H(a,b,c):return ((a+b)*(b+c)*(c+a))%P
B={v for v in proj(3) if Q(*v)==H(*v)==0}
C={v for v in proj(3) if Q(*v)==0}
assert len(B)==len(C)==6 and B==C
assert sorted(B)==[(1,2,3),(1,2,4),(1,3,2),(1,3,4),(1,4,2),(1,4,3)], sorted(B)
assert all((3*(a*a+b*b+c*c+(a+b+c)**2)-3*(a+b)*(b+c)*(c+a))%P==0 for a,b,c in B)

def f4(v):return (sum(t**3 for t in v)-sum(v)**3)%P

def plucker(V,W):
    vals=tuple((V[i]*W[j]-V[j]*W[i])%P for i in range(5) for j in range(i+1,5))
    return normalize(vals)

P5=(1,1,1,1,1)
ordinary=set();nodal=set()
for i in range(5):
    rem=[j for j in range(5) if j!=i]
    for j,k in [(rem[0],rem[1]),(rem[0],rem[2]),(rem[0],rem[3])]:
        l,m=sorted(set(rem)-{j,k})
        V=tuple((int(z==j)-int(z==k))%P for z in range(5))
        W=tuple((int(z==l)-int(z==m))%P for z in range(5))
        ordinary.add(plucker(V,W))
        assert all(f4(tuple((t*V[z]+u*W[z])%P for z in range(4)))==0 for t,u in product(range(P),repeat=2))
for a,b,c in B:
    D=(0,a,b,c,(-a-b-c)%P)
    nodal.add(plucker(P5,D))
    assert all(f4(tuple((t*P5[z]+u*D[z])%P for z in range(4)))==0 for t,u in product(range(P),repeat=2))
assert len(ordinary)==15 and len(nodal)==6 and not (ordinary&nodal)
assert {plucker(tuple(P5[i] for i in perm),tuple((0,1,4,2,3)[i] for i in perm)) for perm in permutations(range(5))}==nodal
print('SIX_RATIONAL_BASE_POINTS_AND_21_LINES_OK')

def det_nonzero(M):
    A=[[a%P for a in r] for r in M];r=0
    for j in range(len(A[0])):
        h=next((i for i in range(r,len(A)) if A[i][j]),None)
        if h is None:continue
        A[h],A[r]=A[r],A[h];q=inv(A[r][j]);A[r]=[(z*q)%P for z in A[r]]
        for i in range(len(A)):
            if i!=r:
                q=A[i][j];A[i]=[(A[i][t]-q*A[r][t])%P for t in range(len(A[0]))]
        r+=1
        if r==len(A):break
    return r

def chart(V,W):
    eye=[tuple(int(z==i) for z in range(4)) for i in range(4)]
    ii,jj=next((i,j) for i in range(4) for j in range(i+1,4)
               if det_nonzero([[V[z],W[z],eye[i][z],eye[j][z]] for z in range(4)])==4)
    SP=sum(V)%P;SW=sum(W)%P
    def grad(z):return [(3*(V[z]*V[z]-SP*SP))%P,(6*(V[z]*W[z]-SP*SW))%P,(3*(W[z]*W[z]-SW*SW))%P]
    a,b=grad(ii),grad(jj)
    columns=[[a[0],a[1],a[2],0],[0,a[0],a[1],a[2]],
             [b[0],b[1],b[2],0],[0,b[0],b[1],b[2]]]
    J=[[columns[j][i] for j in range(4)] for i in range(4)]
    return ii,jj,J

node4=(1,1,1,1);nodeD=(0,1,4,2)
ord4=(0,1,4,0);ordD=(0,0,0,1)
ri,rj,JN=chart(node4,nodeD);oi,oj,JO=chart(ord4,ordD)
assert det_nonzero(JN)==3 and det_nonzero(JO)==4
# Enumerate all kernel vectors to find the nonzero quadratic coefficient on its line.
ker=[vec for vec in product(range(5),repeat=4) if vec!=(0,)*4 and all(sum(JN[i][j]*vec[j] for j in range(4))%5==0 for i in range(4))]
assert len(ker)==4
for v in ker:
    w=[0]*4;w[ri]=v[0];w[rj]=v[2]
    quad=3*(sum(node4[i]*w[i]*w[i] for i in range(4))-sum(node4)*sum(w)**2)%5
    assert quad!=0
print('FANO_SCHEME_CHARTS_OK: ordinary rank4; nodal rank3, quadratic obstruction nonzero')

def make_gf(q):
    if q==5:
        els=list(range(5))
        add=lambda a,b:(a+b)%5
        neg=lambda a:(-a)%5
        mul=lambda a,b:(a*b)%5
        one=1;zero=0
    else:
        # GF(25)=F5[z]/(z^2-2), 2 a nonsquare in F5
        els=[(a,b) for a in range(5) for b in range(5)]
        add=lambda x,y:((x[0]+y[0])%5,(x[1]+y[1])%5)
        neg=lambda x:((-x[0])%5,(-x[1])%5)
        mul=lambda x,y:((x[0]*y[0]+2*x[1]*y[1])%5,(x[0]*y[1]+x[1]*y[0])%5)
        one=(1,0);zero=(0,0)
    return els,add,neg,mul,one,zero
for q in (5,25):
    els,add,neg,mul,one,zero=make_gf(q)
    cubes={x:mul(mul(x,x),x) for x in els}
    count=0
    for i in range(4):
        for tail in product(els,repeat=3-i):
            v=(zero,)*i+(one,)+tail
            S=zero;fs=zero
            for z in v:S=add(S,z);fs=add(fs,cubes[z])
            fs=add(fs,neg(cubes[S]))
            if fs==zero:count+=1
    assert count==q*q+6*q+1,(q,count)
    print('CLEBSCH_POINT_COUNT_GF(%s)=%s'%(q,count))
print('VERIFY_OK')
