"""Independent tree enumerator cross-check via NetworkX; requires networkx >=2.8."""
import networkx as nx
from collections import defaultdict

def hom_from_directed_dfs(source,target):
    vertices=list(source.nodes())
    root=vertices[0]
    def calculate(u,p):
        sub=[calculate(w,u) for w in source.neighbors(u) if w!=p]
        return {v:__import__('math').prod(sum(child[x] for x in target.neighbors(v)) for child in sub) for v in target.nodes()}
    return sum(calculate(root,-1).values())

def main():
    hs={1:[nx.empty_graph(1)]}
    hs.update({k:list(nx.generators.nonisomorphic_trees(k)) for k in range(2,9)})
    sizes=[]
    unique13=None
    for n in range(1,14):
        ts=[nx.empty_graph(1)] if n==1 else list(nx.generators.nonisomorphic_trees(n))
        sizes.append(len(ts))
        if n<4:continue
        cls={k:defaultdict(list) for k in range(1,9)}
        for T in ts:
            profile=[]
            for k in range(1,9):
                profile.extend(hom_from_directed_dfs(H,T) for H in hs[k])
                cls[k][tuple(profile)].append(T)
        nk=next(k for k in range(1,9) if len(cls[k])==len(ts))
        assert nk=={4:3,5:3,6:4,7:4,8:5,9:5,10:6,11:6,12:7,13:8}[n]
        if n==13:
            cc=[v for v in cls[7].values() if len(v)>1]
            assert len(cc)==1 and len(cc[0])==2 and not nx.is_isomorphic(*cc[0])
            tt=cc[0]
            distinguish=sum(hom_from_directed_dfs(H,tt[0]) != hom_from_directed_dfs(H,tt[1]) for H in hs[8])
            assert distinguish==5
            unique13=len(cls[7])
    assert sizes==[1,1,1,2,3,6,11,23,47,106,235,551,1301]
    print('NETWORKX_TREE_COUNTS',sizes)
    print('N13_SEVEN_SOURCE_PROFILES',unique13)
    print('N13_ORDER_EIGHT_SPLITTING_SOURCES',5)
    print('INDEPENDENT_BOUNDED_PROFILE_CROSSCHECK_PASS')
if __name__=='__main__':main()
