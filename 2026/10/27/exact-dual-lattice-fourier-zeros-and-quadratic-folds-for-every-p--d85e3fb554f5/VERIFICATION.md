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

Direct integration on the standard triangle gives the stated numerator and denominator off the three exceptional lines. If it vanishes, w=(1−λ)+λz for λ=η/ξ and the two unit phases z,w. Expanding |w|² gives 2λ(1−λ)(1−Re z)=0; λ can have either sign but is neither 0 nor 1, forcing both phases to one. On an axis or the diagonal the integrated limiting expression would force the modulus of 1±iξ (or 1−iη) to be one at nonzero real frequency, which is impossible; the origin gives 1/2. A change of variables multiplies by a nonvanishing area/phase factor and replaces frequency by Aᵀω, so the lattice is not shifted by translation and the excluded directions are exactly the edge normals. Its covolume is 4π²/|det A|. Boundary cells are in an annulus of fixed width, containing O_A(R) cells, and the three removed lines each lose O_A(R) points. This gives the disk coefficient area(P)/(2π); it is not the density per unit frequency area. The shortest-vector formula follows from local finiteness and for T the permitted pair (1,−1) realizes the minimum squared norm 2. For the fold, at (X,Y) the linear numerator is −i(Xk−Yh) and the quadratic part is (Yh²−Xk²)/2. Along (h,k)=t(X,Y) the quadratic quotient is t²/2, transverse to the purely imaginary derivative image. This establishes the fold condition, not just a nonzero Hessian. For the affine transform the extra derivatives of the phase on this kernel multiply F or DF applied to the kernel direction, both zero; hence the transverse second derivative survives.

## originality

PASS

The vertex-exponential integral and the standard-triangle integer-frequency slice are covered. The distinct result is the complete census of real frequencies, including exclusion of all nonlattice and exceptional-line zeros, together with the real fold classification. The affine transport, first-radius expression and disk count follow from that census and are not independent novelty claims.

## value

PASS

An exact census of real Fourier zeros for a natural nonsymmetric polygon is useful in its own right: for instance it determines which plane waves have zero average and the first possible cancellation radius for the given triangle. It excludes any additional real curves or points and gives a uniform local description of the singular cancellations, distinguishing them from transverse zeros. Neither a general transform formula nor the earlier integer slice suffices for these uses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
