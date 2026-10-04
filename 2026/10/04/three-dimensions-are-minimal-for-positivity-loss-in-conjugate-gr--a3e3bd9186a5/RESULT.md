# Three dimensions are minimal for positivity loss in conjugate gradients on Stieltjes systems
## Finding
Consider exact-arithmetic conjugate gradients started from \(x_0=0\) for a symmetric positive definite linear system
\[
Ax=b.
\]
Even if \(A\) is a Stieltjes matrix, so that \(A^{-1}\) is entrywise nonnegative, and even if \(b\ge0\), a conjugate-gradient iterate need not remain nonnegative.

Three dimensions are minimal for this phenomenon. In dimensions one and two, every exact-arithmetic conjugate-gradient iterate is nonnegative whenever \(A^{-1}\ge0\), \(b\ge0\), and \(x_0=0\). In dimension three, the tridiagonal family
\[
A_a=
\begin{pmatrix}
a&-1&0\\
-1&2&-1\\
0&-1&2
\end{pmatrix},
\qquad
b_B=
\begin{pmatrix}
1\\0\\B
\end{pmatrix},
\]
with
\[
a>\frac23,\qquad B\ge0,
\]
has a sharp internal threshold: its second conjugate-gradient iterate has a negative first component for some \(B\ge0\) if and only if
\[
a>4.
\]

More precisely, writing \(x_2\) for the second iterate,
\[
(x_2)_1=\frac{N_a(B)}{Q_a(B)},
\]
where \(Q_a(B)>0\) and
\[
N_a(B)
=
(4-a)B^4+4B^3+(2a^2-9a+14)B^2+(8-2a)B+2.
\]
Therefore
\[
\frac23<a\le4
\quad\Longrightarrow\quad
(x_2)_1>0\ \text{for every }B\ge0,
\]
whereas for every \(a>4\),
\[
\lim_{B\to\infty}(x_2)_1=\frac{4-a}{3}<0.
\]
The negative iterate is transient: exact conjugate gradients reaches the strictly positive exact solution by the third step.

An exact witness is
\[
A=
\begin{pmatrix}
5&-1&0\\
-1&2&-1\\
0&-1&2
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
1\\0\\7
\end{pmatrix}.
\]
Then
\[
A^{-1}b=
\begin{pmatrix}
10/13\\37/13\\64/13
\end{pmatrix}>0,
\]
but the second conjugate-gradient iterate is
\[
x_2=
\begin{pmatrix}
-5/751\\
1324/751\\
6881/1502
\end{pmatrix},
\]
whose first component is negative. The failure persists after replacing the zero middle entry of \(b\) by a sufficiently small positive number, so strictly positive right-hand sides also exhibit the effect.

## Assumptions and scope
The result concerns the standard unpreconditioned conjugate-gradient recurrence in exact arithmetic, with \(x_0=0\). A Stieltjes matrix here means a real symmetric positive definite matrix with nonpositive off-diagonal entries; such a matrix has an entrywise nonnegative inverse.

The theorem does not claim that every Stieltjes system loses positivity, nor that finite-precision implementations reproduce the exact threshold without perturbation. The sharp \(a=4\) boundary is for the displayed three-by-three tridiagonal family and the right-hand-side family \(b_B=(1,0,B)^\mathsf T\).

The statement is about coordinatewise positivity, not the energy norm. Conjugate gradients retains its usual variational and finite-termination properties.

## Proof
For
\[
A_a=
\begin{pmatrix}
a&-1&0\\
-1&2&-1\\
0&-1&2
\end{pmatrix},
\]
the leading principal minors are
\[
a,\qquad 2a-1,\qquad 3a-2.
\]
Hence \(A_a\) is symmetric positive definite exactly when \(a>2/3\). Its inverse is
\[
A_a^{-1}
=
\frac1{3a-2}
\begin{pmatrix}
3&2&1\\
2&2a&a\\
1&a&2a-1
\end{pmatrix},
\]
which is entrywise positive for \(a>2/3\). Thus the exact solution for \(b_B=(1,0,B)^\mathsf T\) is
\[
x_*=
\frac1{3a-2}
\begin{pmatrix}
B+3\\
aB+2\\
(2a-1)B+1
\end{pmatrix}>0.
\]

Starting from \(x_0=0\), the first conjugate-gradient step has
\[
\alpha_0=\frac{B^2+1}{2B^2+a}.
\]
A direct exact substitution into the second recurrence gives
\[
(x_2)_1=\frac{N_a(B)}{Q_a(B)}
\]
with
\[
N_a(B)
=
(4-a)B^4+4B^3+(2a^2-9a+14)B^2+(8-2a)B+2
\]
and
\[
\begin{aligned}
Q_a(B)
={}&3B^4+4(a-1)B^3\\
&+(2a^3-10a^2+18a-10)B^2\\
&+(-2a^2+8a-4)B+(2a-1).
\end{aligned}
\]
The denominator is positive for every \(a>2/3\) and \(B\ge0\). Indeed the second search direction \(p_1\) satisfies
\[
p_1^\mathsf T A_a p_1
=
\frac{(B^2+1)^2}{(2B^2+a)^3}\,Q_a(B),
\]
and the left side is strictly positive because \(A_a\) is positive definite and \(p_1\ne0\). The latter is automatic here because the middle component of the first residual is
\[
\frac{(B+1)(B^2+1)}{2B^2+a}>0.
\]

