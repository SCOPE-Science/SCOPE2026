# Rank-one shear obstructions to CPPm on diagonal \(\ell_p\)-sums

## Result

Let \(1\leq p\leq\infty\), let \(Z\neq\{0\}\) be a Banach space, let \(Y\) be a
non-reflexive Banach space, and put
\[
X=Z\oplus_p Y.
\]
For every \(c>0\), choose \(z_0\in S_Z\) and a norm-one functional
\(f\in Y^*\) which does not attain its norm. Define
\[
N_c(z,y)=(c f(y)z_0,0),\qquad T_c=I_X-N_c.
\]
Let
\[
S_{p,c}:\ell_p^2\to\ell_p^2,\qquad S_{p,c}(a,b)=(a+cb,b),
\]
with the usual interpretation for \(p=\infty\), and write
\[
\kappa_p(c)=\|S_{p,c}\|.
\]
Then
\[
\|T_c^{-1}\|=\kappa_p(c),\qquad
m(T_c)=\kappa_p(c)^{-1},
\]
and \(T_c\) does not attain its minimum modulus. Moreover,
\[
\boxed{\ \sup_{K\in\mathcal K(X)}m(T_c+K)=1\ },
\]
and the supremum is attained by the rank-one operator \(K=N_c\), because
\(T_c+N_c=I_X\).

Consequently \((X,X)\) fails the compact perturbation property for the minimum
modulus (CPPm) for every \(1\leq p\leq\infty\). The failure is quantitatively
unbounded:
\[
\frac{\sup_{K\in\mathcal K(X)}m(T_c+K)}{m(T_c)}
=\kappa_p(c)\longrightarrow\infty\qquad(c\to\infty).
\]
For the endpoint norms,
\[
\kappa_1(c)=\kappa_\infty(c)=1+c.
\]

This extends the recent \(\mathbb K\oplus_\infty Y\) obstruction of Raposo and
Ribeiro to every diagonal \(\ell_p\)-sum, allows an arbitrary nonzero complementary
summand \(Z\), and identifies the exact compact-perturbation envelope. It also
covers the diagonal case not supplied by Han's finite-\(p\) direct-sum theorem,
which assumes distinct exponents \(p<q\) in the domain and range.

## Proof

Because \(Y\) is non-reflexive, James' theorem gives
\(f\in S_{Y^*}\) which does not attain its norm. The operator \(N_c\) has rank one
and satisfies \(N_c^2=0\). Hence
\[
T_c^{-1}=I_X+N_c.
\]

First suppose \(1\leq p<\infty\). For \(x=(z,y)\), set
\(a=\|z\|\) and \(b=\|y\|\). Then
\[
\begin{aligned}
\|T_c^{-1}x\|_p
&=\big(\|z+c f(y)z_0\|^p+\|y\|^p\big)^{1/p}\\
&\leq\big((a+cb)^p+b^p\big)^{1/p}\\
&\leq \kappa_p(c)\big(a^p+b^p\big)^{1/p}
=\kappa_p(c)\|x\|_p.
\end{aligned}
\]
Thus \(\|T_c^{-1}\|\leq\kappa_p(c)\).

The norm of the positive \(2\times2\) shear \(S_{p,c}\) is attained at some
nonnegative pair \((a,b)\in S_{\ell_p^2}\). Since
\[
\kappa_p(c)\geq\|(c,1)\|_p=(c^p+1)^{1/p}>1,
\]
every maximizing pair has \(b>0\). Choose \(y_n\in S_Y\), after multiplying by
scalars of modulus one when necessary, so that \(f(y_n)\to1\). Then
\[
x_n=(a z_0,b y_n)\in S_X
\]
and
\[
\|T_c^{-1}x_n\|_p
=\big(|a+cb f(y_n)|^p+b^p\big)^{1/p}
\longrightarrow\kappa_p(c).
\]
Therefore \(\|T_c^{-1}\|=\kappa_p(c)\).

The case \(p=\infty\) is similar but explicit:
\[
\|T_c^{-1}(z,y)\|_\infty
\leq\max\{\|z\|+c\|y\|,\|y\|\}
\leq(1+c)\|(z,y)\|_\infty.
\]
Using \((z_0,y_n)\) as above shows equality, so
\(\kappa_\infty(c)=\|T_c^{-1}\|=1+c\).

