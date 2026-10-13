# Three dimensions are minimal for unbounded Euclidean transients in HSS

## Finding
Let
\[
A=H+S,
\qquad
H=H^{\mathsf T}>0,
\qquad
S^{\mathsf T}=-S,
\]
and consider the classical Hermitian/skew-Hermitian splitting iteration with parameter
\[
\alpha>0.
\]
Its error propagation matrix is
\[
M_\alpha
=
(\alpha I+S)^{-1}
(\alpha I-H)
(\alpha I+H)^{-1}
(\alpha I-S).
\]

For every real system of dimension at most two,
\[
\boxed{
\|M_\alpha\|_2
=
\max_{\lambda\in\sigma(H)}
\left|
\frac{\alpha-\lambda}{\alpha+\lambda}
\right|
<1.
}
\]
Thus HSS is stepwise Euclidean-error contractive in dimensions one and two, not merely asymptotically convergent.

Dimension three is minimal for failure, and the failure can be arbitrarily large even with the classical spectral-rate data fixed. Take
\[
H=\operatorname{diag}(1,2,4),
\qquad
\alpha=2,
\]
and
\[
S_t
=
t
\begin{pmatrix}
0&1&0\\
-1&0&-1\\
0&1&0
\end{pmatrix},
\qquad
t>0.
\]
Then
\[
\kappa_2(H)=4
\]
and
\[
\alpha=\sqrt{\lambda_{\min}(H)\lambda_{\max}(H)}
\]
is exactly the classical parameter that minimizes the standard HSS convergence-factor upper bound.

For
\[
A_t=H+S_t,
\]
the HSS iteration matrix satisfies
\[
\rho(M_t)\le\frac13
\]
for every \(t>0\), while
\[
\boxed{
\|M_t\|_2
\ge
\frac{t}{3\sqrt2}.
}
\]
Consequently, for every prescribed \(G>0\), some member of this fixed-\(H\), fixed-\(\alpha\) family amplifies the Euclidean solution error by more than \(G\) in one HSS step.

At
\[
t=6,
\]
the incoming error
\[
e_2=(0,1,0)^{\mathsf T}
\]
is mapped to
\[
(-1,0,1)^{\mathsf T},
\]
so the exact one-step Euclidean amplification is \(\sqrt2\), even though the spectral radius is below \(1/3\).

## Assumptions and scope
The theorem is for real matrices in exact arithmetic. Positive definiteness of a nonsymmetric real matrix means that its symmetric part is positive definite, equivalently
\[
x^{\mathsf T}Ax>0
\]
for every nonzero real vector \(x\).

The monitored quantity is Euclidean solution error after one complete exact HSS iteration. The source HSS analysis also uses a problem-dependent norm based on
\[
\|(\alpha I+S)e\|_2.
\]
Contraction in that norm is not contradicted here.

The three-dimensional family keeps the Hermitian part, its condition number, and the classical bound-optimal HSS parameter fixed while varying only the skew-symmetric part. The spectral condition number of the full nonsymmetric matrix is not held fixed.

No statement is made about inexact HSS inner solves, preconditioned Krylov acceleration, finite precision, or complex dimension two, where a skew-Hermitian matrix has more degrees of freedom than a real skew-symmetric one.

## Proof
The one-dimensional statement is immediate. Consider dimension two.

By an orthogonal change of coordinates, diagonalize \(H\). Every real \(2\times2\) skew-symmetric matrix then has the form
\[
S=sJ,
\qquad
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}.
\]
Put
\[
D=
(\alpha I-H)(\alpha I+H)^{-1}.
\]
Since
\[
S^2=-s^2I,
\]
define
\[
c=\sqrt{\alpha^2+s^2}
\]
and
\[
U=\frac{\alpha I-S}{c}.
\]
Then \(U\) is orthogonal and
\[
(\alpha I+S)^{-1}=\frac{U}{c},
\qquad
\alpha I-S=cU.
\]
Therefore
\[
M_\alpha=UDU.
\]
Left and right multiplication by orthogonal matrices preserves singular values, so
\[
\|M_\alpha\|_2=\|D\|_2.
\]
Because \(D\) is symmetric with eigenvalues
\[
\frac{\alpha-\lambda}{\alpha+\lambda},
\qquad
\lambda\in\sigma(H),
\]
we obtain
\[
\|M_\alpha\|_2
=
\max_{\lambda\in\sigma(H)}
\left|
\frac{\alpha-\lambda}{\alpha+\lambda}
\right|
<1.
\]
At
\[
\alpha_*=
\sqrt{\lambda_{\min}(H)\lambda_{\max}(H)},
\]
the endpoint magnitudes balance, giving the exact factor
\[
\frac{\sqrt{\kappa_2(H)}-1}
{\sqrt{\kappa_2(H)}+1}.
\]

Now take
\[
H=\operatorname{diag}(1,2,4),
\qquad
\alpha=2,
\]
and the displayed \(S_t\). Since \(S_t\) is skew-symmetric,
\[
x^{\mathsf T}(H+S_t)x=x^{\mathsf T}Hx>0,
\]
so every \(A_t=H+S_t\) is positive definite.

