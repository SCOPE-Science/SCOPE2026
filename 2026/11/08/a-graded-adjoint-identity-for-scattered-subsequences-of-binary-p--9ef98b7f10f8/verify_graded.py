#!/usr/bin/env python3
"""Independent graded palindromic-source subsequence transform checks."""
from itertools import product


def plus(a,b):
    n=max(len(a),len(b));return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]

def mul(a,b):
    res=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):res[i+j]+=x*y
    return res

def scale(a,k):return [k*x for x in a]

def shift(a):return [0]+a

def subtract(a,b):return plus(a,scale(b,-1))

def trim(a):
    while a and not a[-1]:a.pop()
    return a or [0]

def graded(word):
    # Conventional distinct-subsequence DP on the entire word (independent of transform).
    length=len(word);e=[[0]*(length+1),[0]*(length+1)]
    for char in word:
        total=[(int(i==0)+e[0][i]+e[1][i]) for i in range(length+1)]
        e[int(char)]=[0]+total[:-1]
    return trim(plus(e[0],e[1]))

def transform(half,center=None):
    A=[0]; B=[0]
    for c in half:
        S=plus(plus(A,B),[1])
        if c=='0':A=shift(S)
        else:B=shift(S)
    # v=(A,B,1), H symmetric: diag t-1, offdiag t (and H_33=0).
    # t P_even=(t-1)(A^2+B^2)+2t A B+2t(A+B).
    Q=plus(mul(subtract([0,1],[1]),plus(mul(A,A),mul(B,B))),scale(shift(plus(mul(A,B),plus(A,B))),2))
    if center is not None:
        # t(P_odd-P_even) = (new f_center - old f_center) * (H v)_center.
        if center=='0':
            d=subtract(shift(plus(plus(A,B),[1])),A)
            row=plus(plus(mul(subtract([0,1],[1]),A),shift(B)),[0,1])
        else:
            d=subtract(shift(plus(plus(A,B),[1])),B)
            row=plus(plus(shift(A),mul(subtract([0,1],[1]),B)),[0,1])
        Q=plus(Q,mul(d,row))
    assert Q[0]==0, Q
    return trim(Q[1:]),A,B

def run():
    even=odd=bruteforce=0
    for m in range(0,13):
        for tup in product('01',repeat=m):
            u=''.join(tup)
            P,A,B=transform(u)
            assert P==graded(u+u[::-1]),(u,P,graded(u+u[::-1]))
            even+=1
            for c in '01':
                P,_,_=transform(u,c)
                assert P==graded(u+c+u[::-1]),(u,c,P,graded(u+c+u[::-1]))
                odd+=1
            if m<=6:
                # Independent subset enumeration of distinct strings, for one representative.
                for c in [None,'0','1']:
                    w=u+('' if c is None else c)+u[::-1]
                    S={''}
                    for z in w:S|={s+z for s in tuple(S)}
                    hist=[sum(len(s)==j for s in S) for j in range(1,len(w)+1)]
                    pred=transform(u,c)[0]
                    assert hist==pred[1:len(w)+1], (u,c,hist,pred)
                    bruteforce+=1
    print('VERIFY_OK')
    print('all_even_halves_length_0_through_12=',even)
    print('all_odd_halves_and_both_centers_length_0_through_12=',odd)
    print('independent_set_oracle_cases=',bruteforce)
    print('example_even_0110=',graded('0110'))
    print('example_odd_010=',graded('010'))

if __name__=='__main__':run()
