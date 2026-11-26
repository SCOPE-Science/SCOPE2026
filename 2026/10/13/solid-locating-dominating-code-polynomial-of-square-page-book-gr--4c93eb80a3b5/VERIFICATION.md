---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Use the closed neighborhoods in RESULT.md lines 56–69; non-codeword traces must be nonempty and pairwise incomparable because the difference condition applies to both orders. If x is absent, any absent v_i has trace inside I_C(x), so all v_i are present. With y present the remaining outsider traces are the distinct singletons {v_i}, incomparable with I_C(x), which contains y but no v_i. Interchanging the sides handles y absent and x present. If both spines are absent the same forcing gives all page vertices, and the two outsider traces U and V are disjoint and nonempty since m≥1. If both spines are present an empty page gives traces {x} and {y}, which prohibit any other outsider. Without an empty page every outsider has a two-element trace containing the corresponding spine and a selected page mate. These traces are distinct, hence incomparable. The disjoint contributions are 2z^(m+1)(1+z)^m from one spine, z^(2m) from neither, mz^(2m) from an empty page with both spines, and z²(2z+z²)^m from both spines and no empty page. The lowest power is m+1; at m=1 the z^(2m) contributions tie and there are four minima, while for m≥2 only the two one-spine choices of lowest size qualify. At z=1 the stated total follows. The frozen checker and output were inspected, not executed; they compare actual masks and coefficients on 349,520 subsets through m=8 only. The trace argument, including sufficiency in each branch, proves the all-m result.

## originality

PASS

The distinct claim is the full family classification and code-size polynomial for square-page books, not the solid condition, general antichain theory, or known ladder minima. The strongest inspected indexed comparators either change the graph (crown and half graphs) or count a different predicate on the same square book (Roman functions and local edge metric bases). The known product-ladder minima cover the smallest two minimum-size values but not the all-code polynomial. Bounded source and catalogue checks support the distinct result, not a priority certification.

## value

PASS

The family is a natural non-ladder prism and shared-edge cycle book. Its full code-size spectrum and actual choices are useful beyond the scalar minimum bound. In particular, the exact rule that emptying one page forces every other page to be full produces a distinct coefficient contribution; it is a structural constraint, not a sampled count or a rescaled existing invariant. The result also accounts for the transition from four minimum codes on the square to two rigid minima on larger books.

The dated certificate retains the supplied scientific assessment, sources and limitations.
