# All-moment stability frontiers for randomized implicit two-stage Runge–Kutta decay

## Finding

For the two randomized implicit two-stage Runge–Kutta schemes of Bochacik and Przybyłowicz, consider the scalar decay test problem \(y'=-a y\), where \(a>0\), \(h>0\), \(s=ah\), and the initial value is nonzero. At every step use an independent \(U\sim\operatorname{Uniform}[0,1]\). For every real \(p>0\), the amplification moment is

\[
F_p(s)=\mathbb E\left|1-\frac{s}{1+sU}\right|^p
=\int_{1-s}^{1/(1+s)}\frac{|r|^p}{(1-r)^2}\,dr.
\]

It has **the same unique minimizing step \(s=\sqrt2\) for every \(p>0\)**, and a **unique stability cutoff \(s_p>2\)**, determined by \(F_p(s_p)=1\). The exact statement for every \(p>0\) is

\[
\mathbb E|y_k|^p\longrightarrow0\quad\Longleftrightarrow\quad 0<s<s_p.
\]

At \(s=s_p\) the moment remains equal to \(|y_0|^p\) for every iteration; for \(s>s_p\) it grows geometrically. The cutoff is strictly decreasing in \(p\): \(p<q\) implies \(s_p>s_q\). Its endpoint laws are

\[
s_p\sim\frac{12}{\pi^2p}\log\frac1p\quad(p\downarrow0),
\qquad
s_p=2+\frac{\log(4p)+o(1)}p\quad(p\to\infty).
\]

In particular \(s_1=6.218262237597\ldots\), while \(s_2=4.033610469358\ldots\). The latter is the previously established mean-square cutoff, not part of the priority claim.

## Assumptions and scope

Both algorithms use one new uniform random stage fraction per step, independent across steps, in exact arithmetic. On an autonomous scalar decay equation, their updates coincide. The assertion concerns the absolute \(p\)-th moment of the iterate, not the local discretization error. For \(0<p<1\), the expression is a moment rather than a norm. The initial value \(y_0\) is deterministic and nonzero. The theorem gives the entire **negative real stability ray**; no general complex-plane \(p\)-stability region is asserted.

## Proof

**1. Common scalar multiplier and its law.** Write \(s=ah\). The semi-implicit method's stage solves \(w=y_{k-1}-sUw\), hence \(w=y_{k-1}/(1+sU)\), followed by \(y_k=y_{k-1}-sw\). The fully implicit method solves \(y_k=y_{k-1}-s[(1-U)y_{k-1}+Uy_k]\), giving the identical update

\[
y_k=R_s(U_k)y_{k-1},\qquad R_s(u)=1-\frac{s}{1+su}.
\]

Since \(R_s\) increases strictly from \(1-s\) to \(1/(1+s)\), and its inverse is \(u=(1-r)^{-1}-s^{-1}\), the push-forward of Lebesgue measure has density \((1-r)^{-2}\) on that interval. Independence yields the exact identity

\[
\mathbb E|y_k|^p=|y_0|^pF_p(s)^k.
\]

**2. Universal minimum.** Leibniz differentiation of the moving-density integral (the fixed interior cusp at \(r=0\) is integrable) yields, for all \(s>0\),

\[
F_p'(s)=\frac{|1-s|^p-(1+s)^{-p}}{s^2}.
\]

For \(0<s<1\), the first numerator term is smaller than the second because \((1-s)(1+s)<1\). For \(s>1\), their comparison is the comparison between \(s-1\) and \(1/(1+s)\); equality occurs exactly at \(s=\sqrt2\). Thus \(F_p\) decreases strictly on \((0,\sqrt2)\) and increases strictly on \((\sqrt2,\infty)\). It extends continuously to \(F_p(0)=1\), and \(F_p(2)<1\) since \(|R_2(u)|<1\) except on a null endpoint.

**3. A unique cutoff for all moments.** For every fixed \(u>0\), \(R_s(u)\to1-u^{-1}\) as \(s\to\infty\). If \(0<p<1\), dominated convergence (\(|R_s(u)|\le\max(1,u^{-1}-1)\)) gives

\[
\lim_{s\to\infty}F_p(s)=\int_0^1u^{-p}(1-u)^p\,du
=B(1-p,1+p)=\frac{\pi p}{\sin(\pi p)}>1.
\]

For \(p\ge1\), Fatou's lemma shows the limit is \(+\infty\), since the pointwise limiting integrand is nonintegrable near zero. Strict monotonicity after \(\sqrt2\) therefore gives precisely one crossing of the value \(1\), necessarily beyond \(2\). The multiplicative moment identity proves the strict stability criterion, including the equality case.

**4. Strict ordering of cutoffs.** If \(0<p<q\), then at \(s=s_q\) strict power-mean monotonicity for the nonconstant variable \(|R_s(U)|\) gives

\[
F_p(s_q)<F_q(s_q)^{p/q}=1.
\]

Since \(s_q>2>\sqrt2\), the monotone-increasing branch gives \(s_p>s_q\).

**5. Small-moment endpoint.** The logarithmic mean is

\[
\mu_s=\mathbb E\log|R_s(U)|
=-\frac{(1+s)\log(1+s)+(1-s)\log|1-s|}{s}<0
\quad(s>0),
\]

with the continuous convention at \(s=1\). The strict sign follows, for example, from the established almost-sure stability theorem for these schemes; alternatively, differentiate the numerator: it is positive for \(s>0\). Consequently, for each fixed \(s>0\), \(F_p(s)=1+p\mu_s+o(p)<1\) as \(p\downarrow0\), so \(s_p\to\infty\).

The universal density \((1-r)^{-2}\) shows that, uniformly in \(s\ge2\), the random variable \(L_s=\log|R_s(U)|\) has bounded \(\mathbb E[|L_s|^3e^{\delta|L_s|}]\) for any fixed \(0<\delta<1\): on the negative half-line put \(v=-r\), and bound the integrand by a constant times \((1+v)^{-2}(v^\delta+v^{-\delta})|\log v|^3\); the positive half-line has length and density uniformly bounded. Therefore

\[
F_p(s)=1+p\mu_s+\frac{p^2}{2}\nu_s+O(p^3),\qquad
\nu_s=\mathbb E[L_s^2],
\]

uniformly in \(s\ge2\) as \(p\downarrow0\). By the same density convergence and uniform integrability, \(\nu_s\to\pi^2/3\) as \(s\to\infty\): the limiting log-ratio is \(\log((1-U)/U)\), whose squared integral is \(\pi^2/3\). Direct expansion of \(\mu_s\) gives \(\mu_s=-(2\log s+2+o(1))/s\). Setting \(s=s_p\) and \(F_p(s_p)=1\) now yields \(p s_p/\log s_p\to12/\pi^2\); inversion of this relation gives the stated \(s_p\sim(12/\pi^2p)\log(1/p)\).

**6. Large-moment endpoint.** The cutoff decreases to \(2\): at \(s=2\) every finite-order moment is below one, while at every fixed \(s>2\) the event \(|R_s(U)|>1\) has positive probability, forcing \(F_p(s)\to\infty\) as \(p\to\infty\). For \(s=s_p\to2\), split the density at zero. The positive contribution is at most \((1+s_p)^{-p}\), while the negative contribution is

\[
\int_0^{s_p-1}\frac{v^p}{(1+v)^2}\,dv
=\frac{(s_p-1)^{p+1}}{(p+1)s_p^2}(1+o(1)),
\]

by endpoint concentration, uniformly as \(p\to\infty\) and \(s_p\to2\). The equation \(F_p(s_p)=1\) gives \((s_p-1)^{p+1}=4p(1+o(1))\). Taking logarithms proves \(s_p=2+[\log(4p)+o(1)]/p\).

**7. Special cases.** For \(s>1\), direct integration yields

\[
F_1(s)=-1+\frac2s+2\log s-\log(1+s),\qquad
F_2(s)=1+\frac{s^2}{1+s}-2\log(1+s).
\]

Their unique positive crossings above \(2\) yield the displayed numerical values. The second formula and its numerical crossing were already derived in the originating paper.

## Verification

Run `python VERIFY.py` with Python 3.10 or later and the `mpmath` package installed. The checker reconstructs both algorithmic updates with exact rational arithmetic, verifies the density's normalization and inverse CDF, checks the \(p\)-independent minimum and analytic derivative against independent quadrature, verifies the first- and second-moment closed forms, and computes ordered cutoffs. The verifier reports 272 passed checks. Numerical checks support but do not establish the global proof, which is above.

## Relationship to prior work

Bochacik and Przybyłowicz introduced the randomized semi-implicit and implicit two-stage Runge–Kutta updates and established that, for the scalar test equation, their multipliers coincide. They proved almost-sure and in-probability stability throughout the open left half-plane, and showed that mean-square stability is restricted on the negative real axis to approximately \((-4.03,0)\); see their 2024 preprint, Section 3, Facts 4 and 7. The later journal version lists a third author and discusses the same three stability notions. The original preprint explicitly identified general \(L^p\)-stability regions as future research. The contribution here is the all-positive-moment real-axis classification, the universal minimizing step, strict nesting, and both endpoint asymptotics, not the already-known quadratic case or almost-sure stability. Other stochastic \(\theta\)-method and randomized Runge–Kutta studies provide related stability principles without the present exact moment-dependent cutoffs for this particular multiplier.

## Limitations

The full complex-valued stability boundary remains unclassified for general \(p\). The result assumes independent uniform stage fractions and a scalar real negative eigenvalue; matrix nonnormality, nonlinear systems, nonuniform sampling, finite precision, and adaptive step sizes are outside the theorem. The cutoff descriptions require evaluation of an ordinary one-dimensional integral for generic \(p\). The moment threshold does not contradict almost-sure decay above it: rare large multipliers can dominate moments. No claim of independent verification or priority beyond the inspected literature is made.

## References

1. T. Bochacik and P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, arXiv:2404.19059v1, first posted 29 April 2024, especially Section 3, Facts 4 and 7, and Section 5 (future work). https://arxiv.org/abs/2404.19059
2. T. Bochacik, P. Przybyłowicz, and Ł. Stępień, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, BIT Numerical Mathematics 65, article 7 (2025), DOI: 10.1007/s10543-024-01050-9. https://doi.org/10.1007/s10543-024-01050-9
3. D. J. Higham, *Mean-square and asymptotic stability of the stochastic theta method*, SIAM Journal on Numerical Analysis 38 (2000), 753–769, DOI: 10.1137/S003614299834736X. https://doi.org/10.1137/S003614299834736X
4. X. Mao, *Almost sure exponential stability in the numerical simulation of stochastic differential equations*, SIAM Journal on Numerical Analysis 53 (2015), 370–389, DOI: 10.1137/140966198. https://doi.org/10.1137/140966198
