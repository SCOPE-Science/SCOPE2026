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

# Finite verification and limitations

Run `python3 mk_ind2_check.py` using Python 3.9 or later; only the standard library is needed. Expected marker: `MOBIUS_KANTOR_IND2_HOMOTOPY_AND_FULL_AUT_CHARACTER_OK`.

The executable checks every graph edge, all nonempty sixteen-bit candidate vertex sets, \(6812\) faces, their face vector, all \(35104\) face-cover incidences, the \(3400\) gradient pairs, and global acyclicity. It constructs the integer Morse boundaries, checks their matrix product is zero and finds a unit determinant \(-1\) three-by-three minor. A completely separate original-chain mod-two elimination computes boundary ranks \((0,15,105,407,917,1147,693,120)\) in chain degrees zero through seven and reduced Betti number three only in degree six.

A graph-isomorphism backtracking routine enumerates all \(96\) automorphisms and computes each reduced signed simplicial Lefschetz number. It verifies character squared norm one, zero group average, rotational character \((3,-1,-1,-1,3,-1,-1,-1)\), and a two-element action kernel.

The homotopy conclusion uses the integer degree classification of attaching maps of cells on wedges of spheres of dimensions four and five; the code does not assert that a finite rank calculation alone classifies arbitrary CW complexes. The quotient statement is rational and does not establish contractibility or integral acyclicity. Independent external validation has not been performed.
