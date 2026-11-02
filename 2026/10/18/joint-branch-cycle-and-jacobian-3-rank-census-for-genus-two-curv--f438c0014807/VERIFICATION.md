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

For exactly F3, every smooth projective geometrically connected genus-two curve has a smooth hyperelliptic model y²=F(X,Z) with F squarefree homogeneous degree six. With F3* squares={1}, arithmetic isomorphisms are exactly GL2(F3) binary-sextic substitutions; quotient by scalars ±I has order 24. Independently enumerated all 3^7 coefficient vectors, tested degree 5/6 and squarefree gcd to obtain 1,296 forms, formed 24 actions by binomial-coefficient expansion (not the package polynomial-power routine), partitioned into 69 disjoint complete orbits, and obtained Burnside fixed count 1,656=24·69. Factorization over F3, rank(A²) for A=[[c2,c1],[c5,c4]], and direct F3/F9 point counts yield exactly 19 nonempty (branch partition,3-rank) cells, 46 nonempty point-count triples, and the nineteen class/equation frequencies in RESULT.md. An independent F9 zeta-numerator computation verified rank(A²) for each of the 1,296 forms (rank-0:144, rank-1:288, rank-2:864 equation counts) and checks all 69 orbit representatives. The supplied full_joint.csv exactly agrees with census.json at all 46 rows. The six rank-zero arithmetic classes occur in (1,1,4),(1,2,3),(6), two each; unique orbit with four rational branch points is ordinary, has four F3-points, and six sextic forms. Stable Hasse-Witt rank, not naive rank(A), is used. The exhaustive finite proof covers all models because q and coefficient space are fixed; no inference to other field sizes is made.

## originality

PASS

Best-of-knowledge originality is restricted to the complete arithmetic joint distribution of Frobenius cycle partition of six Weierstrass points, Jacobian 3-rank and F_3-point count: 19 nonempty (partition,rank) cells and 46 triples across 69 F_3-isomorphism classes. The previously published total of 69, standard Cartier/Hasse-Witt formula, coarse geometric p-rank counts, supersingular Weil-polynomial possibilities and extremal point spectra are expressly excluded from novelty. Readable primary texts and two direct Resultary searches did not show an implication giving the full table. Cardona 2003 is strongly relevant but its complete text could not be examined due to an access barrier: a prior equivalent table remains a genuine priority risk, not a finding of no coverage.

## value

PASS

The precisely motivated finite problem classifies simultaneously the Frobenius conjugacy class on the six Weierstrass points (2-torsion/branch geometry) and the Jacobian 3-rank (3-primary arithmetic) for all arithmetic genus-two classes over the smallest odd prime field. Neither 69 total classes nor 3,6,18 geometric rank marginals fixes the exact 19 intersection counts or the 46 class/point refinements; the supersingular placement and unique four-rational-branch-point ordinary class are specific nontrivial outputs. This complete small-field stratification and reproducible class representatives can support algorithm testing in genus-two arithmetic and finite-field moduli. Value is the natural exact joint invariant and exhaustive classification, not the raw 69 count, code presence alone, routine polynomial factorization or a claim of all-q generality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
