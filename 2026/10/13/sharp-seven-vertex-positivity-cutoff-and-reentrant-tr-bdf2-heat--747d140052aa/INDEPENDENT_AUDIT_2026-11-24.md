# Independent mathematical audit

## correctness

PASS

For the completed step, elimination at the L-stable parameter gives (1+sqrt(2))G²−sqrt(2)G, with G=(I+aL)⁻¹ and a=βh. The periodic Green kernel is positive. With cosh(t)=1+1/(2a), its ratio G_k/G_0 is cosh((n/2−k)t)/cosh(nt/2); its log derivative in t is strictly negative off the diagonal, since x tanh(xt) increases for nonnegative x. As t decreases with a and G²=G+a∂_aG, the diagonal has strictly smallest (G²)_k/G_k. Substitution of G_0=tanh(t/2)coth(nt/2) gives exactly the claimed F_n sign, with strict positivity off the diagonal at the two transition steps. At h=0 the step is the identity. n sinh(t)/sinh(nt) decreases strictly with n for fixed positive t. In an independent exact computation by rational Bernstein collocation I obtained the three n=7 minima 1667336/390625, 165684017/65625000 and 4853759/1562500, all greater than 2; the rational comparison polynomial is a lower bound since U_6(c)≥7. The n=8 sign witness is bounded above by −16383/436900. The product over the real Chebyshev zeros below 1 gives a strictly convex reciprocal on c>1, so the endpoint signs and 5/4 witness imply exactly two roots and strict nesting. The right root converges to sqrt(2); the substitution c=cosh(ξ/n) and sign bracketing at the unique positive crossing of ξ/sinh(ξ)=3−2sqrt(2) justify the scaled return law. Independent 55-digit evaluation gives 4.631334936231… and 10.406445651654… for n=8 and 0.237899999395… for the scaling constant. The independent reproduction is /workspace/branches/independent_checks/trbdf2.py; the packaged script was inspected, not executed. Fourier tests in that script are supplementary, not the proof.

## originality

PASS

The stability map and geometric-resolvent techniques have clear precursors. The closest local sources either use a different rational update on cycles or the same update on a different graph class. None of the inspected results supplies or implies the Chebyshev criterion and strict reentrant window, including the cycle-specific seven/eight cutoff and endpoint laws.

## value

PASS

Cycle diffusion is a canonical constant-coefficient generator and TR-BDF2 is a standard integrator. The exact threshold answers when positivity is unconditional and shows why a single SSP upper step bound cannot describe the full positivity set. The strictly expanding failure bands and quadratic recovery scale give information useful for mesh-size and step-size comparisons; they do not guarantee accuracy or internal-stage positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
