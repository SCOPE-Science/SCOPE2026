# Sharp lattice mean-absolute-deviation envelope for symmetric unimodal laws

## Finding

Let \(X\) be a nondegenerate integer-valued random variable with symmetric
unimodal mass function
\[
\Pr(X=j)=\Pr(X=-j)=p_j,
\qquad
p_0\ge p_1\ge p_2\ge\cdots .
\]
Write
\[
v=\mathbb E X^2>0.
\]
For \(m\ge0\), define
\[
v_m=\frac{m(m+1)}3,
\qquad
d_m=\frac{m(m+1)}{2m+1}.
\]
Choose the unique \(m\) satisfying
\[
v_m\le v\le v_{m+1},
\]
and put
\[
\theta=\frac{v-v_m}{v_{m+1}-v_m}.
\]

Then the attainable set of mean absolute deviations is exactly
\[
\boxed{
\mathbb E|X|\in(0,D(v)],
}
\]
where
\[
\boxed{
D(v)=(1-\theta)d_m+\theta d_{m+1}.
}
\tag{1}
\]

The upper endpoint is attained by the unique variance-matching mixture of the
two centered discrete uniform laws
\[
U_m\sim {\rm Unif}\{-m,\ldots,m\},
\qquad
U_{m+1}\sim {\rm Unif}\{-(m+1),\ldots,m+1\}.
\]
At a grid variance \(v=v_m\), this collapses to \(U_m\).

The lower endpoint is an infimum rather than a minimum: no nondegenerate law
with variance \(v>0\) has zero mean absolute deviation, but values arbitrarily
close to zero are attainable.

The continuous symmetric-unimodal benchmark
\[
\mathbb E|X|\le\frac{\sqrt3}{2}\sqrt v
\]
is approached from below with a sharp lattice phase correction. If
\[
\theta\to\tau\in[0,1]
\]
while \(v\to\infty\), then
\[
\boxed{
v\left(\frac{\sqrt3}{2}-\frac{D(v)}{\sqrt v}\right)
\longrightarrow
\frac{\sqrt3}{48}\bigl(1+4\tau(1-\tau)\bigr).
}
\tag{2}
\]
Thus the complete cluster interval of the scaled correction is
\[
\boxed{
\left[\frac{\sqrt3}{48},\frac{\sqrt3}{24}\right].
}
\]

## Assumptions and scope

The symmetry center and the unimodal mode are both zero. Unimodality means
that the masses decrease weakly with \(|j|\).

No finite-support assumption is imposed. Finite variance is enough for the
upper bound. The result concerns the population mean absolute deviation about
the mean, which equals \(\mathbb E|X|\) by symmetry.

The unit lattice spacing is a normalization; a lattice with spacing \(h\)
rescales both the variance and the mean absolute deviation in the expected way.

## Proof

For \(m\ge0\), let \(U_m\) be uniform on
\[
\{-m,-m+1,\ldots,m\}.
\]
Define
\[
\lambda_m=(2m+1)(p_m-p_{m+1}).
\]
Unimodality gives \(\lambda_m\ge0\), and summation by parts yields
\[
\sum_{m\ge0}\lambda_m=1.
\]
Moreover, for every \(j\ge0\),
\[
\sum_{m\ge j}\frac{\lambda_m}{2m+1}
=
\sum_{m\ge j}(p_m-p_{m+1})
=
p_j.
\]
Hence
\[
X\stackrel d=U_M
\]
for a mixing index \(M\) satisfying
\[
\Pr(M=m)=\lambda_m.
\tag{3}
\]

The relevant moments of the centered discrete uniform are
\[
\mathbb E U_m^2
=
\frac{m(m+1)}3
=
v_m
\]
and
\[
\mathbb E|U_m|
=
\frac{m(m+1)}{2m+1}
=
d_m.
\tag{4}
\]
Thus
\[
v=\sum_m\lambda_m v_m,
\qquad
\mathbb E|X|=\sum_m\lambda_m d_m.
\tag{5}
\]

The grid points \((v_m,d_m)\) lie on the smooth curve
\[
d=\psi(v),
\qquad
\psi(v)=\frac{3v}{\sqrt{12v+1}},
\tag{6}
\]
because
\[
12v_m+1=(2m+1)^2.
\]
A direct differentiation gives
\[
\psi''(v)
=
-\frac{36(3v+1)}{(12v+1)^{5/2}}<0.
\]
Therefore the secant slopes between consecutive grid points decrease
strictly. The piecewise linear interpolation \(H\) through all points
\((v_m,d_m)\) is consequently concave.

Since \(H(v_m)=d_m\), Jensen's inequality and (5) give
\[
\mathbb E|X|
=
\mathbb E H(v_M)
\le
H(\mathbb E v_M)
=
H(v).
\]
On the cell \([v_m,v_{m+1}]\), the value \(H(v)\) is exactly the chord in
(1), proving the upper bound.

The strict decrease of the secant slopes also gives the equality case. Jensen
equality can hold only when the mixing variance points lie in one affine piece
of \(H\). The only grid points in that piece are \(v_m\) and \(v_{m+1}\), so
\[
\Pr(M=m)=1-\theta,
\qquad
\Pr(M=m+1)=\theta.
\]
At a grid point, strict change of slope forces the degenerate mixing law.

