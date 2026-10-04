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

The proof reduces normalized nonnegative weak tiling to an exact linear system. If \(d\in(A-A)\setminus\{0\}\), then nonnegativity and \(h(0)=1\) force \(h(d)=0\). Thus any candidate complement must satisfy the displayed convolution equations and difference-zero equations.

The accompanying `verify.py` uses only Python's standard library and exact `Fraction` arithmetic. It verifies:
\[
|\mathrm{GL}(4,2)|=20160,
\]
all \(32768\) normalized subsets are partitioned into \(46\) generated linear orbits, exactly \(9\) orbit representatives tile, and each of the \(37\) non-tiling representatives has augmented rank exactly one greater than coefficient rank in the necessary weak-tiling system.

It also verifies the normalized tiling-set counts
\[
1,15,455,1395,1
\]
at sizes \(1,2,4,8,16\), respectively. The script prints `VERIFY_OK`.

No floating-point linear programming is used in the packaged verification.
