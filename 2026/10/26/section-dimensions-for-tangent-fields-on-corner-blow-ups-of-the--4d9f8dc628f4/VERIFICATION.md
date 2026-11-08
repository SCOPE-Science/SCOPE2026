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

Verified all seven Git blob identities plus one nested artifact tree from frozen commit, and reconstructed Git tree SHA e68b1b9cffa06834861ca607171cdd128f47fe6e. For Y=P1xP1, global vector fields are independent degree <=2 polynomial vector fields with six coefficients. A field lifts through a blown-up point iff it vanishes at that point. In chart v=ut, the restriction to E of the tangential lift is d+(b-a)t-c*t^2 for linearization [[a,c],[d,b]], so vanishing along E forces c=d=0 and a=b over every field (also checked second chart u=vz with c+(a-b)z-d*z^2). At selected x=0, infinity, vanishing kills a0, a2 respectively (analogous b0,b2); equality of local signed linear coefficients gives eps_x a1=eps_y b1. Independent exact arithmetic computed each of 16 subsets using six-column matrices, with ranks over Q,F2,F3,F5. Dimensions by orbits: empty 6; one 3; opposite pair 1; adjacent pair 1 (char !=2), 2 (char2); triple 0/1; all four 0/1. Ranks follow in any characteristic because all relevant pivot minors lie in {0,1,2}, so field tests are corroborative and the symbolic rank analysis is the unrestricted proof. No arbitrary centers, infinitely near centers, or higher cohomology are claimed.

## originality

PASS

Best-of-knowledge originality concerns the all-16-subsets dimension classification and its adjacent/opposite configuration distinction, NOT the four-corner case or the scalar-differential blow-up technique. Fujino--Sato Remark 6.2 already proves the four-corner characteristic jump and displays a local chart; its statement and proof do not give the new intermediate subset table. General toric automorphism-group formulas and Demazure-root methods are a material possible implicit-coverage risk. Actual Resultary searches found only different surface invariants; searches do not certify novelty.

## value

PASS

Natural complete classification of the 16 torus-fixed corner subsets and the marked exceptional-divisor tangent vanishing invariant. It identifies the first and intermediate configurations with a nonzero characteristic-two jump (adjacent two and all triples), and contrasts opposite two-center sets, which have no jump. That configuration sensitivity is not determined by the previously published four-center value alone. The computation is short and specialized, not a general toric classification, but the precise boundary map of characteristic dependence in a canonical blow-up family has independent geometric use as a small explicit test case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
