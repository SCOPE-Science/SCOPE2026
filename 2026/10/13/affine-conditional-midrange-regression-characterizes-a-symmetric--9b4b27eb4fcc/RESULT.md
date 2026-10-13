# Affine conditional midrange regression characterizes a symmetric power-quantile family

## Finding

Let \(X_1,X_2,X_3\) be independent and identically distributed from a nondegenerate absolutely continuous law. Assume a finite first moment, a strictly positive continuous density on the interior of the support, a continuously differentiable strictly increasing quantile \(Q\), and central symmetry about \(\mu\). Write
\[
X_{1:3}<X_{2:3}<X_{3:3}.
\]

Then
\[
\boxed{
\mathbb E\!\left[
\frac{X_{1:3}+X_{3:3}}2
\,\middle|\,
X_{2:3}=x
\right]
=
a x+b
}
\tag{1}
\]
throughout the interior support if and only if
\[
\boxed{
a\ge\frac12,\qquad b=(1-a)\mu,
}
\tag{2}
\]
and, for some \(s>0\),
\[
\boxed{
Q(p)=
\mu+s(2p-1)[p(1-p)]^{1/(2a)-1},
\qquad 0<p<1.
}
\tag{3}
\]

The endpoint \(a=\frac12\) gives a uniform law on a finite interval. The point \(a=1\) gives a location-scale Student \(t\) law with two degrees of freedom. For \(a>\frac12\),
\[
1-F(x)\asymp x^{-2a/(2a-1)}
\qquad(x\to\infty),
\tag{4}
\]
so the regression slope directly determines the tail index.

## Assumptions and scope

Central symmetry means
\[
X_1-\mu\overset d=\mu-X_1.
\]
The regularity assumptions ensure that conditioning on the sample median can be expressed through truncated means and that the quantile differential equation may be solved pointwise.

The theorem concerns the three-observation midrange conditional on the sample median. It does not classify nonsymmetric parents, regressions using other order statistics, or nonlinear regression functions.

## Proof

Translate by \(\mu\). It is enough to prove the centered case \(\mu=0\). Symmetry gives
\[
Q(1-p)=-Q(p).
\tag{5}
\]
It also transforms \(x\) to \(-x\) and the conditional midrange to its negative. Therefore an affine regression must satisfy
\[
b=0
\]
after centering, which becomes \(b=(1-a)\mu\) before centering.

Put
\[
H(p)=\int_0^p Q(u)\,du.
\tag{6}
\]
Finite first moment and symmetry imply
\[
\int_0^1Q(u)\,du=0.
\tag{7}
\]

Condition on
\[
X_{2:3}=Q(p).
\]
The lower observation has the parent law truncated below \(Q(p)\), while the upper observation has the parent law truncated above \(Q(p)\). Hence
\[
\mathbb E[X_{1:3}\mid X_{2:3}=Q(p)]
=
\frac{H(p)}p,
\tag{8}
\]
and, by (7),
\[
\mathbb E[X_{3:3}\mid X_{2:3}=Q(p)]
=
-\frac{H(p)}{1-p}.
\tag{9}
\]

The centered affine regression is therefore equivalent to
\[
(1-2p)H(p)
=
2a\,p(1-p)Q(p).
\tag{10}
\]

