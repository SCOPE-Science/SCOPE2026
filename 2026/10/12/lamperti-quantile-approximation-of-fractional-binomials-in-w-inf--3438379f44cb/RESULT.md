# Lamperti-quantile approximation of fractional binomials in \(W_\infty\)
## Finding
Fix a real \(0<\alpha<1\). Put \(m_N=\lfloor\alpha N\rfloor\) and define
\[
z_\alpha(v)=\frac2\alpha\operatorname{artanh}
\left(\frac{\tan(\pi\alpha(v-1/2))}{\tan(\pi\alpha/2)}\right),
\qquad
p_\alpha(v)=\frac1{1+e^{-z_\alpha(v)}},\quad 0<v<1.
\tag{1}
\]
Let \(Y_N\) be the convolution of independent Bernoulli variables with deterministic parameters
\[
p_{j,N}=p_\alpha((j-1/2)/m_N),\qquad 1\le j\le m_N.
\tag{2}
\]
For \(X_N\sim\mathrm{Bin}(N,1/2)\),
\[
\boxed{\lim_{N\to\infty}\frac1N W_\infty(\alpha X_N,Y_N)=0.}
\tag{3}
\]
Here \(W_\infty(U,V)\) is the essential-supremum optimal transport distance between their laws. In one dimension it equals
\[
W_\infty(U,V)=\sup_{0<q<1}\left|F_U^{-1}(q)-F_V^{-1}(q)\right|,
\]
where generalized inverse CDFs are used. Each \(Y_N\) is a genuine Poisson-binomial distribution, with generating polynomial \(\prod_j(1-p_{j,N}+p_{j,N}z)\) having only real negative roots.

The construction in particular answers the sublinear part of the rational-scaling approximation question in Tang and Tang: for \(N=3n\) and \(\alpha=2/3\) it gives a Poisson-binomial \(Y_{3n}\) on \(\{0,\ldots,2n\}\) with
\[
W_\infty((2/3)\mathrm{Bin}(3n,1/2),Y_{3n})=o(n).
\]
It also applies to every fixed real scaling strictly between zero and one.

## Assumptions and scope
The scaling \(\alpha\) is fixed while \(N\to\infty\); the target binomial has success probability exactly \(1/2\). No coupling between different values of \(N\) is required. The error is sublinear, not asserted bounded. The endpoint probabilities in (2) lie strictly between zero and one. The integer restriction on the number of Bernoulli trials is handled by the floor \(m_N\).

