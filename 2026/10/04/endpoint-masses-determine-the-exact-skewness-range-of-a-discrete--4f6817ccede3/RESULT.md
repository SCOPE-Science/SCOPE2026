# Endpoint masses determine the exact skewness range of a discrete law

## Finding

Fix positive masses
\[
p_1,\ldots,p_m,
\qquad
\sum_{i=1}^m p_i=1,
\]
and let \(X\) range over all discrete laws with distinct ordered support
\[
x_1<\cdots<x_m,
\qquad
\Pr(X=x_i)=p_i.
\]
For a nondegenerate law write
\[
\gamma(X)
=
\frac{\mathbb E[(X-\mathbb EX)^3]}
{\operatorname{Var}(X)^{3/2}},
\]
and define
\[
g(u)=\frac{2u-1}{\sqrt{u(1-u)}},
\qquad 0<u<1.
\]

If \(m\ge3\), then the complete attainable skewness set is
\[
\boxed{
\gamma(X)\in
\left(
g(p_1),
g(1-p_m)
\right).
}
\tag{1}
\]

The endpoints are sharp but unattained. The lower endpoint is approached by
collapsing the upper \(m-1\) atoms to one level while keeping the first atom
separate. The upper endpoint is approached by collapsing the lower \(m-1\)
atoms while keeping the last atom separate.

Every value strictly between the two endpoints is attained by some strictly
increasing support.

For \(m=2\), every support is a positive affine image of every other one, and
the skewness is the single value
\[
\boxed{
\gamma(X)=g(p_1).
}
\tag{2}
\]

There is a direct sampling consequence. If \(X_1,\ldots,X_n\) are iid copies
with \(n\ge2\), and
\[
\bar X=\frac1n\sum_{j=1}^nX_j,
\qquad
S^2=\frac1{n-1}\sum_{j=1}^n(X_j-\bar X)^2,
\]
then
\[
\operatorname{Cov}(\bar X,S^2)
=
\frac{\mathbb E[(X-\mathbb EX)^3]}{n}.
\]
Hence, for \(m\ge3\),
\[
\boxed{
g(p_1)
<
\frac{n\,\operatorname{Cov}(\bar X,S^2)}
{\operatorname{Var}(X)^{3/2}}
<
g(1-p_m).
}
\tag{3}
\]

The sign is therefore completely classified by the endpoint masses:

- if \(p_1\ge1/2\), then \(\operatorname{Corr}(\bar X,S^2)>0\) for every
  strictly increasing support;
- if \(p_m\ge1/2\), then \(\operatorname{Corr}(\bar X,S^2)<0\) for every
  strictly increasing support;
- if \(p_1<1/2\) and \(p_m<1/2\), then negative, zero, and positive
  correlations are all attainable by changing only the atom locations.

## Assumptions and scope

The probability profile is fixed together with its order. Only the support
locations vary.

All masses are strictly positive. The main interval statement is for
\(m\ge3\); the two-point case is given separately.

Because the support is finite, every moment used here exists. The sampling
corollary concerns the ordinary unbiased sample variance.

The theorem optimizes the standardized third central moment. It does not give
the complete magnitude range of the sample-mean/sample-variance correlation,
whose denominator also depends on kurtosis.

## Proof

Skewness is invariant under transformations
\[
x_i\mapsto a+bx_i,
\qquad b>0.
\]
We may therefore normalize the support values to
\[
\sum_i p_i y_i=0,
\qquad
\sum_i p_i y_i^2=1,
\qquad
y_1\le\cdots\le y_m.
\tag{4}
\]
On this normalized set,
\[
\gamma=\sum_i p_i y_i^3.
\tag{5}
\]

Allow equalities temporarily and let \(\mathcal K\) be the closed normalized
set defined by (4). It is compact: the second-moment constraint gives
\[
|y_i|\le p_i^{-1/2}.
\]

Consider a point of \(\mathcal K\) having exactly \(k\) distinct support
levels
\[
z_1<\cdots<z_k.
\]
Each level consists of a consecutive block of the original ordered atoms.
Let the corresponding block masses be
\[
q_1,\ldots,q_k.
\]
Within the relative interior of this stratum, maximizing or minimizing (5)
subject to
\[
\sum_jq_jz_j=0,
\qquad
\sum_jq_jz_j^2=1
\]
gives the Lagrange equations
\[
3z_j^2=\lambda+2\eta z_j
\qquad(1\le j\le k).
\tag{6}
\]
The right side of (6) says that every distinct \(z_j\) is a root of one
quadratic polynomial. Therefore no relative-interior extremum can have
\(k\ge3\) distinct levels.

