---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Translate m to zero. If s=S_1 and t=S_0/s, positive adjacent masses with p_1≥p_0 give 1<t≤2 and S_2/S_1≤2−t. The nonincreasing positive survival ratios bound the right mean contribution by s/(t−1) and the left contribution from below by Σ_{j≥1}(1−st^j)_+, using both integrable tail-sum identities. Their difference F_s(t) is strictly increasing in s. At s*=a², (1+s*)(1/a−1)=1. On [1/a,2], F_{s*} decreases strictly before t=2 and is zero at 1/a. On each remaining open interval with d active terms, multiplying the derivative by (t−1)² gives s*t^d[d(t−1)−1], so there is no interior maximum. At t_d=(s*)^(−1/d), F is 1/(t_d−1)−(d−1+s*); the function (y−1+s*)(exp(L/y)−1), L=−log s*, is strictly increasing on y≥2 since 1−exp(−v)>v−v²/2 for v>0 and L<2(1−s*). It is one at y=2, exhausting all t>1 including t=2 and ruling out any other equality. At equality S_{−1}=1, every right survival meets its geometric majorant, p_1=p_0, and the mean is zero. The resulting survivals have ratios a,a,b,b,… with 0<b<a, sum to a finite signed mean, and attain the bound. Separate exact rational arithmetic verifies the five-point IFR counterexample, with mean zero and tail 16/49. Bounded checks: `python3 /workspace/independent_reproduction.py 2` independently recovered a=0.5698402909980532659…, a²=0.3247179572447460260…, b=0.2451223337533072399…; it does not prove the continuum optimization. The frozen `verification/check.py` was inspected, not run.

## originality

PASS

The supported distinct claim is the sharp ratio-one IFR inequality and unique equality law, not a new general mean-tail theorem. The closest same-event theorem gives only 1/4 by applicable specialization. No equivalent result was identified in inspected sources; priority is qualified.

## value

PASS

Equal or increasing adjacent masses are a natural endpoint condition of the existing discrete IFR problem. The theorem raises the directly available quarter bound, supplies the actual sharp extremizer in the larger survival-log-concave class, and shows by a small exact witness why the prior three-point mechanism does not extend. Its precision is useful for anyone trying to classify the full ratio curve; it does not claim to solve that curve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
