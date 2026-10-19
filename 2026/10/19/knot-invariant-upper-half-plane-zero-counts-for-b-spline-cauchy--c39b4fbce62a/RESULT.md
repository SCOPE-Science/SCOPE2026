# Knot-invariant upper-half-plane zero counts for B-spline Cauchy transforms

## Finding
Let \(n\geq1\) and let \(a_0<\cdots<a_n\) be any real knots. Let \(B_a\) be the nonnegative probability-normalized Curry–Schoenberg B-spline determined by these \(n+1\) knots (the pushforward of uniform probability on the \(n\)-simplex by the affine map \((u_j)\mapsto\sum_{j=0}^n a_j u_j\)). For every integer \(m\geq0\), define
\[
F_{n,m}(z)=\int_{a_0}^{a_n}\frac{B_a(x)}{(z-x)^{n+m+1}}\,dx,\qquad \operatorname{Im}z>0.
\]
The number of zeros of \(F_{n,m}\) in the open upper half-plane, **counted with their analytic multiplicities**, is exactly
\[
\boxed{N_+(n,m)=n\lfloor m/2\rfloor.}
\]
The answer is independent of all knot spacings. If \(m\) is even, the real rational continuation has no real zero. If \(m\) is odd, its real zeros are exactly \(n\) simple points, one in each interval \((a_j,a_{j+1})\), and none outside the extreme knots. The knot positions are poles, never canceled zeros. Consequently the transforms are zero-free in the upper half-plane for \(m=0,1\), and increasing \(m\) by two adds exactly \(n\) upper-half-plane zeros, counted with multiplicity.

## Assumptions and scope
The knots are strictly increasing and finite; \(n\) and \(m\) are arbitrary integers in the specified ranges. The spline is normalized to integrate to one, not the alternate partition-of-unity convention. Analytic multiplicity applies to zeros in \(\operatorname{Im}z>0\); real-root assertions apply to the meromorphic rational continuation across the real axis away from the knots. The wavelet-type Cauchy kernel order is precisely \(n+m+1\); the result does not concern general non-spline windows or arbitrary independently chosen kernel orders below \(n+1\). No individual nonreal zero is asserted simple.

