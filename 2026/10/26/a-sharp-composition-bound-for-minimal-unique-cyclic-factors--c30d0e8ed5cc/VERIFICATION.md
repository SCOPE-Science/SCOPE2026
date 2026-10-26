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

# Verification details

The file `cyclic_mus_verify.py` uses direct cyclic-window enumeration, with occurrence counts taken by starting position. From its directory run `python3 cyclic_mus_verify.py`. It verifies both inequalities for all binary inputs of lengths 2–15, ternary inputs of lengths 2–8, and four-letter inputs of lengths 2–6 (80,825 cases total), and checks binary de Bruijn cycles of orders 1–6 and ternary cycles of orders 1–4. Its successful output concludes with `ALL_PASS 80825 word_cases 482766 total_mus`.

The checker is finite and does not certify the infinitely quantified theorem; the proof rests on the explicit injection and de Bruijn multiplicity argument. The publication date and priority comparison derive from the cited paper metadata and accessible article material, with the inaccessible full 2011 paper retained as an uncertainty. No independent audit has been carried out.
