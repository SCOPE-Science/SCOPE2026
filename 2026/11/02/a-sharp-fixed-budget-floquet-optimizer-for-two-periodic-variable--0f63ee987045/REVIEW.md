# Independent mathematical audit

## correctness

PASS

PASS: Standard interpolation-based variable-step BDF2 scalar decay transfer factors with s=lambda(h1+h2), r=h2/h1 and q=r+1/r>=2 give monodromy trace ((2-s)q+6)/B, determinant 1/B, B=(s+2)q+(s+2)^2+1. Direct symbolic multiplication independently reproduced both invariants. Strict quadratic Schur inequalities establish all fixed positive ratios are stable. Discriminant is (q+2)((s-2)^2 q-2(s^2+4s-4)); for s<=1 roots are real and positive spectral radius grows with q; for s>1, s!=2, conjugate-root modulus B^{-1/2} decreases to q*=2(s^2+4s-4)/(s-2)^2 then real larger modulus increases, giving exact global optimizer and reciprocal ratios. At s=2 all finite q have conjugate multipliers and rho=1/sqrt(4q+17) approaching zero only at unbounded q; sqrt(r)/2 rate for r->0. Independently verified symbolic traces/det, discriminant and Schur identities and multiple numerical optimum values; a tiny floating discriminant at an exact double root required a numerical tolerance, not evidence of mathematical error. Boundary s=1 optimal r=1; no claim about accuracy, transient norm or nonperiodic grids.

## originality

PASS

The fixed-two-period, fixed-total-time spectral-radius optimum (including equal-step transition s=1 and unattained s=2 resonance) is not a direct corollary of general variable-step BDF2 stability theory. Related published exact two-periodic recurrences concern different operators or objectives.

## value

PASS

PASS: Fixed-total-period asymptotic damping is a motivated performance invariant for scalar BDF2 test-equation dynamics. A complete sharp ratio classification, coalescing Floquet critical point, and unattained zero-radius resonance exhibit a nontrivial qualitative transition between numerical stability and rate optimization. The result does not purport to optimize physical accuracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
