# Independent mathematical audit

## correctness

PASS

On A=lambda I_2, both naive XTrace and XNysTrace basic estimators reduce to B_i=lambda rank(P_-i)+lambda||(I-P_-i)omega_i||^2; Nyström with Moore-Penrose pseudoinverse equals lambda times the range projector even for repeated sign columns. Independent sign probes have exactly two unoriented mutually orthogonal lines. For k>=3, all k lines equal (2 of 2^k line patterns) yields all B=lambda; exactly one minority (2k patterns) yields one B=3lambda and k-1 B=2lambda; all remaining patterns yield B=2lambda. Hence the exact joint law for (T_hat,e_hat), MSE lambda^2 2^(1-k)(1+1/k), proxy E e_hat²=lambda²2^(1-k)/k, basic-estimator pair correlation 1/2, calibration k+1 and strict one-stage false-stop formula for 0<delta<1/2. Independent exact Fraction enumeration for k=3..8 reproduces the three masses and statistics. A zero proxy is not a certificate; no extrapolation to normalized probes or multistage stopping.

## originality

PASS

PASS best-of-knowledge: Epperly-Tropp-Webber 2023/24 defines the naive algorithms, error proxy, adaptive stop, and general Proposition 3.1 relating pairwise correlations to expected posterior error. It does not calculate the discrete two-line full joint law or one-stage false-stop probability on lambda I_2. The known general covariance relation helps interpret the factor k+1 but does not itself determine correlation 1/2 or frequency of false stops. Other Hutch++ and jackknife methods have different dependencies.

## value

PASS

This is a deliberately minimal but natural supported input/discrete sampling scenario, exposing a zero posterior proxy with 50% trace error at explicit positive probability even though the mean estimate is unbiased. The exact full joint law calibrates a widely used heuristic estimator, identifies a concrete failure mode of an advertised adaptive test, and defines the precise boundary of that example. Not merely a code check or arbitrary matrix entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
