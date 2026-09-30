# Independent Audit — 2026-09-29

**Record:** `2026/09/12/054`  
**Title:** Disproof of the cross-polytope versus box masking acceptance–Rényi tradeoff  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `5a01a01782ebfbc39375bd92dfffcd9e569b85bd`  
**Disposition:** **REPAIRED**

## Independent checks

- Re-derived delta_box, delta_cross, and D_alpha=-log(delta) from the uniform-overlap model.
- Recomputed all numerical values independently for both the filed beta=240 and corrected beta=78 cases.
- Checked the standardized parameter tuple against NIST FIPS 204 Table 1, including a visual inspection of the official PDF table.
- Compared scope against the 2024 IACR polytope FSwA paper.

## Three-axis assessment

- **Correctness — PASS_AFTER_REPAIR**: The overlap and Rényi calculations are correct, but the filed numerical witness mixes parameter values from different Dilithium/ML-DSA sets: l=4 and gamma1=2^17 are ML-DSA-44, while tau=60 and eta=4 are never paired in FIPS 204. NIST Table 1 gives ML-DSA-44 tau=39, eta=2, beta=78. Recomputing at that actual tuple preserves the refutation: delta_box=0.9997024536, delta_cross=0.9991949649, acceptance ratio=0.99949236, and D2_cross/D2_box=2.70627.
- **Originality — LIMITED**: The uniform-subset identity D_alpha=-log(delta), box overlap, and l1-ball volume/slicing are elementary, while polytope-based FSwA is already an active literature. The record’s defensible novelty is the explicit evaluation of the proposed tradeoff at the corrected standardized tuple, not a new rejection-sampling principle.
- **Scientific Value — PASS**: After replacing the hybrid tuple by a real ML-DSA-44 parameter set, the counterexample directly addresses a standardized scale and refutes both inequalities with exact formulas. The structural reason—dimension-wide overlap loss in the l1 ball versus one-coordinate loss in the box—is reusable beyond the single numerical instance.

## Findings

- Current tree equals assigned tree SHA.
- FIPS 204 Table 1 lists ML-DSA-44 (k,l)=(4,4), tau=39, eta=2, beta=78, gamma1=2^17; the filed beta=240=60*4 is not a standardized tuple.
- Independent recomputation at beta=78 gives acceptance ratio 0.99949236<1.5 and D2 ratio 2.70627>1.
- The exact analytic formulas remain valid after the parameter correction, so the scientific conclusion is repaired rather than rejected.

## Sources compared

- NIST FIPS 204, Module-Lattice-Based Digital Signature Standard: https://doi.org/10.6028/NIST.FIPS.204 — Table 1 gives the standardized ML-DSA-44 values tau=39, eta=2, beta=78, gamma1=2^17 and (k,l)=(4,4).
- Bambury et al., Polytopes in the Fiat-Shamir with Aborts Paradigm: https://eprint.iacr.org/2024/411 — Shows that polytope-based rejection sampling and comparisons with hypercube/spherical masking are established prior context; the submitted claim should be scoped to its exact tradeoff calculation.

## Limitations

- The repaired counterexample is for the canonical uniform membership-overlap model, not every FSwA rejection rule.
- The priority assessment is deliberately modest; no claim is made that polytope masking or its general tradeoffs are new.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
