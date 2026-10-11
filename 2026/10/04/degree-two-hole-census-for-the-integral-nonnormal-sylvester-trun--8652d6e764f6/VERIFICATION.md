---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The degree-two reduction is exact: source-lattice points are precisely feasible sign vectors, and every degree-two target is uniquely \(2q\) with \(q\in\{-1,0,1\}^{15}\). The carry-free base-three encoding converts decomposability into exact pair-sum membership. An independent implementation, written from the definitions rather than executing the repository verifier, exhaustively found 9552 feasible sign vectors, 6,350,363 feasible ternary targets, and 6,215,123 decomposable targets, hence exactly 135,240 holes. A separately implemented breadth-first action of the stated eight generators of \(\operatorname{AGL}(4,2)\) partitioned the hole set into orbit sizes 840, 13,440, 26,880, 40,320, and 53,760, summing to the full count. The algebraic action identity permutes the sixteen Walsh facet inequalities, so the orbit computation acts on the correct set.

## originality

PASS

Lebedev's current primary paper treats exactly \(P_{5,1}\), proves it integral and nonnormal, and exhibits one degree-two hole, but its full text does not enumerate the degree-two hole set or its affine-character orbits; an exact text search finds no occurrence of 135240. Section 5 explicitly says remaining normality parameters are not classified. Resultary returns the assigned census as the exact hit and no competing same-object census. Thus the complete 135,240-hole/five-orbit classification is not implied by the source's existence witness or normality bands.

## value

PASS

Degree two is the first obstruction degree used to prove nonnormality for this canonical integral truncation. Replacing a single witness by the complete 135,240-element obstruction set and compressing it to five natural symmetry types is a motivated exact finite classification with clear semigroup/Hilbert-basis utility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
