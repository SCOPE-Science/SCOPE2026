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

# Reproducibility

Run `python3 verification/verify_schur_critical.py` from the unpacked research directory. Python standard library only; no external data and no numerical floating point.

Actual successful execution reconstructed the \(64\)-line graph (\(576\) edges, degree \(18\)), verified its exact adjacency annihilating polynomial and traces, computed modular Smith filtration for primes \(2,3,7,11\), confirmed all \(63\) reduced-Laplacian invariant factors, and reproduced the number of spanning trees. The output concluded `VERIFY_OK`.

The finite arithmetic is an exhaustive reconstruction of the specific matrix, not a sample of possible line arrangements. The argument that modular pivots give true integer invariant factors uses row/column unit operations over a discrete valuation ring; the determinant comparison excludes all other prime factors. This does not establish broader uniform surface statements, nor independent historical novelty or independent scientific audit.
