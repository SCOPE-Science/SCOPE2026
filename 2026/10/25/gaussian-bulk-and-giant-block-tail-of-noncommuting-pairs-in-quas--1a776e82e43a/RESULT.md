# Gaussian bulk and giant-block tail of noncommuting pairs in quasitrivial semigroups

## Finding

Let \(n\ge 1\), let \(X_n=\{1,\ldots,n\}\), and let \(\mathcal Q_n\) be the set of all associative quasitrivial operations \(F:X_n\times X_n\to X_n\): thus \(F(F(x,y),z)=F(x,F(y,z))\) and \(F(x,y)\in\{x,y\}\). Define the noncommuting-pair statistic
\[
K(F)=\#\{\{x,y\}\subseteq X_n:x\ne y,\ F(x,y)\ne F(y,x)\}.
\]
Write \(T_n(w)=\sum_{F\in\mathcal Q_n}w^{K(F)}\), with the conventional empty-set term \(T_0(w)=1\). The **complete finite-count distribution** is given by the formal exponential generating function
\[
\boxed{\quad\sum_{n\ge0}\frac{T_n(w)}{n!}z^n
=\left(1-z-2\sum_{m\ge2}\frac{z^m}{m!}w^{\binom m2}\right)^{-1}.\quad}
\]
Equivalently, with \(T_0(w)=1\),
\[
T_n(w)=\sum_{m=1}^n\binom nm a_m w^{\binom m2}T_{n-m}(w),\qquad
 a_1=1,\ a_m=2\ (m\ge2).
\]

Define \(\rho\) as the unique positive solution of \(2e^\rho-\rho=3\), and the probability distribution \(\pi_m=a_m\rho^m/m!\) for \(m\ge1\). For \(B(m)=m\) and \(R(m)=\binom m2\), set
\[
\mu=\mathbb E_\pi B,\qquad
\alpha=\frac{\mathbb E_\pi R}{\mu}
=\frac{\rho e^\rho}{2e^\rho-1},\qquad
\beta=\frac{\mathbb E_\pi[(R-\alpha B)^2]}{\mu}>0.
\]
For a uniformly selected \(F\in\mathcal Q_n\), put \(K_n=K(F)\). Then
\[
\boxed{\quad\mathbb E K_n=\alpha n+O(1),\quad
\operatorname{Var}(K_n)=\beta n+O(1),\quad
\frac{K_n-\alpha n}{\sqrt n}\ \Longrightarrow\ N(0,\beta).\quad}
\]
Numerically, \(\rho\approx0.583073876036691\), \(\alpha\approx0.404401281823201\), and \(\beta\approx0.395674555643731\).

The positive-density upper tail has a **different, sharp superexponential scale**: for every fixed real \(\delta\) with \(0<\delta<1/2\),
\[
\boxed{\quad\lim_{n\to\infty}\frac{\log\Pr(K_n\ge\delta n^2)}{n\log n}
=-\sqrt{2\delta}.\quad}
\]
Both asymptotic laws concern the same exact finite distribution. The exact enumeration and the known structure theorem are ingredients, not independent priority claims.

## Assumptions and scope

The underlying set is labeled; all associative quasitrivial binary laws on it have equal probability. A quasitrivial law always returns one of its two inputs, and associativity is required. Commutation is tested only on unordered pairs of **distinct** elements; repeated inputs commute automatically. The empty-set convention is used only for the generating series. The Gaussian limit is as the integer \(n\to\infty\); the upper-tail statement fixes \(\delta\in(0,1/2)\) before taking the limit. No uniformity as \(\delta\to0\) or \(\delta\to1/2\) is asserted.

## Proof

**1. Classification and the exact statistic.** The established classification of associative quasitrivial operations [1, Theorem 2.1] identifies every \(F\in\mathcal Q_n\) uniquely with an *ordered partition* \((C_1,\ldots,C_j)\) of \(X_n\) and, for each block of size at least two, one of the left or right projections as the within-block product. Between distinct blocks, the operation returns the input in the higher block, regardless of input order. Consequently, distinct elements do not commute if and only if they belong to the same block, and
\[
K(F)=\sum_{i=1}^j\binom{|C_i|}{2}.
\]
There are \(a_m=2\) projection choices for a block of size \(m\ge2\), and just one for a singleton. If the ordered block sizes are \((m_1,\ldots,m_j)\), there are exactly \(n!\prod_i(a_{m_i}/m_i!)\) such operations. Summing over all positive compositions of \(n\) gives the displayed generating function; removing its first block gives the recurrence. At \(w=1\), the established unmarked enumeration [1, Theorem 4.1] is recovered:
\[
\sum_{n\ge0}|\mathcal Q_n|\frac{z^n}{n!}=\frac1{3+z-2e^z}.
\]

