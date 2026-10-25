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

# Verification and limits

The proof is uniform over integers and uses the exact integral Mayer–Vietoris resolution of the cover by star simplices and the split exactness of the augmented exterior chain complex of a simplex. The parity-sensitive symmetry action is recorded at the chain level; ordinary Betti-number or rational rank computations would not certify it.

The accompanying standard-library Python program `verify_kneser.py` enumerates the full combinatorial complex and signed matrices for \(4\le n\le8\), verifies the octahedron chains, their relative \(\partial_4\) coefficients, five-term relations and two generating permutations, and compares finite-field ranks. The resulting degree-two homology ranks are \(1,4,10,20,35\), with full integral conclusions resting on the written proof. The program was executed from the included source, and `verification_output.txt` contains its actual output. It does not purport to exhaust all \(n\), nor does it provide an independent scientific audit.
