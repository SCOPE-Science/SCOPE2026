# Independent audit — 2026-09-29

Record: `2026/09/17/star-interval-resolution-branching--28c149b906dc`  
Assigned and audited source tree: `781fa47cd715bb06a16695c397f2cee8223c2610`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_supported**. The star formula and its degree corollary withstand independent reconstruction. For an oriented star P_{p,q}, every interval is either a singleton leaf or a set containing the center. This makes the upper bound bar-omega(S,C)<=r immediate by interval-pair type, while the pair S=L∪{c}, C={c}∪U is saturated and has bar-omega=r; the two-element chain gives the separate r=1 value 2. A fresh implementation of Aoki's saturated-pair definitions, written independently of the archived verifier, exhaustively checked every orientation with 1<=r<=6 and reproduced gldim Lambda=max{2,r}. The full-subposet on a vertex and all of its Hasse neighbors is exactly an oriented star, so the published full-subposet monotonicity theorem yields int-res-gldim(Q)>=max{0,Delta(Q)-2}. The hereditary-incidence consequence is also correct because a tree Hasse graph gives a unique directed path between comparable vertices, hence its incidence algebra is the acyclic path algebra.

## Originality

**qualified_explicit_evaluation**. Aoki's September 2026 preprint already supplies the general saturated-pair formula for the interval endomorphism algebra, and Aoki-Escolar-Tada already prove full-subposet monotonicity and cover the type-A and D4 special cases. The audited contribution is therefore not a new general homological mechanism. Targeted current searches did not locate the arbitrary-star closed form or the sharp maximum-Hasse-degree lower bound in those sources or elsewhere. Originality is supported only as this explicit family evaluation and corollary, especially for r>=4, with the usual residual risk from very recent or differently phrased work.

## Scientific value

**meaningful_structural_application**. The result turns a new general combinatorial formula into a clean orientation-independent closed form, derives a local branching obstruction for every finite poset, and exhibits unbounded interval-relative homological complexity inside a hereditary incidence-algebra family. It is a useful exact application rather than a replacement for Aoki's general theorem.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/17/star-interval-resolution-branching--28c149b906dc
- https://arxiv.org/abs/2609.15927
- https://doi.org/10.1007/s41468-025-00210-2
- https://arxiv.org/abs/2207.03663

## Limitations

- The theorem relies on Aoki's recent saturated-pair global-dimension formula and the published full-subposet monotonicity theorem.
- The exhaustive computation is corroborative only and was independently rerun only through r=6; the general proof is combinatorial.
- Originality is confined to the explicit star evaluation, degree corollary and hereditary-star consequence, not the underlying relative-Auslander or saturated-pair machinery.
- Because the main source theorem appeared in September 2026, contemporaneous unindexed observations remain a realistic priority risk.
