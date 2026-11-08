---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

First intervention coincides with RL among fair independent tent itinerary bits (B_{n+1},B_{n+2}); one block of length ell forbids adjacent RL in ell+1 symbols, leaving exactly ell+2 sequences, probability (ell+2)/2^(ell+1). Disjoint control blocks use disjoint symbol coordinates, so survival is the product. Splitting inequality p_c p_d-p_(c+d)=cd/2^(c+d+2)>0 yields unique minimum at one block and maximum using r=min(k,N-k+1) nearly equal lengths; infinite controls give a decay bound (3/4)^k. An independent rational cylinder enumeration verified all 510 schedules through N=8, including endpoints up to null sets. Actual verify_tent.py inspected; unrestricted theorem comes from symbolic proof.

## originality

PASS

Exact schedule-dependent first-activation law and sharp fixed-budget extrema are different quantities from attractor and period-increment classifications for binary flat-top patterns. Classical non-self-overlap word avoidance supplies an ingredient, but the dynamical first-intervention optimization in this model was not found as a published statement; residual reduction risk is explicit.

## value

PASS

Provides exact risk under every predetermined timing pattern and a sharp resource-constrained control design rule for a studied dynamical limiter; contrasts one batch with maximally dispersed control without claiming eventual attraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
