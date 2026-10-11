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

A fresh independent enumeration over all 6^3 student-preference profiles and all 6^3 school-priority profiles reimplemented deferred acceptance and direct Pareto comparison against all six perfect matchings. It reproduced exactly 1296 inefficient profiles; priority histogram {0:42,4:36,8:126,12:12}; rank multiset counts 648 each for (2,2,2) and (2,2,3); and for every inefficient profile exactly one Pareto improvement with exactly two strict beneficiaries. The package verifier additionally cross-checks two DA implementations, stability/student-optimality, a trading-cycle criterion, all 16 strict 2x2 profiles, and the Ergin-cycle classification. The finite claim is therefore exhaustively established rather than inferred from sampling.

## originality

PASS

Ergin's acyclicity theorem and Narita's corrected proof characterize the priority structures for which deferred acceptance is always student-Pareto efficient as preferences vary, but they do not enumerate the three-by-three labeled profile incidence, the 0/4/8/12 priority histogram, or the unique two-student repair structure. A fresh Resultary search for the exact 3x3 counts returned no covering published finding.

## value

PASS

Three by three is the first balanced strict market in which deferred acceptance can be Pareto inefficient, so this is a motivated finite boundary rather than an arbitrary census. The exact incidence, priority-stratum histogram and unique two-student repair structure give a compact benchmark for mechanism-design examples and computational checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
