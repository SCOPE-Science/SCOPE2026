# Sharp \(L^p\) commutator norms for two balanced binary conditional expectations

## Finding
Let \((\Omega,\mathcal F,\mu)\) be a probability space and let \(A,B\) be measurable events of probability exactly \(1/2\). Define the two (contractive) conditional expectations
\[P f=\mathbb E(f\mid\sigma(A)),\qquad Qf=\mathbb E(f\mid\sigma(B)),\qquad C=PQ-QP.\]
Write \(X=2\mathbf1_A-1\), \(Y=2\mathbf1_B-1\), \(c=\mathbb E(XY)\), and \(s=|c|\). For \(0<s<1\), let \(a=(1+s)/2\), \(b=(1-s)/2\), and \(\theta_p=\min\{1/p,1-1/p\}\), with \(1/\infty=0\). Then, **simultaneously for every real exponent \(1\le p\le\infty\)**, on real or complex \(L^p\),
\[\boxed{\ \|C\|_{p\to p}=2s\,a^{1-\theta_p}b^{\theta_p}.\ }\]
For each \(1<p<\infty\), the maximal possible norm over all balanced pairs of events is uniquely reached at the correlation magnitude
\[\boxed{\ s_p=\frac{1-2\theta_p+\sqrt{(1-2\theta_p)^2+8}}4\in(0,1).\ }\]
For the endpoint exponents \(p=1\) and \(p=\infty\), the sharp supremum among noncommuting balanced pairs is \(2\), but no noncommuting pair attains it. At \(c=0\) and \(|c|=1\), one has \(C=0\).

As \(s\uparrow1\), for fixed \(1<p<\infty\),
\[\boxed{\ \|C\|_{p\to p}\sim 2^{1-\theta_p}(1-s)^{\theta_p},\qquad \|C\|_{1\to1}=\|C\|_{\infty\to\infty}=s(1+s)\longrightarrow2.\ }\]
Hence almost identical balanced information partitions have commutators tending to zero on every interior \(L^p\), while their endpoint commutator norms approach the universal bound \(2\). At \(p=2\), \(\|C\|_2=s\sqrt{1-s^2}\), and its maximum is \(1/2\) at \(s=1/\sqrt2\).

## Assumptions and scope
No atomlessness assumption is needed. The four intersections \(A\cap B\), \(A^c\cap B^c\), \(A\cap B^c\), and \(A^c\cap B\) have probabilities \(a/2,a/2,b/2,b/2\) (after replacing \(Y\) by \(-Y\) when \(c<0\)); they are all positive for \(0<s<1\). The norm is on the full \(L^p(\mu)\), not just the four-cell subspace; the operator factors through the conditional expectation onto those four cells. Complex coefficients are permitted. The terminal cases \(s=0,1\) have the separate values stated above and must not be filled in by endpoint limits.

## Proof
**Rank-two reduction.** Since \(X,Y\) are mean-zero unit vectors in \(L^2\),
\[Pf=\mathbb Ef+X\,\mathbb E(Xf),\qquad Qf=\mathbb Ef+Y\,\mathbb E(Yf),\]
and direct composition gives
\[Cf=c\bigl(X\mathbb E(Yf)-Y\mathbb E(Xf)\bigr).\]
Replacing \(Y\) by \(\operatorname{sgn}(c)Y\) does not change the conditioning sigma-algebra; therefore assume \(c=s>0\). All cell probabilities are determined by \(\mathbb EX=\mathbb EY=0\) and \(\mathbb EXY=s\), giving aligned mass \(a\) and misaligned mass \(b\).

**Exact norm reduction.** Replace an arbitrary \(f\) by its average on the four cells. This leaves \(Cf\) unchanged and cannot increase \(\|f\|_p\) by Jensen's inequality (also valid for \(p=\infty\)). Denote its four values, in order \((X,Y)=(+,+),(-,-),(+,-),(-,+)\), by \(f_1,f_2,f_3,f_4\), and set \(U=(f_1-f_2)/2\), \(V=(f_3-f_4)/2\). The two even parts of \(f\) on these paired cells have no effect on \(Cf\). Conversely, by pairwise convexity, replacing the values by \((U,-U,V,-V)\) cannot increase \(\|f\|_p\). Thus optimization loses nothing by restricting to this antisymmetric two-dimensional subspace.

