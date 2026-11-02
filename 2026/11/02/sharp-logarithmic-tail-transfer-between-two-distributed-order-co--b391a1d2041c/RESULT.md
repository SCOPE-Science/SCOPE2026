# Sharp logarithmic tail transfer between two distributed-order convolution quadratures

## Finding

Let \(w:[0,1]\to[0,\infty)\) be integrable and suppose that, for some \(c>0\) and \(\alpha>-1\),
\[
w(1-t)\sim c\,t^{\alpha}\qquad(t\downarrow0).
\]
For the distributed-order fractional-integral symbol
\[
F_w(s)=\int_0^1w(\beta)s^{-\beta}\,\mathrm d\beta,
\]
let \(e_n\) and \(b_n\) be the *uncorrected* unit-step convolution-quadrature weights of backward Euler and BDF2:
\[
\sum_{n\ge0}e_nz^n=F_w(1-z),\qquad
\sum_{n\ge0}b_nz^n=F_w\!\left(\frac{(1-z)(3-z)}2\right).
\]
Write \(d_n=b_n-e_n\). Then, as \(n\to\infty\),
\[
 e_n\sim\frac{c\Gamma(\alpha+1)}{(\log n)^{\alpha+1}},\qquad
 d_n\sim\frac{c\Gamma(\alpha+2)}{2n(\log n)^{\alpha+2}}>0.
\]
Moreover \(\sum_{n\ge0}|d_n|<\infty\), \(\sum_{n\ge0}d_n=0\), and
\[
\sum_{j=0}^{n}(e_j-b_j)
\sim\frac{c\Gamma(\alpha+1)}{2(\log n)^{\alpha+1}},\qquad
\lim_{n\to\infty}\frac{\sum_{j=0}^{n}(e_j-b_j)}{e_n}=\frac12.
\]
The initial weight difference is strictly negative:
\[
d_0=\int_0^1w(\beta)\bigl((2/3)^\beta-1\bigr)\,\mathrm d\beta<0.
\]
Thus BDF2 shifts weight away from the initial coefficient into an eventually positive, logarithmically slow long-memory tail, conserving the total weight *difference*. For the uniform density \(w\equiv1\), this specializes to
\[
d_0=\frac1{3\log(3/2)}-1,\qquad
d_n\sim\frac1{2n(\log n)^2},\qquad
\sum_{j=0}^{n}(e_j-b_j)\sim\frac1{2\log n}.
\]

## Assumptions and scope

The order density \(w\) is an ordinary nonnegative integrable function, not an atomic measure; \(\alpha>-1\), \(c>0\), and the endpoint equivalence is meant for almost every sufficiently small \(t>0\). The timestep equals one, and no BDF2 starting correction is included. The indices are integers \(n\ge0\). Both generating functions are initially understood for \(|z|<1\) using the analytic branch inherited from positive real arguments; their coefficients equal the integral over orders of the corresponding fractional CQ coefficients. No PDE solution or finite-time error claim is made.

## Proof

**1. Coefficient factorization.** For \(0<\beta\le1\), set
\[
a_n(\beta)=\frac{(\beta)_n}{n!}=\frac{\Gamma(n+\beta)}{\Gamma(\beta)\Gamma(n+1)},\quad n\ge0.
\]
The backward-Euler fractional coefficient is \(a_n(\beta)\). Since
\[
\frac{(1-z)(3-z)}2=(1-z)\frac32(1-z/3),
\]
the BDF2 fractional coefficient is
\[
B_n(\beta)=\sum_{k=0}^n p_k(\beta)a_{n-k}(\beta),\qquad
p_k(\beta)=\left(\frac23\right)^\beta\frac{(\beta)_k}{3^k k!}.
\]
These \(p_k\) form a probability distribution on nonnegative integers, as their generating function equals \((2/3)^\beta(1-z/3)^{-\beta}\). Its mean is \(\beta/2\), and its second moment is \((3\beta+\beta^2)/4\). For \(0<\beta\le1\), \(p_k(\beta)\le3^{-k}\) and \(0<a_n(\beta)\le1\).

**2. Uniform fractional-weight comparison.** For \(0\le k\le n/4\), the exact ratio is
\[
\frac{a_{n-k}(\beta)}{a_n(\beta)}
=\prod_{j=0}^{k-1}\frac{n-j}{n-j-1+\beta}
=1+\frac{(1-\beta)k}{n}
 +O\!\left(\frac{(1-\beta)(k+k^2)}{n^2}\right),
\]
where the implied constant is uniform for \(0<\beta\le1\) and large \(n\). This follows by expanding \(\log(1+(1-\beta)/(n-j-1+\beta))\), summing, and exponentiating, with \(k/n\le1/4\). The part \(k>n/4\) of either coefficient convolution is bounded in absolute value by \(O(3^{-n/5})\), uniformly in \(\beta\), using the geometric tail and \(a_m\le1\). The corresponding omitted probability moments obey the same bound, after enlarging the exponential constant. Consequently,
\[
B_n(\beta)-a_n(\beta)
=\frac{\beta(1-\beta)}{2n}a_n(\beta)
+O\!\left(\frac{\beta(1-\beta)}{n^2}a_n(\beta)+3^{-n/5}\right).
\]
The identity is also valid at the endpoints by continuity, with the exponentially small term accounting for \(\beta=1\).