For this \(H\),
\[
D=
(2I-H)(2I+H)^{-1}
=
\operatorname{diag}
\left(
\frac13,0,-\frac13
\right).
\]
Direct substitution into
\[
M_t=(2I+S_t)^{-1}D(2I-S_t)
\]
gives
\[
M_t=
\begin{pmatrix}
\dfrac{t^2+4}{6(t^2+2)}&-\dfrac t6&
\dfrac{t^2}{6(t^2+2)}\\[1ex]
\dfrac{t}{3(t^2+2)}&0&
-\dfrac{t}{3(t^2+2)}\\[1ex]
-\dfrac{t^2}{6(t^2+2)}&\dfrac t6&
-\dfrac{t^2+4}{6(t^2+2)}
\end{pmatrix}.
\]
Its characteristic polynomial factors as
\[
\lambda
\left(
\lambda^2+\frac{t^2-2}{9(t^2+2)}
\right).
\]
Hence
\[
\rho(M_t)
=
\frac13
\sqrt{\frac{|t^2-2|}{t^2+2}}
\le\frac13.
\]

For the second coordinate vector,
\[
(2I-S_t)e_2=(-t,2,-t)^{\mathsf T}
\]
and therefore
\[
D(2I-S_t)e_2
=
(-t/3,0,t/3)^{\mathsf T}.
\]
The vector
\[
y=(-t/6,0,t/6)^{\mathsf T}
\]
lies in the kernel of \(S_t\), so
\[
(2I+S_t)y=2y=(-t/3,0,t/3)^{\mathsf T}.
\]
Thus
\[
M_te_2=y.
\]
Since
\[
\|y\|_2=\frac{t}{3\sqrt2},
\]
we have
\[
\|M_t\|_2
\ge
\frac{t}{3\sqrt2},
\]
which diverges with \(t\).

The dimension-two contraction theorem and this dimension-three family prove minimality.

## Verification
The embedded `verify.py` reconstructs the HSS matrix from the actual factors using exact rational arithmetic.

For
\[
t=6,
\]
it verifies
\[
M_6e_2=(-1,0,1)^{\mathsf T}
\]
and hence squared Euclidean amplification \(2\). For
\[
t=12,
\]
it verifies squared amplification \(8\).

It also verifies the exact characteristic-polynomial coefficients for several rational \(t\), and checks a nontrivial two-dimensional sample by comparing the trace and determinant of
\[
M^{\mathsf T}M
\]
with the squared singular values predicted by the two diagonal entries of \(D\).

The universal dimension-two result and the unbounded dimension-three statement are analytic; finite replay is corroborative only.

## Relationship to prior work
Bai, Golub, and Ng introduced the HSS iteration for non-Hermitian positive-definite linear systems. Their convergence theorem gives
\[
\rho(M_\alpha)
\le
\max_{\lambda\in\sigma(H)}
\left|
\frac{\alpha-\lambda}{\alpha+\lambda}
\right|
<1,
\]
and derives the familiar parameter
\[
\alpha_*=
\sqrt{\lambda_{\min}(H)\lambda_{\max}(H)}
\]
by minimizing that upper bound. The same paper proves contraction in the problem-dependent norm induced by \(\alpha I+S\).

Those results are the starting point here. They do not identify when the ordinary Euclidean error is stepwise contractive, nor do they bound Euclidean transients independently of the skew-Hermitian part. Indeed, the use of a transformed norm leaves open precisely the Euclidean nonnormality addressed by the present result.

Later HSS parameter-selection literature continues to optimize spectral-radius bounds or their estimates. Targeted searches using HSS, Euclidean error, transient growth, nonnormality, minimal dimension, and exact two-dimensional contraction did not locate either the dimension-two singular-value identity or the fixed-\(H\) three-dimensional unbounded family.

Generic nonnormal transient growth is classical. The new content is the HSS-specific sharp low-dimensional boundary: exact Euclidean contraction in every real system of dimension at most two, versus unbounded one-step growth beginning in dimension three despite fixed Hermitian conditioning and the standard optimal HSS parameter.

## Limitations
The two-dimensional protection theorem is stated for real systems. The complex \(2\times2\) skew-Hermitian case has additional diagonal imaginary degrees of freedom and is not classified here.

The three-dimensional construction controls the condition number of the Hermitian part, not the full nonsymmetric matrix. This matches the quantity governing the classical HSS convergence bound but is a deliberate limitation.

The result concerns exact HSS iterations. Inexact inner solves may introduce additional transient effects.

No claim is made that the displayed family maximizes Euclidean amplification at fixed bounds on the skew-symmetric part; the theorem instead shows that no finite bound exists when only the classical HSS spectral data are fixed.

## References
1. Z.-Z. Bai, G. H. Golub, and M. K. Ng, “Hermitian and Skew-Hermitian Splitting Methods for Non-Hermitian Positive Definite Linear Systems,” SIAM Journal on Matrix Analysis and Applications 24 (2003), 603–626. DOI 10.1137/S0895479801395458. Published electronically 2003-01-17.
