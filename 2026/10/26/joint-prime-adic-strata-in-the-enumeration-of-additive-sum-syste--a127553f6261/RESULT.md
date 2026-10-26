# Joint prime-adic strata in the enumeration of additive sum systems

## Finding

Let \(m\geq2\) be fixed. Let \(\mathcal N_m(n)\) count labelled \(m\)-part sum systems of size \(n\): ordered tuples of finite subsets \((A_1,\ldots,A_m)\) of nonnegative integers, with each \(|A_j|\geq2\), such that every integer in \(\{0,\ldots,n-1\}\) has exactly one representation as \(a_1+\cdots+a_m\) with \(a_j\in A_j\). Set \(\mathcal N_m(1)=0\).

Fix a **nonempty finite set \(S\) of primes** and nonnegative integer exponents \((e_p)_{p\in S}\), all independent of \(X\). Define

\[
 Z_S(s)=\zeta(s)\prod_{p\in S}(1-p^{-s}),\qquad
 E=\sum_{p\in S}e_p,\qquad Q_m=\frac{m}{m-1}.
\]

There is a unique \(\rho=\rho_{m,S}>1\) with \(Z_S(\rho)=Q_m\). Set \(\alpha=-Z_S'(\rho)>0\). Then the exact joint prime-exponent stratum has the asymptotic

\[
\boxed{\displaystyle
\sum_{\substack{n\leq X\\ \nu_p(n)=e_p\ (p\in S)}}\mathcal N_m(n)
\sim C_{m,S,\mathbf e}\,X^{\rho}(\log X)^E,\qquad
C_{m,S,\mathbf e}=
\frac{m}{(m-1)^2\rho\alpha}
\prod_{p\in S}\frac{1}{e_p!}
\left(\frac{m p^{-\rho}}{(m-1)\alpha}\right)^{e_p}.
}
\]

All constants are strictly positive and are determined by a unique real root and the derivative of an explicit Euler-factor-deleted zeta function. The formula covers simultaneous constraints at arbitrarily many *fixed* primes, including zero exponents. In particular, if \(r_m>1\) is determined by \(\zeta(r_m)=Q_m\), then \(\rho_{m,S}<r_m\), and

\[
\sum_{n\leq X}\mathcal N_m(n)
\sim \frac{m}{(m-1)^2r_m(-\zeta'(r_m))}\,X^{r_m}.
\]

Consequently, when a sum system is selected uniformly from all labelled \(m\)-part systems with size at most \(X\), its size's \(p\)-adic valuation tends to infinity in probability for every fixed prime \(p\); the joint probability of any fixed finite valuation vector is asymptotic to an explicit constant times \(X^{\rho_{m,S}-r_m}(\log X)^E\).

## Assumptions and scope

Here \(\nu_p(n)\) is the largest exponent of \(p\) in a positive integer \(n\); \(n\) ranges over positive integers. A 'labelled' sum system distinguishes the ordered parts \(A_1,\ldots,A_m\). The primes in \(S\), their exponents, and \(m\) are fixed as \(X\to\infty\). The set \(S\) must be finite and nonempty; no uniformity in the number of restricted primes or in exponents growing with \(X\) is asserted.

For \(\Re s>1\), the expansion \(Z_S(s)=\sum_{\gcd(n,\prod_{p\in S}p)=1}n^{-s}\) gives monotonicity from infinity at \(s\downarrow1\) to \(1\) at \(s\to\infty\), proving the uniqueness of \(\rho\) and the positivity of \(\alpha\).

## Proof

**1. A positive factorization series.** The established bijection between labelled sum systems and joint ordered nontrivial factorizations, followed by the proper-colouring count, gives

\[
\mathcal N_m(n)=\sum_{L\geq m}m!\,S(L-1,m-1)c_L(n),
\]

where \(c_L(n)\) counts ordered factorizations into \(L\) factors at least \(2\), and \(S(\cdot,\cdot)\) is a Stirling number of the second kind. The number of admissible length-\(L\) colour strings may also be verified directly from inclusion-exclusion:

\[
\sum_{j=1}^{m}(-1)^{m-j}\binom mj j(j-1)^{L-1}
=m!S(L-1,m-1).
\]

Thus, with \(T=\zeta(s)-1\), the Dirichlet series is \(H_m(T)\), where the elementary Stirling generating identity gives

\[
H_m(t)=\sum_{L\geq m}m!S(L-1,m-1)t^L
=\frac{m!t^m}{\prod_{j=1}^{m-1}(1-jt)}.
\]

**2. Joint prime marking.** Introduce independent indeterminates \((u_p)_{p\in S}\). The Dirichlet series for one nontrivial factor, with \(u_p\) recording its valuation at \(p\), is

\[
T_S(s,\mathbf u)
= Z_S(s)\prod_{p\in S}(1-u_pp^{-s})^{-1}-1.
\]

Absolute convergence for \(\Re s\) sufficiently large, and then coefficient extraction, gives

\[
F_{\mathbf e}(s):=
\sum_{n\geq1}\frac{\mathcal N_m(n)\,\mathbf1_{\{\nu_p(n)=e_p\ \forall p\in S\}}}{n^s}
=[\prod_{p\in S}u_p^{e_p}]H_m(T_S(s,\mathbf u)).
\]

This is an equality of ordinary Dirichlet coefficients, not a probabilistic independence assumption. The coefficients of \(F_{\mathbf e}\) are nonnegative.

**3. Leading pole and exact constant.** At \(t_*=1/(m-1)\), elementary cancellation in the denominator gives

\[
H_m(t)=\frac{B_m}{t_*-t}+\text{a function analytic at }t_*,\qquad B_m=\frac{m}{(m-1)^2}.
\]

At \(s=\rho\), \(T_S(\rho,\mathbf0)=t_*\). Write \(w=s-\rho\). Taylor expansion at \((\rho,\mathbf0)\) yields

\[
t_*-T_S(s,\mathbf u)
=\alpha w-Q_m\sum_{p\in S}p^{-\rho}u_p
+O\left(w^2+|w|\sum_p|u_p|+\sum_{p,q}|u_pu_q|\right).
\]

The coefficient of \(\prod_pu_p^{e_p}\) in the highest-order polar term is

\[
F_{\mathbf e}(s)
=\frac{K_{\mathbf e}}{w^{E+1}}+O(w^{-E}),\qquad
K_{\mathbf e}=\frac{B_m\,E!}{\alpha^{E+1}}
\prod_{p\in S}\frac{(Q_m p^{-\rho})^{e_p}}{e_p!}.
\]

The factorial \(E!\) counts the ways to distribute the total order of the singular term among different prime markers. Lower-order Taylor terms cannot change the coefficient of \(w^{-(E+1)}\), since each marked variable requires at least one factor of a corresponding first-order term.

**4. The Tauberian boundary condition.** On \(\Re s=\rho\),

\[
|Z_S(s)-1|\leq Z_S(\rho)-1=t_*.
\]

Equality for \(s=\rho+it\) would force the phases of \(q^{-it}\), \(q^{-2it}\), and \(r^{-it}\) to agree for any two distinct primes \(q,r\notin S\). Comparing \(q\) with \(q^2\) forces \(q^{-it}=1\), and then \(r^{-it}=1\), which is impossible for \(t\ne0\) since \(\log q/\log r\) is irrational. Thus the inequality is strict except at \(t=0\). All denominators in \(H_m\) are nonzero away from \(\rho\) on this boundary; coefficient extraction of the locally analytic marked series preserves that property. In particular, \(F_{\mathbf e}\) has no other singularities on the boundary \(\Re s=\rho\).

The **Delange Tauberian theorem for Dirichlet series with nonnegative coefficients** now applies with a unique pole of order \(E+1\) and leading coefficient \(K_{\mathbf e}\), giving

\[
\sum_{n\leq X\atop\nu_p(n)=e_p\,(p\in S)}\mathcal N_m(n)
\sim \frac{K_{\mathbf e}}{\rho\Gamma(E+1)}X^{\rho}(\log X)^E.
\]

Since \(\Gamma(E+1)=E!\), substituting \(K_{\mathbf e}\) proves the displayed constant. This is the precise version of Delange's theorem stated in Section 2 of Hwang–Janson (2009); its nonnegativity, boundary analyticity and polar-expansion hypotheses were checked above.

**5. Unrestricted comparison.** Repeating the unmarked argument with \(T(s)=\zeta(s)-1\) gives the total-system estimate at \(r_m\). Because \(S\ne\varnothing\) and \(Z_S(s)<\zeta(s)\) for real \(s>1\), its root satisfies \(\rho_{m,S}<r_m\). The quotient of the two asymptotics tends to zero. For any fixed finite set of primes and threshold \(B\), a union bound over the finitely many events \(\nu_p(n)<B\) gives joint divergence in probability.

## Verification

The supplied standard-library Python file `verify.py` independently enumerates coloured proper factorization words and the corresponding Stirling-weighted proper-factorization sum for each \(2\leq m\leq4\) and \(1\leq n\leq112\). It also constructs finite Dirichlet-convolution powers and checks equality of coefficients, including extracted simultaneous \(2\)-adic and \(3\)-adic strata for exponents up to \(3\). It terminates with `VERIFY_OK`. These finite checks verify normalization and the marking identity in bounded cases; they do not establish the infinite asymptotics, which follow from the pole computation and Delange's theorem.

As a numerical orientation, for \(m=2\), \(S=\{2,3\}\), the defining root and derivative give \(\rho\approx1.2478072085\), \(\alpha\approx5.2473390415\), and \(C_{2,S,(0,0)}\approx0.3054522860\). The coefficient for \(\mathbf e=(1,1)\), multiplying \(X^{\rho}(\log X)^2\), is approximately \(0.0047439749\). These approximations are illustrative, not proof inputs.

## Relationship to prior work

Huxley–Lettington–Schmidt (2026), Theorem 5.1 and Theorem 5.3, provide the positive factorization formula and the unrestricted Dirichlet series, including its convergence abscissa. Law–Lettington–Schmidt (2025) establish the sum-system/multifactorization correspondence and fixed-size counting formulas. Hwang–Janson (2009) give general Tauberian methods for ordered factorizations and the relevant Delange theorem. In particular, their unrestricted ordered-factorization setting already subsumes the elementary one-prime-free, two-part leading-growth special case. The present claim is the **simultaneous fixed prime-valuation vector law for all labelled part counts**, including its exponent-dependent logarithmic order and explicit factorial-product constant; it does not claim novelty for the cited factorization identity, basic Dirichlet series, or the Tauberian theorem.

## Limitations

The estimate is pointwise in fixed \(m,S,\mathbf e\); it is not uniform for increasing primes, increasing support, or exponents growing with \(X\). There is no effective error bound, local central limit theorem, or independent verification of priority. Earlier ordered-factorization methods make some special cases implicit, and an equivalent joint-strata theorem not located in the inspected literature remains a priority risk.

## References

1. M. N. Huxley, M. C. Lettington, K. M. Schmidt, *On Divisor Function Polynomials and Dirichlet Series*, arXiv:2610.13864v1 (October 9, 2026), especially Theorems 5.1 and 5.3; https://arxiv.org/abs/2610.13864.
2. A. D. Law, M. C. Lettington, K. M. Schmidt, *Multifactorisations and divisor functions*, *Utilitas Mathematica* 125 (2025), 43–60, online December 25, 2025; https://combinatorialpress.com/um-articles/vol-125/multifactorisations-and-divisor-functions/.
3. H.-K. Hwang, S. Janson, *Delange's Tauberian theorem and asymptotic normality of random ordered factorizations of integers*, arXiv:0902.3419 (2009), especially Section 2; https://arxiv.org/abs/0902.3419.
4. H. Delange, *Généralisation du théorème de Ikehara*, *Annales scientifiques de l'École Normale Supérieure* 71 (1954), 213–242.
