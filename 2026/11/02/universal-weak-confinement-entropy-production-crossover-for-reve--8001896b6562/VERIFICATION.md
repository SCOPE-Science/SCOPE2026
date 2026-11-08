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

The exact joint Fokker–Planck Shannon balance S′=Π−Φ uses edgewise zero integrated jump currents from detailed balance. Integration by parts gives DΦ=σ²+u²e^(−2κt)+κ²Var(X_t)−2κCov(v_Yt,X_t)−κD. Spectral reversibility yields nonnegative C(t)=Σc_l e^(−λ_l t), R≤W and Var≤(D+W)/κ, hence the uniform flux error κ(2W+D)/D. Independent Gaussian-convolution noise bounds conditional entropy from below while Gaussian maximal entropy and total variance bound it above; their width on [a/κ,b/κ] is (1/2)log[(D+W)/(D(1−e^(−2a)))]. Integration proves claimed error and limit. Numeric covariance/flux test confirms normalization only.

## originality

PASS

Qualified PASS: Paoluzzi–Puglisi–Angelani explain the singular stationary free/trapped entropy-production mismatch in a two-heading model and provide related entropy balances. Their inspected main results do not give this finite scaled-window crossover or reversible multistate uniform remainder. Standard entropy/variance inequalities are ingredients but do not state this evaluated limit.

## value

PASS

The previously observed noncommuting free/trapped stationary limit makes time O(κ^(−1)) a motivated missing regime. The theorem resolves a universal exponential drift-memory crossover with explicit error for an entire family of reversible chains, while carefully fixing the physical entropy convention.

The dated certificate retains the supplied scientific assessment, sources and limitations.
