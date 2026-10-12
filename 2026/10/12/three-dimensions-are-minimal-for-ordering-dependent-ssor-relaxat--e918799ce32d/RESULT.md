# Three dimensions are minimal for ordering-dependent SSOR relaxation

## Finding
Let
\[
A=D+L+L^{\mathsf T}>0
\]
and consider the SSOR preconditioner, up to its condition-number-irrelevant scalar factor,
\[
M_\omega=(D+\omega L)D^{-1}(D+\omega L^{\mathsf T}),
\qquad 0<\omega<2.
\]

There is a sharp dimensional split.

For every real \(2\times2\) SPD matrix and either ordering, \(\omega=1\) minimizes the spectral condition number of the SSOR-preconditioned system. It is the unique minimizer unless the matrix is diagonal.

Dimension three already permits ordering dependence. For the SPD path family
\[
A_r=
\begin{pmatrix}
1&r&0\\
r&1&r\\
0&r&1
\end{pmatrix},
\qquad
0<r<\frac1{\sqrt2},
\]
the natural ordering \(1,2,3\) has
\[
\frac{d}{d\omega}
\kappa(M_\omega^{-1}A_r)\bigg|_{\omega=1}<0,
\]
so a slight overrelaxation strictly improves the preconditioned condition number. For the center-first ordering \(2,1,3\), by contrast, \(\omega=1\) is the unique global minimizer.

Thus
\[
\boxed{
\text{dimension three is minimal for ordering-dependent SSOR relaxation optimality.}
}
\]

At the concrete value \(r=1/2\), the natural-order condition number at \(\omega=1\) is
\[
\frac{32}{23-\sqrt{17}},
\]
and its exact right derivative is
\[
-\frac18-\frac{23\sqrt{17}}{136}<0.
\]
The same matrix reordered center-first has preconditioned spectrum
\[
\{1,1,1/2\}
\]
at \(\omega=1\), and every other relaxation factor gives a strictly worse condition number.

## Assumptions and scope
The matrix is real and SPD. The SSOR preconditioner uses the splitting induced by the chosen coordinate ordering. The conventional scalar multiplier \(1/[\omega(2-\omega)]\) is omitted because multiplying an SPD preconditioner by a positive scalar multiplies all generalized eigenvalues by the same reciprocal scalar and therefore leaves their ratio unchanged.

The result concerns spectral condition number of the preconditioned SPD pair. It does not claim that the same relaxation factor minimizes wall-clock time, parallel communication, finite-precision error, or a particular Krylov iteration count.

The three-dimensional statement is a minimal-dimension obstruction and an explicit path family. It does not classify the globally optimal \(\omega\) for every three-dimensional SPD matrix or every ordering.

## Proof
First consider dimension two. Positive diagonal congruence and a diagonal sign similarity reduce every non-diagonal SPD matrix, without changing the generalized spectrum of the correspondingly transformed preconditioner, to
\[
\widehat A_\rho=
\begin{pmatrix}
1&\rho\\
\rho&1
\end{pmatrix},
\qquad
0<\rho<1.
\]
With the order \(1,2\),
\[
M_\omega=
\begin{pmatrix}
1&\rho\omega\\
\rho\omega&1+\rho^2\omega^2
\end{pmatrix}.
\]
A direct determinant calculation gives
\[
\det(\widehat A_\rho-\lambda M_\omega)
=
\lambda^2-
\left[2-\rho^2\omega(2-\omega)\right]\lambda
+1-\rho^2.
\]
Hence the two positive generalized eigenvalues have fixed product
\[
p=1-\rho^2
\]
and sum
\[
S(\omega)
=
1+p+\rho^2(\omega-1)^2.
\]
For two positive numbers with fixed product, their ratio is strictly increasing with their sum once the larger root is distinguished. Thus \(S\) is uniquely minimized at \(\omega=1\), proving the two-dimensional claim. Reversing the two coordinates gives the same generalized spectrum. If \(\rho=0\), the preconditioner is independent of \(\omega\).

Now use the natural ordering for
\[
A_r=
\begin{pmatrix}
1&r&0\\
r&1&r\\
0&r&1
\end{pmatrix}.
\]
Positive definiteness is equivalent here to
\[
0<r<\frac1{\sqrt2}.
\]
For this ordering,
\[
L=
\begin{pmatrix}
0&0&0\\
r&0&0\\
0&r&0
\end{pmatrix}.
\]
A direct determinant expansion yields
\[
\begin{aligned}
F(\lambda,\omega)
={}&-\lambda^3
+\lambda^2r^4\omega^4
-2\lambda^2r^4\omega^3
+2\lambda^2r^2\omega^2
-4\lambda^2r^2\omega
+3\lambda^2\\
&+\lambda r^4\omega^2
-2\lambda r^2\omega^2
+4\lambda r^2\omega
+2\lambda r^2
-3\lambda
-2r^2+1.
\end{aligned}
\]
At \(\omega=1\),
\[
F(\lambda,1)
=-(\lambda-1)Q_r(\lambda),
\]
where
\[
Q_r(\lambda)
=
\lambda^2+(r^4+2r^2-2)\lambda+1-2r^2.
\]
The two roots are
\[
\lambda_\pm
=
1-r^2-\frac{r^4}{2}
\pm
\frac{r^3}{2}\sqrt{r^2+4}.
\]
Their product is \(1-2r^2>0\), and
\[
\lambda_+<1
\]
because
\[
r\sqrt{r^2+4}<r^2+2.
\]
Thus
\[
0<\lambda_-<\lambda_+<1.
\]
The maximal generalized eigenvalue is therefore the simple branch through \(1\), and the minimal one is the branch through \(\lambda_-\).

