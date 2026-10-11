# Independent mathematical audit

## correctness

PASS

Using the standard generator columns \(g_x=(1,x)^T\), a minimal nontrivial recovery set for a target has odd cardinality and therefore at least three. A recovery triple, after translating by the target, is exactly the three nonzero vectors of a two-dimensional subspace. For odd \(m\), the exact partial two-spread theorem of Năstase--Sissokho at \(q=2,t=2,r=1\) gives \((2^m-5)/3\) disjoint planes. The upper bound does not assume locality three: if one more nontrivial disjoint recovery set existed, counting forces every such set to be a triple and leaves exactly one nonzero vector uncovered; XOR of every plane triple and of all nonzero vectors is zero, forcing the leftover vector to be zero, a contradiction. A fresh independent exact replay verified the explicit maximum partial-spread witnesses and every target at \(m=3,5\).

## originality

PASS

The 2026 all-symbol PIR paper explicitly leaves all-symbol recovery properties of Reed--Muller codes as an open direction. The older Reed--Muller availability paper studies locality/availability and does not state this odd-dimensional exact all-symbol multiplicity. The finite-geometry theorem supplies the maximum number of disjoint planes but not the coding-theoretic arbitrary-recovery-set upper bound or all-symbol conclusion. Focused semantic searches did not locate an equivalent or stronger odd-dimensional theorem.

## value

PASS

Odd dimension is precisely the case where a full two-spread is impossible and the classical Reed--Muller availability story is subtler. The theorem closes a natural open all-symbol family with an exact infinite formula and shows why allowing larger recovery sets cannot beat the finite-geometric construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
