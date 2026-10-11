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

The verification is finite and exact. `verify.py` reconstructs the sixteen two-simplices, derives all twenty-four edges, and verifies the 1133 vertex-degree profile. It contracts a spanning tree algebraically, giving a sixteen-relation presentation on seventeen cycle generators.

The rational rank is computed by exact fraction arithmetic. All seventeen maximal minors are computed by fraction-free Bareiss elimination; their gcd is \(2\). The primitive right-null cofactor vector gives the free-coordinate homomorphism. Every three-clique is enumerated, leaving exactly twenty nonfacial three-cycles.

The same relation matrix is reduced over \(\mathbf F_2\). The quotient has dimension two, every empty triangle has nonzero class, and the three nonzero quotient classes occur with multiplicities \(8,6,6\). Combined with the integral free coordinate, this proves the torsion/primitive classification.

Replay command: `python verify.py`.

Expected terminal line:

`VERIFY_OK f=8,24,16 valence=4x1,5x1,6x3,7x3 H1=Z+Z/2 empty3=20 integral_classes=8,6,6 torsion_empty=8 primitive_empty=12 mod2_nonzero=20`

Limits: the computation proves only the stated finite classification for the 1133 complex. It does not classify longer cycles or other minimal Klein-bottle triangulations.
