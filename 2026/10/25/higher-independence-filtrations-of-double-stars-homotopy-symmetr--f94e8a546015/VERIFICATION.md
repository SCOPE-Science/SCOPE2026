---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The face decomposition by zero, one or two chosen centers is exact: full leaf simplex plus cones u*X_r,v*Y_r,uv*Z_r, with Z_r=sk_{r-3} Delta(L). Because A and B are both nonempty the three-term core is contractible, its quotient is the twofold suspension of the skeleton (r=2 gives a circle), and simplex-skeleton Morse matching gives binomial(N-1,r-2) spheres of dimension r-1. The relative chain complex on faces containing both centers identifies integral top cycles with wedge^{r-2}(ker[Z^L -> Z]) and introduces minus under center interchange. Field homology occurs in a different degree at every consecutive r, so all positive-degree bars die at r+1. Checked r=1 and r>=N+2 endpoints. Reimplemented induced-component face tests and reduced F2 ranks independently for all 54 cases a,b<=3, r<=a+b+2; all matched. Finite checks corroborate but do not prove the all-parameter theorem.

## originality

PASS

Best-of-knowledge originality applies to the complete double-star integral equivariant and persistence classification, not qualitative vertex-decomposability of trees or the 4-vertex path boundary case.

## value

PASS

Double stars form a minimal nontrivial two-center branch family; an exact entire higher-independence filtration, distribution-independent homotopy ranks, and integral automorphism modules distinguish structural information absent from qualitative shellability. These are natural invariant computations, useful as a benchmark for tree filtrations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
