---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For R=1 the convex pentagon conv{0,P,V0,V1,Q} has all vertices within 3/4 of C=(3/8,sqrt(3)/8); three 120-degree rotations tile the filled hexagon, giving the upper bound. In any r≤3/4 cover a disk diameter is ≤3/2<sqrt(3), hence each disk can contain at most two hexagon vertices and only an adjacent pair; six vertices force a perfect matching of C6, hence exactly two alternating patterns. For any matched-pair disk define its boundary-edge contact fractions a,b∈[0,1]. Both farthest contacts lie in that disk, so D(a,b)=(b+(1−a)/2)^2+3(1+a)^2/4≤4r²≤9/4. If a+b≥1, write b=1−a+t, t≥0. Then D−9/4=3(a−1/2)^2+3(1−a)t+t²≥0, with equality only a=b=1/2. Thus each disk has a+b≤1 with equality only at radius 3/4. Every unmatched edge is inaccessible to the remote disk because its occupied pair is vertically sqrt(3) away, greater than 2r; covering its edge requires endpoint-contact fractions sum≥1. Summing gives ≥3 versus the disk-wise ≤3, so all contacts must be equalities and each center is the unique midpoint of a diameter pair; the two matchings yield exactly the claimed unordered triples. This proves global sharpness, all equality cases and scaling for every R>0, without restricting centers to H.

## originality

PASS

The precise original contribution is the universal lower bound rho_3(H_R)>=3R/4 and the exhaustive two-triple equality classification, NOT the previously known three-pentagon radius-3R/4 construction. Liu 2022 directly studies regular hexagon p=3 but its computational lower/upper bounds did not close in the reported run; Bezdek–Henderschedt 2024 supplies the construction for a Borsuk universal-cover argument but its N_n(r) finite-point assertion cannot imply this fixed-region lower bound or uniqueness; Birgin–Gardenghi–Laurain addresses asymptotic m and numerical regular hexagons from m=10. Stoyan–Patsuk 2010 is a directly relevant inaccessible historical source and is explicitly retained as priority risk. Two new Resultary searches found no implication-equivalent theorem, but failed indexing is not proof of novelty. Best-of-knowledge PASS, not absolute priority certification.

## value

PASS

The continuous 3-center Euclidean covering radius of a regular hexagon is a canonical geometric and location-theoretic optimization invariant, used as a nontrivial numerical benchmark in Liu 2022. A known exact construction only gave the upper bound; a sharp universal lower bound plus a complete two-configuration rigidity classification closes a natural finite exact-geometry question, and the novel vertex-perfect-matching/unmatched-edge-contact mechanism supplies a reusable mathematical certificate. This is a self-contained motivated exact fact rather than a routine normalization, known table reprint or negligible numerical improvement. Its merit does not depend on a general theorem for every polygon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
