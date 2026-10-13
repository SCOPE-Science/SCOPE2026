#!/usr/bin/env python3
"""Exhaustive shortest simultaneous reset words for pairs of cycle-collapse DFAs."""
import csv
from collections import deque
from pathlib import Path

MAX_N=11

def image(mask, size, letter):
    if letter == 'a':
        return ((mask << 1) & ((1 << size) - 1)) | (mask >> (size - 1))
    if mask & (1 << (size - 1)):
        return (mask & ~(1 << (size - 1))) | 1
    return mask

def solve(m,n):
    start=((1 << m)-1,(1 << n)-1)
    todo=deque([start]); prev={start:None}
    found=None
    while todo:
        state=todo.popleft()
        if state[0].bit_count()==state[1].bit_count()==1:
            found=state
            break
        for letter in ('a','b'):
            nxt=(image(state[0],m,letter),image(state[1],n,letter))
            if nxt not in prev:
                prev[nxt]=(state,letter)
                todo.append(nxt)
    assert found is not None
    letters=[];s=found
    while s!=start:
        predecessor,letter=prev[s]
        letters.append(letter)
        s=predecessor
    word=''.join(reversed(letters))
    assert len(word)>0
    for size in (m,n):
        states=(1 << size)-1
        for c in word:
            states=image(states,size,c)
        assert states.bit_count()==1
    # All paths to a goal below this BFS depth were checked before goal dequeue.
    return len(word),word,len(prev)

def main():
    lines=[]
    for n in range(3,MAX_N+1):
        for m in range(2,n):
            depth,word,visited=solve(m,n)
            lines.append({'m':m,'n':n,'length':depth,'word':word,'visited_before_goal':visited})
            print(m,n,depth,visited,flush=True)
    outfile=Path(__file__).with_name('table_python.csv')
    with outfile.open('w',newline='',encoding='utf-8') as h:
        wr=csv.DictWriter(h,fieldnames=['m','n','length','word','visited_before_goal'])
        wr.writeheader();wr.writerows(lines)
    print('VERIFY_OK PYTHON',len(lines))
if __name__=='__main__': main()
