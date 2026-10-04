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

The proof is symbolic and covers every integer \(n\ge2\). The executable check is deliberately finite and is not used to infer the infinite statement.

`verify.py` performs four independent finite checks:

1. literal enumeration of every binary word for \(2\le n\le16\), with its adjacent-pair multiset computed directly from the word;
2. comparison of the observed profiles with the run-based feasible-profile generator;
3. comparison of every observed equivalence-class size with the closed run-composition formula, followed by exact singleton-word comparison;
4. an arithmetic-only check of the closed profile count through \(n=200\).

On the packaged bytes the expected terminal line is:

`VERIFY_OK exhaustive_words=131068 exhaustive_profiles=1082 n=2..16 arithmetic_n<=200`

The exhaustive range is a consistency check only. The unbounded conclusion rests on the endpoint-flow identity, explicit run realizations, and finite sums given in `RESULT.md`.
