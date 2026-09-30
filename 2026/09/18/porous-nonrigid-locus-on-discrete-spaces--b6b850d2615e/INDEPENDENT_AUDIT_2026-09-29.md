# Independent Audit — Uniform rigid holes in the space of metrics on every discrete set

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `a882d5c915533c01b3797d291e76451fd172084b`  
**Audited current source tree:** `a882d5c915533c01b3797d291e76451fd172084b`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence; no repository change was made during the audit.

## Correctness — PASS

PASS. The marker-plus-rounding proof checks. The scaled ceiling q(x,y)=δ⌈d(x,y)/δ⌉ is a metric because the ceiling is subadditive, differs from d by <δ off the diagonal, and is uniformly discrete. Adding a=δ/3 times the marker metric preserves the triangle inequality. The Hedrlín–Pultr marker exists for every cardinality at least eight and has only the identity endomorphism; for 3≤|X|≤7 the submitted three-distance marker has a unique 3/2 pair and a distance-1 chain that fixes every point. Distinct marker values in e=q+aρ are separated by at least aσ even across adjacent lattice levels, so every e-prime with D(e,e-prime)<aσ/2 has only the identity self-isometry. With δ=R/2, the center displacement is <5R/6 and the certified hole radii are R/24 in general and R/12 for |X|≥8, each contained in B_D(d,R).

## Originality — PASS

PASS, narrowly scoped. Ishiki explicitly leaves density of rigid metrics for an arbitrary target metric as Question 6.1; the paper settles strongly zero-dimensional spaces only up to continuum cardinality and totally bounded targets in general. Hedrlín–Pultr supply the rigid relation, and earlier Ishiki work supplies stronger-distance constructions below the continuum, but targeted searches did not locate the quantitative rigid-subball statement on arbitrary-cardinality discrete spaces. The audit credits only the robust marker-plus-rounding theorem and its porosity consequences, not rigid graphs or lattice rounding themselves.

## Scientific value — PASS

PASS. The theorem answers the recent density question on the full class of discrete spaces without a cardinality restriction and strengthens density to a scale-uniform interior-hole statement. In particular it covers cardinalities above the continuum, where strongly rigid real-valued distance assignments cannot exist, and identifies a quantitative mechanism making the nonrigid locus nowhere dense and porous within each finite-D component.

## Independent checks

- Re-derived the ceiling-metric triangle inequality and the uniform compatibility with the discrete topology.
- Checked the explicit 3-through-7-point marker and the Hedrlín–Pultr endomorphism-rigid marker regime.
- Recomputed the marker-value separation across equal and adjacent lattice levels and the perturbation-to-rigidity implication.
- Recomputed D(d,e)<5R/6 and both R/24 and R/12 rigid-hole constants.
- Read Ishiki 2609.19773 through Question 6.1 and compared its stated cardinality/totally-bounded ranges with the submitted theorem.
- Verified the current main directory tree SHA exactly equals the assigned source tree SHA.

## Limitations

- The result is restricted to discrete underlying topology and does not settle Ishiki Question 6.1 for arbitrary metrizable spaces.
- The constants 1/24 and 1/12 are sufficient and are not claimed sharp.
- The motivating preprint is very recent, so contemporaneous unindexed work remains a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.19773
- https://arxiv.org/abs/2210.02170
- https://doi.org/10.4153/CJM-1966-121-7
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/porous-nonrigid-locus-on-discrete-spaces--b6b850d2615e

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
