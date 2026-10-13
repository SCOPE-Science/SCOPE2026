# Self-review

## Correctness — PASS

The semantic equivalence is between the lax split of \(\operatorname{dep}(x,y)\vee\operatorname{dep}(x,z)\) and edge covering by a left/right vertex pair in each fixed \(x\)-fiber. Two disjoint edges together with witnesses defeating both cross-covers provide a four-edge certificate. Inclusion-minimal four-edge certificates have matching number two and a monochromatic minimum two-vertex cover by König's theorem, forcing precisely the five four-edge types. Direct reverse checks establish minimality. The counting polynomials follow from distinct vertex choices and permutation factors. The included checker independently tested all 65,536 edge sets on a labeled \(4\times4\) graph and the complete-table formulas for side sizes at most four. Arbitrarily large finite instances are covered by the proof, not by those computations. The theorem concerns finite teams and arbitrary value domains.

## Originality — PASS, residual risk noted

The primary literature proves exact four-coherence for the same formula (Fröhlich–Kolaitis–Meier, Theorem 22) and shows one four-edge witness. That **covers** the size cutoff; no novelty is claimed for it. Its displayed proof and table do not give the exhaustive list of six colored minimal graph isomorphism types or the universal complete-table census. The present classification requires an additional edge-minimality, matching-cover and automorphism count. The 2026 Barlag et al. coherence paper establishes more general coherence/rewritability results, but only its abstract was accessible; an equivalent buried catalogue cannot be excluded. Other terminology for graph coverings presents residual rediscovery risk.

## Value — PASS

Classifying all inclusion-minimal violations, not merely asserting that some small witness exists, is a motivated exact invariant for a well-studied, naturally occurring database constraint. The six patterns form a complete, irredundant test basis; their colored distinction prevents collapsing genuinely different incidence failures. The two closed formulas quantify minimal violation certificates in complete database fibers for arbitrary side sizes, supplying an explicit benchmark family for counterexample enumeration and explanation.

Self-review: passed. Independent audit: not yet performed.