**2. Dominant pole and the Gaussian law.** Write
\[
A(z,t)=z+2\sum_{m\ge2}\frac{z^m}{m!}\exp\!\left(it\binom m2\right),
\qquad H(z,t)=\frac1{1-A(z,t)}
\]
for real \(t\). For each real \(t\), \(A(\cdot,t)\) is entire; on every bounded disk it and all derivatives through order two in \(t\) converge uniformly for \(t\) near zero. At \(t=0\), \(A(z,0)=2e^z-2-z\). The equation \(A(\rho,0)=1\) has a unique positive solution because \(A(x,0)\) strictly increases from zero. The Taylor coefficients of \(A(z,0)\) are positive at both degrees one and two and nonnegative elsewhere. The triangle inequality therefore shows \(|A(z,0)|<1\) for \(|z|\le\rho\) except at \(z=\rho\); equality on the boundary could only hold if the phases at degrees one and two both equal one, which forces \(z=\rho\). The zero is simple since \(\partial_z A(\rho,0)=2e^\rho-1>0\).

Zeros of the entire function \(1-A(z,0)\) are isolated. Select a radius \(r>\rho\) that encloses no other zero and on whose circle the denominator is nonzero. Uniform convergence as real \(t\to0\), Rouché's theorem, and the implicit function theorem yield a unique simple zero \(\rho(t)\) inside that circle for sufficiently small real \(t\), with \(\rho(0)=\rho\) and \(\rho(t)\) twice continuously differentiable at zero. Subtract its pole and apply Cauchy's coefficient formula uniformly on the circle:
\[
[z^n]H(z,t)=\frac{\rho(t)^{-n-1}}{\partial_z A(\rho(t),t)}+O(r^{-n}),
\]
where the error bound is uniform in sufficiently small real \(t\). This expansion, divided by its \(t=0\) version, is the characteristic function of \(K_n\), up to an exponentially small relative error.

The weights \(\pi_m=a_m\rho^m/m!\) sum to \(A(\rho,0)=1\). Differentiating \(A(\rho(t),t)=1\) gives
\[
\left.\frac{d}{dt}\log\rho(t)\right|_{t=0}=-i\alpha,
\qquad
\left.\frac{d^2}{dt^2}\log\rho(t)\right|_{t=0}=\beta.
\]
Indeed, if \(\mu=\mathbb E_\pi B\), \(\nu=\mathbb E_\pi R\), then \(\partial_z A(\rho,0)=\mu/\rho\), \(\partial_t A(\rho,0)=i\nu\), and the second derivative reduces exactly to \(\mathbb E_\pi[(R-(\nu/\mu)B)^2]/\mu\). Hence
\[
\log\rho(t)=\log\rho-i\alpha t+\tfrac12\beta t^2+o(t^2).
\]
Set \(t=u/\sqrt n\), subtract the deterministic centering \(\alpha n\), and use the pole formula; the characteristic functions tend to \(\exp(-\beta u^2/2)\). Lévy's continuity theorem proves the Gaussian limit. Differentiation of the uniform pole expansion at zero yields the stated \(O(1)\) mean and variance errors. Positivity \(\beta>0\) follows because the values of \(R-\alpha B\) at \(m=1\) and \(m=2\) cannot both vanish, and both have positive \(\pi\)-probability.

For numerical evaluation, the needed raw moments are
\[
\begin{aligned}
\mu&=\rho(2e^\rho-1),&\mathbb E_\pi R&=\rho^2e^\rho,\\
\mathbb E_\pi B^2&=2\rho^2e^\rho+\mu,&
\mathbb E_\pi(BR)&=\rho^2(\rho+2)e^\rho,\\
\mathbb E_\pi R^2&=\tfrac12(\rho^4+4\rho^3+2\rho^2)e^\rho.
\end{aligned}
\]
These give the displayed \(\alpha,\beta\) with ordinary real arithmetic.

