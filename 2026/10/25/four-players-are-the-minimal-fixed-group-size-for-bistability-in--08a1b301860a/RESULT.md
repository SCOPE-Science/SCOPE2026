# Four players are the minimal fixed group size for bistability in a Fermi public-goods mean field

## Finding
For the fixed-size version of the Zhang–Tang public-goods death–birth Fermi mean field, in the genuine social-dilemma regime \(1<r<g\), every positive-temperature game with group size \(g=2\) or \(g=3\) possesses precisely one stationary cooperation fraction, globally attracting in \([0,1]\). The bound is sharp: at group size \(g=4\), a strictly admissible pair of multiplication factor and noise strength produces **exactly three distinct hyperbolic interior equilibria**, two attracting and one repelling. Thus four players is the minimal fixed group size allowing bistability in this model without any group-size variability.

An exact witness is \(g=4\), \(r=8/3\), and \(K=1/(3\log 2)\). This is a result about the deterministic infinite-population mean-field equation, not a claim about finite stochastic absorption or networked interactions.

## Assumptions and scope
Consider a well-mixed infinitely large population with current cooperator fraction \(x\in[0,1]\). Fix an integer group size \(g\ge2\), a benefit multiplication factor \(1<r<g\), and strictly positive Fermi temperature \(K>0\). Independently sampled groups contain \(n\in\{0,\ldots,g\}\) cooperators with binomial weight \(\binom gn x^n(1-x)^{g-n}\). The group total payoffs are
\[
P_c(g,n)=n(rn/g-1),\qquad P_d(g,n)=(g-n)rn/g.
\]
The cooperator reproduction probability is
\[
a_n=\frac{1}{1+\exp[-d_n/K]},\qquad d_n=P_c-P_d=n\bigl[(r/g)(2n-g)-1\bigr].
\]
Following the source's equation (5), after a positive time rescaling the mean-field flow is
\[
\dot x=H_g(x)=\sum_{n=0}^g\binom gn x^n(1-x)^{g-n}a_n-x.
\]
Finite positive temperature is essential: \(a_0=1/2\), \(0<a_g<1\), so \(H_g(0)=1/2>0\), \(H_g(1)=a_g-1<0\); hence the physical interval is forward invariant and every equilibrium lies in its interior.

## Proof
**Uniqueness and attraction at sizes two and three.** Using the Bernstein identity
\[
x=\sum_{n=0}^g\binom gn x^n(1-x)^{g-n}\frac ng,
\]
write \(H_g(x)=\sum_{n=0}^g\binom gn x^n(1-x)^{g-n}c_n\), where \(c_n=a_n-n/g\). For \(x\in(0,1)\) put \(z=x/(1-x)>0\). The stationary equation is equivalent to
\[
Q_g(z):=\sum_{n=0}^g\binom gn c_nz^n=0.
\]
For both sizes, \(c_0=1/2>0\) and \(c_g=a_g-1<0\). At \(g=2\), the one-cooperator payoff difference is \(d_1=-1\), so \(c_1=(1+e^{1/K})^{-1}-1/2<0\). Thus the nonzero coefficient sequence of \(Q_2\) has exactly one sign variation. At \(g=3\), \(d_2=2(r/3-1)<0\) because \(r<3\). Hence \(c_2=a_2-2/3<1/2-2/3<0\), while \(c_1\) may have either sign or vanish. Again the nonzero coefficients have exactly one sign variation. Descartes' rule bounds the number of positive zeros counted with multiplicity by one. Since \(H_g(0)>0>H_g(1)\), continuity supplies such a zero. It is simple and unique. The vector field is positive below it and negative above it, establishing global convergence, including boundary initial data.

