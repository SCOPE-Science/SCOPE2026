---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The stationary covariance is sigma²/(2a)*(I+tL)^(-1). For edges uv, the cofactor expansion on a tree gives q_uv=t B_uv/det K with B_uv=det K[V\{u,v}], while q_vv=A_v/det K, hence rho_uv²=t²B_uv²/(A_u A_v). Principal-minor forests enumerate exact positive polynomial coefficients by marking at most two vertices; positivity ensures squared comparison has same sign as Pearson comparison. Independently generated all nonisomorphic trees n=2..8 using NetworkX, computed exact SymPy determinants of K minors (independent from packaged forest-polynomial verifier), and counted 733 edge pairs across 47 representatives: 201 identically equal, 521 uniformly ordered, eleven with exactly one positive root, in six eight-vertex tree classes. SymPy exact factorizations/Sturm positive-root counts and direct rational check matched the six claimed crossing factor families. For E={01,12,05,23,24,56,57}, direct minor calculation yields a positive prefactor times (t²-4t-1) for rho_12²-rho_01², so t=2+sqrt(5) is unique positive rank reversal. Exhaustion is limited to n<=8 and derives its completeness from the independent graph isomorphism generator, not a sample of trees.

## originality

PASS

The resolvent kernel, matrix-forest identities and ecological synchrony phenomena are known. The exact threshold at eight habitats, complete six-of-23 topology classification, eleven pair counts and crossing polynomials concern a different nonlinear observable than published forest distance and were not found in the directly inspected original works. Best-of-knowledge novelty retains specialized covariance comparison risk.

## value

PASS

A sharp first topology/size threshold for rank reversals of adjacent stochastic population synchrony is a natural structural question. The classification identifies exactly which small unweighted dispersal networks exhibit nonmonotone *relative* local correlation under changing coupling, with a closed algebraic witness and exhaustive small-tree census. The exact threshold and six exceptional shapes are useful mathematical data beyond known kernel formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
