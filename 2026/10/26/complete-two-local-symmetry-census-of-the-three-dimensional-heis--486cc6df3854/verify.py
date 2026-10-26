"""Independent finite-field witness checks for two-local symmetries of H_3(F_q).

Execute with Python 3.10+; no external dependencies.  Arithmetic verification
uses prime fields 2 and 3, while the accompanying proof treats any F_q.
"""
from itertools import product, permutations
import random


def fops(q):
    P = list(product(range(q), repeat=3))
    V = list(product(range(q), repeat=2))
    add = lambda x, y: tuple((a+b)%q for a,b in zip(x,y))
    mul = lambda t,x: tuple(t*a%q for a in x)
    return P,V,add,mul


def all_linear_witnesses(q, group):
    P,V,_,_ = fops(q)
    output=[]
    for a,b,c,d in product(range(q),repeat=4):
        det = (a*d-b*c)%q
        if group and not det:continue
        for u,v in product(range(q),repeat=2):
            row=[]
            for x,y,z in P:
                row.append(((a*x+b*y)%q,(c*x+d*y)%q,
                            (u*x+v*y+(det if group else (a+d)%q)*z)%q))
            output.append(tuple(row))
    return P, output


def lookup_for_pairs(witnesses, n):
    lookup={}
    for i in range(n):
        for j in range(i,n):
            lookup[i,j]={ (w[i],w[j]) for w in witnesses }
    return lookup


def check_all_pairs(target, P, allowed):
    for i in range(len(P)):
        for j in range(i,len(P)):
            if (target[i],target[j]) not in allowed[i,j]:
                return False
    return True


def linear_test(arr, P, q):
    D={x:v for x,v in zip(P,arr)}
    for x in P:
        for y in P:
            if D[tuple((a+b)%q for a,b in zip(x,y))] != tuple((a+b)%q for a,b in zip(D[x],D[y])):
                return False
    return True


def classify_binary_derivations():
    q=2
    P,D=fops(q)[0],all_linear_witnesses(q,False)[1]
    allow=lookup_for_pairs(D,len(P))
    vs=[(1,0),(0,1),(1,1)]
    g_reps=[x for x in P if x!=(0,0,0)]
    count=lin=ordinary=0
    dset=set(D)
    for fvals in product(list(product(range(q),repeat=2)),repeat=len(vs)):
        f=dict(zip(vs,fvals))
        for gvals in product(range(q),repeat=len(g_reps)):
            gd=dict(zip(g_reps,gvals))
            cand=tuple((*f.get((x,y),(0,0)),gd.get((x,y,z),0)) for x,y,z in P)
            assert check_all_pairs(cand,P,allow)
            count+=1
            if linear_test(cand,P,q):lin+=1
            if cand in dset:ordinary+=1
    assert (count,lin,ordinary)==(8192,128,64),(count,lin,ordinary)
    assert len(D)==64
    return count,lin,ordinary


def classify_binary_automorphisms():
    q=2
    P,V,_,_=fops(q)
    W=all_linear_witnesses(q,True)[1]
    allow=lookup_for_pairs(W,len(P))
    reps=[(1,0),(0,1),(1,1)]
    aset=set(W)
    count=lin=ordinary=0
    for p in permutations(reps):
        f=dict(zip(reps,p))
        for vertical in product(permutations([0,1]),repeat=3):
            vertical=dict(zip(reps,vertical))
            cand=[]
            for a,b,z in P:
                if (a,b)==(0,0):cand.append((0,0,z));continue
                cand.append((*f[a,b],vertical[a,b][z]))
            cand=tuple(cand)
            assert check_all_pairs(cand,P,allow)
            count+=1
            if linear_test(cand,P,q):lin+=1
            if cand in aset:ordinary+=1
    assert (count,lin,ordinary)==(48,24,24),(count,lin,ordinary)
    assert len(W)==24
    return count,lin,ordinary


def reps(q,dim):
    return [v for v in product(range(q),repeat=dim)
            if 1 in v and next((a for a in v if a),0)==1]


def normalized_nonzero(v,q):
    a=next(a for a in v if a)
    factor=pow(a,-1,q)
    return tuple(factor*x%q for x in v),a


def ternary_examples(group,samples=150):
    q=3
    P,V,_,_=fops(q)
    W=all_linear_witnesses(q,group)[1]
    allow=lookup_for_pairs(W,len(P))
    rng=random.Random(514243)
    projective=reps(q,2)
    three_reps=reps(q,3)
    assert len(projective)==4 and len(three_reps)==13
    for _ in range(samples):
        if group:
            p=projective[:]
            rng.shuffle(p)
            fv={v:tuple(k*e%q for e in w) for v,w in zip(projective,p) for k in [rng.choice([1,2])]}
            gv={v:rng.sample([0,1,2],3) for v in projective}
            tau=rng.choice([1,2])
        else:
            fv={v:tuple(rng.randrange(q) for _ in range(2)) for v in projective}
            gv={v:rng.randrange(q) for v in three_reps}
        row=[]
        for x,y,z in P:
            if (x,y)==(0,0):
                if group:row.append((0,0,tau*z%q))
                else:
                    if z==0:row.append((0,0,0))
                    else:row.append((0,0,z*gv[(0,0,1)]%q))
                continue
            v,a=normalized_nonzero((x,y),q)
            fh=tuple(a*u%q for u in fv[v])
            if group:
                value=a*gv[v][z*pow(a,-1,q)%q]%q
            else:
                p3,b=normalized_nonzero((x,y,z),q)
                value=b*gv[p3]%q
            row.append((*fh,value))
        if not check_all_pairs(tuple(row),P,allow):
            for i in range(len(P)):
                for j in range(i,len(P)):
                    if (row[i],row[j]) not in allow[i,j]:
                        print('FAIL',group,'source',P[i],P[j],'output',row[i],row[j])
                        print('f',fv,'g',gv,'T',tau if group else None)
                        raise AssertionError('not two-local')
    return len(W), samples


def main():
    print('q=2 all 2-local derivation candidates: count, linear, derivations',classify_binary_derivations())
    print('q=2 all 2-local automorphism candidates: count, linear, automorphisms',classify_binary_automorphisms())
    print('q=3 randomized derivation examples: witnesses, samples',ternary_examples(False))
    print('q=3 randomized automorphism examples: witnesses, samples',ternary_examples(True))
    assert 3**(3**2+3*3+3) == 3**21
    assert (4*3*2) * (3-1)**(3+2) * 6**(3+1) == 995328
    print('VERIFY_OK two-local classifications, exact binary enumeration, ternary pair-witness tests')

if __name__=='__main__':main()
