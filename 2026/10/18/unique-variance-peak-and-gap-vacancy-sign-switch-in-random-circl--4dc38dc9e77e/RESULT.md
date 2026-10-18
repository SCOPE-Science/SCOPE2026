# Unique variance peak and gap–vacancy sign switch in random circle covering

## Finding

Let \(n\ge 2\) independent uniform points lie on a circle of circumference one. From every point place a clockwise arc of common length \(s\in(0,1)\). Denote the number of uncovered gaps by \(B_n(s)\), and the total uncovered length by \(U_n(s)\). Set \(a=1-s\) and \(b=(1-2s)_+=\max\{1-2s,0\}\). Then

\[
\operatorname{Var}(U_n(s))=
\frac{2a^{n+1}+(n-1)b^{n+1}}{n+1}-a^{2n},
\]
\[
\operatorname{Cov}(B_n(s),U_n(s))=
 a^n-na^{2n-1}+(n-1)b^n
 =-\tfrac12\frac{d}{ds}\operatorname{Var}(U_n(s)).
\]

**Unique sign-switch/variance-peak theorem.** For every integer \(n\ge2\) there is exactly one \(s_n\in(0,1)\) such that \(\operatorname{Cov}(B_n(s_n),U_n(s_n))=0\). The covariance is strictly negative when \(0<s<s_n\) and strictly positive when \(s_n<s<1\). Equivalently, \(s_n\) is the unique global maximizer of uncovered-length variance. Specifically, \(s_2=1/2\), while \(0<s_n<1/2\) for \(n\ge3\). If \(c_*\) is the unique positive root of \(e^c=1+c+c^2\), then

\[
 n s_n=c_*-\frac{c_*(2c_*-1)}{2n}+O(n^{-2}),
 \qquad c_*=1.79328213290076\ldots .
\]

This theorem concerns the **uncovered-gap count**, which is zero on full coverage. It does not redefine the number of connected components of a fully covered circle.

## Assumptions and scope

The sample consists of exactly \(n\ge2\) independent points, each uniform in circular arclength. The arcs have deterministic equal length \(s\in(0,1)\), measured in units of circumference, with clockwise orientation. Overlap is unrestricted. Let \(S_1,\ldots,S_n\) be the cyclic spacings in order; their joint distribution is uniform Dirichlet on the simplex \(S_i\ge0\), \(\sum_i S_i=1\). Then, almost surely,

\[
 B_n(s)=\sum_{i=1}^n\mathbf1_{\{S_i>s\}},
 \qquad U_n(s)=\sum_{i=1}^n(S_i-s)_+.
\]

The theorem covers all \(n\ge2\) and all \(0<s<1\), including the transition at \(s=1/2\); it does not concern random arc lengths, nonuniform placement or intervals with boundary effects. The limit and expansion are for \(n\to\infty\) with the maximizing length \(s_n\).

## Proof

**1. Exact gap moments.** By uniform-simplex volume ratios, for \(t\in[0,1]\),

\[
 \Pr(S_1>t)=(1-t)^{n-1},\qquad
 \Pr(S_1>t,S_2>u)=(1-t-u)_+^{n-1}.
\]

Tail integration gives, with \(X_i=(S_i-s)_+\),

\[
\mathbb E X_1=\frac{a^n}{n},\qquad
\mathbb E X_1^2=\frac{2a^{n+1}}{n(n+1)},\qquad
\mathbb E(X_1X_2)=\frac{b^{n+1}}{n(n+1)}.
\]

The last identity follows by integrating the displayed joint survival function over \(t,u>s\). Consequently \(\mathbb E U_n=a^n\) and

\[
\mathbb E U_n^2=\frac{2a^{n+1}+(n-1)b^{n+1}}{n+1},
\]

which proves the variance formula. Also

\[
\mathbb E B_n=na^{n-1},\quad
\mathbb E[\mathbf1_{\{S_1>s\}}X_2]=\frac{b^n}{n},\quad
\mathbb E[B_n U_n]=a^n+(n-1)b^n.
\]

Subtracting \(\mathbb E B_n\,\mathbb E U_n\) gives the displayed covariance. Since each sample path \(U_n(s)\) is Lipschitz and has derivative \(-B_n(s)\) except at finitely many spacings, differentiation under expectation (the variables and derivatives are bounded) yields \(\frac{d}{ds}\operatorname{Var}(U_n(s))=-2\operatorname{Cov}(B_n(s),U_n(s))\). The exact algebraic variance expression shows differentiability also at \(s=1/2\).

**2. A single finite-sample sign switch.** For \(0<s<1/2\), factor the covariance as \(a^n[1-F_n(s)]\), where

\[
F_n(s)=na^{n-1}-(n-1)(b/a)^n,
\qquad R_n(s)=\frac{b^{n-1}}{a^{2n-1}},
\]
\[
 F_n'(s)=n(n-1)a^{n-2}[R_n(s)-1],
 \qquad \frac{d}{ds}\log R_n(s)=\frac{1-2ns}{(1-s)(1-2s)}.
\]

Here \(R_n(0)=1\), \(R_n(s)>1\) for sufficiently small positive \(s\), and \(R_n(s)\to0\) as \(s\uparrow1/2\). The logarithmic derivative changes sign exactly once, from positive to negative, at \(s=1/(2n)\). Therefore \(R_n=1\) once more, after \(1/(2n)\); thus \(F_n\) increases strictly from \(F_n(0)=1\) to a value exceeding one and then decreases strictly to \(F_n(1/2)=n/2^{n-1}\). For \(n\ge3\), this last value is strictly smaller than one, so \(F_n=1\) exactly once in \((0,1/2)\), with the required signs. For \(n=2\), the last value equals one, and the only zero in \((0,1)\) is \(1/2\).

