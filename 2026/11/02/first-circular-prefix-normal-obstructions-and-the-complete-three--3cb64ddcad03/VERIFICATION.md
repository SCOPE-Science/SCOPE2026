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

The proof is given in `RESULT.md`; the standalone checker `check_cyclic_prefix_normal.py` uses direct circular window sums and a separate gap formula. Run `python3 check_cyclic_prefix_normal.py` from a directory containing the checker. The checker verifies all binary words through length \(11\) and all words containing exactly three ones through length \(41\), including the rational generating-function coefficients and the exact smallest counterexample. It returns `VERIFY_OK` on success. The finite checks do not establish the all-length theorem; its proof is symbolic.

The generating-function count is for necklaces under rotation, not for words identified under reversal or complementation. The unique exceptional length-six necklace has six labeled representatives, and the named representative is `001011`. The conclusions concern circular factors and are not interchangeable with ordinary linear prefix-normality. An independent audit has not been performed.
