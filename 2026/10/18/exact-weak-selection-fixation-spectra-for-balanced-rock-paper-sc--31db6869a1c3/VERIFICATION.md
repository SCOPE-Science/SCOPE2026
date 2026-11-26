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

The complement is a simple 2-regular graph on six vertices, necessarily C6 or two triangles; taking complements gives the two listed connected cubic graphs. At neutrality each oriented edge has selection probability 1/18. The type-zero fraction is harmonic by cancellation of opposite orientations, and from every transient state one can propagate a present strategy along a spanning tree to absorption with positive probability. Finiteness gives a transient spectral radius less than one and uniqueness of the Dirichlet problem. Analytic inversion persists near zero selection; the payoff sum cancels over undirected edges by antisymmetry (a uniform fitness shift would also cancel in donor normalization). The change in neutral fixation on copying u to v is (1_{s_u=0}-1_{s_v=0})/6, explaining 1/108 in the differentiated equation, with zero derivatives at constant states. Independently ran `python3 /workspace/reproductions/cubic_fixation.py` against the entire supplied JSON as data, without executing the frozen checker. Clearing denominators by 1686 for the prism and 66 for K3,3, used both copy orientations per undirected edge and grouped the forcing as (pi_u-pi_v)(1_{s_u=0}-1_{s_v=0}); all 729 integer residuals and all three boundary values per graph passed, together with all sign swaps. The 90 balanced values per graph gave the stated seven-point and three-point spectra and all four explicit example derivatives. Exact uniqueness turns the complete residual check into proof for this finite system; it does not validate a larger-graph theorem or finite-selection approximation.

## originality

PASS

The supported result is the exact labeled distribution at zero selection on the two cubic six-vertex graphs for the specified three-type antisymmetric game. Closely related three-strategy regular-network work uses pair/diffusion approximation in global frequencies and studies a different RPS payoff example; known configuration-dependent results in the checked literature are two-type. The absorbing-chain method and the neutral harmonic function are standard. No matching earlier table or specialization supplying the two exact spectra was identified in the checked sources; the search is bounded.

## value

PASS

Six vertices is the smallest size at which a connected simple cubic graph supports both a balanced three-strategy mixture and a topology comparison at fixed degree. The exact configuration-resolved distributions give a calibration case for frequency-only or topology-averaged approximations: even on one graph and with fixed focal placement, the sign and size can depend on how the other types are arranged. The two spectra quantify the topology effect beyond a single counterexample, without purporting to quantify approximation error in the original large-network regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
