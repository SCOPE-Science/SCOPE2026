# Independent mathematical audit

## correctness

PASS

For \(z=x+iy\), the imaginary equation is \(y(3x^2-y^2-(b-a))=0\). Real zeros: exactly one because \(x^3+(a+b)x-1\) strictly increases. Nonreal roots correspond bijectively in conjugate pairs to distinct real roots of \(P(x)=8x^3-2(2b-a)x+1\) satisfying \(3x^2>b-a\); no division at singular thresholds. \(\operatorname{disc}(P)=64[4(2b-a)^3-27]\). For \(b>a\), the negative root always passes the cutoff, and the two positive roots are separated by \(t=\sqrt{(b-a)/3}\) according to the signs of \(E=4(a+2b)^2(b-a)-27\) and \(H=3a-2b\), including strict exclusion at equality. The proof reproduces all 3/5/7 cases and the \((a,b)=(3,5/2)\) open seven-regular-zero witness. Independent \(\operatorname{numpy.roots}\) stationary-root checks on 3000 deterministic positive parameter pairs agreed with the table; these samples supplement the exact cubic argument.

## originality

PASS

Best-of-knowledge: the complete \(a,b>0\) discriminant/collision classification of distinct zeros is not implied by the materially inspected same-family results; originality is specifically the off-diagonal complete map, not the known diagonal or asymptotic sectors.

## value

PASS

A complete two-dimensional phase diagram of the smallest nontrivial cubic harmonic quadrinomial is a motivated classification: it identifies open maximal-valence regions, distinct singular collision loci, and the unexpected orientation-preserving \(a>b\) seven-zero phase. The precise boundary counts are not immediate from existing sector inequalities and are reusable for caustic/valence questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
