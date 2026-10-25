---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

The proof for arbitrary finite planes is the two-contractible-piece simplicial cover and its **signed integral** Mayer–Vietoris connecting map. Nothing in the finite verification purports to establish the infinite-parameter statement by sampling.

Execute `python3 verify_fano_rips.py` from this directory. The script uses only the Python standard library. It independently builds the point–line incidence relation on the seven nonzero binary three-vectors; verifies line and point degree three and uniqueness of join/intersection; enumerates all \(331\) nonempty scale-two Rips faces and the complete face vector \((14,63,112,84,42,14,2)\); and performs explicit binary Gaussian elimination on all six nonzero simplicial boundary matrices, obtaining ranks \((13,50,54,30,12,2)\) and mod-two Betti ranks \((1,0,8,0,0,0,0)\).

The same program enumerates all \(168\) invertible binary matrices and the additional \(168\) point–line-exchanging symmetries. For each of the \(336\) permutations, a signed oriented-fixed-face Lefschetz sum is compared with the independent graph-cycle character formula, including the change of sign on dualities. The complete group-type multiplicities, squared character norms for both the full group and its color-preserving subgroup, and the polarity traces \(-2\) and \(+2\) are checked. The program also checks equality of the resulting eight-row character with the already published residual Heawood matching-homology character.

Additionally execute `python3 verify_matching_bridge.py`. This script independently builds all \(3461\) nonempty simplices of the Heawood ordinary matching complex, computes its six mod-two boundary ranks \((20,148,496,722,312,24)\), constructs the eight Sylow-seven subgroups of the color-preserving group, and checks all \(336\) elementwise equalities between the matching residual character \(W\) and the Rips degree-two character. This run must print `HEAWOOD_RIPS_MATCHING_CHARACTER_BRIDGE_OK`. The finite ranks saturate rational upper bounds by the chain-complex dimension inequalities and therefore agree with the rational ranks used to identify \(W\).

The first test must terminate with `FANO_RIPS_EQUIVARIANT_CHECKS_OK`. It verifies the specified finite Fano specialization and relevant calculations; no integral equivariant homotopy splitting and no integral cross-complex matching-module equivalence is asserted. No independent audit has been performed.
