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

Run `python3 verify.py`. Only the Python standard library is required. The program implements the two sequential rules by separate exact rational recurrences, enumerates every weak composition of electorate size \(1\) through \(9\) among the seven nonempty ballot types, tests the six-profile permutation orbit, and checks one hundred members of the all-larger-electorates family. It prints the exact histogram \(0,0,0,0,0,0,0,0,6\), along with the enumerated-profile count of \(11,439\).

Proof of the unbounded minimality and extension claims is the integer-inequality argument in RESULT.md, not extrapolation from finite execution. The checker does not establish novelty, determine consequences for other committee sizes, or assess tied elections. No independent scientific audit has been performed.
