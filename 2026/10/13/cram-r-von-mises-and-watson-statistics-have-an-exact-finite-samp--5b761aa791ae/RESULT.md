# Cramér–von Mises and Watson statistics have an exact finite-sample correlation

## Finding

Let \(X_1,\ldots,X_n\) be iid from a fully specified continuous distribution \(F_0\), and write \(F_n\) for the empirical distribution function. Define the one-sample Cramér–von Mises statistic
\[
W_n^2
=
n\int_{\mathbb R}\bigl(F_n(x)-F_0(x)\bigr)^2\,dF_0(x),
\]
and the Watson statistic
\[
U_n^2
=
W_n^2
-
n\left(
\frac1n\sum_{i=1}^nF_0(X_i)-\frac12
\right)^2.
\]

For every integer \(n\ge2\),
\[
\boxed{
\operatorname{Cov}(W_n^2,U_n^2)
=
\frac{n-1}{180n}.
}
\tag{1}
\]

The exact marginal variances are
\[
\boxed{
\operatorname{Var}(W_n^2)
=
\frac{4n-3}{180n},
\qquad
\operatorname{Var}(U_n^2)
=
\frac{n-1}{360n}.
}
\tag{2}
\]
Therefore
\[
\boxed{
\operatorname{Corr}(W_n^2,U_n^2)
=
\sqrt{\frac{2(n-1)}{4n-3}}.
}
\tag{3}
\]

The correlation is strictly increasing in \(n\), from
\[
\sqrt{\frac25}
\]
at \(n=2\), and satisfies
\[
\boxed{
\operatorname{Corr}(W_n^2,U_n^2)\longrightarrow\frac1{\sqrt2}.
}
\tag{4}
\]

Thus Watson centering removes a substantial but exactly quantifiable component of the Cramér–von Mises fluctuation: even asymptotically the two classical quadratic goodness-of-fit statistics retain correlation \(1/\sqrt2\), rather than becoming equivalent or independent.

## Assumptions and scope

The null distribution \(F_0\) is fully specified and continuous. By the probability integral transform,
\[
Y_i=F_0(X_i)
\]
are iid uniform random variables on \([0,1]\), so all formulas are distribution-free under the simple continuous null.

The normalization is the classical one in which
\[
W_n^2
=
n\int_0^1\bigl(F_n^{Y}(t)-t\bigr)^2\,dt.
\]
The Watson statistic is the centered quadratic functional displayed above.

The theorem does not cover fitted-parameter nulls, two-sample statistics, or modifications that change the empirical-process covariance kernel.

## Proof

Put
\[
Z_y(t)=\mathbf 1\{y\le t\}-t,
\qquad
S_n(t)=\frac1{\sqrt n}\sum_{i=1}^nZ_{Y_i}(t).
\]
Then
\[
W_n^2=\|S_n\|_{L^2[0,1]}^2.
\]
Let \(e(t)\equiv1\), let \(P=I-e\otimes e\) be orthogonal projection off the constants, and note that
\[
\langle S_n,e\rangle
=
\sqrt n\left(\frac12-\overline Y\right).
\]
Hence
\[
U_n^2=\langle S_n,PS_n\rangle.
\tag{5}
\]

We use the following exact quadratic-form identity. If \(Z_1,\ldots,Z_n\) are iid centered Hilbert-space random elements with covariance operator \(\Sigma\), and
\[
S_n=n^{-1/2}\sum_{i=1}^nZ_i,
\]
then for bounded self-adjoint operators \(A,B\),
\[
\operatorname{Cov}
\bigl(\langle S_n,AS_n\rangle,\langle S_n,BS_n\rangle\bigr)
=
2\left(1-\frac1n\right)
\operatorname{tr}(A\Sigma B\Sigma)
+
\frac1n
\operatorname{Cov}
\bigl(\langle Z,AZ\rangle,\langle Z,BZ\rangle\bigr).
\tag{6}
\]
Equation (6) follows by expanding the four sample indices. Terms with an index appearing only once vanish by centering; the two cross-pairings produce the trace term, while the all-equal index produces the one-observation covariance.

For the uniform empirical bridge,
\[
C(s,t)
=
\mathbb E[Z_Y(s)Z_Y(t)]
=
\min(s,t)-st.
\]
Consequently
\[
\operatorname{tr}(\Sigma^2)
=
\int_0^1\!\!\int_0^1 C(s,t)^2\,ds\,dt
=
\frac1{90}.
\tag{7}
\]
Moreover,
\[
(\Sigma e)(t)
=
\int_0^1C(t,s)\,ds
=
\frac{t(1-t)}2,
\]
so
\[
\|\Sigma e\|^2=\frac1{120},
\qquad
\langle e,\Sigma e\rangle=\frac1{12}.
\tag{8}
\]

Since \(P=I-e\otimes e\),
\[
\operatorname{tr}(\Sigma P\Sigma)
=
\frac1{90}-\frac1{120}
=
\frac1{360},
\tag{9}
\]
and
\[
\operatorname{tr}(\Sigma P\Sigma P)
=
\frac1{90}-\frac2{120}+\frac1{144}
=
\frac1{720}.
\tag{10}
\]

