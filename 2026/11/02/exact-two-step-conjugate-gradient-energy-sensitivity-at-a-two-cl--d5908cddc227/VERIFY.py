#!/usr/bin/env python3
"""Exact-rational checks for the two-cluster two-step CG perturbation formula.

No third-party dependencies. Checks the derivative of the CG normal equations,
the residual polynomial, and the closed-form energy coefficient. Numerical
sampling is corroboration, not a substitute for the analytical proof.
"""
from fractions import Fraction as Q
from random import Random


def dot(x, y):
    return sum((a*b for a,b in zip(x,y)), Q(0))


def mv(A, x):
    return [dot(row,x) for row in A]


def add(x, y):
    return [a+b for a,b in zip(x,y)]


def scale(a, x):
    return [a*v for v in x]


def solve2(a,b,c,d,e,f):
    det = a*d-b*c
    assert det != 0
    return [(e*d-b*f)/det, (a*f-c*e)/det]


def moments_at_zero(lam, d, F):
    # Derivative of d^T C(t)^k d at C(0)=diag(lam), C'(0)=F.
    m = [sum((d[i]*d[i]*lam[i]**k for i in range(len(d))),Q(0))
         for k in range(4)]
    md = [Q(0)]
    for k in range(1,4):
        derivative = Q(0)
        for s in range(k):
            derivative += sum((d[i]*d[j]*lam[i]**s * F[i][j] *
                    lam[j]**(k-1-s) for i in range(len(d))
                    for j in range(len(d))),Q(0))
        md.append(derivative)
    return m,md


def linearized_coefficient(beta,gamma,m,n,d,F):
    lam=[beta]*m+[gamma]*n
    assert beta>gamma>0 and dot(d[:m],d[:m])>0 and dot(d[m:],d[m:])>0
    mom,md=moments_at_zero(lam,d,F)
    c10,c20=solve2(mom[1],mom[2],mom[2],mom[3],-mom[0],-mom[1])
    assert c10==-(beta+gamma)/(beta*gamma) and c20==1/(beta*gamma)
    c11,c21=solve2(mom[1],mom[2],mom[2],mom[3],
            -(c10*md[1]+c20*md[2]),
            -(md[1]+c10*md[2]+c20*md[3]))
    Cd=[lam[i]*d[i] for i in range(m+n)]
    CCd=[lam[i]*Cd[i] for i in range(m+n)]
    Fd=mv(F,d)
    FCCd=[lam[i]*Fd[i] for i in range(m+n)]
    FCd=mv(F,Cd)
    r1=add(add(scale(c11,Cd),scale(c21,CCd)),
           add(scale(c10,Fd),scale(c20,add(FCCd,FCd))))
    r_pred=[Q(0)]*(m+n)
    for start,end,L in ((0,m,beta),(m,m+n,gamma)):
        v=d[start:end]
        Mv=[sum((F[i][j]*d[j] for j in range(start,end)),Q(0))
            for i in range(start,end)]
        mean=dot(v,Mv)/dot(v,v)
        slope=(L-(gamma if L==beta else beta))/(beta*gamma)
        for k,i in enumerate(range(start,end)):
            r_pred[i]=slope*(Mv[k]-mean*v[k])
    assert r1==r_pred,(r1,r_pred)
    energy=sum((r1[i]*r1[i]/lam[i] for i in range(m+n)),Q(0))
    def orthmass(v,M):
        Mv=mv(M,v)
        return dot(Mv,Mv)-dot(v,Mv)**2/dot(v,v)
    B1=[row[:m] for row in F[:m]]
    B2=[row[m:] for row in F[m:]]
    cf=(beta-gamma)**2 * (
          orthmass(d[:m],B1)/(beta**3*gamma**2)
         +orthmass(d[m:],B2)/(beta**2*gamma**3))
    assert energy==cf and cf>=0,(energy,cf)
    return cf


