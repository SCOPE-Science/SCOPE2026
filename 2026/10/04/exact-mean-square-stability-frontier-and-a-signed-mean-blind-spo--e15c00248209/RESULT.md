# Exact mean-square stability frontier and a signed-mean blind spot in KGSM
## Finding

Randomized Kaczmarz with geometrically smoothed momentum (KGSM) was introduced to accelerate slowly decaying singular-vector components while suppressing the noise of batch-one heavy-ball momentum. Its defining analysis controls a signed expected error, while the paper explicitly asks for a critical momentum region and for convergence of absolute or \(\ell_2\) error.

On the smallest nontrivial orthonormal system, both questions have an exact answer and the distinction between signed mean and mean square is genuine.

Take
\[
A=I_2,
\qquad
b=0,
\]
and sample either row independently with probability \(1/2\). Use the source KGSM recurrence
\[
x_{k+1}
=
x_k
-
\langle x_k,e_{i_k}\rangle e_{i_k}
+
My_k,
\]
\[
y_{k+1}
=
\beta y_k
+
(1-\beta)(x_{k+1}-x_k),
\]
with
\[
y_0=0,
\qquad
0\le\beta<1,
\qquad
0\le M\le1.
\]

Then
\[
\mathbb E\|x_k\|_2^2\longrightarrow0
\]
for every initial vector \(x_0\) if and only if
\[
\beta+2(1-\beta)M
<
\sqrt{\beta+2}.
\]

Equivalently, define
\[
M_*(\beta)
=
\frac{
\sqrt{\beta+2}-\beta
}{
2(1-\beta)
}.
\]
Within the source range \(0\le M\le1\), the mean-square stable region is exactly
\[
M<M_*(\beta).
\]
If equality is attainable, it is marginal rather than convergent. Every admissible
\[
M>M_*(\beta)
\]
is mean-square unstable.

Two exact consequences make the boundary concrete.

For no geometric smoothing,
\[
\beta=0,
\]
the critical mass is
\[
M_*(0)=\frac1{\sqrt2}.
\]
However, the signed mean
\[
\mathbb E[x_k]
\]
still converges to zero for every
\[
0\le M<1.
\]
Therefore the entire interval
\[
\frac1{\sqrt2}\le M<1
\]
is a signed-mean blind spot: the expected signed error converges, but the expected squared error does not.

At the largest allowed mass,
\[
M=1,
\]
mean-square stability holds exactly when
\[
\beta
>
\frac{5-\sqrt{17}}2
=
0.4384471872\ldots.
\]
Thus sufficient geometric smoothing can stabilize every source-allowed mass on this orthonormal system.

## Assumptions and scope

The system is the consistent two-equation orthonormal problem
\[
A=I_2,
\qquad
b=0.
\]
Translation reduces any consistent identity system to this form.

Rows are sampled independently and uniformly, exactly matching norm-squared sampling because both row norms are one.

The source initialization
\[
y_0=0
\]
is used.

The theorem concerns mean-square convergence of the iterate. It does not claim an exact stability region for nonorthogonal matrices, inconsistent systems, block variants, or other sampling laws.

## Proof

Because the two coordinates are statistically symmetric, analyze one fixed coordinate. Let
\[
I_k
=
\begin{cases}
1,&\text{if that coordinate is selected at step }k,\\
0,&\text{otherwise}.
\end{cases}
\]
Then
\[
I_k\sim\operatorname{Bernoulli}(1/2)
\]
independently of the past.

For
\[
M>0,
\]
write
\[
z_k=My_k,
\qquad
u=(1-\beta)M,
\qquad
a=\beta+u.
\]
The coordinate recurrence is
\[
x_{k+1}
=
(1-I_k)x_k+z_k,
\]
\[
z_{k+1}
=
az_k-uI_kx_k.
\]
The same covariance formulas extend continuously to \(M=0\).

