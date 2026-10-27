#!/usr/bin/env python3
"""Independent finite transition certificate for two Petersen graph families.
Python 3, standard library only. All assertions are exact.
"""

def bit(tile, side):
    return (tile >> side) & 1


def graph(k):
    # A state is 2k consecutive columns, each column a pair of bits.
    length = 2*k
    size = 4**length
    result = [[] for _ in range(size)]
    for state in range(size):
        cols = [(state >> (2*j)) & 3 for j in range(length)]
        for nxt in range(4):
            block = cols + [nxt]
            j = k
            a, b = bit(block[j], 0), bit(block[j], 1)
            outer_opposite = sum(a != bit(block[j+d], 0) for d in (-1, 1)) + (a != b)
            inner_opposite = sum(b != bit(block[j+d], 1) for d in (-k, k)) + (a != b)
            if outer_opposite == inner_opposite == 1:
                destination = state // 4 + (nxt << (2*(length-1)))
                result[state].append(destination)
    return result


def components(adj):
    # Kosaraju: explicit whole-graph SCC enumeration.
    n = len(adj)
    incoming = [[] for _ in range(n)]
    for v in range(n):
        for w in adj[v]: incoming[w].append(v)
    done = [False]*n
    order=[]
    for v in range(n):
        if done[v]: continue
        todo=[(v,0)]
        done[v]=True
        while todo:
            z,j=todo[-1]
            if j<len(adj[z]):
                w=adj[z][j]
                todo[-1]=(z,j+1)
                if not done[w]:
                    done[w]=True
                    todo.append((w,0))
            else:
                order.append(z)
                todo.pop()
    done=[False]*n
    groups=[]
    for v in reversed(order):
        if done[v]: continue
        stack=[v];done[v]=True;group=[]
        while stack:
            z=stack.pop();group.append(z)
            for w in incoming[z]:
                if not done[w]: done[w]=True;stack.append(w)
        groups.append(group)
    return groups


def cyclic_components(adj):
    result=[]
    for comp in components(adj):
        inside=set(comp)
        edges=[(v,w) for v in comp for w in adj[v] if w in inside]
        if len(comp)==1:
            if (comp[0],comp[0]) in edges:
                result.append([comp[0]])
        else:
            assert len(edges)==len(comp), (comp, edges)
            assert all(sum(w in inside for w in adj[v])==1 for v in comp)
            assert all(sum(v in adj[w] for w in comp)==1 for v in comp)
            result.append(sorted(comp))
    return sorted(result,key=lambda c:(len(c),c))


def independent_count(n,k):
    # Brute force the *original vertex-neighbour conditions*, independently
    # of states or graph enumeration. Enumerates all 2^(2n) labelings.
    count=0
    for a in range(1<<n):
        for b in range(1<<n):
            valid=True
            for i in range(n):
                x=(a>>i)&1
                y=(b>>i)&1
                if ((x!=((a>>((i-1)%n))&1))+
                    (x!=((a>>((i+1)%n))&1))+(x!=y))!=1:
                    valid=False;break
                if ((y!=((b>>((i-k)%n))&1))+
                    (y!=((b>>((i+k)%n))&1))+(x!=y))!=1:
                    valid=False;break
            if valid:count+=1
    return count


def verify():
    cases=[(1, {1:2,4:1}, 10, range(3,9)),
           (2, {1:2,5:2}, 160, range(5,9))]
    for k,expected_cycles,expected_edges,nvalues in cases:
        adj=graph(k)
        assert sum(map(len,adj))==expected_edges
        cyclic=cyclic_components(adj)
        sizes={}
        for c in cyclic:sizes[len(c)]=sizes.get(len(c),0)+1
        assert sizes==expected_cycles, (k,sizes,cyclic)
        # Directed SCC certificates imply all closed walks consist of complete
        # turns around one directed simple cycle, each contributing its length.
        for n in list(nvalues)+[20,25]:
            expected=sum(length*quantity for length,quantity in expected_cycles.items() if n%length==0)
            closed_walk_count=0
            # Dynamic enumeration of closed walks (entire state graph).
            for start in set(v for c in cyclic for v in c):
                vcounts={start:1}
                for _ in range(n):
                    nextcounts={}
                    for v,count in vcounts.items():
                        for w in adj[v]: nextcounts[w]=nextcounts.get(w,0)+count
                    vcounts=nextcounts
                closed_walk_count+=vcounts.get(start,0)
            assert closed_walk_count==expected, (k,n,expected,closed_walk_count)
            if n in nvalues:
                brute=independent_count(n,k)
                assert brute==expected, (k,n,expected,brute)
        print('GP(n,%d): %d transitions, cyclic components %s, independent direct counts OK'
              %(k,expected_edges,cyclic))
    print('VERIFY_OK')

if __name__=='__main__':verify()