## Proof
### 1. A probability law realizing fractional logistic cumulants
Let \(S,S'\) be independent, strictly positive \(\alpha\)-stable random variables, normalized by
\[
\mathbb E e^{-sS}=\mathbb E e^{-sS'}=e^{-s^\alpha},\qquad s\ge0.
\]
Existence follows, for example, by taking the total jump mass of a Poisson random measure with Lévy intensity
\[
\frac{\alpha}{\Gamma(1-\alpha)}x^{-1-\alpha}\,dx,
\]
since its Laplace exponent equals \(s^\alpha\). Put \(\Theta=S/S'\). For every \(u>0\), Tonelli's theorem and differentiation of the stable Laplace transform give the exact identity
\[
\begin{aligned}
\mathbb E\frac1{1+u\Theta}
&=\mathbb E\frac{S'}{S'+uS}\\
&=\int_0^\infty \mathbb E[S'e^{-sS'}]\,\mathbb E[e^{-usS}]\,ds\\
&=\int_0^\infty\alpha s^{\alpha-1}e^{-(1+u^\alpha)s^\alpha}\,ds
=\frac1{1+u^\alpha}.
\end{aligned}
\tag{4}
\]

The Stieltjes transform of \(\Theta\) is consequently
\[
G(z)=\mathbb E\frac1{z+\Theta}
=\frac{z^{\alpha-1}}{1+z^\alpha},\qquad z>0.
\]
Standard Stieltjes inversion across the negative real axis yields the positive Lamperti density
\[
f_\Theta(x)=\frac{\sin(\pi\alpha)}\pi
\frac{x^{\alpha-1}}{1+2\cos(\pi\alpha)x^\alpha+x^{2\alpha}},\qquad x>0.
\tag{5}
\]
For completeness, its normalizing integral follows on substituting \(y=x^\alpha\) and using
\[
\int_0^\infty\frac{dy}{1+2\cos(\theta)y+y^2}=\frac\theta{\sin\theta},
\quad 0<\theta<\pi.
\]
Alternatively, (4) already ensures normalization and uniqueness. For \(Z=\log\Theta\), (5) gives density
\[
f_Z(z)=\frac{\sin(\pi\alpha)}{2\pi(\cosh(\alpha z)+\cos(\pi\alpha))}.
\]
Its CDF, as verified by differentiation and by its limits at both infinities, is
\[
F_Z(z)=\frac12+\frac1{\pi\alpha}\arctan\left(
\tan\frac{\pi\alpha}2\,\tanh\frac{\alpha z}2
\right).
\tag{6}
\]
Inverting (6) gives exactly \(z_\alpha(v)\) in (1). Thus (2) consists of midpoint quantiles of the pushforward law \(P=\Theta/(1+\Theta)\in(0,1)\). Its distribution will be denoted \(\nu_\alpha\).

Define the Bernoulli log-cumulant mixture
\[
H(t)=\int_0^1\log(1-p+pe^t)\,d\nu_\alpha(p).
\]
The integrand and its first derivative are bounded uniformly in \(p\in[0,1]\) for each fixed \(t\). Since \(P/(1-P)=\Theta\), differentiating under the integral and using (4) gives
\[
H'(t)=\mathbb E\frac{e^t\Theta}{1+e^t\Theta}
=1-\frac1{1+e^{\alpha t}}
=\frac{e^{\alpha t}}{1+e^{\alpha t}}.
\]
As \(H(0)=0\), integration yields
\[
\boxed{H(t)=\frac1\alpha\log\frac{1+e^{\alpha t}}2.}
\tag{7}
\]

### 2. Matching full large-deviation rate functions
The function \(p_\alpha\) is continuous on \((0,1)\), strictly increasing, and bounded in \((0,1)\). For any fixed real \(t\), the function \(v\mapsto\log(1-p_\alpha(v)+p_\alpha(v)e^t)\) is bounded and continuous except possibly at the two endpoints, hence Riemann integrable. Using \(m_N/N\to\alpha\), (2) and (7),
\[
\begin{aligned}
\Lambda_N(t)
&:=\frac1N\log\mathbb E e^{tY_N}\\
&=\frac1N\sum_{j=1}^{m_N}\log(1-p_{j,N}+p_{j,N}e^t)\\
&\longrightarrow\alpha H(t)
=\Lambda(t):=\log\frac{1+e^{\alpha t}}2.
\end{aligned}
\tag{8}
\]
The same Riemann-sum argument applies to the first two derivatives in \(t\), since each Bernoulli tilted mean is continuous in its parameter and each tilted variance lies in \([0,1/4]\). By contrast, for \(U_N:=\alpha X_N\),
\[
\frac1N\log\mathbb E e^{tU_N}=\Lambda(t)
\]
holds exactly for every \(N\).

The derivative of the common limit is
\[
\Lambda'(t)=\frac{\alpha e^{\alpha t}}{1+e^{\alpha t}},
\]
a strictly increasing bijection from \(\mathbb R\) to \((0,\alpha)\). Its Legendre transform is
\[
I(x)=\frac{x}{\alpha}\log\frac{2x}{\alpha}
+\left(1-\frac{x}{\alpha}\right)
\log\left(2\left(1-\frac{x}{\alpha}\right)\right),
\quad0<x<\alpha.
\tag{9}
\]
This rate is continuous, decreases strictly from \(\log2\) to zero on \((0,\alpha/2)\), and increases strictly from zero to \(\log2\) on \((\alpha/2,\alpha)\).

We record the exact logarithmic one-sided tails, for \(Z_N\) equal to either \(U_N\) or \(Y_N\):
\[
\lim_{N\to\infty}\frac1N\log\Pr\{Z_N\le Nx\}=-I(x),
\quad 0<x<\alpha/2,
\tag{10}
\]
\[
\lim_{N\to\infty}\frac1N\log\Pr\{Z_N>Nx\}=-I(x),
\quad \alpha/2<x<\alpha.
\tag{11}
\]
Here is an elementary proof rather than an appeal to an unverified infinite-support large-deviation theorem. Chernoff's bound using (8) gives the upper logarithmic limits in (10) and (11). For the matching lower bound, fix \(a\in(0,\alpha)\), set \(t_a\) by \(\Lambda'(t_a)=a\), and change law using the exponential tilt
\[
\frac{d\Pr_{N,t_a}}{d\Pr}
=e^{t_a Z_N-N\Lambda_N(t_a)}.
\]
For either family, the tilted mean divided by \(N\) converges to \(a\), while the tilted variance is at most \(\alpha^2 N/4\) for \(U_N\) and \(m_N/4\) for \(Y_N\). By Chebyshev, every fixed interval \([a-\epsilon,a+\epsilon]\) carries tilted probability tending to one. On this interval, reversing the tilt costs at most \(N(|t_a|\epsilon+o(1))\) beyond \(-NI(a)\). For (10), first choose \(a<x<\alpha/2\) and \(\epsilon<x-a\), then send \(a\uparrow x\) and \(\epsilon\downarrow0\); (11) follows symmetrically with \(a>x>\alpha/2\). This proves both rate limits. The same derivative limit or a direct variance bound also gives
\[
U_N/N\longrightarrow\alpha/2,\qquad Y_N/N\longrightarrow\alpha/2
\]
in probability.

### 3. From coincident rates to uniform transport
We prove a quantile lemma sufficient for (3). Let two families of variables have supports contained in \([0,\alpha N]\), satisfy (10)–(11) with the same \(I\), and converge after division by \(N\) in probability to \(\alpha/2\). Then
\[
\sup_{0<q<1}\left|F_{U_N}^{-1}(q)-F_{Y_N}^{-1}(q)\right|=o(N).
\tag{12}
\]
Indeed, if not, there is a subsequence, probability levels \(q_N\), and a fixed \(\epsilon>0\) such that one of the quantile differences is at least \(\epsilon N\). Suppose for definiteness that
\[
F_{U_N}^{-1}(q_N)+\epsilon N\le F_{Y_N}^{-1}(q_N).
\]
After taking a subsequence, the normalized quantiles converge to \(a<b\) in \([0,\alpha]\). Choose fixed \(a<z_1<z_2<b\), both strictly inside \((0,\alpha)\). We may arrange either that both lie below \(\alpha/2\), that both lie above \(\alpha/2\), or that they straddle \(\alpha/2\). By the generalized-inverse definition, for large \(N\) the hypothetical quantile ordering forces
\[
F_{U_N}(Nz_1)\ge q_N>F_{Y_N}(Nz_2).
\tag{13}
\]
If \(z_2<\alpha/2\), the strictly decreasing left-tail rate yields
\[
F_{U_N}(Nz_1)<F_{Y_N}(Nz_2)
\]
for large \(N\), since \(I(z_1)>I(z_2)\). If \(z_1>\alpha/2\), the increasing right-tail rate yields the same strict CDF inequality because \(I(z_1)<I(z_2)\). If the points straddle \(\alpha/2\), convergence in probability again gives the strict CDF inequality. Each case contradicts (13). The reverse quantile difference is ruled out by swapping the two families. Therefore (12) holds. Note that the argument explicitly controls extreme exponential quantile levels as well as central ones: no fixed-quantile-only approximation is used.

Both families in (3) have the required support and tail properties, so (12) proves (3).

## Verification
The included standalone `verify.py` evaluates the closed-form parameter quantiles using only standard-library functions, numerically checks the mixture identity (7) over multiple \(\alpha\) and \(t\) values, and computes finite Poisson-binomial probabilities recursively in floating point. It then computes one-dimensional quantile transport distances for small sample sizes in the \(\alpha=2/3\) case and checks that the resulting values are far below the sample size. These computations verify formulas and finite examples; they are not a proof of (3).

The essential mathematical verification is in the proof: (4) is obtained by positive integrals, (5) by Stieltjes inversion, (6) by direct differentiation, (7) by integrating the exact logarithmic derivative, (10)–(11) by Chernoff and a tilted concentration argument, and (12) by a two-sided quantile contradiction.

## Relationship to prior work
Tang and Tang's 2019 preprint, Section 4, Open Problem 4.6, asks whether a strongly Rayleigh (Poisson-binomial) variable can approximate \((2/3)\mathrm{Bin}(3n,1/2)\) in \(W_\infty\) with error \(o(n)\). Their Proposition 4.5 rules out any fixed-parameter \(\mathrm{Bin}(2n,p)\) choice with that rate, and they observe that evenly spaced heterogeneous Bernoulli parameters also have linear lower error. They conjecture an even stronger bounded-error behavior, which is **not** established here. The present construction answers the sublinear question by a parameter distribution with an exact fractional logistic cumulant identity. It does not imply that their minimum transport error is uniformly bounded, nor does it determine its optimal finite-sample value.

Mattner studies Bernoulli convolutions with prescribed first few moments, proving extremizers with few distinct interior parameters (Theorem 1.1). That is a different optimization: the present construction requires increasingly many heterogeneous parameter values, matches a full large-deviation rate function rather than a fixed finite list of moments, and concerns maximal rather than expected transport cost.

The Lamperti stable-ratio density is classical; the new mathematical use here is the fractional logistic generating-function identity (7), a deterministic Bernoulli quantile discretization, and the rate-to-\(W_\infty\) argument solving the posed approximation question. The stable-ratio law itself is not claimed as new.

Liggett's 2021 full-text article, *Approximating multiples of strong Rayleigh random variables*, proves polynomial factorization properties for rounded multiples of strongly Rayleigh laws, including the Hurwitz property for the \(2/k\) rounding. Those are results about exact probability generating polynomial factors, not a Poisson-binomial law with sublinear \(W_\infty\) transport to an unrounded fractional binomial. Thus this close title does not imply (3).\n\n## Limitations\nThe theorem only establishes sublinear transport discrepancy. It provides no explicit convergence rate, and does not settle the motivating stronger \(O(1)\) conjecture. The source binomial has success probability \(1/2\); extending the exact log-cumulant representation to general success probabilities is not addressed.

The proof uses matching full large-deviation exponents, not just means and variances. Such matching alone does not automatically imply uniform quantile closeness without the strict-rate and endpoint argument supplied here.

A residual priority risk is that the Lamperti transform may have been used for the same Poisson-binomial approximation in probability or optimal-transport literature under terminology not returned by searches.

## References
1. W. Tang and F. Tang, “The Poisson binomial distribution—Old & New,” arXiv:1908.10024v1 (27 August 2019), Section 4, Open Problem 4.6; *Statistical Science* 38 (2023), 108–119, DOI 10.1214/22-STS852. The version-specific open-problem numbering follows the 2019 preprint.
2. L. Mattner, “Extreme expectations of Bernoulli convolutions given their first few moments are attained at shifted convolutions of as few binomials,” arXiv:2204.06040v1 (12 April 2022), Theorem 1.1. Primary MSC 60E15.
3. T. M. Liggett, “Approximating multiples of strong Rayleigh random variables,” *Celebratio Mathematica* (2021), https://celebratio.org/Liggett_T/article/858/.
4. L. F. James, “Lamperti-type laws,” arXiv:0708.0618 (4 August 2007). Background for the classical stable-ratio density; the needed transform is rederived in the proof.
