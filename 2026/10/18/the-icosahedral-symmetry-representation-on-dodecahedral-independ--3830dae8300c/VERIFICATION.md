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
# Reproducible checks and boundaries

Execute both files in the same directory: `python3 verify_character_and_homology.py` and `python3 verify_signed_traces.py`. The second requires a locally installed NetworkX package. Successful execution of each prints `VERIFY_OK`.

The first enumerates all independent sets by recursive include/exclude branching, builds the seven simplicial boundary matrices implicitly as bit vectors and eliminates over \(\mathbb F_2\). It constructs 120 automorphisms by three explicit checked graph automorphisms, and evaluates the exact equivariant Lefschetz traces via fixed permutation cycles. The second separately tests every bitmask, uses row-based boundary elimination, enumerates graph automorphisms by GraphMatcher, and evaluates oriented-sign traces on each invariant simplex. Both return 5,828 faces including the empty face, mod-two reduced homology dimension four in degree five, and the order/trace census \((1,4):1\), \((2,-4):1\), \((2,0):30\), \((3,1):20\), \((5,-1):24\), \((6,-1):20\), \((10,1):24\).

The finite exact computations establish the stated rational representation for the fixed finite graph when combined with Euler characteristic, the Hopf trace formula and the classical identification of the dodecahedral automorphism group. They do not certify a general theorem for other generalized Petersen graphs, integral torsion-freeness, the integral equivariant lattice, or equivariant homotopy type.
