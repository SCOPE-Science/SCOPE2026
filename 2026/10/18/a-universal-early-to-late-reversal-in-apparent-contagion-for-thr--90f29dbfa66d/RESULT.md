# A universal early-to-late reversal in apparent contagion for three-person SIR groups

## Finding

Consider isolated three-person groups, initially with two susceptible individuals and one infectious individual. A group has a fixed per-pair transmission intensity \(\lambda\), drawn independently across groups from any non-point-mass probability distribution \(\mu\) supported on a compact interval \([a,b]\subset(0,\infty)\). Every infectious individual recovers permanently at rate one. A susceptible individual becomes infected at rate \(\lambda i\) when exactly \(i\) group members are infectious. All transition clocks are independent conditional on \(\lambda\).

At time \(t>0\), let \(L_i(t)\) denote the effective **per susceptible–infectious pair** transmission intensity among groups with exactly \(i\) infectious people, pooling over unobserved removed counts and weighting each group by its number of susceptible–infectious pairs. The quantities \(L_1(t)\) and \(L_2(t)\) are well-defined and finite for every \(t>0\). There are constants \(\varepsilon>0\) and \(T<\infty\), depending on \(\mu\), such that

\[
L_2(t)>L_1(t)\qquad(0<t<\varepsilon),
\quad
L_2(t)<L_1(t)\qquad(t>T).
\]

At least one equality time exists between these regimes. Thus every nondegenerate compactly supported distribution of positive *fixed* individual-group transmission rates exhibits an early-to-late reversal of the inferred dependence on infectious count. The microscopic infection hazard remains exactly linear in infectious count at every time. The theorem asserts neither a unique crossing nor appreciable late-time sample sizes.

## Assumptions and scope

Let \(S,I,R\) be susceptible, infectious, and removed group counts, always summing to three. Conditional on a group's \(\lambda\), infection jumps \((S,I,R)\to(S-1,I+1,R)\) at total rate \(\lambda SI\), and removal jumps \((S,I,R)\to(S,I-1,R+1)\) at total rate \(I\). Start all groups at \((2,1,0)\). Groups are isolated, their rates do not change, and \(\lambda\sim\mu\) has support in \([a,b]\) with \(0<a\le b<\infty\), not concentrated at a single point.

Define \(q_{s,i}(\lambda,t)=\Pr(S(t)=s,I(t)=i\mid\lambda)\). For \(i\in\{1,2\}\), define

\[
L_i(t)=\frac{\int\lambda\sum_{s=1}^{3-i}si\,q_{s,i}(\lambda,t)\,\mu(d\lambda)}{\int\sum_{s=1}^{3-i}si\,q_{s,i}(\lambda,t)\,\mu(d\lambda)}.
\]

This is a *pair-weighted* conditional mean, not the posterior mean among groups counted without susceptible-pair weighting. In particular, recovery does not transform a group into a new group of size two for purposes of the original three-person label. Only the at-risk pairs contribute to the estimand.

## Proof

Write \(A=q_{2,1}\), \(B=q_{1,2}\), and \(D=q_{1,1}\), conditional on \(\lambda\). Their exact forward equations are

\[
\dot A=-(1+2\lambda)A,\quad
\dot B=2\lambda A-(2+2\lambda)B,\quad
\dot D=2B-(1+\lambda)D,
\]

with \(A(0)=1\), \(B(0)=D(0)=0\). The term \(2B\) in \(\dot D\) is the recovery of one of the two infectious individuals. Direct integration gives

\[
A=e^{-(1+2\lambda)t},\qquad
B=2\lambda e^{-(1+2\lambda)t}(1-e^{-t}),
\]

and

\[
D=\frac{4e^{-(1+\lambda)t}}{1+\lambda}
\left(1-(1+\lambda)e^{-\lambda t}+\lambda e^{-(1+\lambda)t}\right).
\]

The total at-risk pair mass in groups with \(I=1\) is \(W_1=2A+D\); for \(I=2\), it is \(W_2=2B\). Since the factor two cancels in \(L_2\), put \(h=B/(2A+D)\). The explicit solution reduces this ratio to

\[
h(\lambda,t)=\frac{\lambda(1-e^{-t})}{1+\frac{2}{1+\lambda}\left[e^{\lambda t}-1-\lambda(1-e^{-t})\right]}.
\]

Every denominator is strictly positive. Introduce the probability measure

\[
Q_t(d\lambda)=\frac{W_1(\lambda,t)\mu(d\lambda)}{\int W_1(u,t)\mu(du)}.
\]

Both rate observables are strictly well-defined for each finite positive time because \(W_1,W_2>0\) for every \(\lambda>0\). By change of measure,

\[
L_2(t)-L_1(t)=\frac{\operatorname{Cov}_{Q_t}(\lambda,h(\lambda,t))}{\mathbb E_{Q_t}h(\lambda,t)}.
\]

