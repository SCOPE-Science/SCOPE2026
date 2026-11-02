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

The result follows analytically from the classical invariant-subspace projection theorem, the exact two-to-one vertex-to-edge sign map for a unicyclic graph, the flip-Laplacian equations for the absolute Rademacher sum, and coefficient extraction in two elementary binomial polynomials. The accompanying standard-library `verify.py` enumerates all 45 cases \(3\le m\le11\), \(3\le\ell\le m\) with exact rational arithmetic and independently tests the conditional Fourier coefficient. Expected output: `UNICYCLIC_WALSH_EXACT_OK 45`.

Finite tests do not prove arbitrary graph size. The general constant-projection theorem is prior work; the result concerns an exact graph-specific evaluation and parity law. Bibliographic completeness and independent verification remain outstanding.