For a nondegenerate parent, \(a=0\) is impossible. Differentiate (10), use \(H'(p)=Q(p)\), and put
\[
z=2p-1,\qquad q(z)=Q\!\left(\frac{1+z}{2}\right).
\]
For \(z\ne0\),
\[
a z(1-z^2)q'(z)
=
\bigl(a+(a-1)z^2\bigr)q(z).
\tag{11}
\]
Solving this first-order equation and using symmetry yields
\[
q(z)=c\,z(1-z^2)^{1/(2a)-1}
\tag{12}
\]
with one common constant \(c>0\). Rewriting (12) in the \(p\)-coordinate gives (3), after absorbing a fixed factor into \(s\).

The quantile must be increasing and integrable. For \(a>0\), differentiation of (12) shows that its sign is controlled by
\[
1-\frac{1-a}{a}z^2.
\tag{13}
\]
This is nonnegative for all \(|z|<1\) exactly when \(a\ge\frac12\). If \(a<0\), the endpoint power in (12) is less than \(-1\), contradicting the finite first moment. Thus (2) is necessary.

Conversely, take any \(a\ge\frac12\) and \(s>0\) in (3). The quantile is strictly increasing, symmetric, and integrable. Writing
\[
\gamma=\frac1{2a}-1,
\]
direct integration gives
\[
H(p)
=
-2as[p(1-p)]^{1/(2a)}.
\tag{14}
\]
Substitution into (10) proves the regression.

At \(a=\frac12\), the exponent in (3) is zero, so \(Q\) is affine and the parent is uniform. At \(a=1\), (12) is proportional to
\[
\frac{z}{\sqrt{1-z^2}},
\]
the quantile form of a location-scale Student \(t_2\) law.

For \(a>\frac12\), as \(p\uparrow1\),
\[
Q(p)\sim s(1-p)^{-(2a-1)/(2a)},
\]
which gives (4).

## Verification

The accompanying checker symbolically verifies the differential equation, the explicit quantile solution, and the antiderivative identity that reproduces the regression. It also checks the monotonicity boundary at \(a=\frac12\) and numerically evaluates the conditional regression on a grid for several admissible slopes.

The computational checks are supplementary. The theorem for all admissible slopes follows from equations (8)--(14).

## Relationship to prior work

Akhundov, Balakrishnan, and Nevzorov study the regression
\[
\mathbb E\!\left[
\lambda X_{1:3}+(1-\lambda)X_{3:3}
\,\middle|\,
X_{2:3}=x
\right]=x
\]
and its higher odd-sample analogues. Their theorem characterizes a quantile family; the symmetric case \(\lambda=\frac12\) yields Student \(t_2\). Their discussion explicitly identifies the affine replacement \(a x+b\) as an interesting unsolved extension for their method.

The present theorem resolves the centrally symmetric, equally weighted three-observation case of that affine direction. It is not obtained by varying \(\lambda\) in the earlier identity-regression family: here \(\lambda=\frac12\) is fixed while the regression slope \(a\) varies, producing a continuum from the bounded uniform endpoint through Student \(t_2\) to heavier-tailed laws.

Balakrishnan and Akhundov characterize a related sample-mean regression under an identity condition. Yanev and Ahsanullah later revisit the Student \(t_2\) identity-regression characterization and related average-order-statistic formulations. The inspected statements use slope one and do not state the slope-indexed symmetric family (3).

## Limitations

Central symmetry is essential to the present reduction. The full nonsymmetric affine problem remains outside the claim.

The theorem assumes enough regularity to differentiate the quantile relation. Singular or mixed distributions are not covered.

The power-quantile family may admit other parameterizations or names. The originality claim is limited to the regression equivalence, the sharp slope restriction, and the direct slope-to-tail-index interpretation.

## References

1. I. S. Akhundov, N. Balakrishnan, and V. B. Nevzorov, “New Characterizations by Properties of Midrange and Related Statistics,” *Communications in Statistics—Theory and Methods* 33 (2004), 3133–3143, DOI 10.1081/STA-200039063. Publisher record: published online 2007-02-15. Primary MSC 62E10.
2. N. Balakrishnan and I. S. Akhundov, “A characterization by linearity of the regression function based on order statistics,” *Statistics & Probability Letters* 63 (2003), 435–440, DOI 10.1016/S0167-7152(03)00123-8.
3. G. P. Yanev and M. Ahsanullah, “Characterizations of Student's t-distribution via regressions of order statistics,” arXiv:1010.4355, first submitted 2010-10-21.
