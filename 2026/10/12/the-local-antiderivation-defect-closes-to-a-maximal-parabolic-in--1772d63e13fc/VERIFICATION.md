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

Run `python3 artifacts/verify.py` from the package root. The expected terminal line is `CHECK_OK`.

The verifier uses exact rational arithmetic. It checks the defining antiderivation identity on all ordered basis pairs for a basis of the reconstructed antiderivation space, verifies the structural constraints defining the local-antiderivation candidate, checks constructive local witnesses on a finite integer regression grid, verifies the three explicit triple-bracket generators, and computes the iterative ordinary-Lie and Lie-triple closures. The reported dimensions are \(8\), \(10\), \(13\), and \(13\), and both closures are compared with the \(13\)-dimensional subspace stabilizing \(\operatorname{span}\{e_1,e_2,e_3\}\).

The finite regression grid is not an exhaustive proof over \(\mathbb C\). The universal locality argument is the explicit case split in RESULT.md; the universal closure argument is exact linear algebra together with the fact that the stabilizer is a Lie subalgebra.
