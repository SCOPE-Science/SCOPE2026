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

Conditioning on the index duration, no contact to either susceptible has expectation q=L_a(2λ), and contact to one specified susceptible but not the other has probability p−q for p=L_a(λ). The newly infected person's independent no-contact event contributes p, giving r=2p(p−q). Thus r>0 selects the unique positive quadratic root for p. The nondegenerate Gamma law gives p²<q<p, so the log ratio is in (1,2). Multiplying its derivative by (1+2u)(1+u)log²(1+u)>0 gives 2(1+u)log(1+u)−(1+2u)log(1+2u), negative by strict convexity with H(0)=0. The endpoint limits of the ratio are 2 and 1. Therefore u=λ/a, then a, λ, β from h, and η from β/λ are unique, including both admissible η endpoints. At fixed shape, the m₂ derivative in λ is (q−2p)p′−(1−p)q′>0; the two-mean Jacobian in (β,η) is triangular with diagonal entries nonzero because m₁ grows with β and λ falls with η. This gives exact local fibers at all interior points by the implicit-function theorem. The variance signal has coefficient Var(I)=1/a at second order. I independently checked the rational example and an exact second-shape bracket: at a=2 and β=2(√2−1), m₂(λ=1/2)=269/625 < 82/175 < m₂(λ=3/5)=896379/1827904. Both trial intensities are interior to (β/2,β), so continuity and strict monotonicity give an exact distinct-shape match with h=1/2 and m₂=82/175.

## originality

PASS

Brooks et al. already specify the same forward model and explicitly anticipate that freeing the Gamma shape may make medium-information estimation ambiguous but that high-information outcomes may resolve it. The supported new claim is the exact global inverse from just h,q,r for these two sizes and the exact interior nonidentifiability from the two means, not the model or the qualitative proposal.

## value

PASS

This answers a concrete data-resolution question raised by the motivating likelihood study. In the smallest two nontrivial sizes the two exact means erase information even with perfect estimation, while the household outcome counts allow a unique monotone inverse. The positive variance signal of order λ² explains why population-level uniqueness need not translate into dependable estimation at weak transmission.

The dated certificate retains the supplied scientific assessment, sources and limitations.
