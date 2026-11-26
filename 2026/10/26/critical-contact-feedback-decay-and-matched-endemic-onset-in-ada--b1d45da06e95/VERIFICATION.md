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

For the stated recovery-time-normalized ODE the unit square is positively invariant, initially positive y stays positive, and strict creation gives k_min>0. Direct quotient differentiation gives Z'≤0 and the stated expansion of K, including B(0)=0. The positive part of z−z0 is bounded by its initial excess times exp(−k_min t). Below threshold this gives negative asymptotic log-growth bounded away from zero. At threshold retain the −y² term; multiplying by exp(−integral of the decaying upper error coefficient) gives y=O(1/t), then scalar relaxation gives z→z0. The ratio u=(z−z0)/y obeys u'=−(k+y'/y)u+k(Z(y)−z0)/y. Here y'/y→0 and k→k(0)>0, so the coefficient remains strictly stable at large t; subtracting Z'(0) leaves forcing tending to zero, and variation of constants gives u→Z'(0). The exact derivative (1/y)'=1−tau_c u+tau_c(z−z0) tends to K≥1, proving both critical limits. For r>0 the left side of tau(1−y)Z(y)=1 is strictly decreasing from 1+r to zero. Its first-order excess is r−Ky; the positive derivative gap and a one-sided C² expansion (or a local C² extension for IFT) give the claimed O(r²) branches. Common scaling of the contact rates cancels in Z and its slope. For attraction, the endemic Jacobian has both diagonal terms negative and off-diagonal terms of opposite weak signs. Independently closed the boundary limit-set step: above threshold choose δ>0 with tau(1−δ)Z(δ)>1. On any episode y≤δ, uniform scalar relaxation from z≥0 toward a target at least Z(δ) forces log-growth positive after a fixed time T independent of the episode; during the first T, y'/y≥−1. Consequently y is bounded away from zero for every fixed initially positive trajectory. The y=1 and z=0,1 sides are then uniformly excluded from the omega-limit set by the strict inward bounds (in particular B is bounded below on the persistent y range). If an interior limit set avoids the unique sink it would contain a periodic orbit by planar limit-set theory, contrary to the negative Dulac divergence; if it contains the sink the whole trajectory converges to it. This works also for a disease-free equilibrium at z0=1. The symbolic example gives (z0,Z',K)=(1/2,−3/8,7/4), consistent with the stated signs and normalization. Inspected verify.py, requirements.txt and VERIFICATION.md; finite integration is corroboration only.

## originality

PASS

The distinct supported claim is an explicit general response-derivative prefactor for both the global critical decay and the nearby endemic onset, with its contact-coordinate limit, in the same one-community scalar-feedback model across both allowed baseline regimes. The generic transcritical matching pattern, the old model and threshold, earlier qualitative dynamics, and published solvable onset examples are not new.

## value

PASS

An unresolved equality regime of a natural existing two-dimensional model is quantified, not just declared stable. The result identifies the same response-dependent constant in the critical decay and static onset, distinguishes the contact slope from mere prevalence decay, and works for unprepared initial contacts and boundary baseline cases. The explicit coefficient and the global quantifier are useful even though the local transcritical mechanism is standard. It is a deterministic model result, not a claim for stochastic populations or nonmonotone and multigroup extensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