Define
\[
q_k=\mathbb E[x_k^2],
\qquad
r_k=\mathbb E[x_kz_k],
\qquad
s_k=\mathbb E[z_k^2].
\]
Averaging over the independent Bernoulli row choice gives the exact deterministic recursion
\[
\begin{bmatrix}
q_{k+1}\\
r_{k+1}\\
s_{k+1}
\end{bmatrix}
=
T
\begin{bmatrix}
q_k\\
r_k\\
s_k
\end{bmatrix},
\]
where
\[
T
=
\begin{bmatrix}
1/2&1&1\\
0&\beta/2&a\\
u^2/2&-au&a^2
\end{bmatrix}.
\]

Let the characteristic polynomial be
\[
p(t)=t^3+a_1t^2+a_2t+a_3.
\]
Direct expansion gives
\[
a_1
=
-\frac{
2\beta^2+4\beta u+\beta+2u^2+1
}{2},
\]
\[
a_2
=
\frac{
2\beta^3+8\beta^2u+2\beta^2+10\beta u^2+4\beta u+\beta+4u^3
}{4},
\]
and
\[
a_3
=
-\frac{
(\beta+2u)(\beta^2+2\beta u+2u^2)
}{4}.
\]

For a real monic cubic, the Jury criterion says that all roots lie strictly inside the unit disk exactly when
\[
1+a_1+a_2+a_3>0,
\]
\[
1-a_1+a_2-a_3>0,
\]
\[
1-a_2+a_1a_3-a_3^2>0,
\]
and
\[
|a_3|<1.
\]

The first Jury expression factors as
\[
1+a_1+a_2+a_3
=
\frac{\beta-1}{4}
\left[
(\beta+2u)^2-(\beta+2)
\right].
\]
Since
\[
\beta<1,
\]
this expression is positive exactly when
\[
\beta+2u<\sqrt{\beta+2}.
\]

The second Jury expression is
\[
\frac14
\left(
3\beta^3
+12\beta^2u
+6\beta^2
+16\beta u^2
+12\beta u
+3\beta
+8u^3
+4u^2
+6
\right),
\]
so it is strictly positive throughout the parameter range.

The third expression is also uniformly positive on the whole source parameter rectangle, not merely in the claimed stable region. To certify this without floating-point optimization, substitute
\[
c=1-\beta,
\qquad
u=cM.
\]
The resulting polynomial has bidegree at most \((6,6)\). Its exact tensor-product Bernstein coefficients on
\[
(c,M)\in[0,1]^2
\]
are all positive; the smallest is exactly
\[
\frac3{16}.
\]
Because Bernstein basis functions are nonnegative and sum to one,
\[
1-a_2+a_1a_3-a_3^2
\ge
\frac3{16}.
\]
The accompanying verifier reconstructs this polynomial from the displayed \(a_1,a_2,a_3\) using exact rational arithmetic and recomputes all \(49\) Bernstein coefficients.

Finally, under the first Jury inequality set
\[
S=\beta+2u.
\]
Then
\[
S<\sqrt{\beta+2}\le\sqrt3,
\]
and
\[
\beta^2+2\beta u+2u^2
=
\frac{S^2+\beta^2}{2}.
\]
Hence
\[
|a_3|
=
\frac{S(S^2+\beta^2)}8
<
\frac{\sqrt3(3+1)}8
=
\frac{\sqrt3}{2}
<1.
\]
Thus the first Jury expression is the only active boundary, proving the stated mean-square stability region.

It remains to connect Schur instability to the source initialization rather than to an arbitrary covariance state. Since
\[
y_0=0,
\]
we have
\[
(q_0,r_0,s_0)
=
(q_0,0,0).
\]
At the boundary, \(T\) has eigenvalue \(1\). Above it,
\[
p(1)<0
\]
while
\[
p(t)\to+\infty
\]
as \(t\to+\infty\), so \(T\) has a real eigenvalue
\[
\lambda>1.
\]
For any left eigenvector \(w\) associated with \(\lambda\ge1\), its first component cannot vanish when \(u>0\): if \(w_1=0\), the first left-eigenvector equation forces \(w_3=0\), and then the second forces \(w_2=0\) because \(\beta/2<1\). Therefore
\[
w_1\ne0.
\]
The source covariance state has nonzero projection onto this nondecaying mode, so the full covariance vector cannot converge to zero.

