---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Conditioning on the exploration/relocation decision gives exact v_n, t_n=E(S_n X_n), and s_n=E(S_n²) recurrences. Martingale difference xi_j and weights h_k~1/k give an L²-bounded convergent martingale; an O(log n/n²) mean-square discrepancy and Borel–Cantelli yield a.s. centroid convergence. The explicit generating function F(z)=((1-pz)/(1-z))²I(z) has a double pole whose coefficient yields L=sigma² p(2+p)/(2(1-p)), and a log-singular term yields -sigma² p(1+p)/(1-p)² (log n)/n. Independently checked moment recurrences for multiple p, and the integral I(1) coefficient by quadrature; numerical checks corroborate not prove the asymptotic.

## originality

PASS

Qualified best-of-knowledge: the preferential-relocation model and logarithmic endpoint MSD are established. The assessed statement concerns the unscaled empirical centroid's a.s./L2 convergence, exact nonzero variance and sharp logarithmic finite-size correction, not endpoint scaling or weak occupation-measure limits.

## value

PASS

The empirical centroid of a canonical preferential relocation process is a natural time-average observable, quite different from its known logarithmically spreading endpoint. An exact nondegenerate limit variance plus leading logarithmic convergence correction is useful for occupation fluctuations and random recursive path averages, beyond a routine variance substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