Starting from a global extremum of the compact set \(\mathcal K\), if it has
three or more levels it must lie on the boundary of its stratum. Passing to
that lower-dimensional boundary and repeating the argument shows that every
global extremum has exactly two distinct levels.

Because the original atoms are ordered, a two-level point is determined by a
cut
\[
1\le j<m.
\]
The lower level then has total mass
\[
P_j=\sum_{i=1}^jp_i,
\]
and the upper level has mass \(1-P_j\).

For any two-level distribution whose lower level has mass \(P\), a direct
centering and scaling calculation gives
\[
\gamma=g(P)
=
\frac{2P-1}{\sqrt{P(1-P)}}.
\tag{7}
\]
Moreover,
\[
g'(P)
=
\frac1{2[P(1-P)]^{3/2}}>0.
\tag{8}
\]
Thus among all cuts,
\[
\min_jg(P_j)=g(P_1)=g(p_1)
\]
and
\[
\max_jg(P_j)=g(P_{m-1})=g(1-p_m).
\]

For \(m\ge3\), these two-level extremizers are not allowed in the original
strict-support problem. They are, however, limits of strictly increasing
supports, so they are respectively the exact infimum and supremum.

The open cone
\[
\{(x_1,\ldots,x_m):x_1<\cdots<x_m\}
\]
is convex and hence connected. Skewness is continuous on it. Its image is
therefore an interval. Since its infimum and supremum are the two values above
and neither is attained, the image is exactly the open interval (1).

When \(m=2\), there is only one positive-affine support shape, and (7) gives
(2).

Finally, the standard iid identity
\[
\operatorname{Cov}(\bar X,S^2)
=
\frac{\mu_3}{n}
\]
with
\[
\mu_3=\mathbb E[(X-\mathbb EX)^3]
\]
turns (1) into (3). The sign of the corresponding correlation is the same as
the sign of \(\mu_3\). Since \(g\) is increasing and \(g(1/2)=0\), the three
sign regimes follow immediately.

## Verification

The accompanying exact-rational checker generates many rational probability
profiles and strictly increasing rational supports.

It verifies the lower and upper inequalities by exact squared comparisons,
constructs explicit collapsing sequences approaching both endpoints, checks
the two-point formula, and confirms the exact covariance identity for
\(\bar X\) and \(S^2\) by enumerating iid samples in small rational examples.

The computation is supplementary. The universal result follows from the
compact-stratum and quadratic Lagrange argument above.

## Relationship to prior work

Shanmugam derives a general formula for the correlation between the sample
mean and sample variance and works through many standard non-normal families.
The same full paper records the basic covariance identity
\[
\operatorname{Cov}(\bar X,S^2)=\frac{\mu_3}{n}.
\]
That literature makes skewness operational for the sampling problem, but the
inspected article does not optimize skewness over support locations with a
fixed discrete probability profile.

Zhang gives the covariance formula and examples of zero covariance without
normality. Sen later studies the interrelation further and connects the
sample-mean/sample-variance correlation to skewness and kurtosis. These works
treat a parent distribution as given; they do not provide a fixed-mass
support-geometry classification.

The Bernoulli skewness formula is the two-level boundary calculation (7).
The new point is that, for an arbitrary fixed ordered finite probability
profile, every global skewness extremum in the closure must collapse to two
levels, and monotonicity then shows that only the first and last atom masses
control the complete range.

Targeted searches using fixed probability vectors, finite discrete skewness,
support optimization, standardized third moments, and sample-mean/sample-
variance correlation did not locate the endpoint-mass interval (1).

## Limitations

The probability masses and their order are fixed. Allowing the masses to vary
removes the finite endpoint bounds because a vanishing endpoint mass can make
skewness arbitrarily large in magnitude.

The theorem is one-dimensional and concerns the third standardized moment.
Higher standardized moments lead to higher-degree stationarity equations and
need not reduce to two support levels.

The originality search was targeted. Older finite-population or moment-space
literature may contain an equivalent fixed-profile skewness theorem under
different language.

## References

1. R. Shanmugam, “Correlation between the Sample Mean and Sample Variance,”
   *Journal of Modern Applied Statistical Methods* 7(2) (2008), 408–415,
   DOI 10.22237/jmasm/1225512300.
2. L. Zhang, “Sample Mean and Sample Variance: Their Covariance and Their
   (In)Dependence,” *The American Statistician* 61 (2007), 159–160,
   DOI 10.1198/000313007X188379.
3. A. Sen, “On the Interrelation Between the Sample Mean and the Sample
   Variance,” *The American Statistician* 66 (2012), 112–117,
   DOI 10.1080/00031305.2012.695960.
