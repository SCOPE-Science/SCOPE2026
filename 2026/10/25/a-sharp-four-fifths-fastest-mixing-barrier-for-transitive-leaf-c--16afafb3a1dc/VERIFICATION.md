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

Automorphism averaging of symmetric stochastic P preserves feasibility and cannot increase the convex norm ||P-J||, hence global minimizers can be sought in invariant core-edge a and pendant b. Nontrivial adjacency eigenvalues produce exact 2x2 block eigenvalues 1-t-b ± sqrt(t²+b²), t=a(d-lambda)/2. Noncompleteness guarantees lambda_2>=0 via nonedge Rayleigh 0 and negative lambda_min. The virtual zero-eigenvalue block is an actual block or convex combination of two actual nontrivial blocks. PSD of (4/5)I-B_0 forces determinant <= -(b-2/5)^2 and da+b=1, thus b=2/5, a=3/(5d). If lambda_2>0 that candidate violates .8; if lambda_2=0 all nontrivial adjacency eigenvalues <=0 and candidate attains .8. Negative-semidefinite-on-1-perp implies nonadjacent vertices have identical adjacency rows, hence balanced complete multipartite H. Independently checked 2x2 eigenblocks on C4,C6,C7,C8,Q3 and K2,2,2, and verified equality/non-equality. A statement of uniqueness only in the invariant class, not globally, is respected.

## originality

PASS

Best-of-knowledge PASS only for the universal barrier over ALL noncomplete connected vertex-/edge-transitive cores and its iff balanced multipartite equality class. Prior star–mesh consensus work ALREADY SOLVES complete-multipartite equality-family optimizers, and general fastest-mixing symmetry averaging is known; these are explicitly credited, not claimed new. The strict >4/5 for every other eligible core follows from new spectral-interpolation argument.

## value

PASS

A sharp global mixing lower bound with graph-theoretic equality characterization answers a meaningful natural extremal question across transitive graphs; unlike numerical optimization on one graph, it pinpoints a structural spectral obstruction and explains the gap to standard Metropolis/maximum-degree prescriptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
