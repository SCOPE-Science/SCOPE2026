"""Independent finite-variable logical-type refinement for selected small designs.

A color represents the complete bounded-depth type of an assignment to k
reusable variables. Existential moves correspond to changing one coordinate.
Stabilization is exact for these finite instances; arbitrary-order claims rely
on a separate mathematical back-and-forth proof.
"""
from itertools import product, combinations
from collections import defaultdict
import json

# Independent explicit constructors for the test designs.
def f2_blocks(dim):
    v=2**dim
    return [tuple(Q) for Q in combinations(range(v),4)
            if Q[0]^Q[1]^Q[2]^Q[3]==0]


def sts7_blocks():
    return [tuple(Q) for Q in combinations(range(7),3)
            if (Q[0]+1)^(Q[1]+1)^(Q[2]+1)==0]


def f3_lines():
    points=[(x,y) for x in range(3) for y in range(3)]
    out=set()
    for a,b in ((1,0),(0,1),(1,1),(1,2)):
        for c in range(3):
            z=tuple(i for i,(x,y) in enumerate(points) if (a*x+b*y)%3==c)
            assert len(z)==3
            out.add(z)
    return sorted(out)


def sqs10_blocks():
    points=[(x,y) for x in range(3) for y in range(3)]
    blocks={tuple(sorted((9,)+line)) for line in f3_lines()}
    for a,b in points:
        for r in (1,2):
            B=tuple(i for i,(x,y) in enumerate(points)
                if ((x-a)*(x-a)+(y-b)*(y-b))%3==r)
            assert len(B)==4
            blocks.add(B)
    assert len(blocks)==30
    return sorted(blocks)



def calc(designs,k):
    records=[]
    signatures={}
    for title,t,v,blocks,deleted in designs:
        verts=tuple(x for x in range(v) if x!=deleted)
        h={frozenset(b) for b in blocks if deleted not in b}
        tuples=list(product(verts, repeat=k))
        first=[]
        for tup in tuples:
            eq=tuple(tup.index(x) for x in tup)
            # Each relation instance has arity t+1 and may use any
            # ordered selection of the k variables, including repetitions.
            # A symmetric irreflexive relation is determined by the collection
            # of (t+1)-index subsets whose distinct values form a block.
            b=tuple(tuple(ids) for ids in combinations(range(k),t+1)
                    if len({tup[i] for i in ids})==t+1 and
                    frozenset(tup[i] for i in ids) in h)
            first.append((eq,b))
        records.append({'name':title,'k':k,'n':len(verts),
                        'tuples':tuples,'initial':first,'colors':[]})
    initial_keys=sorted(set(v for d in records for v in d['initial']))
    ids={v:i for i,v in enumerate(initial_keys)}
    for d in records:d['colors']=[ids[s] for s in d['initial']]
    rounds=[]
    for iteration in range(40):
        all_fibers=[[] for _ in range(k)]
        fiber_keys=[]
        for axis in range(k):
            for d in records:
                group=defaultdict(set)
                for tup,c in zip(d['tuples'],d['colors']):
                    key=tup[:axis]+tup[axis+1:]
                    group[key].add(c)
                out={kk:tuple(sorted(cc)) for kk,cc in group.items()}
                fiber_keys.extend(out.values())
                all_fibers[axis].append(out)
        fd={v:i for i,v in enumerate(sorted(set(fiber_keys)))}
        new_sign=[]
        for j,d in enumerate(records):
            new_sign.append([
               (color,tuple(fd[all_fibers[axis][j][tup[:axis]+tup[axis+1:]]]
                            for axis in range(k)))
               for tup,color in zip(d['tuples'],d['colors'])])
        sid={s:i for i,s in enumerate(sorted(set(z for group in new_sign for z in group)))}
        no_change=(len(sid)==len({c for d in records for c in d['colors']}))
        for d,sign in zip(records,new_sign): d['colors']=[sid[s] for s in sign]
        rounds.append({'depth':iteration+1,'all_types':len(sid),
           'individual_support_sizes':{d['name']:len(set(d['colors'])) for d in records}})
        if no_change: break
    supports={d['name']:set(d['colors']) for d in records}
    return {'k':k,'total_tuples':sum(len(d['tuples']) for d in records),
            'fixedpoint_depth':len(rounds), 'stabilized':no_change,
            'rounds':rounds,
            'equivalent_pairs':[[a,b] for a,b in combinations(supports,2)
                                if supports[a]==supports[b]],
            'nonequivalent_pairs':[[a,b] for a,b in combinations(supports,2)
                                if supports[a]!=supports[b]]}


def main():
    f8=f2_blocks(3); f10=sqs10_blocks(); f16=f2_blocks(4)
    full=[('SQS8-full',3,8,f8,None),('SQS10-full',3,10,f10,None)]
    punct=[('SQS8-punct',3,8,f8,0),('SQS10-punct',3,10,f10,9),
           ('SQS16-punct',3,16,f16,0)]
    # Use the same common palette so full and punctured outcomes compare.
    q=calc(full+punct,4)
    assert ['SQS10-punct','SQS16-punct'] in q['equivalent_pairs']
    assert ['SQS8-full','SQS10-full'] in q['equivalent_pairs']
    assert ['SQS8-punct','SQS10-punct'] in q['nonequivalent_pairs']
    assert ['SQS10-full','SQS10-punct'] in q['nonequivalent_pairs']
    t2=calc([('STS7-full',2,7,sts7_blocks(),None),
             ('STS7-punct',2,7,sts7_blocks(),0),
             ('STS9-punct',2,9,f3_lines(),0)],3)
    assert ['STS7-punct','STS9-punct'] in t2['equivalent_pairs']
    assert ['STS7-full','STS7-punct'] in t2['nonequivalent_pairs']
    print(json.dumps({'quadruple_systems':q,'triple_systems':t2,'status':'PASS'},indent=2))

if __name__=='__main__':main()