**3. Order integration and sharp coefficients.** Uniform Gamma-ratio asymptotics give
\[
a_n(\beta)=\frac{n^{\beta-1}}{\Gamma(\beta)}\bigl(1+O(n^{-1})\bigr),\quad0<\beta\le1.
\]
Put \(L=\log n\), \(t=1-\beta\). The assumptions and \(\Gamma(1-t)\to1\) imply, by endpoint Laplace integration,
\[
\int_0^1w(\beta)a_n(\beta)\,\mathrm d\beta
\sim c\int_0^\infty t^\alpha e^{-Lt}\,\mathrm dt
=\frac{c\Gamma(\alpha+1)}{L^{\alpha+1}},
\]
and
\[
\int_0^1w(\beta)\beta(1-\beta)a_n(\beta)\,\mathrm d\beta
\sim\frac{c\Gamma(\alpha+2)}{L^{\alpha+2}}.
\]
The uniform remainder from step 2 integrates to a term negligible relative to \(1/(nL^{\alpha+2})\). Hence the two asserted coefficient asymptotics and eventual strict positivity hold.

**4. Exact mass-difference cancellation.** The established asymptotic yields absolute summability of \(d_n\), since \(\alpha+2>1\). With \(t=1-z\downarrow0\),
\[
\sum_{n\ge0}d_nz^n
=\int_0^1w(\beta)t^{-\beta}\bigl((1+t/2)^{-\beta}-1\bigr)\,\mathrm d\beta.
\]
The absolute value is at most \(\frac12\int_0^1w(\beta)t^{1-\beta}\,\mathrm d\beta\to0\), by dominated convergence (the endpoint \(\beta=1\) has zero measure). Abel's limit and absolute summability therefore imply \(\sum d_n=0\). Since \(d_n\sim C/[n(\log n)^{\alpha+2}]\), the integral test yields
\[
\sum_{j>n}d_j\sim\frac{c\Gamma(\alpha+1)}{2(\log n)^{\alpha+1}},
\]
which equals \(\sum_{j=0}^n(e_j-b_j)\) by cancellation. Dividing by the asymptotic formula for \(e_n\) gives the universal ratio \(1/2\). The strict sign of \(d_0\) follows from positive \(w\)-mass near \(\beta=1\).

## Verification

Run `python3 verify.py` in the same directory. The standalone program evaluates the uniform-order coefficient differences at seven finite indices using Simpson order integration, independently checks the fractional BDF2 recurrence against its coefficient convolution, and tests large-index logarithmic scaling. These are supplementary finite calculations; the proof above establishes the infinite-index conclusions.

## Relationship to prior work

Ren and Su, *Stability and Error Estimates for Convolution Quadrature under Radial Symbol Bounds* (arXiv:2610.23163, first public October 16, 2026), develop radial-symbol bounds, weight estimates and numerical convergence tests for distributed-order CQ; their distributed-order sections treat the same uniform-order symbol and BE/BDF2 discretizations. The work does not present the paired coefficient-difference asymptotic or the conserved difference/finite-prefix law. Yin, Liu, Li and Zhang, *Approximation methods for the distributed order calculus using the convolution quadrature* (first public May 15, 2020, DOI 10.3934/dcdsb.2020168), introduce general distributed-order CQ constructions and convergence/correction theory; the inspected text does not establish the sharp paired asymptotic or the universal endpoint-density law. Lubich's foundational work provides the underlying CQ and fractional-weight framework. The theorem here derives its own uniform coefficient comparison and order-endpoint asymptotics rather than inferring a sharp constant from generic error bounds.

## Limitations

Only uncorrected convolution coefficients are compared; BDF2 initial-value corrections can alter early effective weights. This says nothing about the sign of every individual \(d_n\): positivity is proved only for all sufficiently large indices. Neither positive definiteness of a discretized PDE nor accuracy advantages for arbitrary inputs follow. The proof assumes a nonnegative order density with a power-law endpoint at order one; atomic order measures, signed densities, and endpoint behavior outside this class are not classified. Broader historical priority remains subject to specialist literature review.

## References

1. J. Ren and H. Su, *Stability and Error Estimates for Convolution Quadrature under Radial Symbol Bounds*, arXiv:2610.23163v1 (2026), https://arxiv.org/abs/2610.23163 ; detailed distributed-order sections checked in v2, https://arxiv.org/html/2610.23163v2 .
2. B. Yin, Y. Liu, H. Li and Z. Zhang, *Approximation methods for the distributed order calculus using the convolution quadrature*, Discrete Contin. Dyn. Syst. B 26 (2021), 1447–1468; first online May 15, 2020, https://doi.org/10.3934/dcdsb.2020168 .
3. C. Lubich, *Discretized fractional calculus*, SIAM J. Math. Anal. 17 (1986), 704–719, https://doi.org/10.1137/0517050 .
4. C. Lubich, *Convolution quadrature and discretized operational calculus. I*, Numer. Math. 52 (1988), 129–145, https://doi.org/10.1007/BF01398686 .
