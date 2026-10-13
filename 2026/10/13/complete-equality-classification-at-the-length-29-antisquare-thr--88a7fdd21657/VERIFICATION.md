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

Run `python3 verify.py` beside `certificate.json`.

The search begins from the empty word. Because both admissibility conditions are inherited by factors, every admissible word has an admissible prefix, so prefix extension is exhaustive.

For each appended bit, every new forbidden factor must be a suffix. The verifier checks every even suffix of length \(2h\), \(h\ge4\), for the antisquare relation, and checks every suffix length \(L\) and every candidate period \(p\) satisfying \(3L\ge8p\). Thus no floating-point period or exponent comparison is used.

The verifier regenerates the complete survivor counts through length \(30\), confirms exactly eight survivors at length \(29\) and none at length \(30\), then independently checks every factor and every candidate period in each of the eight extremizers. Finally it recomputes the reversal/complement action and obtains exactly two orbits of size four.

The verification proves only this finite equality classification. It does not reprove the source's other repetition-threshold theorems. Independent audit has not been performed.
