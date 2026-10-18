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
Run `python verify.py` with standard Python 3. The code (1) directly sorts all cyclic rotations; (2) reconstructs the same BWT through an independent gap-based grouped ordering; (3) compares full BWT outputs and the structural case distinction on every binary word containing three ones for lengths four through 22; (4) compares exact theorem counts for each length; and (5) checks the gap criterion on all ordered triples with gap sum at most 35. Expected output: `ALL_CHECKS_PASS full_word_count= 8854 gap_triples_checked= 8435 max_word_length= 22 max_gap_sum= 35`.

Only those finite checks were executed; the proof in `RESULT.md` covers all integer lengths at least four. The tests do not establish priority or supply independent scientific validation.
