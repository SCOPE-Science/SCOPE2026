# Condition three is the sharp positivity frontier for the degree-three Chebyshev semi-iterate
## Finding
Let
\[
Ax=b,
\qquad
A=A^{\mathsf T}>0,
\]
and assume that \(A\) is a Stieltjes matrix, so its off-diagonal entries are nonpositive. Put
\[
\mu=\lambda_{\min}(A),
\qquad
L=\lambda_{\max}(A),
\qquad
\kappa=\frac{L}{\mu}.
\]
Starting from \(x^{(0)}=0\), consider the degree-three Chebyshev semi-iterative approximation whose error polynomial is
\[
p_3(\lambda)
=
\frac{
T_3\!\left(\dfrac{L+\mu-2\lambda}{L-\mu}\right)
}{
T_3\!\left(\dfrac{L+\mu}{L-\mu}\right)
},
\]
where
\[
T_3(t)=4t^3-3t.
\]
Equivalently,
\[
x^{(3)}=q_2(A)b,
\qquad
q_2(\lambda)=\frac{1-p_3(\lambda)}{\lambda}.
\]

Then
\[
\kappa\le3
\quad\Longrightarrow\quad
x^{(3)}\ge0
\]
componentwise for every dimension and every \(b\ge0\).

The constant \(3\) is sharp. For every prescribed
\[
\kappa>3,
\]
there exists a three-dimensional Stieltjes matrix of condition number exactly \(\kappa\) and a strictly positive right-hand side for which the degree-three Chebyshev approximation has a negative coordinate.

Moreover, dimensions one and two are positivity-safe for this degree-three approximation for every condition number. Hence dimension three is minimal for sign failure.

An explicit strictly positive witness at \(\kappa=4\) is
\[
A=
\begin{pmatrix}
31/8&-1/8&0\\
-1/8&31/8&0\\
0&0&1
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
1/194\\
1\\
1/194
\end{pmatrix}.
\]
Its spectrum is
\[
\{1,15/4,4\}.
\]
For the degree-three Chebyshev polynomial on \([1,4]\),
\[
q_2(A)
=
\frac1{365}
\begin{pmatrix}
97&-1&0\\
-1&97&0\\
0&0&338
\end{pmatrix},
\]
so
\[
x^{(3)}
=
\begin{pmatrix}
-1/730\\
18817/70810\\
169/35405
\end{pmatrix}.
\]
The exact solution is strictly positive:
\[
A^{-1}b
=
\begin{pmatrix}
15/1552\\
401/1552\\
1/194
\end{pmatrix}.
\]

## Assumptions and scope
The theorem concerns the classical Chebyshev minimax polynomial on the exact spectral interval \([\mu,L]\) for a symmetric positive definite system. It is a statement about the final degree-three polynomial approximation, not about positivity of every internal implementation stage.

The Stieltjes sign pattern is essential to the universal condition-number bound. The method itself is defined for general symmetric positive definite matrices, but the proof of entrywise positivity uses nonpositive off-diagonal entries.

The spectral endpoints are assumed exact. If practical estimates strictly enlarge the interval, the degree-three polynomial changes and so can the positivity frontier.

## Proof
For \(\kappa>1\), direct expansion of the scaled Chebyshev polynomial gives
\[
q_2(\lambda)
=
\frac{
2\left[
16\lambda^2
-
24(L+\mu)\lambda
+
9L^2+30L\mu+9\mu^2
\right]
}{
(L+\mu)(L^2+14L\mu+\mu^2)
}.
\]
Write
\[
D=(L+\mu)(L^2+14L\mu+\mu^2)>0.
\]
Then
\[
q_2(A)
=
\frac2D
\left[
16A^2
-
24(L+\mu)A
+
(9L^2+30L\mu+9\mu^2)I
\right].
\]

First consider diagonal entries. On \([\mu,L]\), the scaled argument of \(T_3\) lies in \([-1,1]\), while
\[
T_3\!\left(\frac{L+\mu}{L-\mu}\right)>1.
\]
Hence
\[
|p_3(\lambda)|<1
\]
for every \(\lambda\in[\mu,L]\), and therefore
\[
q_2(\lambda)>0.
\]
Thus \(q_2(A)\) is positive definite, so all of its diagonal entries are positive.

For \(i\ne j\), use
\[
(A^2)_{ij}
=
a_{ij}(a_{ii}+a_{jj})
+
\sum_{\ell\ne i,j}a_{i\ell}a_{\ell j}.
\]
Because \(A\) is Stieltjes,
\[
a_{ij}\le0,
\qquad
a_{i\ell}a_{\ell j}\ge0.
\]
Therefore
\[
(q_2(A))_{ij}
=
\frac2D
\left[
(-a_{ij})
\left(
24(L+\mu)-16(a_{ii}+a_{jj})
\right)
+
16
\sum_{\ell\ne i,j}a_{i\ell}a_{\ell j}
\right].
\]
Every diagonal entry of a symmetric matrix lies between its extreme eigenvalues, so
\[
a_{ii}+a_{jj}\le2L.
\]
If
\[
L\le3\mu,
\]
then
\[
2L\le\frac32(L+\mu),
\]
and consequently
\[
24(L+\mu)-16(a_{ii}+a_{jj})\ge0.
\]
Thus every off-diagonal entry of \(q_2(A)\) is nonnegative. Together with the positive diagonal, this proves
\[
q_2(A)\ge0
\]
entrywise and hence
\[
x^{(3)}=q_2(A)b\ge0
\]
for every \(b\ge0\).