The one-observation quadratic forms simplify unusually strongly. For \(Y=y\),
\[
\|Z_y\|^2
=
\frac{y^3+(1-y)^3}{3}
=
\left(y-\frac12\right)^2+\frac1{12},
\tag{11}
\]
whereas
\[
\langle Z_y,PZ_y\rangle
=
\|Z_y\|^2-\langle Z_y,e\rangle^2
=
\frac1{12}
\tag{12}
\]
is deterministic. Thus
\[
\operatorname{Var}(\langle Z,IZ\rangle)
=
\operatorname{Var}\left((Y-\tfrac12)^2\right)
=
\frac1{180},
\tag{13}
\]
while
\[
\operatorname{Var}(\langle Z,PZ\rangle)=0
\]
and
\[
\operatorname{Cov}(\langle Z,IZ\rangle,\langle Z,PZ\rangle)=0.
\tag{14}
\]

Apply (6) first with \(A=B=I\). Using (7) and (13),
\[
\operatorname{Var}(W_n^2)
=
2\left(1-\frac1n\right)\frac1{90}
+
\frac1{180n}
=
\frac{4n-3}{180n}.
\]

Apply (6) with \(A=B=P\). Equations (10), (12), and (14) give
\[
\operatorname{Var}(U_n^2)
=
2\left(1-\frac1n\right)\frac1{720}
=
\frac{n-1}{360n}.
\]

Finally apply (6) with \(A=I\) and \(B=P\). Equations (9) and (14) give
\[
\operatorname{Cov}(W_n^2,U_n^2)
=
2\left(1-\frac1n\right)\frac1{360}
=
\frac{n-1}{180n},
\]
proving (1)--(2). Substitution yields (3), and
\[
\frac{2(n-1)}{4n-3}
\]
is strictly increasing in \(n\) and tends to \(1/2\), proving (4).

## Verification

The accompanying checker does not replay the operator proof. Instead it uses the classical order-statistic computing formulas under iid uniforms:
\[
W_n^2
=
\frac1{12n}
+
\sum_{i=1}^n
\left(
Y_{(i)}-\frac{2i-1}{2n}
\right)^2
\]
and
\[
U_n^2
=
W_n^2
-
n\left(\overline Y-\frac12\right)^2.
\]

For each \(1\le n\le8\), it expands these as multivariate polynomials on the ordered simplex
\[
0<Y_{(1)}<\cdots<Y_{(n)}<1
\]
and integrates every monomial exactly with rational arithmetic against the order-statistic density \(n!\).

The resulting exact means, variances, and covariance are compared to (1)--(2). It additionally checks the exact squared correlation for every \(2\le n\le8\).

This finite calculation is an independent certificate for the tested sample sizes, not the proof for arbitrary \(n\). The all-\(n\) argument is the quadratic-form calculation above.

## Relationship to prior work

Watson introduced the centered statistic for circular goodness-of-fit. Pearson and Stephens then studied the small-sample distributions of both \(W_n^2\) and \(U_n^2\). Their 1962 paper gives finite-sample moments for \(W_n^2\), Monte Carlo distributions for \(U_n^2\), and a simple relation between the cumulants of the two asymptotic limit laws. The inspected full six-page article does not state a finite-sample covariance, joint moment, or correlation between the two statistics.

Hwang and Kuriki treat Cramér–von Mises and Watson statistics as two of the three classical quadratic empirical-distribution statistics and develop explicit limiting eigenstructures and moment-generating functions for broad integrated generalizations. Their full public manuscript treats the marginal limit laws separately; searches of the text found no correlation statement.

The present identity is joint rather than marginal. In particular, separate cumulants or marginal distributions do not determine
\[
\operatorname{Cov}(W_n^2,U_n^2).
\]
The key extra observation is that the Watson projection has a deterministic one-observation quadratic norm, which makes the finite-\(n\) covariance collapse to a simple rational expression.

## Limitations

The formulas use the simple-null probability-integral-transform setting. Parameter estimation changes the empirical-process projection and therefore changes the covariance structure.

The result gives only second-order dependence. It does not determine the joint distribution of \(W_n^2\) and \(U_n^2\).

Watson's 1961 article could not be obtained in full after open-access and institutional-access attempts, so its comparison is based on verified bibliographic information and the later Pearson--Stephens paper that explicitly defines the same statistics and cites Watson's construction. This leaves a small residual historical risk, although the closest full paper devoted jointly to \(W_n^2\) and \(U_n^2\) was inspected.

## References

1. G. S. Watson, “Goodness-of-fit tests on a circle,” *Biometrika* 48 (1961), 109–114, DOI 10.1093/biomet/48.1-2.109, published 1961-06-01.
2. E. S. Pearson and M. A. Stephens, “The goodness-of-fit tests based on \(W_n^2\) and \(U_n^2\),” *Biometrika* 49 (1962), 397–402, DOI 10.1093/biomet/49.3-4.397, published 1962-12-01.
3. H.-K. Hwang and S. Kuriki, “Integrated empirical measures and generalizations of classical goodness-of-fit statistics,” arXiv:2404.06040, first public version 2024-04-09.
