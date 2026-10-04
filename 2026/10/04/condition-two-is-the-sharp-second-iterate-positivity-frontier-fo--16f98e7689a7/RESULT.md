# Condition two is the sharp second-iterate positivity frontier for steepest descent
## Finding
Consider exact-line-search steepest descent for
\[
Ax=b,
\qquad
A=A^{\mathsf T}>0,
\]
started from
\[
x^{(0)}=0.
\]
Write
\[
r^{(k)}=b-Ax^{(k)},
\qquad
\alpha_k=
\frac{(r^{(k)})^{\mathsf T}r^{(k)}}
{(r^{(k)})^{\mathsf T}Ar^{(k)}},
\qquad
x^{(k+1)}=x^{(k)}+\alpha_k r^{(k)}.
\]

Assume first that \(A\) is a Stieltjes matrix: it is symmetric positive definite and has nonpositive off-diagonal entries. Let
\[
\kappa(A)=\frac{\lambda_{\max}(A)}{\lambda_{\min}(A)}.
\]
For every dimension and every \(b\ge0\),
\[
\kappa(A)\le2
\quad\Longrightarrow\quad
x^{(1)}\ge0
\ \text{and}\
x^{(2)}\ge0
\]
componentwise.

The constant \(2\) is sharp. For every prescribed
\[
\kappa>2
\]
there is a three-dimensional diagonal positive definite matrix of condition number exactly \(\kappa\), hence a Stieltjes matrix, and a strictly positive right-hand side for which the second steepest-descent iterate has a negative coordinate. One explicit family is
\[
A_\kappa=
\operatorname{diag}
\left(
1,\frac{\kappa}{2},\kappa
\right),
\qquad
b_\varepsilon=
\begin{pmatrix}
1\\
1\\
\varepsilon
\end{pmatrix}.
\]
If
\[
0<\varepsilon^2<
\frac{(\kappa-2)^3}
{\kappa^3+8\kappa^2-16\kappa+8},
\]
then
\[
\bigl(x^{(2)}\bigr)_3<0.
\]

For example,
\[
A=
\operatorname{diag}(1,2,4),
\qquad
b=
\begin{pmatrix}
1\\
1\\
1/5
\end{pmatrix}
\]
gives
\[
\alpha_0=\frac{51}{79},
\qquad
x^{(1)}
=
\begin{pmatrix}
51/79\\
51/79\\
51/395
\end{pmatrix}>0,
\]
while
\[
\alpha_1=\frac{969}{2171}
\]
and
\[
x^{(2)}
=
\begin{pmatrix}
137853/171509\\
88434/171509\\
-10404/857545
\end{pmatrix}.
\]
The exact solution is
\[
A^{-1}b=
\begin{pmatrix}
1\\
1/2\\
1/20
\end{pmatrix}>0.
\]

There is a second sharp low-dimensional statement. If \(A\) is a one- or two-dimensional Stieltjes matrix and \(b\ge0\), then every exact-line-search steepest-descent iterate from \(0\) is componentwise nonnegative. Hence dimension three and the second iterate are jointly minimal for a sign failure.

## Assumptions and scope
All statements use exact real arithmetic and the classical steepest-descent or Cauchy step for a symmetric positive definite linear system. The Stieltjes assumption is used for the universal condition-number result because it makes the off-diagonal entries of a certain second-iterate matrix nonnegative.

The all-iterate result in dimensions at most two only needs \(b\ge0\) and \(A^{-1}b\ge0\); Stieltjes matrices automatically satisfy the latter implication because their inverses are nonnegative.

The theorem concerns coordinatewise positivity of iterates. It does not assert objective monotonicity beyond the usual steepest-descent property, and it does not classify later iterates in dimensions three or larger.

## Proof
Let
\[
\mu_k=\frac1{\alpha_k}
=
\frac{(r^{(k)})^{\mathsf T}Ar^{(k)}}
{(r^{(k)})^{\mathsf T}r^{(k)}}
\]
whenever \(r^{(k)}\ne0\). Thus each \(\mu_k\) is a Rayleigh quotient and satisfies
\[
\lambda_{\min}(A)\le\mu_k\le\lambda_{\max}(A).
\]

