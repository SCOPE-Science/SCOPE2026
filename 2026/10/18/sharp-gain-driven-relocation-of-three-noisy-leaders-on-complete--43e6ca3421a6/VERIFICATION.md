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

The standalone source `verification/verify.py` reproduces the three symbolic objective-difference identities for all formal parameters, the positive-coefficient certificate after shifting \(m=3+y\), all four orbit objective values against exact full-matrix inversion for \(3\le m\le8\), exact branch classifications over \(3\le m\le12\) and ten positive rational gains, and defining polynomials of critical ties. The recorded successful execution output is `PASS 183 exact symbolic and rational assertions`.

The code requires Python 3 and SymPy, and can be run with `python verification/verify.py`. It has no network dependency. The checked finite instances are not an exhaustive proof of an infinite theorem. The analytical proof rests on the explicit rational identities and coefficient inequalities provided in RESULT.md. Independent audit has not been performed.
