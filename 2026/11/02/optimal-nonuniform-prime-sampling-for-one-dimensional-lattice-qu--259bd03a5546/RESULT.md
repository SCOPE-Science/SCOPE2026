# Optimal nonuniform prime sampling for one-dimensional lattice quadrature

## Finding

Uniform sampling of a prime number of nodes is not minimax for the expected absolute error of the one-dimensional, unshifted lattice quadrature rule. For every integer \(n\ge 2\) and every Korobov smoothness \(\alpha>1/2\), the unique minimax law among **all** probability distributions on the primes \(p\in(n/2,n]\) has an explicit positive formula. If at least two primes are available, the optimal sampling probabilities strictly increase with the prime, and the uniform law is strictly suboptimal.

Set \(s=2\alpha>1\), \(\mathcal P_n=\{p\text{ prime}:n/2<p\le n\}\), and \(u_p=p^{-s}\). Define
\[
S_1=\sum_{p\in\mathcal P_n}\frac1{1-u_p},\qquad
S_2=\sum_{p\in\mathcal P_n}\frac{u_p}{1-u_p},\qquad
c=\frac{S_1}{1+S_2},\qquad
w_p=\frac{1-cu_p}{u_p(1-u_p)},\quad W=\sum_pw_p.
\]
Then every \(w_p>0\), and the unique minimizer is
\[
\boxed{\nu_p^*=\frac{w_p}{W},\qquad
\inf_{\nu}\mathcal E_\alpha(\nu)^2=\frac{2\zeta(s)}W.}
\]
For \(|\mathcal P_n|\ge2\), we have \(\nu_p^*<\nu_q^*\) whenever \(p<q\).

As \(n\to\infty\), with the smoothness fixed,
\[
\nu_p^*=\frac{p^s}{\sum_{q\in\mathcal P_n}q^s}(1+o(1))
\quad\text{uniformly over }p\in\mathcal P_n,
\]
and the uniform-to-optimal **worst-case expected absolute error** ratio converges to
\[
\boxed{\lim_{n\to\infty}\frac{\mathcal E_\alpha(\nu^{\rm unif})}{\mathcal E_\alpha(\nu^*)}
=2\sqrt{\frac{(1-2^{-(s+1)})(2^{s-1}-1)}{(s+1)(s-1)}}>1.}
\]
At \(\alpha=1\) this is \(\sqrt{7/6}\), and at \(\alpha=2\) it is \(\sqrt{217/120}\). For \(n=12\), \(\alpha=1\), the primes are \(7,11\), their optimal probabilities are exactly \(2/7,5/7\), and the squared error ratio between uniform and optimal sampling is exactly \(301/247\).

## Assumptions and scope

The real periodic Korobov Hilbert space consists of real \(1\)-periodic functions with finite norm
\[
\|f\|_{\alpha}^2=|\widehat f(0)|^2+
\sum_{m\in\mathbb Z\setminus\{0\}}|m|^{2\alpha}|\widehat f(m)|^2,
\]
where \(\widehat f(m)\) denotes the complex Fourier coefficient, with conjugate symmetry for real functions. For every \(\alpha>1/2\) these Fourier series are absolutely convergent; thus evaluations at lattice nodes are well defined.

The deterministic rule at prime \(p\) is \(Q_p(f)=p^{-1}\sum_{j=0}^{p-1}f(j/p)\), and the target is \(I(f)=\int_0^1f(x)\,dx\). A prime \(P\in\mathcal P_n\) is sampled **once**, with arbitrary fixed probability vector \(\nu\), independent of the function. The objective is
\[
\mathcal E_\alpha(\nu)=\sup_{\|f\|_\alpha\le1}\ \mathbb E_\nu\left|Q_P(f)-I(f)\right|.
\]
This expectation of the absolute error is neither an RMS criterion nor a worst-case-over-primes criterion. The node cost of choosing a larger prime is **not** part of the optimization objective.

## Proof