To approach the lower endpoint, fix an integer \(R\) with \(v_R\ge v\) and
mix \(U_R\) with \(U_0\):
\[
\Pr(M=R)=\frac{v}{v_R},
\qquad
\Pr(M=0)=1-\frac{v}{v_R}.
\]
This law has variance \(v\), while
\[
\mathbb E|X|
=
\frac{v}{v_R}d_R
=
\frac{3v}{2R+1}
\longrightarrow0.
\]
Zero itself is impossible when \(v>0\), because \(\mathbb E|X|=0\) would
force \(X=0\) almost surely. Hence the lower endpoint is open.

Every value strictly between zero and \(D(v)\) is attainable. Choose \(R\)
large enough that the preceding low-deviation construction has value below the
target. Both it and the upper extremizer have the same variance \(v\), and a
convex mixture of their laws remains symmetric unimodal with variance \(v\).
Its mean absolute deviation interpolates linearly.

For the lattice correction, set
\[
s=m+1,
\qquad
t=2\theta-1.
\]
Then
\[
v=\frac{s^2+st}{3}
\]
and a direct simplification of (1) gives
\[
D(v)
=
\frac{s(2s^2+st-1)}{4s^2-1}.
\tag{7}
\]
Therefore
\[
\frac{D(v)}{\sqrt v}
=
\sqrt3\,
\frac{2+t/s-1/s^2}{4-1/s^2}
\frac{1}{\sqrt{1+t/s}}.
\]
Uniformly for \(t\in[-1,1]\), expansion at \(s=\infty\) gives
\[
\frac{D(v)}{\sqrt v}
=
\frac{\sqrt3}{2}
-
\frac{\sqrt3}{16s^2}(2-t^2)
+O(s^{-3}).
\]
Since \(v/s^2\to1/3\), this proves (2), because
\[
2-(2\tau-1)^2
=
1+4\tau(1-\tau).
\]

## Verification

A standalone exact-rational checker accompanies the result. It verifies the
discrete-uniform moment formulas, monotonicity of consecutive secant slopes,
exact attainment by adjacent-uniform mixtures, and the lower sequence tending
to zero.

It also tests many random rational mixtures of centered discrete uniforms and
checks that none exceeds the claimed upper envelope. Representative phase
sequences are replayed numerically against the asymptotic formula.

Finite computation is supplementary; the theorem follows from the exact
mixture representation and concavity argument.

## Relationship to prior work

Segers treats mean absolute deviation as a population dispersion functional and
develops the asymptotic law of its sample estimator under weak assumptions. His
2014 paper does not impose unimodality and does not optimize the population mean
absolute deviation at fixed variance.

Navard, Seaman, and Young give a convexity-based characterization of discrete
unimodality and derive variance upper bounds for discrete unimodal laws. Their
full paper develops the relevant lattice shape class and convexity machinery,
but does not give a sharp mean-absolute-deviation envelope at fixed variance.

For continuous symmetric unimodal distributions, Khintchine's uniform-mixture
representation immediately yields
\[
\mathbb E|X|\le\frac{\sqrt3}{2}\sqrt{\mathbb E X^2},
\]
with equality for a centered continuous uniform law. Modern Gauß-inequality
work uses the same representation to obtain sharp tail bounds under first- or
second-moment constraints. The theorem here is the lattice analogue, but the
integer support prevents a single uniform radius from matching an arbitrary
variance. The exact replacement is the adjacent-discrete-uniform interpolation
(1), together with the phase correction (2).

Two earlier sharp results for the same symmetric-unimodal integer class optimize
a tail probability and a fourth moment, respectively. Neither implies the
present statement: their objectives have different supporting functionals and
different equality conditions, and pointwise tail maxima cannot be summed to
obtain a sharp global first absolute moment because their extremizers depend on
the threshold.

## Limitations

The theorem assumes symmetry. Without symmetry, the mean need not coincide
with the mode and the centered-uniform mixture reduction is unavailable in this
form.

The lower endpoint is only an infimum because the support radius is unbounded.
A support-radius constraint would produce a positive minimum, but that is a
different problem.

The originality search was targeted. An equivalent adjacent-uniform envelope
could exist in older discrete-unimodality or moment-problem literature under a
different terminology.

## References

1. J. Segers, “On the asymptotic distribution of the mean absolute deviation
   about the mean,” arXiv:1406.4151, first submitted 2014-06-16.
2. S. E. Navard, J. W. Seaman Jr., and D. M. Young, “A characterization of
   discrete unimodality with applications to variance upper bounds,”
   *Annals of the Institute of Statistical Mathematics* 45 (1993), 603–614,
   DOI 10.1007/BF00774775.
3. C. A. J. Klaassen, “A Markovian Gauß inequality for asymmetric deviations
   from the mode of symmetric unimodal distributions,” arXiv:2312.06606.
4. S. Dharmadhikari and K. Joag-Dev, *Unimodality, Convexity, and
   Applications*, Academic Press, 1988.
