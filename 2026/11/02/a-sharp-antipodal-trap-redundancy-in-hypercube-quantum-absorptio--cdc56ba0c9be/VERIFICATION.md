---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For Q_d, d>=2, adjacency Hamiltonian J A with J nonzero, two positive local irreversible sink rates, the dark space is the orthogonal complement of the two-source cyclic subspace B=span{H^j|a>,H^j|b>}; any nondecaying eigenvector of H-iK/2 must lie in ker K and thus be dark. Finite-dimensional evolution on B decays, even with Jordan blocks. Uniform mixed initial state yields eta=dim(B)/2^d independently of rates. Distinct Walsh eigenspaces indexed by l have rank 1 at l=0,d. If separation k=d, parity of intersection with b is constant across each l-subset, giving rank 1 in all d+1 levels. For 1<=k<d, both parity signs occur among each 1<=l<=d-1 (connectivity of Johnson l-subset graph and availability of an inside-outside exchange), giving rank 2, hence total rank 2d. Checks of exact Walsh parity rank for every 2<=d<=11 agree. The proof is all-dimensional; finite tests only corroborate.

## originality

PASS

Novo et al 2015 and Razzoli et al 2021 establish the single-trap bright cyclic subspace and hypercube baseline, not this two-sink classification. The full-text 2021 paper specifically treats a single trap and concludes multiple traps require future analysis, supporting the no-direct-coverage comparison. Multi-marked quantum walks remain a broader priority risk.

## value

PASS

The difference between an antipodal second sink (zero marginal benefit) and any other second sink (uniform best gain) is a sharp, unexpected design law for coherent transport on a canonical symmetric graph. It gives an exact all-dimensional optimal trap-placement classification beyond a routine single-trap calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
