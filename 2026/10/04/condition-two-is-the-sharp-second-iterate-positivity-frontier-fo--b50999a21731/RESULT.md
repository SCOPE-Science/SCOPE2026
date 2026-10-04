# Condition two is the sharp second-iterate positivity frontier for MINRES
## Finding
Let
\[
Ax=b,\qquad A=A^{\mathsf T}>0,
\]
with \(A\) a Stieltjes matrix, and start MINRES from \(x^{(0)}=0\). Write
\[
\mu=\lambda_{\min}(A),\qquad
L=\lambda_{\max}(A),\qquad
\kappa(A)=L/\mu.
\]
Then
\[
\kappa(A)\le2
\quad\Longrightarrow\quad
x^{(1)}\ge0,\qquad x^{(2)}\ge0
\]
componentwise for every \(b\ge0\).

The constant \(2\) is sharp. For every prescribed
\[
\kappa>2
\]
there exists a three-dimensional diagonal positive definite matrix of condition number exactly \(\kappa\), hence a Stieltjes matrix, and a strictly positive right-hand side for which the second MINRES iterate has a negative coordinate.

More precisely, take
\[
A_\kappa=
\operatorname{diag}\left(1,\frac{\kappa}{2},\kappa\right),
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
{\kappa^4+16(\kappa-1)^2},
\]
then
\[
\bigl(x^{(2)}\bigr)_3<0.
\]

For example,
\[
A=\operatorname{diag}(1,2,4),
\qquad
b=
\begin{pmatrix}
1\\
1\\
1/10
\end{pmatrix}
\]
has strictly positive exact solution
\[
A^{-1}b=
\begin{pmatrix}
1\\
1/2\\
1/40
\end{pmatrix},
\]
while MINRES gives
\[
x^{(1)}
=
\begin{pmatrix}
76/129\\
76/129\\
38/645
\end{pmatrix}>0
\]
and
\[
x^{(2)}
=
\begin{pmatrix}
22/25\\
109/200\\
-1/80
\end{pmatrix}.
\]

There is also a sharp dimension statement. In dimensions one and two, MINRES reaches the exact solution in at most two steps, so for every Stieltjes matrix and every \(b\ge0\),
\[
x^{(k)}\ge0
\]
for every iterate that is produced. Hence dimension three and iteration two are jointly minimal for coordinatewise sign loss.

## Assumptions and scope
All statements use exact arithmetic and the unpreconditioned MINRES residual-minimizing Krylov method with \(x^{(0)}=0\). The matrix is symmetric positive definite and Stieltjes, meaning that its off-diagonal entries are nonpositive. This implies \(A^{-1}\ge0\).

The theorem concerns the first two MINRES approximations. It does not classify later MINRES iterates in dimensions at least three, preconditioned MINRES, indefinite systems, or non-Stieltjes positive definite matrices.

The result is coordinatewise. It is distinct from monotonicity of residual norms, Euclidean solution norms, error norms, or quadratic objectives.

## Proof
MINRES chooses
\[
x^{(k)}
=
\arg\min_{x\in\mathcal K_k(A,b)}
\|b-Ax\|_2,
\]
where
\[
\mathcal K_k(A,b)
=
\operatorname{span}\{b,Ab,\ldots,A^{k-1}b\}.
\]

The first iterate has the form
\[
x^{(1)}=\alpha b,
\qquad
\alpha=
\frac{b^{\mathsf T}Ab}{b^{\mathsf T}A^2b}>0,
\]
so \(x^{(1)}\ge0\) whenever \(b\ge0\).

For the second iterate write
\[
x^{(2)}=c_0b+c_1Ab.
\]
Define spectral moments
\[
m_j=b^{\mathsf T}A^jb,\qquad j=1,2,3,4.
\]
The residual
\[
r=b-Ax^{(2)}
\]
is orthogonal to
\[
A\mathcal K_2(A,b)=\operatorname{span}\{Ab,A^2b\}.
\]
Thus
\[
m_1-c_0m_2-c_1m_3=0,
\qquad
m_2-c_0m_3-c_1m_4=0.
\]
When \(b\) has spectral support on at least two distinct eigenvalues,
\[
\Delta=m_2m_4-m_3^2>0
\]
and
\[
c_0=
\frac{m_1m_4-m_2m_3}{\Delta},
\qquad
c_1=
-\frac{m_1m_3-m_2^2}{\Delta}.
\]
Set
\[
\beta=-c_1>0,
\qquad
\theta=\frac{c_0}{\beta}.
\]
Then
\[
x^{(2)}
=
\beta(\theta I-A)b.
\]

Let
\[
A=U\operatorname{diag}(\lambda_1,\ldots,\lambda_n)U^{\mathsf T},
\qquad
w_i=(u_i^{\mathsf T}b)^2.
\]
A pairwise expansion of the moments gives
\[
m_1m_3-m_2^2
=
\sum_{i<j}
w_iw_j\lambda_i\lambda_j(\lambda_i-\lambda_j)^2
\]
and
\[
m_1m_4-m_2m_3
=
\sum_{i<j}
w_iw_j\lambda_i\lambda_j(\lambda_i-\lambda_j)^2
(\lambda_i+\lambda_j).
\]
Therefore
\[
\theta
=
\frac{
\sum_{i<j}
\omega_{ij}(\lambda_i+\lambda_j)
}{
\sum_{i<j}\omega_{ij}
},
\qquad
\omega_{ij}
=
w_iw_j\lambda_i\lambda_j(\lambda_i-\lambda_j)^2\ge0.
\]
Thus \(\theta\) is an exact weighted average of pairwise spectral sums and
\[
2\mu\le\theta\le2L.
\]

