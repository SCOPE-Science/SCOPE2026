---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Smooth plane quartics are canonical genus-three models, so their F2-rational automorphisms extend to PGL3(F2). At a rational projection center P, every projective fiber-fixing transformation is a shear I+P\otimes ell with ell(P)=0; precisely three nonidentity elations exist, giving possible group orders 1,2,4. The invariant-quartic expression shows a nontrivial fiberwise automorphism forces an inner center to be singular, hence all such centers are outer. Independent exhaustive binary homogeneous-quartic orbit enumeration covered all 32,767 nonzero masks, found 279 PGL3(F2) orbits, and exact geometric smoothness (three affine-chart Groebner unit-ideal tests) selected 78 smooth orbits comprising 10,920 forms. Checking all seven rational centers and their three elations independently reproduced class profiles (0,0):61, (1,0):14, (3,0):1, (2,1):1, (0,7):1 and weighted equation counts 9736/1134/28/21/1 respectively, hence 17 positive classes. A nontrivial full order-four deck group gives exactly the asserted Galois-point characterization.

## originality

PASS

Nart–Ritzenthaler already give the full characteristic-two genus-three nonhyperelliptic curve classification and automorphism normal forms, so the 78 curve classes and the characteristic-two Klein Galois example are NOT new. Fukasawa–Miura–Takahashi define quasi-Galois points and prove general quartic bounds, with the Klein exceptional curve known. The candidate novelty is specifically the simultaneous distribution of fiber-fixing groups of orders two and four at every F2-rational center across all 78 arithmetic classes and weighted equations, which requires an elation-incidence refinement not explicitly stated in materially read main tables. Best-of-knowledge PASS qualified by possible implicit extraction from older stabilizer tables.

## value

PASS

The seven rational points of PG(2,2) and partial deck groups are intrinsic arithmetic invariants of plane quartic projections. The completed joint distribution across every genus-three nonhyperelliptic F2 class distinguishes full Galois projections from merely quasi-Galois involutions, giving a natural complete arithmetic classification rather than a gratuitous table of coefficients. It is useful independently of the already known 78-class census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
