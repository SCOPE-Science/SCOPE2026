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

The exact checker `verify.py` uses only Python's standard library. It verifies the Hopf eigenvector and adjoint eigenvector identities, the normalization \(\bar p^Tq=1\), the two linear solves entering the first-Lyapunov formula, the symbolic polynomial identity

\[
l_1=\frac{8\alpha^2-13\alpha+15\gamma-1}{20},
\]

and the two source-parameter substitutions \(1217/2000\) and \(1157/2000\). A successful run prints `VERIFY_OK`.

The checker is an exact algebraic replay; it is not a proof of novelty and it does not test global continuation of the local periodic branch. The mathematical proof of the parameter-uniform formula is given in `RESULT.md`, including the explicit intermediate contraction \(G\). The degenerate surface where \(l_1=0\) remains outside the nondegenerate conclusion.
