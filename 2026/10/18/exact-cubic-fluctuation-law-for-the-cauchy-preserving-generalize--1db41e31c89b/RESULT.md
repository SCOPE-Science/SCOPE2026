# Exact cubic fluctuation law for the Cauchy-preserving generalized Boole map

## Finding

Let \(0<\alpha<1\) and \(\beta>0\), and let the real rational map be
\[
T_{\alpha,\beta}(x)=\alpha x-\frac{\beta}{x}.
\]
Use the invariant Cauchy probability \(\mu_s(dx)=s\,dx/[\pi(x^2+s^2)]\), where \(s=\sqrt{\beta/(1-\alpha)}\). Let \(X\sim\mu_s\), and define the bounded, centered observable and its stationary sums by
\[
\phi(x)=\frac{x^2-s^2}{x^2+s^2},\qquad Y_j=\phi(T_{\alpha,\beta}^{\circ j}(X)),\qquad S_N=\sum_{j=0}^{N-1}Y_j.
\]
The map is defined for almost every point and its iterates are defined almost surely. Put \(t=2\alpha-1\in(-1,1)\), and for integers \(m\ge1\) put
\[
c_m=(1+t)t^{m-1}(1-t^m),
\]
with the usual polynomial interpretation \(t^0=1\), including at \(t=0\).

**The complete second- and third-order correlation laws are**
\[
\mathbb E[Y_iY_j]=\frac{t^{|j-i|}}2\quad(i,j\ge0),
\qquad
\mathbb E[Y_iY_jY_k]=\frac14t^{j-i}c_{k-j}\quad(0\le i\le j<k).
\]
Third moments with the latest time repeated, \(i<j=k\), and third moments with all three times equal, vanish. Consequently, at every integer \(N\ge1\),
\[
\operatorname{Var}(S_N)=\frac N2+\sum_{d=1}^{N-1}(N-d)t^d,
\]
\[
\kappa_3(S_N)=\frac34\sum_{q=1}^{N-1}(N-q)c_q
+\frac32\sum_{\substack{p,q\ge1\\p+q<N}}(N-p-q)t^pc_q.
\]
Here \(\kappa_3\) is the centered third cumulant; it equals \(\mathbb E[S_N^3]\). In particular, the exact asymptotic coefficients are
\[
\boxed{\lim_{N\to\infty}\frac{\operatorname{Var}(S_N)}N=\frac{1+t}{2(1-t)}=\frac{\alpha}{2(1-\alpha)}}
\]
and
\[
\boxed{\lim_{N\to\infty}\frac{\kappa_3(S_N)}N=\frac{3(1+t)}{4(1-t)^2}=\frac{3\alpha}{8(1-\alpha)^2}.}
\]
Equivalently, the normalized skewness has the precise first-order law
\[
\lim_{N\to\infty}\sqrt N\,\frac{\kappa_3(S_N)}{\operatorname{Var}(S_N)^{3/2}}
=\frac{3}{\sqrt{2(1-t^2)}}=\frac{3}{2\sqrt{2\alpha(1-\alpha)}}.
\]
The cubic coefficient tends to zero linearly as \(\alpha\downarrow0\) but diverges quadratically as \(\alpha\uparrow1\), although the previously known Lyapunov exponent tends to zero at **both** boundaries. The exact cubic law and its asymmetric critical behavior are the substantive claim; the second-order formula is provided to normalize the third cumulant and to identify its relation to existing general covariance theory.

## Assumptions and scope

All expectations refer to the invariant Cauchy initial distribution. The result is for the specific natural bounded rational observable \(\phi\), not for arbitrary observables. No claim about moments of the unbounded original Cauchy coordinate is made. The boundary parameters \(\alpha=0\) and \(\alpha=1\) are not included: the limits displayed above are one-sided limits of coefficients with \(0<\alpha<1\) held fixed before \(N\to\infty\). The scale \(\beta\) changes the invariant Cauchy width but cancels from these standardized-observable cumulants.

