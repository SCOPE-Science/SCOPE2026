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

The accompanying `verify_e8_orbits.py` script is a complete exact-arithmetic census of the **finite** lattice step: there are \(2160\) vectors of norm \(4\) in \(E_8\), forming \(135\) congruence classes modulo \(2E_8\), each with \(16\) representatives. It independently computes \(136\) isotropic classes of the mod-two norm-halving form in \(E_8/2E_8\). It uses standard-library Python 3 and asserts all totals.

The geometric reduction for infinitely many conic pencils is an ordinary mathematical proof, not a finite extrapolation: the E8 Mordell–Weil section intersection pairing forces the difference of two intersecting sections to have norm \(4\); Costa's conic-class characterization identifies their divisor sum with a conic pencil, and the classification of singular fibers shows every conic pencil arises in this way. A translation changes the E8 coordinate by \(2w\), and a class with elliptic-fiber degree \(2\) and square \(0\) is determined by this coordinate. The Euler characteristic \(12=4+8\) accounts for the eight singular conic fibers.

The theorem is limited to smooth rational elliptic surfaces over \(\mathbb C\) without reducible elliptic fibers. Neither a proof for surfaces with reducible fibers nor an arithmetic descent statement is asserted. Independent audit and independent validation have not been performed.
