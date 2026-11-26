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

Finite norm implies ∫_0^a |f|<∞ for each a<1, since otherwise the norm is infinite on (a,1). Power maps are nonsingular on the open interval, so composition is well-defined on equivalence classes. For 0<α≤1, the primitive after substitution is α^(−1)∫_0^(x^α)|f(u)|u^(1/α−1)du, at most α^(−1)x^(1−α)F(x^α). Dividing by x^σ converts this to α^(−1)x^((1−α)(1−σ))H_σ f(x^α); the outer Jacobian yields exactly the exponent (1−α)(1+p(1−σ))/α in the p-th power estimate. This exponent is positive if α<1, proving strictness for every nonzero f. At α=1 the identity attains its norm. Integrating a right-end indicator yields ε^(p+1)/(p+1)(1+O(ε)); its preimage has width ε/α+O(ε²), so the optimal bound follows. For α>1 the left-end indicator's p-th norm equals r^(1+p(1−σ))/(1+p(1−σ))+r^p∫_r^1 x^(−pσ)dx. The resulting leading powers are p for pσ<1, p with an extra log(1/r) at equality and 1+p(1−σ)>0 for pσ>1. Replacing r by r^(1/α) therefore makes the norm ratios divergent even at pσ=1. This suffices for failure of boundedness, without assuming or asserting anything about the domain of an unbounded realization. As a separate check, at p=1 Tonelli gives weighted L¹ with weight W(u)=∫_u^1 x^(−σ)dx, so composition has density ratio (1/α)u^(1/α−1)W(u^(1/α))/W(u); at σ=0, α=1/2 it is 2u(1+u), with essential supremum 4 and no norm-attainment. `python /workspace/review_checks/frozen_probes.py` checks that example and a closed-form p=2,σ=1/2 endpoint test. The proof, not the bounded replay, covers the full parameter set.

## originality

PASS

The exact norm and nonattainment profile for power substitutions across all stated p and σ survives the comparison. The earlier incorrect measure-distortion norm assertion does not establish it, and the counterexample to that assertion is already known and not credited as new here.

## value

PASS

Power maps form a natural one-parameter nonlinear semigroup and a concrete test of how composition interacts with a non-rearrangement-invariant norm. The exact uniform constant, strict nonattainment, and transition to divergence from the opposite endpoint resolve the entire stated range. They explain precisely why a simple measure-distortion heuristic misses a factor in this natural case, rather than merely verifying a known endpoint value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
