# Independent mathematical audit

## correctness

PASS

For the specified state-dependent transition law, iteration gives log2|z_n| = 2^n(t-R_n), with t=log2 r. At t=R the scaled remaining tail lies in [0,1], so there is no escape; every coding cylinder has mass at most (1-eps)^n and the at-most-two expansions of a point give no atoms. Hence endpoint threshold conventions do not affect either exact identity. On the upper and lower endpoint intervals of width 2^-n in t, the forced prefixes are respectively n ones and n zeros; subtract the prefix and rescale the tail. The two deterministic runs saturate after at most any N such that (1-alpha)^N(1-eps)<=eps, uniformly in p. Their masses then factor into the displayed positive prefactors times (1-eps)^n. Digit/state complementation identifies the two tails; for phases u in [1/2,1] the common profile is in [1-eps,1], yielding uniform sharp bounds, with the radial changes of variable having nonzero endpoint derivatives. At alpha=1/2, eps=1/4 the probability of the prefix 01 is 3/32, giving H(3/4)=27/32; (3/4)^log2(4/3) > sqrt(3)/2 > 27/32, giving distinct normalized subsequential limits. The finite-cylinder checker is supplementary, not a replacement for these arguments.

## originality

PASS

The clipped law, polynomials, continuity, and escape probability one at r=2 are prior, not contributions. In the evidence inspected the paired exact all-state endpoint profiles and the explicit non-power-law witness are not established by an existing endpoint theorem. They use a finite-saturation and complement argument in the exact prior model; proximity to that model considerably limits the novelty claim.

## value

PASS

The sharp modulus at both boundaries is a natural quantitative gap for a known escape function. The exact finite-level common profile gives state-uniform control while distinguishing a genuine discrete-scale oscillation from a pure power asymptotic; this is useful beyond either endpoint continuity or a local-dimension number. It does not claim arbitrary parameters oscillate or give interior regularity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
