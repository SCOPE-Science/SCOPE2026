"""Direct finite checks for asymmetric two-block-marked partition lattices.
Usage: python3 verify_refinement.py. Python 3 standard library only.
This finite test is not a proof of the general theorem.
"""
from collections import Counter,defaultdict


def partitions(n):
    out=[]
    def f(w,maxval):
        if len(w)==n:
            blocks=[0]*(maxval+1)
            for i,j in enumerate(w): blocks[j]|=1<<i
            out.append((tuple(w),tuple(blocks)))
            return
        for j in range(maxval+2):f(w+[j],max(maxval,j))
    f([0],0)
    return out


def refine_structure(n, ps):
    # Edge x -> y means x is a strictly finer partition than y.
    N=len(ps)
    less=[[] for _ in ps];greater=[[] for _ in ps]
    for i,(_,bi) in enumerate(ps):
        for j,(_,bj) in enumerate(ps):
            if i!=j and all(any(x&y==x for y in bj) for x in bi):
                greater[i].append(j); less[j].append(i)
    return less,greater


def refine(labels, less,greater):
    labels=list(labels)
    for step in range(1,7):
        signatures=[]
        for i in range(len(labels)):
            signatures.append((labels[i],tuple(sorted(Counter(labels[j] for j in less[i]).items())),tuple(sorted(Counter(labels[j] for j in greater[i]).items()))))
        index={v:i for i,v in enumerate(sorted(set(signatures)))}
        nxt=[index[v] for v in signatures]
        # Compare equivalence classes, not numeric colour IDs.
        old_count=len(set(labels));new_count=len(index)
        if new_count==old_count: return labels,step-1
        labels=nxt
    raise AssertionError('unexpectedly slow refinement')


def orbit_key(blocks,a):
    mask=(1<<a)-1
    return tuple(sorted(((x&mask).bit_count(),(x&~mask).bit_count()) for x in blocks))


def main():
    cases=0; vertices=0; depthmax=0
    for n in range(3,8):
        ps=partitions(n)
        less,greater=refine_structure(n,ps)
        for a in range((n//2)+1,n):
            b=n-a
            if a<=b:continue
            anchor_word=tuple([0]*a+[1]*b)
            anchor=next(i for i,(w,_) in enumerate(ps) if w==anchor_word)
            colors,depth=refine([1 if i==anchor else 0 for i in range(len(ps))],less,greater)
            keys=[orbit_key(blocks,a) for _,blocks in ps]
            c_to_key=defaultdict(set);key_to_c=defaultdict(set)
            for c,key in zip(colors,keys):c_to_key[c].add(key);key_to_c[key].add(c)
            assert all(len(s)==1 for s in c_to_key.values()),(n,a,'WL fused orbits')
            assert all(len(s)==1 for s in key_to_c.values()),(n,a,'WL split orbit')
            assert depth<=4,(n,a,depth)
            print(f'n={n}, anchor=({a},{b}), vertices={len(ps)}, cells={len(set(colors))}, stable_by_round={depth}')
            cases+=1;vertices+=len(ps);depthmax=max(depthmax,depth)
    print('VERIFY_REFINEMENT_OK',cases,vertices,depthmax)


if __name__=='__main__':main()
