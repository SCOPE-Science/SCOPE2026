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

The non-backtracking arc chain decomposes into 2m oriented deterministic hub-to-hub tours; at the hub its tour transition is (J−R)/(2m−1). A transfer determinant and symmetric/antisymmetric splitting give the full characteristic polynomial ∏(z^ℓ_i−t)(z^ℓ_i+t)(1−2tΣ1/(z^ℓ_i+t)); differentiation at z=1 yields K_nb, as eigenvalue 1 is simple even if the chain is periodic. The ordinary arc chain shares nonzero spectrum with the vertex chain; resistance on a one-vertex join gives K_e=M+m−1+(S2−m)/3−(S3−M)/(6M). Their difference Δ increases strictly with each ℓ_i: for one variable x≥3, the derivative of A=S2/3−S3/(6M) is ≥3/2 and ∂(S2/M)>−1, proving ∂Δ>0; equal-cycle basepoint and four two-cycle boundary cases give the classification. Independently formed exact directed-edge transition matrices for (3,3),(3,4),(3,5),(4,4),(3,3,3) and verified both fundamental-matrix trace formulae by rational inversion. Additional full parameter grid sign checks 2–4 petals, lengths 3–7 passed.

## originality

PASS

Breen et al. first studied edge-space non-backtracking Kemeny constants and cycle-barbell families. Their two distinct degree-three junctions are not the single degree-four (or 2m-degree) hub of a bouquet; letting a barbell bridge have zero length does not retain transition probabilities. Later equal-petal pinwheel work treats vertex-space instead of the directed edge-space observables here. Thus arbitrary heterogeneous bouquet exact pair and sharp comparison is a genuine unlocated generalization, with small cases potentially known numerically.

## value

PASS

A complete all-parameter comparison between two natural random walks on the same directed-edge state space, with only three exceptional/tie small bouquets, sharpens known non-backtracking intuition and gives reusable closed graph invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
