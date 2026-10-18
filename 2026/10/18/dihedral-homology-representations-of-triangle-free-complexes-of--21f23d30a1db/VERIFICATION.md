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

# Computational and proof verification

Run `python3 verification.py` with Python 3.10 or newer and no external packages. The included `verification_output.txt` records one successful execution. The verifier reconstructs the graphs' triangles for \(7\le n\le14\), independently computes orbit-weight sums under all \(2n\) dihedral elements for \(7\le n\le13\), and directly evaluates the signed trace of each setwise-fixed oriented simplex for \(7\le n\le11\). Its mod-two boundary-reduction calculation checks the Betti vectors through \(n=12\). It also verifies the finite matrix identities underlying the transfer recurrence.

The scientific proof of the all-length statement is not based on extrapolating the tested examples. Critical exact premises are the cited Kim–Kim mod-two homology theorem, the equality between the squared-cycle triangles and cyclic consecutive triples, the signed Lefschetz identity, and the two transfer-matrix calculations. The input theorem supplies only mod-two ranks; rational concentration follows by the universal coefficient theorem, and exact rational ranks are independently recovered from Euler characteristic. These steps do not assert integral torsion-freeness or a homotopy classification. No independent scientific audit has yet been performed.
