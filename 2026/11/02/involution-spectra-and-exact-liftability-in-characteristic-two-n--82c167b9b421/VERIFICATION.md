---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Work under substitution over characteristic two. At depth d the first possible square-difference term is (d+1)a² t^(2d+1), giving exactly the even-depth obstruction and the high-depth automatic finite involutions. If the square is nontrivial with depth r, comparing f∘f² and f²∘f in degree d+r+1 shows (r-d)ab=0 for their nonzero leading coefficients a,b. Thus at odd d any first square defect has even degree. For each even n≥2d+2 the outer term indexed n-d contributes a a_(n-d); the contribution linear in that coefficient from the inner argument and leading outer term has factor d+1=0, and two insertions involving it would have degree >n. This gives one triangular condition per even degree and no other independent conditions. Changing coefficients at degrees ≥N cannot affect the square below N+d, and thereafter this same recursion imposes all even conditions and, by parity, the entire infinite involution equation. The identity jet has an infinite lift, including at arbitrarily large odd depths by the recursion. For the total finite count let h=floor(N/2), m=floor((N-1)/2). Depths d≥h plus the identity contribute q^(N-h-1); the floor(h/2) odd depths below h contribute (q-1)q^(N-2-m) each. These give all four totals, and the odd lifting exponents descend through consecutive values ending at zero. An independent truncated-Horner exact enumeration matched both depth histograms for F2 at N=3–11, F4 at N=3–7 and F8 at N=3–6. It checks the finite lifting criterion, not infinite existence; the latter is supplied by the recursion.

## originality

PASS

Verified coverage is recorded for the finite-only spectrum and total in the later indexed all-depth census and for depth-one lifting in the later specialized record. The supported distinct claim is the full depth-by-depth finite/formal comparison, with the all-odd-depth finite-precision test, lifting fibers and resulting total and ratio. Known genuine-torsion conjugacy and bounded prime-field class counts are prior ingredients but do not give this comparison in the inspected passages. The overlap with later dated records is not evidence of priority in either direction beyond the stated scope comparisons.

## value

PASS

The all-depth comparison answers a natural finite-quotient question that conjugacy of genuine torsion does not settle: which finite solutions are actual truncations, how many exist, and how far above the given precision one must test the square to tell. The exact criterion and quantified O(1/N) scarcity (indeed Theta(1/N)) are useful across all truncation levels and even field sizes. The rationale does not treat the later matched finite census on its own as a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
