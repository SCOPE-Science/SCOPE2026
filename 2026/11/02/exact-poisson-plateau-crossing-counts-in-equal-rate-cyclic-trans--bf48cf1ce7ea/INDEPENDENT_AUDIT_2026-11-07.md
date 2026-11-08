# Independent mathematical audit

## correctness

PASS

Marked interarrival times are iid Erlang(n,gamma), so the stationary renewal covariance transform gives F=[(1+z²)^n−1]/|(1+iz)^n−1|² for z=omega/gamma. The sign of F−1 is sign[Re(1+iz)^n−1]. Substituting theta=arctan z gives H_n(theta)=cos(n theta)/cos(theta)^n, H_n prime=−n sin((n−1)theta)/cos(theta)^(n+1); its strict alternating extrema below −1/above 1 and final divergent endpoint imply exactly floor(n/2)−1 simple positive roots. At omega=0 the continuous value 1/n; n=1 is a flat Poisson exception, not counted. Independent symbolic positive Sturm root counts and squarefreeness passed n=2..48.

## originality

PASS

The stationary renewal PSD identity and equal-rate Erlang waiting times are established and credited; the assessed addition is a complete analytic all-finite-n crossing count, simple roots and phase localization, plus adjacent-pair identification ambiguity. Prior broad noise formula allows derived count but does not directly state it in inspected text.

## value

PASS

The exact number of sign-changing spectral bands is a robust natural feature of an equal-rate multi-stage renewal process and quantitatively restricts inferred hidden stage count; the full sharp all-n root classification is mathematically more than plotting finitely many examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
