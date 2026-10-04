#!/usr/bin/env python3
from functools import lru_cache


def graph(n):
    # vertices 0,1 are the singleton parts; 2..n+1 form the independent part.
    N=n+2
    adj=[set() for _ in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            same_big=(i>=2 and j>=2)
            if not same_big:
                adj[i].add(j); adj[j].add(i)
    return adj


def alice_wins_terminal(adj,state):
    # A colour class is dominating iff every vertex is in it or adjacent to it.
    N=len(state)
    for c in (1,2):
        C=[v for v,x in enumerate(state) if x==c]
        if not C:
            return False
        for v in range(N):
            if state[v]==c:
                continue
            if not any(u in adj[v] for u in C):
                return False
    return True


def canon(state):
    # The vertices in the large part are twins, so sort only that tail.
    return (state[0],state[1])+tuple(sorted(state[2:]))


def game_value(n, starter):
    adj=graph(n)
    N=n+2
    @lru_cache(None)
    def win(state,alice_turn):
        state=tuple(state)
        if 0 not in state:
            return alice_wins_terminal(adj,state)
        moves=[]
        seen=set()
        for v,x in enumerate(state):
            if x: continue
            for c in (1,2):
                t=list(state); t[v]=c; t=canon(tuple(t))
                if t in seen: continue
                seen.add(t)
                moves.append(t)
        if alice_turn:
            return any(win(t,False) for t in moves)
        return all(win(t,True) for t in moves)
    return win((0,)*N, starter=='A')


def formula_A(n):
    return n%2==1

def formula_B(n):
    return n%2==0


def ordinary_domatic_is_three(n):
    adj=graph(n)
    N=n+2
    # Explicit three classes: {0}, {1}, and the large part.
    classes=[{0},{1},set(range(2,N))]
    for C in classes:
        for v in range(N):
            if v in C: continue
            if not (adj[v] & C):
                return False
    # delta=2, so ordinary domatic number <= delta+1 = 3.
    return min(len(a) for a in adj)==2


def terminal_characterization(n):
    adj=graph(n); N=n+2
    # Exhaust all 2-colourings and check the structural characterization:
    # Alice wins iff universal vertices have different colours, or they have
    # the same colour and every large-part vertex has the opposite colour.
    for mask in range(1<<N):
        st=tuple(1+((mask>>i)&1) for i in range(N))
        exact=alice_wins_terminal(adj,st)
        u,v=st[0],st[1]
        char=(u!=v) or (u==v and all(x==3-u for x in st[2:]))
        if exact!=char:
            raise AssertionError((n,st,exact,char))


def main():
    cases=0
    for n in range(2,8):
        terminal_characterization(n)
        A=game_value(n,'A')
        B=game_value(n,'B')
        assert A==formula_A(n), (n,A)
        assert B==formula_B(n), (n,B)
        assert ordinary_domatic_is_three(n)
        cases+=1
    print(f"ALL CHECKS PASSED; n_range=2..7; parameter_cases={cases}; terminal_colourings={sum(2**(n+2) for n in range(2,8))}")

if __name__=='__main__':
    main()
