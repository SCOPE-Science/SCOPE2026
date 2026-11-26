# Independent mathematical audit

## correctness

PASS

The defender of the least-index zero in B necessarily sees every B-zero, and the defender of the greatest-index zero in A sees every A-zero. Thus for positive-support sizes α,β, the weight is at least g_n(α)+g_n(β) with g_n(t)=ceil((n+t)/2), also when one side has no zeros. A zero support on one side forces full support on the other, giving weight at least n+ceil(n/2); this is strictly above the target for odd n≥3, and for even n it ties at n=4 and exceeds the target thereafter. With both supports nonempty the bound gives n+1 for odd n and n+2 for even n. For odd n equality forces one positive on each side. If a1 is not the positive A-vertex, b1 must be the sole positive B-vertex, forcing all a2,…,an positive and contradicting n≥3; duality forces bn. Equality fixes their labels. The endpoint function attains both bounds, and for n=2q the alternate label q at a2 covers exactly the n−2 B-zeros, while q+1 at bn covers all n−1 A-zeros; its weight is n+2. All labels respect the cap. An independent support/composition enumeration checked 449,345 labelings at orders 3–7, with values 4,6,6,8,8 and respective optimizer counts 1,28,1,49,1.

## originality

PASS

The standard invariant and its label rule are prior. The supported distinct claim is the exact parity-dependent strong Roman value on the staircase half-graph family together with the exact uniqueness split. The strongest same-graph indexed result has a different domination constraint, and the strongest same-invariant indexed result has incompatible graph hypotheses. The inspected primary works do not provide this specialization.

## value

PASS

The half graph is the canonical nested-neighborhood bipartite family, so it tests how a neighbor-load constraint changes both the exact optimum and its stability under changing graph order. The parity law distinguishes consecutive orders and, more substantially, determines when the two extreme defenders are forced versus when the same minimum admits different support patterns. This exact invariant and optimizer split are independently useful benchmarks rather than a small-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
