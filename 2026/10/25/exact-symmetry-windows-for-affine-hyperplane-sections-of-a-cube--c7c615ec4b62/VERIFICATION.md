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

# Verification evidence and limits

The complete proof is in RESULT.md. The critical steps are the nonparallelity of distinct restricted coordinate normals for three or more nonzero coefficients, pairing of actual facets under a central inversion, at least \(r-1\) active coordinate pairs by boundedness, and equivalence of full coordinate projection to \(W-w_j\le t\le w_j\). The converse follows from reflection at the central offset or the explicit affine-cube parametrization. The case \(r\le2\) and endpoints are treated separately.

The standalone checker `verify_cube_slices.py` uses only Python's standard library and `fractions.Fraction`. It enumerates vertices via cube-edge intersections and checks symmetry exactly by vertex-pair reflection. In dimensions \(3,4,5\), all nonzero coefficient vectors with entries from \(\{0,1,2,3\}\) and all positive half-integer offsets below the coefficient sum were tested: exactly \(17{,}667\) slices. Output: `CUBE_HYPERPLANE_SYMMETRY_OK 17667 exact rational sections`.

Finite computation is neither a proof in all dimensions nor a test of historical priority. Full-text historical comparison is incomplete for one old publication. No independent audit has been performed.
