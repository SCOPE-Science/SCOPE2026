# Three interior nodes are the first uniform one-dimensional Galerkin heat mesh with transient negativity
## Finding
Consider the heat equation on a one-dimensional interval with homogeneous Dirichlet boundary conditions, discretized in space by continuous piecewise-linear finite elements on a uniform mesh of spacing \(h>0\), using the standard consistent mass matrix. Let \(N\) denote the number of interior nodes and let
\[
E_N(t)=\exp(-M_N^{-1}S_N t)
\]
be the nodal semidiscrete solution matrix.

For \(N=1\) and \(N=2\),
\[
E_N(t)>0
\qquad\text{entrywise for every }t>0.
\]
For \(N=3\), positivity fails immediately but reappears at one exact scale-free time. Put
\[
\tau=\frac{t}{h^2}.
\]
There is a unique number
\[
\tau_* = 0.2128117769214312049971627383\ldots
\]
satisfying
\[
\exp\!\left(\frac{9(2\sqrt2-1)}7\tau_*\right)
+
\exp\!\left(-\frac{9(1+2\sqrt2)}7\tau_*\right)
=2.
\]
Then
\[
E_3(t)\not\ge0
\quad\text{for }0<t<\tau_*h^2,
\]
\[
E_3(\tau_*h^2)\ge0,
\]
and
\[
E_3(t)>0
\quad\text{for }t>\tau_*h^2.
\]
The only entries that can be negative are the two corner couplings between the first and third interior nodes. More precisely,
\[
(E_3(t))_{13}=(E_3(t))_{31}
=
\frac14 e^{-\lambda_1\tau}
-\frac12 e^{-3\tau}
+\frac14 e^{-\lambda_3\tau},
\]
where
\[
\lambda_1=\frac{30-18\sqrt2}{7},
\qquad
\lambda_3=\frac{30+18\sqrt2}{7}.
\]
This entry is negative exactly for
\[
0<\tau<\tau_*.
\]

Consequently, among uniform one-dimensional standard Galerkin heat semidiscretizations, three interior nodes are the smallest system size at which the consistent mass matrix can create a transient negative nodal value from nonnegative nodal initial data. Taking initial data equal to the third coordinate vector gives
\[
u_1(t)=(E_3(t))_{13}<0
\]
throughout the interval \(0<t<\tau_*h^2\).

For the unit interval with three interior nodes, \(h=1/4\), the exact reappearance time is
\[
t_*=\frac{\tau_*}{16}
=
0.01330073605758945031232267114\ldots.
\]

## Assumptions and scope
The result concerns the spatially semidiscrete standard Galerkin method for the homogeneous heat equation, with continuous piecewise-linear finite elements, exact \(L^2\) mass integration, a uniform one-dimensional mesh, and homogeneous Dirichlet endpoint conditions. Positivity is nodal positivity, equivalently entrywise nonnegativity of the solution matrix.

The result classifies only the first three possible interior-node counts. It does not claim an all-\(N\) formula for the positivity threshold on longer meshes, nor does it address lumped mass, finite-volume elements, nonlinear diffusion, or fully discrete time-stepping.

The dimensionless time \(\tau=t/h^2\) removes the trivial mesh scaling. Thus \(\tau_*\) is intrinsic to the three-interior-node consistent-mass stencil.

## Proof
For \(N\) interior nodes on a uniform mesh,
\[
M_N=\frac h6 T_N,
\qquad
S_N=\frac1h K_N,
\]
where \(T_N\) is tridiagonal with diagonal entries \(4\) and off-diagonal entries \(1\), and \(K_N\) is tridiagonal with diagonal entries \(2\) and off-diagonal entries \(-1\). Hence
\[
M_N^{-1}S_N
=
\frac6{h^2}T_N^{-1}K_N.
\]

For \(N=1\),
\[
h^2M_1^{-1}S_1=3,
\]
so
\[
E_1(t)=e^{-3\tau}>0.
\]

For \(N=2\),
\[
h^2M_2^{-1}S_2
=
\begin{pmatrix}
18/5&-12/5\\
-12/5&18/5
\end{pmatrix}.
\]
Its negative is an irreducible Metzler matrix. Therefore
\[
E_2(t)>0
\]
entrywise for every \(t>0\). Equivalently, its off-diagonal entry is
\[
\frac12\left(e^{-6\tau/5}-e^{-6\tau}\right)>0.
\]

For \(N=3\),
\[
H:=h^2M_3^{-1}S_3
=
\begin{pmatrix}
51/14&-18/7&9/14\\
-18/7&30/7&-18/7\\
9/14&-18/7&51/14
\end{pmatrix}.
\]
The mass and stiffness Toeplitz matrices are simultaneously diagonalized by the discrete sine basis. The three eigenvalues of \(H\) are
\[
\lambda_1=\frac{30-18\sqrt2}{7},
\qquad
\lambda_2=3,
\qquad
\lambda_3=\frac{30+18\sqrt2}{7},
\]
with orthonormal eigenvectors
\[
v_1=
\begin{pmatrix}
1/2\\
1/\sqrt2\\
1/2
\end{pmatrix},
\qquad
v_2=
\begin{pmatrix}
1/\sqrt2\\
0\\
-1/\sqrt2
\end{pmatrix},
\qquad
v_3=
\begin{pmatrix}
1/2\\
-1/\sqrt2\\
1/2
\end{pmatrix}.
\]
Therefore
\[
E_3(t)=
e^{-\lambda_1\tau}v_1v_1^{\mathsf T}
+
e^{-3\tau}v_2v_2^{\mathsf T}
+
e^{-\lambda_3\tau}v_3v_3^{\mathsf T}.
\]

