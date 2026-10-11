# Independent mathematical audit

## correctness

PASS

For p at most one half, the standard erasure channel is degradable, so the optimum defect is zero. For p greater than one half, covariance twirling and pinching reduce an arbitrary degrading channel to a block-covariant form. Its data-to-data component is a subnormalized depolarizing map. Testing the defect on a maximally entangled input gives the scalar lower bound A*f_q(B/A), with q=d^2 and A at least 2p-1. The exact piecewise minimization of f_q over nonnegative arguments has minimum 2*(1-1/q), attained at one. This proves the lower bound 2*(2p-1)*(1-d^-2). The explicit degrading map in the package leaves exactly (2p-1) times identity-minus-replacer on the quantum block, whose diamond norm is 2*(1-d^-2), and therefore attains the lower bound. An independent symbolic piecewise check reproduced the scalar minimum, while the assigned exact-rational verifier checks the Choi positive-part certificate and the proposed degrading probabilities.

## originality

PASS

Sutter et al. introduce epsilon-degradability and a general SDP for its optimal parameter, but their complete article's application section treats depolarizing, BB84 and randomizing channels rather than solving the erasure-channel SDP analytically. Siddhu and Tayur explicitly use the erasure channel only on the degradable side p<=1/2, where epsilon=0, and note antidegradability above one half; they do not give the nonzero optimum there. Targeted Resultary and web searches for the exact formula, its dimension factor and erasure epsilon-degradability found no earlier closed-form solution. The audited theorem therefore appears to be a genuine analytic solution of a canonical instance of the general SDP.

## value

PASS

The erasure channel is a canonical exactly solvable quantum channel, and epsilon-degradability is a standard capacity-bounding invariant defined by a general SDP. A dimension-dependent closed form on the entire nondegradable half, together with an optimal degrading map and matching diamond-norm lower certificate, is a natural exact benchmark with reusable methodological value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
