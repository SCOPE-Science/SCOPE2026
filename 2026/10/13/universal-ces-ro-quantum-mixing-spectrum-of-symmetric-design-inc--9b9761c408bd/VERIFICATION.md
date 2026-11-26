---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For the unweighted adjacency walk, write E=J/v, C=I−E, D=B−kE. The design equation gives DDᵀ=DᵀD=s²C with 0<s<k. The constant sector and its orthogonal complement give exactly the four projectors at ±k and ±s, including multiplicity v−1 at each of ±s. In the Cesàro average the unequal eigenvalue terms vanish. The Schur squares of the two constant-sector and the two complementary projectors yield X=(E∘E+C∘C)/2 and Y=(E∘E+(D∘D)/s²)/2. Since B is 0–1, X=cI+J/v² and Y=αB+βJ with the stated α,β. Both blocks sum to 1/2 per row, giving eigenvalues 1 and 0 on the two constant directions. On the complementary pair of spaces the off-diagonal singular value is |α|s, giving each of c±d exactly v−1 times. For 2≤k≤v−2, s≥1 and |v−2k|≤v−4 give c−d≥1/v; for k=v−1, s=1 and d=c, and writing B=J−P gives Y=XP and kernel (u,−Pᵀu). The trace, projective-plane specialization for q≥2, and smallest positive eigenvalues follow. Conversely a connected regular bipartite graph with four eigenvalues has two positive singular values, k simple and s on the orthogonal complement; the Gram matrix has constant off-diagonal entries and recovers the symmetric design conditions. Independent numerical grouping of the actual adjacency eigenspaces compared full spectra on six examples, including both signs of v−2k and the smallest crown case (OPENBLAS_NUM_THREADS=1 python3 /workspace/branches/independent_checks.py 5). This corroborates the all-parameter proof rather than replacing it.

## originality

PASS

The supported distinct content is the full family-specific average spectrum with sharp rank boundary and exact least positive mode, not the general projector-Schur-square machinery or the classical adjacency spectrum. The strongest inspected general results reduce the problem to computing squared projectors or a commutant projection, but give neither the design-specific cross-block coefficient nor the positivity and multiplicity classification. No covering theorem was verified in the bounded comparison.

## value

PASS

The exact average-mixing spectrum is a natural quantum-walk invariant, and the design class covers all connected four-eigenvalue regular bipartite graphs. It identifies the unavoidable sign kernel, isolates the crown nullity jump, and provides the exact smallest positive mode to quantify behavior on the nonsingular subspace. Parameter-only equality makes those quantities usable without choosing or diagonalizing an individual incidence matrix. This value is in the complete spectrum and boundary, rather than merely applying the known general time-average identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
