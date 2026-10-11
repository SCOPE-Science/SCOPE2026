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

The six displayed unit effects sum exactly to zero, so the finite-population weak null holds. For each of the 20 actual assignments, sharp-null Fisher imputation fixes the observed outcome vector and reassigns all 20 treatment triples. Exact-rational enumeration of the squared studentized statistic reproduces p-value multiplicities 7 at 1/10, 3 at 1/5, 3 at 9/10 and 7 at 1, with all 400 variance denominators positive. Hence the exact weak-null rejection probability at nominal 0.1 is 7/20=0.35.

## originality

PASS

Wu--Ding prove exact sharp-null validity and asymptotic weak-null conservativeness for the studentized Fisher randomization test, while emphasizing asymptotic rather than finite-sample weak-null control. Cohen--Fogarty likewise explain that sharp-null randomization reference distributions may be anti-conservative for weak nulls. Those general statements establish possibility but do not imply this exact balanced six-unit finite population, its complete p-value distribution, or the 7/20 size. Targeted searches for the exact witness/count did not locate prior coverage.

## value

PASS

The studentized Fisher test is specifically promoted for weak-null asymptotic validity. An exact balanced two-arm finite population where nominal 10 percent size becomes 35 percent is a motivated counterexample that sharply illustrates the finite-sample boundary without contradicting the asymptotic theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
