---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS. For all integers n>=2, the definition minimizes directed total domination over all orientations with positive indegree at each vertex. S is feasible exactly when it closed-dominates the original graph and every connected component of G[S] has an undirected cycle: each selected vertex needs a selected predecessor; conversely orient one cycle in every component, its attached forest outward and remaining S-to-complement edges outward. The upper witness consists of every middle-row vertex plus top-row vertices in columns 1,2, forming an induced square and dominating all vertices, size n+2. For lower bound write r occupied-column runs, e empty columns and b empty boundary columns. Cyclicity forces at least two columns with >=2 selected vertices per run, with extra surplus at boundary-occupied runs; hence surplus >=2r+b. Domination of empty columns gives e<=2(r-1)+b. Therefore |S|=(n-e)+surplus>=n+2; n=1 has no valid orientation and is explicitly excluded.

## originality

PASS

PASS (best-of-knowledge, with specified residual risks). Equivalent formulation is minimum cardinality of a closed-dominating vertex set with a cycle in every induced component. In the present P3xPn geometry, cycle surplus accounting yields n+2. This criterion appears as known structural observation in primary orientable domination literature. The primary general grid bounds are strictly weaker in the three-row case. Stronger currently uninspected recent versions or independently known special-case propositions could subsume this exact n+2 formula, so historical risk persists. The new n+2 formula attains the existing upper bound and sharpens its weaker lower bound. Neither known cyclic-component feasibility nor the general graph bound by itself implies n+2 without the three-row run surplus argument.

## value

PASS

PASS. This solves the exact three-row specialization of a natural orientable total domination grid problem: earlier general bounds n<=dom_t<=n+2 leave a real gap. The all-width equality follows from a nontrivial column-run/cycle argument and the exact boundary accounting, not a brute-force table or arbitrary instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
