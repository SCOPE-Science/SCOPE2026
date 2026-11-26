# Independent mathematical audit

## correctness

PASS

With r=B/T the area element is T^2 r dr dθ. At fixed area subtract the common threshold q/T on the symmetric difference: the loss away from the strict superlevel region is strictly positive except on a null level set. The area of the bounded Jordan superlevel region decreases continuously from infinity to zero; differentiation gives H'(A)=q/T. Near the constrained maximizer the normalized density drop is 2 tanh(ρ)(r−ρ)+2(θ−π/4)^2 to leading order. For threshold q=sech²(ρ)(1−η) the limiting parabolic strip gives A/T² ~ sqrt(2)ρ η^(3/2)/(3 tanh ρ); integrating the marginal deficit gives the stated A^(5/3) coefficient. At the opposite end, the angular log-sine moments give A/T²=(π/16)(log(1/q)+log 2)^2+π³/192−πρ²/4+o(1); the endpoints can be bounded in layers of width O(sqrt(q)), with integrated quadratic logarithmic factors tending to zero. Thus q(A)~2 exp(−4 sqrt(A)/(sqrt(π)T)); integrating the marginal yields exactly the stated sqrt(πA) prefactor. The total flux follows by the radial primitive G with G(∞)=log 2. These limits hold at fixed T and positive ρ, not uniformly in the cutoff. The source Python checker was inspected, not executed; the prose report of 114 assertions has no attached output and is not the basis of the analytic verification.

## originality

PASS

The curvature, full-quadrant Landauer limit and threshold rearrangement are not new. The distinct claim supported by bounded source comparisons is the sharp fixed-Euclidean-area envelope including the positive-gap cusp coefficient and the gap-independent leading large-area deficit.

## value

PASS

For the specified slow qubit pump, an ordinary control-area budget selects an actual unique contour. The fractional correction quantifies the effect of a positive-gap boundary maximum, and the large-budget law determines how rapidly a finite contour can approach its available flux. These evaluated sharp laws add information beyond the generic rearrangement or an unconstrained cap. They do not predict finite-speed performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