Since \(A\) is Stieltjes, the off-diagonal entries of
\[
\theta I-A
\]
are nonnegative. If \(L\le2\mu\), then
\[
\theta\ge2\mu\ge L\ge a_{ii}
\]
for every \(i\), so the diagonal entries are also nonnegative. Hence
\[
x^{(2)}
=
\beta(\theta I-A)b\ge0.
\]

If \(b\) is supported on only one eigenspace, MINRES solves the system in one step, and the same positivity conclusion is immediate.

To prove sharpness, take
\[
A_\kappa=
\operatorname{diag}
\left(1,\frac{\kappa}{2},\kappa\right),
\qquad
b_\varepsilon=(1,1,\varepsilon)^{\mathsf T},
\]
and put
\[
t=\varepsilon^2.
\]
The pairwise formula gives
\[
\kappa-\theta
=
\frac{
(\kappa-2)^3
-
t\left[\kappa^4+16(\kappa-1)^2\right]
}{
2\left[
(\kappa-2)^2
+
t(\kappa^3+8\kappa^2-16\kappa+8)
\right]
}.
\]
The denominator is positive. Hence the displayed bound on \(t\) implies
\[
\theta<\kappa
\]
and therefore
\[
\bigl(x^{(2)}\bigr)_3
=
\beta(\theta-\kappa)\varepsilon<0.
\]

For dimension two, \(\dim\mathcal K_2(A,b)\le2\). If the grade of \(b\) is one, MINRES terminates in one step; otherwise \(\mathcal K_2(A,b)=\mathbb R^2\), so the residual-minimizing second iterate is the exact solution \(A^{-1}b\ge0\). This proves the minimal-dimension statement.

## Verification
The accompanying `verify.py` uses exact rational arithmetic.

It reconstructs the second MINRES iterate from the normal equations, checks the signs of \(c_0\) and \(c_1\), and independently verifies the pairwise moment identities for many rational diagonal systems.

For the sharpness family it verifies the closed expression for \(\kappa-\theta\) at rational values of \(\kappa>2\) and on both sides of the stated \(\varepsilon\) threshold.

For the explicit \(\kappa=4\) witness it checks the exact first and second MINRES iterates, the negative third component, and the strictly positive exact solution.

The universal Stieltjes result is proved analytically by the spectral-barycenter identity and is not inferred from finite sampling.

## Relationship to prior work
MINRES is a classical residual-minimizing Krylov method for symmetric systems. Choi, Paige, and Saunders review MINRES as the method that minimizes
\[
\|b-Ax\|_2
\]
over each Krylov subspace, and develop MINRES-QLP for singular or ill-conditioned problems. Fong and Saunders study MINRES on positive definite systems and prove monotonicity of solution norms, error norms, residual norms, and backward errors. Liu and Roosta later develop further monotonicity and negative-curvature properties of MINRES.

These are prior results and are not claimed here. None of the inspected sources states coordinatewise nonnegativity of MINRES iterates on Stieltjes systems. In particular, norm monotonicity does not imply preservation of the positive orthant.

The present result isolates the first nontrivial coordinatewise question and solves it sharply. The key structural identity is that the zero of the affine second-step solution polynomial is a weighted average of pairwise spectral sums. This produces the exact robust frontier
\[
\kappa=2,
\]
a matching counterexample for every larger condition number, and the minimal-dimension classification.

## Limitations
The theorem is finite-horizon: it does not determine coordinate signs of later MINRES iterates in dimensions at least three.

Preconditioning changes both the Krylov subspaces and the coordinate system in which the residual is minimized, so the unpreconditioned result should not be transferred automatically to preconditioned MINRES.

MINRES and conjugate-residual literature is extensive. An older monotone-iteration or \(M\)-matrix source may contain an equivalent low-degree polynomial sign criterion under different terminology. This remains the principal originality risk.

## References
1. Sou-Cheng T. Choi, Christopher C. Paige, and Michael A. Saunders, *MINRES-QLP: A Krylov Subspace Method for Indefinite or Singular Symmetric Systems*, Optimization Online, first posted March 16, 2010; SIAM Journal on Scientific Computing 33 (2011), 1810--1836, DOI: 10.1137/100787921.
2. David Chin-Lung Fong and Michael A. Saunders, *CG Versus MINRES: An Empirical Comparison*, Sultan Qaboos University Journal for Science 17 (2012), 44--62, DOI: 10.24200/squjs.vol17iss1pp44-62.
3. Mark Embree, Josef A. Sifuentes, Kirk M. Soodhalter, Daniel B. Szyld, and Fei Xue, *Short-Term Recurrence Krylov Subspace Methods for Nearly Hermitian Matrices*, SIAM Journal on Matrix Analysis and Applications 33 (2012), 480--500, DOI: 10.1137/110851006.
4. Yang Liu and Fred Roosta, *MINRES: From Negative Curvature Detection to Monotonicity Properties*, arXiv:2206.05732; SIAM Journal on Optimization 32 (2022), 2636--2661, DOI: 10.1137/21M143666X.
