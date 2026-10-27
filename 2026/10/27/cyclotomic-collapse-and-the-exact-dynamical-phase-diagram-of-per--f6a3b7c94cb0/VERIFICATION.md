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

# Reproducibility and limitations

The proof explicitly supplies the operator, periodic product, spectral mapping reduction, eigenvector recurrence, bounded diagonal similarity, and the open disk conditions for the eigenvector criteria. The shadowing equivalence uses Theorem 3.6 of Messaoudi–Tofanin Neto–Tsokanos (arXiv:2610.15023), specialized through the exact one-period product; this published criterion is an external premise, not independently reproved here. The mixing and frequent-hypercyclicity steps use the Godefroy–Shapiro criterion and Grivaux's perfectly-spanning-eigenvector theorem, respectively. All hypotheses are complex \(\ell^p\) with \(1\le p<\infty\), nonzero exact-periodic weights, and primitive cyclotomic diagonal.

Running `python verify.py` from the extracted package tests finite-matrix collapse, exact repeated-block coefficients and gauge equivalence. It is a reproducible algebraic consistency test only: neither infinite-dimensional hypercyclicity nor spectral mapping nor shadowing is inferred from finite matrices.

The parameter endpoints \(R=L\) and \(R=U\) are excluded from shadowing. The mixed region \(L<R\le U\) disappears if \(a=0\), because then \(L=U=1\). The theorem has not received independent audit or independently certified historical priority.
