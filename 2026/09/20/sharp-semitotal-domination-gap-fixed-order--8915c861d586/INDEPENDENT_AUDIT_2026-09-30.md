# Independent audit — 2026-09-30

**Record:** `2026/09/20/sharp-semitotal-domination-gap-fixed-order--8915c861d586`  
**Audited repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `9b99691f0643ee4156671cff695151cbc665de58`  
**Disposition:** **PASSED**

## Correctness — PASS

The proof was reconstructed. For a minimum dominating set D with |D|>=2, the auxiliary graph joining dominators at graph distance at most three is connected; a spanning tree and one internal vertex for each distance-three tree edge give a semitotal dominating set of size at most 2γ(G)-1. Together with the established half-order bound γ_t2(G)<=n/2 this yields the parameter-sensitive gap bound. The proposed tree B_{d,s} was checked arm by arm: γ=d+1 and every semitotal dominating set uses at least two vertices on each length-four arm plus one center/direct-leaf vertex, while an explicit set has size 2d+1. Boundary orders n=2,...,5 are consistent. The repository's exhaustive artifact independently checks connected Graph Atlas graphs through order 7, nonisomorphic trees through order 10, and the extremal family through order 20.

## Originality — PASS (literature-bounded)

Goddard–Henning–McPillan introduced semitotal domination and established the half-order extremal setting; Wei–Hao and Zhuang study tree comparisons with domination/total domination, and Chen–Xu characterize the half-order equality case. Targeted searches for the fixed-order maximum of γ_t2-γ, synonymous difference/gap formulations, and the explicit all-order tree family did not locate this exact theorem. The upper bound is a short optimization of known-type inequalities, so an unindexed or differently phrased corollary remains a real residual priority risk.

## Scientific value — PASS

The record converts separate semitotal-domination bounds into an exact fixed-order extremal difference and supplies a sharp tree construction for every order. It also shows cycles cannot increase the extremal gap beyond what trees already attain.

## Evidence and literature

- Goddard, Henning, McPillan, Semitotal Domination in Graphs (2014): https://people.computing.clemson.edu/~goddard/papers/SemiTDomUtilitas.pdf
- Zhuang, Semitotal domination versus domination and total domination in trees (2024): https://doi.org/10.1051/ro/2024037
- Chen and Xu, Graphs with semitotal domination number half their order (2025): https://doi.org/10.1017/S0004972724000509

## Limitations

- No classification of all fixed-order extremal connected graphs or trees is claimed.
- The fixed-order formula is obtained by a short synthesis of comparison/order bounds, so equivalent older wording remains the principal originality risk.

The independent audit finds the record scientifically complete on all three axes at the audited tree. The literature verdict is bounded by the sources and searches explicitly described above; it is not inferred merely from failure to find a match.
