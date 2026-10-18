"""Check finite instances of atom-free two-agent K45 believed-announcement rank construction."""
from itertools import combinations

def construction(height):
    nodes=[()]
    for length in range(1,height+1):
        nodes.extend(tuple(reversed(c)) for c in combinations(range(height),length))
    nodes=sorted(nodes,key=lambda x:(len(x),x))
    N=len(nodes); ind={x:i for i,x in enumerate(nodes)}
    outgoing=[[set() for _ in nodes] for _ in range(2)]
    blocks=[]
    for s in nodes:
        rank=s[-1] if s else height
        kids=[s+(j,) for j in range(rank)]
        agent=len(s)%2
        for x in [s]+kids:
            for y in kids:
                outgoing[agent][ind[x]].add(ind[y])
        blocks.append((s, agent, [ind[x] for x in [s]+kids], [ind[y] for y in kids]))
    return nodes,outgoing,blocks

def k45(R):
    return all(R[y]==R[x] for x,row in enumerate(R) for y in row)

def run(h):
    nodes,R,blocks=construction(h)
    assert all(k45(v) for v in R)
    for t in range(h+1):
        assert all(k45(v) for v in R)
        for s,i,sources,targets in blocks:
            e={y for y in targets if nodes[y][-1]>=t}
            assert all(R[i][x]==e for x in sources),(h,t,s,i,e)
        if t<h:
            truth={j for j in range(len(nodes)) if R[0][j] and R[1][j]}
            nxt=[[row&truth for row in Ra] for Ra in R]
            assert nxt != R,(h,t)
            R=nxt
    assert not any(row for Ra in R for row in Ra)
    print('h',h,'N',len(nodes),'initial_arrows',sum(len(row) for Ra in construction(h)[1] for row in Ra),'stabilizes',h)
for h in range(0,9): run(h)
print('VERIFY_OK')