**1. Exact worst-case representation.** Discrete Fourier orthogonality gives
\[
Q_p(f)-I(f)=\sum_{m\ne0:\,p\mid m}\widehat f(m).
\]
For \(\omega_\nu(m)=\sum_{p\in\mathcal P_n:\,p\mid m}\nu_p\ge0\), the triangle inequality followed by Cauchy--Schwarz gives
\[
\mathbb E_\nu|Q_P(f)-I(f)|\le
\sum_{m\ne0}\omega_\nu(m)|\widehat f(m)|
\le\left(\sum_{m\ne0}|m|^{-s}\omega_\nu(m)^2\right)^{1/2}\|f\|_\alpha.
\]
Both inequalities are attained simultaneously by the real function with \(\widehat f(0)=0\) and \(\widehat f(m)=C|m|^{-s}\omega_\nu(m)\ge0\) for \(m\ne0\), normalized to unit norm. All individual quadrature errors then have the same nonnegative sign. The normalization exists since \(s>1\) and some prime has positive mass. Hence
\[
\mathcal E_\alpha(\nu)^2
=\sum_{m\ne0}|m|^{-s}\omega_\nu(m)^2
=2\zeta(s)\sum_{p,q\in\mathcal P_n}\frac{\nu_p\nu_q}{\operatorname{lcm}(p,q)^s}.
\]

**2. A strictly positive quadratic optimization.** Distinct primes have product equal to their least common multiple. Therefore the normalized quadratic matrix is
\[
A=D+uu^{\mathsf T},\qquad
D=\operatorname{diag}\big(u_p(1-u_p)\big)_{p\in\mathcal P_n},
\qquad u=(u_p)_p.
\]
Since each \(0<u_p<1\), the matrix \(A\) is strictly positive definite. The unconstrained minimizing vector on \(\mathbf1^{\mathsf T}\nu=1\) is \(A^{-1}\mathbf1/(\mathbf1^{\mathsf T}A^{-1}\mathbf1)\). The Sherman--Morrison formula yields \((A^{-1}\mathbf1)_p=w_p\), with \(c\) as defined above; consequently \(W=\mathbf1^{\mathsf T}A^{-1}\mathbf1\) and the optimal normalized quadratic value is \(1/W\).

This unconstrained minimizer lies in the probability simplex. Let \(p_0=\min\mathcal P_n\), \(K=|\mathcal P_n|\). Since \(S_1=K+S_2\), \(c=(K+S_2)/(1+S_2)\le K\). Every prime in the interval is an integer between \(p_0\) and \(n\), so \(K\le n-p_0+1\le p_0\), where the last inequality follows from \(p_0>n/2\). Hence \(cu_p\le Kp_0^{-s}\le p_0^{1-s}<1\). Thus all \(w_p\) are strictly positive and the constrained optimum is attained uniquely by \(\nu^*\).

**3. Strict monotonicity.** For fixed \(c>0\), differentiation gives
\[
\frac{d}{du}\frac{1-cu}{u(1-u)}
=\frac{-1+2u-cu^2}{u^2(1-u)^2}<0
\quad(0<u\le2^{-s}<1/2).
\]
Since \(u_p=p^{-s}\) decreases strictly with increasing prime, the weights \(w_p\) increase strictly. In particular, when \(K\ge2\), the unique optimizer is not uniform, establishing a strict improvement.

**4. Large-\(n\) law.** By the prime number theorem, \(K\sim n/(2\log n)\) and for fixed real \(r\),
\[
\sum_{p\in\mathcal P_n}p^r
\sim\frac{n^{r+1}}{\log n}\int_{1/2}^1 x^r\,dx.
\]
We have \(c\le K\) and \(cu_p=O(Kn^{-s})=o(1)\) uniformly in the prime. Likewise \(u_p=o(1)\), so \(w_p=p^s(1+o(1))\) uniformly. Furthermore
\[
\mathcal E_\alpha(\nu^{\rm unif})^2
=2\zeta(s)\left(K^{-2}\sum_p p^{-s}(1-p^{-s})
+\left(K^{-1}\sum_pp^{-s}\right)^2\right),
\]
where the second term is lower order relative to the first because \(K\max_pp^{-s}=o(1)\). Thus
\[
\frac{\mathcal E_\alpha(\nu^{\rm unif})^2}
{\mathcal E_\alpha(\nu^*)^2}
\longrightarrow
4\left(\int_{1/2}^1x^{-s}dx\right)
\left(\int_{1/2}^1x^{s}dx\right)
=\frac{4(1-2^{-(s+1)})(2^{s-1}-1)}{(s+1)(s-1)}.
\]
Strict Cauchy--Schwarz on the interval \([1/2,1]\) makes this limit strictly greater than one for \(s>1\). Taking square roots completes the proof.

