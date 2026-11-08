# Independent mathematical audit

## correctness

PASS

Under i.i.d. atomless entries, all 9! rank permutations of 3×3 cells have probability 1/9!. The row minima and column maxima uniquely determine a six-vertex functional digraph. The rank-constrained linear-extension recurrence L(S)=sum over available cells of L(S∪{cell}) exhausts every rank order and correctly counts each of 3^6 possible map pairs, including zero-count inconsistent pairs. Independently enumerated all 362880 permutations in the working container, not merely read a recorded VERIFY_OK: joint (cycle type, max depth) counts were (2,1):9576,(2,2):69264,(2,3):22464,(2,4):6912,(4,1):127872,(4,2):110592,(6,0):15552,(2+4,0):648, summing 9!. Weighted counts of six vertex depths were (1267488,625536,247968,29376,6912), summing 6×9!, so P(T=0..4)=(163/280,181/630,41/360,17/1260,1/315) and E[T]=179/315. Summing by maximum gives (5/112,1909/5040,1249/2520,13/210,2/105). At least two vertices lie on a cycle so depth<=4, and an explicit rank matrix attains it. The full finite probability space, not an extrapolated sample, is exhausted for precisely 3×3 games. This says nothing about arbitrary play protocols or larger matrices.

## originality

PASS

The same zero-sum alternating-best-response functional digraph is studied by Karelas–Lugosi–Zhang (2026), whose cycle distribution and cycle-probability formulas are prior coverage. Their Section 5 concerns common-interest paths. Exact transient-forest depth distributions from six strategy vertices require more information than cycle type and were not provided by inspected prior results. Exact finite census remains subject to possible unindexed earlier computations.

## value

PASS

Time to first reach a recurrent class is a natural functional-digraph observable in alternating best-response play, not determined by the usual numbers or lengths of cycles. The 3×3 matrix is the first balanced zero-sum size allowing a four-edge transient; the complete exact distribution and sharp rare-delay probability are useful finite benchmarks rather than an arbitrary numerical slice. No claim of asymptotic large games is needed for this exact finite value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
