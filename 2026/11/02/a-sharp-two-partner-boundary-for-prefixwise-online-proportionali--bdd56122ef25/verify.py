"""Standalone exact-integer finite checks of the two-sided PROP1 guarantee.
No external dependencies. Run: python verify.py
"""
from itertools import product
from random import Random

def run(n, items):
    # item: ((one or two eligible vertices), positive integer size)
    load = [0]*n
    double_share = [0]*n
    received = [[] for _ in range(n)]
    unreceived = [[] for _ in range(n)]
    local = {}
    for eligibility,p in items:
        assert p>0 and len(eligibility) in (1,2)
        e=tuple(sorted(eligibility))
        if len(e)==1: winner=e[0]
        else:
            x,y=e
            ax,ay=local.get(e,(0,0))
            winner=x if ax<=ay else y
            local[e]=(ax+p,ay) if winner==x else (ax,ay+p)
        load[winner]+=p
        for v in e:
            double_share[v]+=2*p//len(e) # p if pair, 2p if singleton
            (received if v==winner else unreceived)[v].append(p)
        for i in range(n):
            over=2*load[i]-double_share[i]
            under=-over
            if over>2*max(received[i],default=0) or under>2*max(unreceived[i],default=0):
                return False, (i, tuple(items), tuple(load),tuple(double_share),tuple(received[i]),tuple(unreceived[i]))
    return True,None

def exhaustive(n,edges,weights,depth):
    options=[((u,v),w) for u,v in edges for w in weights]
    total=0
    for k in range(depth+1):
        for seq in product(options,repeat=k):
            ok,detail=run(n,seq)
            assert ok, detail
            total+=1
    return total

if __name__=='__main__':
    counts={}
    counts['three_vertex_path']=exhaustive(3,[(0,1),(1,2)],(1,2,5),6)
    counts['four_vertex_cycle']=exhaustive(4,[(0,1),(1,2),(2,3),(0,3)],(1,2,3),5)
    rng=Random(17289)
    edges=[(0,1),(1,2),(2,3),(3,4),(4,5),(0,5)]
    for z in range(10000):
        seq=[]
        for k in range(rng.randint(1,75)):
            if rng.randrange(9)==0:
                seq.append(((rng.randrange(6),),rng.choice((1,2,5,11,23))))
            else:
                seq.append((edges[rng.randrange(len(edges))],rng.choice((1,2,5,11,23))))
        ok,detail=run(6,seq)
        assert ok,detail
    counts['seeded_random']=10000
    print('PASS',counts)

def tournament_check():
    from itertools import product
    checked=0
    for bits in product((0,1),repeat=7):
        champs=list(range(8))
        loads=[0]*8
        incident=[0]*8
        jobs=[]
        pos=0
        for _ in range(3):
            next_round=[]
            for index in range(0,len(champs),2):
                u,v=champs[index:index+2]
                winner=(u,v)[bits[pos]]
                pos+=1
                loads[winner]+=1
                incident[u]+=1;incident[v]+=1
                jobs.append((u,v,winner))
                next_round.append(winner)
            champs=next_round
        assert len(champs)==1
        winner=champs[0]
        assert loads[winner]==3 and incident[winner]==3
        assert loads[winner]-1>incident[winner]/2
        assert max(incident)<=3
        checked+=1
    return checked
if __name__=='__main__':
    print('TOURNAMENT PASS', tournament_check(), 'adaptive recipient histories')
