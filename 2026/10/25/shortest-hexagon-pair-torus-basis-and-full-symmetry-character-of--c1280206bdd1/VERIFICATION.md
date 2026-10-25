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
# Exact reproducibility

Run `python verify_heawood.py` in a directory containing the bundled `requirements.txt`, after installing the listed dependencies. The verifier constructs the LCF graph and a separately defined Fano incidence graph; builds all cells of the unordered deleted cubical product and both signed boundary maps; tests their composition; enumerates the 28 hexagons and 42 vertex-disjoint pairs; constructs their integral product-torus cycles and verifies their vanishing boundary.

The explicit fourteen-column by fourteen-row coefficient minor equals \(-1\), and elimination over \(\mathbb F_{101}\) gives boundary rank 154. These two tests together prove the top integral homology basis: the integral unit minor gives a saturated rank-fourteen subgroup and the modular rank provides the matching rank upper bound for the kernel. The Smith normal form of the boundary has invariant factors \(1\) repeated 153 times and \(2\) once. Connectedness and the Euler characteristic give \(H_1\cong\mathbb Z^8\oplus\mathbb Z/2\).

The full automorphism test enumerates 336 graph automorphisms, checks signed transformations of actual cellular torus chains and compares their integral coordinates with the full chains, then computes all character values. The trace values are also checked by an independent fixed-cell Lefschetz calculation and the graph cycle-space character. The program asserts all these claims and ends with the message `INDEPENDENT_FIXED_CELL_LEFSCHETZ_CHECK_ALL_AUTOMORPHISMS` following `VERIFY_OK_HEAWOOD_HEXAGON_TORUS_INTEGRAL_BASIS_AND_CHARACTER`.

Limit: these tests establish statements about the specified finite graph. They neither classify related graph families nor determine an integral irreducible group-ring decomposition. No external independent scientific validation is claimed.
