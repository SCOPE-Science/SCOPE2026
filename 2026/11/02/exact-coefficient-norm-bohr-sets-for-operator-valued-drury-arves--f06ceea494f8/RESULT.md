# Exact coefficient-norm Bohr sets for operator-valued Drury–Arveson multipliers

## Finding

Let \(d\) be any positive integer or \(d=\infty\), the latter meaning countably many variables. Write \(\mathbb B_d\) for the open unit ball of \(\mathbb C^d\) or \(\ell^2\), and let \(H_d^2\) denote the Drury–Arveson space with kernel
\[
K(z,w)=\frac{1}{1-\langle z,w\rangle}.
\]
For an operator-valued multiplier \(F(w)=\sum_\alpha A_\alpha w^\alpha\), normalized by \(\|M_F\|\le1\) and \(F(0)=0\), define its *coefficient-norm majorant* by
\[
\mathfrak B_F(z)=\sum_{\alpha\ne0}\|A_\alpha\|\,|z^\alpha|\in[0,\infty].
\]
The following exact pointwise identity holds, including possible divergence on the right:
\[
\boxed{\sup_{\|M_F\|\le1,\ F(0)=0}\mathfrak B_F(z)
=\mathcal S_d(z):=\sum_{\alpha\ne0}\sqrt{\frac{|\alpha|!}{\alpha!}}\,|z^\alpha|.}
\]
The supremum can be taken over all operator-valued multipliers on one fixed separable infinite-dimensional coefficient Hilbert space. One diagonal contractive multiplier attains the identity simultaneously at every point where the sum is finite. Consequently, the exact zero-anchored coefficient-norm Bohr set is
\[
\boxed{\{z\in\mathbb B_d:\mathcal S_d(z)\le1\}.}
\]

The formula has three consequences. For \(d=1\), \(\mathcal S_1(z)=|z|/(1-|z|)\), so the sharp zero-anchored operator-valued radius is \(1/2\), not the scalar radius \(1/\sqrt2\). For \(d\ge2\) the Bohr set is not a Euclidean ball: the axial point \((2/5,0,\ldots)\) belongs, but the equal-norm point \((\sqrt2/5,\sqrt2/5,0,\ldots)\) does not. For \(d=\infty\), no centered Euclidean ball of positive radius is contained in the Bohr set, even restricting to finite-support test points.

If the normalization \(F(0)=0\) is removed and the constant operator coefficient is included in the majorant, the corresponding universal operator-valued Bohr set is exactly \(\{0\}\); a \(2\times2\) diagonal multiplier witnesses failure at every nonzero point.

## Assumptions and scope

A multiindex \(\alpha\) is a finitely supported tuple of nonnegative integers; \(|\alpha|=\sum_j\alpha_j\), \(\alpha!=\prod_j\alpha_j!\), and \(z^\alpha=\prod_j z_j^{\alpha_j}\). Let \(\mathcal I_d^+\) be the countable collection of all nonzero multiindices. A coefficient Hilbert space \(\mathcal E\) is arbitrary; a multiplier \(F\) takes values in \(\mathcal B(\mathcal E)\) and \(M_F\) acts by pointwise multiplication on \(H_d^2\otimes\mathcal E\). Contractivity is **multiplier-norm**, not merely pointwise supremum-norm, contractivity. The coefficient-norm majorant sums the norms of the individual multiindex coefficients; it is neither the norm of the coefficient sum nor the majorant formed from norms of homogeneous polynomial blocks. These distinct conventions are not interchangeable.

For finite \(d\), the series defining \(\mathcal S_d\) converges at every point of \(\mathbb B_d\). For \(d=\infty\), the series is interpreted as an extended nonnegative sum; both finite values and infinite values are covered. For a fixed finite matrix size, the formula is always an upper bound, while its exact supremum over *all* matrix sizes is the displayed value. The single equality witness uses the separable Hilbert space \(\ell^2(\mathcal I_d^+)\).

## Proof

