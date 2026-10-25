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

The proof's uniform input is the published homotopy theorem for \(\operatorname{VR}_{\le k}((\mathbb Z/3k\mathbb Z)^2)\), \(k\ge2\), together with the directly proved orbit-diameter and fixed-simplex lemmas. The character calculation uses the oriented simplicial Lefschetz formula; the group-module identification uses finite-group rational semisimplicity. No integral splitting or equivariant homotopy equivalence is verified.

Execute `python3 verify.py` from this directory with `morse_certificate.json` beside it. This requires only Python's standard library. The verifier reconstructs the full simplex sets for \(k=2,3\), their Euler characteristics, all 36/81 translations, fixed oriented simplices, predicted traces and Fourier multiplicity totals. It also validates an exhaustive 432-pair acyclic discrete-Morse matching for \(k=2\), with critical vector \((1,0,23,0,0)\), proving the known 23-sphere homotopy type independently in that finite case. The recorded run is in `verification_output.txt`.

Finite enumeration is not offered as a proof for arbitrary \(k\). The all-\(k\) claim is obtained by the general published homotopy theorem and the elementary proof in `RESULT.md`. No independent scientific audit has been performed.
