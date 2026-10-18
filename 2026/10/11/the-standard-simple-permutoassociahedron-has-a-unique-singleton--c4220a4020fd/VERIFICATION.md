---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

From the actual RESULT.md and arXiv:1708.02482 H-description, write N=n+1, mu=3^N/N, W=sum normal coefficients, Q=sum squares and P=Q-W²/N; intrinsic distance is (mu W-kappa)/sqrt(P). Singleton has kappa=3, P=n/N and distance (3^N-3N)/sqrt(Nn). For t>=2, H=sqrt(NP/n)<=sqrt(Q)<=W-t+sqrt(t), hence W-H>=t-sqrt(t). Compare kappa<3^(t+1)/2+1 with mu>=3^(t+1)/(t+1); t>=6 wins strictly, other cases reduce to five (N,t) rational inequalities. Independent exact rational reconstruction for n=2..12 checks strict separation and minima 45,1191/2,1683/2,53901/5,118818 at (3,2),(4,2),(4,3),(5,4),(6,5). The symbolic growth inequality, not finite sampling, covers all n>=2. Singleton halfspaces xi>=3 and sum xi=3^N give global radius upper bound and force equality center uniform, proving uniqueness.

## originality

PASS

Best-of-knowledge no prior determination of the Euclidean inball for this precise exponentially scaled H-realization; face-lattice equivalence or other graph-associahedron inballs do not imply metric data. The original source supplies the defining inequalities but no metric optimization theorem.

## value

PASS

The Euclidean inball is an intrinsic metric invariant of the explicitly normalized simple permutoassociahedron, a natural polytope in associativity/coherence geometry; identifying exactly its n+1 active facets among many nontrivial ones answers a motivated all-dimensions geometric question. Its strict inequality is not an automatic consequence of simplex containment and matters to metric comparison of realizations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
