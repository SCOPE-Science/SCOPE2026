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

# Verification of the Schläfli sampling statement

## Reproduction

Run `python3 verify_schlaefli.py` in the directory containing this document and that standalone script. The script uses only the Python 3 standard library (`fractions`, `math`, `itertools`) and must finish with `SCHLAEFLI_ALL_DEGREE_CERTIFICATE_OK 27 points, 9 exact ranks`.

The verifier constructs all 27 points in exact rational coordinates with a factored \(\sqrt3\) scale on the first five axes. It checks the norms, both off-diagonal inner products and their multiplicities, all 729 entries of \(A^2=8I+2A+8J\), all 729 entries of the Gram-matrix linear combination at each \(0\leq k\leq8\), the exact three eigenvalues at each of those degrees, and 27-by-27 exact rational Gaussian elimination for each of the nine asserted ranks. It checks the strict rational inequalities \((16/15)^3<(10/9)^2\), \((4/3)^3<(8/5)^2\) and \(304/3<110\).

## Infinite-degree proof and limits

The code alone does not establish anything for every \(k\geq9\). That conclusion follows from the proved identity \(C_k^{(2)}=U_{k+1}'/2\), the trigonometric Chebyshev expression and the analytic bound \(|P_k(t)|\leq3/[(k+1)(k+2)(1-t^2)^{3/2}]\). It implies all three exact Gram eigenvalues are strictly positive at every integer degree at least nine. The finite and infinite proof portions are independently stated in `RESULT.md`; no extrapolation, interval timeout, symbolic black box or external certificate is used.

The theorem does not assert original construction of the Schläfli configuration, a new general Gegenbauer addition formula, or any independent validation. Older implicit equivalent formulations remain a literature risk.
