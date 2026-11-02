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

# Verification record

The exact general result is supported by the proof in `RESULT.md`. Its nonstandard module-theoretic step is the integrality of an isomorphism between nonrational first-layer lattices, deduced from the lack of a nonzero \(k\)-linear form vanishing on the residue line and equality of lattice indices. The absence of independent mathematical audit must not be mistaken for external certification.

Run `python3 verify.py` with Python 3 and no additional packages. The program constructs finite extension arithmetic and independently exhausts \(\mathrm{PGL}_2(\mathbb F_p)\) point-orbits for prime fields \(p=2,3\) and extension degrees \(d=2,3,4,5\) where listed. It checks the expected orbit sizes, total point count, free-type size and complete predicted module-class counts.

Observed output includes `VERIFY_OK`, with type counts \(2,2,4,6\) at \((p,d)=(2,2),(2,3),(2,4),(2,5)\), and \(2,2,5\) at \((3,2),(3,3),(3,4)\). The program tests projective-orbit arithmetic; it does not mechanically verify the symbolic equivalence between module isomorphisms and fractional-linear transformations, nor does it establish the theorem for arbitrary prime powers or unbounded extension degrees.
