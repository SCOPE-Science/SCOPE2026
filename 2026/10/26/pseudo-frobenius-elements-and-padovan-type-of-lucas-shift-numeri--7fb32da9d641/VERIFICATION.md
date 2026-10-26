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

The all-index proof is in RESULT.md and invokes the explicit legal-Lucas-digit and Apéry results of arXiv:2211.01436. The checks below are reproducible finite corroboration, not an independent audit or proof of all cases.

Run `python3 verify_lucas_type.py` with the Python 3 standard library. This constructs exact legal digit sets and brute-force pseudo-Frobenius criteria for every index \(5\le a\le21\), comparing full sets and cardinalities. For \(5\le a\le13\) it independently computes Apéry residues using shortest paths in the semigroup Cayley graph and verifies the weighted coin formula. It also checks maximal-independent-set combinatorics.

Limits: The theorem is not established by finite enumeration; its all-index evidence is the symbolic transformation argument in RESULT.md. Broader originality remains subject to independent publication-priority review. Independent mathematical audit has not been performed.
