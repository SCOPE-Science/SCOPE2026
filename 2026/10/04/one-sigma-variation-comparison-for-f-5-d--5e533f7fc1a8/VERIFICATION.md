---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The primary F-distribution paper reduces denominator-step monotonicity to inequalities (4.1) and (4.2), and its odd-numerator Section 5.2 gives the finite-sum sufficient inequalities (5.2) and (5.3). At numerator degree five those sums collapse to the submitted scalar forms. The inspected verifier uses outward rational square-root intervals to exhaust every integer \(5\le d\le26\), and exact resultants plus Sturm root counts for the infinite tails: independently replayed certificate structure gives the degree-26 no-root polynomial for the upper bound, the quartic for \(z-1\), and the degree-22 no-root polynomial for the lower endpoint. The endpoint-crossing quartic has the claimed sign split at 14. These exact certificates, not finite extrapolation, establish \(p_{d+2}<p_d\) for all integers \(d\ge5\). The chi-square limit then follows by Slutsky, and the cited Gamma theorem supplies the strict Gaussian comparison. RESULT.md has one harmless notational typo in the displayed \(M_d\): the previously defined variable \(u\) is printed once as \(\nu\); the verifier and surrounding derivation unambiguously use \(u\), so the theorem/proof content is reconstructible without changing the scientific conclusion.

## originality

PASS

The complete 25-page primary paper was inspected, including rendered pages 24-25. It proves the conjecture only for numerator degrees 1 through 4, then Section 5.2 explicitly treats odd \(d_1\ge5\), derives inequalities (5.2) and (5.3), and closes by saying the conjecture would be resolved if those two-variable inequalities could be established. The audited result solves exactly the first open odd numerator, \(d_1=5\), for every admissible denominator using exact certificates. Targeted Resultary/web searches found no later source covering this case.

## value

PASS

This is the first unresolved numerator degree in an explicit published conjecture, and the result proves the full infinite denominator range rather than a finite sample. The exact Sturm/resultant certificates resolve a natural boundary case and establish the conjectured one-sigma comparison for numerator five.

The dated certificate retains the supplied scientific assessment, sources and limitations.
