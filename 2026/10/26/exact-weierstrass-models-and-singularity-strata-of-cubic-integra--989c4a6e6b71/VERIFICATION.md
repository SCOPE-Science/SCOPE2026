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

# Verification of the explicit cubic integration-root model

The accompanying \(\texttt{verify.py}\) is a standalone executable SymPy-based exact checker. It verifies, as formal identities in all four coefficients, the invertible projective coordinate substitution and cubic discriminant factorization. It also checks the necessary depressed-cubic repeated-root invariant and the equivalence of the cusp parameterization, and computes exact smooth, nodal and cuspidal examples. Execute \(\texttt{python verify.py}\) from a directory containing that file; success terminates with \(\texttt{VERIFY_OK}\).

The program does not replace the geometric proof: irreducibility and singularity types follow from the \(v^2=f(u)\) local model, the smooth projective point at infinity, and the standard genus formula for integral plane cubics. The input coefficient domain is \(a_0a_3\ne0\) over \(\mathbb C\). Results on positive integer or real fractional integration follow only through the given polynomial-family interpretation; the projective theorem is about its complex algebraic continuation. Independent audit has not been performed.
