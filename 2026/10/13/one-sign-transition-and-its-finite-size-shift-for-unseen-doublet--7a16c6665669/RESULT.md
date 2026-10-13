# One sign transition and its finite-size shift for unseen–doubleton covariance

## Finding

Let \(k\ge3\) and \(a>0\). Draw a probability vector \(P\sim\operatorname{Dirichlet}(a,\ldots,a)\) on \(k\) categories, and then draw \(N\) independent categorical observations conditional on \(P\). Write \(X_i\) for the count in category \(i\), and \(C_j=\sum_{i=1}^{k}\mathbf1\{X_i=j\}\). The statistics \(C_0\) and \(C_2\) count unseen categories and doubletons, respectively.

For every integer \(N\ge2\), define the rising factorial \((x)^{\overline n}=\prod_{j=0}^{n-1}(x+j)\) (the empty product is one), and set
\[
\begin{aligned}
 u_{k,N}&=\frac{((k-1)a)^{\overline N}}{(ka)^{\overline N}},\\
 v_{k,N}&=\binom N2\frac{a(a+1)((k-1)a)^{\overline{N-2}}}{(ka)^{\overline N}},\\
 R_{k,N}&=\frac{k-1}{k}\frac{((k-2)a)^{\overline{N-2}}}{((k-1)a)^{\overline{N-2}}}
 \frac{(ka)^{\overline N}}{((k-1)a)^{\overline N}}.
\end{aligned}
\]
Then the exact covariance is
\[
 \operatorname{Cov}(C_0,C_2)=k^2u_{k,N}v_{k,N}(R_{k,N}-1).
\]
The positive ratio \(R_{k,N}\) decreases strictly with \(N\):
\[
 \frac{R_{k,N+1}}{R_{k,N}}
 =1-\frac{a(a+2)}{((k-1)a+N-2)((k-1)a+N)}\in(0,1).
\]
There is exactly one real number \(r_{k,a}>2\), obtained by extending the rising factorials through gamma functions, such that \(R_{k,r_{k,a}}=1\). At every integer \(N\ge2\) the covariance is strictly positive for \(N<r_{k,a}\), zero for \(N=r_{k,a}\), and strictly negative for \(N>r_{k,a}\). It is zero at \(N=0,1\).

For each fixed \(a>0\), this unique crossing has the **constant-order finite-size shift**
\[
 \boxed{r_{k,a}=\frac{a}{a+1}k+\frac{a+3}{2(a+1)}+O_a(k^{-1})}\qquad(k\to\infty).
\]
Put \(\lambda_a=a/(a+1)\), \(\beta_a=(a+3)/(2(a+1))\), and
\[
 D_a=\left(\frac{a+1}{a+2}\right)^{2a}\frac{(a+1)^3}{2(a+2)^3}>0.
\]
Whenever integer sequences \(N=N(k)\) satisfy \(N-\lambda_ak\to\beta\in\mathbb R\), their **critical-window covariance** has the finite nonzero-scale limit
\[
 \boxed{\operatorname{Cov}(C_0,C_2)\longrightarrow D_a(\beta_a-\beta).}
\]
At the Bose–Einstein shape \(a=1\) there is also an all-size closed form:
\[
 R_{k,N}-1=\frac{k+2-2N}{k(k+N-4)},\qquad r_{k,1}=\frac{k+2}{2}.
\]

## Assumptions and scope

The distribution is symmetric Dirichlet–multinomial: the latent category weights are sampled once and held fixed throughout all \(N\) observations. The number of categories is at least three; \(a\) is any positive real number; and \(N\) is a nonnegative integer. The continuous extension \(r_{k,a}\) is a comparison device and is not itself a sample size. Statements involving \(k\to\infty\) hold for **fixed** \(a\); they do not assert uniformity as \(a\) varies with \(k\). No claim is made about asymmetric Dirichlet vectors or about independent multinomial observations outside this mixture.

## Proof

