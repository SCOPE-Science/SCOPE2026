---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For every n>=1, a monotone regressive idempotent has image=fixed set F containing 1. For i, e(i) is fixed <=i, and monotonicity gives e(i)>=every fixed j<=i, so e=e_F is the floor to F; conversely each floor is an idempotent. If a common-fixed-point gap contains both F-only and G-only sites, take a later site x of one type with an earlier site u of the other. At x, one composite yields u while the reverse yields e_F(u)<u (or the symmetric counterpart), so the maps do not commute. If no gap contains both types, one floor map collapses each whole gap to its left common endpoint, the other fixes it, and both orders equal e_H for H=F∩G. For a fixed H, each gap of ell noncommon sites admits 2^ell F-only/absent words or 2^ell G-only/absent words, with the all-absent word double-counted, hence 2^(ell+1)-1 choices. Independence across gaps gives N_n(H)=product_i (2^(ell_i+1)-1). The formal OGF B(z)=1/((1-z)(1-2z)) gives y/(1-(3+y)z+2z^2), and selecting k common fixed points gives c_{n,k}=[z^(n-k)](1-z)^(-k)(1-2z)^(-k). Boundaries n=1, H={1}, terminal gap and ell=0 are included; map composition is ordinary rightmost-first and ordered pairs are counted. Independently reimplemented retraction enumeration for all ordered pairs n=1..9, verifying both composition orders, every H fiber and all coefficient rows; independently enumerated all Catalan maps and their idempotents for n=1..8 (Catalan counts 1,2,5,14,42,132,429,1430 and idempotents 1,2,4,8,16,32,64,128). These finite checks corroborate only; the proof above establishes every n.

## originality

PASS

Best-of-knowledge priority for the complete gapwise commutation classification and multiplicities at each specified product e_H, not for the known idempotent parametrization, rank-triangle coefficients or total sequence. Ganyushkin–Mazorchuk (2011) Theorem 1(iii),(viii) counts idempotents and identifies the Catalan monoid; Pantazi–Spircu (2016/2017) Lemma 2 and §§4–5 give segment commutation/absorption, idempotent decompositions, and dominance products but not an explicit all-pair fiber theorem. OEIS A206306 already tabulates the entire rank coefficient triangle, and A007070 the total recurrence; those consequences are excluded from novelty. Actual Resultary semantic searches and targeted semigroup/full-transformation/dual-convention literature searches found no direct dominating theorem. Specialist semigroup literature remains a meaningful priority risk, and this PASS is not a guarantee of historical uniqueness.

## value

PASS

Commuting idempotents and multiplication fibers are intrinsic structural data for the Catalan transformation monoid, not an arbitrary numerical slice. The formula gives a complete all-n description of a natural family of multiplication fibers over concrete idempotents. At fixed rank two in C_4, e_{\{1,2\}} has 7 commuting pair factorizations and e_{\{1,3\}} has 9; thus a rank-only table genuinely loses structural information. The gap independence gives a clean product law, and summation realizes the previously known Mersenne/Riordan triangle as a natural semigroup rank profile. The exact fiber counts could be used in studies of idempotent partial multiplication, probabilistic random retractions and subsemigroup structure, without requiring a larger downstream theorem. This is more than merely reproducing the known OEIS table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
