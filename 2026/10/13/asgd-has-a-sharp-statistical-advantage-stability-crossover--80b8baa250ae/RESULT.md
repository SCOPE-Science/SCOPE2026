# ASGD has a sharp statistical-advantage stability crossover
## Finding

The practical two-state Accelerated Stochastic Gradient Descent (ASGD) form of Kidambi, Netrapalli, Jain, and Kakade mixes a short gradient step with a running average that itself receives a much longer gradient step. On a scalar quadratic, the exact stability boundary can be written in closed form.

Let
\[
f(w)=\frac12 h w^2,\qquad h>0,
\]
and use the source constant
\[
c=0.7.
\]
Let
\[
\delta>0,\qquad \kappa\ge1,\qquad 0<\xi\le\sqrt{\kappa}.
\]
The practical source algorithm sets
\[
a=1-\frac{c^2\xi}{\kappa}.
\]
Define
\[
e=1-a=\frac{c^2\xi}{\kappa},
\qquad
s=\delta h.
\]

The source updates specialize exactly to
\[
\bar w_{t+1}
=
(1-e)\bar w_t
+
e\left(1-\frac{\kappa s}{c}\right)w_t
\]
and
\[
w_{t+1}
=
\frac{c}{c+e}(1-s)w_t
+
\frac{e}{c+e}\bar w_{t+1}.
\]

The resulting two-state system is Schur stable if and only if
\[
\boxed{0<s<s_{\max}(\kappa,\xi),}
\]
where
\[
\boxed{
s_{\max}(\kappa,\xi)
=
\frac{2(200\kappa+21\xi)}
{200\kappa+49\xi^2-49\xi}.
}
\]
At
\[
s=s_{\max},
\]
one eigenvalue is exactly
\[
-1.
\]

Scalar gradient descent is stable for
\[
0<s<2.
\]
The exact ASGD comparison is
\[
\boxed{s_{\max}>2\iff\xi<\frac{10}{7},}
\]
\[
\boxed{s_{\max}=2\iff\xi=\frac{10}{7},}
\]
and
\[
\boxed{s_{\max}<2\iff\xi>\frac{10}{7}.}
\]

Thus the statistical-advantage parameter controls a genuine large-step crossover: smaller \(\xi\) lets the two-state average tolerate short steps beyond the scalar SGD ceiling, while sufficiently large \(\xi\) makes the ASGD short-step stability interval narrower than SGD's.

There is nevertheless a uniform source-parameter safety margin. Over
\[
\kappa\ge1,\qquad 0<\xi\le\sqrt{\kappa},
\]
\[
\boxed{s_{\max}>\frac{400}{249}}
\]
for every finite admissible pair, and
\[
\boxed{\inf_{\kappa,\xi}s_{\max}=\frac{400}{249}\approx1.6064257.}
\]
The infimum is approached along
\[
\xi=\sqrt{\kappa},\qquad \kappa\to\infty.
\]

Consequently every scalar mode with
\[
s\le1
\]
is uniformly inside the stability region throughout the source parameter range. This remains true even though the isolated long gradient step has multiplier
\[
1-\frac{\kappa s}{c},
\]
which can be far outside the unit disk. Stability is a property of the coupled short-step/running-average mechanism, not of either constituent gradient step alone.

## Assumptions and scope

The theorem concerns the deterministic scalar quadratic specialization of the practical ASGD form displayed in the 2018 source paper.

The earlier 2017 ASGD paper introduces the accelerated stochastic method in a four-sequence parameterization and proves stochastic least-squares guarantees. The 2018 paper gives the simpler short-step/long-step form analyzed here and states its relation to the earlier method.

The source statistical-advantage parameter is treated as a fixed positive number satisfying
\[
\xi\le\sqrt{\kappa}.
\]
No probabilistic interpretation is needed for the deterministic modal stability calculation.

The result is a Schur-stability classification of one scalar curvature mode. It does not claim that a larger stability interval implies a better convergence rate or lower stochastic variance.

## Proof

Write
\[
z_t=
\begin{bmatrix}
w_t\\
\bar w_t
\end{bmatrix},
\qquad
L_s=1-\frac{\kappa s}{c}.
\]
After substituting the running-average update into the descent-iterate update,
\[
M=
\begin{bmatrix}
\dfrac{c(1-s)+e^2L_s}{c+e}
&
\dfrac{e(1-e)}{c+e}
\\[8pt]
eL_s
&
1-e
\end{bmatrix}.
\]

Its determinant is
\[
D=\frac{c(1-e)(1-s)}{c+e},
\]
and its trace is
\[
T=
1-e+
\frac{c(1-s)+e^2L_s}{c+e}.
\]

