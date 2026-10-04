# Spectral width is the sharp second-iterate positivity threshold for good Broyden
## Finding
Consider the linear system
\[
F(x)=Ax-b=0,
\qquad
A=A^{\mathsf T}>0,
\]
where \(A\) is Stieltjes, meaning that its off-diagonal entries are nonpositive. Assume
\[
\sigma(A)\subset[\mu,L],
\qquad
0<\mu\le L,
\qquad
b\ge0.
\]
Apply Broyden's first, or good, Jacobian update from
\[
x^{(0)}=0,
\qquad
B_0=\gamma I,
\qquad
\gamma>0,
\]
with
\[
x^{(k+1)}=x^{(k)}-B_k^{-1}F(x^{(k)}),
\]
and
\[
B_{k+1}=B_k+
\frac{(y_k-B_ks_k)s_k^{\mathsf T}}{s_k^{\mathsf T}s_k},
\qquad
s_k=x^{(k+1)}-x^{(k)},
\qquad
y_k=F(x^{(k+1)})-F(x^{(k)}).
\]

Then the second iterate is componentwise nonnegative for every dimension, every such Stieltjes matrix, and every \(b\ge0\) if
\[
\gamma\ge L-\mu.
\]
This threshold is sharp over the whole spectral class: if
\[
0<\gamma<L-\mu,
\]
there is already a two-dimensional diagonal positive definite system with a strictly positive right-hand side and strictly positive exact solution for which the second Broyden iterate has a negative coordinate.

More precisely, if
\[
\rho=\frac{b^{\mathsf T}Ab}{b^{\mathsf T}b},
\]
then
\[
x^{(1)}=\frac{b}{\gamma}
\]
and the exact second-iterate identity is
\[
\boxed{
 x^{(2)}=
 \frac{[(\rho+\gamma)I-A]b}{\gamma\rho}
 }.
\]
Thus the sufficient positivity mechanism is not a norm estimate: it is the entrywise nonnegativity of a shifted Stieltjes matrix, forced uniformly by
\[
\rho+\gamma\ge\mu+\gamma\ge L.
\]

For sharpness, take
\[
A=\operatorname{diag}(\mu,L),
\qquad
b=(1,\varepsilon)^{\mathsf T}.
\]
Then
\[
\rho=\frac{\mu+L\varepsilon^2}{1+\varepsilon^2},
\]
and the second coordinate is negative whenever
\[
0<\varepsilon^2<\frac{L-\mu-\gamma}{\gamma}.
\]
Consequently two dimensions are minimal for failure. In one dimension the first secant update recovers the exact scalar Jacobian and the second iterate is the positive exact solution.

A convenient normalization is \(\gamma=\mu\). Under this common lower-curvature scalar initialization, the sharp criterion becomes
\[
\frac{L}{\mu}\le2.
\]
Hence condition number \(2\) is the exact universal second-iterate positivity frontier for that normalized initialization.

An exact witness is
\[
A=\operatorname{diag}(1,4),
\qquad
b=\begin{pmatrix}1\\1/2\end{pmatrix},
\qquad
\gamma=2.
\]
Here
\[
\rho=\frac85,
\qquad
x^{(1)}=\begin{pmatrix}1/2\\1/4\end{pmatrix}>0,
\]
but
\[
x^{(2)}=\begin{pmatrix}13/16\\-1/16\end{pmatrix},
\]
while
\[
A^{-1}b=\begin{pmatrix}1\\1/8\end{pmatrix}>0.
\]

## Assumptions and scope
The result concerns the classical good Broyden rank-one update applied to a linear root-finding problem. The Jacobian approximation is stored directly as \(B_k\), not as an inverse approximation, and the initialization is the isotropic positive matrix \(B_0=\gamma I\).

The universal threshold uses both symmetry and the Stieltjes sign pattern. Symmetry supplies the Rayleigh interval \(\mu\le\rho\le L\); the Stieltjes property turns the shifted matrix \((\rho+\gamma)I-A\) into an entrywise nonnegative matrix once its diagonal is nonnegative.

The theorem classifies only the second iterate. It does not assert positivity of every later Broyden iterate for non-diagonal systems, nor does it classify nonsymmetric \(M\)-matrices.

## Proof
The first step is immediate:
\[
x^{(1)}=-B_0^{-1}F(0)=\frac{b}{\gamma}.
\]
Hence
\[
s_0=\frac b\gamma,
\qquad
y_0=\frac{Ab}{\gamma},
\]
and the good Broyden update gives
\[
B_1
=
\gamma I+
\frac{(A-\gamma I)bb^{\mathsf T}}{b^{\mathsf T}b}.
\]
Set
\[
u=\frac{(A-\gamma I)b}{b^{\mathsf T}b}.
\]
Because
\[
b^{\mathsf T}u=\rho-\gamma,
\]
one obtains
\[
B_1u
=\gamma u+(\rho-\gamma)u
=\rho u.
\]
Also
\[
F(x^{(1)})
=\frac{(A-\gamma I)b}{\gamma}
=\frac{b^{\mathsf T}b}{\gamma}u.
\]
Therefore
\[
B_1^{-1}F(x^{(1)})
=
\frac{(A-\gamma I)b}{\gamma\rho},
\]
and subtraction from \(x^{(1)}\) yields
\[
x^{(2)}
=
\frac{[(\rho+\gamma)I-A]b}{\gamma\rho}.
\]