Differentiating the characteristic polynomial at \(\omega=1\) gives
\[
\partial_\omega F(\lambda,1)
=-2\lambda r^4(\lambda-1).
\]
At \(\lambda=\lambda_-\), this is positive. Also
\[
\partial_\lambda F(\lambda_-,1)
=-(\lambda_--1)Q_r'(\lambda_-)<0,
\]
because the derivative of a monic quadratic at its smaller root is negative. Hence the implicit-function formula gives
\[
\lambda_-'(1)
=-\frac{\partial_\omega F}{\partial_\lambda F}>0.
\]
For the branch through \(\lambda=1\), the same formula gives derivative zero because \(\partial_\omega F(1,1)=0\). The eigenvalue ordering persists locally, so
\[
\frac{d}{d\omega}
\kappa(M_\omega^{-1}A_r)\bigg|_{\omega=1}
=-\frac{\lambda_-'(1)}{\lambda_-(r)^2}<0.
\]
Therefore \(\omega=1\) is not even locally condition-number optimal in the natural ordering.

Finally permute the same matrix to the center-first order \(2,1,3\):
\[
\widetilde A_r=
\begin{pmatrix}
1&r&r\\
r&1&0\\
r&0&1
\end{pmatrix}.
\]
Its generalized characteristic polynomial factors for every \(\omega\) as
\[
(\lambda-1)
\left[
-\lambda^2+
\left(2-2r^2\omega(2-\omega)\right)\lambda
+2r^2-1
\right].
\]
The two nontrivial positive roots have product
\[
1-2r^2
\]
and sum
\[
2-2r^2+2r^2(\omega-1)^2.
\]
Their ratio is therefore uniquely minimized at \(\omega=1\). At that value they are \(1\) and \(1-2r^2\), so together with the fixed eigenvalue \(1\) the spectrum is
\[
\{1,1,1-2r^2\}.
\]
For \(\omega\ne1\), the nontrivial pair has the same product but larger sum; one root falls below \(1-2r^2\) and the other rises above \(1\), so the full condition number is strictly larger.

This proves both the ordering dependence in dimension three and its minimality.

## Verification
The embedded `verify.py` uses exact rational arithmetic to reconstruct the two-dimensional generalized characteristic polynomial and both three-dimensional determinant formulas at rational test values.

For \(r=1/2\), it verifies the exact natural-order factorization
\[
-(\lambda-1)
\left(
\lambda^2-\frac{23}{16}\lambda+\frac12
\right),
\]
the lower root
\[
\lambda_-=rac{23-\sqrt{17}}{32},
\]
and the exact condition-number derivative
\[
-\frac18-\frac{23\sqrt{17}}{136}<0.
\]
It also verifies that the center-first ordering has spectrum
\[
\{1,1,1/2\}
\]
at \(\omega=1\) and that its nontrivial-root sum increases by a positive multiple of \((\omega-1)^2\).

Finite replay is corroborative only; the all-matrix two-dimensional statement and the full \(r\)-family proof are analytic.

## Relationship to prior work
SSOR preconditioning and the effect of orderings are classical. Kuo and Chan analyze red/black and natural orderings for elliptic problems by two-color Fourier analysis. Their full paper shows that ordering can substantially affect SSOR-preconditioned convergence and, for their red/black model, derives a condition-number optimum at \(\omega=1\). Thus generic ordering dependence and red/black optimality at \(\omega=1\) are prior work.

Ortega reviews orderings for conjugate-gradient preconditioners and emphasizes that red/black or multicolor orderings can degrade convergence relative to natural ordering. The publisher record places that work primarily in numerical linear algebra under MSC \(65F10\).

The result here is narrower and structural: it classifies every two-dimensional SPD problem, proves that no ordering can move the SSOR condition-number optimum away from \(\omega=1\) there, and then gives an exact three-node path where one ordering has \(\omega=1\) as its unique optimum while another has a strictly improving overrelaxed direction at \(\omega=1\). Targeted searches did not locate this minimal-dimension boundary or the displayed three-node mechanism.

## Limitations
The theorem does not identify the global optimal relaxation parameter for the natural ordering of the three-node path; it proves only that \(\omega=1\) is locally suboptimal there. This is sufficient for the minimal-dimension and ordering-dependence claim.

The complete body of Ortega's 1991 article was not available through the inspected publisher route, so a small-dimensional example hidden there cannot be excluded. Kuo and Chan's full article was inspected and already covers broad ordering effects and a red/black \(\omega=1\) optimum; those facts are not claimed as new.

The machine-readable source date uses the earliest exact day-resolved public date verified for the cited journal records. Earlier print issues are documented only at month resolution in the inspected records and are not converted into invented calendar days.

## References
1. C.-C. Jay Kuo and Tony F. Chan, “Two-Color Fourier Analysis of Iterative Algorithms for Elliptic Problems with Red/Black Ordering,” SIAM Journal on Scientific and Statistical Computing 11 (1990), 767–793. DOI 10.1137/0911045.
2. James M. Ortega, “Orderings for Conjugate Gradient Preconditionings,” SIAM Journal on Optimization 1 (1991), 565–582. DOI 10.1137/0801034.
