# Exact isotropic supercritical comass profile for the Tsai--Wang form

## Finding

Fix an integer
\[
r\ge2
\]
and a number
\[
\lambda>0.
\]
Consider the affine minimal map
\[
F_\lambda:\mathbb R^r\longrightarrow\mathbb R^r,
\qquad
F_\lambda(x)=\lambda x,
\]
and let \(\Theta_\lambda\) denote the Tsai--Wang \(r\)-form associated with this graph.

Its comass is exactly
\[
\boxed{
\|\Theta_\lambda\|
=
\begin{cases}
1,
&
(r-1)\lambda^2\le1,
\\[5pt]
\displaystyle
\frac{(r-1)^{r-1}\lambda^r(1+\lambda^2)^{(r-2)/2}}
{\bigl(1+(r-1)^2\lambda^2\bigr)^{(r-2)/2}},
&
(r-1)\lambda^2>1.
\end{cases}
}
\]

In the supercritical regime
\[
(r-1)\lambda^2>1,
\]
a maximizing graphical \(r\)-plane is
\[
\boxed{
\Gamma_{-((r-1)\lambda)^{-1}I_r}.
}
\]
Thus the plane used by Chen--Lien to prove failure of the comass-one condition,
\[
\Gamma_{-\lambda I_r},
\]
is sharp exactly at the threshold but is not the optimal comass witness once the isotropic family is strictly supercritical.

For example, in the first genuinely higher-rank case \(r=3\),
\[
\|\Theta_\lambda\|
=
\frac{4\lambda^3\sqrt{1+\lambda^2}}
{\sqrt{1+4\lambda^2}},
\qquad
\lambda>\frac1{\sqrt2},
\]
and the maximizing slope is
\[
-\frac1{2\lambda}.
\]

## Assumptions and scope

The result concerns the canonical isotropic affine family
\[
dF_\lambda=\lambda I_r.
\]
Every such graph is affine and hence minimal, so the Tsai--Wang form is closed.

The computation is pointwise. Chen and Lien show that, for comass purposes, one may work in equal-dimensional domain and target coordinates and test graph planes \(\Gamma_B\), which are dense in the Grassmannian.

No claim is made here about an exact supercritical comass formula for arbitrary unequal singular values.

## Proof

For equal singular values
\[
\lambda_1=\cdots=\lambda_r=\lambda,
\]
the coordinate formula of Chen--Lien gives
\[
C=(1+\lambda^2)^{r/2},
\qquad
S=\frac{r\lambda^2}{1+\lambda^2},
\]
and, for every real \(r\times r\) matrix \(B\),
\[
\Theta_\lambda(\Gamma_B)
=
C\,
\frac{a+d\,\operatorname{tr}B}
{\sqrt{\det(I+B^TB)}},
\]
where
\[
a
=
\frac{1-(r-1)\lambda^2}{1+\lambda^2},
\qquad
d
=
\frac{\lambda}{1+\lambda^2}.
\]

Let
\[
b_1,\ldots,b_r\ge0
\]
be the singular values of \(B\). By the trace inequality,
\[
|\operatorname{tr}B|
\le
\sum_{i=1}^r b_i.
\]
Therefore, with
\[
q=|a|,
\]
we have
\[
|\Theta_\lambda(\Gamma_B)|
\le
C\,
\frac{q+d\sum_i b_i}
{\prod_i\sqrt{1+b_i^2}}.
\]

Write
\[
b_i=\tan\theta_i,
\qquad
0\le\theta_i<\frac\pi2.
\]
After multiplying through the denominator, the quantity to maximize becomes
\[
H(\theta_1,\ldots,\theta_r)
=
q\prod_i\cos\theta_i
+
d\sum_i
\sin\theta_i
\prod_{j\ne i}\cos\theta_j.
\]

This symmetric objective has an exact pairwise smoothing property. Hold all angles except
\[
\alpha=\theta_i,
\qquad
\beta=\theta_j
\]
fixed. After factoring out the remaining cosine product, the dependence on this pair is
\[
Q\cos\alpha\cos\beta
+
d\sin(\alpha+\beta),
\]
where
\[
Q\ge0.
\]
Put
\[
u=\frac{\alpha+\beta}{2},
\qquad
v=\frac{\alpha-\beta}{2}.
\]
Then
\[
\cos\alpha\cos\beta
=
\cos^2u-\sin^2v,
\]
while
\[
\sin(\alpha+\beta)=\sin(2u)
\]
does not depend on \(v\). Replacing \((\alpha,\beta)\) by \((u,u)\) therefore never decreases \(H\). Repeated pairwise averaging shows that the global maximum is attained when
\[
\theta_1=\cdots=\theta_r,
\]
equivalently
\[
b_1=\cdots=b_r=t
\]
for some \(t\ge0\).

It remains to maximize the one-variable function
\[
h(t)
=
C\,
\frac{q+rdt}{(1+t^2)^{r/2}}.
\]

