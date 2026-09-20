# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The upper bound was checked from first principles. If a b-coloring has \(q\) colors, its \(q\) selected b-vertices each have degree at least \(q-1\); connectedness and \(n\ge2\) force degree at least one on every other vertex. The resulting degree sum is exactly the inequality used in `RESULT.md`.

Both sharpness regimes were checked separately. In the sparse regime, the core has the requested cycle rank and the prescribed leaf counts exactly fill the missing colors in each core b-vertex neighborhood. In the dense regime, the clique is retained while extra edges adjust cycle rank; the simple-graph capacity inequality guarantees that enough nonedges exist. The boundary \(r=(k-1)(k-2)/2\) is consistent in both descriptions and reduces to \(K_k\).

For the sparse minimum-order equality statement, equality in the degree sum leaves no degree slack: the selected \(k\) vertices have degree exactly \(k-1\) and all remaining vertices have degree one. Connectivity forces the high-degree vertices to induce a connected core, so all other vertices are leaves and the claimed leaf counts follow.

Exact enumeration of all connected Graph Atlas graphs through order 7 found no violation and reproduced the claimed maximum for every feasible parameter pair. Explicit witnesses were also checked for every feasible pair through order 30. These computations are corroborative rather than a substitute for the proof.

## Originality

Irving and Manlove (1999) explicitly establish the necessity of at least \(k\) vertices of degree at least \(k-1\) for a b-coloring with \(k\) colors and the associated m-degree upper bound. Kouider and Mahéo (2002), as reported in the 2018 Jakovac--Peterin survey, give the size-only bound \(b(G)\le 1/2+\sqrt{2m+1/4}\). The survey's general-bounds section also records order-, complement-, clique-, and matching-based estimates, but the checked material does not state the simultaneous connected order-size bound or a cycle-rank extremum.

Searches for b-chromatic/b-coloring together with cyclomatic number, cycle rank, circuit rank, excess, minimum order, and joint order-size formulations did not locate the exact formula, its all-parameter sharpness construction, or the sparse threshold equality classification. Current-status checking also located Zaker's 2026 preprint on independence- and chromatic-number bounds; its abstract does not state a cycle-rank/order result.

The originality assessment is therefore PASS only to the best of our knowledge. The full Kouider--Mahéo paper was not inspected directly and is the most relevant inaccessible source because it contains classical size/order bounds. Its relevant advertised statements were checked through the 2018 survey. The 2026 Zaker paper was inspected only at abstract level. Differently indexed theses or proceedings using excess, circuit-rank, or m-degree language remain a residual risk.

## Value

The principal theorem is an exact two-parameter extremum, not only an isolated bound: every feasible \((n,r)\) is attained. Its inverse gives the exact minimum order needed for a prescribed b-chromatic threshold at fixed cycle rank, and the sparse minimum-order equality graphs are completely described by leaf-completing a connected core to degree \(k-1\). This provides a direct structural refinement of the classical high-degree and size-counting bounds.

## Limitations

The dense-regime minimum-order equality graphs are not classified. No claim is made that the tree and unicyclic specializations are independently new. Finite computations do not constitute proof. Originality remains subject to the source-access and indexing uncertainties stated above.
