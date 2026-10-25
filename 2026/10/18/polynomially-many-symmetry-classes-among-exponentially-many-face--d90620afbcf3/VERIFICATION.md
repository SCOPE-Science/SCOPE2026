---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Higashitani–Jochemko–Michałek tight-edge criterion reduces facets to integer 1-Lipschitz potentials with connected spanning nonzero-edge graph. Short arm enforces pole difference Δ=0,±1,±2; on long arms admissible words number 6 (Δ0) or 3 (other Δ) and short-arm patterns 2,1,2. S_m permutes long arms, pole swapping and global sign yield explicit letter involutions. Burnside counts six-color multisets with two fixed letters+two swaps (fixed H_m), three-color multisets with outer-color swap (fixed floor(m/2)+1), and short-branch Δ±1 classes with no further multiset identification. Multinomial orbit sizes sum to known total. Independently built color-multiset orbit representatives (not checker source) for m=2,3,4 and found class counts (13,4,6),(32,6,10),(70,9,15): 23,48,94, matching formula. Analytical count proves all m; finite verification is not general proof.

## originality

PASS

Braun–Bruegge 2023 Section4 Proposition 4.6 of 29-page primary paper gives *aggregate facets* for mixed-parity path bundles, including total 2·6^m+6·3^m. Higashitani et al 2018 facet potential criterion and Chen–Davis–Korchevskaia facet graph constructions are prior. These do not determine graph-automorphism-plus-sign orbit classes, explicit multiplicities, or polynomial asymptotic, absent a separately established orbit theorem. A Resultary semantic query returned no same object among inspected top hits. Unindexed orbit census remains possible.

## value

PASS

Exact symmetry-classification of a canonical family of finite-dimensional graph transportation polytopes separates exponentially many facets into O(m^5) types and gives orbit multiplicity; that is a natural and reusable equivariant classification, not just recomputing known total facet counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
