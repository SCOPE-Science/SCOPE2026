# Independent mathematical audit

## correctness

PASS

Polar integration gives the stated eigenvalues and integration by parts gives the real-interpolated endpoint difference. For s=n+1 outside the extreme endpoints it has the appropriate strict sign since the bandwise integrand e^(-t)t^(s-1)(t-s) does. Reexpanding the logarithm of the gamma density with x=R+u sqrt(R), t=R+v sqrt(R)+w gives the order R^(-1/2) polynomial in the proof; the linear w term integrates to zero. The even mixture divided by its value at zero is exp(-u²/2)cosh(delta_R u), with quadratic coefficient (delta_R²-1)/2 and critical quartic coefficient -1/12. Direct differentiation of the first Stirling correction gives zero at u=0 and derivative -2/3 after normalization at delta=1. Stirling's differentiated remainders are uniform on the compact u-window. Integrating the derivative over a unit step therefore gives the stated scaled difference and C¹ convergence on bounded y. Away from u=0 the limit has sign tanh(u)-u; for u→0 with |u|/R^(-1/6)→∞ the cubic -u³/3 dominates the O(|u|^5+R^(-1/3)|u|+R^(-1/2)) error. Thus no roots escape the local scale. Simple roots of P' give exactly one real crossing each; their gaps in degree tend to infinity, so discretization produces one or two indices per plateau. Reflection beats every positive quartic maximizer and the negative half-line has a unique critical point; the nonzero limiting separation in peak heights gives the finite-R winner. Equality kappa=1/2 and joint limits approaching it are excluded. The independent recheck scanned the full admissible integer window at two noninteger radii and four kappa values, confirming counts and selection, and found the kappa=0 norm coefficient 0.6276208573 at the larger radius versus limit 2^(-2/3); see independent_recheck.py, annuli. The inspected frozen script asserts mode and norm accuracy, not the printed counts; the proof, not the tests, establishes the theorem.

## originality

PASS

The surviving distinct theorem is the detuned moving-width cusp, with off-threshold plateau count and sharp norm coefficient. Do not credit cubic-root critical drift or inward preference in general as new: the October 18 fixed-width result already gives substantial counterparts, including the same critical profile up to a scalar.

## value

PASS

The Gaussian degeneracy makes the ordinary fixed-separation mode picture uninformative. Resolving it locates the actual discrete plateau transition and mode positions and supplies a sharp operator norm, including the detuned range where the leading Gaussian mixture suggests two modes but the actual spectrum has one. This is a useful narrow asymptotic classification, not a claim about arbitrary windows or the excluded double root.

The dated certificate retains the supplied scientific assessment, sources and limitations.
