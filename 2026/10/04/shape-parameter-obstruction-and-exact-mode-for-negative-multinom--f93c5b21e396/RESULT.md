# Shape-parameter obstruction and exact mode for negative-multinomial cells
## Finding
Fix an integer \(d\ge1\), an interior probability vector \(\mathbf{x}=(x_1,\ldots,x_d)\) with \(x_i>0\) and \(q=1-\|\mathbf{x}\|_1\in(0,1)\), and use the standard Gamma extension of the negative-multinomial mass to real shape \(r>0\). For a fixed cell \(\mathbf{k}\in\mathbb{N}_0^d\), write \(m=\|\mathbf{k}\|_1\).

If \(m=0\), the cell probability is \(q^r\), hence it is completely monotone and logarithmically completely monotone on \((0,\infty)\). If \(m\ge1\), the cell probability is strictly log-concave in \(r\), increases on one interval and decreases thereafter, and has a unique maximizer \(r_{m,q}\) determined by
\[
\sum_{j=0}^{m-1}\frac{1}{r_{m,q}+j}=-\log q.
\]
Consequently, every nonzero interior cell fails complete monotonicity in the ordinary shape coordinate and therefore cannot be jointly completely monotone in any parameter system that retains that coordinate. The maximizer depends only on the total count \(m\) and \(q\), not on the composition of \(\mathbf{k}\). For fixed \(q\in(0,1)\),
\[
r_{m,q}=\frac{q}{1-q}m+\frac12-\frac{1-q^2}{24q}m^{-1}+O(m^{-2})
\qquad (m\to\infty).
\]

## Assumptions and scope
The negative-multinomial mass is taken in the form
\[
P_{r,\mathbf{x}}(\mathbf{k})=
\frac{\Gamma(r+m)}{\Gamma(r)\prod_{i=1}^d\Gamma(k_i+1)}
q^r\prod_{i=1}^d x_i^{k_i},
\qquad r>0.
\]
This is the continuous Gamma-form extension of the formula used in the motivating source. The theorem concerns the interior \(x_i>0\), where every cell mass is positive and logarithmic complete monotonicity is well-defined. It does not classify boundary cells with zero probability, nor does it address reparameterizations that eliminate or transform the ordinary shape coordinate.

A positive smooth function \(f\) is completely monotone when \((-1)^n f^{(n)}(r)\ge0\) for every integer \(n\ge0\); it is logarithmically completely monotone when \((-1)^n(\log f)^{(n)}(r)\ge0\) for every integer \(n\ge1\).

## Proof
For fixed \(\mathbf{x}\) and \(\mathbf{k}\), all dependence on \(r\) is
\[
P_{r,\mathbf{x}}(\mathbf{k})=C_{\mathbf{k}}e^{-cr}\frac{\Gamma(r+m)}{\Gamma(r)},
\qquad c=-\log q>0,
\]
where \(C_{\mathbf{k}}>0\) is independent of \(r\).

When \(m=0\), the Gamma ratio is one, so the claim follows from \(q^r=e^{-cr}\).

Now let \(m\ge1\). Since \(m\) is an integer,
\[
\frac{\Gamma(r+m)}{\Gamma(r)}=\prod_{j=0}^{m-1}(r+j).
\]
Writing \(\ell(r)=\log P_{r,\mathbf{x}}(\mathbf{k})\) and discarding the additive constant gives
\[
\ell'(r)=\sum_{j=0}^{m-1}\frac{1}{r+j}-c,
\qquad
\ell''(r)=-\sum_{j=0}^{m-1}\frac{1}{(r+j)^2}<0.
\]
Thus \(\ell'\) is strictly decreasing. Because its \(j=0\) term forces \(\ell'(r)\to+\infty\) as \(r\downarrow0\), while \(\ell'(r)\to-c<0\) as \(r\to\infty\), it has exactly one zero. This proves strict log-concavity, the unique maximizer, and the displayed harmonic equation. In particular, the cell probability is increasing for sufficiently small \(r\), so it is not completely monotone; strict log-concavity also precludes logarithmic complete monotonicity. Any jointly completely monotone function restricts to a completely monotone function on each coordinate line, so this shape-coordinate failure obstructs joint complete monotonicity.

For the asymptotic, put \(a=q/(1-q)\). The mode equation can be written
\[
\psi(r+m)-\psi(r)=-\log q=\log\frac{a+1}{a},
\]
where \(\psi\) is the digamma function. Uniformly for \(r\) proportional to \(m\), the standard expansion
\[
\psi(z)=\log z-\frac{1}{2z}-\frac{1}{12z^2}+O(z^{-4})
\]
shows, after substituting
\[
r=am+\frac12+\frac{b}{m},
\]
that the coefficient of \(m^{-2}\) vanishes exactly for
\[
b=-\frac{2a+1}{24a(a+1)}=-\frac{1-q^2}{24q}.
\]
At this trial point the mode equation has residual \(O(m^{-3})\). Its derivative with respect to \(r\) is
\[
-\sum_{j=0}^{m-1}\frac{1}{(r+j)^2}=-\frac{1}{a(a+1)}m^{-1}+O(m^{-2}),
\]
so the mean-value theorem moves the true root by only \(O(m^{-2})\). This gives the asserted expansion.

## Verification
The proof uses an exact factorization of the Gamma ratio, so uniqueness and the complete-monotonicity obstruction do not depend on numerical testing. The asymptotic coefficient was checked independently by expanding the two digamma terms through order \(m^{-2}\): the coefficient is
\[
-\frac{24a^2b+24ab+2a+1}{24a^2(a+1)^2},
\]
which vanishes at the stated \(b\). Numerical root calculations were used only as stress tests and are not part of the proof.

## Relationship to prior work
Ouimet's 2023 paper gives the negative-multinomial mass above and explicitly asks whether the distribution is completely monotone in its parameters. The same paper points to positive multinomial results. Ouimet's 2018 theorem proves complete monotonicity for a different one-parameter path in which the multinomial total and all cell counts scale simultaneously; its full statement does not fix a cell and vary a negative-multinomial shape parameter. The present theorem therefore identifies a shape-coordinate obstruction specific to the negative-multinomial setting and replaces the proposed monotonicity with a complete one-dimensional profile.

Waller and Zelterman's negative-multinomial likelihood work discusses shape estimation and reports that a shape maximum-likelihood estimate need not exist in their multi-observation log-linear model. That result is not the fixed-cell statement proved here and does not give the harmonic mode equation, composition invariance, or its asymptotic expansion.

## Limitations
The result is deliberately restricted to the ordinary real shape coordinate \(r>0\) with a fixed interior probability vector and a fixed cell. It does not rule out complete monotonicity along specially coupled rays or after nonlinear reparameterization, and it does not classify complete monotonicity in the probability coordinates themselves. The originality comparison cannot exclude an equivalent elementary calculation hidden in unindexed negative-binomial likelihood literature; this is the principal residual literature risk.

## References
1. F. Ouimet, “Moments of the Negative Multinomial Distribution,” *Math. Comput. Appl.* 28 (2023), 85. DOI: 10.3390/mca28040085; first arXiv version: arXiv:2209.04733v1 (2022-09-10).
2. F. Ouimet, “Complete monotonicity of multinomial probabilities and its application to Bernstein estimators on the simplex,” *J. Math. Anal. Appl.* 466 (2018), 1609–1617. arXiv:1804.02108; DOI: 10.1016/j.jmaa.2018.06.049.
3. L. A. Waller and D. Zelterman, “Log-Linear Modeling with the Negative Multinomial Distribution,” *Biometrics* 53 (1997), 971–982. DOI: 10.2307/2533557.
