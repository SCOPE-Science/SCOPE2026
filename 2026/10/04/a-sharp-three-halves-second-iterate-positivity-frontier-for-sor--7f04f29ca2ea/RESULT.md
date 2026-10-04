# A sharp three-halves second-iterate positivity frontier for SOR
## Finding
Consider forward successive overrelaxation for
\[
Ax=b,
\]
started from
\[
x^{(0)}=0,
\]
with relaxation factor
\[
0<\omega<2.
\]
For every nonsingular \(M\)-matrix and every \(b\ge0\), the first SOR iterate is nonnegative. In one dimension, every iterate is nonnegative throughout the convergent range. Thus a negative SOR iterate, if it occurs, can appear no earlier than the second iterate and in no dimension smaller than two.

For a \(2\times2\) symmetric positive definite Stieltjes matrix
\[
A=
\begin{pmatrix}
a&-c\\
-c&b
\end{pmatrix},
\qquad
a>0,\quad b>0,\quad 0\le c<\sqrt{ab},
\]
put
\[
\rho=\frac{c}{\sqrt{ab}}\in[0,1).
\]
Positive diagonal scaling reduces the system to
\[
\widehat A=
\begin{pmatrix}
1&-\rho\\
-\rho&1
\end{pmatrix}
\]
without changing coordinatewise signs.

For the normalized system, the second SOR iterate is
\[
y^{(2)}=P_2(\rho,\omega)g,
\]
where
\[
P_2(\rho,\omega)=
\begin{pmatrix}
\omega(2-\omega+\omega^2\rho^2)&\rho\omega^2\\
\rho\omega^2(3-2\omega+\omega^2\rho^2)&
\omega(2-\omega+\omega^2\rho^2)
\end{pmatrix}.
\]
Every entry is nonnegative except possibly the lower-left entry. Hence the exact fixed-coupling criterion is
\[
y^{(2)}\ge0
\quad\text{for every }g\ge0
\]
if and only if
\[
3-2\omega+\omega^2\rho^2\ge0.
\]

This gives the complete phase diagram in the convergent SOR range. If
\[
\rho\ge\frac12,
\]
then the second iterate is nonnegative for every nonnegative right-hand side and every
\[
0<\omega<2.
\]
If
\[
0<\rho<\frac12,
\]
define
\[
\omega_*(\rho)
=
\frac{1-\sqrt{1-3\rho^2}}{\rho^2}
=
\frac{3}{1+\sqrt{1-3\rho^2}}.
\]
Then
\[
y^{(2)}\ge0\ \text{for every }g\ge0
\quad\Longleftrightarrow\quad
0<\omega\le\omega_*(\rho).
\]

Taking the worst case over every \(2\times2\) positive definite Stieltjes matrix gives the sharp universal threshold
\[
\boxed{\omega=\frac32}.
\]
More precisely, every such system with \(b\ge0\) has
\[
x^{(2)}\ge0
\]
for every
\[
0<\omega\le\frac32.
\]
For every
\[
\frac32<\omega<2,
\]
there is a positive definite Stieltjes matrix and a strictly positive right-hand side for which the first iterate is positive, the exact solution is positive, SOR converges, but the second iterate has a negative component.

An exact witness is
\[
A=
\begin{pmatrix}
1&-1/5\\
-1/5&1
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
1\\
1/10
\end{pmatrix},
\qquad
\omega=\frac53.
\]
Then
\[
x^{(1)}
=
\begin{pmatrix}
5/3\\
13/18
\end{pmatrix}>0,
\]
but
\[
x^{(2)}
=
\begin{pmatrix}
43/54\\
-4/81
\end{pmatrix},
\]
while the exact solution is
\[
A^{-1}b=
\begin{pmatrix}
17/16\\
5/16
\end{pmatrix}>0.
\]

## Assumptions and scope
The theorem uses the standard forward SOR ordering. With
\[
A=D-L-U,
\]
where \(D\) is the positive diagonal and \(L,U\ge0\) are the strict lower and upper parts in the \(M\)-matrix sign convention, the iteration is
\[
(D-\omega L)x^{(k+1)}
=
\bigl[(1-\omega)D+\omega U\bigr]x^{(k)}
+\omega b.
\]

