# Independent mathematical audit

## correctness

PASS

The claim is for total vertex path length P_n on uniform ordered rooted trees with n edges. In the Dyck contour each edge to depth d contributes 2d-1 to all-step area, so A_n=2P_n-n. Returns count the primitive factors. B=zC marks one primitive factor and Lagrange inversion gives c_{m,r}=[z^m]B^r. Additivity and the lift of a primitive interior give F=W/(1-B)^2 and W=zF+2zB'-B, hence W=z/(1-4z). Thus Q_r=rWB^(r-1)=(z/sqrt(1-4z))(B^r)' gives the stated convolution formula. For r>=2 the ratio c_{m,r+1}/c_{m,r} increases strictly with m, so normalizing at m=n lowers the intermediate positive terms when r increases, and the positive m=r term is lost even if there are no intermediate terms. For r=1, c_{m,1}=c_{m,2} for m>=2, and the extra m=1 term gives the area gap n, i.e. the path-length gap n/2. Full support and the independent-copy identity then give negative covariance with every nonconstant nondecreasing test. Setting S=sqrt(1-4z), Q_r has leading terms r 2^(-r-1)[S^(-2)-(r-1)S^(-1)], and B^r has leading nonpolynomial term -r 2^(-r) S; coefficient transfer gives the fixed-r expansion. For the sums of Q_r and rQ_r the two leading singular terms are respectively S^(-2)-2S^(-1) and 3S^(-2)-10S^(-1). With E[R_n]=3n/(n+2), the n^(3/2) terms cancel and the area covariance is -4n+O(sqrt n), hence the path-length covariance is -2n+O(sqrt n). A separate enumeration through n=8 corroborated counts, area sums, strictness and the first gap: enumerate length-2n balanced parentheses with no negative prefix, sum heights before steps, and group by positive-time returns. It is not proof of the unbounded or asymptotic conclusions. The uploaded verifier was inspected, not executed. No inference of conditional stochastic dominance or uniformity in a growing r is made.

## originality

PASS

The supported distinct result is the strict all-degree regression (and consequently the sign for every nonconstant increasing degree test), with its fixed-degree correction. Standard Catalan counts and primitive decompositions are not new. Later indexed records cover equivalent conditional moment formulas, the first-step gap and stronger covariance formulas, but the inspected statements do not establish all-degree strictness. No historical priority is inferred merely from catalogue dates.

## value

PASS

Root branching is a natural local statistic and total depth a natural global one. The exact regression shows, for every size, that their negative association is not just an average covariance or a comparison of extremes. It gives the sign for any nonconstant increasing root test, a sharp first-step gap and a degree-dependent next-order shift even though the leading path-length scale is unchanged. This is a useful structural fact without requiring dominance of full conditional distributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
