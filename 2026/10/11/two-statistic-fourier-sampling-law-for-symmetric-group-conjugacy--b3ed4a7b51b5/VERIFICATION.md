---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the conjugacy-class Fourier sampling theorem

The analytic proof establishes the complete spectrum for every integer \(n\ge4\) and every class; the computation below is finite corroboration only. The proof uses Schur orthogonality, the multiplicity-free decomposition of the standard endomorphism module, three explicit orthogonal sector-energy calculations, and the residual energy. Its normalization and the exceptional \(n=4\) cases are stated in the mathematical report.

Run `python3 artifacts/verify.py` from the package root with Python 3 and no third-party dependencies. The checker constructs every conjugacy class of \(S_n\) for \(4\le n\le7\), builds the exact integer class frame operator, verifies its annihilating polynomial on each ambient coordinate, and matches enough exact integer trace moments to uniquely determine eigenvalue multiplicities. The observed terminal line was:

`VERIFY_OK conjugacy_classes=38 permutations=5904 n=4..7 exact_annihilating_polynomial_and_moment_multiplicities`

No floating-point tolerance is involved. The program works with a larger ambient matrix representation and counts its known extra zero directions separately. The experiment does not establish the theorem for \(n>7\), exclude equivalent prior publications, or constitute an independent audit.
