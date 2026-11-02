#!/usr/bin/env python3
"""Direct finite-vector check of binary quadratic polar-graph orbit extensions.
Independent of the quadratic Fourier-count derivation: explicitly enumerate
all nonzero singular vectors and their four-round extension configurations."""
from verify_orthogonal_types import Model

def Q(z,r,eps):
    y=0
    for i in range(r):
        a=(z>>(2*i))&1
        b=(z>>(2*i+1))&1
        if eps==-1 and i==r-1:
            y^=a ^ b ^ (a&b)
        else:
            y^=a&b
    return y

def B(x,y,r,eps): return Q(x^y,r,eps)^Q(x,r,eps)^Q(y,r,eps)

def state_of(v,r,eps):
    basis=[];coords=[]
    for u in v:
        found=False
        for c in range(1<<len(basis)):
            t=0
            for i,b in enumerate(basis):
                if (c>>i)&1:t^=b
            if t==u:
                coords.append(c);found=True;break
        if not found:
            coords.append(1<<len(basis))
            basis.append(u)
    rows=tuple(sum(B(basis[i],basis[j],r,eps)<<j for j in range(len(basis))) for i in range(len(basis)))
    return (tuple(coords),rows),basis

def verify(r,eps):
    mo=Model(r,eps)
    verts=[z for z in range(1,1<<(2*r)) if not Q(z,r,eps)]
    length_expected=(1<<(2*r-1))+eps*(1<<(r-1))-1
    assert len(verts)==length_expected
    reprs={((),()):()}
    counts=[]
    for k in range(4):
        counts.append(len(reprs))
        nxt={}
        for state,tuple_vec in reprs.items():
            expected=set(mo.ext(state))
            found=set()
            abstract,basis=state_of(tuple_vec,r,eps)
            assert abstract==state,(r,eps,state,abstract)
            for t in range(1<<len(basis)):
                total_direct=sum(all(B(x,b,r,eps)==((t>>i)&1) for i,b in enumerate(basis)) for x in range(1<<(2*r)) if not Q(x,r,eps))
                rows=state[1]
                m=len(rows)
                gauss=sum(1 if ((a&t).bit_count()%2)^quad(a,rows)==0 else -1 for a in range(1<<m))
                total_formula=((1<<(2*r))+eps*(1<<r)*gauss)//(1<<(m+1))
                assert total_direct==total_formula,(r,eps,state,t,total_direct,total_formula)
            for x in verts:
                newtuple=tuple_vec+(x,)
                child,_=state_of(newtuple,r,eps)
                found.add(child)
                nxt.setdefault(child,newtuple)
            assert found==expected,(r,eps,k,state,len(found),len(expected),found^expected)
        reprs=nxt
    print('DIRECT_EXTENSIONS_OK',r,eps,'vertices',len(verts),'state_counts',counts,'last_states',len(reprs))

def quad(x,rows):
    v=0
    while x:
        i=(x&-x).bit_length()-1
        x&=x-1
        v ^= (rows[i]&x).bit_count()&1
    return v

if __name__=='__main__':
 for r in (2,3,4):
  for eps in (1,-1):
   verify(r,eps)
 print('DIRECT_VERIFY_OK')

def separators(r,eps):
    verts=[z for z in range(1,1<<(2*r)) if not Q(z,r,eps)]
    N={x:{y for y in verts if y!=x and B(x,y,r,eps)==0} for x in verts}
    edge=any(N.values())
    claw=False
    K4=False
    for a in verts:
        candidates=sorted(N[a]); size=len(candidates)
        for i in range(size):
            for j in range(i+1,size):
                x,y=candidates[i],candidates[j]
                if y in N[x]:
                    # a,x,y mutually adjacent: search a fourth clique vertex
                    if N[a] & N[x] & N[y]-{a,x,y}:
                        K4=True
                else:
                    # a,x,y forms an induced V; another nonadjacent neighbor gives claw
                    if any(z!=x and z!=y and z not in N[x] and z not in N[y] for z in candidates):
                        claw=True
                if claw and K4:break
            if claw and K4:break
        if claw and K4:break
    return edge,claw,K4

if __name__=='__main__':
 for r in (2,3,4):
  for eps in (1,-1):
   print('SEPARATORS',r,eps,separators(r,eps))
