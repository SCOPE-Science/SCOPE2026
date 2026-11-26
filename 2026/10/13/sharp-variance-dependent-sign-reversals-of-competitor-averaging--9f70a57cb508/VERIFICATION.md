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

Reconstructed the absorbing-chain derivation for independent fitness-weighted parent and uniform replacement, as in RESULT.md lines 23–56. On a two-allele edge the target's down/up ratio is z/a; the two harmonic equations give K1=a²/(a²+az+z²) and K2=a(a+z)/(a²+az+z²). At (1,1,1) the total holding probability is 1/3, so an ordered distinct-allele replacement conditional on a change has probability equal to the parent's fitness divided by 2(a+b+c). Two events extinguish A and the other four land on the edges. Their sum gives the stated P_A. For D=a²+am+m² and x=d², the exact P_A simplifies to a²(D−x)/[(D+x)²−(a+2m)²x]. Subtracting a²/D leaves numerator a²x[(a+2m)²−3D−x]=a²x[(m−a)(m+2a)−x] over a positive denominator. Since 0≤x<m², the nonzero boundary is feasible exactly when m/2<a<m; this also checks a=m/2, a=m, and d=0. Independently enumerated ordered individual replacements and solved the two-state edge systems with exact fractions: at a=2,m=3 the two examples give P_A=3/14 and 3904/18907, with differences +1/266 and −1452/359233. No uploaded code was run. The exact identities apply to this N=3 model only.

## originality

PASS

The standard two-allele formulas and the ability to compute the three-allele fixation probability via the general exact Moran system are prior methods. The supported distinct claim is the complete signed aggregation error for the arithmetic-mean competitor, including its admissible crossover and both signs at fixed mean. The closest averaging result uses Wright–Fisher diffusion; the closest constant-fitness Moran approximation is first order and cannot detect the effect.

## value

PASS

Three individuals is the smallest population where competitor aggregation changes which alleles can coexist. The sharp variance threshold isolates a meaningful failure of an averaging heuristic at fixed target fitness and background mean, and the exact model-matched witnesses refute either sign as universal. The value is this comparison, not a routine solution of the seven-state chain or an extrapolation to other population sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
