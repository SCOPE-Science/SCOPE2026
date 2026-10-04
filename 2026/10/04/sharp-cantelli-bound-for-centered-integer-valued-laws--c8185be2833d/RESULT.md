# Sharp Cantelli bound for centered integer-valued laws

## Finding

Let \(X\) be integer-valued with
\[
\mathbb E X=0,\qquad \operatorname{Var}(X)=v\ge0,
\]
and let \(k\ge1\) be an integer threshold. Define
\[
j=\left\lfloor\frac{v}{k}\right\rfloor.
\]
Then
\[
\boxed{
\Pr(X\ge k)
\le
\frac{v+j(j+1)}{(k+j)(k+j+1)}.
}
\tag{1}
\]
This bound is sharp for every \(v\ge0\).

More precisely, put
\[
r=v-kj,\qquad 0\le r<k.
\]
Equality in (1) is attained by the law supported on
\[
\{-(j+1),-j,k\}
\]
with masses
\[
\Pr(X=k)
=
\frac{v+j(j+1)}{(k+j)(k+j+1)},
\]
\[
\Pr(X=-j)
=
\frac{k(j+1)-v}{k+j},
\]
and
\[
\Pr(X=-(j+1))
=
\frac{v-kj}{k+j+1}.
\]
Zero masses are omitted. These masses give the unique equality law once the
mean and variance are fixed.

The exact gain over the classical one-sided Cantelli bound is
\[
\frac{v}{v+k^2}
-
\frac{v+j(j+1)}{(k+j)(k+j+1)}
=
\frac{r(k-r)}
{(k+j)(k+j+1)(v+k^2)}.
\tag{2}
\]
Thus the lattice bound is strictly sharper whenever \(v/k\notin\mathbb Z\),
and it coincides with Cantelli exactly when \(v/k\in\mathbb Z\).

An affine form follows immediately. If \(Y\) is supported on
\(\mu+h\mathbb Z\), with \(h>0\), \(\mathbb E Y=\mu\), and
\(\operatorname{Var}(Y)=\sigma^2\), then applying (1) to
\(X=(Y-\mu)/h\) gives the corresponding exact bound at thresholds
\(\mu+kh\), provided \(\mu\) belongs to the supporting lattice.

## Assumptions and scope

No independence, symmetry, bounded-support assumption, or higher moment is
required. The only probabilistic hypotheses are integer support, finite
variance, and centering.

The threshold is an integer \(k\ge1\). The affine corollary covers a general
one-dimensional lattice after translating by the mean and scaling by its span
when the mean is itself a lattice point. No claim is made here for a
non-lattice-aligned mean, a non-lattice threshold, or constraints involving
higher moments.

## Proof

For an integer \(j\ge0\), define the quadratic
\[
Q_j(x)
=
\frac{(x+j)(x+j+1)}
{(k+j)(k+j+1)}.
\]
The numerator is a product of consecutive integers whenever \(x\in\mathbb Z\).
Consequently
\[
(x+j)(x+j+1)\ge0
\qquad\text{for every }x\in\mathbb Z.
\]
Hence \(Q_j(x)\ge0\) at every integer below \(k\). For every integer
\(x\ge k\), both numerator factors are positive and increase with \(x\), so
\[
Q_j(x)\ge Q_j(k)=1.
\]
Therefore the pointwise lattice majorization
\[
\mathbf 1_{\{x\ge k\}}\le Q_j(x),
\qquad x\in\mathbb Z,
\tag{3}
\]
holds.

Taking expectations in (3) and using
\(\mathbb E X=0\) and \(\mathbb E X^2=v\) yields
\[
\Pr(X\ge k)
\le
\mathbb E Q_j(X)
=
\frac{v+j(j+1)}{(k+j)(k+j+1)}.
\tag{4}
\]
At this point (4) is valid for every integer \(j\ge0\). To make it sharp,
choose
\[
j=\left\lfloor\frac{v}{k}\right\rfloor.
\]

Let
\[
a=\frac{v+j(j+1)}{(k+j)(k+j+1)},\qquad
b=\frac{k(j+1)-v}{k+j},\qquad
c=\frac{v-kj}{k+j+1}.
\]
Because
\[
kj\le v<k(j+1),
\]
all three numbers are nonnegative. Direct simplification gives
\[
a+b+c=1,
\]
\[
ka-jb-(j+1)c=0,
\]
and
\[
k^2a+j^2b+(j+1)^2c=v.
\]
Thus the three-point law
\[
\Pr(X=k)=a,\qquad
\Pr(X=-j)=b,\qquad
\Pr(X=-(j+1))=c
\]
has mean zero and variance \(v\), while
\[
\Pr(X\ge k)=a,
\]
so equality holds in (4).

