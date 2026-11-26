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

For a path edge, reroot at the target side and use first-step equations: the expected crossing time from the adjacent root-side endpoint equals one plus the sum over its off-target neighbors of one plus their mean return time. Induction on the root-side component size M gives 2M-1; summing gives the forward identity, and commute gives 2ND_N. Every label below b is on the root side of its path edge. The later descent indicators from b either become constantly one or, before that happens, alternate: two zeros are absorbing and cannot reach c_N=1. Each continuation of alternation needs a consecutive second-predecessor choice, so the excess M_b-b is at most L_N+1 (zero at b=N). A union bound on all starting positions and Borel–Cantelli give L_N=O(log N) almost surely, making H⁺−2A_N negligible at scale N^(3/2). Backwards exploration samples previously unseen iid attachment choices at distinct labels; at label 1 the forced final edge preserves all positive labels, so the same bounded-step renewal sequence gives jointly D_N=K_N and A_N=sum of K_x for x=1,…,N in law. A separate enumeration compared the full positive-path profile law and confirmed the deterministic bound for N=1–11 at p=1/2. For the unbounded proof, set K_0=0; the overshoot 0≤S_(K_x)-x≤1 composes the centered partial-sum Donsker process with K_floor(Nt)/N→t/μ uniformly and multiplies it by -1/μ. Brownian scaling then gives -sqrt(v)/μ^(3/2) times standard Brownian motion. Riemann summation and endpoint evaluation give the pair of Brownian functionals ∫B and B(1)−∫B (with common prefactor -2sqrt(v)/μ^(3/2)); their variances are 1/3 and their covariance is 1/6. For the almost-sure conclusion the overshoot yields uniform deviation of K from x/μ bounded by (1+max_(k≤N)|S_k−μk|)/μ. Hoeffding plus a union bound makes linear deviations summably unlikely. Applying this to the fixed-N joint tree laws and then Borel–Cantelli proves the result in the original environment, without a false common renewal coupling across N.

## originality

PASS

The supported distinct claim is the joint conditional-mean law, covariance and two almost-sure laws at the endpoints of the finite birth-label prefix. Tang–Wang–Wu construct the same tree and supply its infinite geometry, while the same-tree Resultary ray-index result has close regenerative ingredients but a different index and a single hitting direction. The matching sources are compared below rather than dismissed based on title or date.

## value

PASS

The deterministic commute identity controls only the sum. A joint area-and-endpoint representation resolves the fluctuation split and gives the exact universal half-correlation of the two conditional means at the same finite endpoints. That covariance is useful for joint prediction and directional asymmetry and is not determined by either a scalar ray limit or the commute law alone. The main mechanism is the uniform pathwise control of discarded branches combined with a common inverse-renewal profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
