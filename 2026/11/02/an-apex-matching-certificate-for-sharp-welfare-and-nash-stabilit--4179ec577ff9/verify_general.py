"""Exact finite stress-tests for the apex-matching certificate theorem.

Requires networkx. This enumerates connected and disconnected base graphs from
all non-isomorphic graphs on at most seven base vertices with max degree <=2
and with no 3- or 4-cycles. It checks an unbounded theorem only on these finite
instances; the written inequality argument is the infinite proof.
"""
from fractions import Fraction
import networkx as nx


def count_matchings(adj, mask):
    if not mask:
        return 1
    bit = mask & -mask
    u = bit.bit_length() - 1
    others = mask ^ bit
    count = 0
    for v in range(len(adj)):
        if others & (1 << v) and adj[u] & (1 << v):
            count += count_matchings(adj, others ^ (1 << v))
    return count


def verify(H):
    m = len(H)
    if m < 2:
        return
    H = nx.convert_node_labels_to_integers(H)
    base = [0] * m
    for i, j in H.edges:
        base[i] |= 1 << j
        base[j] |= 1 << i
    full = (1 << m) - 1
    cert = 0
    for u in range(m):
        for v in range(u + 1, m):
            if base[u] & (1 << v):
                cert += count_matchings(base, full ^ (1 << u) ^ (1 << v))
    for u in range(m):
        for v in range(u + 1, m):
            for w in range(v + 1, m):
                E = sum(bool(base[a] & (1 << b)) for a,b in ((u,v),(u,w),(v,w)))
                if E == 2:
                    cert += count_matchings(base, full ^ (1 << u) ^ (1 << v) ^ (1 << w))
    n = m + 1
    adj = [0] * n
    for u in range(1, n):
        adj[0] |= 1 << u
        adj[u] |= 1
        adj[u] |= base[u-1] << 1
    lim = 1 << n
    sz = [0]*lim
    welfare = [Fraction(0)]*lim
    for mask in range(1,lim):
        b = mask & -mask
        v = b.bit_length()-1
        t = mask ^ b
        sz[mask] = sz[t] + 1
        edges = sum((adj[i] & mask).bit_count() for i in range(n) if (mask >> i) & 1)//2
        welfare[mask] = Fraction(2*edges,sz[mask])
    target = Fraction(m,2)+1
    count_opt = 0
    maxw = -1
    nash_opt = 0
    def nash(part):
        for coalition in part:
            for u in range(n):
                if not (coalition >> u & 1):
                    continue
                current = Fraction((adj[u]&coalition).bit_count(),sz[coalition])
                for other in part:
                    if other != coalition and Fraction((adj[u]&other).bit_count(),sz[other]+1)>current:
                        return False
        return True
    def walk(rem,part,sw):
        nonlocal maxw,count_opt,nash_opt
        if not rem:
            maxw = max(maxw,sw)
            if sw == target:
                count_opt += 1
                if nash(part):nash_opt+=1
            return
        bit = rem & -rem
        others = rem ^ bit
        sub = others
        while True:
            coal = sub | bit
            walk(rem^coal,part+(coal,),sw+welfare[coal])
            if not sub:break
            sub=(sub-1)&others
    walk(lim-1,(),Fraction(0))
    assert maxw <= target,(m,maxw,target)
    assert (maxw==target)==(cert>0),(m,maxw,cert)
    assert count_opt==cert,(m,count_opt,cert)
    assert nash_opt==cert,(m,nash_opt,cert)
    return bool(cert)


def main():
    eligible = 0
    hits = 0
    for G in nx.graph_atlas_g():
        m = len(G)
        if m < 2 or m > 7:continue
        if max(dict(G.degree()).values()) > 2:continue
        if any(len(c) in (3,4) for c in nx.cycle_basis(G)):continue
        eligible += 1
        hits += bool(verify(G))
    print('eligible_unlabeled_base_graphs',eligible,'matching_certificate_instances',hits)
    print('GENERAL EXACT FINITE STRESS TESTS PASSED')

if __name__ == '__main__': main()
