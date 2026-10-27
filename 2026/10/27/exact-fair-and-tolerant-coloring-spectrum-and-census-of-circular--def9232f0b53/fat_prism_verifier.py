#!/usr/bin/env python3
"""Independent finite checks for fair-and-tolerant colorings of circular ladders.
Public reproducibility program. No external packages required.
"""
from itertools import product


def is_local_fat(colors, center_index, k):
    n=len(colors)
    a,b=colors[center_index]
    prev=colors[(center_index-1)%n]
    nextc=colors[(center_index+1)%n]
    for own, vertical, left, right in ((a,b,prev[0],nextc[0]),(b,a,prev[1],nextc[1])):
        counts=[int(left==t)+int(right==t)+int(vertical==t) for t in range(k)]
        away=[counts[t] for t in range(k) if t!=own]
        if len(set(away))!=1 or away[0]==0:
            return False
        if counts[own]+sum(away)!=3:
            return False
    return True


def count_by_backtracking(n,k):
    # Enumerates all column words with pruning. The state generator does NOT
    # use the two-step structural recurrence established in the proof.
    states=list(product(range(k),repeat=2))
    counts=0
    valid=[]
    def recurse(word):
        nonlocal counts
        if len(word)==n:
            if is_local_fat(word,0,k) and is_local_fat(word,n-1,k):
                counts+=1
                if n<=8:valid.append(tuple(word))
            return
        for c in states:
            word.append(c)
            if len(word)<3 or is_local_fat(word,len(word)-2,k):
                recurse(word)
            word.pop()
    recurse([])
    return counts,valid


def expected(n,k):
    if k==4:return 24 if n%4==0 else 0
    if k==3:return (36 if n%6==0 else 6) if n%3==0 else 0
    raise ValueError(k)


def test():
    evaluated=0
    for n in range(3,21):
        for k in (3,4):
            count,valid=count_by_backtracking(n,k)
            assert count==expected(n,k),(n,k,count,expected(n,k))
            evaluated+=1
            for word in valid:
                assert all(is_local_fat(word,i,k) for i in range(n))
                step=3 if k==3 else 2
                assert all(word[(i+step)%n]==tuple(reversed(word[i])) for i in range(n)), (n,k,word)
    # A direct generic test, without using the dichotomy, for the lower bound k=2.
    for n in range(3,101):
        word=[(0,1)]*n
        assert all(is_local_fat(word,i,2) for i in range(n))
    print('VERIFY_OK local_census_cases='+str(evaluated)+' prism_orders=3..20'+
          ' two_color_constructions=98')
if __name__=='__main__':test()
