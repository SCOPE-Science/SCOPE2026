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

Run

`python verify_moment_extension.py`

The verifier uses exact rational arithmetic. It checks the source breakpoints, the equality of the two controlling affine exponents at \(\sigma_2\), the sign condition that forces the high-value second term to be maximized at \(\sigma_2\), dominance over the remaining endpoint exponents across the whole interval, and the exact crossing
\[
\frac{520/445121}{58907/445121-1/8}=\frac{832}{5227}.
\]

Expected replay output is stored in `verification_output.txt`:

`VERIFY_OK sigma1=451/3688 sigma2=58907/445121 nu=832/5227 k0=63556/5227 delta12=520/445121 samples=1001`

The 1001-point rational loop is a regression check only. The interval proof is the affine endpoint-and-slope argument in `RESULT.md`; no finite enumeration is used to justify an infinite statement.
