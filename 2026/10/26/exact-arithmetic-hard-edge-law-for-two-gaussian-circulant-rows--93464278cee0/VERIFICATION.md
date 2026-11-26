---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The two Gram diagonals are ||g||^2 and the off-diagonal is g^T C g for C=(S+S^T)/2. The lower eigenvalue is the minimum of the forms I-C and I+C. Each of d cycles has the L cosine eigenvalues, giving the I-C nullity d and the I+C nullity d only for even L. On each cycle the nonzero product for I-C is L^2/2^(L-1): taking absolute squares in the roots-of-unity identity prod_(j=1)^(L-1)(1-exp(2 pi i j/L))=L proves it. When L is even the alternating signs conjugate I+C to I-C. On the positive k-dimensional eigenspace Gaussian density at zero times the ellipsoid volume gives t^k/[2^(k/2) Gamma(k/2+1) sqrt(pseudodet)]. For odd L the other event is O(t^m); for even L their intersection implies ||g||<=t by summing the forms, hence is again O(t^m). The leading positive coefficient proves full row rank a.s. and the pseudoinverse moment cutoff by the tail integral, with logarithmic divergence at equality. Independently, write g=Ru with R independent of u; for p<m, E R^(-p) is positive finite and factors exactly from E sigma_min(g)^(-p). On the sphere, 1<=sigma_max(u)<=sqrt(2), so the same criterion holds for the condition number at p<m. For p>=m divergence follows from the already divergent p=k moment and kappa>=1. At m=2,r=1 the two singular forms give independent absolute coordinates scaled by sqrt(2), consistent with the coefficient 2/sqrt(pi). An independent exact cofactor check on signed cycle Laplacians passed 212 cases for 2<=m<=18, including the two-cycle parallel-edge convention; replay with python3 /workspace/reproductions/independent_finite_checks.py. The frozen verifier was read, not run; its numerical and positivity checks do not prove the hard edge.

## originality

PASS

Pass for the explicit fixed-size unnormalized shifted-row arithmetic law, not for Gaussian ellipsoid small-ball geometry, generic quadratic-form distributions, or Fourier diagonalization. The closest Hankel result agrees with the coprime exponent but changes the dependence, gives bounds rather than the coefficient, and has no cyclic parity. The closest Gaussian rectangular circulant paper treats growing aspect ratio, not this hard edge. The real numerical shadow is a known equivalent angular variable and gives a general distributional representation; the contribution here is the explicit two-endpoint repeated-spectrum and radial small-value analysis with the arithmetic constant, not a new angular distribution principle. No inspected source covers that full law as a straightforward parameter substitution.

## value

PASS

The sampling shift is an actual design parameter. Within one ambient m it changes the exponent from m-1 in the coprime case to m/2 for a half-cycle shift when m is even, and parity independently counts the contributing rank-loss mechanisms. The exact law quantifies rare instability, distinguishing almost-sure invertibility from finite inverse moments. It provides a sharp fixed-size benchmark for dependent sketches, beyond a generic probability bound or an obvious statement of full row rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
