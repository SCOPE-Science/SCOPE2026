#!/usr/bin/env python3
"""Exhaustive small-formula and sampled larger-team checks for guarded witnesses."""
import itertools
import random
from functools import lru_cache

LEAVES = tuple([('lit', i, bit) for i in range(2) for bit in (0, 1)] + [('ne',),('top',),('bot',)])

@lru_cache(None)
def flat(f, a):
    tag=f[0]
    if tag=='lit': return (a>>f[1])&1==f[2]
    if tag=='ne' or tag=='top':return True
    if tag=='bot':return False
    if tag=='and':return flat(f[1],a) and flat(f[2],a)
    if tag=='or':return flat(f[1],a) or flat(f[2],a)
    raise AssertionError(f)

@lru_cache(None)
def eval_bruteforce(f, team):
    tag=f[0]
    if tag=='ne':return team!=0
    if tag=='top':return True
    if tag=='bot':return team==0
    if tag=='lit':return all(flat(f,a) for a in range(8) if team&(1<<a))
    if tag=='and':return eval_bruteforce(f[1],team) and eval_bruteforce(f[2],team)
    if tag=='or':
        # Enumerate every pair of subteams Y,Z with Y union Z = team.
        y=team
        while True:
            mandatory=team & ~y
            both=y
            while True:
                z=mandatory|both
                if eval_bruteforce(f[1],y) and eval_bruteforce(f[2],z):return True
                if both==0:break
                both=(both-1)&y
            if y==0:break
            y=(y-1)&team
        return False
    raise AssertionError(f)

def guarded(f):
    # Returns flattened classical formula f with ne replaced by top and
    # classical formulas whose value must occur in at least one team row.
    tag=f[0]
    if tag=='ne': return ('top',), (('top',),)
    if tag in ('lit','top','bot'):return f, ()
    l,wl=guarded(f[1]);r,wr=guarded(f[2])
    if tag=='and':return ('and',l,r), wl+wr
    if tag=='or':return ('or',l,r), tuple(('and',l,w) for w in wl)+tuple(('and',r,w) for w in wr)
    raise AssertionError(f)

def eval_guarded(f,team):
    c,needs=guarded(f)
    if any(not flat(c,a) for a in range(8) if team&(1<<a)):return False
    return all(any(flat(w,a) for a in range(8) if team&(1<<a)) for w in needs)

def check(f,team):
    truth=eval_bruteforce(f,team)
    form=eval_guarded(f,team)
    if truth!=form:raise AssertionError(('normal_form',f,team,truth,form))
    c,_=guarded(f)
    candidate=sum(1<<a for a in range(8) if team&(1<<a) and flat(c,a))
    has_good_subteam=False
    sub=team
    while True:
        if eval_bruteforce(f,sub):has_good_subteam=True;break
        if sub==0:break
        sub=(sub-1)&team
    if has_good_subteam!=eval_bruteforce(f,candidate):
        raise AssertionError(('largest_subteam',f,team))
    if has_good_subteam and (candidate&~team or not eval_bruteforce(f,candidate)):
        raise AssertionError(('canonical',f,team))

# Enumerate all syntax trees with at most two binary connectives.
parts={0:LEAVES}
for binary_count in (1,2):
    level=[]
    for left_nodes in range(binary_count):
        right_nodes=binary_count-1-left_nodes
        for left in parts[left_nodes]:
            for right in parts[right_nodes]:
                for op in ('and','or'):
                    level.append((op,left,right))
    parts[binary_count]=tuple(level)
checked=0
for level in parts.values():
    for f in level:
        for team in range(16):
            check(f,team);checked+=1
print('EXHAUSTIVE_2_VARIABLES_NODES_LE_2',sum(map(len,parts.values())),'FORMULAS',checked,'FORMULA_TEAM_PAIRS')

rng=random.Random(20261008)
leaf3=LEAVES+(('lit',2,0),('lit',2,1))
def randformula(depth):
    if depth==0 or rng.random()<0.23:return rng.choice(leaf3)
    return (rng.choice(('and','or')),randformula(depth-1),randformula(depth-1))
for k in range(100):
    f=randformula(4)
    for _ in range(48):check(f,rng.randrange(256))
print('RANDOM_THREE_VARIABLE_CHECKS',100*48)
print('VERIFY_OK')
