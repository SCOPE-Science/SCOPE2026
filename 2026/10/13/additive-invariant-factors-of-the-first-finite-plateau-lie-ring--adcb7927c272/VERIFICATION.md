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
The verifier in `artifacts/verify.py` regenerates the class-\(4\) free-metabelian Hall basis for the source order \(x_5<x_1<x_2<x_3<x_4\), normalizes brackets by skew-symmetry, Jacobi, and metabelian tail symmetry, and checks those normalization identities on generator data. It reconstructs the source's \(N=1\) relators, checks the six relations displayed in equation (3.5) after imposing the source's weight-\(4\) killing relation, forms every surviving ideal consequence through class \(4\), and appends the three terminal \(u_i\) relations.

The resulting exact integer presentation has \(160\) Hall generators and \(483\) relation rows. Smith normal form gives \(155\) nonzero diagonal entries, five free generators, and nonunit factors with multiplicities \(2^{\times1},4^{\times22},8^{\times1},16^{\times15},64^{\times7},256^{\times3}\). As a separate check on the unreduced presentation matrix, modular Gaussian elimination gives ranks \(106\) modulo \(2\) and \(155\) modulo \(3\), as forced by the claimed Smith factors. The recorded run in `artifacts/verify.txt` ends with `CHECK_OK`.

The computation proves only the additive invariant factors of the explicit \(L_1\) presentation. It does not verify a general \(N\)-formula. The Smith reduction is performed by exact integer arithmetic in SymPy; no independent software implementation has been run.
