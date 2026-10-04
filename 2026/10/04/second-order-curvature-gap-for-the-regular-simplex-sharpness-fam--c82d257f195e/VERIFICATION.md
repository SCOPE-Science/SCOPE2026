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

The proof uses no finite enumeration to establish an infinite statement. The following checks were performed on the final package:

- The regular-simplex cap is the exact homothetic copy with scale \(m/(m+1)\), hence its Euclidean volume fraction is \((m/(m+1))^m\).
- The full-simplex second moment is \(m^2/(m+2)\).
- The cap second moment differs from the full-simplex moment by
  \[
  -\frac{m^2(m-1)}{(m+1)^2(m+2)}.
  \]
- Combining this difference with the gnomonic density expansion \((1+\varepsilon^2\lVert y\rVert^2)^{-n/2}\) gives the normalized \(\varepsilon^2\) coefficient \(m^2(m-1)/(2(m+1)(m+2))\).
- Since \(m\varepsilon=\tan\rho\), the normalized \(\tan^2\rho\) coefficient is \((n-2)/(2n(n+1))\).
- `verify.py` replays these identities with exact rational arithmetic for dimensions \(3\) through \(80\) and prints `VERIFY_OK`.

The finite replay is a sanity check only. The general proof is symbolic and is given in `RESULT.md`. No global spherical stability theorem or optimality among all shrinking families is verified or claimed.