For \(s\ge1/2\), \(b=0\) and the covariance equals \(a^n[1-na^{n-1}]\), which is strictly positive for \(s>1/2\), and also at \(s=1/2\) when \(n\ge3\). Thus there are no further zeros, and the derivative identity makes \(s_n\) the unique variance maximum.

**3. Density limit and correction.** Fix \(c>0\) and put \(s=c/n\). Elementary binomial/exponential expansions, uniform for \(c\) in compact positive intervals, give

\[
 \operatorname{Cov}(B_n(c/n),U_n(c/n))=
 h(c)+\frac{j(c)}n+O_c(n^{-2}),
\]
\[
 h(c)=e^{-c}-(1+c+c^2)e^{-2c},
\qquad j(c)=-\tfrac12c^2e^{-c}+(c^2-c^3+\tfrac32c^4)e^{-2c}.
\]

For positive \(c\), the equation \(h(c)=0\) is equivalent to

\[
 \sum_{k=3}^\infty\frac{c^{k-2}}{k!}=\frac12.
\]

The left side is strictly increasing from zero to infinity, hence has exactly one positive root \(c_*\). The finite-sample single-crossing property and the signs of \(h\) on either side imply \(ns_n\to c_*\). At the root, \(h'(c_*)=e^{-2c_*}c_*(c_*-1)>0\), and

\[
 j(c_*)=\tfrac12 e^{-2c_*}c_*^2(c_*-1)(2c_*-1).
\]

Substituting \(ns_n=c_*+d/n+O(n^{-2})\) into the uniform expansion and solving the nonzero linear term yields \(d=-j(c_*)/h'(c_*)=-c_*(2c_*-1)/2\). Standard smooth implicit-root Taylor estimates justify the stated remainder.

## Verification

The standalone script `circle_coverage_verification.py` carries out independent deterministic simplex-grid approximations for \(n=2,3,4\), exact one-dimensional rational integration for \(n=2\), exact rational variance-derivative identities for \(2\le n\le7\), and numerical finite-sample root checks through \(n=500\). It also compares the limiting root and its first finite-size correction. Run `python circle_coverage_verification.py` using Python 3 (standard library only). A simplex lattice is only a finite numerical check, not a proof of any continuum/infinite assertion. The proof above is analytic.

## Relationship to prior work

Random circular spacings, the number of uncovered gaps, and the total vacant measure have classical distributions. Huillet's *Random Covering of the Circle: the Size of the Connected Components* (2003), Sections 2–3 and Propositions 4–5, gives the gap-count law and an exact marginal distribution for the vacant length, along with limiting regimes. Thus the exact variance and its derivative can in principle be recovered from earlier marginal-distribution results; **neither formula alone is asserted as a discovery of an unknown marginal law**. Holst and Hüsler (1984) study joint limiting laws for gap count and vacancy. The claim made here is the *finite-\(n\) uniqueness* of the variance peak and the associated strict two-sided sign classification, together with the sharp limiting maximizing density and first correction. These are not stated in the inspected full text of Huillet (2003); the 1984 full text was not accessible for an exhaustive comparison. A general variance-of-coverage treatment by Pitts (1981) and related variability-ordering work by Huffer (1984) are further overlap risks, with accessible metadata/abstracts but not complete text.

## Limitations

No statement of novelty follows solely from an unsuccessful database query. The 1984 Holst–Hüsler paper and the 1984 Huffer technical report were not fully inspected, so a prior equivalent maximizer theorem remains possible. The theorem proves covariance signs and a unique variance maximizer only in the stated equal-arc model; it does not assert stochastic dominance, independence at the covariance zero, or that the number of covered components equals the gap count under complete coverage. The numerical checks are supportive and do not replace the proof. The work has not undergone independent audit.

## References

1. T. Huillet, *Random covering of the circle: the size of the connected components*, Advances in Applied Probability **35** (2003), 563–582, DOI: `10.1239/aap/1059486818`. Full text inspected at `https://www.researchgate.net/publication/38349613_Random_covering_of_the_circle_the_size_of_the_connected_components`; MSC2020 primary category 60D05 is confirmed by the article's bibliographic record.
2. T. Huillet, *Random covering of the circle: the configuration-space of the free deposition process*, Journal of Physics A **36** (2003), 12143–12155, DOI: `10.1088/0305-4470/36/49/002`; dated publication 2003-11-25. Abstract and bibliographic material inspected.
3. L. Holst and J. Hüsler, *On the random coverage of the circle*, Journal of Applied Probability **21** (1984), 558–566, DOI: `10.2307/3213617`; abstract inspected, full text unavailable.
4. A. F. Siegel and L. Holst, *Covering the circle with random arcs of random sizes*, Journal of Applied Probability **19** (1982), 373–381, DOI: `10.2307/3213488`; abstract inspected (generalized random-length setting).
5. E. Pitts, *The overlap of random particles and similar problems: expressions for variance of coverage and its analogue*, SIAM Journal on Applied Mathematics **41** (1981), 493–498, DOI: `10.1137/0141040`; abstract inspected.
6. F. Huffer, *Variability orderings related to coverage problems on the circle*, Stanford technical report SOL ONR 346 (June 1984), `https://statistics.stanford.edu/technical-reports/variability-orderings-related-coverage-problems-circle`; bibliographic record inspected.
