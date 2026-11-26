---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a length-ell factor at phase r, the earliest subsequence embedding uses one copy of P plus one for each descent. There are ell-1-floor((r+ell-1)/q) descents. Thus r must be at least A=(q-1)ell-qm+1, and the actual factor starts give 0<=r<=min(q-1,qn-ell). With 1<=ell<=qn, nonemptiness requires just A<=q-1 and A<=qn-ell, respectively equivalent over the integers to ell<=m+ceil(m/(q-1)) and ell<=m+n-1. This proves the length and the entire phase interval directly, including ell=1, n=1 and q=2; different phases have different first letters. The equal-power simplification is valid for q>=3,m>=2, and the alternating two-letter subsequence proves the claimed linear lower bound on the gap. The transition-window proof has a harmless empty-window edge case at t=0 (there need not be a first increasing edge); the interval proof covers it directly. Independently, for q=3,m=n=2 the only optimal factors are 102 and 021. The 567 parameter cells and 70,756 per-factor checks are recorded supporting results, not an independent run or the basis of the theorem.

## originality

PASS

The supported distinction is the symbolic LCSS length and exact phase classification for opposite periods with independent exponents. Ordinary-LCS information for the same words is not new; the gap is a consequence of the LCSS theorem, not a new ordinary-LCS theorem.

## value

PASS

Opposite orders are a natural tractable stress test of the asymmetry between LCSS and LCS. The result solves the length, distinct witnesses and phase count for every pair of exponents, and provides a fixed-alphabet linear separation. It gives a reusable exact benchmark without claiming a general algorithmic improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
