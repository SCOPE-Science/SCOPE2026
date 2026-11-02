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

# Reproduction and proof boundaries

Execute `python3 verify.py` using the Python 3 standard library. The verified package replay returned `VERIFY_OK 100 checks; exact traces, Fourier-resolvent identity, finite-size constant, optimized drift`.

The checker constructs weighted toroidal Laplacians at \(n=3,4\) and rational conductances, then computes the exact trace of the inverse of \(L+\mathbf1\mathbf1^T/n^2\) minus one using rational Gaussian elimination. It compares these values to Fourier reciprocal eigenvalue sums. Additional checks compare the Chebyshev cycle-resolvent formula at seven sizes and seven anisotropies, measure the explicit constant-term error at three larger sizes across seven anisotropies, and solve positive directional price-allocation problems for five price choices and four sizes.

No finite check certifies the infinite asymptotic. The analytic proof relies on the matrix strict-convexity calculation, the exact cycle resolvent, uniform endpoint-layer summability with its first two parameter derivatives, and differentiation of a unique interior minimizer. A direct comparison of result and proof uses the same \(\operatorname{tr}(L^+)\) normalization throughout; the unordered-pair Kirchhoff index is \(n^2\) times that trace.

The focal source was first made public 2013-09-09 (arXiv:1309.2172), distinct from its later journal publication. The independently supplied proof has not been externally validated, and specialized historical priority remains open.