The input and output profiles are now exact:
\[\|f\|_p^p=a|U|^p+b|V|^p,\qquad\|Cf\|_p^p=a|2sbV|^p+b|2saU|^p\quad (p<\infty),\]
with the corresponding maximum formulas at \(p=\infty\). After multiplying \(U\) and \(V\) by \(a^{1/p}\) and \(b^{1/p}\), this becomes a two-dimensional off-diagonal linear map whose operator norm on \(\ell_p^2\) is the maximum of its two coefficient magnitudes. Consequently
\[\|C\|_p=2s\max\{a^{1/p}b^{1-1/p},\,a^{1-1/p}b^{1/p}\}=2s\,a^{1-\theta_p}b^{\theta_p}.\]
Each coefficient is attained by choosing exactly one of \(U,V\) nonzero. Therefore the displayed bound is sharp for real and complex inputs, at both endpoints as well.

**Optimization and sharp boundary.** For \(1<p<\infty\), \(\theta_p\in(0,1/2]\), and differentiating \(\log[2s((1+s)/2)^{1-\theta_p}((1-s)/2)^{\theta_p}]\) shows that its derivative has the sign of
\[1+(1-2\theta_p)s-2s^2.\]
This quadratic is positive at \(s=0\), negative at \(s=1\), and has exactly one positive root, precisely \(s_p\). The norm vanishes at both ends, so that root is the unique global optimizer. For \(\theta_p=0\), the formula is \(s(1+s)\), strictly increasing on \((0,1)\) toward the unattained bound \(2\). Expanding \(a\to1\) and \(b\sim(1-s)/2\) gives the claimed endpoint/interior asymptotics. At \(s=0\), the two expectations commute; at \(s=1\), the two event sigma-algebras are identical, so \(C=0\) in both cases.

## Verification
The accompanying `checker.py` uses exact rational four-cell matrices of the two conditional expectations to check the rank-two commutator identity, weighted \(L^1\)/\(L^\infty\) norms, and the exact Hilbert--Schmidt trace. It tests sharp antisymmetric sector witnesses and deterministic finite-value \(L^p\) checks at six exponents, as well as the optimizer's quadratic equation and strict local maximality. Execute `python3 checker.py`; the expected line is `PASS: 2612 exact rational and finite Lp consistency assertions`. Infinite-exponent and global claims are justified by the preceding argument, not by sampled tests.

## Relationship to prior work
Zaharopol (1990) establishes strong convergence of powers of products of conditional expectations in interior \(L^p\), without computing commutator norms. Herron (2011) gives operator-theoretic formulas for a weighted conditional expectation operator, a different single-expectation construction. Estaremi (2013) treats spectral properties of weighted conditional expectation type operators, not the two-event commutator norm. A published analysis entitled *Exact mixing norms and time-reversal obstruction for binary conditional-expectation chains* treats centered products and their powers and provides the rank-one product representations; these do not give sharp norms of their difference. A separate published *Sharp numerical radius of a three-point conditional-expectation commutator* studies the spatial numerical radius for a fixed real three-point configuration, not its full \(L^p\) operator norm. The present result's contribution is the exact all-exponent difference norm, its sharp correlation optimizer, and the endpoint-discontinuity law. Background rank-two projection identities are standard and are not claimed novel.

## Limitations
The formula requires **balanced binary** events. It does not classify unequal marginal probabilities, partitions with more than two cells, nor general conditional-expectation commutators. The endpoint discontinuity is for the family of probability laws with tiny but positive crossing-cell masses; it does not contradict Hilbert-space convergence. Historical literature on alternating projections is extensive, so a differently presented equivalent all-\(p\) finite-table identity remains a priority risk. Independent audit has not been performed.

## References
1. R. Zaharopol, *On Products of Conditional Expectation Operators*, Canadian Mathematical Bulletin **33** (1990), 257--260, DOI `10.4153/CMB-1990-041-3` (full text inspected).
2. J. D. Herron, *Weighted Conditional Expectation Operators*, Operators and Matrices **5** (2011), 107--118, DOI `10.7153/oam-05-07` (full text inspected).
3. Y. Estaremi, *Some classes of weighted conditional type operators and their spectra*, arXiv:1302.2708, first publicly posted 2013-02-12 (abstract examined).
4. *Exact mixing norms and time-reversal obstruction for binary conditional-expectation chains*, published mathematical note (full result inspected).
5. *Sharp numerical radius of a three-point conditional-expectation commutator*, published mathematical note (full result inspected).
