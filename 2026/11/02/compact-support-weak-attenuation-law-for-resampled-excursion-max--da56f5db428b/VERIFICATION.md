---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Solving the two-boundary difference equation gives H=p/Σ_i T_i, including the probability p of taking the initial step. For fixed p in (0,1), ε log T_floor(u/ε) converges uniformly on compact u-intervals to F(p,u). Its strictly increasing u-derivative gives the stated sign split. When F(p,t)>0 the final term, even at index floor(t/ε)−1, grows exponentially. When F(p,t)<0, the early terms are uniformly geometrically bounded and converge termwise, and the remaining O(1/ε) terms are exponentially small by uniform negativity away from zero. Thus the positive exceedance limit is 2p−1 below t_c(p) and zero above it. This proves conditional weak convergence at its continuity points for each fixed p and hence joint convergence by integrating bounded test functions; replacing a floor by a ceiling at a fixed positive continuity threshold gives the same limits. Strict decrease of F in p and continuity at p=1 (integrable log singularity at u=0) give the unique increasing inverse p_t. Integration gives p_t(1−p_t), the 3/4 atom, absence of an atom at the upper endpoint, and the marked density by normalization. At the upper edge, on a fixed small u-interval, 1/u−1/(e^u−1) is bounded; the difference between the two corresponding log(1+δ·) integrals is therefore O(δ). The model integral gives δ log(1/δ)+O(δ) uniformly near t_*, and the positive derivative in t at t_* yields the stated edge constant by inversion. Independent numerical integration gives t_*=1.7054281548003088645…; this is corroboration, not proof. The provided checker and recorded output were inspected without running the supplied script.

## originality

PASS

Yoshida's exact finite-scale law and resampled excursion model are directly credited. The distinct result is the singular joint limit for that model, its uniformly mixed law, and the logarithmic endpoint with an explicit constant. Neither the exact-model source nor the strongest inspected analogous sources give that package. This judgment does not establish priority.

## value

PASS

This extracts an explicit single-excursion scaling law from an exact but ε-dependent hitting formula. The phase boundary separates microscopic from macroscopic excursions conditional on p, and the mixed law predicts both the bias of environments seen in tall excursions and a logarithmically thinned upper edge, which cannot be read from a support bound alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
