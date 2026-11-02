---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Rotation invariance diagonalizes the polynomial norm: ||z^n||^2=kappa+M_n with M_0=1, M_n decreasing to 0 for measures supported strictly in D. Thus K(t)=sum_{n>=0}t^n/(kappa+M_n) and (1-t)K(t)=a0+sum_{n>=1}c_n t^n with c_n>=0, a0=1/(1+kappa), sum c_n=1/[kappa(1+kappa)]. Triangle inequality gives |(1-t)K(t)|>=(kappa-|t|)/[kappa(1+kappa)] for |t|<min(kappa,1). For delta_0, K=(kappa+t)/[kappa(1+kappa)(1-t)], achieving bound at negative real t and realizing zero -kappa for kappa<1. Smooth beta radial densities tend locally uniformly to delta_0 by moment convergence, so Rouche yields a unique nearby real simple zero. M_1=1/(alpha+2), M_n<=M_2=O(alpha^-2) for n>=2 give t_alpha=-kappa-(1+kappa)^2/(alpha+2)+O(alpha^-2). Exact Fraction sums with rigorous geometric tails independently certify alpha=3,kappa=1/6 signs at -9/10 and -24/25. This demonstrates a true smooth interior zero. The proof, not the finite certificate, establishes the universal radius.

## originality

PASS

QUALIFIED PASS: The standard weighted Bergman kernel moment expansion and interior-radial zero examples are prior work (Zeytuncu 2010, including his Dirac-mass remark), but his full text does not add a fixed positive Hardy boundary norm and does not prove the uniform mixed-norm zero-free radius min(kappa,1), sharp equality, or smooth beta limiting displacement. Seip treats interpolation/sampling and Mitkovski-Wick kernel operator estimates, not this mixed-kernel zero threshold in inspected accessible material. Closely related norm-mixture zeros may be studied elsewhere; search absence is not novelty proof.

## value

PASS

Adding Hardy boundary energy is a canonical Hilbert-norm interpolation/regularization of radial Bergman weights; determining exactly when it prevents Lu Qi-Keng zeros for every radial measure is a natural structural threshold. The sharp worst-case measure and smooth counterexamples show the uniform boundary between guaranteed nonvanishing and possible zeros, with quantitative approach to criticality. The finding also distinguishes a sum of norms from a sum of reproducing kernels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
