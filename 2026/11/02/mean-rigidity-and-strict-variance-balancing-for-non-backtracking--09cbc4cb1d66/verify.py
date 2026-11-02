"""Exact finite consistency checks for non-backtracking cover times on cycle bouquets.

The checks independently solve the complete directed-edge/visited-vertex
Markov chain, rather than using the petal-chain reduction of the proof.
All operations use Python standard-library fractions only.
"""
from fractions import Fraction as F
from itertools import product


def linear(A, b):
    n = len(b)
    z = [[F(y) for y in A[i]] + [F(b[i])] for i in range(n)]
    for c in range(n):
        pivot = next((r for r in range(c, n) if z[r][c]), None)
        if pivot is None:
            raise ArithmeticError('noninvertible reachable transient block')
        z[c], z[pivot] = z[pivot], z[c]
        v = z[c][c]
        z[c] = [x / v for x in z[c]]
        for r in range(n):
            if r != c and z[r][c]:
                v = z[r][c]
                z[r] = [x-v*y for x, y in zip(z[r], z[c])]
    return [x[-1] for x in z]


def graph(lengths):
    edges = []
    n = 1
    for ell in lengths:
        vertices = list(range(n, n + ell-1))
        n += ell-1
        path = [0]+vertices+[0]
        edges += [tuple(sorted((a,b))) for a,b in zip(path, path[1:])]
    adj = [set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    return [sorted(x) for x in adj]


def direct_moments(lengths):
    adj = graph(lengths)
    n = len(adj)
    full = (1 << n)-1
    arcs = [(u,v) for u in range(n) for v in adj[u]]
    moments = {}
    count = 0
    for cardinality in range(n, 1, -1):
        for mask in range(1, 1 << n, 2):  # hub is visited
            if mask.bit_count() != cardinality:
                continue
            states = [(u,v) for u,v in arcs if mask >> u & 1 and mask >> v & 1]
            if not states:
                continue
            if mask == full:
                for uv in states: moments[(mask,uv)] = (F(0),F(0))
                continue
            pos = {s:i for i,s in enumerate(states)}
            size = len(states)
            A = [[F(i==j) for j in range(size)] for i in range(size)]
            b = [F(1) for _ in states]
            steps = []
            for i,(u,v) in enumerate(states):
                choices = [w for w in adj[v] if w != u]
                p = F(1,len(choices))
                nxt = []
                for w in choices:
                    dest = (v,w)
                    newmask = mask | (1<<w)
                    nxt.append((p,newmask,dest))
                    if newmask == mask:
                        A[i][pos[dest]] -= p
                    else:
                        b[i] += p*moments[(newmask,dest)][0]
                steps.append(nxt)
            mean = linear(A,b)
            b2 = [F(1) for _ in states]
            for i,nxt in enumerate(steps):
                for p,newmask,dest in nxt:
                    u = mean[pos[dest]] if newmask == mask else moments[(newmask,dest)][0]
                    v = F(0) if newmask == mask else moments[(newmask,dest)][1]
                    b2[i] += p*(2*u+v)
            second = linear(A,b2)
            for i,state in enumerate(states):
                moments[(mask,state)] = (mean[i],second[i])
                count += 1
    choices = adj[0]
    m = F(1)
    sec = F(1)
    for v in choices:
        mask = 1 | (1<<v)
        u,s = moments[(mask,(0,v))]
        m += u / len(choices)
        sec += (2*u+s) / len(choices)
    return m, sec-m*m, count


def theoretical(lengths):
    k = len(lengths)
    assert k >= 2 and min(lengths) >= 3
    L = sum(lengths)
    Q = sum(x*x for x in lengths)
    H = sum((F(1,j) for j in range(1,k)), F(0))
    H2 = sum((F(1,j*j) for j in range(1,k)), F(0))
    avg = F(L,k)
    EJ = 1 + F(2*k-1,2)*H
    VJ = F((2*k-1)**2,4)*H2 - F(2*k-1,2)*H
    B = F(1,k) + F((2*k-1)*(k-2),2*k*(k-1))*H
    return avg*EJ-1, avg*avg*VJ+(Q-F(L*L,k))*B


def run():
    tested = [
        (3,3),(3,4),(3,5),(4,4),(4,5),
        (3,3,3),(3,3,4),(3,4,4),(4,4,4),
        (3,3,3,3)
    ]
    count = 0
    for lengths in tested:
        observed, variance, states = direct_moments(lengths)
        expected, predicted_variance = theoretical(lengths)
        assert observed == expected, (lengths,observed,expected)
        assert variance == predicted_variance, (lengths,variance,predicted_variance)
        count += 2
        print('PASS',lengths,'mean',expected,'variance',variance,'states',states)
    # Verify balance minimization for fixed total lengths using the exact formula.
    for k in range(2,6):
        for lengths in product(range(3,8), repeat=k):
            L=sum(lengths)
            a,b=divmod(L,k)
            balanced=tuple([a]*(k-b)+[a+1]*b)
            candidate=theoretical(lengths)
            optimal=theoretical(balanced)
            assert candidate[0]==optimal[0]
            assert candidate[1]>=optimal[1]
            count+=2
    print('VERIFY_OK; exact assertions:', count)

if __name__ == '__main__':
    run()
