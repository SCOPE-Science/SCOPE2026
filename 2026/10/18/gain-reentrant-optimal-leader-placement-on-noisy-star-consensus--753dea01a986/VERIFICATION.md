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

The bundled `verify.py` is a standard-library exact-rational checker for the new theorem. The executed command was `python3 verify.py`. Its observed output is:

```
VERIFY_OK rational_inverse_and_orbit_cases=1455 n=3..14; reentrant_example=n7_q3
```

The checker reconstructs full pinned-star matrices, computes inverse traces by independent rational Gauss–Jordan elimination, and compares with the block-resolvent formulas for every integer order \(3\le n\le14\), every admissible leader budget, and gains \(1/10\), \(1/3\), \(1\), \(3\), \(10\). It also checks the analytical objective-difference expression and all 35 placements for seven vertices and three leaders at three gains. The exact witness \(J_C=31/8\), \(J_L=23/6\) is checked at gain one. The finite checks are not exhaustive over arbitrary graph size or real feedback gain. Those domains are covered only by the universal symbolic Schur-complement proof and gain-function argument in `RESULT.md`. Independent external mathematical validation has not been carried out.
