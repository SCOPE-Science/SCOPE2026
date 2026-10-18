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

For any equal-census positive abundance triples, majorization comparison gives a fixed rarefaction order by discrete convexity of j↦binom(N−j,m). For incomparable triples, after sorting and interchanging, a>A and c>C, and signed abundance counts have three ordered blocks of first-cumulative support. Twice summation by parts produces H_m=Σ_j G_j binom(N−j−2,m−2), with G_j sign pattern negative then positive. The binomial kernel has the reverse-monotone-likelihood-ratio cross product for j1<j2,m1<m2 (higher depths favor lower abundance index), so its negative/positive contribution ratio is monotone; hence H_m has at most one sign change. Independent exact rational check: for x=(6,2,2) vs y=(5,4,1), (R_2,R_3,R_4,R_9) are x=(73/45,61/30,163/70,3), y=(74/45,41/20,242/105,29/10). The crossing at m=3→4 proves sharpness. The source verifier fully enumerates profiles through N=35 and verifies binomial-kernel minors; the proof covers every finite N without reliance on finite enumeration.

## originality

PASS

The paper-level ecological literature defines exact individual-based hypergeometric rarefaction and documents arbitrary species-accumulation crossings, but the targeted primary materials do not give the all-N three-species one-reversal ceiling and endpoint certificate. The result is best-of-knowledge original given verified integrated-histogram obstruction; earlier total-positivity/majorization theory is methodologically prior and may provide a hidden equivalent abstraction.

## value

PASS

An exact no-return principle for three-species richness rankings answers a concrete ecological comparison question in the first nontrivial equal-richness case; a sharp crossing witness and two-depth certificate make the all-census theorem useful. The variation-diminishing abundance constraint is not an elementary sample table recomputation and does not follow from knowing that crossings can happen.

The dated certificate retains the supplied scientific assessment, sources and limitations.
