# Independent audit — Exact Jung-defect decomposition in constant-curvature space forms

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/20/jung-defect-decomposition-space-forms--3a2f1fd32372`  
**Assigned and audited tree:** `66ea39112e70b1c1239d000d2741e519dc8c7c5e`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026` at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`

## Disposition

**PASSED.** The record survives independent review without a substantive research-file edit.

## Correctness

PASS. Minimum-enclosing-ball first-order optimality gives an active equilibrium support with at most n+1 tangent directions. The Euclidean, spherical, and hyperbolic cosine laws all reduce to Phi_kappa(d_ij)=Psi_kappa(R)(1-<u_i,u_j>), while the equilibrium condition gives sum_{i<j} lambda_i lambda_j(1-<u_i,u_j>)=1/2. These identities yield the displayed support formula and, after adding and subtracting the diameter value, the exact nonnegative defect decomposition. The support-cardinality bound follows sharply from sum lambda_i^2>=1/m; the near-equality threshold, weight lower bound, and componentwise edge estimate follow with the stated constants. The spherical diameter hypothesis keeps the active geometry away from antipodal singularities.

## Originality

PASS on a cautious literature-bounded boundary. Classical Jung inequalities, Dekster's spherical/hyperbolic theorem, Lang–Schroeder's CAT(kappa) extension, and known Euclidean minimum-enclosing-ball duality are prior art and are not claimed as new. Targeted searches did not locate the exact constant-curvature split into barycentric imbalance plus weighted active-edge shortfall or the sharp deficit-to-support-cardinality hierarchy. Dekster's 1995 paper is the most important residual source: after open-access/arXiv attempts did not provide inspectable full text, the authorized Oxford retrieval was tried repeatedly but timed out at the publisher page, so its full text is not represented as read. This unresolved historical-access limitation weakens priority confidence but is not decisive against the specific defect decomposition.

## Scientific value

PASS. The record upgrades a sharp extremal radius-diameter inequality into a termwise nonnegative certificate that separates two distinct mechanisms of deficit and converts a scalar deficit into a sharp discrete support-dimension conclusion. The same formula simultaneously covers Euclidean, spherical, and hyperbolic model spaces and gives quantitative control of support weights and individual active edges.

## Independent checks

- Derived the three cosine-law identities and the equilibrium sum identity independently and recomputed the defect decomposition.
- Verified the sharp m-point hierarchy and the threshold epsilon<1/[n(n+1)] using Cauchy-Schwarz/equal-weight extremizers.
- Attempted authorized retrieval of Dekster (1995) after open-access/preprint attempts; the job timed out and no inaccessible text was treated as read.
- Checked that the current main-path tree is unchanged from the assignment snapshot.

## Literature and evidence

- https://doi.org/10.1007/BF01874495 — Dekster (1995), spherical and hyperbolic Jung theorem; full text could not be obtained in this audit.
- https://doi.org/10.1023/A:1006574402955 — Lang and Schroeder (1997), Jung theorem for Alexandrov spaces of curvature bounded above.
- https://doi.org/10.1007/s00022-010-0028-0 — Schneider (2009), a different stability theorem for simplex extremality.
- https://doi.org/10.1007/s00022-024-00714-9 — Böröczky, Csépai and Sagmeister (2024), modern hyperbolic convex-geometry context.

## Limitations

- Dekster (1995), the most plausible older source for an implicit constant-curvature calculation, remained inaccessible in full text after lawful retrieval attempts; it is not claimed as read.
- The theorem controls an active circum-support rather than global Hausdorff or Banach-Mazur distance of the whole set.
- The spherical statement is restricted to the non-antipodal Jung regime, and no exact extension is asserted for general CAT(kappa) spaces.

## Repository guard

The current `main` record tree was checked against the assignment and is unchanged at `66ea39112e70b1c1239d000d2741e519dc8c7c5e`. The publication plan changes only independent-audit materials and `VERIFICATION.md`; the Lean and expert-attestation channels are preserved exactly as `unknown` with null evidence.
