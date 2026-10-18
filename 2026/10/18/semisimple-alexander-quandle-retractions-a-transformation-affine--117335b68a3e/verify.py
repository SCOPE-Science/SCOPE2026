"""Independent finite quandle-operation enumeration for rank-refined retractions.
No external packages. Python 3.11+."""
from collections import Counter
from itertools import product
from math import comb

def qbin(n,k,q):
    if k<0 or k>n:return 0
    a=1;b=1
    for i in range(k):
        a*=q**(n-i)-1;b*=q**(i+1)-1
    assert a%b==0
    return a//b

def formula(p,s,factors):
    # factors: [(degree,multiplicity)] distinct, semisimple nonunit eigen factors
    N=p**s
    curr=Counter()
    for k in range(1,N+1):
        cur=Counter({1:comb(N,k)*k**(N-k)})
        for e,d in factors:
            q=p**e
            ext=Counter()
            for z,c in cur.items():
                for r in range(d+1):
                    ext[z*p**(e*r)]+=c*qbin(d,r,q)*q**((r+1)*(d-r))
            cur=ext
        curr+=Counter({k*z:c for z,c in cur.items()})
    return curr

def table_prime(p,s,w,T):
    # W dimension w, T is w-by-w matrix over Fp, U dimension s.
    U=list(product(range(p),repeat=s)); W=list(product(range(p),repeat=w));
    pts=list(product(U,W)); indices={a:i for i,a in enumerate(pts)}
    N=len(pts)
    table=[]
    for u,v in pts:
        row=[]
        for up,vp in pts:
            z=tuple((sum(T[i][j]*v[j] for j in range(w))+vp[i]-sum(T[i][j]*vp[j] for j in range(w)))%p for i in range(w))
            row.append(indices[u,z])
        table.append(row)
    return table

def scan_all(n,star):
    # Generate all quandle endomorphisms by constraint propagation rather than post-selecting normal forms.
    count=0
    idempotent=Counter()
    hist=Counter()
    by_image=Counter()
    def rec(state):
        nonlocal count
        state=list(state)
        while True:
            changed=False
            assigned=[i for i in range(n) if state[i]!=-1]
            for x in assigned:
                a=state[x]
                for y in assigned:
                    b=state[y]
                    z=star[x][y]
                    v=star[a][b]
                    if state[z]==-1:
                        state[z]=v
                        changed=True
                    elif state[z]!=v:
                        return
            if not changed:break
        if -1 not in state:
            count+=1
            image=tuple(sorted(set(state)))
            rank=len(image);hist[rank]+=1
            if all(state[state[i]]==state[i] for i in range(n)):
                idempotent[rank]+=1
                by_image[image]+=1
            return
        # Most-constraining unassigned variable first.
        assigned=[i for i in range(n) if state[i]!=-1]
        free=[i for i in range(n) if state[i]==-1]
        if assigned:
            idx=max(free,key=lambda z:sum((star[z][i] not in assigned)+(star[i][z] not in assigned) for i in assigned))
        else:idx=0
        for val in range(n):
            nextstate=state[:]
            nextstate[idx]=val
            rec(nextstate)
    rec([-1]*n)
    return count,idempotent,hist,by_image

def check(label,p,s,T,factors):
    w=len(T)
    table=table_prime(p,s,w,T)
    count,idem,hist,by_image=scan_all(len(table),table)
    want=formula(p,s,factors)
    assert idem==want,(label,idem,want)
    expected_images=Counter()
    for k in range(1,p**s+1):
        for ranks in product(*(range(d+1) for e,d in factors)):
            image_count=comb(p**s,k)
            multiplicity=k**(p**s-k)
            for (e,d),r in zip(factors,ranks):
                q=p**e
                image_count*=qbin(d,r,q)*q**(d-r)
                multiplicity*=q**(r*(d-r))
            expected_images[multiplicity]+=image_count
    assert Counter(by_image.values())==expected_images,(label,'image fibers')
    print(label,'elements',len(table),'all_homomorphisms',count,'rank_hist',dict(sorted(hist.items())),'retractions',dict(sorted(idem.items())),'image_multiplicity',dict(sorted(Counter(by_image.values()).items())))
    return count

def main():
    assert check('p3-singleton',3,0,[],[])==1
    assert check('p2-all-fixed-dimension2',2,2,[],[])==4**4
    assert check('p3-s0-eigen2',3,0,[[2]],[(1,1)])==3**2
    assert check('p5-s0-eigen2',5,0,[[2]],[(1,1)])==5**2
    assert check('p3-s1-eigen2',3,1,[[2]],[(1,1)])==3**3*3**2
    assert check('p3-s0-eigen2-multiplicity2',3,0,[[2,0],[0,2]],[(1,2)])==3**6
    assert check('p2-s1-irreducible-quadratic',2,1,[[0,1],[1,1]],[(2,1)])==2**2*4**2
    print('ALL_EXACT_CHECKS_PASSED')
if __name__=='__main__':main()
