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
The mathematical proof is based on explicit convolution, the two jumps of the correlation's second derivative, Fourier integration by parts, and a two-real-variable implicit-function theorem. Differentiation of the three exponential pieces verifies \(f,f'\) are continuous and \(f''(0+)-f''(0-)=-1\). Numerical zeros are not used to establish an infinite count.

`CHECK.py` requires Python 3, NumPy, and SciPy. Run `python CHECK.py` to reproduce the `CHECK_OUTPUT.txt` results. The checker uses exact elementary exponential integral formulas and two-dimensional root solving for the example \((a,b,r)=(2,3,1)\) and tests the high-frequency threshold ratio in representative regimes. Its finite checks do not certify the asymptotic uniformity or bibliographic novelty. Independent audit is not performed.
