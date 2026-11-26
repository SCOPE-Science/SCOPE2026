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

In each clique only the uniform vector and its normalized endpoint contrast enter; other contrasts have zero endpoint amplitude and are invariant. In the contrast/uniform basis this gives exactly K, B, D as displayed. With m=min(p,q), the two low energies of K have a gap bounded below in terms of fixed w>0, lie order m below D, and ||B||=O_w(m^-1/2). Weyl first isolates each low eigenvalue; eliminating the high component bounds its norm by O_w(m^-3/2) and gives a Schur correction O_w(m^-2), so the low eigenvalues and their low-sector normalized components differ from those of K by O_w(m^-2). Orthogonality gives low-sector weight O_w(m^-3/2) in each high eigenvector at the level of norm. This proves the low-low and mixed propagator bounds with no need for any separation between the two high eigenvalues. In the high-high block the first-order Duhamel correction vanishes and the double integral is bounded by t^2||B||^2/2; the cross-entry of exp(-itD) itself is at most |t|w/sqrt(pq). Endpoint overlap factors give O_{w,T}(m^-2) for both mixed and high-high amplitude contributions. Evaluating exp(-itK) gives the stated sign and phase; at pi/(2w) the sine differs from one by O_w(m^-2), giving the claimed probability. For fixed unequal p,q the conserved H^2 expectations p-1+w^2 and q-1+w^2 differ, precluding endpoint PGST. This proof is uniform for arbitrary ratios, not for variable w or growing time. Independent replay: python3 /workspace/review_replay.py 2 (NumPy/SciPy, 300 independently constructed reduced-matrix expm diagnostics, including q=p^2 and negative times). These diagnostics are finite, not a substitute for the bounds. Uploaded verifier inspected only.

## originality

PASS

Best of inspected evidence supports the uniform compact-time endpoint amplitude with second-order remainder for the fixed-weight unequal-clique adjacency family, and its explicit leading fixed-time infidelity. The four-dimensional symmetry reduction and the unequal-endpoint moment obstruction are standard ingredients, not new general mechanisms. The frozen prior-work paragraph miscites the one-bridge theorem number and misidentifies the graph in the cited corona theorem; neither assertion is needed for the Finding. Cite Coutinho et al. Theorem 11 for a single unweighted bridge; do not use Ackelsberg et al. Theorem 5.3 as evidence of equal-clique-barbell PGST.

## value

PASS

The phase-resolved estimate quantitatively distinguishes coherent single-edge transfer from time-optimized transfer on a fixed graph. It explains both the constant-time approach to unit probability and its leading size deficit, uniformly even for arbitrarily unbalanced cliques. A mere effective two-state heuristic would not give the second-order error or justify this leading loss; the conserved-moment contrast clarifies the noncommuting size and time questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
