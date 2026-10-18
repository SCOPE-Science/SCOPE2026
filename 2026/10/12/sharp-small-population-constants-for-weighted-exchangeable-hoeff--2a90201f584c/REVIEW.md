# Independent mathematical audit

## correctness

PASS

Lee–Kim Proposition 2/Remark 1 reduce the global finite-exchangeable problem to the max over hypergeometric population count k, sample size m, and real tilt t; symmetry reduces k,m <= floor(N/2). For Bernoulli reductions use sharp Kearns–Saul constant, giving 1/log(2) at N=3 and 1/[2log(3/2)] at N=5. For N=4, the k=m=2 hypergeometric MGF (2+cosh t)/3 <= exp(t^2/6) by nonnegative series coefficients, while an m=1 balanced Bernoulli attains 4/3 in the variance limit. For N=5 k=m=2, differentiation gives variance 6u(u²+2u+3)/(u²+6u+3)² maximized at sqrt(3) with bound 5(sqrt(3)-1)/3 < 1/[2log(3/2)]; remaining small pairs are dominated. For N=6, explicit rational nonnegative tilted-variance certificates for (k,m)=(2,2),(2,3),(3,3) and Bernoulli k=1 prove <=6/5, attained by k=3,m=1 as t tends to zero. The entire range of real tilts follows by double integration of variance; no finite numerical search is used as infinite proof. Independent symbolic simplification checked all three N6 identities and the N5 derivative identity from the source package.

## originality

PASS

PASS: the leading Lee–Kim paper gives the exact variational hypergeometric optimization and general sufficient Γ_N and lower bounds, but not evaluated sharp C_N at all four sizes. Bernoulli Kearns–Saul settles m=1 pieces, not k=m=2 domination; new small-population evaluations close the remaining analytic cases.

## value

PASS

A natural exact optimal-constant sequence in finite-sample concentration, not an arbitrary four-number recomputation: variational definition alone does not decide finite N, and these first consecutive nontrivial sizes show alternating nonzero-tilt versus variance-limit extremality. Sharp constants can be used without numerical optimization for small finite randomizations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
