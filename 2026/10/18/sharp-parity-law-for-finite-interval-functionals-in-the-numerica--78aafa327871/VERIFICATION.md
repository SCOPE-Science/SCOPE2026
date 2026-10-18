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

# Verification notes

The theorem follows from a universal two-level unit-vector Rayleigh bound and explicit saturating Jacobi weights. For even length \(k=2q\), the weight sums adjacent to even and odd vertices are exactly \(2\sqrt{q/(q+1)}\) and \(2\sqrt{(q+1)/q}\), respectively. These identities certify every coordinate of the positive eigenvector and the finite operator norm. Equality forces the same eigen-equations, which uniquely determine the interval weights from the left boundary. Odd lengths reduce to a direct sum of symmetric two-by-two blocks.

`CHECK.py` performs exact rational recurrence checks, independent numerical eigenvalue checks over lengths 1 through 120, and 2,800 seeded random finite-weight tests. Floating-point tests are not used as a substitute for the analytical proof. The test script requires Python 3 and NumPy and can be run as `python CHECK.py`. There are no infinite enumerations, external certificates, or independent audit assertions.
