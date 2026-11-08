---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The greedy arch factorization yields a complete labelled finite-state recurrence A_j=1+zuE+1_{j<h}zA_{j+1}, E=1+zA_1+1_{h>=2}zA_2. Solving gives F_h=(1+2zS_h+uz^(h+1))/(1-uz²T_h). Positive polynomial supports show all and only n from 2k to (h+1)k+h, plus the exact boundary multiplicities; the h=1 alternating case is separate. For fixed h>=2 the lengths 2 and 3 in z²T_h are coprime, yielding a unique analytic dominant pole; quasi-powers differentiations give the stated mean, variance and Gaussian CLT. A fresh independent brute-force enumeration of all admissible binary words for h=1..4 and n=0..13 confirmed 56 full coefficient rows against the rational formula. These finite tests do not prove the asymptotics.

## originality

PASS

Best-of-knowledge differentiated same-object formulations and stronger-coverage implications; no confirmed statement-level coverage found. This is a qualified priority decision, not evidence of exhaustive absence.

## value

PASS

A uniform exact refinement of the subsequence universality index under a natural bounded-homopolymer constraint, including sharp possible-index intervals, extremizers and fluctuations. The run cap matters in coding and constrained sequence models; the result is not a renaming of unrestricted enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
