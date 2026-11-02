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

# Reproduction checks

The complete finite certificate is `CERTIFICATE.tsv`, with exactly 24 rows for all nonzero pairs modulo five. The script `verify.py` uses only the Python standard library. Run `python3 verify.py` in the same directory. It reconstructs the state recurrence from the digit maps, checks the exact total-vector identity at depths one and five, the min/max vector translations at depths sixteen and twenty-eight, and the eight smaller root cases proving the sharp starting index eight.

The script independently computes Stern's sequence directly up to index 131072, checks its signed partial-sum extrema, enumerates all digit words for signed-digit widths one to six, and checks the representation imbalance maxima and minima through width seventeen.

Observed output from the actual package source files:

`VERIFY_OK states=24 levels=53 total_period=4 from=1 root_shift_start=8 all_states_start=16 increment=4 direct_stern_terms=131072 direct_BSD_widths=8..17 enumeration_widths=1..6 certificate_rows=24`

The state recurrences and the two finite complete-vector certificates, not finite extrapolation from the independent arithmetic checks, underwrite the infinite claim. No theorem about other moduli, every prefix histogram, or independent certification is made.
