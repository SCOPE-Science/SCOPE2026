---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The proof was reconstructed independently. For a repeated exponent \(n=p^\alpha m\) with \(m>1\), the Bertrand-prime choice gives \(t\) with \(2t+1\) prime and \(\alpha<3t-2\). The incomparable vertices \(C_{p^t}\) and \(C_{p^{t-1}m}\) cannot have a common lower neighbor because that would give a nontrivial proper divisor of \(2t+1\), and cannot have a common upper neighbor because \(2t-1\mid 2s+1\) forces \(s\ge3t-2>\alpha\). The square-free direction follows from multiplicativity and the universal top vertex. Independent exact graph construction found no counterexample for \(2\le n\le400\).

## originality

PASS

The foundational paper explicitly states the missing implication as Problem 2.9 and says the converse is clear. Fresh exact web searches and Resultary retrieval found the assigned solution itself and recent work on other invariants, but no earlier solution. The 2026 extreme-vertices paper is confined to prime-power cyclic groups and does not settle the mixed-prime diameter classification.

## value

PASS

This is a natural complete classification of a basic graph invariant for cyclic groups and closes an explicitly numbered open problem from the paper that introduced the graph. The proof also supplies a uniform structural distance obstruction, not merely a bounded census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
