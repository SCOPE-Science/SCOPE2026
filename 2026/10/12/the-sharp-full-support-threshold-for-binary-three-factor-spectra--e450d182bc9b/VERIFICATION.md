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

# Reproducibility and verification

All attached programs use Python 3 standard library and operate independently on small exact integer state spaces. Run `python3 verify_presence_dp.py`, `python3 verify_presence_raw.py` and `python3 verify_presence_ie.py` from this directory. The complete numeric census of all 256 masks is represented in `finite_profiles_3_to_50.csv` by per-length maxima and the exact maximizing support masks. The full recurrence has 1024 states and 2048 binary transitions at each length; the computation checks exact partition totals \(2^n\) and strict dominance for every length \(14\) through \(50\). A separate exhaustive word-by-word reconstruction of masks through length \(18\) and independently evaluated matrix inclusion-exclusion at lengths \(13\) through \(25\) provide cross-checks of the boundary and full-spectrum counts.

The general \(n\ge51\) case is not established by this table: it follows from the written union-bound proof and the exact rational check \(9(7/8)^{17}=2093674625884863/2251799813685248<1\). No tests were done for alphabets other than binary, cyclic words, other factor lengths, or noisy measurements. The scientific originality comparison is self-review only, not an independent audit.
