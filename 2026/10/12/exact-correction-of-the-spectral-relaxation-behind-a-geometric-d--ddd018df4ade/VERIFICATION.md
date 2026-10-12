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

The proof was checked in two layers. First, the constrained minimization was reduced analytically to a strictly convex quadratic in the largest coordinate; this establishes the formula for all allowed parameters and does not rely on sampling. Second, `verify_relaxation.py` was executed from the packaged path using exact rational arithmetic and returned `VERIFY_OK`.

For the source-specific witness, the checker verifies ordering and all displayed Eq. (9)/(10) constraints at representative exact rational negativities and separately verifies the polynomial identities
\[
R(N)=-\frac{7N^2}{24},
\qquad
R(N)-\frac{N(2-5N)}{16}=\frac{N(N-6)}{48}.
\]
The all-\(N\) conclusion follows algebraically from these identities for \(0<N\le1\), not from the finite test list.

The result is limited to the source's displayed spectral relaxation. It does not claim that the witness spectra are physically realizable state/optimizer spectra, and it does not challenge the source's independently supplied physical counterexamples.
