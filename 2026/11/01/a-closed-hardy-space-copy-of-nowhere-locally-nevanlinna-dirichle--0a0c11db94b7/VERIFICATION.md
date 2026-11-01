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

# Verification record

The claim was checked by reconstructing four distinct proof steps: (1) odd-index projection of Harper blocks, (2) uniform Euler lower bound for bounded imaginary parts, (3) dense-open argument in the countable Hardy-intersection Fréchet topology, and (4) disjoint-prime tensor norm factorization and local analytic nonvanishing. The published input \(\|D_X\|_{\mathscr H^p}\lesssim_p\sqrt X/(\log\log X)^{1/4}\), \(p<2\), is Theorem 1 of Harper's original arXiv:1703.06654 and is cited, not reproved.

To replay finite sanity tests from a clean extraction of this package, execute `python3 check.py` with Python 3 and NumPy installed. It checks the exact finite odd decomposition against direct summation at sample arguments, bounds the finite Euler-summation remainder for increasing samples, and verifies independent prime-coordinate product factorization numerically. These checks are **not** an exhaustive or infinite-dimensional proof; the complete analytical argument is in RESULT.md.

Novelty checks compare source statements and implications; they do not certify that all mathematical literature has been indexed or read. No independent audit has been performed.
