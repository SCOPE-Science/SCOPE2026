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

For rank-one A the conditions at C=0 identify B with arbitrary maps k²/im A→ker A, giving q possibilities; A=0 gives q⁴ and invertible A gives one. With (q²−1)²/(q−1) rank-one matrices and (q²−1)(q²−q) invertible matrices this gives q²(3q²−2). At a nonzero nilpotent C, both factors centralize C, whose algebra is the dual numbers. Two nonunits there multiply to zero, whereas two units cannot give a nilpotent product. Choosing which factor is the unit and then the unit itself determines the other factor uniquely, giving 2q(q−1). The orbit of the sole nonzero nilpotent Jordan form has size |GL₂|/[q(q−1)]=q²−1. Summing gives the stated total. The q scalar centralizers have size q⁴, all others q². For independent factors, rank-one A imposes one nonzero linear trace condition, rank-two A gives q² choices and rank-zero A gives q⁴; the unrestricted count is q⁴(2q²−1). Division and subtraction give the positive factored expression and the stated asymptotics for all prime powers, including characteristic two. The separate exhaustive replay uses C²=0 rather than a trace/determinant criterion and enumerates the unrestricted comparison as well as each commuting nilpotent fiber over F₂, F₃ and F₄.

## originality

PASS

Credit Huang for the zero fiber, Feit–Fine for the commuting-pair denominator, and the earlier indexed work for the unrestricted benchmark. The supported distinct claim is the nonzero nilpotent-product stratum with arbitrary commuting factors and its exact consequence for conditional enrichment. No inspected competing theorem counts that stratum or mechanically specializes to it; the extra factorization step in the centralizer is necessary.

## value

PASS

The product-fiber profile is a natural refinement of both the standard commuting-pair statistic and nilpotent-product probability. It supplies an independently useful exact dimension-two baseline across all finite fields: conditioning strictly enriches nilpotent products for every q, by a leading factor 5/2, and the nonzero stratum contributes at the same order as the zero one. This is not a new claim about the previously known zero locus or unconditioned probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