For the characteristic polynomial
\[
z^2-Tz+D,
\]
the second-order Jury conditions are
\[
1-D>0,\qquad 1-T+D>0,\qquad 1+T+D>0.
\]

Substituting
\[
c=\frac7{10},
\qquad
e=\frac{49\xi}{100\kappa}
\]
gives
\[
1-D
=
\frac{100\kappa s-49\xi s+119\xi}
{10(10\kappa+7\xi)},
\]
\[
1-T+D
=
\frac{49s\xi(\xi+1)}
{10(10\kappa+7\xi)},
\]
and
\[
1+T+D
=
\frac{
400\kappa+42\xi-s(200\kappa+49\xi^2-49\xi)
}{
10(10\kappa+7\xi)
}.
\]

Under
\[
\kappa\ge1,\qquad 0<\xi\le\sqrt{\kappa},\qquad s>0,
\]
the first two expressions are strictly positive. The third is positive exactly when
\[
s<
\frac{2(200\kappa+21\xi)}
{200\kappa+49\xi^2-49\xi}.
\]
This proves the exact stability interval.

At equality,
\[
1+T+D=0,
\]
so the characteristic polynomial vanishes at
\[
z=-1.
\]

Subtracting the SGD ceiling gives
\[
s_{\max}-2
=
\frac{14\xi(10-7\xi)}
{200\kappa+49\xi^2-49\xi},
\]
which proves the crossover at
\[
\xi=\frac{10}{7}.
\]

Finally,
\[
s_{\max}-\frac{400}{249}
=
\frac{
14(1400\kappa-1400\xi^2+2147\xi)
}{
249(200\kappa+49\xi^2-49\xi)
}.
\]
Since
\[
\xi^2\le\kappa,
\]
the numerator is strictly positive for every finite admissible pair. Along
\[
\xi=\sqrt{\kappa},
\]
the ceiling tends to
\[
400/249
\]
as
\[
\kappa\to\infty.
\]
This proves sharpness of the global infimum.

## Verification

The accompanying `verify.py` reconstructs the exact two-state source recurrence and compares the analytic stability criterion against direct characteristic-root calculations over deterministic parameter grids.

It checks the \(-1\) boundary root, the crossover at
\[
\xi=10/7,
\]
the strict global lower bound
\[
400/249,
\]
and convergence toward that lower envelope on the deterministic parameter slice.

The computations are transcription guards. The if-and-only-if stability theorem and global infimum are proved algebraically above.

## Relationship to prior work

Jain and coauthors introduced ASGD for stochastic least-squares regression and gave a sharp stochastic-process analysis with accelerated statistical guarantees. Their original algorithm uses a four-parameter accelerated recurrence.

Kidambi, Netrapalli, Jain, and Kakade later present an intuitive, easier-to-tune two-state form. Its inputs are a short step, a long-step parameter, and a statistical-advantage parameter. The paper states that the short step plays the same role as the SGD step, that the long-step parameter estimates a condition number, and that in the deterministic case the statistical-advantage parameter equals the square root of that condition number and the method is equivalent to Nesterov acceleration.

The inspected primary sources establish stochastic convergence rates and the equivalence of parameterizations, but they do not state the exact scalar Schur boundary above, the crossover at
\[
\xi=10/7,
\]
or the uniform lower envelope
\[
400/249.
\]

Classical scalar Nesterov stability is directly relevant to the deterministic endpoint
\[
\xi=\sqrt{\kappa}
\]
and is therefore treated as broader prior context rather than as a new consequence by itself. The contribution here is the complete stability law across the source statistical-advantage interpolation, including regimes that are not the deterministic Nesterov slice.

Focused published-record searches for the ASGD short-step/long-step form, statistical-advantage stability, and scalar quadratic Schur boundaries did not identify an implication-equivalent statement.

## Limitations

The theorem is deterministic and one-dimensional.

The long-step parameter and statistical-advantage parameter are held fixed.

The result concerns stability, not optimal spectral radius, stochastic variance, or tail-averaged statistical risk.

The deterministic endpoint is related to classical Nesterov acceleration; originality is restricted to the complete source-parameter stability frontier and its crossover structure.

## References

1. Prateek Jain, Sham M. Kakade, Rahul Kidambi, Praneeth Netrapalli, and Aaron Sidford, “Accelerating Stochastic Gradient Descent For Least Squares Regression,” arXiv:1704.08227v1, first submitted 2017-04-26.
2. Rahul Kidambi, Praneeth Netrapalli, Prateek Jain, and Sham M. Kakade, “On the insufficiency of existing momentum schemes for Stochastic Optimization,” arXiv:1803.05591v1, first submitted 2018-03-15; ICLR 2018.
