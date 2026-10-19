"""Exact prime-field enumeration and conjugacy checks for canonical Heisenberg Lie-affgebra Rota--Baxter operators."""
from itertools import product
from collections import Counter


def bracket(u,v,q):
    return (0,0,(u[0]*v[1]-u[1]*v[0])%q)


def add(u,v,q):
    return tuple((a+b)%q for a,b in zip(u,v))


def sub(u,v,q):
    return tuple((a-b)%q for a,b in zip(u,v))


def scale(s,v,q):
    return tuple(s*x%q for x in v)


def mv(g,v,q):
    return tuple(sum(g[3*i+j]*v[j] for j in range(3))%q for i in range(3))


def mm(a,b,q):
    return tuple(sum(a[3*i+k]*b[3*k+j] for k in range(3))%q for i in range(3) for j in range(3))


def rank(m,q):
    A=[list(m[3*i:3*i+3]) for i in range(3)]
    r=0
    for j in range(3):
        idx=next((i for i in range(r,3) if A[i][j]%q),None)
        if idx is None:continue
        A[idx],A[r]=A[r],A[idx]
        fac=pow(A[r][j],-1,q)
        A[r]=[(x*fac)%q for x in A[r]]
        for i in range(r+1,3):
            fac=A[i][j]
            A[i]=[(x-fac*y)%q for x,y in zip(A[i],A[r])]
        r+=1
    return r


def inverse(g,q):
    A=[list(g[3*i:3*i+3])+[int(i==j) for j in range(3)] for i in range(3)]
    for col in range(3):
        pivot=next((i for i in range(col,3) if A[i][col]),None)
        assert pivot is not None
        A[col],A[pivot]=A[pivot],A[col]
        inv=pow(A[col][col],-1,q)
        A[col]=[x*inv%q for x in A[col]]
        for i in range(3):
            if i!=col:
                v=A[i][col]
                A[i]=[(x-v*y)%q for x,y in zip(A[i],A[col])]
    return tuple(A[i][j+3] for i in range(3) for j in range(3))


def operators(q):
    E=[(1,0,0),(0,1,0),(0,0,1)]
    I=(1,0,0,0,1,0,0,0,1)
    elems=list(product(range(q),repeat=3))
    out=set()
    for r in product(range(q),repeat=9):
        if mm(r,r,q)!=r:continue
        re=[mv(r,e,q) for e in E]
        if any(bracket(re[i],re[j],q)!=mv(r,sub(add(bracket(re[i],E[j],q),bracket(E[i],re[j],q),q),bracket(E[i],E[j],q),q),q)
               for i in range(3) for j in range(i+1,3)):
            continue
        for p in elems:
            if mv(r,p,q)!=(0,0,0):continue
            if any(mv(r,bracket(p,e,q),q)!=bracket(p,re[i],q) for i,e in enumerate(E)):continue
            out.add((r,p))
    counts=Counter(rank(r,q) for r,p in out)
    expected={0:q**3,1:q**3*(q+1),2:q**3*(q+1),3:1}
    assert counts==expected,(q,counts,expected)
    # Verify original affine Rota--Baxter identity by direct evaluation on every pair.
    for r,p in out:
        for x in elems:
            px=add(mv(r,x,q),p,q)
            for y in elems:
                py=add(mv(r,y,q),p,q)
                desc=add(sub(add(bracket(px,y,q),y,q),add(bracket(x,y,q),y,q),q),add(bracket(x,py,q),py,q),q)
                assert add(mv(r,desc,q),p,q)==add(bracket(px,py,q),py,q)
    # Enumerate full affine automorphism group, including central translations.
    autos=[]
    for a,b,c,d in product(range(q),repeat=4):
        determinant=(a*d-b*c)%q
        if determinant==0:continue
        for u,v,t in product(range(q),repeat=3):
            g=(a,b,0,c,d,0,u,v,determinant)
            autos.append((g,inverse(g,q),(0,0,t)))
    reps=[((0,0,0,0,0,0,0,0,0),(0,0,0)),
          ((0,0,0,0,0,0,0,0,0),(1,0,0)),
          ((1,0,0,0,0,0,0,0,0),(0,0,0)),
          ((1,0,0,0,0,0,0,0,1),(0,0,0)),
          ((1,0,0,0,0,0,0,0,1),(0,1,0)),
          (I,(0,0,0))]
    orbits=[]
    for r,p in reps:
        orbit=set()
        for g,ginv,t in autos:
            rr=mm(mm(g,r,q),ginv,q)
            pp=add(mv(g,p,q),sub(t,mv(rr,t,q),q),q)
            orbit.add((rr,pp))
        assert orbit<=out,(q,r,p,'bad conjugate')
        orbits.append(orbit)
    assert sum(len(o) for o in orbits)==len(out)
    assert set.union(*orbits)==out
    assert all(not(orbits[i]&orbits[j]) for i in range(6) for j in range(i+1,6))
    sizes=[len(o) for o in orbits]
    exp=[q,q**3-q,q**3*(q+1),q**2*(q+1),(q-1)*q**2*(q+1),1]
    assert sizes==exp,(q,sizes,exp)
    assert len(autos)==(q*q-1)*(q*q-q)*q**3
    print(f'q={q} operators={len(out)} ranks={dict(sorted(counts.items()))} 6 affine orbits={sizes} automorphisms={len(autos)}')


if __name__=='__main__':
    for q in (2,3):operators(q)
    print('VERIFY_OK: complete prime-field affine-map scan, direct RB identities and full affine conjugacy orbits')
