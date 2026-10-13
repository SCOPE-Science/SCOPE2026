from functools import lru_cache
from itertools import product

def build(u,m):
    n=u+m
    adj=[[False]*n for _ in range(n)]
    # U=0..u-1 clique; I=u..u+m-1 independent; all cross edges
    for i in range(n):
        for j in range(i+1,n):
            if i<u or j<u:
                adj[i][j]=adj[j][i]=True
    return adj

def formula(u,m,starter):
    if u%2:
        return (u+1)//2
    q=u//2
    if starter=='A':
        return q + (1 if m%2 else 0)
    return q + (1 if m%2==0 else 0)

def winning_terminal(adj,state,k):
    n=len(adj)
    for v in range(n):
        seen={state[v]}
        for w in range(n):
            if adj[v][w]: seen.add(state[w])
        if len(seen)<k: return False
    return True

def game_win(adj,k,starter):
    n=len(adj)
    @lru_cache(None)
    def rec(state,alice_turn):
        if -1 not in state:
            return winning_terminal(adj,state,k)
        if alice_turn:
            for v,x in enumerate(state):
                if x==-1:
                    for c in range(k):
                        s=list(state); s[v]=c
                        if rec(tuple(s),False): return True
            return False
        else:
            for v,x in enumerate(state):
                if x==-1:
                    for c in range(k):
                        s=list(state); s[v]=c
                        if not rec(tuple(s),True): return False
            return True
    return rec(tuple([-1]*n), starter=='A')

def terminal_criterion(u,m,k):
    adj=build(u,m)
    n=u+m
    checked=0
    for state in product(range(k), repeat=n):
        lhs=winning_terminal(adj,state,k)
        U=state[:u]; I=state[u:]
        good=True
        for c in range(k):
            if c in U: continue
            if not all(x==c for x in I):
                good=False; break
        if lhs!=good:
            raise AssertionError((u,m,k,state,lhs,good))
        checked += 1
    return checked

term=0
for u,m,k in [(1,2,2),(2,2,2),(2,3,2),(3,2,3)]:
    term += terminal_criterion(u,m,k)
profiles=0
for u in range(1,5):
    for m in range(2,6):
        if u+m>8: continue
        adj=build(u,m)
        for starter in ('A','B'):
            expected=formula(u,m,starter)
            # Downward closure is known, but check exact boundary directly.
            if not game_win(adj,expected,starter):
                raise AssertionError(('lower',u,m,starter,expected))
            if game_win(adj,expected+1,starter):
                raise AssertionError(('upper',u,m,starter,expected+1))
            profiles += 1
print(f'ALL CHECKS PASSED; game_profiles={profiles}; terminal_colorings={term}; max_order=8')
