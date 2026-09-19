# Exact FGM validity window and entropy failure under block copula substitution

## Statement

Let
\[
C_\theta(u,v)=uv\bigl[1+\theta(1-u)(1-v)\bigr],\qquad -1\le \theta\le 1,
\]
be the bivariate Farlie--Gumbel--Morgenstern (FGM) copula. For integers \(r,s\ge1\), let
\[
\Pi_r(x_1,\ldots,x_r)=\prod_{i=1}^r x_i,
\qquad
\Pi_s(y_1,\ldots,y_s)=\prod_{j=1}^s y_j,
\]
and consider the block substitution
\[
G_{r,s,\theta}(x,y)
=
C_\theta\bigl(\Pi_r(x),\Pi_s(y)\bigr).
\]
Write
\[
A_r=2^r-1,\qquad A_s=2^s-1.
\]
Then \(G_{r,s,\theta}\) is an \((r+s)\)-copula if and only if
\[
\boxed{
-\frac{1}{A_rA_s}
\le \theta\le
\frac{1}{\max\{A_r,A_s\}}.
}
\]
Its density, whenever it is a copula, is
\[
\boxed{
g_{r,s,\theta}(x,y)
=
1+\theta\bigl(1-2^r\Pi_r(x)\bigr)
          \bigl(1-2^s\Pi_s(y)\bigr).
}
\]

Consequently, direct substitution of arbitrary copulas into arbitrary copula arguments is not closed on the class of copulas. In particular, the general closure claim in Proposition 2.2 and Theorem 2.3 of Lu, *Copula Operad and Copula Entropy*, arXiv:2609.20512v1, is false as stated.

A second consequence concerns copula entropy. Suppose \(\theta\ne0\) lies in the interior of the displayed admissible interval. If \(r+s>2\), then
\[
\boxed{
H(G_{r,s,\theta})<H(C_\theta),
}
\]
where
\[
H(C)=-\int c\log c
\]
is copula entropy. Since \(H(\Pi_r)=H(\Pi_s)=0\), this gives a family of valid, bounded-density copulas for which
\[
H\bigl(C_\theta(\Pi_r,\Pi_s)\bigr)
\ne H(C_\theta)+H(\Pi_r)+H(\Pi_s).
\]
Thus the entropy-additivity claim of Theorem 4.1 in arXiv:2609.20512v1 also fails even when the composite is a genuine copula and every density is bounded and bounded away from zero.

## Proof of the exact admissibility interval

Put
\[
U=\Pi_r(x),\qquad V=\Pi_s(y).
\]
The function \(G_{r,s,\theta}\) is grounded and has uniform one-dimensional margins for every \(\theta\in[-1,1]\), because setting all coordinates except one equal to one reduces it to \(C_\theta(t,1)=t\) or \(C_\theta(1,t)=t\).

The full mixed derivative can be evaluated directly. Since
\[
\frac{\partial^r U}{\partial x_1\cdots\partial x_r}=1,
\qquad
\frac{\partial^r U^2}{\partial x_1\cdots\partial x_r}=2^rU,
\]
and similarly for \(V\), differentiating
\[
UV+\theta(UV-U^2V-UV^2+U^2V^2)
\]
gives
\[
g_{r,s,\theta}
=1+\theta(1-2^rU)(1-2^sV).
\]
Because \(U,V\) independently range over all of \([0,1]\), the two factors independently range over
\[
[-A_r,1],\qquad[-A_s,1].
\]
Their product therefore has exact range
\[
\left[-\max\{A_r,A_s\},\;A_rA_s\right].
\]
Hence \(g_{r,s,\theta}\ge0\) everywhere exactly when
\[
\theta\le \frac{1}{\max\{A_r,A_s\}}\quad(\theta\ge0),
\]
and
\[
|\theta|\le\frac1{A_rA_s}\quad(\theta\le0).
\]
For a smooth grounded function with the correct margins, nonnegativity of the full mixed derivative is equivalent here to nonnegative rectangle volumes, so the condition is both necessary and sufficient.

The window collapses with block arity. In particular, no fixed nonzero FGM parameter survives arbitrary product-block substitutions: the intersection of the admissible intervals over all \(r,s\) is \(\{0\}\).

## Explicit counterexample to unrestricted closure

Take \(r=2\), \(s=1\), and \(\theta=1\). The outer FGM copula \(C_1\), the inner independence copula \(\Pi_2\), and the one-dimensional identity copula are all legitimate copulas with bounded densities. Their proposed substitution is
\[
G(x,y,z)=C_1(xy,z),
\]
whose mixed derivative is
\[
\frac{\partial^3G}{\partial x\,\partial y\,\partial z}
=1+(1-4xy)(1-2z).
\]
At
\[
(x,y,z)=\left(\frac9{10},\frac9{10},\frac1{10}\right)
\]
this equals
\[
\boxed{-\frac{99}{125}<0}.
\]
It is therefore negative on an open neighborhood, so a sufficiently small rectangular increment is negative and \(G\) is not 3-increasing. Hence \(G\) is not a copula.

This same example shows why the density formula in Proposition 3.1 of arXiv:2609.20512v1 misses terms. The formula claimed there would give
\[
c_\theta(xy,z)
=1+\theta(1-2xy)(1-2z),
\]
whereas repeated differentiation within the two-variable block gives the actual factor \(1-4xy\).

There is also a probabilistic obstruction to the closure proof. A multivariate copula CDF evaluated at a random point is generally not uniform. Already for \(\Pi_2\), if \(X,Y\) are independent uniforms then
\[
\Pi_2(X,Y)=XY
\]
has distribution function
\[
\Pr(XY\le t)=t-t\log t,
\qquad0<t<1,
\]
not the uniform law. This is the classical Kendall-distribution phenomenon.