**1. Vacuum coefficient bounds.** The normalized monomials
\[
e_\alpha(w)=\sqrt{\frac{|\alpha|!}{\alpha!}}\,w^\alpha
\]
form an orthonormal basis of \(H_d^2\). If \(\|M_F\|\le1\), apply \(M_F\) to the constant vector function with value a unit vector \(v\in\mathcal E\). Orthogonality yields
\[
\sum_\alpha \frac{\alpha!}{|\alpha|!}\|A_\alpha v\|^2
=\|F(\cdot)v\|_{H_d^2\otimes\mathcal E}^2\le1.
\]
Therefore, for every \(\alpha\),
\[
\|A_\alpha\|\le\sqrt{\frac{|\alpha|!}{\alpha!}}.
\]
Summing these independent bounds gives \(\mathfrak B_F(z)\le\mathcal S_d(z)\).

**2. Each normalized monomial is contractive as a multiplier.** Fix \(\alpha\) with \(n=|\alpha|\) and test \(M_{e_\alpha}\) on the orthonormal monomial basis \(e_\beta\) with \(m=|\beta|\). Its squared shift weight is exactly
\[
\|e_\alpha e_\beta\|_{H_d^2}^2
=\frac{\prod_j\binom{\alpha_j+\beta_j}{\alpha_j}}{\binom{n+m}{n}}\le1.
\]
The inequality is the elementary multivariate Vandermonde identity: the numerator is one nonnegative term in the expansion of the denominator
\[
\binom{n+m}{n}
=\sum_{|\gamma|=n}\prod_j\binom{\alpha_j+\beta_j}{\gamma_j}.
\]
Terms with impossible binomial arguments are zero. The same identity holds in countably many variables because \(\alpha+\beta\) has finite support. Distinct basis vectors \(e_\beta\) are shifted to distinct basis vectors \(e_{\alpha+\beta}\); hence the operator norm is the supremum of the weights, at most one. The vacuum \(\beta=0\) has weight one. Thus \(\|M_{e_\alpha}\|=1\) for every multiindex, including the constant monomial.

**3. Simultaneous attainment.** On \(\mathcal E=\ell^2(\mathcal I_d^+)\), define
\[
F_\star(w)=\operatorname{diag}\big(e_\alpha(w)\big)_{\alpha\in\mathcal I_d^+}.
\]
By Step 2, its multiplication operator is a direct sum of norm-one scalar multipliers, so \(\|M_{F_\star}\|=1\). It has zero constant coefficient. Its degree-\(n\) block has norm at most \(\|w\|_2^n\), by the multinomial formula, so its operator-valued Taylor series converges locally in operator norm. For each \(\alpha\ne0\), its Taylor coefficient is the diagonal rank-one operator with norm \(\sqrt{|\alpha|!/\alpha!}\). Consequently \(\mathfrak B_{F_\star}(z)=\mathcal S_d(z)\), proving equality. When the sum diverges, finite diagonal truncations produce arbitrarily large majorants, giving the same extended supremum without interpreting infinity as an ordinary finite number.

**4. Finite-dimensional convergence and geometric consequences.** Cauchy–Schwarz and the multinomial theorem give, with \(r=\|z\|_2<1\),
\[
\sum_{|\alpha|=n}\sqrt{\frac{n!}{\alpha!}}|z^\alpha|
\le\sqrt{\binom{n+d-1}{d-1}}\,r^n
\]
for finite \(d\), proving convergence. On a coordinate axis, \(\mathcal S_d(z)=r/(1-r)\). At \(r=2/5\), the degree-one through degree-four contribution for \(z=(\sqrt2/5,\sqrt2/5,0,\ldots)\) is
\[
\frac{2\sqrt2}{5}+\frac{4+2\sqrt2}{25}
+\frac{4\sqrt2+4\sqrt6}{125}
+\frac{24+4\sqrt6}{625}
>\frac{3148}{3125}>1,
\]
using \(\sqrt2>7/5\) and \(\sqrt6>12/5\). The coordinate-axis point of the same Euclidean radius has majorant \(2/3\), proving nonradiality. In countably many variables, take \(N\) coordinates equal to \(r/\sqrt N\): the degree-one part is \(r\sqrt N>1\) for any fixed \(r>0\) and sufficiently large \(N\), so no positive Euclidean-radius ball works.

