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

# Verification and reproduction

From the directory containing the supplementary file, run `python3 verify.py`. The script uses only the Python standard library; it directly enumerates all preference vectors for each integer from 1 through 6, checks the successful parking-function count and record means by exact rational arithmetic, and compares independently two published-algebraic representations of the expectation.

It also computes the exact product sum in floating point for sizes 1,000, 10,000, 100,000 and 1,000,000, and compares it with the claimed three-term asymptotic using an explicit high-precision value of Euler's constant. The script records 26 passed checks on the supplied run; execution at the stated paths succeeded. The finite tests do not establish the infinite asymptotic; the proof uses a uniform product expansion, a Gaussian tail bound, Euler--Maclaurin, and an integral evaluation.

The earlier finite exact identity and leading square-root asymptotic are from R. G. Pinsky, *The distribution on permutations induced by a random parking function*, Theorem 16 and equation (85), DOI:10.37236/13842; first public preprint arXiv:2404.11529. Their attribution is necessary. Independent audit has not been performed.
