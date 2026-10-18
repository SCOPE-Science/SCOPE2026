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
# Verification of integral and rational calculations

Run `python verify_integral.py` and `python verify_independent.py` with Python 3.9 or later. Both programs use the Python standard library only; no external datasets, serialized caches, or other files are needed. The programs enumerate the same mathematically defined complex by independent methods, not by reading each other's output.

The first verifies the complete \(2,927\)-face set including the empty simplex, acyclicity of all oriented nonempty Hasse covering relations, \(1,415\) Morse pairs, critical vector \((1,24,54,17)\) in dimensions \(0,3,4,5\), signed Morse differential \(\partial_5=0\), exact rational rank \(11\) of \(\partial_4\), and the determinant \(-1\) of its explicit \(11\)-minor. These establish free reduced integral groups of ranks \(13,43,17\).

The second enumerates faces by combinations and independently checks unsigned Betti ranks of direct simplicial chains over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_{101}\). It constructs signed rotation-orbit chains and obtains ranks \((2,22,68,90,20)\) in degrees \(1\) to \(5\) over \(\mathbb Q\), cross-checked over \(\mathbb F_{101}\) and \(\mathbb F_{1000003}\). The rational invariant Betti numbers are \((1,7,5)\) in dimensions \(3,4,5\).

The computations exhaust one finite, precisely specified object; they do not assert an infinite-family result, the integral homology representation, or a full homotopy decomposition. Independent mathematical audit has not been performed.
