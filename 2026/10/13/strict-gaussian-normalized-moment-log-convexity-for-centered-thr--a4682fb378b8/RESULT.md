# Strict Gaussian-normalized moment log-convexity for centered three-exponential sums

## Finding

Let \(E_1,E_2,E_3\) be independent exponential random variables with mean one. For every real coefficient vector \((x_1,x_2,x_3)\ne(0,0,0)\) satisfying \(x_1+x_2+x_3=0\), define \(X=x_1E_1+x_2E_2+x_3E_3\), and let \(G\) be a standard Gaussian random variable. Then the function
\[
R(s)=\frac{\mathbb E|X|^s}{\mathbb E|G|^s}
\]
is **strictly log-convex** for all real \(s\ge2\). In particular, for every \(2\le p<q<\infty\),
\[
\boxed{\quad\frac{\|X\|_p}{\|G\|_p}<\frac{\|X\|_q}{\|G\|_q}\quad}.
\]
This establishes the three-summand, including genuinely asymmetric, case of the Gaussian-normalized \(L_p\)-to-\(L_q\) comparison conjectured in [1, Section 4.2].

## Assumptions and scope

Each \(E_i\) has density \(e^{-t}\mathbf 1_{\{t>0\}}\), and all three are independent. The real coefficients are not all zero and sum to zero; zero individual coefficients are allowed. The norm means \(\|Z\|_s=(\mathbb E|Z|^s)^{1/s}\). All conclusions concern finite real orders \(s\ge2\) and do not require equal magnitudes of the nonzero coefficients.

## Proof

**Step 1: reduction and densities.** Permutation of indices and, if needed, replacement of \(X\) by \(-X\) reduce every admissible coefficient triple to
\[
X=aE_1+bE_2-cE_3,\qquad a\ge b\ge0,\qquad \(c=a+b>0\).
\]
For \(a>b>0\), convolution of the density \((e^{-t/a}-e^{-t/b})/(a-b)\) of \(aE_1+bE_2\) with that of \(-cE_3\) gives, for \(t>0\),
\[
 f_X(t)=\frac{\frac{a}{a+c}e^{-t/a}-\frac{b}{b+c}e^{-t/b}}{a-b},
 \qquad
 f_X(-t)=\frac{c}{(a+c)(b+c)}e^{-t/c}.
\]
The formula extends by continuity to \(b=0\). The coincidence \(a=b\) is the continuous limit of the displayed divided difference.

**Step 2: a positive moment decomposition.** The elementary identity
\[
\frac{d}{du}\left(\frac{u}{u+c}e^{-t/u}\right)
=e^{-t/u}\left(\frac{c}{(u+c)^2}+\frac{t}{u(u+c)}\right),\qquad u,t,c>0,
\]
rewrites the density of \(|X|\) as the manifestly nonnegative expression
\[
 f_{|X|}(t)=\frac{c}{(a+c)(b+c)}e^{-t/c}
 +\frac1{a-b}\int_b^a
 \left(\frac{c}{(u+c)^2}+\frac{t}{u(u+c)}\right)e^{-t/u}\,du.
\]
When \(a=b\), the average integral is replaced by its integrand evaluated at \(u=a\). The case \(b=0\) is taken by continuity; the integrand at \(u=0\) is not needed for \(t>0\). By Tonelli and the Gamma-integral formulas, for every real \(s\ge2\),
\[
\frac{\mathbb E|X|^s}{\Gamma(s+1)}
 =\frac{c^2}{(a+c)(b+c)}c^s
 +\frac1{a-b}\int_b^a \left[
 \frac{cu}{(u+c)^2}+\frac{u}{u+c}(s+1)\right]u^s\,du.
\tag{1}
\]
Again the average-integral convention applies at \(a=b\). The standard Gaussian moment and the Gamma duplication formula yield
\[
 \frac{\Gamma(s+1)}{\mathbb E|G|^s}
 =2^{s/2}\Gamma(1+s/2).
\]
Thus \(R(s)\) is a positive linear combination/integral, with coefficients independent of \(s\), of two types of functions indexed by \(r>0\):
\[
 A_r(s)=2^{s/2}\Gamma(1+s/2)r^s,
 \qquad B_r(s)=(s+1)2^{s/2}\Gamma(1+s/2)r^s.
\tag{2}
\]

**Step 3: strict log-convexity.** With \(\psi_1\) the trigamma function, direct differentiation gives
\[
 (\log A_r)''(s)=\tfrac14\psi_1(1+s/2)>0,
\]
and
\[
 (\log B_r)''(s)=\tfrac14\psi_1(1+s/2)-\frac1{(s+1)^2}
 >\frac1{2(s+2)}-\frac1{(s+1)^2}>0
 \qquad(s\ge2).
\]
For the first strict bound we used \(\psi_1(z)=\sum_{j=0}^{\infty}(j+z)^{-2}>\int_0^\infty(z+t)^{-2}dt=1/z\) for \(z>0\). For the second, \((s+1)^2>2(s+2)\) follows from \(s^2>3\) for \(s\ge2\). Positive integrals and sums of log-convex functions are log-convex by Hölder's inequality, and are strictly so here because every nonzero component in (2) is strictly log-convex. Formula (1) has positive mass because \(c>0\). Consequently \((\log R)''(s)>0\) for all \(s\ge2\). More explicitly, after normalizing (1) by its value, the second derivative is an average of strictly positive component curvatures plus a nonnegative variance of component log-derivatives.

