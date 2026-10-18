---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For each j-set J, independent size-s packets avoid J with probability product_l C(n-j,s_l)/C(n,s_l), establishing the exact PGF by factorial moments. If F has nonpositive real zeros, the hypergeometric packet update T_tF=[w^t](1+w)^n F((1+zw)/(1+w))/C(n,t) preserves real nonpositive zeros: its factorization has no zeros for Im z>0 and Im w<0; Gauss-Lucas applied in w and Hurwitz at w=0 preserve upper-half-plane zero exclusion. Iterating from F=z^n establishes every n and finite varying schedule, including empty and full packets. F(1)=1 yields a Poisson-binomial factorization. Exchangeability and stable-polynomial polarization give the strongly Rayleigh joint unseen vector; independence is asserted only for the distributional Bernoulli representation, not for actual missing indicators.

## originality

PASS

The exact per-round root-preserving transformation and its group-coupon finite-sample strong Rayleigh conclusion were not shown in the inspected group-drawing asymptotics. Borcea–Brändén–Liggett supply general stability/polarization, not an inspected statement proving this particular packet update. Brändén–Jonasson discuss stability under sampling/conditioning and could subsume an equivalent form; full text could not be inspected, so this is a substantial explicit priority risk rather than negative proof.

## value

PASS

For heterogeneous group coupon drawing, an exact Poisson-binomial representation gives all finite-sample distributional parameters and full negative association, much stronger than Gaussian/Poisson limits and useful for sharp tail probabilities; arbitrary packet sizes and joint vector properties make this a motivated structural statement rather than a routine numerical check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