The first iterate is
\[
x^{(1)}=\alpha_0b\ge0.
\]
If \(r^{(1)}=0\), then \(x^{(1)}\) is already the exact solution and there is nothing more to prove. Otherwise,
\[
x^{(2)}
=
\alpha_0b+\alpha_1\left(b-\alpha_0Ab\right).
\]
Using
\[
\alpha_0+\alpha_1
=
\alpha_0\alpha_1(\mu_0+\mu_1),
\]
we obtain the exact identity
\[
x^{(2)}
=
\alpha_0\alpha_1
\left[
(\mu_0+\mu_1)I-A
\right]b.
\]
If \(A\) is Stieltjes, all off-diagonal entries of the bracketed matrix are nonnegative. Also
\[
\mu_0+\mu_1
\ge
2\lambda_{\min}(A).
\]
When \(\kappa(A)\le2\),
\[
2\lambda_{\min}(A)
\ge
\lambda_{\max}(A)
\ge
a_{ii}
\]
for every diagonal entry. Therefore
\[
(\mu_0+\mu_1)I-A
\]
is entrywise nonnegative, proving
\[
x^{(2)}\ge0.
\]

To prove sharpness for every \(\kappa>2\), consider the displayed diagonal family. For a diagonal system with positive entries, the second iterate has the coordinate formula
\[
\bigl(x^{(2)}\bigr)_i
=
\frac{b_i}{\mu_0\mu_1}
\left(
\mu_0+\mu_1-\lambda_i
\right).
\]
For
\[
A_\kappa=
\operatorname{diag}
\left(
1,\frac{\kappa}{2},\kappa
\right),
\qquad
b_\varepsilon=(1,1,\varepsilon)^{\mathsf T},
\]
put
\[
t=\varepsilon^2.
\]
A direct rational simplification gives
\[
\kappa-(\mu_0+\mu_1)
=
\frac{
(\kappa-2)^3
-
t\left(
\kappa^3+8\kappa^2-16\kappa+8
\right)
}
{
2\left[
(\kappa-2)^2+
t\left(
5\kappa^2-8\kappa+4
\right)
\right]
}.
\]
The denominator is positive. Hence the stated bound on \(\varepsilon\) makes
\[
\mu_0+\mu_1-\kappa<0,
\]
and therefore
\[
\bigl(x^{(2)}\bigr)_3<0.
\]
The explicit \(\kappa=4\) witness follows by exact substitution.

It remains to prove positivity of every iterate in dimension two. Let
\[
0<\lambda_1\le\lambda_2
\]
be the eigenvalues of \(A\). The scalar-matrix case and the case in which \(b\) is an eigenvector terminate in one step, so suppose both eigencomponents of \(b\) are nonzero and \(\lambda_1<\lambda_2\). In an orthonormal eigenbasis write the squared components of \(b\) as
\[
p>0,
\qquad
q>0.
\]
The first two reciprocal step lengths are
\[
\mu_0=
\frac{\lambda_1p+\lambda_2q}{p+q},
\qquad
\mu_1=
\frac{\lambda_1q+\lambda_2p}{p+q},
\]
so in particular
\[
\mu_0+\mu_1=\lambda_1+\lambda_2.
\]