**3. The sharp positive-density upper tail.** Fix \(0<\delta<1/2\). If an ordered-block profile has sizes \(m_1+\cdots+m_j=n\) and \(K\ge\delta n^2\), then
\[
\sum_i(m_i/n)^2=2K/n^2+1/n\ge2\delta.
\]
Fix \(0<\varepsilon<2\delta\), and let \(s\) be the total mass of those blocks with \(m_i\ge\varepsilon n\), divided by \(n\). For the smaller blocks, \(\sum(m_i/n)^2\le\varepsilon\); for the larger blocks, \(\sum(m_i/n)^2\le s^2\). Thus \(s\ge\sqrt{2\delta-\varepsilon}\). The elementary bound \(m!\ge(m/e)^m\) shows
\[
\prod_i m_i!\ge(\varepsilon n/e)^{sn}.
\]
There are at most \(2^{n-1}\) positive block-size compositions, with at most \(2^n\) projection assignments per composition. Since \(|\mathcal Q_n|\ge n!\) (the total-order maximum laws), division by the total count gives
\[
\Pr(K_n\ge\delta n^2)\le
4^n(\varepsilon n/e)^{-n\sqrt{2\delta-\varepsilon}}
\]
for all sufficiently large \(n\). Taking logarithms, dividing by \(n\log n\), and then sending \(\varepsilon\downarrow0\) proves the desired upper bound.

For the matching lower bound, take one block of size \(m=\lceil\sqrt{2\delta}\,n+2\rceil\) as the highest block, with every other block a singleton in any total order. For sufficiently large \(n\), \(m\le n\) and \(\binom m2\ge\delta n^2\). These choices produce \(2n!/m!\) distinct operations. For any fixed \(r\in(0,\rho)\), nonnegative coefficients of the unmarked generating function give
\[
|\mathcal Q_n|\le n!\frac{r^{-n}}{3+r-2e^r}.
\]
Therefore the tail probability is at least \(2(3+r-2e^r)r^n/m!\). Stirling's formula implies
\[
\log(m!)=\sqrt{2\delta}\,n\log n+O(n),
\]
so the logarithmic lower bound is \(-\sqrt{2\delta}\). The upper and lower bounds match.

## Verification

The self-contained standard-library script `checks/check_quasitrivial.py` constructs every quasitrivial multiplication table for \(1\le n\le4\), tests associativity directly on all triples, and compares the resulting noncommuting-pair counts to the independent recurrence. It checks \(4,165\) candidate multiplication tables in total and reproduces the totals \(1,4,20,138\) for those sizes. For \(n=4\), the exact spectrum is
\[
T_4(w)=24+72w+24w^2+16w^3+2w^6.
\]
It also reproduces the established total sequence through \(n=8\), and computes exact recurrence moments through \(n=60\) as finite consistency checks on the constants. To run after extracting the embedded files: `python checks/check_quasitrivial.py`. The analytic pole and large-deviation bounds, not finite testing, establish the limits.

## Relationship to prior work

Couceiro, Devillet and Marichal [1] establish the unique ordered-partition/projection classification, enumerate all labeled quasitrivial semigroups, and give the unmarked generating function. Thus the block description and unmarked enumeration are prior work. Devillet, Marichal and Teheux [2] classify related isomorphism/orbit types, identify the fully commutative and anticommutative extreme cases, and state the sharp asymptotic total count. In particular, their total-count asymptotic is **not** claimed here as new. The precise new claim concerns the full noncommuting-pair statistic, its explicit Gaussian bulk constants, and its qualitatively different \(n\log n\) positive-density tail exponent. The characteristic-function transfer and factorial estimates are classical techniques, used here with a quadratic block reward.

## Limitations

The exact generating series is interpreted **formally** in \(z\) for arbitrary \(w\). Because the block reward grows quadratically, it need not converge for nonzero \(z\) when real \(w>1\); the Gaussian proof only uses \(w=e^{it}\) with real \(t\), for which the coefficient series is entire in \(z\). The upper-tail result is logarithmic only and supplies neither a sharp multiplicative prefactor nor a uniform assertion at the endpoints of the \(\delta\) interval. No local limit theorem, asymptotic independence statement, or independent priority certification is asserted. The basic block classification, total-count asymptotic, and general analytic techniques are not new. An equivalent formulation in older weak-order/preferential-arrangement asymptotic literature remains a priority risk.

## References

1. M. Couceiro, J. Devillet, and J.-L. Marichal, *Quasitrivial semigroups: characterizations and enumerations*, arXiv:1709.09162 (first submitted 2017-09-26), Theorems 2.1 and 4.1, https://arxiv.org/abs/1709.09162 .
2. J. Devillet, J.-L. Marichal, and B. Teheux, *Classifications of quasitrivial semigroups*, arXiv:1811.11113 (first submitted 2018-11-27), Sections 2, 3, and 5, https://arxiv.org/abs/1811.11113 .
