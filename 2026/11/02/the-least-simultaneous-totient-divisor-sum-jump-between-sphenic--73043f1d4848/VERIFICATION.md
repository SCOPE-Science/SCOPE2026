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

# Verification scope

The exact proof is in `RESULT.md`. Run `python3 verify.py` to reproduce the bounded integer discriminant census of \(37\) triples arising from the proved normalization \(h=abc<320\), the modulo-\(3\) exclusions of the two positive-square cases, and the values for the explicit \(320\) witness. The script uses standard Python 3 only, exact integer arithmetic and trial division for its six small primality checks.

Expected certificate includes `tested_normalized_even_offset_triples=37`, `subthreshold_shapes=[(96,...),(192,...)]`, and `jump=320`. A finite list over the normalized differences is exhaustive because the algebraic argument bounds \(a\le4\) and the increasing even offsets \(b,c\), not because an integer search over \(n\) terminated. It does not claim to enumerate all pairs at shift \(320\) or to have received independent scientific auditing.
