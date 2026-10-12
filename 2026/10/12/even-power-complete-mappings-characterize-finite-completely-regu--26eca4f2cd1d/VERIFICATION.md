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

# Verification

The symbolic proof of the theorem is included in `RESULT.md`. The main nonstandard implication is the finite permutation-cycle argument: the composition \(\theta\circ\alpha^{-1}\) sends each \(y\) into \(S^1y^k\), which lies in \(S^1y^2\) when \(k\geq2\). Since this composition permutes \(S\), the descending principal-left-ideal sequence along each finite cycle is constant. Consequently \(y=uy^2\), and iteration to an idempotent power constructs an inverse in a local group. No Green-relation separation theorem is assumed.

The constructive converse is elementary arithmetic on group exponents. For even \(k\), the prime two never presents two forbidden residues, and every odd prime leaves at least one nonzero permitted residue; CRT then supplies a power exponent making both global power maps bijective.

To reproduce the finite checks, run:

```bash
python3 verify.py
```

Expected terminal summary:

```
ORDER 1 ASSOCIATIVE_TABLES 1
ORDER 2 ASSOCIATIVE_TABLES 8
ORDER 3 ASSOCIATIVE_TABLES 113
ASSOCIATIVE_TOTAL 122 COMPLETELY_REGULAR 57 ODD_THREE_COMPLETE 43 CRT_CASES 900 VERIFY_OK
```

The exhaustive tests cover only multiplication tables of orders at most three, explicit examples of larger matrix-unit structures, and 900 CRT pairs. They do not establish the all-order theorem without the general mathematical proof. This review does not represent independent verification.
