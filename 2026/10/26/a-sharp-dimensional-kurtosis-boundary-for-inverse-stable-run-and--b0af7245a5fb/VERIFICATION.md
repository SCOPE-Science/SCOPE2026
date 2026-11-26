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

An independent operational-time check uses the renewal equation at the first Poisson redraw: the projection's characteristic-function Laplace transform is A/(1−αA), where A=E[(w+α−ikvY)⁻¹] and Y is the initial directional projection. Expansion at k=0 with μ₂=1/d and μ₄=3/[d(d+2)] gives the recorded transforms, with the fourth coefficient including both the single-direction μ₄ and repeated-direction αμ₂² terms. The independent inverse clock inserts s^ν for w and multiplies by s^(ν−1). With no redraw the operational jth even moment starts at v^j μ_j u^j; the redraw error is O(u^(j+1)) as u↓0. The poles at zero of the operational transforms give growth 2v²μ₂ u/α and 12v⁴μ₂² u²/α², with polynomially bounded remainders of orders 1 and u+1. Averaging using E[(E_ν(t))^j]=j!t^(jν)/Γ(1+jν) justifies both kurtosis limits without a Laplace-to-pointwise inference. Continuity follows also from the marginal clock scaling and the bound on displacement; the no-redraw event gives positive variance for positive t. Digamma monotonicity gives the unique short-time boundary and strict late positivity for 0<ν<1; the intermediate value theorem yields at least one finite zero for ν>ν_d. The derivative F′(1)=14 verifies the large-d expansion; an independent numerical bisection gives ν₂≈0.693572909926177. Redraw rate α means flip rate α/2 in d=1. No uniqueness, global positivity below threshold or sign at equality is inferred. The supplied check.py was inspected, not executed.

## originality

PASS

Credit is limited to the exact dimension-dependent short-time sign boundary for the specified time change, combined with a strictly positive late limit and the resulting sign reversal. The model and inverse-stable kernel are known; the operational fourth transform is directly covered and the physical fourth transform follows mechanically by subordination, so neither moment transform by itself supports originality. The strongest inspected statements do not classify the inverse-clock kurtosis signs. Their combination supplies inputs for the claim, but requires analysis of the two moment scales, the normalized limits and the monotone dimension-dependent boundary; it is not a specialization of their stated sign classifications. This is a bounded comparison, not a priority certification.

## value

PASS

The sign boundary distinguishes ballistic directional mixing from the macroscopic randomness of the inverse clock and gives a concrete, dimension-sensitive crossover condition. It applies to a natural projection observable and can guide a researcher beyond MSD-based comparisons; it does not overstate what is known about the full time profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
