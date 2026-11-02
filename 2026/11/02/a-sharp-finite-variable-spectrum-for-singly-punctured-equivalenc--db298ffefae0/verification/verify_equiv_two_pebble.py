#!/usr/bin/env python3
"""Independently classify the FO^2 vertex transition profiles of finite grids.

Only existence of a witness is recorded; multiplicities are intentionally ignored.
This finite diagnostic is separate from the unrestricted proof.
"""
from itertools import product

def grid(m,n,hole):
    return tuple((r,c) for r in range(m) for c in range(n)
                 if not hole or (r,c)!=(0,0))

def predicted(m,n,hole):
    if not hole or min(m,n)>=3: return 'generic'
    if m==2 and n==2:return 'both-singleton'
    if m==2:return 'singleton-column'
    return 'singleton-row'

def classification():
    specs=list(product(range(2,7),range(2,7),(False,True)))
    grids=[grid(*spec) for spec in specs]
    starts=[];acc=0
    for g in grids:starts.append(acc);acc+=len(g)
    colors=[0]*acc
    def compress(seq):
        uniques={t:i for i,t in enumerate(sorted(set(seq)))}
        return [uniques[t] for t in seq]
    def rel(x,y):
        if x==y:return 0
        if x[0]==y[0]:return 1
        if x[1]==y[1]:return 2
        return 3
    nrounds=0
    for iteration in range(100):
        sig=[]
        for g,start in zip(grids,starts):
            for x in g:
                sig.append((colors[start+g.index(x)],tuple(sorted(set(
                    (rel(x,y),colors[start+j]) for j,y in enumerate(g))))))
        new=compress(sig)
        nrounds+=1
        if len(set(new))==len(set(colors)):
            colors=new;break
        colors=new
    else:raise AssertionError('no stabilization')
    fingerprints=[]
    for g,start in zip(grids,starts):
        fingerprints.append(frozenset(colors[start:start+len(g)]))
    for i,sp in enumerate(specs):
        for j in range(i+1,len(specs)):
            expected=predicted(*sp)==predicted(*specs[j])
            observed=bool(fingerprints[i]&fingerprints[j])
            assert observed==expected,(sp,specs[j],expected,observed)
    groups={}
    for sp in specs:groups[predicted(*sp)]=groups.get(predicted(*sp),0)+1
    print('Models:',len(specs),'(full or punctured grids, both dimensions 2..6)')
    print('Unrestricted two-pebble classes:',len(set(fingerprints)))
    print('Phases:',', '.join('%s=%d'%(k,groups[k]) for k in sorted(groups)))
    print('Pairs checked:',len(specs)*(len(specs)-1)//2)
    print('Refinement rounds:',nrounds)
    print('VERIFIED')

if __name__=='__main__':classification()