## Proof

**1. Exact conjugacy and stationarity.** Set \(u=x/s\) and introduce the Cayley coordinate \(z=(u-i)/(u+i)\), where the \(i\) here is the imaginary unit. Under the Cauchy probability of \(u\), \(z\) is uniformly distributed on the unit circle \(\partial\mathbb D\). A direct rational simplification gives the degree-two finite Blaschke map
\[
B_t(z)=z\frac{z+t}{1+tz},\qquad B_t(0)=0,\qquad t=2\alpha-1.
\]
For real \(|t|<1\), this map sends the unit circle to itself. Every analytic polynomial \(p\) satisfies
\[
\int_{\partial\mathbb D}p(B_t(z))\,dm(z)=p(B_t(0))=p(0)
=\int_{\partial\mathbb D}p(z)\,dm(z),
\]
by the mean-value formula; applying the same identity to conjugate polynomials and then using trigonometric density proves that \(B_t\) preserves normalized arc measure \(m\). Moreover, \(\phi(x)=\operatorname{Re}z\). Thus it suffices to set \(b_n=B_t^{\circ n}\) (with \(b_0(z)=z\)) and \(Y_n=\operatorname{Re}b_n(z)\) with \(z\sim m\). In particular, \(\mathbb E Y_n=0\), and every \(b_n\) has boundary modulus one and zero constant Taylor coefficient.

