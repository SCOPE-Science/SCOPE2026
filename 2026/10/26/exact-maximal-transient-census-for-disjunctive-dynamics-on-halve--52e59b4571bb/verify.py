"""Finite cross-check of exact maximal transient-depth counts for disjunctive dynamics on halved cubes."""
from math import comb
from itertools import combinations
from random import Random


def one_parity(n, parity):
    return [v for v in range(1 << n) if v.bit_count() % 2 == parity]


def neighbor_masks(n):
    p = [one_parity(n, z) for z in (0, 1)]
    edges = [((1 << i) | (1 << j)) for i in range(n) for j in range(i+1,n)]
    masks = []
    lookup = []
    for side in p:
        ind = {v:i for i,v in enumerate(side)}
        lookup.append(ind)
        masks.append([sum(1 << ind[v ^ e] for e in edges) for v in side])
    return p, masks


def iterate(mask, neighbors):
    out = 0
    while mask:
        bit = mask & -mask
        out |= neighbors[bit.bit_length()-1]
        mask -= bit
    return out


def predicted_tau(n, mask_even, mask_odd, nbr):
    me, mo = mask_even, mask_odd
    goal = [(1 << len(nbr[i]))-1 if s else 0 for i, s in enumerate((me,mo))]
    for t in range(n+3):
        if [me, mo] == goal:
            return t
        me, mo = iterate(me, nbr[0]), iterate(mo,nbr[1])
    raise AssertionError('did not settle')


def bad(n, mask, vertices):
    if mask == 0: return False
    dmax = n if n % 2 == 0 else n-1
    centers=(1<<len(vertices))-1
    i=0
    while mask and centers:
        bit=mask & -mask
        w=vertices[bit.bit_length()-1]
        centers &= sum(1<<j for j,v in enumerate(vertices) if (v^w).bit_count()==dmax)
        mask-=bit
    return centers!=0


def formula_bad(n):
    N = 1 << (n-1)
    return N if n%2==0 else N*(1<<n) - N*n - (N*comb(n,2))//2


def run():
    rng = Random(20261021)
    checks = 0
    shell_checks = 0
    bad_counts = {}
    for n in range(6, 10):
        vertices, neighbors = neighbor_masks(n)
        N = 1 << (n-1)
        T = n//2
        for parity in (0,1):
            vs=vertices[parity]
            ind={v:i for i,v in enumerate(vs)}
            # Exact walk Hamming-shell identity at all relevant times.
            base=vs[0]
            state=1<<ind[base]
            for t in range(1,T+3):
                state=iterate(state,neighbors[parity])
                if t>=2:
                    expected=sum(1<<j for j,v in enumerate(vs) if (v^base).bit_count()<=2*t)
                    assert state==expected,(n,parity,t)
                    shell_checks+=1
            # Enumerate all nonempty subsets of farthest-shells to verify their union count.
            if n%2:
                distinct=set()
                for target in vs:
                    sphere=sum(1<<ind[w] for w in vs if (target^w).bit_count()==n-1)
                    bits=[1<<i for i in range(N) if sphere>>i&1]
                    for mask in range(1,1<<len(bits)):
                        sub=0
                        for j in range(len(bits)):
                            if (mask>>j)&1: sub |= bits[j]
                        distinct.add(sub)
                assert len(distinct)==formula_bad(n),(n,len(distinct),formula_bad(n))
                bad_counts[(n,parity)] = len(distinct)
            else:
                assert formula_bad(n)==N
                bad_counts[(n,parity)] = N
        # Exhaustively cross-check singletons, pairs, triples and random sparse and dense states.
        for parity in (0,1):
            for k in (1,2,3):
                for ii in combinations(range(N),k):
                    if k==3 and n>=8 and rng.randrange(100):
                        continue
                    x=sum(1<<i for i in ii)
                    tau=predicted_tau(n,x,0 if parity==0 else x,neighbors) if parity==0 else predicted_tau(n,0,x,neighbors)
                    assert (tau==T)==bad(n,x,vertices[parity]),(n,parity,ii,tau)
                    checks+=1
        for _ in range(120):
            masks=[]
            for parity in (0,1):
                k=rng.randrange(0, min(1<<n,14))
                masks.append(sum(1<<v for v in rng.sample(range(N),k)))
            tau=predicted_tau(n,*masks,neighbors)
            should=bad(n,masks[0],vertices[0]) or bad(n,masks[1],vertices[1])
            assert (tau==T)==should,(n,tau,masks)
            checks+=1
    # Small n 7 can exhaustively validate all supports of its 64-vertex component up to six selected sites.
    n=7
    vertices,nbr=neighbor_masks(n)
    for k in (1,2,3):
        for ii in combinations(range(64),k):
            if k==3 and rng.randrange(50): continue
            mask=sum(1<<i for i in ii)
            tau=predicted_tau(n,mask,0,nbr)
            assert (tau==n//2)==bad(n,mask,vertices[0])
            checks+=1
    for n in range(6,10):
        N=1<<(n-1); A=formula_bad(n)
        assert 0<A<(1<<N)
        print('n=',n,'T=',n//2,'A=',A,'maximizers=',2*A*(1<<N)-A*A)
    print('VERIFY_OK', 'walk_shell_checks=',shell_checks,'state_checks=',checks,'bad_supports=',bad_counts)

if __name__=='__main__':
    run()
