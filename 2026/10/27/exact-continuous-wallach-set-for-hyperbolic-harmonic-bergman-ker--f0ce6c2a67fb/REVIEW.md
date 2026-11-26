# Independent mathematical audit

## correctness

PASS

The normalization and meromorphic identity are correct: write S_m(t)=1+(m/2)(1-t), integrate its three squared terms against the beta weight, and factor the common gamma denominator. The result is (1), with the separately normalized constant sector I_0=1. For s>=-2 the coefficient is finite and positive, and at -2 it equals one. On (-4,-3) both the gamma quotient and the affine-in-m bracket are negative. On (-3,-2) and (-5,-4) the quotient is positive and the slope of the bracket is negative, so some large degree gives a negative coefficient. For noninteger s<-5 the I_1 denominator has three negative factors, while its numerator is a positive multiple of 3(s+2)(s+5)+4. At s=-k, k>=3, choosing m=k+3 gives denominator Gamma(8) and nonzero bracket: -2m for k=3,4, 4 for k=5, and positive for k>=6. These poles exclude all remaining integers. For admissible s other than -2, the gamma ratio and the nonzero linear leading term give I_m(s)^{-1}=O(m^(s+1)); at -2 the inverses are one. On compact subsets, the spherical addition kernel is bounded by the dimension (m+1)^2 under the normalized angular norm, the S_m factors are at most linear, and the radial factor decays geometrically. Thus the positive-weight kernel sum converges there to the kernel of the Hilbert completion. A negative sector would violate kernel positivity by angular orthogonality on a sphere of fixed radius. The finite checks described in VERIFICATION.md and verify.py are not a replay or an all-degree proof.

## originality

PASS

Credit is confined to the simultaneous real-parameter positivity classification in real dimension four. The coefficient formula itself is just the n=4 evaluation of Moravík's existing general formula, and the s=-2 identity is already known. The primary papers supply the problem and input formulas but do not settle the continuous sign set; the proof must handle all harmonic degrees and global pole exceptions, not just substitute n=4. No earlier statement or positivity theorem implying the same set was identified in the bounded comparisons.

## value

PASS

The invariant is explicitly motivated by the previously posed continuous Wallach problem. The exact set determines which continued hyperbolic-harmonic norms on the real four-ball give genuine positive kernels. The disconnected second interval and its exclusion boundaries cannot be inferred just from the physical weights or the discrete residue parameters. This supplies a complete answer in one natural low dimension where the angular radial factor is nonconstant, without claiming a result in all dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