**2. Iterated Taylor coefficient.** The expansion at the origin is
\[
B_t(w)=tw+(1-t^2)w^2+O(w^3).
\]
Write \(b_m(w)=t^mw+c_mw^2+O(w^3)\). Composition yields \(c_{m+1}=tc_m+(1-t^2)t^{2m}\), starting with \(c_1=1-t^2\). Summing the resulting finite geometric series proves
\[
c_m=(1+t)t^{m-1}(1-t^m)
\]
for every integer \(m\ge1\), including \(t=0\) under polynomial evaluation. Also write \(b_m(w)=w H_m(w)\), where \(H_m(0)=t^m\) and \(H_m'(0)=c_m\).

**3. The two-point function.** For \(j>i\), stationarity permits replacing \(b_i\) by a uniformly distributed variable \(w\); then \(b_j=b_{j-i}(b_i)\). The analytic terms \(\int b_i b_j\,dm\) and their conjugates vanish. The remaining term is
\[
\int b_i\overline{b_j}\,dm
=\int w\,\overline{b_{j-i}(w)}\,dm(w)=t^{j-i},
\]
by extraction of the coefficient of \(w\). Since \(Y=(b+\overline b)/2\), this gives \(\mathbb E[Y_iY_j]=t^{j-i}/2\); the diagonal has variance \(1/2\).

**4. The three-point function.** Fix \(0\le i\le j<k\), and put \(m=k-j\). Because \(b_k=b_jH_m(b_j)\) and \(|b_j|=1\) on the circle,
\[
\int b_i b_j\overline{b_k}\,dm
=\int b_i\overline{H_m(b_j)}\,dm.
\]
Replacing \(b_i\) by the uniform variable \(w\), the integrand becomes \(w\overline{H_m(b_{j-i}(w))}\). Its integral is the coefficient of \(w\) in the analytic function \(H_m(b_{j-i}(w))\), namely \(c_m t^{j-i}\). In the expansion of \(8Y_iY_jY_k\), the other mixed types vanish: \(b_i\overline{b_j}b_k=b_iH_m(b_j)\) is analytic with zero constant term; likewise \(\overline{b_i}b_jb_k\) reduces to an analytic expression with zero constant term because \(b_j/b_i\) is analytic for \(j\ge i\). Terms containing three analytic factors or three conjugate factors also have zero integral. Exactly the term just computed and its conjugate survive, giving
\[
\mathbb E[Y_iY_jY_k]=\frac14c_{k-j}t^{j-i}.
\]
If \(j=k>i\), then \(b_j\overline{b_j}=1\) and all remaining analytic mixed terms have zero integral, so the third moment vanishes. For \(i=j=k\), \(b_i\) is uniform and its real part has zero third moment.

**5. Exact sums and limits.** Because \(\mathbb E Y_j=0\), the variance is the sum of all pair correlations. For the third cumulant, triples with the smallest index repeated have three permutations, while triples with three distinct indices have six; triples with their latest index repeated contribute zero. This produces precisely the two finite sums in the Finding section. For fixed \(|t|<1\), all sums below converge absolutely and
\[
\sum_{q\ge1}c_q=\frac{1}{1-t},\qquad
\sum_{p\ge1}t^p=\frac{t}{1-t}.
\]
Dividing the finite sums by \(N\), dominated convergence gives the two displayed limiting coefficients. The positive variance coefficient permits normalization, yielding the stated skewness law. Finally, substituting \(t=2\alpha-1\) gives the explicit endpoint scalings.

## Verification

The accompanying `verify.py` is standalone Python code. Running `python verify.py` returns `VERIFY_OK`. It checks exact rational Taylor recurrences for several rational parameters and all orders through fifteen, compares two independent combinatorial organizations of the exact finite third-cumulant sum, and separately computes Haar-circle quadrature of pair/triple correlations and of cumulants for three parameters and observation horizons up to seven. The complete proof above, rather than those finite checks, establishes the identities for all permitted real parameters and all integer horizons.

## Relationship to prior work

Umeno and Okubo (first public manuscript 2015-10-29, arXiv:1510.08569; journal version 2016) established the Cauchy invariant density, mixing-phase picture, and exact Lyapunov exponent \(\log(1+2\sqrt{\alpha(1-\alpha)})\). None of these antecedents is claimed as new. Nicolau's work on iterates of inner functions and the subsequent general central limit theorem of Nicolau and Soler i Gibert give the general covariance/normalization and Gaussian-limit framework for boundary iterates of an inner function fixing the origin. In particular, the *second-order* covariance here is a direct specialization of that existing theory. The present claim is instead the closed, finite-horizon **third** correlation/cumulant law for the generalized Boole family and its asymmetric two-endpoint scaling; the inspected sections of these works do not state that law or an equivalent coefficient. General inner-function correlation estimates do not by themselves specify this coefficient, though an equivalent derivation elsewhere remains a bibliographic risk.

## Limitations

The result does not show a uniform central limit theorem as \(\alpha\) approaches a boundary simultaneously with \(N\to\infty\), and its normalized-skewness coefficient is not a quantitative normal-approximation error bound. It concerns the canonical Cayley-real observable only; it does not classify arbitrary bounded observables or all higher cumulants. Numerical quadrature is verification support, not an infinite proof. A general Blaschke-product result not found in the examined literature may already imply the particular third-order law; originality therefore remains subject to independent bibliographic assessment. No independent audit has been performed.

## References

1. K. Umeno and K.-i. Okubo, *Exact Lyapunov exponents of the generalized Boole transformations*, arXiv:1510.08569 (initial public submission 2015-10-29), journal version *Progress of Theoretical and Experimental Physics* **2016**, 021A01, DOI:10.1093/ptep/ptv195. https://arxiv.org/abs/1510.08569
2. A. Nicolau, *Convergence of linear combinations of iterates of an inner function*, arXiv:2103.07238 (2021), *Journal de Mathématiques Pures et Appliquées* **161** (2022), 135–165, DOI:10.1016/j.matpur.2022.03.003. https://arxiv.org/abs/2103.07238
3. A. Nicolau and O. Soler i Gibert, *The Central Limit Theorem for inner functions II*, arXiv:2305.02042 (2023), especially Theorem 1, equation (1.2), and Lemma 4. https://arxiv.org/abs/2305.02042
