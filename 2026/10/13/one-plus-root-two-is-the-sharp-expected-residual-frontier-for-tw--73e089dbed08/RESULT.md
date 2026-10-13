# One plus root two is the sharp expected-residual frontier for two-coordinate randomized Gauss–Seidel

## Finding
Let
\[
A=
\begin{pmatrix}
a&c\\
c&b
\end{pmatrix}
=A^{\mathsf T}>0,
\]
and write the equation residual as
\[
r=b_{\mathrm{rhs}}-Ax.
\]
Choose coordinate \(1\) with probability
\[
\frac{a}{a+b}
\]
and coordinate \(2\) with probability
\[
\frac{b}{a+b},
\]
and then perform the exact Gauss–Seidel coordinate update
\[
x_i^+
=
x_i+\frac{r_i}{A_{ii}}.
\]

For a fixed matrix define
\[
p=\frac{|c|}{a},
\qquad
q=\frac{|c|}{b}.
\]
Then
\[
\boxed{
\mathbb E\!\left[\|r^+\|_2^2\mid r\right]
\le
\|r\|_2^2
\text{ for every }r
\quad\Longleftrightarrow\quad
p+q+pq\le1.
}
\]

Now fix the spectral condition number
\[
\kappa
=
\frac{\lambda_{\max}(A)}
{\lambda_{\min}(A)}.
\]
The exact robust condition-number frontier is
\[
\boxed{
\mathbb E\!\left[\|r^+\|_2^2\mid r\right]
\le
\|r\|_2^2
\text{ for every }2\times2\text{ SPD }A\text{ of condition }\kappa
\quad\Longleftrightarrow\quad
\kappa\le1+\sqrt2.
}
\]

Sharpness is attained by the equal-diagonal family
\[
A_\kappa
=
\frac12
\begin{pmatrix}
\kappa+1&\kappa-1\\
\kappa-1&\kappa+1
\end{pmatrix}.
\]
For
\[
r=(1,-1)^{\mathsf T},
\]
the two coordinates are sampled uniformly and
\[
\frac{
\mathbb E\|r^+\|_2^2
}{
\|r\|_2^2
}
=
\frac{2\kappa^2}{(\kappa+1)^2}.
\]
This exceeds one exactly for
\[
\kappa>1+\sqrt2.
\]

A simple exact witness is
\[
A=
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix},
\qquad
\kappa=3,
\qquad
r=(1,-1)^{\mathsf T}.
\]
Either coordinate update leaves one residual component equal in magnitude to \(3/2\), so
\[
\mathbb E\|r^+\|_2^2=\frac94,
\qquad
\|r\|_2^2=2,
\qquad
\frac{\mathbb E\|r^+\|_2^2}{\|r\|_2^2}
=
\frac98.
\]

## Assumptions and scope
The result concerns exact arithmetic, two real coordinates, an SPD coefficient matrix, one randomized exact coordinate update, and sampling probabilities proportional to the coordinate Lipschitz constants \(A_{ii}\).

The Euclidean norm is applied to the equation residual
\[
b_{\mathrm{rhs}}-Ax.
\]
This is not the same metric as the quadratic objective gap or the \(A^{-1}\)-weighted residual energy naturally controlled by coordinate descent.

The theorem does not classify dimensions above two, uniform sampling when the diagonal entries differ, greedy sampling, block updates, asynchronous variants, delayed reads, finite precision, or multi-step path maxima.

## Proof
Changing the sign of the second coordinate by a diagonal orthogonal similarity changes the sign of \(c\) but preserves the eigenvalues, diagonal entries, sampling probabilities, and Euclidean residual norms. It is therefore enough to assume
\[
c\ge0.
\]
The diagonal case \(c=0\) is immediate, so suppose \(c>0\) and put
\[
p=\frac{c}{a},
\qquad
q=\frac{c}{b}.
\]
Positive definiteness gives
\[
pq=\frac{c^2}{ab}<1.
\]

If coordinate \(1\) is selected, then
\[
r^+
=
\begin{pmatrix}
0\\
r_2-pr_1
\end{pmatrix}.
\]
If coordinate \(2\) is selected, then
\[
r^+
=
\begin{pmatrix}
r_1-qr_2\\
0
\end{pmatrix}.
\]
Since
\[
\frac{a}{a+b}
=
\frac{q}{p+q},
\qquad
\frac{b}{a+b}
=
\frac{p}{p+q},
\]
the conditional expected squared residual is
\[
\mathbb E\!\left[\|r^+\|_2^2\mid r\right]
=
r^{\mathsf T}Mr,
\]
where
\[
M
=
\frac1{p+q}
\begin{pmatrix}
p(1+pq)&-2pq\\
-2pq&q(1+pq)
\end{pmatrix}.
\]

Thus expected residual nonincrease for every incoming residual is equivalent to
\[
M\preceq I.
\]
The diagonal entries of \(I-M\) are
\[
\frac{q(1-p^2)}{p+q},
\qquad
\frac{p(1-q^2)}{p+q},
\]
and
\[
\det(I-M)
=
\frac{pq}{(p+q)^2}
\bigl(pq-p-q-1\bigr)
\bigl(pq+p+q-1\bigr).
\]
Because
\[
pq<1
\]
and \(p,q>0\), the factor
\[
pq-p-q-1
\]
is strictly negative. If
\[
p+q+pq\le1,
\]
then \(p<1\) and \(q<1\), both diagonal entries of \(I-M\) are nonnegative, and the determinant is nonnegative. Conversely, if \(M\preceq I\), the determinant is nonnegative, forcing
\[
p+q+pq\le1.
\]
This proves the fixed-matrix criterion.

