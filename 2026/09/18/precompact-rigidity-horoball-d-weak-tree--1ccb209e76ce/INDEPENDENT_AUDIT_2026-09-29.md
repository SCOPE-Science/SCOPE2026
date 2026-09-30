# Independent Audit — Precompact rigidity and horoball limit sets for metric-functional weak convergence

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `7a58564145b19247c333823da91777c0d2d499b8`  
**Audited current source tree:** `7a58564145b19247c333823da91777c0d2d499b8`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence; no repository change was made during the audit.

## Correctness — PASS

PASS. The precompact-rigidity argument is exact: an r/4-net of A_r={y:d(x,y)≥r} gives finitely many internal functionals h_w with h_w(z)-h_w(x)<-3r/4 for every z∈A_r, so the relative sigma-neighborhood lies inside the metric r-ball. Since sigma is already coarser than the metric topology, the two topologies agree on every totally bounded subset. In the proper binary R-tree, every metric functional is either internal or a Busemann function: a pointwise-convergent net of internals has either a bounded cofinal subnet, yielding an internal limit by properness, or an escaping subnet whose endpoint directions converge in the compact Cantor boundary. For y_n on 0^(n-1)1... at radius 2(n-1)+C, b_xi(y_n)=C while every other Busemann and every internal functional tends to +infinity, so the exact d-weak limit set is {b_xi≤C}. Moving to radius 3n sends also b_xi to +infinity, producing convergence to every point.

## Originality — PASS

PASS. Gutiérrez–Nevanlinna’s September 2026 paper constructs the topology, proves net convergence equals d-weak convergence, and gives an every-point non-Hausdorff example on the snowflaked real line. Targeted searches did not locate a total-bounded-subspace rigidity theorem, an exact Busemann-horoball realization, or an every-point d-weak sequence in a proper CAT(0) tree. The earlier metric-functional paper gives closed/W-convex limit-set structure rather than these existence and rigidity statements.

## Scientific value — PASS

PASS. The two results sharply separate bounded/precompact behavior from escape-to-infinity pathology for the new topology. The proper CAT(0) tree example is especially informative: even in a complete uniquely geodesic setting the topology can be maximally non-Hausdorff, while bounded d-weak convergence in every proper metric space collapses to ordinary metric convergence. Exact realization of every Busemann horoball adds geometric structure beyond a single counterexample.

## Independent checks

- Checked the source topology basis and d-weak net equivalence against the full open preprint.
- Re-derived the finite internal-functional neighborhood proving topology equality on totally bounded subsets.
- Checked the metric-functional boundary classification for the locally finite binary R-tree, including the net/subnet dichotomy.
- Recomputed all Busemann and internal-functional limits for the horoball and universal-limit sequences.
- Searched specifically for d-weak/tree/CAT(0)/horoball and total-bounded rigidity formulations.
- Verified the current main directory tree SHA exactly equals the assigned source tree SHA.

## Limitations

- The universal-limit construction is specific to the regular binary R-tree, not arbitrary proper CAT(0) spaces.
- The topology is the Gutiérrez–Nevanlinna metric-functional d-weak topology, not the established projection/Delta-weak CAT(0) topology.
- The motivating topology paper is only days old, so unindexed parallel work remains a residual originality risk.

## Evidence and references

- https://arxiv.org/abs/2609.19368
- https://arxiv.org/abs/2506.04154
- https://doi.org/10.4171/ZAA/1828
- https://doi.org/10.1007/s11856-022-2420-5
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/precompact-rigidity-horoball-d-weak-tree--1ccb209e76ce

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
