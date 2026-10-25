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

# Reproducible mathematical verification

The separate file `vr_cube_translation_check.py` is a standalone Python 3 script requiring only the standard library. Run `python3 vr_cube_translation_check.py`. It verifies the predicted Betti numbers by Euler characteristic, all signed oriented-simplex translation Lefschetz traces for \(n=3,4,5,6\), the Fourier multiplicities at each possible character weight, all forty-eight dimension-three affine symmetries, and the exterior-cube coordinate-permutation traces (all twenty-four permutations at dimension four and one representative per seven conjugacy classes at dimension five). A successful replay prints `RIPS_QN_TRANSLATION_CHARACTER_CHECKS_OK 281`.

The complete mathematical proof in `RESULT.md` does not depend on these finite tests. In particular the general cube orbit graphs and three-cube orientation degrees are proved by direct combinatorial arguments. The script's clique-generation procedure is explicit and independently checks pairwise distances but does not itself certify maximal-clique exhaustion in unbounded dimension; the proof does not depend on that empirical assertion. The full integral equivariant lattice is not classified, and no external independent validation is claimed.
