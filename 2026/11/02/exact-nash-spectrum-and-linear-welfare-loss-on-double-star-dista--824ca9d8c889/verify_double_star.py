"""Exact exhaustive verification of social-distance equilibria on double stars.

Run: python3 check_double_star.py
Uses no third-party modules.
"""
from collections import deque


def partitions(vertices):
    if not vertices:
        yield ()
        return
    first, *rest = vertices
    for pi in partitions(rest):
        yield ((first,),) + pi
        for j, block in enumerate(pi):
            yield pi[:j] + ((first,) + block,) + pi[j+1:]


def oracle(a, b):
    n = a+b+2
    graph = [set() for _ in range(n)]
    for j in range(2, 2+a):
        graph[0].add(j); graph[j].add(0)
    for j in range(2+a,n):
        graph[1].add(j); graph[j].add(1)
    graph[0].add(1); graph[1].add(0)
    def utility(v, block):
        if len(block)==1: return 0
        dist={v:0}
        frontier=deque([v])
        while frontier:
            w=frontier.popleft()
            for z in graph[w].intersection(block):
                if z not in dist:
                    dist[z]=dist[w]+1
                    frontier.append(z)
        if len(dist)!=len(block):return -10**6
        if max(dist.values())>3:return -10**6
        return sum({1:1,2:0,3:-1}[dist[w]] for w in block if w!=v)
    welfare_max=-10**9
    opt=0
    ns=0
    ns_w=[]
    checked=0
    for pi in partitions(list(range(n))):
        checked+=1
        # invalid partitions may be safely discarded for both objectives.
        if any(utility(v,block)<-100 for block in pi for v in block):continue
        sw=sum(utility(v,block) for block in pi for v in block)
        if sw>welfare_max: welfare_max=sw;opt=1
        elif sw==welfare_max:opt+=1
        stable=True
        for block in pi:
            for v in block:
                own=utility(v,block)
                if own<0:
                    stable=False;break
                for newblock in pi:
                    if newblock is block:continue
                    if utility(v, newblock+(v,))>own:
                        stable=False;break
                if not stable:break
            if not stable:break
        if stable:
            ns+=1; ns_w.append(sw)
    return checked,welfare_max,opt,ns, sorted(ns_w)


def theorem(a,b):
    # equilibria: separated hubs; two one-sided hubs with all leaves of one side;
    # and one leaf on each side together with the two hubs.
    return 2*(a+b),a*b+3,sorted([2*(a+b),2*(a+1),2*(b+1)]+[4]*(a*b))

if __name__ == '__main__':
    total=0
    pairs=[(a,b) for a in range(1,5) for b in range(1,5) if a+b<=7]
    pairs.extend([(4,4),(1,6),(2,5)])
    for a,b in pairs:
            count,sw,opt,ns,vals=oracle(a,b)
            expect_sw,expect_ns,expect_vals=theorem(a,b)
            assert (sw,ns,vals)==(expect_sw,expect_ns,expect_vals),(a,b,sw,ns,vals,expect_sw,expect_ns,expect_vals)
            total+=count
            print(f'a={a} b={b} partitions={count} optimum={sw} opt_count={opt} equilibria={ns} worst={min(vals)}')
    print('PASS total partitions:',total)