**Joint probabilities.** Integrating the multinomial mass function against the symmetric Dirichlet law gives, for nonnegative counts summing to \(N\),
\[
 \Pr(X_1=x_1,\ldots,X_k=x_k)
 =\frac{N!}{(ka)^{\overline N}}
  \prod_{i=1}^{k}\frac{a^{\overline{x_i}}}{x_i!}.
\]
In particular \(\Pr(X_1=0)=u_{k,N}\), \(\Pr(X_2=2)=v_{k,N}\), and
\[
 \Pr(X_1=0,X_2=2)
 =\binom N2\frac{a(a+1)((k-2)a)^{\overline{N-2}}}{(ka)^{\overline N}}.
\]
Because an individual category cannot simultaneously have zero and two observations,
\[
 \mathbb E[C_0C_2]=k(k-1)\Pr(X_1=0,X_2=2).
\]
Subtracting \(\mathbb E C_0\,\mathbb E C_2=k^2u_{k,N}v_{k,N}\) proves the exact covariance and the displayed \(R_{k,N}\).

**Strict monotonicity and the unique crossing.** Cancel adjacent rising factorials in \(R\). The denominator minus the numerator in the ratio of successive terms equals precisely \(a(a+2)>0\); hence \(R_{k,N+1}/R_{k,N}\in(0,1)\). Its initial value is
\[
 R_{k,2}=\frac{ka+1}{(k-1)a+1}>1.
\]
The gamma continuation is positive for all real \(x\ge2\) and its logarithmic derivative is
\[
 \begin{aligned}
 \frac{d}{dx}\log R_{k,x}
 ={}&\psi((k-2)a+x-2)+\psi(ka+x)\\
 &-\psi((k-1)a+x-2)-\psi((k-1)a+x),
 \end{aligned}
\]
where \(\psi\) is the digamma function. The first two arguments have the same mean as the last two but have half-separation \(a+1\), versus half-separation one. Strict concavity \(\psi''<0\) therefore makes this derivative strictly negative. Using gamma-ratio asymptotics at fixed \(k,a\),
\[
 \lim_{x\to\infty}R_{k,x}
 =\frac{k-1}{k}\frac{\Gamma((k-1)a)^2}{\Gamma((k-2)a)\Gamma(ka)}<1;
\]
the strict inequality follows from log-convexity of \(\Gamma\). Continuity and strict monotonicity provide exactly one root, and the covariance prefactor is positive for \(N\ge2\).

**Critical root and covariance profile.** A useful exact product is
\[
 R_{k,N}=\frac{ka+1}{(k-1)a+1}
 \prod_{j=2}^{N-1}\left(1-
 \frac{a(a+2)}{((k-1)a+j-2)((k-1)a+j)}\right).
\]
Take \(N=\lambda k+b\) with fixed \(\lambda>0\) and bounded real \(b\), using the gamma continuation when necessary. Expanding the logarithm and applying the endpoint-corrected Riemann-sum formula to the smooth functions \((a+t)^{-2}\) and \((a+t)^{-3}\) yields, uniformly for \(\lambda\) in a fixed compact subset of \((0,\infty)\) and bounded \(b\),
\[
 \log R_{k,\lambda k+b}
 =\frac{L_1(\lambda)}{k}+\frac{L_2(\lambda,b)}{k^2}+O_{a,\lambda,b}(k^{-3}),
\]
where
\[
 L_1(\lambda)=\frac{a-(a+1)\lambda}{a+\lambda},\qquad
 L_2(\lambda,b)=-(a+1)+\frac{a(a+2)(a+\tfrac32-b)}{(a+\lambda)^2}.
\]
For completeness, the required expansion of the initial factor is
\[
 \log\frac{ka+1}{(k-1)a+1}
 =\frac1k+\frac{a-2}{2ak^2}+O_a(k^{-3});
\]
the sum extends over indices \(2\le j\le N-1\), so its first endpoint correction is \((b-\tfrac12)/(a+\lambda)^2-3/(2a^2)\). Integrating the leading term gives \(\int_0^\lambda(a+t)^{-2}\,dt=1/a-1/(a+\lambda)\), and integrating the next term gives \(\frac12(1/a^2-1/(a+\lambda)^2)\), which simplify to \(L_1,L_2\) as stated. Uniform Taylor remainders and Euler summation establish the displayed order.

The unique positive zero of \(L_1\) is \(\lambda_a=a/(a+1)\). Monotonicity, the positivity of \(L_1\) below this point, and negativity above it imply \(r_{k,a}/k\to\lambda_a\). At \(\lambda=\lambda_a\),
\[
 L_2(\lambda_a,b)
 =-\frac{(a+1)^2}{a(a+2)}(b-\beta_a),
 \qquad \beta_a=\frac{a+3}{2(a+1)}.
\]
The same expansion at bounded offsets and strict monotonicity then give
\(r_{k,a}=\lambda_a k+\beta_a+O_a(k^{-1})\).

