#!/usr/bin/env python3
"""Reproduce finite checks for an exact CountSketch rank and conditioning theorem."""
import itertools, math

SQ3=math.sqrt(3)
BASE=((1.0,0.0),(-0.5,SQ3/2),(-0.5,-SQ3/2))

def det(u,v):return u[0]*v[1]-u[1]*v[0]
def mat(e):return [BASE[0],BASE[1],(BASE[2][0]+e,BASE[2][1]+e)]
def gram2(rows):
    a=sum(x*x for x,y in rows);b=sum(x*y for x,y in rows);c=sum(y*y for x,y in rows)
    return a,b,c

def cond2(rows):
    a,b,c=gram2(rows); tr=a+c; d=a*c-b*b
    if d<=1e-14:return float('inf')
    big=(tr+math.sqrt(max(0.,(a-c)**2+4*b*b)))/2
    return big/math.sqrt(d)

def right_precond_cond(A,sketch):
    a,b,c=gram2(sketch)
    if a*c-b*b<=0:return float('inf')
    r11=math.sqrt(a);r12=b/r11;r22=math.sqrt(max(0.,c-r12*r12))
    if r22<=0:return float('inf')
    # R^{-1}=[(1/r11,-r12/(r11*r22)),(0,1/r22)]
    inv=((1/r11,-r12/(r11*r22)),(0.,1/r22))
    B=[(x*inv[0][0]+y*inv[1][0],x*inv[0][1]+y*inv[1][1]) for x,y in A]
    return cond2(B)

def enumerate_case(s,e):
    A=mat(e);sing=0;valid=[];bad_classes=[]
    for h in itertools.product(range(s),repeat=3):
      for sign in itertools.product((-1,1),repeat=3):
        sk=[[0.,0.] for _ in range(s)]
        for i in range(3):
            for j in range(2):sk[h[i]][j]+=sign[i]*A[i][j]
        sk=[tuple(x) for x in sk]
        z=cond2(sk)
        # determinant by minors avoids near-zero normal-equation cancellation
        area2=sum(det(sk[i],sk[j])**2 for i in range(s) for j in range(i+1,s))
        rank2=area2>1e-20
        if not rank2:sing+=1
        else:valid.append(z)
    return sing/(8*s**3),sum(valid)/len(valid)

def check():
    tests=0
    assert abs(sum(det((1.,1.),r)**(-1) for r in BASE))>0;tests+=1
    assert all(abs(sum(BASE[i][j] for i in range(3)))<1e-14 for j in range(2));tests+=1
    a,b,c=gram2(BASE)
    assert abs(a-1.5)<1e-14 and abs(c-1.5)<1e-14 and abs(b)<1e-14;tests+=1
    for s in (2,3,6):
        p0,k0=enumerate_case(s,0.)
        assert abs(p0-(3*s-1)/(2*s*s))<1e-12;tests+=1
        want=(1+2*SQ3)/(s+1)
        for e in (0.01,0.001):
            p,k=enumerate_case(s,e)
            assert abs(p-1/(s*s))<1e-12;tests+=1
            assert abs(e*k-want)<0.01;tests+=1
        print('buckets',s,'tight failure',p0,'perturbed failure',1/s**2,'scaled conditional limit',want)
    # Verify each same-sign pair has the predicted *exactly linear* cross product.
    for e in (0.01,0.2):
      A=mat(e)
      for k in range(3):
        i,j=[l for l in range(3) if l!=k]
        pair=(A[i][0]+A[j][0],A[i][1]+A[j][1])
        assert abs(det(pair,A[k])-e*det((1,1),BASE[k]))<1e-13;tests+=1
    A=mat(1e-4); sk=[(A[0][0]+A[1][0],A[0][1]+A[1][1]),A[2]]
    ratio=right_precond_cond(A,sk)/cond2(sk)
    assert abs(ratio-1)<0.001;tests+=1
    print('direct QR preconditioning ratio',ratio,'checks',tests)
if __name__=='__main__':check()
