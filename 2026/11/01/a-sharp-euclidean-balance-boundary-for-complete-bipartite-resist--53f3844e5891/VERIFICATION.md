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

For K_(m,n) with m,n>=2 and unit conductance, the Laplacian spectral decomposition gives within-part resistances 2/n and 2/m and cross resistance (m+n-1)/(mn); these were recomputed independently via reduced rational Laplacian inversion on six small graphs. For every zero-total coefficient vector, the powered-distance quadratic form splits without lost directions into -b^p||u0||^2-c^p||v0||^2+s^2[(m-1)b^p/m+(n-1)c^p/n-2a^p]. Dividing by a^p yields a strictly convex weighted sum of exponentials, negative at p=0 and p=1 and tending to +infinity, hence exactly one positive crossing and strict p-negative type below it. Independent symbolic algebra verifies F(2)=2[(m-n)^2-1]/(m^2 n^2), proving R itself Euclidean precisely for |m-n|<=1. Centered Gram ranks N-1 below and N-2 at the endpoint follow from the two within-part sectors plus one contrast; fixed-defect and extreme-imbalance asymptotics follow by expansions of the same unique root and are consistent with independent test calculations. No extrapolation from the six small graphs is used as an all-size proof.

## originality

PASS

Sanchez arXiv:1108.0451 Theorem 3.1 gives maximal negative type of K_(m,n) with path metric (cross 1 and both within 2), not the effective-resistance metric (three size-dependent distances), so the shared graph and equality-vector shape do not imply equal threshold. Liu et al. arXiv:2512.14195 studies identifying graphs from resistance-distance multisets, not powered conditional definiteness; Yang 2012 and Gervacio 2012 establish resistance values and Kirchhoff-type invariants only. Resultary queries for effective resistance p-negative type and Euclidean balance returned no covering result. The equation, one-dimensional endpoint, and balance criterion survive best-of-knowledge comparison, with uninspected older resistance sources a residual risk.

## value

PASS

The exact supremal negative-type exponent for all complete bipartite effective-resistance metrics is a canonical spectral metric classification. The surprising exact |m-n|<=1 Euclidean boundary and endpoint embedding dimension drop answer natural Hilbertian embedding questions; this is not simply repetition of known edge resistances or Schoenberg’s general criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
