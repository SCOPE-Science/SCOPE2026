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

## Reproducible check
Run `python3 VERIFIER.py` with a Python 3 standard-library installation. The verifier directly evaluates the defining \(p\)-strong Roman inequality at each zero-labelled vertex and enumerates small legal label assignments, rather than implementing the symbolic reduction used in the proof. The output is captured in `VERIFIER_OUTPUT.txt`.

## Verified scope
Ten small complete tripartite instances total 763,975 complete labelled assignments. The sharp family cases \(a=4,5,6,7\) were independently enumerated up to weight five, finding no smaller solutions and exactly \(3a^3\) weight-five solutions. A further 97 exact threshold comparisons cover \(4\le a\le100\).

## Unproved by the checks
Finite tests alone do not prove the infinite formula, nor the infinite sharp-family count; both depend on the stated combinatorial argument. This is not independent external validation. Absolute novelty is not certified.
