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

# Reproducible checks and mathematical limits

The exact identity \(T_{z^2}=T_z^2+(1/6)e_1\otimes e_{-1}\) is checked by the normalized harmonic monomial coefficients, with the sole discrepancy at the first anti-analytic monomial. The inverse weighted-shift products telescope and the inside/outside resolvent series converge in operator norm. For the unique outlier, the scalar resolvent pairing is \(m=-6\) and its derivative is \(m'=686/b^2\). Summing the two complete coefficient families computes both eigenvector squared norms, giving the explicit Riesz-projection norm. Finally, elementary expansions of \(1-49/(16r^2)\) and \(1-9r^2/49\) establish the two collision coefficients.

Run `python3 checker.py` using Python 3 without external packages. The script evaluates right and left eigenvector coordinates on symmetric finite sections, verifies their norm ratio and resolvent pairing, and computes residuals for real and complex examples. The printed results are finite diagnostic confirmations; neither they nor any bounded finite enumeration prove the infinite-dimensional theorem. Independent audit: not performed.