The equality classification is also immediate from (3). Equality in
expectation forces all mass onto lattice points where
\[
Q_j(x)=\mathbf 1_{\{x\ge k\}}.
\]
For \(x<k\), the quadratic vanishes only at
\[
x=-j,\qquad x=-(j+1),
\]
and for \(x\ge k\), it equals one only at \(x=k\). Hence every equality law is
supported on exactly these three candidate points. The mass, mean, and
second-moment equations then determine \(a,b,c\) uniquely, with any zero mass
deleted.

It remains to compare (1) with Cantelli. Write
\[
v=kj+r,\qquad 0\le r<k.
\]
A common-denominator calculation gives
\[
\frac{v}{v+k^2}
-
\frac{v+j(j+1)}{(k+j)(k+j+1)}
=
\frac{r(k-r)}
{(k+j)(k+j+1)(v+k^2)}.
\]
This proves (2), including the strictness criterion.

Finally, if \(Y\) is supported on \(\mu+h\mathbb Z\) with
\(\mathbb E Y=\mu\), then \(X=(Y-\mu)/h\) is integer-valued, centered, and has
variance \(\sigma^2/h^2\). Applying the theorem to \(X\) gives the stated
affine-lattice form.

## Verification

A standalone exact-rational checker accompanies the result. It verifies the
moment-matching masses, the exact Cantelli-gap identity, and the pointwise
quadratic majorant over a broad lattice window for many rational variances and
integer thresholds.

The finite computation is supplementary. The theorem for the full infinite
integer lattice follows from the sign of a product of consecutive integers and
the monotonicity of the quadratic above the threshold, not from finite
enumeration.

## Relationship to prior work

The classical Cantelli inequality gives
\[
\Pr(X\ge k)\le\frac{v}{v+k^2}
\]
for an arbitrary real-valued centered random variable with variance \(v\).
The present result uses the integer support to insert a quadratic majorant
whose two roots are consecutive lattice points. Formula (2) quantifies exactly
how much the lattice restriction improves the continuous-support bound.

Rujeerapaiboon, Kuhn, and Wiesemann formulate sharp probability inequalities
from first and second moments as generalized moment problems and dual
polynomial majorization problems. Their 2016 work supplies the natural
optimization framework, but the inspected abstract and moment-duality
development do not state the consecutive-root integer-lattice bound (1), its
three-point extremizer, or the exact gap (2).

Ghosh studies best one-sided and interval probability bounds from a known mean
and standard deviation for arbitrary or nonnegative random variables. The
available abstract does not impose integer support or state (1); the full
article was not inspected, so it remains a residual historical-coverage risk.

Troffaes and Basu derive a Cantelli-type inequality under exchangeability using
sample mean and sample variance, with a bounded-range correction. Their object
is a prediction bound based on sample statistics, not a moment problem for one
integer-valued law.

A published finite-sample result on exchangeable externally studentized
prediction residuals gives an exact staircase through a deterministic
finite-vector Cantelli count. Its optimized object, constraints, and extremal
laws differ from (1), and its statement does not imply the present
integer-support moment envelope.

Targeted searches for integer-valued, lattice-valued, discrete, sharp
one-sided Chebyshev/Cantelli bounds, the consecutive-root quadratic, and the
explicit denominator in (1) did not locate an equivalent statement.

## Limitations

The affine corollary assumes that the mean is a point of the lattice. If the
mean is not lattice-aligned, the two consecutive roots in the proof must be
repositioned, and a different piecewise formula may be required.

Only the one-sided half-line event at a lattice-aligned threshold is treated.
The theorem does not claim optimal bounds for two-sided tails, intervals,
higher moments, multivariate lattices, or conditional prediction problems.

The originality assessment used targeted semantic, bibliographic, and
full-text comparisons rather than an exhaustive historical search. In
particular, older Markov--Chebyshev moment-problem or lattice-probability
literature could contain an equivalent result under different terminology,
and the full text of Ghosh's 2002 article was not inspected.

## References

1. N. Rujeerapaiboon, D. Kuhn, and W. Wiesemann,
   “Chebyshev Inequalities for Products of Random Variables,”
   arXiv:1605.05487, first posted 2016-05-18.
2. B. K. Ghosh, “Probability Inequalities Related to Markov's Theorem,”
   *The American Statistician* 56 (2002).
   DOI: 10.1198/000313002119.
3. M. C. M. Troffaes and T. Basu,
   “A Cantelli-Type Inequality for Constructing Non-Parametric P-Boxes Based
   on Exchangeability,” *Proceedings of Machine Learning Research* 103
   (2019), 386–393.