def two_step_energy(lam,F,d,t):
    N=len(d)
    C=[[ (lam[i] if i==j else Q(0))+t*F[i][j] for j in range(N)] for i in range(N)]
    C2=mv(C,mv(C,d))
    Cd=mv(C,d)
    moms=[dot(d,d),dot(d,Cd),dot(d,C2),dot(Cd,C2)]
    c1,c2=solve2(moms[1],moms[2],moms[2],moms[3],-moms[0],-moms[1])
    r=add(add(d,scale(c1,Cd)),scale(c2,C2))
    # Solve C y = r using Gauss-Jordan elimination, all rational.
    A=[C[i][:]+[r[i]] for i in range(N)]
    for j in range(N):
        p=next(i for i in range(j,N) if A[i][j])
        A[p],A[j]=A[j],A[p]
        fac=A[j][j]
        A[j]=[x/fac for x in A[j]]
        for i in range(N):
            if i==j:continue
            fac=A[i][j]
            A[i]=[a-fac*b for a,b in zip(A[i],A[j])]
    return dot(r,[A[i][-1] for i in range(N)])


def main():
    count=0
    rng=Random(192837)
    for m,n in [(1,1),(2,1),(1,2),(2,2),(3,2),(2,3),(3,3)]:
        for k in range(80):
            gamma=Q(rng.randint(1,5),rng.randint(1,4))
            beta=gamma+Q(rng.randint(1,6),rng.randint(1,4))
            N=m+n
            d=[Q(rng.randint(-3,3),rng.randint(1,5)) for _ in range(N)]
            if not any(d[:m]):d[0]=Q(1)
            if not any(d[m:]):d[m]=Q(1)
            F=[[Q(0) for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(i,N):
                    F[i][j]=F[j][i]=Q(rng.randint(-4,4),rng.randint(1,5))
            linearized_coefficient(beta,gamma,m,n,d,F)
            count+=1
    beta,gamma=Q(4),Q(1)
    d=[Q(1),Q(1),Q(1)]
    F=[[Q(1,4),Q(0),Q(0)],[Q(0),Q(0),Q(0)],[Q(0),Q(0),Q(0)]]
    coeff=linearized_coefficient(beta,gamma,2,1,d,F)
    assert coeff==Q(9,2048)
    print('Example 1 exact leading coefficient:',coeff)
    discrepancies=[]
    for denom in (100,1000,10000):
        val=two_step_energy([beta,beta,gamma],F,d,Q(1,denom))/Q(1,denom)**2
        print('t=1/%d: error/t^2=%.13f'%(denom,float(val)))
        discrepancies.append(abs(float(val)-float(coeff)))
    assert discrepancies[0]>discrepancies[1]>discrepancies[2]
    assert discrepancies[2]<5e-9
    # Sharp Frobenius robustness. Off-diagonal symmetric entries have norm^2=2;
    # after unit-Frobenius normalization, the coefficient divides by two.
    Fsharp=[[Q(0),Q(1),Q(0)],
            [Q(1),Q(0),Q(0)],
            [Q(0),Q(0),Q(0)]]
    assert linearized_coefficient(beta,gamma,2,1,[Q(1),Q(0),Q(1)],Fsharp)/2==Q(9,128)
    Fsharp2=[[Q(0),Q(0),Q(0)],
             [Q(0),Q(0),Q(1)],
             [Q(0),Q(1),Q(0)]]
    assert linearized_coefficient(beta,gamma,1,2,[Q(1),Q(1),Q(0)],Fsharp2)/2==Q(9,32)
    print('Sharp Frobenius constants: 9/128 and 9/32 (two cluster choices)')
    # Pure cross-block coupling has vanishing first-order residual.
    F=[[Q(0),Q(0),Q(1,4)],[Q(0),Q(0),Q(0)],[Q(1,4),Q(0),Q(0)]]
    assert linearized_coefficient(beta,gamma,2,1,d,F)==0
    for denom in (100,1000,10000):
        t=Q(1,denom)
        ratio=two_step_energy([beta,beta,gamma],F,d,t)/(t**4)
        print('cross-block t=1/%d: error/t^4=%.13f'%(denom,float(ratio)))
        assert ratio >= 0 and float(ratio)<1
    print('PASS:',count,'random exact-rational block perturbation identities; two explicit families')


if __name__=='__main__':
    main()
