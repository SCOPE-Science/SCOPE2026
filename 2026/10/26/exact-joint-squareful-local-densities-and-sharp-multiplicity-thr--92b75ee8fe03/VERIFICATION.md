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

Using Python 3 and no third-party packages, run `python verify.py`. The verifier enumerates primitive pairs modulo \(p^2\) and directly applies the predicate \(F_i(x,y)\not\equiv0\pmod p\) or \(F_i(x,y)\equiv0\pmod{p^2}\). It compares exact rational proportions against the structural formula and constructed fixed-\(k\) minimizers.

The executed certificate is:

`CERTIFICATE_OK primitive_pair_counts 553 primes 4 k range(1, 8)`

The verified primes are \(3,5,7,11\), with \(1\le k\le7\). A deterministic random seed fixes reproducible coefficient selections. Every extremal construction for these \(p,k\) is independently enumerated. This is finite corroboration only; the proof in RESULT.md establishes the infinite family. No independent mathematical audit has been performed.
