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

# Verification

The proof's key finite identities are explicit polynomial identities in \(\mathbb Z[z]\), holding for every admissible network size. The entropy formula follows from the eigenvalues of the exact two-dimensional symplectic blocks. The passage to improper integrals is justified analytically by logarithmic uniform integrability at the two cube-root singularities; it is not an extrapolation from finite-size data.

Run `python3 checks/verify_stride3.py` using Python 3 and only the standard library. `checks/output.txt` records the executed polynomial, Fourier, degree, and asymptotic diagnostics. Exact polynomial checks for \(3\le n\le500\) and Fourier checks for \(3\le n\le120\) are independent implementation checks, not universal proofs. Numerical estimates of the limiting integrals have no certified interval bounds.

Publication priority has not been independently certified. The closest full-text sources establish the model and spectral entropy reduction; they do not explicitly evaluate this arithmetic entropy-density phase diagram. The analyzed scope is the stated stride-three family under Haar measure, not arbitrary couplings.