For \(t\downarrow0\), uniformly in \(\lambda\in[a,b]\), with the expansion differentiated uniformly in \(\lambda\),

\[
h(\lambda,t)=\lambda t+O(t^2),\qquad
\partial_\lambda h(\lambda,t)=t+O(t^2).
\]

Thus \(h\) is strictly increasing in \(\lambda\) on the entire support for all sufficiently small positive \(t\). For \(t\to\infty\), the same uniform compact-parameter calculus gives

\[
h(\lambda,t)=\frac{\lambda(1+\lambda)}2e^{-\lambda t}
\left(1+O(e^{-at})\right),
\qquad
\partial_\lambda\log h(\lambda,t)
=\frac1\lambda+\frac1{1+\lambda}-t+O(te^{-at}).
\]

The last derivative is negative uniformly on \([a,b]\) for sufficiently large \(t\), so \(h\) is then strictly decreasing.

For any non-point-mass probability measure \(Q\), the identity

\[
2\operatorname{Cov}_{Q}(\lambda,h(\lambda))=
\iint(\lambda-u)(h(\lambda)-h(u))\,Q(d\lambda)Q(du)
\]

makes the covariance strictly positive for strictly increasing \(h\) and strictly negative for strictly decreasing \(h\). Here \(Q_t\) and \(\mu\) have identical support, because \(W_1>0\). Applying the identity yields the two strict inequalities. All integrals are continuous in \(t>0\), so the difference also vanishes at least once at an intermediate time. This proves the theorem.

## Verification

Run `python3 VERIFY.py` with Python 3 and its standard library only. Its independent seven-state continuous-time Markov transition calculation is evaluated by stochastic uniformization, rather than by solving the displayed three-variable equations. The script compares all three formulas against that independent calculation for forty-two positive rate/time pairs (126 comparisons), checks signs and identities (91 further checks), and reproduces the two-point example. It reports 217 passed checks. Its finite computations are supplementary and do not establish the infinite-distribution theorem; the uniform analytic argument above does.

For \(\mu=\tfrac12\delta_1+\tfrac12\delta_2\), the direct formulas yield

\[
(L_1(0.1),L_2(0.1))\approx(1.45277818,1.62084755),
\]

whereas

\[
(L_1(2),L_2(2))\approx(1.09080988,1.03533684).
\]

## Relationship to prior work

St-Onge, Hébert-Dufresne, and Allard, *Nonlinear bias toward complex contagion in uncertain transmission settings* (arXiv:2302.13358, first posted 26 February 2023), establish a heterogeneous-transmission mechanism for early apparent superlinearity. Their Section 2.2 considers conditional rates at fixed group-size/count and numerically documents the later failure of early-time approximations; their Section 4.5 treats SIR dynamics via an effective surviving-group size. The present result concerns a separate, explicitly at-risk-pair-weighted observable with fixed original group size three, demonstrates a strict **opposite ordering** at late times, and proves it for every nondegenerate compactly supported positive rate law. Neither the source's early-time moment ratios nor its discussion that an approximation eventually fails logically entails a late-time strict sign reversal for this distinct estimand. The published discussion nevertheless anticipates the broader scientific warning; the qualitative caution itself is not claimed as new.

Related models of heterogeneous dose and context-dependent behavior involve different exposure/interaction mechanisms; they do not supply an examined exact three-person SIR conditional-rate reversal. Standard Markov-chain integration and covariance sign identities are classical tools, not claimed as new. A theorem implicit in an unexamined general result or supplementary calculation remains a publication-priority risk.

## Limitations

This is an exact result for independent closed groups, fixed pairwise linear infection hazards, exponential unit-rate recoveries, a shared initial state, and compact positive transmission heterogeneity. It does not establish the corresponding sign reversal for SIS dynamics, groups sharing members, arbitrary initial infections, time-varying rates, group-unweighted conditional means, or general rate laws with zero or unbounded support. Late-time conditioning is on rare surviving susceptible–infectious pairs; finite observed samples can be insufficient to estimate the limiting conditional rates reliably. Nothing here establishes that observational Bayesian posterior estimates in a finite dataset converge at a stated speed. The crossing time need not be unique. The paper's inaccessible ancillary supplement was not fully reviewed for priority.

## References

1. G. St-Onge, L. Hébert-Dufresne, and A. Allard, *Nonlinear bias toward complex contagion in uncertain transmission settings*, arXiv:2302.13358, first public version 26 February 2023, https://arxiv.org/abs/2302.13358, full-text https://arxiv.org/html/2302.13358v2. Sections 2.2, 3, and 4.5 are particularly relevant.
2. G. St-Onge et al., *Universal nonlinear infection kernel from heterogeneous exposure on higher-order networks*, arXiv:2101.07229, https://arxiv.org/abs/2101.07229. Different random-exposure mechanism.
