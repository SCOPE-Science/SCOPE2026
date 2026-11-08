---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Derived the actual core update from n neighbors: for n=2m the next core is 0, old leaf vector, or 1 according as core weight is <m, =m, or >m; for n=2m+1 the two intermediate cases are complement(c)∩leaf and complement(c)∪(c∩leaf). Swapping core and leaf on the weight-m layer gives B=binom(n,m) even fixed-points B+2 and two-cycles B(B-1)/2; odd support-disjoint/covering cases give exactly B(m+2) two-cycle orbits, each basin 2^(m+1). Other states reach a homogeneous fixed point by <=3 updates; n=2,3 by <=2. Thus F^5=F^3 and exact entry-time formulas and Stirling asymptotics follow. Independent from-scratch adjacency-list majority transition enumerator n=2..6 checked every labelled initial state (sum 4^n=5456), orbit counts, all four depth bins, maximal entrance time and F^5=F^3. Source C++ and compressed Python verifiers were inspected, not treated as infinite proofs.

## originality

PASS

Established general symmetric-threshold period<=2 does not include this corona graph’s exact labelled orbit and basin counts or parity-asymptotic rarity; tree-dynamics fixed-point classifications do not cover K_n corona for arbitrary n. No stronger exact whiskered-clique census was identified by Resultary search or primary-source comparison. This is a best-of-knowledge priority conclusion with a named inaccessible 1980 original, not proof of global novelty.

## value

PASS

Natural fully-whiskered clique is the smallest rich corona family with a global majority-coupled core and private feedback leaves. Full labelled recurrence and first-entry classification explains a nontrivial oscillation-mass transition: polynomial 2/(πn) on even n versus exponentially suppressed sqrt(n/π)2^(-n/2) on odd n. A generic eventual-two-cycle theorem has neither the basin law nor sharp transient index.

The dated certificate retains the supplied scientific assessment, sources and limitations.
