"""Finite exact remanent-language state certificate for four odd cycles.
All vertices are both initial and accepting; + moves along directed edges, - against them.
Python standard library only.
"""
from collections import deque

EXPECTED = {3:(6,6),5:(24,18),7:(230,102),9:(8936,1098)}
WITNESSES = [(3,5,'++-++'),(5,7,'++-+-++'),(7,9,'++-+-+-++')]

def oriented_neighbors(n,mask):
    edges=[]
    for i in range(n):
        j=(i+1)%n
        edges.append((i,j) if mask & (1<<i) else (j,i))
    return edges

def path_exists(n,word,mask):
    s=(1<<n)-1
    for ch in word:
        t=0
        for u,v in oriented_neighbors(n,mask):
            if ch=='+':
                if s>>u &1:t|=1<<v
            else:
                if s>>v &1:t|=1<<u
        s=t
        if not s:return False
    return True

def rem_accept(n,word):
    return all(path_exists(n,word,m) for m in range(1<<n))

def evaluate(n):
    allmask=(1<<n)-1
    # For each orientation, compute letter actions on all vertex subsets.
    components=[]
    for mask in range(1<<n):
        per_vertex=[[0,0] for _ in range(n)]
        for u,v in oriented_neighbors(n,mask):
            per_vertex[u][0] |= 1<<v
            per_vertex[v][1] |= 1<<u
        actions=[(0,0)]
        for s in range(1,1<<n):
            bit=s & -s
            k=bit.bit_length()-1
            old=actions[s^bit]
            actions.append((old[0] | per_vertex[k][0],old[1] | per_vertex[k][1]))
        components.append(actions)
    start=(allmask,)*(1<<n)
    states=[start]
    ids={start:0}
    q=deque([0])
    transitions=[]
    while q:
        i=q.popleft()
        cur=states[i]
        row=[]
        for letter in (0,1):
            if cur is None:
                dest=None
            else:
                v=[component[cur[h]][letter] for h,component in enumerate(components)]
                dest=tuple(v) if all(v) else None
            if dest not in ids:
                ids[dest]=len(states)
                states.append(dest)
                q.append(ids[dest])
            row.append(ids[dest])
        transitions.append(tuple(row))
    # Moore's theorem: each refinement splits exactly the pairs separated by
    # suffixes of length <= the current iteration depth.
    colors=[int(s is not None) for s in states]
    refinements=0
    while True:
        signatures=[(colors[i],colors[t[0]],colors[t[1]]) for i,t in enumerate(transitions)]
        labels={v:j for j,v in enumerate(sorted(set(signatures)))}
        revised=[labels[v] for v in signatures]
        assert len(set(revised)) >= len(set(colors))
        refinements+=1
        if len(set(revised))==len(set(colors)):
            colors=revised
            break
        colors=revised
    # Verify quotient transitions and final output are class-invariant.
    signatures={}
    for i,row in enumerate(transitions):
        outcome=(states[i] is not None, colors[row[0]],colors[row[1]])
        if colors[i] in signatures:
            assert signatures[colors[i]]==outcome
        signatures[colors[i]]=outcome
    count=len(set(colors))
    assert (len(states),count)==EXPECTED[n],(n,len(states),count)
    assert not any(s is None for s in states[:1])
    assert sum(1 for s in states if s is None)==1
    print(f'C{n}: oriented={1<<n}, reachable={len(states)}, minimum_complete_DFA={count}, Moore_refinements={refinements}')
    return len(states),count

if __name__=='__main__':
    for n in EXPECTED:evaluate(n)
    for a,b,word in WITNESSES:
        assert rem_accept(a,word),('not accepted',a,word)
        assert not rem_accept(b,word),('not rejected',b,word)
        bad=(2**(b-1)-1)//3
        assert not path_exists(b,word,bad),('bad mask',b,bad)
        print(f'C{a} versus C{b}: {word!r} accepted for all lower orientations, rejected by higher orientation mask {bad}')
    print('ALL CHECKS PASS')
