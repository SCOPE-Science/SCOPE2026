# Independent mathematical audit

## correctness

PASS

Symbolic independent differentiation confirms F''>0 and F''<0 for all alpha,t>0: F'' = alpha L^(alpha-2)(alpha-1-L)/(t(1+e^alpha t)^2)<0 because L>=alpha. Scaling F(st)/F(t)<=s(1+log(1/s)/alpha)^alpha gives a uniform two-sum quasi-triangle bound, and coordinatewise limits with Fatou give completeness. Disjoint basis vectors have ||e_i||=1/a_alpha and ||sum_{i=1}^n e_i||=1/F^{-1}(1/n); asymptotic inversion yields lower coefficient a_alpha. For arbitrary normalized summands the weighted modal bound is (a_alpha/C) sum_i w_i(r_alpha+log C+log(1/w_i))^alpha, and self-information W=-log w_i obeys P(W>log n+u)<=e^-u for every positive weight vector; stochastic domination by log n+Exp(1) gives the uniform matching upper bound with C=(1+eps)a_alpha(log n)^alpha. This proves limit for all fixed alpha; n-independent norm equivalence is contradicted. Independent symbolic derivative and 16 disjoint-asymptotic numeric checks corroborate.

## originality

PASS

Theorem 4.2 of Kamińska–Żyluk (2019), full arXiv PDF page 19 visually inspected, characterizes quasi-Orlicz normability and p-upper estimates in terms of growth conditions; it does not give the n-dependent sharp amplification coefficient for this specific concave logarithmic modular. Mayoral (2025) treats r-convexification nonnormability, a qualitative weaker conclusion. The Kameník (September 2026) sequence-space preprint abstract concerns fundamental functions and coincidence of Orlicz/Lorentz–Zygmund spaces, not an explicit n-summand leading coefficient; full text inaccessible via arXiv/Oxford, so its coverage remains a specific risk. Distinguish known nonnormability from new sharp rate and normalization.

## value

PASS

The n-summand amplification constant is a natural quantitative finite-dimensional obstruction to normability. Exact leading growth (log n)^alpha and the explicit normalization a_alpha distinguish logarithmic near-l1 gauges beyond the familiar binary quasi-triangle or qualitative p-normability classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
