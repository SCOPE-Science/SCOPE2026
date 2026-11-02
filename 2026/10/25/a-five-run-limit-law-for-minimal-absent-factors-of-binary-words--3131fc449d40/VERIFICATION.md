---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For all a,b,c,d,e>=1 the bridge 01^k0 is a minimal absent contiguous factor exactly for 1<=k<=max(b,d), k not one of b,d; 10^k1 occurs exactly for 1<=k<=max(c,min(a,e)), k!=c. Their disjoint count is T+M-1-|{b,d}|. The prior proved RLE five-type bounds give at most 2 unary, 0 missing two-letter factors, 196 type-four, 10 type-five residual factors, hence 0<=R<=208. The fixed-dimensional positive-composition grid converges to Dirichlet(1,1,1,1,1); continuity and bounded error yield weak convergence and all fixed moment convergence. For selected j simplex coordinates, E[min]=1/(5j), so E[max(C,min(A,E))]=7/30 and E[max(B,D)]=3/10; piecewise-affine rational simplex lattice sums yield E[N_n]=(8/15)n+O(1). Independently enumerated all 1024 quintuplets with each run in 1..4, constructing factors afresh; exact bridge family and remainder checked, max observed remainder 7. Read actual verify.py (3125-case planned checker); its output is not substituted for proof. Domain five positive runs, n>=5, linear contiguous factors.

## originality

PASS

Best-of-knowledge original five-run positive-composition probability law and first moment; known Akagi RLE characterization is explicitly a premise, not claimed new. No inspected prior result states the Dirichlet functional or its 8/15 moment.

## value

PASS

The exact asymptotic distribution and rational mean answer a natural probabilistic question about minimal absent contiguous words under a fixed-run composition ensemble. Five runs give two distinct competing bridge orientations and the first genuinely joint max/min functional. The bounded-remainder lemma makes a complete nondegenerate law out of the combinatorial count; the known deterministic RLE bounds alone are not the requested random-ensemble statistic. No paper-size theorem or exact density required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
