"""Exact arithmetic verification for a family of Young reverse-multiple graphs."""
from collections import defaultdict, deque


def proposed(n):
    assert n >= 3
    g = n*n-1
    k = n*n-n-1
    a=n-2
    b=n*a
    c=(n+1)*a
    v={"O":(0,0),"B":(0,b),"A":(a,a),"D":(a,c),
       "E":(b,0),"F":(b,b),"G":(c,a),"H":(c,c)}
    out={
        "O":[("O",(0,0)),("B",(1,k))],
        "B":[("A",(0,a)),("D",(1,g-2))],
        "A":[("E",(a,0)),("F",(a+1,k))],
        "D":[("G",(a,a)),("H",(a+1,g-2))],
        "E":[("O",(k,1)),("B",(k+1,k+1))],
        "F":[("A",(k,n-1)),("D",(k+1,g-1))],
        "G":[("E",(k+a,1)),("F",(g-1,k+1))],
        "H":[("G",(k+a,n-1)),("H",(g-1,g-1))]
    }
    return g,k,v,out


def exact_edges(g,k,state):
    L,R=state
    answer=[]
    for u in range(g):
        numer=k*u+R
        v=numer%g
        Rp=numer//g
        Lp=u+g*L-k*v
        if 0<=Rp<k and 0<=Lp<k:
            answer.append(((Lp,Rp),(v,u)))
    return sorted(answer)


def check(n):
    g,k,v,out=proposed(n)
    assert len(set(v.values()))==8
    assert c_is_k_minus_one(n)
    for label,state in v.items():
        actual=exact_edges(g,k,state)
        expected=sorted((v[dest],digits) for dest,digits in out[label])
        assert actual==expected,(n,label,actual,expected)
    assert exact_edges(g,k,(0,0))==sorted([(v['O'],(0,0)),(v['B'],(1,k))])
    reached={'B'}
    queue=deque(['B'])
    while queue:
        node=queue.popleft()
        for dest,_ in out[node]:
            if dest not in reached:
                reached.add(dest)
                queue.append(dest)
    assert reached==set(v)
    even={label for label,(l,r) in v.items() if l==r}
    odd={label for label in v if any(dest==next((key for key,value in v.items() if value==v[label][::-1]),None) for dest,_ in out[label])}
    assert even=={'O','A','F','H'}
    assert odd=={'O','D','E','H'}
    dp={'B':1}
    for t in range(1,13):
        if t>=2:
            assert sum(dp.get(u,0) for u in even)==2**(t-2),(n,t,'even')
            assert sum(dp.get(u,0) for u in odd)==2**(t-2),(n,t,'odd')
        else:
            assert sum(dp.get(u,0) for u in even)==0
            assert sum(dp.get(u,0) for u in odd)==0
        nd=defaultdict(int)
        for node,ct in dp.items():
            for dest,_ in out[node]:
                nd[dest]+=ct
        dp=nd


def c_is_k_minus_one(n):
    return (n+1)*(n-2)==n*n-n-2

if __name__=='__main__':
    for n in range(3,61):
        check(n)
    print('VERIFY_OK: n=3..60, exhaustive legal digit-pair transitions, 8-state reachability, both pivot classes, exact counts through digit length 25')