If \(2/3<a\le4\), then every coefficient of \(N_a(B)\) is nonnegative. The only coefficient requiring comment is
\[
2a^2-9a+14,
\]
whose discriminant is
\[
81-112=-31<0,
\]
so it is strictly positive for every real \(a\). The constant term of \(N_a\) is \(2\), hence
\[
N_a(B)>0
\]
for every \(B\ge0\). Thus no member of this right-hand-side family loses positivity at the second iterate when \(a\le4\).

If \(a>4\), the leading coefficient \(4-a\) is negative. Hence
\[
N_a(B)\longrightarrow-\infty
\]
as \(B\to\infty\), while \(N_a(0)=2\). Therefore all sufficiently large \(B\) yield \((x_2)_1<0\). Since the leading coefficient of \(Q_a(B)\) is \(3\),
\[
\lim_{B\to\infty}(x_2)_1=\frac{4-a}{3}.
\]
This proves the sharp family threshold.

For the explicit witness \(a=5\), \(B=7\), exact recurrence arithmetic gives
\[
\alpha_0=\frac{50}{103},
\qquad
\beta_0=\frac{3641}{10609},
\qquad
\alpha_1=\frac{34093}{75100},
\]
and therefore the displayed negative \(x_2\). The exact solution follows from the inverse formula. Since all conjugate-gradient denominators remain positive on positive definite systems, the second iterate depends continuously on \(b\) in a neighborhood of this witness. The strict inequality \((x_2)_1<0\) therefore persists when the middle entry \(0\) is replaced by a sufficiently small positive number.

It remains to prove dimension minimality. In one dimension, the first conjugate-gradient step is already the exact solution. In two dimensions, the first iterate is
\[
x_1=\alpha_0b,\qquad \alpha_0>0,
\]
so it is nonnegative when \(b\ge0\). If the method has not already terminated, its second iterate is the exact solution in exact arithmetic; that solution is nonnegative when \(A^{-1}\ge0\). Thus no one- or two-dimensional inverse-positive symmetric positive definite system can have a negative exact-arithmetic conjugate-gradient iterate from \(x_0=0\). The three-dimensional witness is therefore dimension-minimal.

## Verification
The accompanying `verify.py` uses only exact rational arithmetic. It reconstructs the conjugate-gradient recurrence for the witness, verifies the inverse formula numerically at multiple rational parameters, checks the exact solution and the negative second iterate, and verifies the polynomial expression for \((x_2)_1\) against direct recurrence evaluation over a grid of rational \((a,B)\) values on both sides of the threshold.

The all-parameter claims do not rely on that finite grid. Positive definiteness, inverse positivity, denominator positivity, the coefficient argument for \(a\le4\), and the negative leading term for \(a>4\) are analytic arguments given above.

## Relationship to prior work
Hestenes and Stiefel introduced conjugate gradients for linear systems and established its finite-step and variational structure. Those foundational properties are prior work.

Meijerink and van der Vorst specifically studied conjugate-gradient solution methods for symmetric \(M\)-matrices, using regular splittings and incomplete factorization. Thus the combination of conjugate gradients with symmetric \(M\)-matrix systems is emphatically prior work and is not claimed here.

More recently, Schmelzer and Stoll explicitly observe that ordinary conjugate gradients for symmetric positive definite systems need not respect the constraint \(x\ge0\), and develop an active-set method that enforces nonnegativity. Therefore the broad fact that a conjugate-gradient iterate can become negative is also prior work.

The present result isolates a sharper structural boundary not found in the checked sources: positivity can fail even when the system matrix itself is inverse-positive, three dimensions are necessary and sufficient for such a transient failure, and the displayed Stieltjes family has the exact threshold \(a=4\) for existence of a negative second iterate under the natural nonnegative forcing family \(b_B\).

## Limitations
The exact threshold \(a=4\) is not asserted to be a universal threshold over all three-dimensional Stieltjes matrices. It is the sharp threshold inside the displayed one-parameter tridiagonal matrix family with right-hand sides \(b_B\).

The full text of Meijerink and van der Vorst's 1977 paper was not recovered through the open and authorized access routes checked during this review; its abstract and bibliographic record were inspected. The full text of the 2026 nonnegative-conjugate-gradient preprint was likewise not available through the checked text route, although its detailed abstract was inspected. Consequently, an equivalent small-dimensional example or specialized Stieltjes observation inside either full text cannot be ruled out. Older literature on positivity of Krylov iterates is an additional residual originality risk.

Finite precision may perturb the precise sign boundary. The theorem is an exact-arithmetic statement.

## References
1. Magnus R. Hestenes and Eduard Stiefel, *Methods of Conjugate Gradients for Solving Linear Systems*, Journal of Research of the National Bureau of Standards 49 (1952), 409--436, DOI: 10.6028/jres.049.044.
2. J. A. Meijerink and H. A. van der Vorst, *An Iterative Solution Method for Linear Systems of Which the Coefficient Matrix is a Symmetric M-Matrix*, Mathematics of Computation 31 (1977), 148--162, DOI: 10.1090/S0025-5718-1977-0438681-4.
3. Steven F. Ashby, Thomas A. Manteuffel, and Paul E. Saylor, *A Taxonomy for Conjugate Gradient Methods*, SIAM Journal on Numerical Analysis 27 (1990), 1542--1568, DOI: 10.1137/0727091.
4. Thomas Schmelzer and Martin Stoll, *Non-Negative Conjugate Gradients*, arXiv:2607.22121v1, July 24, 2026.