We next show that \(T_c^{-1}\) does not attain its norm. For finite \(p\), suppose
a unit vector \(x=(z,y)\) attained \(\kappa_p(c)\). Equality would have to hold
throughout the preceding estimate. The scalar pair
\((\|z\|,\|y\|)\) would therefore maximize the scalar shear norm, so
\(\|y\|>0\). Since the \(\ell_p\)-norm is strictly increasing in each nonnegative
coordinate, equality in
\[
\|z+c f(y)z_0\|\leq \|z\|+c|f(y)|\leq\|z\|+c\|y\|
\]
forces \(|f(y)|=\|y\|\), contradicting the choice of \(f\). For \(p=\infty\),
attainment of \(1+c\) likewise forces
\(|f(y)|=\|y\|=1\), the same contradiction.

For an invertible operator \(T\),
\[
m(T)=\|T^{-1}\|^{-1},
\]
and \(T\) attains its minimum modulus if and only if \(T^{-1}\) attains its norm.
Hence
\[
m(T_c)=\kappa_p(c)^{-1},
\]
and \(T_c\) is not minimum-modulus attaining.

It remains to compute the entire compact-perturbation envelope. Since \(Y\) is
non-reflexive, \(X\) is infinite-dimensional. If \(C\in\mathcal K(X)\), then a
compact operator on an infinite-dimensional Banach space cannot be bounded below.
Thus there are \(u_n\in S_X\) with \(\|Cu_n\|\to0\), and therefore
\[
m(I_X+C)\leq\lim_n\|(I_X+C)u_n\|=1.
\]
For arbitrary \(K\in\mathcal K(X)\),
\[
T_c+K=I_X+(K-N_c),
\]
where \(K-N_c\) is compact, so \(m(T_c+K)\leq1\). Taking \(K=N_c\) gives
\(T_c+K=I_X\), proving
\[
\sup_{K\in\mathcal K(X)}m(T_c+K)=1.
\]

Finally, \(\kappa_p(c)\to\infty\): for \(p<\infty\),
\(\kappa_p(c)\geq(c^p+1)^{1/p}\), while
\(\kappa_\infty(c)=1+c\). This proves the quantitative assertion.

## Relation to the recent literature

Han introduced the CPPm in the current systematic study of weak minimizing
properties. In Theorem 3.4 of arXiv:2601.17316v1, Han proves a direct-sum
obstruction of the form
\[
(X\oplus_p Z,\;Y\oplus_q Z),\qquad 1\leq p<q<\infty,
\]
assuming the existence of a positive-minimum-modulus nonattaining operator
\(X\to Y\). That theorem deliberately uses a gap between the two sum exponents.
It does not cover the diagonal case \(p=q\).

Raposo and Ribeiro subsequently prove in Theorem 2.1 of arXiv:2605.01397v1 that
if
\[
X=\mathbb K\oplus_\infty Y
\]
with \(Y\) non-reflexive, then \((X,X)\) fails CPPm. Their construction is the
\(p=\infty\), scalar-summand, \(c=1\) instance of the shear mechanism above:
\(T(a,y)=(a-f(y),y)\), with a rank-one perturbation returning the identity.

The present statement fills the diagonal finite-\(p\) direct-sum regime, removes
the scalar-summand restriction, and quantifies the failure exactly. In particular,
taking \(Z=\mathbb K\) and \(Y=\ell_1\) gives a rank-one-shear proof of CPPm failure
for every \(\mathbb K\oplus_p\ell_1\), including the classical
\(\ell_1\cong\mathbb K\oplus_1\ell_1\) case.

## Limitations

The theorem gives a structural obstruction for spaces that admit the specified
isometric \(\ell_p\)-sum decomposition. It does not assert that every
non-reflexive Banach space fails CPPm, nor does it characterize CPPm for arbitrary
equivalent renormings or non-complemented subspaces.

Originality is claimed only to the best of our knowledge. The core ingredients
(James' reflexivity theorem, rank-one nilpotent shears, and the elementary fact that
a compact operator on an infinite-dimensional space is not bounded below) are
classical. The claimed contribution is their combination into the all-\(p\)
diagonal CPPm obstruction, together with the exact compact-perturbation envelope
and unbounded quantitative defect.

## References

1. M. Han, *Weak minimizing property on pairs of classical Banach spaces*,
   J. Math. Anal. Appl. 562 (2026), 130716.
   arXiv:2601.17316. https://doi.org/10.1016/j.jmaa.2026.130716
2. A. Raposo Jr. and G. Ribeiro, *Weak Minimizing Property and the Compact
   Perturbation Property for the Minimum Modulus*, arXiv:2605.01397v1 (2026).
   https://arxiv.org/abs/2605.01397
3. R. C. James, *Characterizations of reflexivity*, Studia Math. 23 (1964),
   205--216. https://doi.org/10.4064/sm-23-3-205-216
