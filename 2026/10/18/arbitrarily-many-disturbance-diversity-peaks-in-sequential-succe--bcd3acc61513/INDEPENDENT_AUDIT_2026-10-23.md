# Independent mathematical audit

## correctness

PASS

Homogeneous Poisson resets at rate c and independent exponential stage transitions with rates lambda_j give survival products y_k=prod(lambda_i/(lambda_i+c)) and stationary pi_j=y_j-y_(j+1). With R=10000 n^4 and decreasing geometric rates, at c=lambda_i two adjacent stage masses exceed 0.49 (Simpson >0.48 and Shannon >=Simpson), while at the intervening geometric means one stage has mass >=1-1/(100n) (Simpson<=0.01, Shannon<0.105). Analyticity and endpoint point-mass limits force >=n-1 distinct strict maxima of each diversity. For n=3 the exact Simpson derivative quartic has discriminant 4r²F(r), where degree-seven F has a unique positive zero in (12,13), established by sign-fixed Möbius transforms and Descartes after r=12. Quartic signs above threshold give three positive critical points and exactly two maxima; equality leaves one. Independent Sympy polynomial/discriminant check and small-n rational balance checks corroborated algebra, not infinite generality.

## originality

PASS

Johst–Huth 2005 already studies exactly stage succession under disturbance and demonstrates two peaks, so no originality is assigned to the ecological model or two-peak example. The explicit unbounded n−1 construction for both diversity measures and sharp if-and-only-if three-stage Gini–Simpson ratio r*>12 are not mathematically implied by the inspected two-peak examples or descriptions.

## value

PASS

An all-stage constructive lower bound on the number of strict diversity peaks disproves dimension-independent unimodality/bimodality for two standard indices in a natural succession model; the exact n=3 bifurcation gives a parameter frontier with independently useful interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
