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

# Reproducibility and verification

Extract `verify.py` and `cocycle.json` into the same directory and run `python3 verify.py` with Python 3 and NumPy installed. The checker independently reconstructs the off-diagonal rook positions, enumerates every matching, and constructs the integer oriented simplicial chain matrices in degrees one through four.

The exact computed face numbers in dimensions zero through four are \((20,130,320,265,44)\). Reduction over the primes \(3\) and \(101\) gives boundary ranks \((19,111,208,44)\). Over the integers, every consecutive boundary composition is zero. The code constructs an eight-triangle two-cycle \(z\), loads the standalone 120-entry signed cochain \(\phi\), and verifies \(\partial_2 z=0\), \(\delta^2\phi=0\), and \(\langle\phi,z\rangle=2\). These integer equalities, not modular extrapolation, establish the required nonzero rational second-homology class; the argument in `RESULT.md` upgrades the modular rank lower bounds to equal rational ranks.

The checker computes signed fixed-simplex traces for all \(240\) automorphisms, checks their conjugacy-class consistency, constructs the seven orthonormal rational irreducible characters of \(S_5\), and checks all four possible one-dimensional degree-two characters against exact integral multiplicities for the resulting degree-three representations. A single candidate remains, giving the displayed three-Specht degree-three decomposition.

Expected terminal lines:

`VERIFY_OK CROWN_5 F_VECTOR_20_130_320_265_44 RANKS_19_111_208_44`

`GROUP_ORDER_240 H2_TRIVIAL_TIMES_TRANSPOSE_SIGN H3_4_PLUS_5_PLUS_4`

The code verifies finite exact identities; the theorem uses elementary chain algebra and ordinary rational finite-group representation theory to draw its mathematical conclusions. It does not certify a general family, an integral representation lattice, or publication priority. Independent audit has not been performed.
