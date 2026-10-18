"""Independent finite-set semantic closure for one-letter bilateral state logic.
No external dependencies; complete exhaustive test, not a statistical sample.
"""
from itertools import combinations
from collections import deque

U = frozenset((0,1))
TEAMS = tuple(frozenset(comb) for n in range(3) for comb in combinations(U,n))
assert len(TEAMS) == 4 and TEAMS[0] == frozenset()
TINDEX = {t:i for i,t in enumerate(TEAMS)}
# semantic signatures as pairs of frozensets of *teams*, not bitwise masks
ALL=frozenset(TEAMS)
base = {
    (frozenset((frozenset(),)),ALL),
    (frozenset(t for t in TEAMS if t),frozenset((frozenset(),))),
    (frozenset(t for t in TEAMS if 0 not in t),frozenset(t for t in TEAMS if 1 not in t)),
}
def split(a,b):
    return frozenset(t for t in TEAMS if any(left|right==t for left in a for right in b))
def neg(x):return (x[1],x[0])
def conj(x,y):return (x[0]&y[0],split(x[1],y[1]))
def disj(x,y):return (split(x[0],y[0]),x[1]&y[1])
def diamond(x):
    return (frozenset(t for t in TEAMS if any(s and s.issubset(t) for s in x[0])),x[1])
def close_under_propositional(seed):
    found=set(seed)
    q=deque(sorted(found,key=repr))
    while q:
        x=q.popleft()
        # Negation on all generated states
        for z in (neg(x),):
            if z not in found:
                found.add(z);q.append(z)
        for y in tuple(found):
            for z in (conj(x,y),disj(x,y)):
                if z not in found:
                    found.add(z);q.append(z)
    # check postfixed under operations as a separate explicit exhaustive certificate
    assert all(neg(x) in found for x in found)
    assert all(conj(x,y) in found and disj(x,y) in found for x in found for y in found)
    return frozenset(found)
def enc(sig):
    return [sum(1<<TINDEX[t] for t in x) for x in sig]

if __name__=='__main__':
    import json,sys
    rank0=close_under_propositional(base)
    rank1=close_under_propositional(set(rank0)|{diamond(x) for x in rank0})
    rank2=close_under_propositional(set(rank1)|{diamond(x) for x in rank1})
    rank3=close_under_propositional(set(rank2)|{diamond(x) for x in rank2})
    assert (len(rank0),len(rank1),len(rank2),len(rank3)) == (39,64,66,66)
    assert rank2==rank3
    exceptional=sorted(enc(x) for x in rank2-rank1)
    assert exceptional == [[10,12],[12,10]],exceptional
    # exact simple witnesses for both missing rank-1 types
    p=next(x for x in base if enc(x)==[5,3])
    assert enc(diamond(neg(diamond(p)))) == [10,12]
    assert enc(diamond(neg(diamond(neg(p))))) == [12,10]
    # every base + all four operations in rank2: completeness for all modal depths
    assert base <= rank2
    assert all(diamond(x) in rank2 and neg(x) in rank2 for x in rank2)
    assert all(conj(x,y) in rank2 and disj(x,y) in rank2 for x in rank2 for y in rank2)
    certificate = {'schema_version':1,'team_encoding':{'0':[],'1':[0],'2':[1],'3':[0,1]},
      'signature_encoding':'[support_mask,antisupport_mask] with team index bits 0..3',
      'counts':[39,64,66,66],
      'depth0_signatures':sorted(enc(x) for x in rank0),
      'depth1_new_signatures':sorted(enc(x) for x in rank1-rank0),
      'depth2_new_signatures':exceptional,
      'all_signatures':sorted(enc(x) for x in rank2)}
    if len(sys.argv)>1:
        with open(sys.argv[1],encoding='utf-8') as f: expected=json.load(f)
        assert expected == certificate, 'certificate differs from recomputed exhaustive closure'
    if len(sys.argv)>2:
        with open(sys.argv[2],encoding='utf-8') as f: dag=json.load(f)
        assert dag['schema_version']==1
        nodes=dag['nodes']; evaluated=[]; depths=[]
        literals={'bot':(frozenset((frozenset(),)),ALL),
                  'ne':(frozenset(t for t in TEAMS if t),frozenset((frozenset(),))),
                  'p':(frozenset(t for t in TEAMS if 0 not in t),frozenset(t for t in TEAMS if 1 not in t))}
        for row in nodes:
            op=row['op']; args=row['args']
            assert all(isinstance(i,int) and 0<=i<len(evaluated) for i in args)
            if op in literals:
                assert args==[]; sig=literals[op]; d=0
            elif op=='not':
                assert len(args)==1;sig=neg(evaluated[args[0]]);d=depths[args[0]]
            elif op=='diamond':
                assert len(args)==1;sig=diamond(evaluated[args[0]]);d=depths[args[0]]+1
            elif op=='and':
                assert len(args)==2;sig=conj(*[evaluated[i] for i in args]);d=max(depths[i] for i in args)
            elif op=='or':
                assert len(args)==2;sig=disj(*[evaluated[i] for i in args]);d=max(depths[i] for i in args)
            else:raise AssertionError('unknown formula constructor')
            assert enc(sig)==row['signature'] and d==row['modal_depth']
            evaluated.append(sig);depths.append(d)
        assert len(nodes)==len(rank2)==66
        assert len(set(evaluated))==66 and set(evaluated)==rank2
        assert all({sig for sig,d in zip(evaluated,depths) if d<=k}==L
                   for k,L in enumerate((rank0,rank1,rank2)))
    print('BILATERAL_ONE_LETTER_DEPTH_COUNTS_OK 39 64 66 66')
    print('missing at depth1:',exceptional)
