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

The result is an exact algebraic theorem for an \(s\)-stage Erlang-feedback phase-type family, \(s\ge3\), with \(0\le p<1\) and \(\lambda>0\). To replay the checks, run `python3 VERIFIER.py` from the directory containing the extracted files. Only the Python standard library is needed.

The verifier derives raw moments through degree four from the rational moment-generating function and checks independent closed forms, the rational derivative identity and the strict phase bounds for 132 rational parameter instances; it also checks further derivative identities. The general theorem follows from the displayed polynomial factorization and positive coefficients, not from enumerating a finite parameter grid. Pole arguments prove non-acyclic representability for \(p>0\), \(s\ge3\), using elementary triangular-generator spectral facts. No independent audit has been performed.
