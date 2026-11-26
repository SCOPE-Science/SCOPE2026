---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the zero-one adjacency of the once-subdivided K_n, the singular values of the unsigned incidence matrix B follow from BBᵀ=(n−2)I+J. The two nonzero singular-value modes split into opposite adjacency eigenvalues; the remaining projector is supported on the edge kernel of B and has rank n(n−3)/2, zero at n=3. Cesàro averaging pairs only equal adjacency eigenvalues, so the squared projectors are added, without mixing the opposite signs. In the edge block, writing x for intersection size, the standard edge projector has entry (x−4/n)/(n−2), and the kernel projector has entry δ−1/m−(x−4/n)/(n−2). Squaring gives the three edge orbit coefficients in the record. In the cross block, (B_ie−2/n)²=(1−4/n)B_ie+4/n² gives the stated coefficient h_n; on mean-zero modes the cross entry is h_n√(n−2). The constant block has original-vertex row sum 1/2 within that part, and the Schur sum is stochastic, giving its two stated eigenvalues. The triangular graph acts by n−4 on Bᵀ of the mean-zero space and by −2 on ker B. Substitution gives the stated b_n and η_n, and a_n b_n−(n−2)h_n²=(n−4)(n−3)/(2n(n−2)). Together the sectors exhaust n+m. The n=3 constant and standard sectors give rank 3; the n=4 standard block has only one nonzero eigenvalue per pair, giving rank 7 overall. All sectors are positive at n≥5. A separate exact characteristic-polynomial check at n=3,4,5 matched and gave ranks 3,7,15.

## originality

PASS

The strongest same-observable catalogue matches concern graph blow-ups and primitive strongly regular graphs, neither containing this family. The primary exact-object source puts the subdivision walk in its future-work discussion and evaluates a distinct total graph for K_n. General projector identities and algorithms do not provide the evaluated uniform eigenvalues or the rank cutoffs without the additional incidence and Schur-orbit spectral calculation. No covering statement was established in the sources checked.

## value

PASS

An established graph construction models the natural walk that alternates between vertices and incident edges, explicitly distinguished from the total-graph walk in prior work. The exact spectrum of its long-time mixing operator is informative beyond the ordinary adjacency spectrum, and the 3,7,full rank transition distinguishes the exceptional sizes from all larger complete graphs. The invariant is motivated and the closed decomposition is usable without calculating graph-sized matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
