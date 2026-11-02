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

The complete finite proof certificate is `verify.py`, run with `python3 verify.py`. It enumerates every binary word of lengths 1 through 15, retains exactly one canonical rotation/reversal representative of each orbit, and checks total orbit coverage against \(2^n\) and Burnside's bracelet count. It computes every cyclic window-composition histogram independently by direct slicing and rolling sums, checks the short-to-long complement relation, then tests the exact fiber lists and sizes. It also checks each complement and nonequivalence statement.

Observed local run: `VERIFY_OK`. The script prints the per-length number of bracelets, distinct complete spectra, autocorrelation profiles, and collision pairs, then verifies the length-fifteen representative pair powers through multiplier six. The identity for all multipliers is proved mathematically in `RESULT.md`, not assumed from finite replay.

The mathematical statement relies on exact enumeration only for lengths at most fifteen; no unbounded exhaustive search or formal proof-assistant certification is asserted. Literature-priority comparisons are qualified by the material actually inspected. Independent audit and independent validation have not been performed.
