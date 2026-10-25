---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Given Graham–Ramsey 1981 Prop. 3.2 with exact support operations, all cases are exhaustive. Autocorrelation/flat modulus equivalence follows from Fourier inversion and four unimodular masses. For E={0,x,y,x+y} with 2x=0 and |E|=4, signs (1,1,1,-1) yield Fourier 1+χ(x)+χ(y)−χ(x)χ(y)=2 when χ(x)=1 and 2χ(y) when χ(x)=−1; hence |transform|≡2, for finite or infinite G. On Z7 E={0,1,2,4}, (1,−1,−1,−1) has C(0)=4 and zero C(d) for each d≠0 (two cancelling terms per nonzero difference). On Z5 E={0,1,2,3}, each nonzero difference has three ordered realizations, so an odd sum of signs cannot be zero. For exceptional Z4×Z2 F={00,10,31,01}, the involution difference h=(0,1) has exactly the two opposite ordered pairs between 00 and 01, giving 2 ε00 ε01≠0. The listed classification operations—automorphism, subgroup passage, translation—preserve existence/nonexistence of a sign convolution identity. An independently written integer-autocorrelation check enumerated all 16 signs for both negative prototypes; found zero solutions. Z7 positive example has exactly 2 sign solutions in those 16 patterns; symbolically proved rectangle witness was also corroborated for over 100 cyclic cases. These finite checks are supplementary, not the infinite-group proof. No claim about all complex equality cases or supports size ≠4.

## originality

PASS

Best-of-knowledge PASS after a fresh statement-and-implication comparison. Graham–Ramsey (1981) classify the four-element extreme supports but do not characterize the restricted real sign alphabet. Graham (2019) already provides the Z7 sign witness and a Z5 nonreal example; the full four-family binary iff is not stated there. The published Z5 equality classification implies its one negative subcase but not the rectangle/exceptional branches. Group-invariant and circulant weight-four weighing-matrix theorems supply an equivalent group-ring formulation and strong structural restrictions, but the inspected theorems do not individually imply the complete fixed-support iff. This is not a claim of priority over unindexed matrix/sequence literature; specific access and alias risks remain.

## value

PASS

It answers a natural support-sensitive realizability question: among the COMPLETE smallest nontrivial known four-point Sidon-extreme geometries, exactly which admit the least complex coefficient alphabet {±1}? The result is a structural positive/negative dichotomy for signed flat spectra, useful in harmonic-analysis extremizers and sparse group-invariant weighing matrices. It separates finite geometry from coefficient alphabet, provides a universal positive order-two rectangle construction and an elementary obstruction on the exceptional torsion support. It is not merely the already known Z7 example, nor a table over a single arbitrary group. Proof is short because the previously published classification supplies the natural exhaustive boundary. Limits: four elements only, no exact description of all complex phases or larger supports.

The dated certificate retains the supplied scientific assessment, sources and limitations.