First suppose
\[
(r-1)\lambda^2\le1.
\]
Then
\[
q=a=\frac{1-(r-1)\lambda^2}{1+\lambda^2}.
\]
Differentiation gives
\[
h'(t)
=
\frac{Cr}{(1+t^2)^{r/2+1}}
\left(
d-qt-(r-1)dt^2
\right).
\]
The bracket is strictly decreasing from \(d>0\) and has the unique nonnegative zero
\[
t=\lambda.
\]
At this value,
\[
q+rd\lambda=1
\]
and hence
\[
h(\lambda)=1.
\]
The graph tangent plane \(B=\lambda I_r\) attains equality, so
\[
\|\Theta_\lambda\|=1.
\]

Now suppose
\[
(r-1)\lambda^2>1.
\]
Then
\[
q=-a
=
\frac{(r-1)\lambda^2-1}{1+\lambda^2}.
\]
The same derivative formula shows that the unique positive critical point is
\[
t_*=\frac1{(r-1)\lambda}.
\]
It is the global maximum because the derivative bracket decreases strictly from positive to negative.

Substitution gives
\[
q+rdt_*
=
\frac{(r-1)^2\lambda^2+1}
{(r-1)(1+\lambda^2)}
\]
and
\[
1+t_*^2
=
\frac{(r-1)^2\lambda^2+1}
{(r-1)^2\lambda^2}.
\]
Therefore
\[
h(t_*)
=
\frac{(r-1)^{r-1}\lambda^r(1+\lambda^2)^{(r-2)/2}}
{\bigl(1+(r-1)^2\lambda^2\bigr)^{(r-2)/2}}.
\]

Finally take
\[
B=-t_*I_r.
\]
Then
\[
\operatorname{tr}B=-rt_*,
\]
all its singular values equal \(t_*\), and both inequalities used above are equalities. Hence the displayed upper bound is attained, proving the exact supercritical comass formula.

## Verification

The bundled symbolic checker verifies, for symbolic \(r\), that the subcritical critical point is
\[
t=\lambda,
\]
the supercritical critical point is
\[
t=\frac1{(r-1)\lambda},
\]
and substitution gives the displayed closed form exactly.

It also verifies the pairwise smoothing identity
\[
H(u,u)-H(u+v,u-v)
=
Q\sin^2v,
\]
which is the key global reduction from \(r\) variables to one.

For representative integer ranks \(2\le r\le10\), the checker reconstructs the graph-plane formula at the maximizing \(B\), verifies that its value equals the closed formula, verifies continuity at
\[
\lambda^2=\frac1{r-1},
\]
and checks the large-\(\lambda\) leading scale
\[
\|\Theta_\lambda\|
\sim
(r-1)\lambda^r.
\]

No finite sampling is used to infer the all-rank theorem; the finite checks only replay the symbolic identities after the analytic proof.

## Relationship to prior work

Tsai and Wang introduced the differential form \(\Theta(F)\) for minimal graphs and reduced its comass to a Grassmannian optimization problem. They obtained sufficient singular-value conditions for comass one.

Chen and Lien subsequently proved the exact threshold
\[
S(\lambda)
=
\sum_i\frac{\lambda_i^2}{1+\lambda_i^2}
\le1
\]
for comass one. Their reduced formula evaluates \(\Theta\) on arbitrary graph planes. To prove necessity when \(S>1\), they test
\[
B=-\operatorname{diag}(\lambda_1,\ldots,\lambda_r)
\]
and obtain the value
\[
1-2S.
\]
Their paper determines whether the comass equals one, but does not compute the comass magnitude once \(S>1\).

The present result solves that quantitative optimization completely on the isotropic affine locus
\[
\lambda_1=\cdots=\lambda_r.
\]
It shows that the source's necessity witness is optimal at the threshold but ceases to be optimal beyond it; the maximizing graph slope moves to the reciprocal scale
\[
1/((r-1)\lambda).
\]

Targeted searches using the exact source identifier, equal-singular-value and conformal-linear formulations, supercritical comass terminology, and the reciprocal maximizing slope did not locate a prior statement of this profile.

## Limitations

The theorem is exact only for equal singular values. It does not solve the general supercritical optimization for an arbitrary singular-value vector.

The maximizing-plane statement is given in the paired singular-value coordinates. Under simultaneous orthogonal changes of domain and target, it has the corresponding invariant interpretation.

The result quantifies the comass of the Tsai--Wang form. A comass larger than one says that this particular form is not a calibration; it does not by itself prove that the affine graph fails to be area minimizing by some other argument. Affine planes are, of course, area minimizing by the standard constant calibration.

## References

1. Wei-Chun Chen and Chun-Kai Lien, *The Exact Comass Criterion for the Tsai--Wang Form*, arXiv:2609.39159v1, first submitted 30 September 2026.
2. Chung-Jun Tsai and Mu-Tao Wang, *Calibrating Forms for Minimal Graphs in Arbitrary Codimension*, arXiv:2604.04336v1, first submitted 6 April 2026.