Moreover,
\[
q_{k+1}
=
\frac12\mathbb E[(x_k+z_k)^2]
+
\frac12\mathbb E[z_k^2]
\ge
\frac12s_k.
\]
Thus if \(q_k\) tended to zero, then \(s_k\) would also tend to zero, and Cauchy-Schwarz would force
\[
r_k\to0,
\]
contradicting the nondecaying covariance mode. Hence the iterate itself fails to converge in mean square at and above the boundary.

For the signed-mean separation at
\[
\beta=0,
\]
the mean state \((\mathbb E x_k,\mathbb E z_k)\) evolves by
\[
B
=
\begin{bmatrix}
1/2&1\\
-M/2&M
\end{bmatrix}.
\]
Its characteristic polynomial is
\[
t^2-\left(M+\frac12\right)t+M.
\]
The quadratic Jury conditions hold exactly for
\[
0\le M<1.
\]
Combining this with the mean-square threshold
\[
M<1/\sqrt2
\]
proves the blind-spot interval.

At
\[
M=1,
\]
the mean-square condition becomes
\[
2-\beta<\sqrt{\beta+2},
\]
equivalently
\[
\beta^2-5\beta+2<0.
\]
Within
\[
0\le\beta<1,
\]
this is precisely
\[
\beta>\frac{5-\sqrt{17}}2.
\]

## Verification

The accompanying `verify.py` reconstructs the covariance polynomial using exact rational bivariate polynomial arithmetic.

It verifies the factorization of the first Jury expression, positivity of the second expression, the exact \(49\)-coefficient Bernstein certificate with minimum \(3/16\), the signed-mean quadratic criterion at \(\beta=0\), and direct covariance iteration on representative stable, marginal, and unstable parameter choices.

No finite simulation is used as an infinite-time proof. The stability classification follows from the exact covariance recursion and the cubic Jury criterion.

## Relationship to prior work

Alderman, Luikart, and Marshall introduced KGSM and proved decay formulas for the expected signed error along singular-vector directions. They explicitly identify two limitations that motivate the present calculation: determining a critical momentum value or region in \((M,\beta)\), and proving convergence for expected absolute error or the \(\ell_2\) norm.

Their numerical work shows that momentum can enter a critical regime, but their theorem does not classify mean-square stability. The orthonormal example here shows why that distinction matters: for unsmoothed momentum, signed expectation remains stable throughout
\[
M<1,
\]
while mean-square stability already fails at
\[
M=1/\sqrt2.
\]

Loizou and Richtárik earlier proved \(L_2\)-type convergence guarantees for stochastic heavy-ball and randomized Kaczmarz with ordinary momentum under sufficient parameter conditions. That update uses the unsmoothed displacement
\[
\beta(x_k-x_{k-1})
\]
rather than KGSM's extra geometrically smoothed velocity state, and the inspected result gives sufficient global rates rather than the exact KGSM phase boundary above.

Focused searches for KGSM critical momentum, covariance stability, orthonormal systems, and mean-square convergence did not locate an implication-equivalent theorem.

## Limitations

The exact frontier is for
\[
A=I_2
\]
with uniform independent row sampling.

It does not classify nonorthogonal systems or claim that the same curve is a universal KGSM boundary.

Mean-square instability does not imply almost-sure divergence on every sample path.

The signed-mean blind spot is shown exactly for
\[
\beta=0.
\]
Other smoothing values may also exhibit gaps between signed and unsigned observables, but those gaps are not classified here.

## References

1. Seth J. Alderman, Roan W. Luikart, and Nicholas F. Marshall, “Randomized Kaczmarz with Geometrically Smoothed Momentum,” arXiv:2401.09415v1, 2024; SIAM Journal on Matrix Analysis and Applications 45(4), 2024, DOI 10.1137/24M1633820.
2. Nicolas Loizou and Peter Richtárik, “Momentum and Stochastic Momentum for Stochastic Gradient, Newton, Proximal Point and Subspace Descent Methods,” arXiv:1712.09677v2, 2017; Computational Optimization and Applications 77, 2020.
