---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Conditional row normalization and mean constraints give exactly r,s∈[0,1/4] and r+s=H=p−1/2, so all couplings are parameterized. Monotone one-dimensional W2 coupling of the discrete rows to their centered Gaussians has covariance g(t)=φ(Φ^{-1}(t))+φ(Φ^{-1}(t+1/2)); objective is constant−Rg(r)−g(s). g″ is strictly negative, g′(0+)=+∞, g′(1/4)=0; unique interior critical point follows by endpoint derivative signs. Derivative w.r.t. R positive. Mills ratio implies g′(t)∼√(2log(1/t)) at 0 and Taylor g′(1/4−t)=ct+O(t²); the three regimes follow separately with H relative to 1/4. I independently solved 13 parameter/scale cases, confirmed feasibility, stationarity, concavity and c≈6.293730161. The analytic proof, not finite R numerics, establishes the quantifiers.

## originality

PASS

Marini’s October 2026 state-dependent q_x-Bass paper contains the general martingale transport framework, duality and uniqueness, but the inspected primary text does not provide this specific 2x3 heteroscedastic Gaussian critical p=3/4 or its sharp asymptotic scales. Other Acciaio–Marini q-Bass papers treat state-independent q and remain potential broader-theory risks; their complete material was not available in this execution.

## value

PASS

The first nontrivial martingale coupling polytope yields three genuinely distinct scaling laws separated by exact p=3/4. This identifies a natural optimizer-support boundary phenomenon and provides explicit rate constants useful in semidiscrete q_x-Bass calibration rather than routine restatement of general existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