For the robust condition-number statement, scale the eigenvalues to
\[
1,\kappa
\]
and define
\[
\delta=\frac{\kappa-1}{\kappa+1}.
\]
After a planar rotation one can write
\[
a=m(1-\delta z),
\qquad
b=m(1+\delta z),
\qquad
|c|=m\delta\sqrt{1-z^2},
\]
where
\[
-1\le z\le1
\]
and \(m>0\). Put
\[
t=\sqrt{1-z^2}.
\]
Then
\[
p+q+pq
=
\frac{
2\delta t+\delta^2t^2
}{
1-\delta^2+\delta^2t^2
}.
\]

Suppose first that
\[
\delta\le\sqrt2-1.
\]
A direct subtraction gives
\[
2\delta+\delta^2-(p+q+pq)
=
\frac{
\delta(1-t)
\left[
2-(1+t)(\delta^3+2\delta^2-\delta)
\right]
}{
1-\delta^2+\delta^2t^2
}.
\]
Because
\[
\delta^3+2\delta^2-\delta
=
\delta(\delta^2+2\delta-1)
\le0,
\]
the right-hand side is nonnegative. Hence
\[
p+q+pq
\le
2\delta+\delta^2
\le1.
\]
The fixed-matrix criterion therefore holds for every orientation.

Conversely, if
\[
\delta>\sqrt2-1,
\]
take equal diagonal entries, which means \(z=0\) and \(t=1\). Then
\[
p=q=\delta,
\qquad
p+q+pq=2\delta+\delta^2>1,
\]
so expected residual monotonicity fails for some residual.

Finally,
\[
\delta\le\sqrt2-1
\]
is equivalent to
\[
\kappa\le1+\sqrt2.
\]
This proves the sharp robust frontier.

## Verification
The embedded `verify.py` uses exact rational arithmetic for the witness
\[
A=
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix}
\]
and checks that both possible coordinate updates have squared residual norm \(9/4\) from an incoming squared norm \(2\).

It also samples exact rational SPD matrices and verifies that the matrix criterion
\[
M\preceq I
\]
agrees with
\[
p+q+pq\le1,
\]
and it checks the equal-diagonal family symbolically through rational identities.

The all-matrix condition-number theorem is analytic; numerical or finite sampling is not used to establish its quantifiers.

## Relationship to prior work
Randomized Gauss–Seidel is the same exact-coordinate update that appears as randomized coordinate descent. Ma, Needell, and Ramdas describe the method by selecting a column with probability proportional to its squared Euclidean norm and exactly minimizing the least-squares objective in that coordinate. For an SPD quadratic represented with
\[
X^{\mathsf T}X=A,
\]
this sampling becomes proportional to \(A_{ii}\), exactly as in the theorem.

Their convergence analysis controls the least-squares residual
\[
X(x-x_*)
\]
or, equivalently for the SPD quadratic, the \(A^{-1}\)-weighted equation residual. It does not assert monotonicity of the ordinary Euclidean equation residual
\[
b_{\mathrm{rhs}}-Ax.
\]
This distinction is decisive: the displayed \(\kappa=3\) example has an expected Euclidean residual increase after one coordinate minimization.

A related published result analyzes two-coordinate deterministic Gauss–Seidel ordering in Euclidean solution error, not randomized one-coordinate updates or expected equation-residual energy. Another published result treats randomized Gauss–Seidel with stale-read delays in a diagonal-scaled mean-square error. Neither implication controls the Euclidean residual quantity classified here.

Targeted searches using randomized Gauss–Seidel, randomized coordinate descent, expected residual norm, two-dimensional SPD, one-step residual growth, and condition-number terminology did not locate the fixed-matrix criterion or the sharp constant
\[
1+\sqrt2.
\]

## Limitations
The theorem is two-dimensional and one-step. Higher dimensions introduce a genuinely larger expected-residual matrix and are not classified here.

The coordinate probabilities are proportional to \(A_{ii}\). Uniform sampling is identical only when the two diagonal entries coincide.

The result concerns the Euclidean equation residual. It does not contradict classical expected convergence in the objective, energy norm, or least-squares residual associated with a square root of \(A\).

The literature comparison leaves a residual risk that an older coordinate-relaxation paper contains the same two-dimensional Euclidean-residual criterion under different terminology.

## References
1. A. Ma, D. Needell, and A. Ramdas, “Convergence Properties of the Randomized Extended Gauss–Seidel and Kaczmarz Methods,” arXiv:1503.08235, first submitted 2015-03-27; SIAM Journal on Matrix Analysis and Applications 36 (2015), 1590–1604. DOI 10.1137/15M1014425.
2. A. Hefny, D. Needell, and A. Ramdas, “Rows versus Columns: Randomized Kaczmarz or Gauss–Seidel for Ridge Regression,” arXiv:1507.05844, first submitted 2015-07-21; SIAM Journal on Scientific Computing 39 (2017), S528–S542. DOI 10.1137/16M1077891.
