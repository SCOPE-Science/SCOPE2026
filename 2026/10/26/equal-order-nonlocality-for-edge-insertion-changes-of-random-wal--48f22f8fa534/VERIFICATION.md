---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Both graph constructions have 4+r+K vertices where K=max(100,4r+10): a remote path of length q=r+K versus a length-(r+1) stem entering a terminal K-clique. The radius-r marked balls have the same degree labels, and u-c-v are bridge links giving R_uv=2. Reconstructing the published cut-vertex Poisson-excursion transfer with artificial remote completion time T, its Laplace transforms a=E exp(-T), b=E exp(-3T/2) and unused suffix J yields delta=2ET-2(2m-1)(a-2b/3)-2E[J(exp(-T)-exp(-3T/2))]. For the long path, ET=q and J=q^2 reduce to the strictly positive rational function 2(6q^3+5q^2-23q-10)/(3(q+1)(3q+2)). For the terminal clique, a single excursion covers the clique with conditional probability >1/2 when K>=100; thinning gives ET<=2(r+1) and a>=1/(2r+3). The negative bound follows from K(K-1)>12r^2+28r+11, verified symbolically from K>=4r+10. Independent exact visited-subset Bellman calculations reproduce strict signs on (r,K)=(1,3),(1,4),(2,4); these are finite corroborations only.

## originality

PASS

Si (arXiv:2608.27474), the directly preceding paper, already proves different-order arbitrary-radius nonlocality and the required cut-vertex transfer identity. Its dated abstract explicitly calls equal-order nonlocality open. The new witness makes vertex counts identical with a remote terminal clique behind the radius cutoff, retaining marked degree labels and effective resistance. Resultary returned no matching same-order theorem. The full Si text was not retrievable by the attempted accessible arXiv routes, so priority and exact transfer assumptions remain a stated comparison limitation; abstract alone is not misrepresented as full-text noncoverage.

## value

PASS

Graph order is a natural global datum one might add to local geometric/electrical statistics to predict whether inserting an edge accelerates cover. The same-order construction rules out that strengthened local criterion at every radius, directly answering a stated gap rather than merely changing a numerical example. Exact signs and matching invariants provide a reusable counterexample family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
