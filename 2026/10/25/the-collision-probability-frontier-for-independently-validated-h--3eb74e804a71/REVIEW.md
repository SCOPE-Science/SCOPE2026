# Independent mathematical audit

## correctness

PASS

On each pair of independent update/validation indices, the normalized feedback is zero off the diagonal and equals -alpha+h alpha²/(2p_i) when xi=zeta=i, hence E H=-c alpha+(h/2)alpha², uniquely minimized at c/h. Frozen coordinate multiplier is 1-c/p_i. If c<2 min p_i each coordinate contracts on infinitely many independent matched events (prob p_i²), yielding a.s. convergence for all tie policies. If c>=2p_i, any accepted move fails to decrease |x_i|, giving pathwise necessity, including equality and any initial nonzero bad coordinate. Exact collision convexity over simplex p_i>=m gives worst-case vertex (1-(d-1)m,m,...,m) and threshold 1/(sqrt d(sqrt d+1)). Independent Fraction computations verified the expectation, raw/gated one-step factors and d=2 threshold on rational test grids; p=(1/4,3/4) yields unguarded factor 21/16, gate-with-ties-accepted 79/64. Only frozen population-optimal scalar steps are proved, not online step learning. Individual f_i have nonunique hyperplane minimizers but share the unique *common* zero point, clarifying an imprecise phrase in the package.

## originality

PASS

Zhang–Gao–Ye–Udell introduce exactly the motivating independent out-of-sample normalized feedback and conditional convergence for the online algorithm, but not the present sparse coordinate collision threshold or every tie-policy failure. Qu–Richtárik arbitrary-sampling coordinate methods and published scalar-feedback curvature results treat other rules/models. Search compared mathematical implications, not merely coincident hypergradient words.

## value

PASS

The collision probability c is intrinsic to two independent sample indices; its exact comparison to twice the least coordinate probability gives a sharp design/instability frontier. The all-tie-policy failure shows a concrete blind spot of independent validation even with globally strongly convex interpolating objective; a four-component uniformly sampled example is realizable. No false assertion about failure of the full adaptive algorithm is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
