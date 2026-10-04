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
The proof was reconstructed from the all-shock Rankine--Hugoniot objective rather than inferred from a numerical experiment.

For each admissible \(k\)-shock, the right-state Lax inequalities imply \(s_k\notin\operatorname{spec}(DF(u^{(k)}))\), hence \(A_k=DF(u^{(k)})-s_kI\) is invertible. In the full derivative with respect to internal variables and endpoint parameters, the columns for \(u^{(1)},\ldots,u^{(n-1)},u_r\) form a square block lower-triangular matrix with diagonal \(A_1,\ldots,A_n\). This verifies surjectivity at every zero of the open admissible locus without invoking a regular-manifold hypothesis.

The parametric-transversality step is applied only on that open locus, where nondegeneracy, strict Lax inequalities, and speed ordering hold. Its source and target dimensions are equal for the restricted map \(x\mapsto\mathcal J(x;p)\), so \(C^1\) regularity is sufficient for the usual Sard/transversality threshold. At generic endpoints the square derivative \(D_x\mathcal J\) is therefore invertible at every admissible zero.

For perturbations of the flux, the all-shock objective depends \(C^1\)-smoothly on \(F\in[C^2(K)]^n\). The implicit function theorem gives a unique nearby Rankine--Hugoniot chain. On compact \(K\), sufficiently small \(C^2\) perturbations preserve strict hyperbolicity; the strict Lax and speed inequalities are open and persist by continuity.

Limits: no existence theorem is asserted for all-shock solutions, no global uniqueness across different wave patterns is asserted, and no statement is made for rarefactions or non-Lax waves. The 2003 Kong comparison was limited to its published abstract because lawful full text was unavailable in the checked sources.
