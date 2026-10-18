---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Checked original full Castillo–Liu arXiv:1710.01899 equations (4.1)–(4.3), Definition4.4 and Proposition4.6 for two-permutation vertices v_{pi,tau}=Σ_i[Mi+N(tau_{i-1}−tau_i)]e_{pi^{-1}(i)} for appropriate M,N. The N-summand telescopes and center is c=M(d+2)1/2; coordinates decompose a_i=i−(d+2)/2 and b_i=tau_{i-1}−tau_i. Sum a_i²=d(d+1)(d+2)/12 and sum a_i b_i=d(d+1)/2, leaving endpoint-zero path roughness E(tau)=Σ(tau_{i-1}−tau_i)². Uniform permutation sampling gives E[E]=(d+1)²(d+2)/6 and E-variance=(d−2)(d+1)²(d+2)(5d+11)/180 from identical, adjacent-overlap, disjoint path-edge products; independently exact-enumerated all permutations d=2..7, matching these formulas, including 0 iff d=2. Covariance by Sn permutation invariance has equal diagonal/off-diagonal, vanishes on 1, and trace=mean R², yielding (meanR²/d)(I−J/(d+1)). All dimensions d>=2 and only appropriate positive M,N, not full arbitrary nested deformations.

## originality

PASS

Read the 2017 Castillo–Liu primary 2022 published full paper at original vertex formulas (4.1)–(4.3) and Proposition4.6. Paper develops nested fans, deformations and combinatorics, does not state Euclidean radii, covariance or radial variance. Resultary nearest analogous geometry is bipermutahedron radial spectrum (different polytope) and partial permutohedron ellipsoid formulas (different objects/invariants). No exact nested-permutohedron radial second-moment stronger theorem found. Residual possibility known adjacent-permutation energy moment under different combinatorial name.

## value

PASS

Natural metric invariant of new symmetric nested permutohedra, with exact vertexwise radial fluctuations, tight-frame covariance and sharp d=2-only cosphericity transition for every admissible M,N. The variance is not a group-theoretic tautology: full value derives from permutation edge-overlap combinatorics. Does not claim extreme radii or John ellipsoid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
