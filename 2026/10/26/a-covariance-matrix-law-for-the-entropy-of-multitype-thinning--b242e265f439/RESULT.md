# A covariance-matrix law for the entropy of multitype thinning

## Finding
Let \(d\ge2\) be fixed. For a bounded random vector of nonnegative integer event counts \(X=(X_1,\ldots,X_d)\), with strictly positive coordinate means \(\lambda_i\), the leading relative-entropy cost of sparse, independently marked multitype aggregation is an exact squared norm of its second factorial-cumulant matrix. Set
\[
D=\operatorname{diag}(\lambda_1,\ldots,\lambda_d),\qquad K=\operatorname{Cov}(X)-D.
\]
For the thinned aggregate \(Y_n\) defined below and \(Q=\bigotimes_i\operatorname{Poi}(\lambda_i)\),
\[
\lim_{n\to\infty}n^2D_{\mathrm{KL}}(\mathcal L(Y_n)\Vert Q)
=\frac14\left\|D^{-1/2}KD^{-1/2}\right\|_F^2
=\sum_i\frac{K_{ii}^2}{4\lambda_i^2}
 +\sum_{i<j}\frac{K_{ij}^2}{2\lambda_i\lambda_j}.
\]
The sharper dependence-specific statement is
\[
\boxed{\displaystyle\lim_{n\to\infty}n^2 I(Y_{n1};\ldots;Y_{nd})
=\frac12\sum_{i<j}\frac{\operatorname{Cov}(X_i,X_j)^2}{\lambda_i\lambda_j},}
\]
where \(I(Y_{n1};\ldots;Y_{nd})\) is the multivariate total correlation, namely relative entropy to the product of the actual marginals. Thus the leading information shared between event types is determined only by pairwise count covariances; higher-order dependence affects smaller terms. This is an exact leading-order limit, not merely a bound.

For the explicit dependent two-type count \(X=(Z,Z)\), \(\Pr(Z=0)=\Pr(Z=2)=1/2\), both coordinate means and variances equal one. Every thinned marginal is exactly equidispersed at every \(n\), yet
\[
I(Y_{n1};Y_{n2})=\frac{1+o(1)}{2n^2},\qquad
D_{\mathrm{KL}}(\mathcal L(Y_{ni})\Vert\operatorname{Poi}(1))=O(n^{-4}).
\]
Hence the first detectable entropy discrepancy is joint dependence, not either individual Poisson fit.

## Assumptions and scope
Fix an integer \(d\ge2\) and a finite upper bound \(B\ge1\). Assume \(X\in\{0,1,\ldots,B\}^d\) almost surely; its coordinates may have any joint law, including complete dependence. Suppose \(\lambda_i=\mathbb EX_i>0\). For each positive integer \(n\), take \(n\) independent copies \(X^{(a)}\). Given these copies, retain each of the \(X_i^{(a)}\) units of type \(i\), independently across all units, coordinates and copies, with probability \(1/n\). Let \(Y_{ni}\) be the total retained count of type \(i\). No assumption that different coordinates of \(X\) are independent is made. Natural logarithms are used throughout. Write \(P_n=\mathcal L(Y_n)\), \(Q=\bigotimes_{i=1}^d\operatorname{Poi}(\lambda_i)\), and \(I(P_n)=D_{\mathrm{KL}}(P_n\Vert\bigotimes_i(P_n)_i)\). The notation \(\|\cdot\|_F\) denotes Frobenius norm. All limits keep \(d,B\), and the distribution of \(X\), fixed.

## Proof
**1. The uniform first signed correction.** Write \(F(z)=\mathbb E\prod_i z_i^{X_i}\), an entire polynomial, and \(w_i=z_i-1\). Coordinatewise Bernoulli thinning and independence of the \(n\) copies give the entire probability generating function
\[
P_n(z)=F(1+w/n)^n,\qquad Q(z)=\exp\!\left(\sum_i\lambda_iw_i\right).
\]
At the all-ones vector, the mixed second derivatives of \(\log F\) equal \(K_{ij}\): they are \(\operatorname{Cov}(X_i,X_j)\) off the diagonal, and \(\operatorname{Var}(X_i)-\lambda_i\) on it. Taylor expansion therefore yields locally uniformly on \(\mathbb C^d\),
\[
n(P_n(z)-Q(z))\longrightarrow\frac12Q(z)\sum_{i,j}K_{ij}w_iw_j.\tag{1}
\]