The sharp \(\omega=3/2\) statement is a robust result over all \(2\times2\) symmetric positive definite Stieltjes matrices. It is not claimed for every dimension, for nonsymmetric \(M\)-matrices at the second iterate, for symmetric SOR, or for later iterates after the second.

The matrix is assumed exact and the ordering is fixed. Permuting the variables changes the forward SOR sweep and can change finite-iterate signs, although it does not change the positive definiteness of the underlying Stieltjes system.

## Proof
For a general nonsingular \(M\)-matrix,
\[
A=D-L-U
\]
with \(D>0\) diagonal and \(L,U\ge0\). Starting from zero gives
\[
x^{(1)}
=
\omega(D-\omega L)^{-1}b.
\]
Since \(D^{-1}L\) is strictly lower triangular and nilpotent,
\[
(D-\omega L)^{-1}
=
\left(
\sum_{j=0}^{n-1}
(\omega D^{-1}L)^j
\right)D^{-1}\ge0.
\]
Therefore
\[
x^{(1)}\ge0.
\]

In one dimension the SOR recurrence is
\[
x^{(k+1)}
=
(1-\omega)x^{(k)}
+
\omega\frac ba.
\]
With \(x^{(0)}=0\),
\[
x^{(k)}
=
\left[1-(1-\omega)^k\right]\frac ba.
\]
For \(0<\omega<2\), one has \(-1<1-\omega<1\), so the bracket is positive for every \(k\ge1\). This proves the minimal-iteration and minimal-dimension statements.

Now take
\[
A=
\begin{pmatrix}
a&-c\\
-c&b
\end{pmatrix}.
\]
Let
\[
S=\operatorname{diag}(\sqrt a,\sqrt b).
\]
Then
\[
A=S\widehat A S,
\qquad
\widehat A=
\begin{pmatrix}
1&-\rho\\
-\rho&1
\end{pmatrix},
\qquad
\rho=\frac{c}{\sqrt{ab}}.
\]
Writing
\[
y=Sx,\qquad g=S^{-1}b,
\]
transforms the SOR equations into the same forward SOR equations for \(\widehat A y=g\). Since \(S\) has positive diagonal entries, coordinatewise signs are preserved.

For the normalized system, write
\[
\widehat A=I-L-U,
\quad
L=
\begin{pmatrix}
0&0\\
\rho&0
\end{pmatrix},
\quad
U=
\begin{pmatrix}
0&\rho\\
0&0
\end{pmatrix}.
\]
The iteration has the affine form
\[
y^{(k+1)}=Ty^{(k)}+Gg,
\]
where
\[
T=(I-\omega L)^{-1}\bigl[(1-\omega)I+\omega U\bigr],
\qquad
G=\omega(I-\omega L)^{-1}.
\]
Since \(y^{(0)}=0\),
\[
y^{(1)}=Gg,
\qquad
y^{(2)}=(TG+G)g.
\]
Direct multiplication gives
\[
G=
\begin{pmatrix}
\omega&0\\
\rho\omega^2&\omega
\end{pmatrix}
\]
and the displayed matrix \(P_2=TG+G\).

For \(0<\omega<2\) and \(0\le\rho<1\),
\[
\omega(2-\omega+\omega^2\rho^2)>0,
\qquad
\rho\omega^2\ge0.
\]
Thus the sign of \(P_2\) is controlled entirely by
\[
f_\rho(\omega)=3-2\omega+\rho^2\omega^2.
\]

If \(\rho\ge1/2\), then \(f_\rho(\omega)>0\) for every \(0<\omega<2\). Indeed, when \(1/2\le\rho\le1/\sqrt3\), the quadratic decreases throughout \((0,2)\) and
\[
f_\rho(2)=4\rho^2-1\ge0;
\]
when \(\rho>1/\sqrt3\), its discriminant is negative.

If \(0<\rho<1/2\), then
\[
f_\rho(0)=3>0,
\qquad
f_\rho(2)=4\rho^2-1<0.
\]
The unique root in \((0,2)\) is
\[
\omega_*(\rho)
=
\frac{1-\sqrt{1-3\rho^2}}{\rho^2}
=
\frac{3}{1+\sqrt{1-3\rho^2}},
\]
which proves the fixed-coupling phase diagram.

