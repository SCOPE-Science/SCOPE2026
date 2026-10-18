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

The classification for all even \(n\ge4\) is derived by exact one- and two-spoke face classification, relative ball/cone attachments and an explicit simplicial retraction onto the rim boundary. Every special pair adds one top sphere; no unproved limiting step or numerical extrapolation occurs.

Run `python3 verify_wheel.py` with standard Python 3. Its checks enumerate every arc subset of the alternating-spoke directed wheel for even rim lengths \(4,6,8,10\); independently test directed path-forest validity, link formulas, rim retraction, mod-two boundary ranks and Euler characteristics. Expected lines begin `PASS` followed by rim length and the corresponding data; reported nonzero reduced Betti ranks are \((1,2)\), \((1,3)\), \((1,4)\), \((1,5)\) in adjacent dimensions \((2,3)\), \((4,5)\), \((6,7)\), \((8,9)\).

The executable test is a finite corroboration in characteristic two, not a replacement for the integral, infinite-family topological argument. An external mathematical review has not been conducted.
