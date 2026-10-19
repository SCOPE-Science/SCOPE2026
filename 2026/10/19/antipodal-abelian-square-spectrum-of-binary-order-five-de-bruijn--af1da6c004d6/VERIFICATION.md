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

Execute `python3 verify.py` from the same directory as this document, with Python 3 and no third-party dependencies. The complete edge-traversal search and exhaustive local pairing search are separately implemented; the former visits every allowed Eulerian path starting with the unique five-zero edge, and the latter enumerates all 65,536 local binary matchings. Both return the same set of exactly 2,048 valid rotation representatives, and separate count implementations (prefix sums and cyclic direct-sum comparison) return the same per-word statistics. All 32 five-bit cyclic factors and the global weight are checked for each word.

The checker also enumerates orbits under reversal and bitwise complementation and verifies the complete histogram and moments. Its successful terminal message is `HALF_PERIOD_ABELIAN_DB5_PASS words=2048 switches=65536 orbits=528`.

The computation verifies a finite, exhaustive order-five statement. It does not establish analogues for other orders, and neither the script nor this document claims independent external validation.
