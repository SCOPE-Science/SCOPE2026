"""Exact finite checks for idempotent Alexander-quandle self-maps.
Uses only standard-library enumeration of matrices over prime fields.
"""
from itertools import product
from fractions import Fraction
from collections import Counter


def rank(A,p):
    a=[list(r) for r in A]; m=len(a); n=len(a[0]) if m else 0
    i=0
    for j in range(n):
        k=next((k for k in range(i,m) if a[k][j]%p),None)
        if k is None: continue
        a[i],a[k]=a[k],a[i]
        z=pow(a[i][j],-1,p)
        a[i]=[(t*z)%p for t in a[i]]
        for k in range(i+1,m):
            if a[k][j]%p:
                z=a[k][j]
                a[k]=[(x-z*y)%p for x,y in zip(a[k],a[i])]
        i+=1
        if i==m: break
    return i


def matrixprod(A,B,p):
    return [[sum(x*y for x,y in zip(row,col))%p for col in zip(*B)] for row in A]


def pred_A(p, degrees_parts):
    ans=Fraction(1)
    for d,m in degrees_parts.items():
        Q=p**d
        longest=max(m,default=0)
        exponent=sum(sum(v for e,v in m.items() if e>=j)**2 for j in range(1,longest+1))
        z=Fraction(Q**exponent)
        for _,multiplicity in m.items():
            for j in range(1,multiplicity+1):
                z*=Fraction(Q**j-1,Q**j)
        ans*=z
    assert ans.denominator==1
    return ans.numerator


def predicted(p, fparts):
    # input: f label => (irreducible degree, length multiplicity dictionary)
    Fs=list(fparts)
    choices=[list(product(*(range(m+1) for _,m in sorted(fparts[f][1].items())))) for f in Fs]
    data={}; n=sum(deg*sum(e*m for e,m in ds.items()) for deg,ds in fparts.values())
    def Af(choice):
        ans=1
        for f,(deg,ds) in fparts.items():
            ms={e:choice[f].get(e,0) for e in ds}
            ans*=pred_A(p,{deg:ms})
        return ans
    base=Af({f:dict(ds) for f,(_,ds) in fparts.items()})
    for tuple_choices in product(*choices):
        U={f:dict(zip(sorted(fparts[f][1]), vals)) for f,vals in zip(Fs,tuple_choices)}
        W={f:{e:m-U[f][e] for e,m in ds.items()} for f,(deg,ds) in fparts.items()}
        du=sum(fparts[f][0]*sum(e*v for e,v in U[f].items()) for f in Fs)
        dw=n-du
        x=Fraction(base,pred_A_comb(p,fparts,U)*pred_A_comb(p,fparts,W))*p**dw
        assert x.denominator==1,(x,U)
        data[du]=data.get(du,0)+x.numerator
    return data


def pred_A_comb(p,fparts,X):
    v=1
    for f,(deg,ds) in fparts.items():
        v*=pred_A(p,{deg:X[f]})
    return v


def brute(p,T):
    n=len(T)
    assert rank(T,p)==n
    sub=[[((1 if i==j else 0)-T[i][j])%p for j in range(n)] for i in range(n)]
    assert rank(sub,p)==n
    cnt=Counter(); count_central=0
    for a in product(range(p),repeat=n*n):
        A=[list(a[i*n:(i+1)*n]) for i in range(n)]
        if matrixprod(A,T,p)!=matrixprod(T,A,p): continue
        if matrixprod(A,A,p)!=A: continue
        count_central+=1
        r=rank(A,p)
        cnt[r]+=p**(n-r)
    return dict(cnt),count_central


def J(p,sizes,ev=2):
    n=sum(sizes); T=[[0]*n for _ in range(n)]; a=0
    for e in sizes:
        for i in range(e):
            T[a+i][a+i]=ev%p
            if i+1<e: T[a+i][a+i+1]=1
        a+=e
    return T


