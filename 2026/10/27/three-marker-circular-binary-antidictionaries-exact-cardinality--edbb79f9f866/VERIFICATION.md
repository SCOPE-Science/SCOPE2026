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

For a word using both symbols, let C(k) be periodic factor complexity and B(k) the bispecial count. Counting missing two-sided extensions with both one-sided extensions present gives m(k+2)=2C(k+1)-C(k)-C(k+2)+B(k). At length at least the least period, the phase is determined up to equivalence, so the complexity difference vanishes. The total is 1+sum B(k). The maximal gap gives exactly M zero-only bispecials including the empty word. After dihedral reordering, the one-marker outer-gap contexts are (a,b),(b,c),(c,a) with a<=b<=c. In each coordinate an eligible context must meet the threshold and another must exceed it. This gives no one-marker bispecial with all gaps equal, just (a,a) with a repeated gap, and (a,a),(a,b),(b,a) with distinct gaps. An internal gap has two phases only if repeated (or all equal); in the two-phase case the outer contexts are swapped with distinct entries, forcing both thresholds to be the smaller entry. With three or more markers, two complete consecutive gaps fix the phase unless all gaps are equal, in which case every marker already fixes the least-period phase. Thus the bispecial totals are M, M+2 and M+3. For 111 the constant language has exactly the single-letter obstruction 0. Writing S=n-3, maximum equality in the repeated or distinct cases requires the smaller gaps to sum to 0 or 1 respectively, and balanced two-equal triples attain the lower bound when S is not divisible by 3. This proves the formula and extrema for unbounded gaps, including zero gaps and nonprimitive words.

## originality

PASS

Pass for the all-gap weight-three classification and its extremizers, not for novelty of the positive distinct-gap count in isolation. The strongest prior Resultary finding gives an even stronger antidictionary description on that subclass. It excludes zero gaps and repeated gaps, and therefore does not cover either maximizing family or the all-gap theorem. The published length bound is also prior; it does not identify the weight-three equality cases.

## value

PASS

This gives the exact antidictionary size without enumerating factors for the entire natural three-marker class. It resolves when marker contexts coincide, including adjacency and reduced period, and supplies a sharp equality classification and minimum at fixed length. These uses go beyond the generic n bound and the already known positive-distinct count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
