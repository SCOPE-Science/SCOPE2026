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

# Reproducibility and limits

`verify.py` is a standalone Python 3 program using only the standard library. Execute `python3 verify.py`. It generates every order-preserving, regressive character on the labeled blocks; for each character it enumerates every possible point assignment, checks idempotency directly by composition, and constructs the point-image-rank histogram. Separately, it computes the polynomial recursively from the weighted-run theorem and compares the full histograms coefficient by coefficient.

Exact test cases: all pairs \((k,d)\) with \(0\le k\le3\), \(1\le d\le3\), and additionally \((k,d)=(2,4)\). The explicit \(E_{2,2}(z)=2z+8z^2+4z^3+z^4\) is tested independently. The script prints `VERIFY_OK` after all comparisons pass. Earlier source references and theorem arguments are in `RESULT.md`.

These finite enumerations do not establish all infinite \(k,d\), the existence or uniqueness of dominant complex singularities, or the limiting Gaussian distribution; those conclusions follow from the algebraic-combinatorial proof and analytic argument in `RESULT.md`. Independent audit is not performed.
