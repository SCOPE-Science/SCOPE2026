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

# Reproduction and verification

Run `python3 check.py` with a standard Python 3 interpreter. No third-party modules, network connection, or external datasets are required. The script enumerates the \(q\) cyclic windows for each coprime \((p,q)\) with \(2\le q\le50\), uses integer floor arithmetic for the primitive mechanical period, independently computes the one-step tortoise image of every window, and compares the exact number of distinct images with the stated two-branch formula for all lengths \(1\le n\le2q+1\). It separately checks selected period-boundary and stabilization cases. Expected recorded output is in `check_output.txt`. Run `python3 boundary_check.py` to recompute the mechanical cells independently from exact rational midpoint arithmetic and check lexicographic monotonicity plus 48,807 adjacent-boundary identification decisions. Its recorded output is in `boundary_output.txt`.

All calculations are exact. These tests do not prove the universal claim; the proof is a general discontinuity analysis at all rational slopes. In particular, it proves that exactly \(h=\lfloor(q-1)/p\rfloor\) adjacent factor pairs may be merged just below and at the period boundary, and that their mergers disappear at one additional length per index. No independent audit or external validation is claimed.
