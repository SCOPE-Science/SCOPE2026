---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The actual RESULT.md writes y=R0² as the larger root of P(y,x)=y²-[Ax²+B(1-x)²+C]y+ACx². At x<1, P(C,x)<0 and Py at the larger root is positive. Solving Px=0 with P=0 yields y=Ax and the unique interior critical x*=(B+C)/(A+B), admissible only A>C. x(p) increases from x0 to 1, proving all boundary cases and the stated p*. I independently used exact rational arithmetic to reproduce quadratic, x*=2/5, p*=5/8, threshold polynomial P(1,x(p))=[6-80(p-1/2)^2]/[25(5-4p)^2], and endpoint signs; the strict-subcritical set follows because the smaller root stays below C=3/5. Source’s 2026 paper supplies only the underlying next-generation expression. The p=1 reducible case is evaluated by continuity, not assumed human invasion.

## originality

PASS

The full source-specific unique optimizer and two-sided *p*-window are not the reproduction-number expression in Peterson et al. or the separate published mathematical correction of its Appendix threshold rule. A related published two-host vector-preference optimizer motivates priority caution, but uses a different network and variable. Best-of-knowledge PASS, not absolute novelty proof.

## value

PASS

A mathematically meaningful optimization of a natural residence-control parameter in a specific host-vector epidemic system: an exact interior minimizer and subcritical window, with a genuine wildlife-only p=1 interpretation boundary. This supplies a usable analytic diagnostic rather than an arbitrary numerical point; no claim of seasonal or intervention efficacy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
