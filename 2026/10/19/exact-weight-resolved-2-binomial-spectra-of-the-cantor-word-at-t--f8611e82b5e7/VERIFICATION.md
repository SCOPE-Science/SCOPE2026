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

# Verification of the exact triadic Cantor spectrum

Run `python3 verify.py` with the Python 3 standard library. The executed standalone program returned `VERIFY_OK: exact arithmetic k=0..11; two-arm / rolling-window sets k=0..7`.

The program recomputes exact digit positions and integer intersections for every \(0\leq k\leq11\), testing twelve stated totals and all weight ranges. For each level \(0\leq k\leq7\), a second construction generates both entire families of padded-prefix and reversed factors from the finite Cantor block and checks their actual profile sets. A third construction scans every length-\(3^k\) factor of an independently generated larger Cantor prefix by rolling the weight and first moment and compares the complete sets of profiles. All comparisons are exact integer checks.

The finite scanning comparison does not establish completeness for the infinite word; the block decomposition in `RESULT.md` proves that completeness for every exponent. The proof independently establishes the normalization (zero-based positions), binary \(2\)-binomial reduction, endpoint cases, interval intersections and digit-carry gap law. The verification does not assert any closed formula for the all-exponent value beyond the displayed finite arithmetic expression. It does not constitute an independent audit.
