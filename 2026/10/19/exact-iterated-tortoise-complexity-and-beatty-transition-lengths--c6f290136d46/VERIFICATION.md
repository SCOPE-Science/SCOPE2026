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

# Verification of the iterated-tortoise formula

The theorem relies on the explicit finite-word prefix identity, the standard floor-sum identity for Sturmian mechanical words, the pairwise distinctness of irrational phase cut points, and monotone coordinate changes. Each of these is independently stated and proved in `RESULT.md`.

The reproducible standard-library checker `checker.py` performs all of the following finite checks: all binary words through length \(11\), all powers from \(2\) to \(n+2\), every output-prefix comparison; seven irrational slopes evaluated using 70-digit decimal arithmetic; and all factor lengths through \(68\) with the listed powers including one larger than the word length. The original program's output is recorded verbatim in `checks.txt`. Run with `python checker.py`.

The finite checks are regression tests only. The infinite all-slope, all-length proof is the cut-counting argument in `RESULT.md`. Boundary phases coincide only at the irrationally distinct partition endpoints; they introduce no additional factors. The original literature's definitions and the already-known one-pass specialization are excluded from claims of new priority. Independent scientific audit or publication-priority verification has not been performed.
