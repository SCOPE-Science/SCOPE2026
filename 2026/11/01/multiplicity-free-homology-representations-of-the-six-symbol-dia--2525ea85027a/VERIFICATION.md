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
# Verification of the six-symbol diagonal-deleted chessboard result

Run `python3 verification/verify.py` from the file package root with standard Python 3. The program constructs all allowed faces directly from injective row-column selections excluding the diagonal; checks their counts \(30,315,1420,2715,1854,265\); and checks the simplicial boundary-square identity on every face.

It computes an exact rational basis for the fourth boundary image (rank \(1557\)) and evaluates its character for every one of the \(22\) symmetry conjugacy classes using rational transition coordinates, not floating point or a probabilistic estimate. It then applies an independent border-strip recurrence to all partitions of six and verifies the representation decompositions and character orthogonality. Finite-field computations independently recover the full rank profile \((29,286,1134,1557,265)\) at primes \(1009\) and \(65521\). The archived stdout in `verification/verification_output.txt` terminates `VERIFY_OK`.

The result pertains only to this finite complex. No extra tensor representations, torsion-module structure, homotopy equivalences, or external audits are established.
