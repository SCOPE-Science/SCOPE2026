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

# Reproducibility checks

The separately constructed `verify_primary.py` enumerates every perfect matching from vertex pairing for widths 4 through 11, checks every possible exchange pair, degree and component structures, and tests the odd-width lower bound and one-rung threshold witnesses. Its successful run ends with `PRIMARY_ALL_PASS`.

The `verify_alt.cpp` verifier constructs perfect matchings from cyclic column-dimer masks, explicitly adds odd-width exceptions, tests symmetric differences, and computes component counts for widths 4 through 12. Build and run with `g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt && ./verify_alt`. It ends with `ALT_ALL_PASS`.

These are finite checks, not a replacement for the published-form all-width mathematical argument. Reconstruct that proof's classification, winding-parity lower bound and one-rung witness to verify arbitrary parameters. The available abstract of the 2020 Möbius-ladder matching enumeration paper does not prove that it omits all analogous results in its full text; this remains a literature coverage risk.
