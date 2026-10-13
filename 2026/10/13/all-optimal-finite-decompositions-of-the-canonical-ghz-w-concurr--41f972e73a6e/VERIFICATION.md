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

The analytic verification has four steps.

1. The HJW rows are orthonormal, so \(\sum_jp_jr_j=1\). For \(0<\lambda<1\), the source quadratic has \(g''(r)=10\lambda^2/9>0\), hence equality in Jensen is equivalent to \(r_j=1\) for every positive-probability term.
2. The definition of \(r_j\) and the probability equation then give \(|v_{1j}|^2=|v_{2j}|^2=p_j\). Orthogonality of the two HJW rows is therefore the single complex condition \(\sum_jp_je^{i\theta_j}=0\).
3. Conversely that complex condition makes the two rows \((\sqrt{p_j})_j\) and \((\sqrt{p_j}e^{i\theta_j})_j\) orthonormal, so it generates an optimal ensemble with every \(r_j=1\).
4. With two positive weights, a zero weighted sum of two unit complex numbers is possible only for equal weights and antipodal phases. Rank \(\rho_\lambda=2\) rules out a one-state ensemble.

The bundled `artifacts/verify.py` additionally evaluates the one-qubit reduction of \(\sqrt q\,|\mathrm{GHZ}\rangle+e^{i\theta}\sqrt{1-q}\,|W\rangle\) for several phases and confirms \(4\det\rho_A=(5q^2-4q+8)/9\). It also checks the source four-column co-isometry and a strict Jensen gap for nonconstant sample values. These computations are finite consistency checks, not an exhaustive proof.

Unproved limits: no statement is made about arbitrary rank-two eigenvector pairs, the endpoint rank-one cases, infinite ensemble measures, or other entanglement monotones.
