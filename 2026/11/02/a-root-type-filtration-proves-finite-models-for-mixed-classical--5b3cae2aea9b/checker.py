"""Finite tests for root-type / local-type filtration of concrete mixed models.

No inference about arbitrary models is drawn from this finite test.
"""
from __future__ import annotations
from itertools import product
import random
RNG=random.Random(314159)
P=('p',);Q=('q',);BOT=('bot',);TOP=('top',)

def forms(depth):
    x={P,Q,BOT,TOP}
    for _ in range(depth):
        small=sorted(x,key=str)
        x=set(x)
        for a in small:
            x.add(('box',a))
        for a in small[:8]:
            for b in small[:8]:
                for op in ('and','or','imp'):
                    x.add((op,a,b))
    return tuple(sorted(x,key=str))

def subs(t):
    s={t}
    if len(t)==2:
        s|=subs(t[1])
    if len(t)==3:
        s|=subs(t[1])|subs(t[2])
    return s

class Model:
    def __init__(self,orders,values,edges):
        self.orders,self.values,self.edges=orders,values,edges
        self.n=len(orders)
    def ev(self,w,x,f):
        z=f[0]
        if z=='bot': return False
        if z=='top': return True
        if z in ('p','q'):return z in self.values[w][x]
        if z=='and': return self.ev(w,x,f[1]) and self.ev(w,x,f[2])
        if z=='or': return self.ev(w,x,f[1]) or self.ev(w,x,f[2])
        if z=='imp': return all(not self.ev(w,y,f[1]) or self.ev(w,y,f[2]) for y in range(len(self.orders[w])) if self.orders[w][x][y])
        if z=='box':return all(self.ev(v,0,f[1]) for v in range(self.n) if (w,v) in self.edges)
        raise ValueError(z)

def mk():
    num=RNG.randrange(1,5)
    orders=[];values=[]
    for w in range(num):
        m=RNG.randrange(1,5)
        # Transitive closures of random acyclic orientation by index.
        o=[[a==b or (a<b and RNG.random()<.35) for b in range(m)] for a in range(m)]
        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if o[i][k] and o[k][j]:o[i][j]=True
        # ensure root 0 <= all points
        for j in range(m):o[0][j]=True
        vals=[]
        seed=[{p for p in ('p','q') if RNG.random()<.5} for i in range(m)]
        for i in range(m):
            vals.append({p for j in range(m) if o[j][i] for p in seed[j]})
        orders.append(o);values.append(vals)
    edges={(a,b) for a in range(num) for b in range(num) if RNG.random()<.4}
    return Model(orders,values,edges)

def filt(model,formula,designated_component=0):
    sigma=tuple(sorted(subs(formula),key=str))
    pattern={(w,x):frozenset(g for g in sigma if model.ev(w,x,g))
             for w in range(model.n) for x in range(len(model.orders[w]))}
    roots={}
    # make designated root-type represented by its actual component
    for w in [designated_component]+[w for w in range(model.n) if w!=designated_component]:
        roots.setdefault(pattern[w,0],w)
    keys=list(roots)
    neworders=[];newvalues=[];localtypes=[]
    for k in keys:
        oldw=roots[k]
        patterns=[]
        for x in range(len(model.orders[oldw])):
            if pattern[oldw,x] not in patterns: patterns.append(pattern[oldw,x])
        # guarantee root at index 0
        assert patterns[0]==k
        localtypes.append(patterns)
        neworders.append([[t<=u for u in patterns] for t in patterns])
        newvalues.append([{atom for atom in ('p','q') if (atom,) in t} for t in patterns])
    newedges=set()
    for i,k in enumerate(keys):
        oldw=roots[k]
        for g in sigma:
            if g[0]!='box' or g in k: continue
            witness=next((v for v in range(model.n) if (oldw,v) in model.edges and not model.ev(v,0,g[1])),None)
            assert witness is not None
            newedges.add((i,keys.index(pattern[witness,0])))
    new=Model(neworders,newvalues,newedges)
    for i,parts in enumerate(localtypes):
        for j,t in enumerate(parts):
            for g in sigma:
                assert new.ev(i,j,g)==(g in t),(formula,i,j,g)
    # original counterexample at chosen (component,node) types preserved:
    return new,sigma,keys,localtypes,pattern

def main():
    ff=forms(1)
    cases=0
    for _ in range(250):
        m=mk()
        samples=RNG.sample(ff,min(len(ff),20))
        for f in samples:
            new,sigma,keys,types,pattern=filt(m,f)
            assert new.ev(0,0,f)==m.ev(0,0,f)
            # Every local node of the designated component retains its Sigma type.
            for x in range(len(m.orders[0])):
                j=types[0].index(pattern[0,x])
                assert new.ev(0,j,f)==m.ev(0,x,f)
            assert new.n <= 2**len(sigma)
            assert sum(len(x) for x in types) <= 2**(2*len(sigma))
            cases+=1
    print('ALL_CHECKS_OK randomized_models=250 formula_model_cases=%d root_local_truth_lemmas=all'%cases)
if __name__=='__main__':main()