**Sharp four-person witness.** Set \(g=4\), \(r=8/3\), \(K=1/(3\log2)\). Then \(d_n/K=n(4n-11)\log2\) and, in order \(n=0,1,2,3,4\),
\[
(a_0,a_1,a_2,a_3,a_4)=\left(\frac12,\frac1{129},\frac1{65},\frac89,\frac{1048576}{1048577}\right).
\]
Consequently
\[
H_4(x)=-\frac{105204829297}{52753908870}x^4+\frac{36826}{25155}x^3+\frac{8383}{2795}x^2-\frac{383}{129}x+\frac12.
\]
Exact rational evaluations give
\[
H_4(0)=\frac12>0,\quad H_4(1/4)=-\frac{178754083691}{4501666890240}<0,
\]
\[
H_4(9/10)=\frac{945172651927}{58615454300000}>0,\quad H_4(1)=-\frac1{1048577}<0.
\]
The intermediate value theorem therefore places one crossing in each disjoint interval \((0,1/4)\), \((1/4,9/10)\), and \((9/10,1)\). These roots are **the only** roots in \((0,1)\): three sign-changing roots already consume at least three degrees of the quartic; any extra interior root (of odd multiplicity) would make the total number of sign reversals between the endpoints even, contrary to the opposite endpoint signs; an extra tangency of even multiplicity would require at least five degrees. Each of the three roots is simple, since otherwise its odd multiplicity is at least three and the quartic would require at least five degrees. The alternating signs prove the first and third are asymptotically stable, and the middle root is unstable. Simplicity also gives open parameter robustness by continuity and the implicit-function theorem. This achieves bistability at four and, together with the smaller-size result, proves minimality.

## Verification
The accompanying standalone `verify.py` reconstructs the five rational Fermi probabilities directly from integer powers of two, the quartic coefficients from binomial expansion, all four exact sign certificates, and the Bernstein coefficient sign patterns. It uses Python's standard-library `fractions.Fraction` to eliminate floating-point ambiguity. The arbitrary-parameter \(g=2,3\) conclusion rests on the proof's universal inequalities and Descartes' rule, not finite sampling. The recorded roots near \(0.2219163855\), \(0.8466333490\), and \(0.9999982834\) are optional approximations only; all existence and stability conclusions follow from exact rational certificates.

## Relationship to prior work
Zhang and Tang (arXiv:2402.16317, first submitted 26 February 2024) introduce the same group payoffs, Fermi reproduction rule, and mean-field equation, study group sizes drawn from ranges, solve the size-range \(1\)–\(3\) equation, and report numerical bistability for groups drawn from \(1\)–\(5\). Those findings and the underlying model are not new here. The theorem isolates **degenerate fixed-size distributions**, proves a uniform *impossibility* result at fixed sizes two and three under the social-dilemma constraint, and gives an exact nonasymptotic size-four *possibility* certificate. Prior general Bernstein-polynomial analyses of nonlinear public goods, notably Archetti (2018), supply the general sign-variation methodology but do not in the inspected accessible material state this specific sharp Fermi fixed-group threshold. This is a claim about the specific Zhang–Tang update rule, not about all public-goods games; other nonlinear games can be bistable under different mechanisms.

## Limitations
Only the deterministic infinite-population homogeneous fixed-group mean field with finite positive Fermi noise and the stated payoff normalization is covered. Discrete stochastic birth–death chains at finite population sizes have absorption behavior not represented by the interior deterministic sinks. The proof does not rule out bistability at smaller sizes outside \(1<r<g\), for non-Fermi updates, or with time-varying group sizes. The originality assessment is bounded by the accessible literature inspected, not a mathematical proof of publication priority. Independent scientific validation has not been performed.

## References
1. H.-B. Zhang and D.-P. Tang, *Effects of group size and noise on cooperation in population evolution of dynamic groups*, arXiv:2402.16317 (first public version 26 February 2024), https://arxiv.org/abs/2402.16317. Primary model, equations (1)–(5) and results on dynamic group-size distributions.
2. M. Archetti, *How to Analyze Models of Nonlinear Public Goods*, Games **9** (2018), article 17, https://doi.org/10.3390/g9020017. General Bernstein-polynomial approach to nonlinear public-goods dynamics.
3. J. Peña, *Group-Size Diversity in Public Goods Games*, Evolution **66** (2012), 623–636, https://doi.org/10.1111/j.1558-5646.2011.01504.x. Earlier model of group-size diversity with a different evolutionary payoff function.