**5. Unrestricted constant coefficient.** The same coefficient bounds hold at \(\alpha=0\). If \(z_j\ne0\), choose \(F(w)=\operatorname{diag}(1,w_j)\), a contractive \(2\times2\) multiplier with coefficient-norm majorant \(1+|z_j|>1\). At \(z=0\) the bound is \(\|F(0)\|\le1\). Therefore the unrestricted matrix-valued Bohr set is \(\{0\}\).

## Verification

The accompanying `CHECKER.py` verifies the exact Vandermonde weight inequality as rational arithmetic over every nonzero multiindex of total degree at most six in dimensions one through four, paired with all test multiindices of degree at most six. It also verifies exact rational values for the \(2\times2\) one-variable witness, finite truncations of the nonradial example, and small-radius dimension-collapse witnesses. It passed 52,012 finite assertions. These checks supplement, rather than replace, Steps 1–5; in particular they do not certify any infinite-dimensional statement by enumeration.

A direct finite-matrix witness is \(F(w)=\operatorname{diag}(w,w^2)\) on the disk. It is a contractive matrix-valued Hardy (equivalently one-variable Drury–Arveson) multiplier with \(F(0)=0\), yet at \(r=2/3<1/\sqrt2\) its coefficient-norm majorant is
\[
\mathfrak B_F(2/3)=\frac23+\frac49=\frac{10}{9}>1.
\]

## Relationship to prior work

Brevig, Seip, and Zlotnikov (2026) identify the scalar-valued coefficient Bohr set of Drury–Arveson multipliers as the Euclidean ball of radius \(1/3\), using complete Pick kernels. The present statement concerns **operator-valued coefficient norms** and the zero-at-origin normalization. Diagonal independent coefficient channels prevent scalar Cauchy–Schwarz control from extending to the sum of separate operator norms. In fact, the same matrix-valued coefficient-norm convention with no zero normalization has only the origin as a universal Bohr set.

Allu and Halder (2021/2022, Lemma 2.2 and Theorem 2.2) state a \(1/\sqrt2\) zero-constant radius for bounded operator-valued functions when the majorant sums homogeneous operator norms. The displayed \(2\times2\) example satisfies the stated disk hypotheses and shows that this bound does not hold for the full stated operator class. Their general multidimensional setting also differs from the contractive Drury–Arveson multiplier setting. The exact factorial-weighted pointwise set obtained here is not furnished by that assertion.

Bhowmik and Das (2020), in contrast, study the *operator-order* majorant \(\sum |A_n|r^n\le I\), which is not \(\sum\|A_n\|r^n\le1\). Their results do not imply the latter, as orthogonal diagonal projections illustrate. Popescu's noncommutative polyball Bohr bounds likewise apply to norms of free homogeneous evaluations; they do not identify the coefficientwise commutative Drury–Arveson pointwise profile proved here.

## Limitations

No sharp claim is made for a *fixed* finite matrix dimension; the exact supremum is for arbitrary coefficient dimensions and is attained on a separable infinite-dimensional coefficient Hilbert space. No assertion is made about matrix-valued functions that are only pointwise contractive but fail to be contractive Drury–Arveson multipliers. The exact set uses individual multiindex coefficient norms, not sums of operator absolute values and not block-homogeneous norms. The historical numerical-radius, operator-order, and free-variable Bohr quantities are distinct. Publication priority remains subject to full independent literature assessment; no independent mathematical audit has been performed.

## References

1. O. F. Brevig, K. Seip, and I. Zlotnikov, *Bohr sets for multiplier algebras of complete Pick spaces*, arXiv:2609.26395 (first posted 2026-09-22), https://arxiv.org/abs/2609.26395.
2. V. Allu and H. Halder, *Operator valued analogues of multidimensional Bohr's inequality*, arXiv:2111.11713, Canadian Mathematical Bulletin 65 (2022), 1020–1035, https://arxiv.org/abs/2111.11713.
3. B. Bhowmik and N. Das, *Bohr phenomenon for operator valued functions with fixed initial coefficient*, arXiv:2003.05810, https://arxiv.org/abs/2003.05810.
4. G. Popescu, *Bohr inequalities for free holomorphic functions on polyballs*, arXiv:1709.01375, Advances in Mathematics 347 (2019), 1002–1053, https://arxiv.org/abs/1709.01375.
5. G. Popescu, *Multivariable Bohr inequalities*, arXiv:math/0507156, https://arxiv.org/abs/math/0507156.
