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

The gradient g_i=f(i+1)−f(i) is exactly a zero-sum edge vector, and it evolves by the same nearest-neighbor cycle Markov generator Q. Any zero-sum g is a positive transport combination of dipoles e_i−e_j preserving weighted l1 cost, so it suffices to test all dipoles. The exact right derivative F_ij=−(2+a_ij)(w_i+w_j)+sum_{k!=i,j}w_k|a_ki−a_kj| is both necessary (positive F gives strict small-time increase) and sufficient (for h<1/3 Euler step exactly decreases weighted l1 on all dipoles; powers converge to e^{tQ}). Counting adjacent/distance-two/distance-three/four cases gives stated n<=5 inequalities and n=6 pair-sum S and distance-two condition. For n>=7, nonpositive distance-three dipole derivatives have total zero, forcing w_i+w_i+3=S; n=7 gives w_i=w_i+6 and hence equality; n>=8 distance-four analogue gives w_i+w_i+4=T, and cyclic constant consecutive difference forces all weights equal. I independently computed F from raw Qg, without using package gain formula, and exhaustively matched classification on exact integer profiles at n=3..9 with totals 64,256,243,729,2187,256,512, including stable hexagon. These finite profiles corroborate, but universal result rests on transport/Euler identities.

## originality

PASS

The graph TV/cut framework and MBO heat-threshold dynamics of van Gennip et al. are known; anisotropic continuum TV regularization and total cyclic variation of circle-valued signals are different mathematical operations. General Markov/semigroup l1 contraction does not imply weighted contraction on the constrained zero-sum gradient hyperplane for arbitrary independent positive edge weights. Targeted Resultary retrieval located weighted-cycle numerical index and quartic heat/energy invariants, not this exact 3..6 admissible cone / n=7 rigidity theorem. A classical logarithmic-norm classification may implicitly subsume it and remains a risk.

## value

PASS

Anisotropic edge TV monotonicity under a canonical graph smoother is a natural stability/design question. The complete finite-weight cone conditions for small cycles, an explicit nonconstant stable 6-cycle family, and sharp 7-edge rigidity offer a structural boundary and constructive small-time witnesses rather than routine contraction for uniform weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