The diagonal entries are positive sums of exponentials. The nearest-neighbor entries satisfy
\[
(E_3(t))_{12}=(E_3(t))_{23}
=
\frac{\sqrt2}{4}
\left(e^{-\lambda_1\tau}-e^{-\lambda_3\tau}\right)>0
\]
for every \(\tau>0\). Thus only
\[
c(\tau):=(E_3(t))_{13}
=
\frac14e^{-\lambda_1\tau}
-\frac12e^{-3\tau}
+\frac14e^{-\lambda_3\tau}
\]
can change sign.

Multiplying by the positive factor \(4e^{3\tau}\) shows that the sign of \(c(\tau)\) is the sign of
\[
g(\tau)
=
\exp(p\tau)+\exp(-q\tau)-2,
\]
where
\[
p=3-\lambda_1=\frac{9(2\sqrt2-1)}7>0,
\qquad
q=\lambda_3-3=\frac{9(1+2\sqrt2)}7>p.
\]
Now
\[
g(0)=0,
\qquad
g'(0)=p-q<0,
\]
and
\[
g''(\tau)=p^2e^{p\tau}+q^2e^{-q\tau}>0
\]
for every \(\tau\ge0\). Hence \(g'\) is strictly increasing. Since
\[
g'(\tau)\to\infty
\quad\text{as }\tau\to\infty,
\]
it has exactly one positive zero, so \(g\) first decreases and then increases. Because
\[
g(\tau)\to\infty
\quad\text{as }\tau\to\infty,
\]
there is exactly one positive root \(\tau_*\). Therefore
\[
c(\tau)<0
\quad\text{for }0<\tau<\tau_*,
\]
\[
c(\tau_*)=0,
\]
and
\[
c(\tau)>0
\quad\text{for }\tau>\tau_*.
\]
This proves both the sharp positivity threshold and the minimality of \(N=3\).

## Verification
The accompanying `verify.py` reconstructs the \(N=1,2,3\) mass and stiffness matrices with exact rational arithmetic, verifies the displayed dimensionless matrix \(H\), and checks its three algebraic eigenpairs in the quadratic field \(\mathbb Q(\sqrt2)\).

The checker then evaluates the scalar corner-entry equation with high-precision decimal arithmetic and verifies the certified bracket
\[
0.21281177692
<
\tau_*
<
0.21281177693.
\]
It also checks directly that the corner entry is negative below the bracket and positive above it, while all other nontrivial off-diagonal entries have the stated strictly positive formula.

The proof of uniqueness of the positive root is analytic and depends only on strict convexity of \(g\); it is not inferred from numerical root finding.

## Relationship to prior work
The loss and later recovery of nonnegativity for consistent-mass finite-element heat semidiscretizations is classical. Thomée and related work formulate the semidiscrete solution as
\[
E(t)=e^{-M^{-1}St},
\]
show that standard Galerkin discretizations can fail positivity for small positive time, and prove eventual positivity under an inverse-positivity hypothesis. They also define and numerically study positivity thresholds on two-dimensional triangulations.

The present result isolates the smallest uniform one-dimensional standard Galerkin system where that mechanism can occur. The prior general theorems do not identify this minimal one-dimensional node count, nor do the inspected numerical tables give the closed scalar threshold equation above. The two-node system is positivity improving for all positive times, whereas the three-node system has one explicitly computable nonlocal negative channel and one exact reappearance time.

The closest published finite-element positivity literature also studies lumped mass, finite-volume elements, backward Euler, and rational time-stepping. Those results concern different spatial operators or additional time discretization and do not imply the three-node consistent-mass threshold.

## Limitations
No all-size statement is made for \(N\ge4\). In particular, the positivity threshold on longer uniform one-dimensional meshes may involve several competing entries rather than the single corner channel found here.

The result is specific to the consistent \(L^2\) mass matrix. Mass lumping changes the generator to a Metzler form on the one-dimensional uniform mesh and removes this particular transient-negativity mechanism.

The originality assessment is limited by terminology: older finite-element or positive-semigroup literature could encode the same \(N=3\) calculation without emphasizing the minimal-node classification or the scale-free threshold constant.

## References
1. Vidar Thomée, *On Positivity Preservation in Some Finite Element Methods for the Heat Equation*, Numerical Methods and Applications, LNCS 8962, 13–24 (2015), DOI: 10.1007/978-3-319-15585-2_2.
2. Panagiotis Chatzipantelidis, Zoltán Horváth, and Vidar Thomée, *On Preservation of Positivity in Some Finite Element Methods for the Heat Equation*, Computational Methods in Applied Mathematics 15 (2015), 417–437, DOI: 10.1515/cmam-2015-0018.
3. Bangti Jin, Raytcho Lazarov, Vidar Thomée, and Zhi Zhou, *On Nonnegativity Preservation in Finite Element Methods for Subdiffusion Equations*, arXiv:1510.02825.
4. Vidar Thomée and Lars B. Wahlbin, *On the Existence of Maximum Principles in Parabolic Finite Element Equations*, Mathematics of Computation 77 (2008), 11–19, DOI: 10.1090/S0025-5718-07-02021-2.
