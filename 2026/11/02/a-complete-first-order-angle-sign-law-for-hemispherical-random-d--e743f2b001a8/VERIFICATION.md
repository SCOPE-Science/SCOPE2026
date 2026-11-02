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

The mathematical proof uses (i) a Gaussian representation of independent hemisphere-uniform directions, (ii) an exact Gaussian quadratic-form determinant, (iii) an explicit Fourier expansion with integrated \(O_k(d^{-1})\) remainder, and (iv) Gaussian orthant integration against independent half-normal products.

The standalone `verify.py` performs exact Wick-pairing checks for all pairs of edges and all distinct triples of edges in the complete graph on five vertices, checks normalization of the signed first-order coefficient over every sign pattern for \(k=3,4,5\), and executes a seeded finite-sample comparison for all eight patterns at \(k=3\) and \(d=300\). Its acceptance tolerances apply to finite diagnostics only: they are not numerical certification of the analytic error term or of infinite-dimensional claims.

To reproduce: place `verify.py` alone in a writable directory with Python 3 and NumPy installed, then execute `python verify.py`. The intended success marker is `VERIFY_OK`.

No independent mathematical audit has been performed. In particular, the evidence here does not establish absolute historical priority; specialist overlap of unindexed material remains possible.
