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

# Reproducible verification

Run `python3 verify.py` using standard Python 3.8 or newer. The script builds the two signed carry matrices directly, evaluates their powers, and compares against direct enumeration of every integer in all 18 dyadic intervals \(0\le n<2^r\) for \(0\le r\le17\). It independently compares the complete four-class parity frequencies, including normalization/integrality, as well as the marginal closed form and the cubic recurrence for the mixed term. The run completed with `PASS` across 262143 input evaluations.

The symbolic argument is documented in `RESULT.md`: binary carry invariants derive the matrices, matrix identities prove rational generating functions, and an irrational spectral angle proves sharp oscillations for all indices. Exhaustive checks were performed only up to \(r=17\); no claim of computational exhaustiveness at larger indices is made. No external independent audit or scientific certification has been performed.
