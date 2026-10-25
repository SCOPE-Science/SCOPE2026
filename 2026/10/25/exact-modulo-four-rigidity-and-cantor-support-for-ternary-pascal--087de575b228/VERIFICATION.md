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

## Mathematical verification

The proof is an exact application of Lucas's digit congruence and two multiplicative signed transforms. Its delicate case is the ternary digit \(2\), for which the local ordinary alternating sum is \(1\) and the character-weighted alternating sum is \(3\). The divisions by \(2\) in the signed-sum formula are exact integer operations; modulo \(4\), exponents are reduced modulo \(8\) before division, avoiding an invalid cancellation of a nonunit.

The standalone Python file `verifier.py` builds Pascal rows by an independent recurrence and checks signed sums, residue classes, and triadic interval counts. The finite checks supplement but do not replace the proof. No independent mathematical audit has been performed.