Finally,
\[
\inf_{0<\rho<1/2}\omega_*(\rho)=\frac32,
\]
with the infimum approached as \(\rho\to0^+\). Equivalently, if
\[
0<\omega\le\frac32,
\]
then
\[
3-2\omega+\rho^2\omega^2\ge0
\]
for every \(\rho\in[0,1)\). If
\[
\frac32<\omega<2,
\]
choose
\[
0<\rho^2<\frac{2\omega-3}{\omega^2}.
\]
Then the lower-left entry of \(P_2\) is negative. A strictly positive right-hand side
\[
g=(1,\varepsilon)^{\mathsf T}
\]
still yields a negative second component whenever
\[
0<\varepsilon<
\frac{\rho\omega(2\omega-3-\omega^2\rho^2)}
{2-\omega+\omega^2\rho^2}.
\]
This proves sharpness with strictly positive data.

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It reconstructs the forward SOR update for the normalized matrix
\[
\begin{pmatrix}
1&-\rho\\
-\rho&1
\end{pmatrix}
\]
and independently verifies the first- and second-iterate response matrices on multiple rational values of \(\rho\) and \(\omega\).

It checks the exact witness
\[
\rho=\frac15,
\qquad
\omega=\frac53,
\qquad
g=(1,1/10)^{\mathsf T},
\]
including the positive first iterate, negative second component, and positive exact solution. It also checks representative points on both sides of the sharp robust frontier.

The all-\(\rho\), all-\(\omega\) phase diagram is established analytically by the quadratic sign argument in the proof; finite replay is corroborative rather than a substitute for that proof.

## Relationship to prior work
Classical SOR theory is primarily asymptotic. James and Riha study convergence criteria for SOR on \(L\)-matrices and characterize symmetric irreducible \(L\)-matrices that are positive definite, namely Stieltjes matrices, through generalized diagonal dominance. Their paper therefore covers the matrix class and convergence setting used here.

Chang studies spectral-radius bounds for SOR on nonsingular \(M\)-matrices and gives an explicit \(2\times2\) \(M\)-matrix example with overrelaxation. Lu develops a generalization of SOR and lists the numerical linear algebra classification \(65F10\). These sources establish the standard SOR iteration matrix, its parameter range, and its convergence theory.

Yun points out that for \(\omega>1\), the SOR splitting of an \(M\)-matrix cannot be a weak regular splitting. This is a matrix-splitting obstruction, not a finite-horizon statement. In particular, the present theorem shows a different phenomenon: despite loss of weak regularity as soon as \(\omega>1\), every two-variable Stieltjes problem started from zero remains coordinatewise nonnegative through the second iterate uniformly all the way to the larger sharp value \(\omega=3/2\).

The claimed contribution is the exact finite-iterate positivity phase diagram, the robust three-halves threshold, and the proof that the second iterate in dimension two is the earliest possible setting for a convergent SOR trajectory with a positive exact solution to develop a negative coordinate.

## Limitations
The theorem stops at the second iterate. It does not assert that
\[
\omega\le\frac32
\]
keeps every later SOR iterate nonnegative in two dimensions.

The closest source on weak regularity for overrelaxed \(M\)-matrix SOR was available at abstract level but not as a verified full text during this review, so a finite-iterate observation hidden there cannot be excluded. Classical monographs and older work on monotone matrix iterations may also contain an equivalent low-dimensional calculation under different terminology.

The robust threshold is specific to symmetric positive definite \(2\times2\) Stieltjes matrices. Nonsymmetric \(M\)-matrices can have different finite-iterate behavior.

## References
1. K. R. James and W. Riha, *Convergence Criteria for Successive Overrelaxation*, SIAM Journal on Numerical Analysis 12 (1975), 137--143, DOI: 10.1137/0712013.
2. Da-Wei Chang, *A Note on the Upper Bound of the Spectral Radius for SOR Iteration Matrix*, Journal of Computational and Applied Mathematics 167 (2004), 251--253, DOI: 10.1016/j.cam.2003.09.052.
3. Jae Heon Yun, *A Note on SOR(\(\omega\)) Splitting of an M-Matrix*, Journal of Computational and Applied Mathematics 179 (2005), 407--409, DOI: 10.1016/j.cam.2004.07.029.
4. Hao Lu, *Stair Matrices and Their Generalizations with Applications to Iterative Methods I: A Generalization of the Successive Overrelaxation Method*, SIAM Journal on Numerical Analysis 37 (1999), 1--17, DOI: 10.1137/S0036142998343294.
