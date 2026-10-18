#!/usr/bin/env python3
"""Exact finite tests for rough-approximation fiber multiplicities on paths."""
from collections import defaultdict

M = {
    '0': ((1,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0)),
    '1': ((0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,1)),
    '*': ((0,1,0,0),(0,0,1,1),(1,1,0,0),(0,0,1,0)),
}
END = {'0': (1,0,0,0), '1': (0,0,0,1), '*': (0,1,1,0)}

def fib(k):
    a,b=0,1
    for _ in range(k):
        a,b=b,a+b
    return a

def approx_output(n, bits):
    symbols=[]
    for i in range(n):
        w=[(bits >> j)&1 for j in range(max(0,i-1),min(n,i+2))]
        symbols.append('0' if not any(w) else '1' if all(w) else '*')
    return ''.join(symbols)

def transfer_count(y):
    assert len(y)>=2
    v=list(END[y[0]])
    for s in y[1:-1]:
        v=[sum(v[i]*M[s][i][j] for i in range(4)) for j in range(4)]
    return sum(v[i]*END[y[-1]][i] for i in range(4))

if __name__ == '__main__':
    checked_words=checked_fibers=0
    for n in range(2,15):
        fibers=defaultdict(int)
        for bits in range(1<<n):
            fibers[approx_output(n,bits)]+=1
        checked_words+=1<<n
        for y, count in fibers.items():
            assert transfer_count(y)==count, (n,y,transfer_count(y),count)
        checked_fibers+=len(fibers)
        largest=max(fibers.values())
        winners=[y for y, count in fibers.items() if count==largest]
        assert largest==2*fib(n-1), (n,largest,2*fib(n-1))
        assert winners==['*'*n], (n,winners)
        print('CASE',n,'distinct_rough_outputs',len(fibers),'largest_fiber',largest,'unique_all_uncertain',True,'PASS')
    assert transfer_count('01010')==0
    assert transfer_count('0*1*0')==0
    print('VERIFY_OK','original_subsets',checked_words,'individual_fibers',checked_fibers,'transition_counts=PASS','unique_extremum=PASS')
