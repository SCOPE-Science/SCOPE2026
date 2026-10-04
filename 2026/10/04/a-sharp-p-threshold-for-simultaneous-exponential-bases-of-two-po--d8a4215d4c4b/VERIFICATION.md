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

For a two-point set \(E=\{x,y\}\) and two characters \(\chi_0,\chi_1\), writing \(\psi=\chi_1\chi_0^{-1}\) gives
\[
\det T(E,\{\chi_0,\chi_1\})
=\chi_0(x)\chi_0(y)\psi(x)\bigl(\psi(y-x)-1\bigr).
\]
Thus the determinant vanishes exactly when the quotient character belongs to \((y-x)^\perp\). This was re-derived symbolically before packaging.

The strict union bound used in the proof is
\[
\left|\bigcup_{j=1}^m d_j^\perp\right|
\le 1+m\left(\frac{|G|}{p}-1\right)
\le |G|-p+1<|G|
\]
for \(m\le p\), where \(p\) is the least prime divisor of \(|G|\).

The accompanying `verify.py` was run from its packaged path. It exhaustively enumerates characters and two-point subsets for several small product groups, checks the determinant/annihilator equivalence and the pair-existence conclusion, and verifies the sharp \(p+1\)-direction obstruction for \(p=2,3,5,7\). It prints `VERIFY_OK`.

The finite checker is not evidence for the universal theorem; the analytic determinant identity and counting proof establish the full quantified claim.
