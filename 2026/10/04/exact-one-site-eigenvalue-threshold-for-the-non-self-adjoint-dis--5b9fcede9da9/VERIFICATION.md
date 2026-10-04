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

The analytic check starts from the published Laurent resolvent formula. For a potential supported at one site, the eigenvalue equation at an off-spectrum parameter \(\lambda\) is equivalent to singularity of \(I+v_0T_0(k)\). If this matrix is singular on a nonzero vector \(x\), then
\[
1\le \|v_0\|\,\|T_0(k)\|.
\]
Conversely, a top right singular vector of \(T_0(k)\) gives an explicit map taking \(T_0(k)x\) to \(-x\), and an orthogonal extension gives exactly any prescribed norm above the threshold.

The bundled `verify.py` uses only the Python standard library. It checks representative complex parameters by reconstructing \(k\), \(T_0(k)\), and a maximizing singular vector; it verifies the prescribed map, the block norm, and numerical singularity of \(I+v_0T_0(k)\). It also searches a small grid for a point with \(\|T_1(k)\|>\|T_0(k)\|\), and confirms that on the improved-boundary normalization \(Q=1/\|T_1(k)\|\) the necessary one-site inequality fails.

Run:

`python3 verify.py`

Expected terminal line:

`VERIFY_OK cases=4 off_diagonal_obstruction=1`

The computation is not used to infer an infinite or exhaustive statement. The proof is exact and finite-dimensional once the published resolvent identity is accepted.
