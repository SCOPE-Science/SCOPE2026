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

The analytical proof classifies the three height intervals without numerical enumeration. On the coordinate sector \(0<s<t<1\), direct differentiation establishes the spherical area element \((1+t^2+s^2)^{-3/2}\,dt\,ds\). Integration gives the normalized one-variable density \(12t/[\pi(1+t^2)\sqrt{1+2t^2}]\). The endpoint checks give survival values exactly one at \(q=0\) and zero at \(q=1\).

Run `python verify_tetra_sections.py` using Python 3 (standard library only). The checker repeats density quadrature, survival-law threshold integration, ordered-projection identities, direct intersection-edge counts and seeded \(150000\)-normal sampling. During preparation, it printed `ALL_CHECKS_PASSED` and numerical probabilities close to the exact formulas. The checker is not a computer-assisted proof of all directions; the analytic spherical integral supplies that proof.

The motion-invariant comparison follows independently from the identity \(\sum_{i<j}|h_i-h_j|=3(h_4-h_1)+(h_3-h_2)\) and the Cauchy–Steiner edge-dihedral mean-width formula. The invariant-plane marginal is contextual, not assessed as a new statement.

Checks not performed: independent review, exhaustive historical-priority search and complete reconstruction of inaccessible specialized publications.
