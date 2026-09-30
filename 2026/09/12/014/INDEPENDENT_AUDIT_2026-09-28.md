# Independent Audit — 2026-09-29

**Record:** `2026/09/12/014`  
**Title:** Finite-order rigidity of the P8 six-reflection Coxeter lift  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `2a6ed2c986b0002d742d7615fac08acec599ff5d`  
**Disposition:** **PASSED**

## Independent checks

- Rebuilt the 8x8 Gram matrix and six reflections independently with integer arithmetic.
- Computed c_M powers and verified exact order 12.
- Checked that the quotient block is -E6 and that the induced Coxeter product has order 12.
- Compared scope against P8 monodromy literature to avoid elevating the one-product computation into a general rigidity theorem.

## Three-axis assessment

- **Correctness — PASS**: For the explicitly filed 8x8 Gram matrix and ordered product S5...S0, the matrix conclusion is exact. Independent integer-matrix reconstruction gives c_M^12=I and no smaller divisor 1,2,3,4,6 gives identity; the induced six-dimensional quotient is the E6 Coxeter element of exact order 12. Thus this particular lift has zero radical translation. The conclusion is correctly limited to the fixed matrix/product.
- **Originality — LIMITED**: E6 Coxeter order and characteristic polynomial are classical, and the full-lattice conclusion is an exact computation for one stated lift. Broader P8 automorphism/affine-reflection phenomena are already studied in the literature, so this should be read as a targeted certificate rather than a new structural classification.
- **Scientific value — PASS**: The computation is useful as a falsification of the proposed nontrivial-translation alternative for the distinguished product and as a reproducible check on a subtle radical-lift question. Its scope is narrow but clearly delimited.

## Findings

- The current record tree exactly matches the assigned tree SHA.
- Independent reconstruction of the filed Gram matrix and reflections gives first return to identity at exponent 12 on the full 8-dimensional lattice.
- The quotient is negative E6, so the order-12 quotient and polynomial Phi12*Phi3 are classical and reproduced exactly.
- The zero translation conclusion follows immediately from c_M^12=I for this fixed lift; no claim about every P8 monodromy element is warranted or made.
- The repository's `output/artifacts/...` wording is a stale workspace path; actual packaged scripts are under `artifacts/`, a non-scientific issue.

## Sources compared

- Ebeling, Distinguished bases and monodromy of complex hypersurface singularities: https://arxiv.org/abs/1905.12435 — Survey reference for distinguished bases, Picard–Lefschetz transformations, and monodromy context.
- Goryunov–Kerner, Automorphisms of P8 singularities and the complex crystallographic groups: https://arxiv.org/abs/0806.1720 — Shows that P8 automorphism/affine reflection phenomena are broader than the single distinguished product audited here.

## Limitations

- The audit validates the exact matrix statement only for the stated Gram data and product S5...S0.
- It does not independently certify that the precise Gram matrix normalization is the unique or canonical published Gabrielov presentation.
- No analytic Torelli, deformation, or classification consequence is inferred.

This audit is independent of the repository's pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