To justify subsequent summation over the unbounded state space, the convergence in (1) can be made uniform in a weighted coefficient norm. Put \(S=\sum_i|w_i|\). Since \(F(1+w/n)=1+(\lambda\cdot w)/n+O(S^2/n^2)\), one may choose a fixed \(\varepsilon>0\) such that the analytic logarithm is defined whenever \(S\le\varepsilon n\), and
\[
\big|n\log F(1+w/n)-\lambda\cdot w\big|\le CS^2/n.
\]
Using \(S^2/n\le\varepsilon S\) then gives \(n|P_n(z)-Q(z)|\le CS^2e^{CS}\) in that region. In the complementary region, boundedness of \(X\) implies \(|F(1+w/n)|\le e^{BS/n}\), so \(|P_n(z)|\le e^{BS}\) and \(|Q(z)|\le e^{CS}\). There \(n\le S/\varepsilon\). Combining the regions, increasing constants if needed, gives for **all** complex \(z\) and **all** integers \(n\ge1\):
\[
 n|P_n(z)-Q(z)|\le C(1+\textstyle\sum_i|z_i|)^2
                    \exp\!\left(C\textstyle\sum_i|z_i|\right).\tag{2}
\]
For a multiindex \(k=(k_1,\ldots,k_d)\), apply the multivariate Cauchy coefficient bound to (2) on circles of radii \(R_i=1+k_i/(C+1)\). Using \(k_i!\le k_i^{k_i}\) for \(k_i>0\), one obtains fixed constants \(A,C'>0\) such that
\[
 n|P_n\{k\}-Q\{k\}|\le C'(1+|k|)^2\frac{A^{|k|}}{\prod_i k_i!}.\tag{3}
\]
Here \(|k|=\sum_i k_i\); the estimate remains true for coordinates \(k_i=0\) by the corresponding radius choice. Dividing (3) by the everywhere-positive product-Poisson mass \(q(k)=e^{-\sum\lambda_i}\prod_i\lambda_i^{k_i}/k_i!\), we obtain a dominating envelope
\[
 n\left|\frac{P_n\{k\}}{q(k)}-1\right|\le C''(1+|k|)^2
       \prod_i\left(\frac A{\lambda_i}\right)^{k_i}.\tag{4}
\]
The right side belongs to \(L^2(Q)\), by Poisson exponential moments. This is a genuine global summable bound, not merely a fixed-coordinate asymptotic.

**2. Coefficients and quadratic entropy.** Let the monic Charlier polynomials be \(C_1(k;\lambda)=k-\lambda\) and \(C_2(k;\lambda)=(k-\lambda)^2-k\). They obey
\[
\sum_{k\ge0}\operatorname{Poi}(\lambda)\{k\}\frac{C_r(k;\lambda)}{\lambda^r}z^k
=(z-1)^re^{\lambda(z-1)},\quad r=1,2,
\]
and \(\mathbb E[C_r(N;\lambda)C_s(N;\lambda)]=\mathbf1_{r=s}\,r!\lambda^r\) for \(N\sim\operatorname{Poi}(\lambda)\). Comparing coefficients in (1) gives
\[
 n\left(\frac{P_n\{k\}}{q(k)}-1\right)\longrightarrow h(k):=
\frac12\sum_i\frac{K_{ii}}{\lambda_i^2}C_2(k_i;\lambda_i)
+\sum_{i<j}\frac{K_{ij}}{\lambda_i\lambda_j}
 C_1(k_i;\lambda_i)C_1(k_j;\lambda_j).
\]
The terms in this expression are pairwise orthogonal in \(L^2(Q)\), so
\[
\mathbb E_Qh^2
=\frac12\sum_i\frac{K_{ii}^2}{\lambda_i^2}
 +\sum_{i<j}\frac{K_{ij}^2}{\lambda_i\lambda_j}.
\]
For \(r\ge0\), set \(\phi(r)=r\log r-r+1\), with continuous value \(\phi(0)=1\). The exact inequality \(0\le\phi(r)\le(r-1)^2\) and the expansion \(\phi(1+t)=t^2/2+o(t^2)\), together with (4), permit dominated convergence:
\[
 n^2D_{\mathrm{KL}}(P_n\Vert Q)
 =\mathbb E_Q\!\left[n^2\phi(P_n/q)\right]
 \longrightarrow\tfrac12\mathbb E_Qh^2.
\]
This proves the claimed squared-Frobenius formula.

**3. Cancellation of individual fit errors.** For each marginal separately, the same argument gives
\[
 n^2D_{\mathrm{KL}}((P_n)_i\Vert\operatorname{Poi}(\lambda_i))
 \longrightarrow\frac{K_{ii}^2}{4\lambda_i^2}.
\]
The exact information decomposition
\[
D_{\mathrm{KL}}(P_n\Vert Q)
 =I(P_n)+\sum_iD_{\mathrm{KL}}((P_n)_i\Vert\operatorname{Poi}(\lambda_i))
\]
then cancels every diagonal contribution, leaving precisely \(\tfrac12\sum_{i<j}K_{ij}^2/(\lambda_i\lambda_j)\). Because \(K_{ij}=\operatorname{Cov}(X_i,X_j)\) for \(i\ne j\), the dependence formula follows.

**4. A dependence-only witness.** Let \(X=(Z,Z)\), where \(Z=0\) or \(2\) equiprobably. Then \(\lambda_1=\lambda_2=1\), \(\operatorname{Var}(Z)=1\), and
\[
K=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
The general theorem gives \(n^2 I(P_n)\to1/2\). For each marginal the count generating polynomial of \(Z\) is \(F_0(1+t)=1+t+t^2/2\), whose logarithm is \(t+O(t^3)\) with vanishing quadratic coefficient. Repeating the growth-and-coefficient argument leading to (3) with the first nonzero discrepancy multiplied by \(n^2\) proves a uniform \(L^2(\operatorname{Poi}(1))\) bound on \(n^2(p_{ni}/q_i-1)\); hence \(D_{\mathrm{KL}}((P_n)_i\Vert\operatorname{Poi}(1))=O(n^{-4})\). Alternatively, the exact marginal second factorial moment equals \(1\) for every \(n\), whereas the joint covariance equals \(1/n\). This completes the example.

## Verification
A standalone standard-library program, `check.py`, computes the finite joint law by conditioning on the number of nonzero input copies. It verifies 24 exact-rational cross-covariance and equidispersion identities, the Charlier polynomial moment identities, normalized probabilities, and sample joint and marginal KL values for six finite sizes. In particular, at \(n=64\), it obtains \(n^2D_{\mathrm{KL}}(P_n\Vert Q)\approx0.497973\), versus the proved limit \(1/2\); at the same size it obtains \(n^4D_{\mathrm{KL}}((P_n)_1\Vert\operatorname{Poi}(1))\approx0.083423\). These finite computations support but do not establish the limiting assertions; those depend on the analytic argument above.

Run with a standard Python interpreter: `python3 check.py` from the directory containing both files. The script has no third-party dependencies. The finite calculation has rounding at very small cell probabilities and does not certify arbitrary \(n\).

## Relationship to prior work
Kavvadias, *Thinning Operation via the Poisson–Föllmer Process* (first posted August 3, 2026, arXiv:2608.02927), analyzes entropy and rates for **scalar** thinning by a Poisson–Föllmer method (not the multitype covariance-matrix constant). Harremoës, Johnson and Kontoyiannis (2010), *Thinning, Entropy, and the Law of Thin Numbers*, develops scalar information convergence and Poisson–Charlier expansions; Sections V–VI give scalar chi-square asymptotics, entropy comparisons and convergence rates. These results motivate the use of orthogonal Poisson polynomials but do not state the displayed multitype total-correlation law.

B. Roos (1998/1999), *Metric Multivariate Poisson Approximation of the Generalized Multinomial Distribution*, gives a multivariate Charlier expansion and **total variation/point-distance** bounds for sums of vectors each taking values in \(\{0,e_1,\ldots,e_d\}\). That exclusive-one-category summand model differs from arbitrary vector count clusters with simultaneously nonzero coordinates. Roos (2017), *Refined total variation bounds in the multivariate and compound Poisson approximation*, treats more general convolutions but provides total-variation estimates rather than the exact Shannon-information coefficient. These works are relevant to the signed expansion, not direct assertions of this KL or total-correlation limit. An older 1999 multivariate Poisson paper by Roos concerns total-variation bounds and second-order signed approximations; its full text was not available during this comparison, so historical priority remains a residual risk. No absence-of-prior-work claim is inferred solely from a failed search.

## Limitations
The theorem fixes dimension and bounds the original count vector; growing dimension and unbounded original counts are not treated. The term given is only the leading quadratic coefficient; if all cross covariances vanish, total correlation is \(o(n^{-2})\) but need not be zero or have a universal higher-order decay without extra assumptions. The example's \(O(n^{-4})\) marginal entropy estimate does not assert its precise nonzero fourth-order constant. Historical novelty has not been independently certified and could be affected by inaccessible older multivariate approximation results. Independent validation has not been performed.

## References
1. I. Kavvadias, *Thinning Operation via the Poisson–Föllmer Process*, arXiv:2608.02927 (first submitted 2026-08-03), https://arxiv.org/abs/2608.02927.
2. P. Harremoës, O. Johnson, and I. Kontoyiannis, *Thinning, Entropy, and the Law of Thin Numbers*, IEEE Transactions on Information Theory 56 (2010), 4228–4244, DOI:10.1109/TIT.2010.2053893, https://www.dpmms.cam.ac.uk/~ik355/PAPERS/UBthin.pdf.
3. B. Roos, *Metric Multivariate Poisson Approximation of the Generalized Multinomial Distribution*, Theory of Probability and Its Applications 43 (1999), 306–316, DOI:10.1137/S0040585X97976921, https://www.mathnet.ru/eng/tvp1480.
4. B. Roos, *Refined total variation bounds in the multivariate and compound Poisson approximation*, ALEA 14 (2017), 337–360, DOI:10.30757/ALEA.v14-19, https://alea.impa.br/articles/v14/14-19.pdf.
5. B. Roos, *On the Rate of Multivariate Poisson Convergence*, Journal of Multivariate Analysis 69 (1999), 120–134 (abstract inspected; full text unavailable), https://ideas.repec.org/a/eee/jmvana/v69y1999i1p120-134.html.
