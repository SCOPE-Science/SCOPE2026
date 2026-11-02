from itertools import combinations
from functools import lru_cache

@lru_cache(None)
def canon(edges):
    k=len(edges)
    best=None
    for flip in range(1<<k):
        labels={}; nxt=0; out=[]
        for i,(u,v) in enumerate(edges):
            if flip>>i&1: u,v=v,u
            for x in (u,v):
                if x not in labels: labels[x]=nxt;nxt+=1
                out.append(labels[x])
        t=tuple(out)
        if best is None or t<best:best=t
    return best

def flat_edges(t):return tuple((t[2*i],t[2*i+1]) for i in range(len(t)//2))
def build(n,k):
    start=canon(((0,1),)*k)
    order=[start]; ids={start:0}; trans=[]
    for state in order:
        es=flat_edges(state); v=1+max(state)
        target=[]
        for i in range(k):
            outcomes=set()
            for a,b in combinations(range(min(n,v+2)),2):
                new=canon(es[:i]+((a,b),)+es[i+1:])
                if 1+max(new)>n:continue
                if new not in ids:
                    ids[new]=len(order);order.append(new)
                outcomes.add(ids[new])
            target.append(frozenset(outcomes))
        trans.append(tuple(target))
    atom=[]
    for st in order:
        es=flat_edges(st)
        a=[]
        for i in range(k):
            for j in range(i+1,k):
                a.append(0 if es[i]==es[j] else 1 if bool(set(es[i])&set(es[j])) else 2)
        atom.append(tuple(a))
    return order,trans,atom

def refine(models):
    nodes=[(n,i) for n, (_,trans,_) in models.items() for i in range(len(trans))]
    colors={key:models[key[0]][2][key[1]] for key in nodes}
    def compress(d):
        vals=sorted(set(d.values()))
        ix={v:i for i,v in enumerate(vals)}
        return {key:ix[value] for key,value in d.items()}
    colors=compress(colors)
    history=[]
    for q in range(25):
        per_n={n:colors[(n,0)] for n in models}
        groups={};
        for n,c in per_n.items():groups.setdefault(c,[]).append(n)
        history.append([tuple(g) for g in groups.values()])
        sig={}
        for n,i in nodes:
            sig[(n,i)]=(colors[(n,i)],tuple(tuple(sorted({colors[(n,j)] for j in targets})) for targets in models[n][1][i]))
        newer=compress(sig)
        if len(set(newer.values()))==len(set(colors.values())):
            return q,history,len(set(colors.values()))
        colors=newer
    return 25,history,len(set(colors.values()))

def run():
    for k,lim in [(2,7),(3,9),(4,10)]:
        models={n:build(n,k) for n in range(3,lim+1)}
        q,history,count=refine(models)
        print('k',k,'n',list(models),'orbit counts',[(n,len(x[0])) for n,x in models.items()])
        print('stabilized q',q,'total partition types',count)
        print('class partition by round:')
        for i,groups in enumerate(history):print(i,groups)
        pred=[(n,) for n in range(3,2*k)] + [tuple(range(2*k,lim+1))]
        assert sorted(map(tuple,history[-1]))==sorted(pred),(history[-1],pred)
        print('CLASSIFICATION_OK',k)
if __name__=='__main__':run()
