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

# Verification

Run `python3 verify_prism.py` using Python 3 and the standard library. The exact test program checks the signed cellular Lefschetz trace for every \(D_n\times C_2\) element with \(4\le n\le18\), reconstructing the graph and deleted square-complex cells independently of the closed-form proof. For \(4\le n\le10\), it constructs every disjoint face-pair torus chain, verifies its integer cellular boundary is zero, identifies a unimodular coefficient minor, and computes the mod-two rank of the second boundary, thereby checking both Betti-number formulas at these parameters.

Expected terminal lines:
```
VERIFY_OK_PRISM_GRAPH_TWO_PARTICLE
ALL_SYMMETRIES_N4_TO18_SIGNED_CELLULAR_LEFSCHETZ
EXACT_TORUS_BOUNDARIES_AND_UNIMODULAR_MINOR_N4_TO10
MOD2_SECOND_BOUNDARY_RANKS_N4_TO10
H1_CHAR_SIGN_TWIST_FACES H2_SIGNED_NONADJACENT_PAIRS_PLUS_CAP_SWAP
```
These checks are genuine exhaustive finite calculations but do not, alone, prove the all-parameter theorem. The latter relies on the explicit modular indicator identity, the uniform planar face-pair basis theorem, and the representation-theoretic argument. The precise differences between topological quotient homology and quotient-group homology are addressed through finite-group rational transfer. Publication priority has not been independently certified.
