"""Direct rooted graph automorphism enumeration for small unequal odd tori."""
from collections import defaultdict
import networkx as nx


def check():
    for m, n in [(5, 7), (5, 9), (7, 9)]:
        G = nx.Graph()
        for x in range(m):
            for y in range(n):
                G.add_node((x, y), marked=(x == 0 and y == 0))
                G.add_edge((x,y),((x+1)%m,y))
                G.add_edge((x,y),(x,(y+1)%n))
        matcher=nx.algorithms.isomorphism.GraphMatcher(
            G,G,node_match=lambda a,b:a['marked']==b['marked'])
        count=0; orbit=defaultdict(set)
        for mapping in matcher.isomorphisms_iter():
            count+=1
            for v,w in mapping.items():orbit[v].add(w)
        assert count==4, (m,n,count)
        for x in range(m):
            for y in range(n):
                want={(u,v) for u in {x,(-x)%m} for v in {y,(-y)%n}}
                assert orbit[x,y]==want,(m,n,(x,y),orbit[x,y],want)
        print(f'AUTOMORPHISM_PASS m={m} n={n} rooted_group_order={count}')


if __name__=='__main__':
    check()
