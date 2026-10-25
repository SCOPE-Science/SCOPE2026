---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For rational line L with F_q basis U,V, each Frobenius binomial restricts to its corresponding cross-product coefficient times (s^q t−s t^q). This factors curve|_L as a product of a simple rational-point factor and Q_L, the restriction of (c+kb)X²+aY²+bZ². Q_L is not identically zero: a rank-three ternary quadratic has no 2-plane totally isotropic; rank-two such a plane must contain its radical axis, which fails for L in each parameter case; rank-one gives a nonzero square. Consequently 0,1,2 rational roots of nonzero binary Q correspond respectively to 0 tangencies, a double rational flex of exact contact three, or two rational tangencies. In odd characteristic its discriminant equals −4λ²(a³b+b³c+ac³+k(b⁴+abc²)) via the adjugate identity. Counting each rational point’s unique tangent gives 2B+F=N and counting rational lines gives zero-tangent count E=B, with F=#D_k(F_q), N=q²+q+1. For smooth quartic genus 3 gives Hasse |F−(q+1)|≤6√q, |B−q²/2|≤3√q. Fresh independent direct tangent-gradient tests for five prime fields q=3,5,7,11,13 exactly match quartic F and B. Minor proof typo: the rank-one γ-only line is Y−kZ=0 (source writes Y+kZ=0), but Q_L=bZ² still nonzero in either expression, so theorem and nonvanishing conclusion are unaffected.

## originality

PASS

Asgarli–Ghioca introduced this exact degree-(q+3) plane-filling family and its rational smoothness parameter condition; a separate paper studies tangent-filling coverage, a different incidence predicate. Neither mathematically read source supplies its dual quartic discriminant and exact flex/bitangent counts. Standard Hasse–Weil and adjugate algebra are acknowledged inputs. No equal or stronger targeted result appeared in Resultary’s high-level matches; classical dual-curve equivalents remain priority risk.

## value

PASS

The result reduces rational tangent fibers of a high-degree Frobenius plane-filling curve uniformly in q to rational points of a fixed quartic (genus three when smooth), yielding exact three-type incidence census and square-root errors. This is a natural structural arithmetic-geometric bridge rather than an arbitrary finite table or mere restatement of smoothness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
