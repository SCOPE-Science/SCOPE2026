---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Görtz–Yu Proposition 2.5 recalls the elementary-sequence containment equivalence φ_h=0 with h=g−floor(g/2). Muller's (1) and (5) match the permutation and dimension; Definitions 1.3–1.5 and Theorem 1.7 confirm the arrow direction, good-to-bad reachability requirement and odd-characteristic nonemptiness test. The first h indices have weights at least k+1; the only exceptions to containment at weights k+1 and k+2 are e_h, then e_(h−1) and e_h+e_g. For e_j, j≤h, the alternating orbit runs 1,g,2,g−1,…,j (singleton when j=1); π(j)=1 and the unique one leaves 2j−2 zeros. This is bad and no other cycle has a source one. Turning on g in e_h changes no permutation value, since both rules send g to 2. Now h→1→g is one intervening zero and the returning arc has 2h−4 zeros, so the cycle is good and all other cycles have no ones. This gives contact but not containment (φ_h=1). For g=3 the singletons and (1,3,2) give the same disjoint and mixed decisions without degeneracy. The finite checker is corroborative, not used as the general proof.

## originality

PASS

Existing containment, intersection criteria and small-genus results are credited. The distinct claim is the uniform extremal classification, with the two first-contact dimensions and exact exception types obtained by an exhaustive weight argument and symbolic analysis of the changing cycle.

## value

PASS

The first dimensions at which contact and containment diverge give exact, uniform geometric cutoffs beyond the known containment boundary. The unique first mixed stratum in particular supplies a systematic minimal test case without scanning all EO types of each genus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
