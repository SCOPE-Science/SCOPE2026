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

# Verification details

The program `verify.py` uses only Python's standard library and runs from the current package directory with `python3 verify.py`. It enumerates all \(8!=40320\) full \(9\)-cycles by their cyclic order starting at \(0\), retains precisely those for which the product with the fixed full cycle is again a full cycle, and tests direct conjugation by each element of \(C_9\). It checks the identity fixed set has \(8064\) elements, order-three generators fix \(9\) each, order-nine generators fix \(3\) each, and the full orbit-size distribution is \(3\) singleton orbits, \(2\) three-element orbits, and \(895\) nine-element orbits.

Actual execution produced `VERIFY_OK`, `UNROOTED_BELYI_COVERS=900`, and `AUTOMORPHISM_ORDER_COUNTS=1:895,3:2,9:3`. Independent of computation, the proof uses character-theoretic full-cycle counting and an explicit wreath-product centralizer description. No enumeration beyond \(9\) sheets, arbitrary target automorphisms, or Galois-orbit computation is claimed.
