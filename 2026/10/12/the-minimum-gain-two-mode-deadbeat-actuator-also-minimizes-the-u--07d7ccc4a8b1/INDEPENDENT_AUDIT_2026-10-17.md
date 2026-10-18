# Independent mathematical audit

## correctness

PASS

The characteristic polynomial trace/determinant conditions force b1k1=a²/(a−d), b2k2=−d²/(a−d) for every admissible b. With x=b1², squared gain equals [a⁴/x+d⁴/(1−x)]/(a−d)², minimized exactly at x=a²/(a²+d²) by Cauchy. Nilpotent nonzero 2×2 closed loop is rank one, so spectral norm equals Frobenius norm. Its squared norm equals [a²(1−x)+d²x]²/[x(1−x)(a−d)²], minimized at the SAME x using [a√(1−x)−d√x]²≥0. Exact rational witness a=4/5,d=3/5,b=(4/5,3/5),k=(4,−3) gives a nilpotent matrix (12/5)[[-1,1],[-1,1]] with spectral norm 24/5 and gain norm5; algebra independently checked on rational values. Blow-up is at fixed coalescence s∈(0,1); no universality for diagonalization by nonorthogonal similarities.

## originality

PASS

Feedback-gain minimization for fixed (A,b) and deadbeat pole assignment are classical. The assessed theorem instead optimizes the unit actuator *direction* jointly for exact two-step nilpotency, finding that the minimizer of required feedback gain equals the minimizer of one-step transient norm. Full available later fixed-input pole-placement and input-co-design sources do not give this result; the inaccessible 1988 Amin–Elabdalla primary full text remains a particular overlap risk, not proof of coverage.

## value

PASS

Two-step deadbeat pole placement is a natural minimal control objective and nonnormal transient amplification is a distinct practical criterion. Solving the first nontrivial continuous actuator-direction co-design determines a previously unstated common optimizer and exact reciprocal-gap blow-up. The result supplies a precise counterintuition: zero closed-loop poles and minimum gain do not prevent a factor-24/5 one-step amplification for a stable open-loop plant. It is motivated structural optimization rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