**Step 4: strict cross-exponent comparison.** Let \(v=\operatorname{Var}(X)=a^2+b^2+c^2>0\), and \(Y=X/\sqrt v\). Write \(h(s)=\log(\mathbb E|Y|^s/\mathbb E|G|^s)\). Step 3 gives \(h''(s)>0\), and \(h(2)=0\). The sharp single-order Gaussian moment lower bound for independent exponential sums [1, Theorem 1] applies to the centered variable \(Y\), giving \(h(s)\ge0\) for all \(s\ge2\); hence its right derivative obeys \(h'(2)\ge0\). Define \(D(s)=s h'(s)-h(s)\). Then \(D(2)=2h'(2)\ge0\) and \(D'(s)=s h''(s)>0\) for every \(s>2\). Therefore
\[
\frac{d}{ds}\left(\frac{h(s)}s\right)=\frac{D(s)}{s^2}>0\qquad(s>2).
\]
Because \(\exp(h(s)/s)=\|Y\|_s/\|G\|_s\), the claimed strict inequality follows for \(Y\) and, on multiplying by \(\sqrt v\), for \(X\). \(\square\)

## Verification

A standalone standard-library script, `verification/check_moments.py`, independently computes integer even moments from the moment-generating-function expansion
\[
\prod_{j=1}^3(1-x_jz)^{-1}=\sum_{k\ge0}\frac{\mathbb E X^k}{k!}z^k
\]
and compares them by exact rational arithmetic with the integrated density formula. It checks variance, mass normalization, the published single-order Gaussian lower bound at sampled orders, and the exact elementary curvature bound. Numerical curvature spot-checks test noninteger orders. The script passes 2,647 assertions; the proof of the continuum statement is analytic, not numerical.

For exact moment replay, one may also use
\[
\frac{\mathbb E|X|^k}{k!}=
\frac{\frac{a^{k+2}}{a+c}-\frac{b^{k+2}}{b+c}}{a-b}
+\frac{c^{k+2}}{(a+c)(b+c)},
\]
for even integers \(k\ge0\) when \(a>b\), with the quotient interpreted as a derivative when \(a=b\).

## Relationship to prior work

Brazitikos, Tang and Tkocz [1, Section 4.2] explicitly conjecture the Gaussian-normalized two-exponent comparison for every mean-zero weighted sum of exponentials, and suggest log-convexity of its Gaussian-normalized moment quotient. Their Theorem 1 supplies the one-exponent Gaussian lower bound used in Step 4, but alone does not compare the ratios at two distinct orders. Their symmetric paired-coefficient case follows from Gaussian scale mixtures; a three-term vector with \(a,b>0\) and \(-a-b\) is not of that paired form.

Brazitikos and Pandis [2, Sections 2.5 and 5] provide a general moment interpolation formula and determine extremal coefficient configurations for several regimes of three-summand moments under a zero-sum and variance constraint. The divided-difference moment identity above is consistent with their interpolation formula and is **not** claimed as a new standalone formula. Their fixed-order extremal assertions do not supply strict log-convexity across all real moment orders for each asymmetric coefficient vector or the resulting universal two-order comparison. Melbourne, Roysdon, Tang and Tkocz [3] study different moment ranges and normalizations for centered log-concave laws, rather than the stated two-exponent Gaussian comparator.

## Limitations

The assertion is restricted to at most three independent rate-one exponential variables with a mean-zero coefficient sum; it does not establish the conjecture for four or more summands. It does not claim the Gaussian comparison below order \(2\), nor a classification for general independent non-exponential summands. Earlier unindexed equivalent results in exponential moment theory remain a possible priority limitation.

## References

[1] S. Brazitikos, C. Tang, T. Tkocz, *Moments of sums of exponentials, beyond CHS*, arXiv:2602.03058v1 (first posted 3 February 2026), Theorem 1 and Section 4.2. https://arxiv.org/html/2602.03058v1

[2] S. Brazitikos, C. Pandis, *Sharp inequalities for symmetric polynomials, Hunter's conjecture, and moments of exponential random variables*, arXiv:2512.12254v1 (2025), Sections 2.5 and 5, including Proposition 5.3. https://arxiv.org/pdf/2512.12254

[3] J. Melbourne, M. Roysdon, C. Tang, T. Tkocz, *From simplex slicing to sharp reverse Hölder inequalities*, arXiv:2505.00944 (2025), Theorems 1–2. https://arxiv.org/pdf/2505.00944