A direct two-step residual calculation gives
\[
r^{(2)}=\rho\,r^{(0)},
\]
where
\[
\rho=
\frac{
pq(\lambda_2-\lambda_1)^2
}{
(\lambda_1p+\lambda_2q)
(\lambda_1q+\lambda_2p)
}.
\]
Moreover,
\[
0<\rho<1,
\]
because
\[
(\lambda_1p+\lambda_2q)
(\lambda_1q+\lambda_2p)
-
pq(\lambda_2-\lambda_1)^2
=
\lambda_1\lambda_2(p+q)^2>0.
\]
Scaling a residual does not change its exact steepest-descent step length, so induction yields
\[
r^{(2m)}=\rho^m b,
\qquad
r^{(2m+1)}=\rho^m r^{(1)}.
\]
Let
\[
x^*=A^{-1}b.
\]
Since
\[
r^{(k)}=A(x^*-x^{(k)}),
\]
we obtain
\[
x^{(2m)}
=
(1-\rho^m)x^*
\]
and
\[
x^{(2m+1)}
=
(1-\rho^m)x^*
+
\rho^m\alpha_0b.
\]
If \(b\ge0\) and \(x^*\ge0\), both expressions are componentwise nonnegative for every \(m\). This proves the all-iterate two-dimensional statement and, together with the three-dimensional counterexample, the minimal-dimension claim.

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It verifies the second-iterate identity
\[
x^{(2)}
=
\alpha_0\alpha_1
\left[
(\mu_0+\mu_1)I-A
\right]b
\]
on a collection of rational Stieltjes systems.

It checks the exact \(\kappa=4\) witness, including both step lengths, both iterates, and the positive exact solution. It also symbolically checks the rational numerator controlling the family \(A_\kappa\), \(b_\varepsilon\) at many rational values of \(\kappa>2\) and admissible \(\varepsilon\).

For two-dimensional systems, the checker verifies the two-step residual multiplier and the closed formulas for even and odd iterates over many rational diagonal examples. The all-matrix two-dimensional result and the universal \(\kappa\le2\) theorem are proved analytically above; finite replay is corroborative rather than exhaustive.

## Relationship to prior work
Exact-line-search steepest descent for positive definite quadratic problems is classical. Knyazev and Lashuk formulate steepest descent for symmetric positive definite linear systems, record its standard residual and optimal-step update, and give a geometric convergence analysis. Their paper is indexed primarily under MSC \(65F10\).

Gonzaga and Schneider give a detailed account of the classical Cauchy algorithm on quadratic functions. They diagonalize the quadratic, write the exact Cauchy step, emphasize the orthogonality of successive gradients, and develop the Akaike--Forsythe oscillation theory. In particular, two-mode oscillation and alternating spectral behavior are established background facts.

The present theorem asks a different finite-horizon, coordinatewise question. It identifies an exact condition-number frontier for positivity of the second iterate on the entire Stieltjes class, proves that the frontier is sharp through a three-dimensional diagonal family for every larger condition number, and shows that no coordinate sign failure is possible at any iteration in dimensions one or two when the solution is nonnegative.

Targeted searches under steepest-descent, Cauchy-method, Stieltjes, \(M\)-matrix, positive-orthant, second-iterate, and condition-number terminology did not locate a statement implying this combined positivity frontier. Classical convergence-rate and oscillation results do not by themselves impose coordinatewise signs in the original basis.

## Limitations
The sharp condition-number statement concerns only the second iterate. In dimensions three and higher, later iterates can have different positivity behavior even when the second iterate is nonnegative.

The Stieltjes sign pattern is essential to the universal \(\kappa\le2\) argument. A general symmetric positive definite matrix with a nonnegative solution need not make the matrix
\[
(\mu_0+\mu_1)I-A
\]
entrywise nonnegative.

Classical steepest-descent literature is extensive, and some older monotone-iteration source may contain an equivalent finite-horizon positivity statement under different terminology. The full texts inspected here focus on convergence, oscillation, preconditioning, and spectral behavior rather than orthant invariance; this remains the main originality risk.

## References
1. Andrew V. Knyazev and Ilya Lashuk, *Steepest Descent and Conjugate Gradient Methods with Variable Preconditioning*, arXiv:math/0605767v1, May 30, 2006; SIAM Journal on Matrix Analysis and Applications 29 (2007/08), 1267--1280, DOI: 10.1137/060675290.
2. Clóvis C. Gonzaga and Ruana M. Schneider, *On the Steepest Descent Algorithm for Quadratic Functions*, Optimization Online, June 15, 2015; Computational Optimization and Applications 63 (2016), 523--542.