## Entropy is strictly non-additive on the valid part of the family

Let \(X_1,X_2,\ldots\) and \(Y_1,Y_2,\ldots\) be independent \(\mathrm{Unif}(0,1)\) variables and set
\[
P_r=2^r\prod_{i=1}^rX_i,
\qquad
Q_s=2^s\prod_{j=1}^sY_j,
\]
\[
A_r=1-P_r,
\qquad
B_s=1-Q_s.
\]
Under Lebesgue measure on the cube,
\[
g_{r,s,\theta}=1+\theta A_rB_s.
\]
Thus the KL divergence from independence is
\[
D_{r,s}(\theta)
=-H(G_{r,s,\theta})
=
\mathbb E\!\left[(1+\theta A_rB_s)
\log(1+\theta A_rB_s)\right].
\]

The sequence \((A_r)_{r\ge1}\) is a martingale with respect to its natural filtration, because
\[
\mathbb E[A_{r+1}\mid A_r]
=1-P_r\,\mathbb E[2X_{r+1}]
=A_r.
\]
For fixed \(b\ne0\), the map
\[
a\longmapsto(1+\theta ab)\log(1+\theta ab)
\]
is strictly convex throughout the interior of the admissible parameter range, with second derivative
\[
\frac{\theta^2b^2}{1+\theta ab}>0.
\]
Conditional Jensen therefore gives
\[
D_{r+1,s}(\theta)>D_{r,s}(\theta)
\]
for every nonzero interior \(\theta\); the same argument applies in \(s\). Since \(D_{1,1}(\theta)=-H(C_\theta)\), any genuine block enlargement makes the entropy strictly more negative:
\[
H(G_{r,s,\theta})<H(C_\theta),\qquad r+s>2.
\]

The failure is already visible in the curvature at independence. Since
\[
\mathbb E A_r^2
=
\left(\frac43\right)^r-1,
\]
one has
\[
\boxed{
H''_{r,s}(0)
=-\left[\left(\frac43\right)^r-1\right]
 \left[\left(\frac43\right)^s-1\right].
}
\]
For the outer bivariate FGM copula, \(H''_{1,1}(0)=-1/9\), whereas for the valid \((r,s)=(2,1)\) substitution,
\[
H''_{2,1}(0)=-\frac7{27}.
\]

As a concrete bounded-density example, \((r,s,\theta)=(2,1,1/4)\) lies strictly inside the exact validity window \([-1/3,1/3]\). Direct quadrature gives
\[
H(C_{1/4})\approx-0.00348541259188370856,
\]
while
\[
H(G_{2,1,1/4})\approx-0.00823719152104166084.
\]
The difference is about \(-0.00475177892915795227\), although both inner entropies are zero.

## Relation to prior literature

The general fact that hierarchical/nested copulas require compatibility conditions is established prior art. In particular, nested Archimedean copulas are not formed by unrestricted substitution: McNeil (2008) gives sufficient nesting conditions in terms of complete monotonicity. No novelty is claimed for that general warning.

Likewise, the non-uniformity of \(C(U)\) for a multivariate copula is classical and is precisely the subject of Kendall distribution functions; Nelsen, Quesada-Molina, Rodríguez-Lallena and Úbeda-Flores studied these probability-integral-transform analogues in 2001 and 2003.

The contribution claimed here is narrower: the exact two-sided FGM/product-block admissibility window, the explicit full-density formula, the strict entropy monotonicity under block enlargement, and their use to give direct counterexamples to the central unrestricted closure and entropy-additivity statements of arXiv:2609.20512v1. Targeted searches for the displayed FGM threshold and equivalent product-block formulations did not locate a prior statement. Older FGM and hierarchical-copula literature remains a residual originality risk.

## Limitations

The exact characterization is for a bivariate FGM outer copula with product-copula inner blocks. It does not classify all outer copulas or all admissible nested constructions. The entropy comparison is stated for nonzero parameters in the interior of the validity window; boundary cases can be handled separately but are not needed for the counterexample. The source-specific conclusions refer to arXiv:2609.20512v1; a later revision may change or withdraw the affected claims.

## Reproducibility

`artifacts/verify_fgm_substitution.py` symbolically differentiates the block substitution for several arities, checks the exact admissible intervals, evaluates the explicit negative density, and reproduces the entropy values and entropy curvatures. The accompanying `artifacts/verification.txt` records its output. The verification was executed with Python 3, SymPy 1.14.0 and mpmath 1.3.0.

## References

1. X. Lu, *Copula Operad and Copula Entropy*, arXiv:2609.20512v1 (2026). https://arxiv.org/abs/2609.20512v1
2. A. J. McNeil, *Sampling nested Archimedean copulas*, Journal of Statistical Computation and Simulation 78 (2008), 567–581. https://doi.org/10.1080/00949650701255834
3. R. B. Nelsen, J. J. Quesada-Molina, J. A. Rodríguez-Lallena, and M. Úbeda-Flores, *Distribution functions of copulas: a class of bivariate probability integral transforms*, Statistics & Probability Letters 54 (2001), 277–282.
4. R. B. Nelsen, J. J. Quesada-Molina, J. A. Rodríguez-Lallena, and M. Úbeda-Flores, *Kendall distribution functions*, Statistics & Probability Letters 65 (2003), 263–268. https://doi.org/10.1016/j.spl.2003.08.002
5. R. B. Nelsen, *An Introduction to Copulas*, 2nd ed., Springer, 2006.
