# Same-model review

## Correctness
PASS. The claim is reconstructed directly from the printed six-dimensional vector field. On a bounded complete trajectory, solving \(\dot v+v=y^2\) backwards gives a nonnegative convolution representation. If \(v=0\), then the entire past has \(y=0\); with \(d>0\), backward boundedness forces \(z=0\), and then \(\dot y=k\) contradicts \(k\ne0\). The invariant-measure identities follow from the generator applied to \(u\), \(v\), \(v^2/2\), \(y^2/2\), and \(z^2/2\). The strict upper inequality uses \(0<\tanh v<v\) on the compact support.

## Originality
PASS. Statement-level searches covered the exact source title and DOI, the equation \(\dot v=y^2-v\), stationary balance formulations, positive-half-space formulations, and broader compact-invariant-measure language. The introducing paper discusses equilibria, hidden attractors, Lyapunov exponents, bifurcations, transient degradation, offset boosting, and DSP implementation, but not this theorem. The nearest indexed records concern stationary balances or memory identities in different systems and do not imply the source-specific equality or strict half-space geometry.

## Value
PASS. The source is primarily numerical. The new statement supplies an exact geometric constraint on every compact recurrent regime and a strict moment law that can be used to validate simulations or rule out purported recurrent statistics. The result is parameter-robust over \(a,b,e\) and directly covers the paper's hidden-attractor parameter choice.

## Closest literature and residual limits
The introducing article is the closest source because it contains the exact vector field. A later memristive hyperchaotic-system paper located during comparison uses a different memory equation, \(\dot v=x\), so it does not imply the present convolution positivity or transfer identity. The principal residual risk is that a less discoverable paper may have derived the same stationary law for this exact model without using the searched terminology.

Same-model review: passed. Independent audit: not yet performed.
