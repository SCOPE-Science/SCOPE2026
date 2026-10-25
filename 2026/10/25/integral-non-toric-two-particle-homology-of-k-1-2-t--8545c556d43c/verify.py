"""Exact and modular checks for two-point homology of complete tripartite K_{1,2,t}.
Requires Python 3 standard library only. Run: python verify.py
"""
from itertools import combinations


def graph(t):
    assert t >= 3
    E = {('d', 0): (0, 1), ('d', 1): (0, 2)}
    for i in range(t):
        w = i + 3
        E[('p', i)] = (0, w)
        E[('q', i)] = (1, w)
        E[('r', i)] = (2, w)
    names = list(E)
    pair_keys = [(e, f) for e, f in combinations(names, 2)
                 if not set(E[e]).intersection(E[f])]
    c1 = [(e, x) for e in names for x in range(t+3) if x not in E[e]]
    return E, names, pair_keys, c1


def partial(E, pair):
    e, f = pair
    a, b = E[e]
    c, d = E[f]
    return {(f, b): 1, (f, a): -1, (e, d): -1, (e, c): 1}


def cells(t):
    E, names, pairs, c1 = graph(t)
    assert len(names) == 3*t+2
    assert len(c1) == (3*t+2)*(t+1)
    assert len(pairs) == 3*t*t-t
    return E, names, pairs, c1


def vector(t, P, pairs):
    assert len(P) == t and all(len(row) == t for row in P)
    assert all(P[i][i] == 0 and sum(P[i]) == 0 for i in range(t))
    assert all(P[i][j] == P[j][i] for i in range(t) for j in range(t))
    idpair = {p:k for k,p in enumerate(pairs)}
    out = [0]*len(pairs)
    def add(e, f, val):
        if (e, f) in idpair:
            out[idpair[e, f]] += val
        else:
            out[idpair[f, e]] -= val
    for i in range(t):
        for j in range(t):
            if i != j and P[i][j]:
                a = P[i][j]
                add(('p',i),('q',j),a)
                add(('p',i),('r',j),-a)
                add(('q',i),('r',j),a)
    return out


def cycle_sample(t, i, j, k, l):
    P = [[0]*t for _ in range(t)]
    for a,b,v in [(i,j,1),(j,k,-1),(k,l,1),(l,i,-1)]:
        P[a][b]=P[b][a]=v
    return P


def action_on_chain(E, pairs, coeffs, permutation):
    key_of_endpoints = {frozenset(edge):name for name,edge in E.items()}
    idpair = {p:i for i,p in enumerate(pairs)}
    ans = [0]*len(pairs)
    for k,(e,f) in enumerate(pairs):
        if not coeffs[k]:continue
        e2=key_of_endpoints[frozenset(permutation[x] for x in E[e])]
        f2=key_of_endpoints[frozenset(permutation[x] for x in E[f])]
        # Each graph edge is directed from a special vertex to another part;
        # a part-preserving automorphism preserves those edge orientations.
        if (e2,f2) in idpair:ans[idpair[e2,f2]]+=coeffs[k]
        else:ans[idpair[f2,e2]]-=coeffs[k]
    return ans


def rank_mod(t, prime):
    E,names,pairs,c1=cells(t)
    row_index={x:i for i,x in enumerate(c1)}
    # Sparse elimination by pivot rows, over the prime field.
    piv={}
    for pair in pairs:
        vec={row_index[cell]:v%prime for cell,v in partial(E,pair).items()}
        while vec:
            ix=min(vec)
            val=vec[ix]
            if ix not in piv:
                inv=pow(val,-1,prime)
                piv[ix]={k:(v*inv)%prime for k,v in vec.items() if v%prime}
                break
            row=piv[ix]
            for k,v in row.items():
                vv=(vec.get(k,0)-val*v)%prime
                if vv:vec[k]=vv
                elif k in vec:del vec[k]
    return len(piv)


def run():
    for t in range(3,9):
        E,names,pairs,c1=cells(t)
        expected = t*(t-3)//2
        r101=rank_mod(t,101)
        r2=rank_mod(t,2)
        assert r101==len(pairs)-expected, (t,r101)
        assert r2==r101-1, (t,r2)
        print('t',t,'cells',((t+3)*(t+2)//2,len(c1),len(pairs)),
              'rank_mod101',r101,'rank_mod2',r2,'H2rank',expected)
        if t<4:continue
        # All distinct ordered quadrilaterals, up to t=6.
        choices=list(combinations(range(t),4))
        for quadruple in choices:
            P=cycle_sample(t,*quadruple)
            coeffs=vector(t,P,pairs)
            check={}
            for ix,c in enumerate(coeffs):
                if c:
                    for row,sgn in partial(E,pairs[ix]).items():
                        check[row]=check.get(row,0)+c*sgn
            assert not any(check.values()),(t,quadruple)
            # The unique nontrivial automorphism of the two-vertex part is -1.
            flip=list(range(t+3));flip[1],flip[2]=2,1
            assert action_on_chain(E,pairs,coeffs,flip)==[-x for x in coeffs]
            # The adjacent transpositions generate the symmetry of the t-vertex part.
            for i in range(t-1):
                pp=list(range(t+3));pp[3+i],pp[4+i]=pp[4+i],pp[3+i]
                P2=[[P[pp[3+a]-3][pp[3+b]-3] for b in range(t)] for a in range(t)]
                assert action_on_chain(E,pairs,coeffs,pp)==vector(t,P2,pairs)
        print('equivariant_integral_quadrilateral_checks',len(choices))
    print('VERIFY_OK_K12T_NON_TORIC_INTEGRAL_SECOND_HOMOLOGY_MODULE')

if __name__=='__main__':run()
