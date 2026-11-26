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

For the natural past filtration, the directed-pair independence makes the three centered noise increments before projection conditionally uncorrelated, with variances h²B_i/(1+a_i)². The deterministic centered multiplier is 1−6γ, and the projection onto the disagreement plane has diagonal 2/3. Thus its conditional squared norm is exactly the stated recursion. With ΣB_i=6S, the supremum of the one-step ratio over S>0 is ρ=(1−6γ)²+4h²: all sufficiently small rescalings of any fixed nonconstant state approach that ratio. Solving ρ=1 for the positive gain gives γ_c, and ρ>1 yields actual local one-step expansion. For opinion gaps p,q,p+q, the sum of pair products of the three squared gaps is (p²+pq+q²)²=9S²/4. Hence Σa_i B_i=9S²/2. At γ_c, using a_i≤2S and 1−(1+a_i)^(−2)≥a_i/(1+a_i) yields the claimed drift. The convex function S²/(1+2S), the supermartingale bound ES_t≤S₀, and reciprocation of u_(t+1)≤u_t−3h²u_t²/(1+2S₀) give the displayed rate for u_t=ES_t (zero stays zero). Supermartingale convergence and Fatou give the a.s. conclusion. Below threshold, the expected disagreement decays geometrically, and the sum of second moments of the mean-martingale increments is finite (each bounded by (2h²/3)ES_t), proving individual a.s. and L² convergence to the common limit. At equality, constant modulation gives ES_t=S₀ exactly. Critical mean-square agreement means E||x−mean(x)1||²→0; it does not claim E[S_t²]→0, convergence of the common mean, or a matching decay lower bound. Supercritical one-step expansion does not establish long-run divergence. The frozen verify.py and VERIFICATION.md were inspected, not executed; the finite Rademacher checks do not substitute for the moment and supermartingale arguments.

## originality

PASS

The equation is a specialization of Shang's pair-noise model; the earlier sufficient consensus theorem and the standard martingale tools are not novelty claims. The supported difference is the exact uniform one-step frontier together with the nonlinear critical drift and the constant-modulation contrast for the specified discrete three-agent equation. No inspected statement yields those endpoint results for this model.

## value

PASS

The three-agent system is the full interaction of the smallest genuine three-body hyperedge. Its exact variance-neutral gain is a natural endpoint at which the uniform contracted factor disappears. The nonlinear modulation then yields almost-sure and quantified mean-square agreement even though the constant modulation retains its second moment. This addresses a concrete stochastic endpoint obstruction without claiming a global long-run transition or mere novelty for standard inequalities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
