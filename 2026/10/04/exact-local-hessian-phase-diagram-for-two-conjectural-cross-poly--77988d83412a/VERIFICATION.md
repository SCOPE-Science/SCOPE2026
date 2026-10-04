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

The proof uses the exact integral representation
\[
I_n(a)=\int_0^\infty\prod_j(1+a_j^2t^2)^{-1}\,dt
\]
and intrinsic great-circle variations inside \(M_n\). At the sparse candidate, the two tangent isotypic components reduce to beta integrals and yield the exact eigenvalues \(-3\) and \((n-8)/n\) for every admissible dimension. This part is symbolic and dimension-uniform.

At the dense candidate, permutation symmetry reduces the Hessian to one scalar integral. The standalone checker `artifacts/verify_hessian.py` reconstructs the second-variation rational function and evaluates that integral exactly for \(n=4,5,6,7,8\). It verifies
\[
\frac{3}{68},\ -\frac{2393}{7865},\ -\frac{5899}{9762},\ -\frac{2290207}{2630733},\ -\frac{16822403}{15129624},
\]
respectively. It also checks the exact candidate-value comparisons in dimensions \(5\) and \(6\). With the packaged dependency version, execution terminates with `VERIFY_OK`.

The finite dense integrations are used only for the five explicitly claimed dimensions. They are not extrapolated to higher dimension. No computation establishes the unproved global maximizer conjecture, and no higher-order conclusion is drawn from the zero Hessian mode at \(n=8\).