Suppose now that \(A\) is Stieltjes and \(\gamma\ge L-\mu\). For \(i\ne j\),
\[
-a_{ij}\ge0.
\]
Moreover every diagonal entry of a symmetric matrix lies below its largest eigenvalue, so
\[
a_{ii}\le L.
\]
Since \(\rho\ge\mu\),
\[
\rho+\gamma-a_{ii}
\ge
\mu+\gamma-L
\ge0.
\]
Thus every entry of
\[
(\rho+\gamma)I-A
\]
is nonnegative. Because \(b\ge0\) and \(\gamma\rho>0\), this proves
\[
x^{(2)}\ge0.
\]

For sharpness assume \(0<\gamma<L-\mu\). With the diagonal two-dimensional family in the finding,
\[
\rho+\gamma-L
=
\frac{\mu+L\varepsilon^2}{1+\varepsilon^2}+\gamma-L.
\]
Multiplying by \(1+\varepsilon^2\) shows that this quantity is negative exactly when
\[
\gamma\varepsilon^2<L-\mu-\gamma.
\]
Thus every positive \(\varepsilon\) satisfying the displayed bound produces
\[
(x^{(2)})_2<0.
\]
The exact solution is
\[
A^{-1}b=(1/\mu,\varepsilon/L)^{\mathsf T}>0.
\]
This proves necessity over the spectral class and the minimal two-dimensional obstruction.

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It constructs the good Broyden update directly, solves the resulting rational linear systems by Gaussian elimination, and checks the closed second-iterate formula on several rational symmetric positive definite Stieltjes systems.

It separately checks the complete two-dimensional sharpness family at rational parameter values, including points on both sides of the predicted \(\varepsilon\) boundary. The explicit witness
\[
A=\operatorname{diag}(1,4),
\qquad b=(1,1/2)^{\mathsf T},
\qquad\gamma=2
\]
is replayed exactly.

The universal statement for all dimensions is proved analytically above; finite replay is corroborative and is not used as an exhaustive proof.

## Relationship to prior work
Broyden's 1965 paper introduced the rank-one quasi-Newton family for nonlinear simultaneous equations. The secant condition and good Broyden update are classical and are not claimed as new.

O'Leary's analysis of Broyden on linear equations is especially close background. It treats good Broyden as a projection method, recalls finite termination in at most \(2n\) linear steps, and explicitly remarks that earlier termination proofs gave little insight into intermediate iterates. Its subject classification is headed by MSC \(65H10\). The full text analyzes residual subspaces, rank, and termination rather than coordinatewise positivity of an iterate.

Carlsson and Cary later compare standard Broyden with a hypersecant Jacobian approximation for sparse nonlinear systems. That work reinforces the practical relevance of Jacobian-update initialization but does not supply the spectral-width orthant criterion proved here.

Targeted searches under good Broyden, Stieltjes and \(M\)-matrix terminology, positive-orthant invariance, nonnegative right-hand sides, scalar Jacobian initialization, second iterates, and spectral width did not locate an implication-equivalent theorem. Convergence and finite-termination results do not determine signs of coordinates in the original basis.

## Limitations
The threshold is uniform over the spectral class and is sharp in that robust sense. A particular fixed Stieltjes matrix can admit smaller \(\gamma\) for particular right-hand sides.

Later iterates are not classified. The rank-one update can create dense sign patterns even when the original matrix is Stieltjes.

The initialization \(B_0=\gamma I\) is structurally natural but not the only possible quasi-Newton initialization. Diagonal or problem-specific initial Jacobians can have different positivity behavior.

Older literature on monotone nonlinear equations, inverse-positive Jacobians, or positivity-preserving quasi-Newton variants may encode an equivalent early-iterate observation under different terminology. This is the principal residual originality risk.

## References
1. C. G. Broyden, *A Class of Methods for Solving Nonlinear Simultaneous Equations*, Mathematics of Computation 19 (1965), 577--593, DOI: 10.1090/S0025-5718-1965-0198670-6.
2. Dianne P. O'Leary, *Why Broyden's Nonsymmetric Method Terminates on Linear Equations*, SIAM Journal on Optimization 5 (1995), 231--235, DOI: 10.1137/0805012.
3. Johan Carlsson and John R. Cary, *The Hypersecant Jacobian Approximation for Quasi-Newton Solves of Sparse Nonlinear Systems*, arXiv:0905.1054v1, May 7, 2009.