## Verification

The standalone, standard-library Python program `verify.py` independently builds the exact rational quadratic kernel, solves the proposed weights, and compares them with uniform and multiple sampled competitors. It checks all integers \(2\le n\le100\) at \(s\in\{2,3,4,5\}\), verifies discrete Fourier truncations against the proven infinite sum, and checks the stated limiting constants. All 402 test groups passed. These finite checks are reproducibility safeguards, **not** substitutes for the preceding all-dimensional-in-parameter analytic proof and prime-number-theorem argument.

## Relationship to prior work

Kuo, Nuyens and Wilkes, *Random-prime--fixed-vector randomised lattice-based algorithm for high-dimensional integration* (2023), define the uniformly sampled random prime algorithm and give the exact Fourier-frequency worst-case expected absolute error formula for their uniform setting. The present result instead optimizes the entire prime distribution, in the one-dimensional unshifted specialization, and proves the explicit unique optimizer and asymptotic nonuniformity penalty. It relies on, rather than replaces, the standard lattice Fourier aliasing mechanism.

Kritzer, Kuo, Nuyens and Ullrich (2017 preprint) analyze randomized algorithms allowing random numbers of lattice points and random generating vectors, with different sharp-order questions. Dick, Goda and Suzuki (2021) study constructing randomized lattice rules. Nuyens and Wilkes (2023) analyze randomly shifted random-prime lattices in another smoothness/error setting. Goda and Krieg (2024) study uniform random prime and random generator choices with repetition/median. None of the inspected primary texts directly proves the particular distributional minimax and its limiting strict gap. A pre-existing general quadratic-design theorem or specialized nonuniform lattice-sampling result could cover part of this conclusion; publication priority has not been independently established.

## Limitations

The optimizer is for the **one-dimensional** periodic Korobov ball, an unshifted one-draw rule, and the worst-case expected **absolute** error. It does not optimize work-normalized error, worst-case RMS error, randomized shifts, multidimensional generating vectors, or composite moduli. At a single available prime the optimum is trivially the only distribution; strict nonuniformity requires at least two. The smoothness boundary \(\alpha>1/2\) is required for point evaluations and finite error. The asymptotic statement relies on the prime number theorem and asserts no explicit finite-size approximation rate. Scientific originality remains subject to independent literature review.

## References

1. F. Y. Kuo, D. Nuyens and L. Wilkes, *Random-prime--fixed-vector randomised lattice-based algorithm for high-dimensional integration*, arXiv:2304.10413, first posted 20 April 2023. https://arxiv.org/abs/2304.10413
2. P. Kritzer, F. Y. Kuo, D. Nuyens and M. Ullrich, *Lattice rules with random \(n\) achieve nearly the optimal \(\mathcal O(n^{-\alpha-1/2})\) error independently of the dimension*, arXiv:1706.04502, 2017. https://arxiv.org/abs/1706.04502
3. J. Dick, T. Goda and K. Suzuki, *Component-by-component construction of randomized rank-1 lattice rules achieving almost the optimal randomized error rate*, arXiv:2109.11694, 2021. https://arxiv.org/abs/2109.11694
4. D. Nuyens and L. Wilkes, *A randomised lattice rule algorithm with pre-determined generating vector and random number of points for Korobov spaces with \(0<\alpha\le 1/2\)*, arXiv:2308.03138, 2023. https://arxiv.org/abs/2308.03138
5. T. Goda and D. Krieg, *A simple universal algorithm for high-dimensional integration*, arXiv:2411.19164, 2024. https://arxiv.org/abs/2411.19164
