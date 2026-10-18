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

PASS: For upward-open thresholds U_t the raw box and diamond indicators are exactly 1[a_i≥t] and 1[b_i≥t], with (a,b)=(m,−1) for empty rows. Both openness conditions force weakly increasing minima/maxima and forbid mixing empty/nonempty rows; for nonempty rows all interior membership choices are independent and contribute 2^max(b−a−1,0). Interval-row pairs biject to two-row SSYT via (a_i+1,b_i+2), yielding hook-content formula. A finite weighted multichain rational generating function has unique largest weight 2^{m−2} at (0,m−1), giving the exact C_m residue and 4^(−r) fraction; lower poles have at most half that weight. Independent exhaustive semantic check of 74,954 relations for all 1≤r,m≤4 gives 3958 qualifying and 960 interval-valued or empty; diagonal count 2,7,80,2855,374660. Finite checks corroborate, infinite theorem follows analytically.

## originality

PASS

PASS: Best-of-knowledge PASS: finite-poset semicontinuity criteria of Barmak–Mrozek–Wanner, Collinson modal relational continuity, and classical hook-content tableaux all predate this work. The claimed contribution is the unrestricted weighted count over *arbitrary* row interiors and exact fixed-target 1/4 exponential decay, neither automatically deduced by prior structural characterizations. Older isotone-relation enumeration may be hidden under alternate terminology; record risk.

## value

PASS

PASS: Complete enumeration of natural two-sided continuous relations on finite Alexandrov chains, with a weighted tableau formula, tractable transfer count, exact small diagonal values, and uniform-in-fixed-m 1/4 probability decay. This is substantive combinatorial enumeration beyond tautological semantics and may be reused in modal finite-model counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