## Proof
Put \(P(z)=\prod_{j=0}^n(z-a_j)\) and \(R(z)=1/P(z)\). For \(f_z(t)=(z-t)^{-1}\), the Hermite–Genocchi formula identifies the divided difference \(f_z[a_0,\ldots,a_n]\) with the normalized simplex average of \((z-X)^{-(n+1)}\), because \(f_z^{(n)}(t)=n!(z-t)^{-(n+1)}\). Direct partial fractions yield \(f_z[a_0,\ldots,a_n]=1/P(z)\). Thus \(F_{n,0}=R\). Differentiating \(m\) times under the integral, which is valid off the compact support, gives the exact identity
\[
F_{n,m}(z)=\frac{(-1)^m n!}{(n+m)!}\,R^{(m)}(z).
\]
Define the rational numerator polynomial
\[
Q_m(z)=\frac{(-1)^m}{m!}P(z)^{m+1}R^{(m)}(z).
\]
For example, \(Q_0=1\), and differentiating the defining equation gives the polynomial recurrence
\[
Q_{m+1}(z)=P'(z)Q_m(z)-\frac{P(z)Q_m'(z)}{m+1}.
\]
Since \(R(z)=z^{-n-1}(1+O(z^{-1}))\) as \(|z|\to\infty\), the leading coefficient of \(Q_m\) is \(\binom{n+m}{m}\), and \(\deg Q_m=nm\). Near a knot \(a_j\), the leading principal part of \(R\) is \(1/[P'(a_j)(z-a_j)]\), hence
\[
Q_m(a_j)=P'(a_j)^m\ne0.
\]
Therefore every zero of \(R^{(m)}\), and hence of \(F_{n,m}\), is a zero of \(Q_m\) and there is no pole cancellation.

Now fix real \(x\notin\{a_0,\ldots,a_n\}\), and put \(w_j=(x-a_j)^{-1}\). Expanding the product of geometric series \(\prod_j(1-w_jt)^{-1}\) proves
\[
R^{(m)}(x)=(-1)^m m!\,R(x)\,h_m(w_0,\ldots,w_n),
\]
where \(h_m\) is the complete homogeneous symmetric polynomial of degree \(m\), with \(h_0=1\). For strict positivity of every even-degree expression, take independent mean-one exponential variables \(E_0,\ldots,E_n\). Their moment-generating function gives
\[
(2k)!h_{2k}(w_0,\ldots,w_n)
=\mathbb E\bigl(\sum_j w_jE_j\bigr)^{2k}>0
\]
for all \(k\ge1\), because \((w_j)\ne0\); for \(k=0\), \(h_0=1\). Thus every even derivative \(R^{(2k)}\) has the same nonzero sign as \(R\) on every real pole-complement interval. In particular, no even derivative has real zeros.

For odd \(m\), \(R^{(m+1)}\) is even order and nonzero on every such interval, so \(R^{(m)}\) is strictly monotone between successive poles. Its leading behavior near \(a_j\) is
\[
R^{(m)}(x)\sim\frac{(-1)^m m!}{P'(a_j)(x-a_j)^{m+1}}.
\]
As \(m+1\) is even and \(P'(a_j)P'(a_{j+1})<0\), the endpoint infinities have opposite signs. By continuity and strict monotonicity there is exactly one real zero in \((a_j,a_{j+1})\), and it is simple. For \(x<a_0\) or \(x>a_n\), all \(w_j\) have one common strict sign, hence all monomials of \(h_m(w)\) have one nonzero sign and the derivative cannot vanish. This proves exactly \(n\) real zeros if \(m\) is odd, and zero if \(m\) is even.

The polynomial \(Q_m\) has real coefficients, degree \(nm\), and no roots at the knots. Its remaining roots occur in conjugate pairs, with algebraic multiplicity preserved. When \(m\) is even, the upper-half-plane count is \(nm/2\). When \(m\) is odd, it is \((nm-n)/2\). Both expressions equal \(n\lfloor m/2\rfloor\), completing the proof.

## Verification
The accompanying standalone `checker.py` uses exact rational and integer polynomial arithmetic. Its `checker_output.txt` records 28 passing tests, covering four distinct knot configurations, dimensions \(1\) through \(4\), and derivative orders \(0\) through \(6\). For each case it verifies polynomial degree, exact noncancellation at all knots, the real-root count, the one-per-gap property in odd order, and the induced conjugate-pair census using exact root isolation. This finite test is supplementary; the arbitrary-knots and all-orders theorem is proved above.

## Relationship to prior work
The spline probability normalization and divided-difference integration are classical: the Hermite–Genocchi formula is explicitly presented in Baxter and Brummelhuis [1]. The key nonvanishing fact for even complete homogeneous polynomials is attributed to Hunter and discussed by Böttcher, Garcia, Omar and O'Neill [2]. These are treated as established ingredients, not new discoveries. Langley [3] studies nonreal zeros of higher derivatives of reciprocals of real entire functions, but its stated growth-theoretic conclusions do not provide this finite arbitrary-real-knot exact census. Mallat and Waldspurger [4] explain why zero sets of analytic Cauchy wavelet transforms and associated Blaschke factors matter to phase recovery; that work does not state the present B-spline zero count. The contribution here is the complete two-parameter, knot-independent zero census and the boundary parity classification for the explicitly normalized B-spline Cauchy family, not a claim to have introduced the underlying positivity theorem or Cauchy transform identities.

## Limitations
The nonreal zeros are counted with multiplicity and need not have a proved simplicity or geometric localization law. The result does not determine their individual positions, handle repeated knots, extend to general positive pulse trains or wavelets, or establish new phase-retrieval stability estimates. The proof uses classical identities and may have an equivalent formulation in older rational-function literature; independent publication-priority evaluation is outstanding. Exact checker outputs are not a substitute for the analytic proof.

## References
[1] B. J. C. Baxter and R. Brummelhuis, *Functionals of Exponential Brownian Motion and Divided Differences*, arXiv:1006.1996v1 (10 June 2010), Theorem 4.2.

[2] A. Böttcher, S. R. Garcia, M. Omar and C. O'Neill, *Weighted Means of B-Splines, Positivity of Divided Differences, and Complete Homogeneous Symmetric Polynomials*, arXiv:2001.01658v2 (2020), §§1–2.

[3] J. K. Langley, *The reciprocal of a real entire function and non-real zeros of higher derivatives*, Ann. Acad. Sci. Fenn. Math. 38 (2013), 855–871, DOI:10.5186/aasfm.2013.3847.

[4] S. Mallat and I. Waldspurger, *Phase retrieval for the Cauchy wavelet transform*, arXiv:1404.1183v1 (2014).
