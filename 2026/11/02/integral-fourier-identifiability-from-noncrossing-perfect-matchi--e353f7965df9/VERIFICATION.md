---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Every noncrossing perfect matching of 2n vertices in strictly convex cyclic order has only opposite-parity chords, yielding an n×n permutation incidence matrix X. For any four alternating-parity polygon vertices, pairing the intervening even-length boundary arcs gives two concrete noncrossing completions whose incidence difference is a signed 2×2 checkerboard. For fixed even rows i<k, allowable column pairs join I={i,…,k-1} to its nonempty complement; the complete bipartite column graph is connected, so telescoping generates every row-pair checkerboard integrally. In particular the standard (n-1)^2 basis of the zero-row/zero-column integer lattice is generated: no torsion index or modular rank loss. The covariance quadratic form is the variance of a linear functional and, for strictly positive weights, vanishes iff the functional is constant across the entire matching set. Its orthogonal complement is precisely arrays u_i+v_j, rank (n-1)^2; Walsh's factor -2 preserves this nullspace. Fixing one edge cuts the polygon into two independent Catalan regions; two disjoint noncrossing edges cut three and yield the displayed Catalan product formula. Independent full enumeration of noncrossing matchings for n=2,3,4,5,6 recovered Catalan counts 2,5,14,42,132 and corresponding exact anchored incidence rank 1,4,9,16,25, with exact single-edge Catalan occurrence counts.

## originality

PASS

The full Birkhoff/permutation-matrix polytope's affine dimension is known, and convex noncrossing matching Catalan counts and flip-graph connectivity are classical; those broader-object facts do not imply that the dramatically restricted Catalan family integrally saturates the zero-marginal lattice. Houle–Hurtado–Noy–Rivera-Campo's original available flip paper treats connectivity rather than the integer checkerboard span; Asinowski counts noncrossing perfect matchings; Paffenholz treats all permutation matrices. The closest 2002 Hernando–Hurtado–Noy *Graphs of Non-Crossing Perfect Matchings* article was accessible only as abstract/fragments; direct lawful OA PDF failed and authorized Oxford retrieval returned vpn_disconnected. Cannot assert entire historical paper noncovering. Resultary hits were matching-polytope and finite-field matching subjects, not this exact integral noncrossing incidence lattice; best-of-knowledge originality PASS with material reserved priority risk.

## value

PASS

Arithmetic saturation of incidence differences over Z is a structural tomography/identifiability result for a natural geometric Catalan ensemble, stronger than its real rank or known flip connectivity. It yields uniform rank over every coefficient field and exact first-order Fourier null relations for any fully supported distribution without an arbitrary sample cutoff. This is mathematically useful even without closed positive eigenvalues or a conditioning bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
