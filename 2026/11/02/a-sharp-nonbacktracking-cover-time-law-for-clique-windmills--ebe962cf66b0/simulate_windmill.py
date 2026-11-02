#!/usr/bin/env python3
"""Seeded finite-sample illustration for vertex-cover times on clique windmills."""
from random import Random
from math import log

def cover(n,m,nonbacktracking,rng):
    visited=[False]*(n*m);remaining=n*m
    pos=-1; prev=None;step=0
    while remaining:
        if pos==-1: choices=range(n*m)
        else:
            part=pos//m
            choices=list(range(part*m,(part+1)*m))+[-1]
            choices.remove(pos)
        if nonbacktracking and prev is not None:
            choices=[v for v in choices if v!=prev]
        nxt=choices[rng.randrange(len(choices))]
        prev,pos=pos,nxt
        step+=1
        if nxt>=0 and not visited[nxt]:
            visited[nxt]=True;remaining-=1
    return step

def main():
    rng=Random(91737)
    for m,n,rep in [(3,60,120),(3,160,80),(4,60,120),(4,160,80)]:
        values=[]
        for nb in (False,True):
            sample=[cover(n,m,nb,rng) for _ in range(rep)]
            mean=sum(sample)/rep
            q=(m+2 if nb else m+1)/(2*m)
            predicted=(m+1)*n/q*(log(n*m)+0.5772156649015329)
            values.append((round(mean),round(predicted),round(mean/predicted,3)))
        print('m,n,reps=',m,n,rep,'simple versus nonbacktracking (sample mean, Gumbel first-order mean, ratio):',values)
if __name__=='__main__':main()
