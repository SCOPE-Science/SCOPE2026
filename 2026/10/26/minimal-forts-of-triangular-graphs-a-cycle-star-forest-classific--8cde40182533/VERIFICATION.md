---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For each uv outside selected edges F of K_n, exactly d_F(u)+d_F(v) adjacent vertices lie in F in T_n. Hence the fort condition is equivalent to the absence of simultaneous isolated and degree-one vertices in H=([n],F). If H has an isolate, the no-leaf condition forces a cycle, whose edge set is itself a nonspanning fort; inclusion-minimality forces exactly that one simple cycle. If H has no isolates, F is a spanning edge cover, and minimality implies each edge meets a degree-one vertex, equivalent to each component being a star. Conversely every such cycle and star forest is a minimal fort, checking all nonempty proper subsets. A size-m star contributes m z^(m-1) u^m/m! for m>=3 and zu^2/2 for m=2, giving the proposed EGF; nonspanning unoriented k-cycles contribute binom(n,k)(k-1)!/2. Boundary n=3 has three size-two stars, n=4 has three K2 unions plus four stars and four triangles, and n>=5 starts at size three. The gap-free spectrum, maximum n-1 and n+n!/(2(n-1)) largest-count formula follow. Independent direct adjacency/fort enumeration of all 8,64,1024,32768 subsets for n=3..6 agrees with 3,11,60,308 minimal forts, and independent labeled component recurrence agrees through n=15; these finite checks do not establish the infinite result, which follows from the structural proof.

## originality

PASS

The all-parameter two-family minimal-fort classification and weighted polynomial were not implied by the material read in foundational fort-count/hypergraph papers or the published Johnson-family minimum. The minimum size and generic transversal interpretation are prior art. Search coverage is best-of-knowledge; the 2024 Johnson paper is an accessible-abstract-only priority risk, not a certified absence of overlap.

## value

PASS

A complete minimal-obstruction hypergraph of the natural Johnson/triangular graph family, rather than an arbitrary cutoff or recomputed minimum, is a mathematically useful exact invariant. The line-graph incidence translation exposes genuinely different nonspanning cycle and spanning edge-cover obstruction mechanisms, and the weighted enumerator gives every fort size relevant to zero-forcing transversal/cover formulations. Its all-n result and distribution are not mechanically implied by the published minimum-fort-size statistic alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