def brute_image_fibers(p,T):
    # Independently group maps by their exact image as a set of points.
    n=len(T); points=list(product(range(p),repeat=n)); fibers=Counter()
    for a0 in product(range(p),repeat=n*n):
        A=[list(a0[i*n:(i+1)*n]) for i in range(n)]
        if matrixprod(A,T,p)!=matrixprod(T,A,p): continue
        if matrixprod(A,A,p)!=A: continue
        for a in points:
            if any(sum(A[i][j]*a[j] for j in range(n))%p for i in range(n)): continue
            image=tuple(sorted(set(tuple((a[i]+sum(A[i][j]*x[j] for j in range(n)))%p for i in range(n)) for x in points)))
            fibers[image]+=1
    return fibers


def verify_all():
    cases=[
      ('scalar-3-2',3,J(3,[1,1]), {'t+1':(1,{1:2})}),
      ('Jordan-3-2',3,J(3,[2]), {'t+1':(1,{2:1})}),
      ('mixed-3-3',3,J(3,[2,1]), {'t+1':(1,{2:1,1:1})}),
      ('scalar-3-3',3,J(3,[1,1,1]), {'t+1':(1,{1:3})}),
      ('split-5-2',5,[[2,0],[0,3]], {'t-2':(1,{1:1}),'t-3':(1,{1:1})}),
      ('scalar-5-2',5,J(5,[1,1]), {'t-2':(1,{1:2})}),
      ('irreducible-2-2',2,[[0,1],[1,1]], {'t2+t+1':(2,{1:1})}),
      ('irreducible-double-2-4',2,[[0,1,0,0],[1,1,0,0],[0,0,0,1],[0,0,1,1]], {'t2+t+1':(2,{1:2})}),
      ('irreducible-thick-2-4',2,[[0,0,0,1],[1,0,0,0],[0,1,0,1],[0,0,1,0]], {'t2+t+1':(2,{2:1})}),
    ]
    for name,p,T,parts in cases:
        a,c=brute(p,T)
        b=predicted(p,parts)
        print(name,'observed',a,'predicted',b,'linear_projections',c)
        assert a==b,(name,a,b)
    for name,p,T,parts,expect in [
      (cases[0][0],cases[0][1],cases[0][2],cases[0][3],{1:1,3:3,9:1}),
      (cases[1][0],cases[1][1],cases[1][2],cases[1][3],{1:1,9:1}),
      (cases[2][0],cases[2][1],cases[2][2],cases[2][3],{1:1,3:3,9:3,27:1}),
    ]:
        fibers=brute_image_fibers(p,T)
        for image,nr in fibers.items():
            assert nr==expect[len(image)],(name,len(image),nr)
        assert sum(fibers.values())==sum(predicted(p,parts).values())
        print('image_fibers',name,len(fibers),'distinct images',len(fibers))
    # Exhaustively check the un-enriched quandle homomorphism definition
    # over the 3-element kei and the connected four-element quandle.
    for name,p,T,parts in [('scalar-3-1',3,[[2]],{'t+1':(1,{1:1})}),cases[6]]:
        n=len(T); X=list(product(range(p),repeat=n)); m=len(X)
        index={v:i for i,v in enumerate(X)}
        star=[[index[tuple((sum(T[i][j]*x[j]+((1 if i==j else 0)-T[i][j])*y[j] for j in range(n)))%p for i in range(n))] for y in X] for x in X]
        count=0
        for ff in product(range(m),repeat=m):
            if not all(ff[star[x][y]]==star[ff[x]][ff[y]] for x in range(m) for y in range(m)):continue
            if all(ff[ff[x]]==ff[x] for x in range(m)):count+=1
        expect=sum(predicted(p,parts).values())
        print('full_quandle_map',name,count,expect)
        assert count==expect
    print('ALL_EXACT_CHECKS_PASSED',len(cases),'linear cases + 3 image-fiber cases + 2 full quandle cases')

if __name__=='__main__':verify_all()
