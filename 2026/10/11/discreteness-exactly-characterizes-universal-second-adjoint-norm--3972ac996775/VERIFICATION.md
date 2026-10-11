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
# Reproducibility and verification

The proof has four checkable components:

1. Verify the topological annulus construction: select a convergent sequence, nested relatively compact neighborhoods, disjoint \(C_c\) bump functions \(\psi_n\), and a compact-support cutoff \(h\) which is one on all \(\operatorname{supp}\psi_n\). The map \(E(a)=a_\infty h+\sum_n(a_n-a_\infty)\psi_n\) is uniformly convergent because \(a_n\to a_\infty\); its range is in \(C_0(K)\). Evaluation \(R\) satisfies \(RE=I_c\). Norm-one estimates use only convexity of scalar intervals.
2. Use the isometric identification \(\Phi:\ell_1\to c^*\), identify the columns of \(S=\Phi^{-1}T^*\Phi\), and compute \(\|Se_{n+1}\|_1=1-2^{-(n+2)}\). The supplied `verify_columns.py` checks the rational identity for the first 60 indices, computing the infinite geometric tail exactly rather than truncating it.
3. If \(S^*\) had a norm-one maximizing vector \(\zeta\), the bound \(\|S^*\zeta\|\le (|\zeta(u)|+1)/2\) would force all its coordinates to be identically \(+1\) or \(-1\), and therefore \(\zeta(b_n)=0\) for all \(n\). This yields \(\|S^*\zeta\|=1/2\), a contradiction. This is an infinite-dimensional analytic argument, not a finite-test inference.
4. For \(A=ETR\), norm-one preservation follows from \(RE=I_c\). If \(A^{**}\) attained one, its witness would transfer under \(R^{**}\) to an unattainable norm-one witness for \(T^{**}\).

The full September 1, 2026 arXiv source was inspected for the real \(c_0(\Gamma)\) positive case and the \(c\) negative case. The full public mathematical proof of the nearest third-adjoint result was also inspected; its weaker parity-three assertion does not cover this second-adjoint classification.

Finite exact arithmetic is supplemental. There is no claim of computer-assisted verification of the theorem for all spaces. The case of spaces without convergent sequences is unproved here.
