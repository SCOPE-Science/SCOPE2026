#!/usr/bin/env python3
"""Exact reproducible classification of the periodic-lifting index of the 256 elementary binary cellular automata.

The certificate is finite: for each Wolfram rule close the two labeled four-vertex
relations under composition, then determine the shortest directed cycle in every
relation. Independently repeat in a different representation and spot-check by
enumerating cyclic input rings. No third-party packages are required.
"""
from collections import Counter, deque
from itertools import product
from pathlib import Path
import csv

ID = sum(1 << (5*i) for i in range(4))
assert ID == 0x8421


def mult(a, b):
    ans = 0
    for i in range(4):
        bs = (a >> (4*i)) & 15
        r = 0
        for j in range(4):
            if bs & (1 << j):
                r |= (b >> (4*j)) & 15
        ans |= r << (4*i)
    return ans


def gen(rule):
    out = [0, 0]
    for a, b, c in product(range(2), repeat=3):
        symbol = (rule >> (4*a + 2*b + c)) & 1
        out[symbol] |= 1 << (4 * (2*a+b) + 2*b+c)
    assert (out[0] & out[1]) == 0
    assert (out[0] | out[1]).bit_count() == 8
    return out


def cyclic_index(r):
    q = r
    for k in range(1, 5):
        if q & ID:
            return k
        q = mult(q,r)
    return 0


def close(rule):
    gs=gen(rule)
    seen={ID: None}
    todo=deque([ID])
    while todo:
        p=todo.popleft()
        for digit,g in enumerate(gs):
            q=mult(p,g)
            if q not in seen:
                seen[q]=(p,digit)
                todo.append(q)
    return seen


def word_from(parent, r):
    parts=[]
    while parent[r] is not None:
        p,d=parent[r];parts.append(str(d));r=p
    return ''.join(reversed(parts))


def tuple_gen(rule):
    rows=[[0]*4 for _ in range(2)]
    for triple in range(8):
        ab=triple >> 1
        bc=triple & 3
        symbol=(rule >> triple) & 1
        rows[symbol][ab] |= 1 << bc
    return tuple(map(tuple,rows))


def tuple_compose(x,y):
    rr=[]
    for j in range(4):
        rr.append(0)
        for t in range(4):
            if x[j] & (1<<t): rr[-1] |= y[t]
    return tuple(rr)


def tuple_close(rule):
    gens=tuple_gen(rule)
    start=(1,2,4,8)
    seen={start}
    todo=deque([start])
    while todo:
        x=todo.popleft()
        for g in gens:
            y=tuple_compose(x,g)
            if y not in seen:
                seen.add(y);todo.append(y)
    return seen


def graph_girth(rows):
    # Independent shortest directed cycle by simple-cycle DFS, not matrix powers.
    for length in range(1,5):
        for start in range(4):
            def search(v,k,used):
                if k == length:
                    return v == start
                for nxt in range(4):
                    if rows[v] & (1<<nxt) and (nxt == start if k+1==length else not used&(1<<nxt)):
                        if search(nxt,k+1,used | (1<<nxt)):
                            return True
                return False
            if search(start,0,1<<start):return length
    return 0


def out_rule(rule,inp):
    n=len(inp)
    return tuple((rule >> (4*inp[(i-1)%n]+2*inp[i]+inp[(i+1)%n]))&1 for i in range(n))


def classify():
    groups={1:[],2:[],3:[],4:[]}
    max_size=0
    sizes=[]
    witnesses={}
    for rule in range(256):
        table=close(rule)
        direct={tuple((r>>(4*i))&15 for i in range(4)) for r in table}
        second=tuple_close(rule)
        assert direct == second, ('closure mismatch',rule)
        classes=Counter(cyclic_index(r) for r in table)
        assert sum(classes.values()) == len(table)
        for rows in second:
            r=sum(rows[i]<<(4*i) for i in range(4))
            assert graph_girth(rows) == cyclic_index(r),('cycle mismatch',rule,r)
        k=max((j for j in (1,2,3,4) if classes[j]),default=0)
        assert k in groups
        groups[k].append(rule)
        candidates=[word_from(table,r) for r in table if cyclic_index(r)==k]
        witnesses[rule]=min(candidates,key=lambda w:(len(w),w))
        sizes.append(len(table))
        max_size=max(max_size,len(table))
    return groups, sizes, witnesses


def equivalence_orbits(indices):
    def modify(rule, operation):
        ans=0
        for j in range(8):
            if operation == 'inputflip': jj=j^7
            elif operation == 'mirror': jj=((j&1)<<2)|(j&2)|((j&4)>>2)
            else: jj=j
            bit=(rule>>jj)&1
            if operation == 'outputflip':bit ^=1
            ans |= bit<<j
        return ans
    idx=set(indices)
    out=[]
    while idx:
        r=min(idx)
        orb={r}
        todo=[r]
        while todo:
            x=todo.pop()
            for op in ('inputflip','outputflip','mirror'):
                y=modify(x,op)
                if y not in orb:
                    orb.add(y);todo.append(y)
        assert orb <= idx,('symmetry not invariant',r)
        idx.difference_update(orb)
        out.append(sorted(orb))
    return out


def ring_crosscheck():
    # Verify all n<=7 fixed-ring outputs for same-period lifting against
    # independent cyclic input enumeration; compare to relation cycles.
    count=0
    for rule in range(256):
        gs=gen(rule)
        for n in range(1,8):
            direct={out_rule(rule,inp) for inp in product((0,1),repeat=n)}
            for word in product((0,1),repeat=n):
                r=ID
                for s in word:r=mult(r,gs[s])
                assert ((r&ID)!=0) == (word in direct), ('ring mismatch',rule,n,word)
                count+=1
    return count


def main():
    groups,sizes,wits=classify()
    expected3=[22,30,86,94,104,106,120,122,133,135,149,151,161,169,225,233]
    assert groups[3] == expected3
    assert groups[4] == [90,165]
    assert [len(groups[k]) for k in range(1,5)] == [156,82,16,2]
    assert [len(x) for x in equivalence_orbits(groups[3])] == [4,8,4]
    assert equivalence_orbits(groups[4]) == [[90,165]]
    assert wits[90] == '1' and wits[165]=='0'
    assert wits[22] == wits[30] == wits[94] == '1'
    assert max(map(len,wits.values())) == 3
    third=[r for r in range(256) if len(wits[r])==3]
    assert third == [41,97,105,107,121,134,148,150,158,214]
    rows=[]
    for k,rules in groups.items():
        for rule in rules:
            rows.append({'rule':str(rule),'optimal_multiplier':str(k),
                         'shortest_witness':wits[rule] if k>1 else '',
                         'relation_semigroup_size':str(sizes[rule])})
    rows.sort(key=lambda x:int(x['rule']))
    expected_path=Path(__file__).with_name('classification.csv')
    with expected_path.open(newline='',encoding='utf-8') as f:
        data=list(csv.DictReader(f))
    assert rows == data, 'full classification table mismatch' 
    for k, rules in groups.items():
        for rule in rules:
            assert len(close(rule))==sizes[rule]
    rings=ring_crosscheck()
    print('VERIFY_OK: 256 rules; optimal multipliers 1/2/3/4 = 156/82/16/2;'
          ' exceptional triple rules 16 in orbits 4/8/4; quadruple 90/165;'
          ' sharp witness output period <=3 (10 rules first require 3);'
          ' max relation-semigroup size',max(sizes),';', rings,
          'independently checked cyclic image words for n<=7')

if __name__=='__main__': main()