The single-box probabilities converge, when \(N/k\to\lambda>0\), to
\[
 u_\infty=\left(\frac a{a+\lambda}\right)^a,
 \qquad
 v_\infty=u_\infty\frac{a(a+1)}2\left(\frac\lambda{a+\lambda}\right)^2.
\]
At \(\lambda=\lambda_a\), the log-ratio expansion implies
\[
 k^2(R_{k,N}-1)\longrightarrow
 \frac{(a+1)^2}{a(a+2)}(\beta_a-\beta),
\]
and substitution into \(k^2u_{k,N}v_{k,N}(R_{k,N}-1)\) yields \(D_a(\beta_a-\beta)\).

**Exact shape-one case.** When \(a=1\), cancel the rising factorials explicitly:
\[
 R_{k,N}=\frac{(k-2)(k+N-1)}{k(k+N-4)}.
\]
The resulting numerator difference is \(k+2-2N\), proving the all-size threshold formula.

## Verification

The accompanying standalone `verify.py` enumerates Dirichlet–multinomial probabilities over complete finite compositions using exact rational arithmetic. It independently computes \(\operatorname{Cov}(C_0,C_2)\) directly and compares it with the formula in 170 parameter cells, then checks 8,316 rational successive-ratio identities and shape-one specializations. Separately, high-precision gamma calculations confirmed convergence of the continuous crossing offsets for \(a=0.2,0.5,1,2,5\) and \(k=100,400,1000\). These finite checks support, but do not replace, the preceding analytic proof.

Run with `python3 verify.py` using only the Python standard library.

## Relationship to prior work

Keener and Wu, *On Dirichlet Multinomial Distributions* (2006), introduce this exact symmetric mixture and prove a central limit theorem for general occupancy sums, including the first-order covariance scale. Their marginal expansion gives first-order dependence coefficients, so neither the model nor a leading-order covariance limit is claimed as new. The present classification concerns a particular off-diagonal pair of occupancy classes at **every finite sample size**, strict one-crossing in the sample size, and a **constant-order shift** and finite covariance profile precisely where that leading term vanishes. These latter conclusions are not stated in the inspected original paper. Keener, Rothman and Starr (1987) develop earlier partition models, and Griffiths and Spanò (2010 preprint) treat Dirichlet–multinomial polynomial kernels and canonical correlations, not this specific sign classification. Bartroff, Goldstein and Işlak (2014 preprint) prove concentration for related occupancy thresholds, not the mixed covariance sign. Classical independent multinomial allocation has its own occupancy-frequency covariance sign classification; that model is recovered only in the separate limit \(a\to\infty\), not at finite Dirichlet shape. Thus a multinomial one-switch statement does not supply the finite-\(a\) shift or profile. This is a scoped originality assessment, not a guarantee of priority against all historical work.

## Limitations

The statement requires symmetric fixed-shape Dirichlet weights. The root expansion is not uniform across joint limits with varying shape. The exact finite covariance itself is an elementary consequence of classical Dirichlet–multinomial probabilities; any originality attaches only to the complete sign classification and the critical shift/profile. Historical literature on random partitions may imply or contain unlocated related sign statements; the 1987 full text was not accessible during this comparison. No independent audit has been performed.

## References

- R. W. Keener and W. B. Wu, “On Dirichlet Multinomial Distributions” (2006), DOI:10.1142/9789812772558_0008. Author-hosted manuscript: https://www.stat.uchicago.edu/~wbwu/papers/keener.pdf.
- R. W. Keener, E. D. Rothman and N. Starr, “Distributions on Partitions,” *The Annals of Statistics* 15 (1987), 1466–1481, DOI:10.1214/aos/1176350604.
- F. W. Huffer, J. Sethuraman and S. Sethuraman, “A study of counts of Bernoulli strings via conditional Poisson processes,” arXiv:0801.2115 (first submitted 2008-01-14); relevant combinatorial-probability classification and count-mixture context, not a theorem about Dirichlet–multinomial occupancy covariance.
- R. C. Griffiths and D. Spanò, “Orthogonal polynomial kernels and canonical correlations for Dirichlet measures,” arXiv:1003.5131 (first submitted 2010-03-26).
- J. Bartroff, L. Goldstein and Ü. Işlak, “Bounded size biased couplings, log concave distributions and concentration of measure for occupancy models,” arXiv:1402.6769 (first submitted 2014-02-27).
