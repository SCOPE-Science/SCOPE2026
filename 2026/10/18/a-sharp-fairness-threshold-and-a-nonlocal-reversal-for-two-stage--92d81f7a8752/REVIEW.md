# Independent mathematical audit

## correctness

PASS

Independently checked stationary renewal reward, the Perron branch and the strict comparison. Integrating the Erlang-2 survival function and multiplying by the rate gives (1+y)exp(-2y), with continuous no-booster limit 1. With t=alpha/2, the larger eigenvalue is (1-t)m+sqrt(t²m²+(1-2t)d²), where m and d are the half-sum and half-difference of the positive susceptibilities. The discriminant has the equivalent strictly positive form (1-t)²d²+t²s1s2. The symmetry makes the first derivative zero; the second derivative from the expansion is c²[F''+2(1-alpha)(F')²/(alpha F)] at c, with sign given by 1+4c+4c²-alpha(1+2c+2c²). At alpha=3/2, c=3/8 it is 3exp(-3/4)/1408, strictly positive. For a=exp(-3/4) the endpoint characteristic polynomial has negative constant term and thus precisely one positive root; substituting the positive fair value (11/8)a gives a(130a-44-77a²)/128. The degree-five alternating sum is 19339/40960>47/100 and the exponential upper bound gives a<1/2. The bracket increases on that interval and is 907/10000 at 47/100. Thus the endpoint's positive root is strictly smaller. For exponential clocks, s1s2=exp(-2c) is constant and the Perron branch is strictly increasing with the half-sum for t<1; that sum strictly increases in |x|. At t=1 the radius is sqrt(s1s2), constant for exponential boosters and strictly decreasing in |x| for Erlang-2. This verifies the exact model-specific statements without running the frozen script or treating its finite grid as a proof. Neither the degenerate curvature boundary nor global optimality of the concentrated endpoint is asserted.

## originality

PASS

The fixed-dose-rate spectral optimization problem and known concentration effects are not new. Credit only the stated Erlang-2/step-immunity exact threshold and the strict local-minimum/better-endpoint witness, with the memoryless calculation as a control. The strongest located material uses different coverage coordinates or different booster and waning laws; statement-level comparisons did not establish equivalent or stronger coverage of that remaining claim.

## value

PASS

The exact threshold separates local behavior across the natural mixing parameter in an existing constrained allocation problem. The witness shows that even a strict local optimum at the symmetric allocation does not justify a global fairness conclusion under the same budget; the exponential control isolates a substantive effect of the renewal law. This is a usable caution for spectral-factor optimization in the stipulated model, not a real-world vaccination recommendation or a general global solution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
