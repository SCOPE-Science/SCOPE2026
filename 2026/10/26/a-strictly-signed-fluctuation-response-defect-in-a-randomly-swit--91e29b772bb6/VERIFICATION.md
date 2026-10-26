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

# Reproducibility and limits

The closed-form result follows from the two-state generator \(Q\), the tilted matrix \(Q-K\), and the stationary second-moment equation \((2K-Q)u=2Dp\). The critical exact identities are \(-C'(0)=D\), \(\mathcal F'(0)=Dab(k_1-k_0)^2/[(a+b)Z]\), \(\lambda_+\lambda_-=Y\), and the two-mode spectral decomposition. The theorem explicitly includes the nontrivial boundary \(k_0=0\) because switching into the \(k_1>0\) state still ensures stationary second moments.

Run `python verify_fluctuation_response.py` with NumPy and SciPy. The program forms the matrices independently from the displayed scalar expression, checks 960 response/covariance comparisons over 160 parameter regimes, verifies 160 area formulas and peak conditions, and performs two separate event-driven switching/Brownian Monte Carlo checks. The matrix-exponential checks are numerical approximations; the stationary generator identities and exact eigenvalue calculations provide the proof. The Monte Carlo checks have sampling tolerance and cannot establish all-parameter statements or priority against prior research.

No external or independent scientific audit has been performed. Claims outside two-state Markov switching, harmonic drift and additive-force response are not covered.