The two-dimensional statement is stronger. If \(A\) is \(2\times2\), then
\[
a_{11}+a_{22}
=
\operatorname{tr}(A)
=
L+\mu
\]
and there is no intermediate-index sum. Hence
\[
(q_2(A))_{12}
=
-\frac{16(L+\mu)}D\,a_{12}\ge0
\]
for every condition number. The diagonal entries remain positive by positive definiteness. Dimension one is immediate.

For sharpness, fix any
\[
\kappa>3
\]
and choose
\[
0<c<\frac{\kappa-3}{4}.
\]
Set
\[
A_{\kappa,c}
=
\begin{pmatrix}
\kappa-c&-c&0\\
-c&\kappa-c&0\\
0&0&1
\end{pmatrix}.
\]
Its eigenvalues are
\[
1,\qquad
\kappa-2c,\qquad
\kappa.
\]
The chosen range of \(c\) gives \(\kappa-2c>1\), so
\[
\kappa(A_{\kappa,c})=\kappa.
\]
For \(\mu=1\), \(L=\kappa\),
\[
(q_2(A_{\kappa,c}))_{12}
=
\frac{
16c(3-\kappa+4c)
}{
(\kappa+1)(\kappa^2+14\kappa+1)
}
<0.
\]
Thus \(b=e_2\) already produces a negative first coordinate. Since the diagonal entry \((q_2(A_{\kappa,c}))_{11}\) is positive, replacing \(e_2\) by
\[
b_\varepsilon=(\varepsilon,1,\varepsilon)^{\mathsf T}
\]
with sufficiently small \(\varepsilon>0\) preserves that negative coordinate and makes the right-hand side strictly positive. The inverse of a Stieltjes matrix is entrywise nonnegative, so the exact solution is nonnegative; in this block-diagonal family it is strictly positive for every strictly positive \(b_\varepsilon\).

The displayed \(\kappa=4\) example follows by taking
\[
c=\frac18
\]
and evaluating \(q_2(A)\) exactly.

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It checks the closed form of \(q_2\) against the defining Chebyshev polynomial at many rational spectral intervals and evaluation points.

It verifies the general three-dimensional sharpness identity
\[
(q_2(A_{\kappa,c}))_{12}
=
\frac{
16c(3-\kappa+4c)
}{
(\kappa+1)(\kappa^2+14\kappa+1)
}
\]
for rational \(\kappa>3\) and admissible \(c\).

For the explicit \(\kappa=4\) witness, it reconstructs \(q_2(A)\) exactly, multiplies by the strictly positive \(b\), verifies the negative first coordinate, and checks the displayed positive exact solution.

The universal \(\kappa\le3\) theorem and the all-condition-number two-dimensional theorem are analytic consequences of the matrix-entry identities above; finite tests are not used in place of those proofs.

## Relationship to prior work
Chebyshev semi-iteration is classical. Golub and Varga formulate semi-iterative acceleration through minimax polynomials and identify the Chebyshev polynomial as the unique spectral minimax choice. Gutknecht and Röllin revisit the classical three-term Chebyshev iteration and describe its interval-scaled recurrence for symmetric definite systems. Those construction and convergence facts are prior work.

Modern numerical-linear-algebra literature also uses Chebyshev polynomial acceleration and classifies such iterative linear-system methods under MSC \(65F10\). Those classification and implementation facts are not claimed here.

A nearby recent result studies a different constraint: Euclidean nonexpansion of every individual Richardson stage in an optimized two-step schedule. The present theorem instead asks whether the final degree-three Chebyshev polynomial maps every nonnegative right-hand side of a Stieltjes system to a nonnegative approximation. The exact condition-number frontier \(3\), the all-condition-number two-dimensional immunity, and the matching three-dimensional obstruction address that coordinatewise finite-horizon question.

Targeted searches under Chebyshev semi-iteration, Stieltjes and \(M\)-matrix terminology, positive-orthant invariance, degree-three polynomial iteration, and condition-number-\(3\) aliases did not locate an implication-equivalent theorem.

## Limitations
The result is specific to degree three. Higher-degree Chebyshev polynomials contain higher powers of \(A\), whose entry signs involve longer graph paths, and are not classified here.

The theorem concerns the final polynomial approximation. A particular ordered Richardson implementation may have negative intermediate stages even when the final degree-three approximation is nonnegative.

The result uses the exact spectral interval. Robustness under inaccurate spectral bounds is a separate question.

Classical semi-iterative and \(M\)-matrix literatures are extensive. An older monotone-iteration source may contain the same finite-horizon coordinatewise criterion under different terminology; this remains the principal originality risk.

## References
1. Gene H. Golub and Richard S. Varga, *Chebyshev Semi-Iterative Methods, Successive Overrelaxation Iterative Methods, and Second Order Richardson Iterative Methods*, Numerische Mathematik 3 (1961), Parts I and II.
2. Martin H. Gutknecht and Stefan Röllin, *The Chebyshev Iteration Revisited*, Parallel Computing 28 (2002), 263--283, DOI: 10.1016/S0167-8191(01)00139-9.
3. Bing Zheng, Liying Duan, and Ke Wang, *Chebyshev Polynomial Acceleration for Block SOR Methods for Solving the Rank-Deficient Least-Squares Problem*, International Journal of Computer Mathematics 88 (2011), 6--20, DOI: 10.1080/00207160903456831.
