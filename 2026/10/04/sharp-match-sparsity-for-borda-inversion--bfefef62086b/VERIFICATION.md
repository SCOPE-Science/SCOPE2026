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

Reduced strict reversal forces survivor win totals \(r_{i+1}-r_i\ge1\); full strict reversal forces \(w_i-w_{i+1}\ge1\). Writing \(w_i=r_i+q_i\) yields \(q_i-q_{i+1}\ge2\), hence the deleted player participates in at least \((n-1)(n-2)\) matches. Also \(r_{n-1}\ge n-2\) and strict full scores imply \(w_i\ge2n-3-i\), whose sum gives \(3\binom{n-1}{2}\). The explicit decisive-match construction attains both bounds; the \(n=3\) load case is checked separately.

## originality

PASS

Fresh Resultary search returned no Borda inversion sparsity theorem. The exact Chèze--Fieux source proves existence of the inversion paradox for Borda and frames the same deletion reversal, but its current accessible abstract contains no extremal match count or maximum-player load. The frozen package cites and analyzes its few-matches discussion; this round independently compares the final theorem against the current primary statement and finds no implication from mere existence to sharp sparsity.

## value

PASS

The motivating literature treats large schedules as a realism defect. Total match count and maximum participant load are canonical sparsity measures, and the theorem gives complete sharp formulas for every \(n\), with one construction attaining both.

The dated certificate retains the supplied scientific assessment, sources and limitations.
