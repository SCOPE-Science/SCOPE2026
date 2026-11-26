# Independent mathematical audit

## correctness

PASS

For c>xi the response (z+xi)/(z+c), z=x/(1+b x^2), is strictly increasing in z. With gamma=1/sqrt(b), the normalized response gap factors exactly as beta(c-xi)b(x-gamma)^2/[(1+2c sqrt(b))(c(1+b x^2)+x)]. This ensures predator monotonicity; positivity, logistic upper comparison and regularity give global bounded solutions. If y tends to a positive L, the response gap is integrable along the trajectory and uniformly continuous, hence tends to zero. Its only zero on the bounded prey range is gamma, where the limiting prey derivative would be -f(gamma)L<0, a contradiction. Once y tends to zero, comparing x with logistic equations of growth rates 1 and 1-epsilon gives x tending to gamma. The exact quotient w=(x-gamma)/y solves w'=-(x/gamma-a(x))w-f(x), where a is the gap; the coefficient tends to 1 and forcing to -F with F=f(gamma). A stable scalar variation-of-constants argument gives w tending to -F. With G=-g''(gamma)=2(c-xi)b^(3/2)/(1+2c sqrt(b))^2, the derivative of y^-2 tends to beta G F^2. Integrate and divide by t to recover both stated constants. The positive leading constants rule out exponential approach on these trajectories. Global means finite strictly positive initial densities, not the invariant x=0 or y=0 faces. Replay: RESULT.md lines 32–97; verifier.py lines 9–43 inspected, not executed, checks identities and the rational witness but not global convergence.

## originality

PASS

The supported distinct claim is the global sharp law at the tuned predator-free collision in these exact equations. The numerical-response maximizer and coincident root are already in Verma et al.; neither a general local cubic exponent nor the coalescence itself is credited as new. The closest catalogue analogue has extinction of the other species in a different functional-response system.

## value

PASS

The equality omitted by strict linear stability is a natural extinction boundary. Resolving the double threshold for all strictly positive initial densities, with a sharp non-exponential rate and explicit coupled coefficients, distinguishes genuine critical slowing from mere local nonhyperbolicity. The exact parameter tuning limits applicability and no ecological intervention inference follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
