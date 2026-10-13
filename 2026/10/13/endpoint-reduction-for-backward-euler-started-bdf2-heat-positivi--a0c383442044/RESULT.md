# Endpoint reduction for backward-Euler-started BDF2 heat positivity
## Finding
Let \(T_n\) be the \(n\times n\) tridiagonal Dirichlet second-difference matrix with diagonal entries \(2\) and adjacent entries \(-1\). For \(s>0\), define
\[
R_n(s)=(I+sT_n)^{-1}.
\]
Consider the semidiscrete heat equation \(u'=-T_nu\) with nonnegative initial vector \(u^{(0)}\ge0\). Use one backward-Euler start
\[
u^{(1)}=R_n(s)u^{(0)},
\]
then take the first constant-step BDF2 value from
\[
(3I+2sT_n)u^{(2)}=4u^{(1)}-u^{(0)}.
\]
The first BDF2 step is therefore \(u^{(2)}=F_n(s)u^{(0)}\), where
\[
F_n(s)=4R_n(s)-3R_n(2s/3).
\]
The exact positivity test is a single endpoint inequality:
\[
F_n(s)\ge0\quad\Longleftrightarrow\quad 4(R_n(s))_{11}-3(R_n(2s/3))_{11}\ge0.
\]
Thus the \(n^2\) entrywise constraints reduce to one boundary diagonal entry. If
\[
\theta_x=\operatorname{arcosh}\!\left(1+\frac{1}{2x}\right),
\]
then the same criterion is
\[
\frac{\sinh(n\theta_s)\sinh((n+1)\theta_{2s/3})}{\sinh(n\theta_{2s/3})\sinh((n+1)\theta_s)}\ge\frac98.
\]
In the semi-infinite Dirichlet limit this yields the sharp frontier
\[
s\le 180-102\sqrt3=3.3308176279745\ldots.
\]
For \(n=2\), the choice \(s=5/2\) gives the exact counterexample
\[
F_2(5/2)=\frac1{1904}
\begin{pmatrix}
-11&45\\
45&-11
\end{pmatrix}.
\]
Hence \(u^{(0)}=e_1\) produces a negative first component in \(u^{(2)}\), despite the positivity of the backward-Euler startup value.

## Assumptions and scope
The statement concerns the standard centered second-difference discretization of the one-dimensional heat operator on \(n\) interior points with homogeneous Dirichlet boundary conditions. The nondimensional step parameter is \(s=\kappa\Delta t/h^2\) after the diffusion coefficient and mesh width are absorbed into the semidiscrete operator. Arithmetic is exact in the proof. The claim is only about the first BDF2 value after a backward-Euler starter; it is not a claim that later BDF2 values remain nonnegative whenever this first-step criterion holds.

## Proof
Because \(3I+2sT_n=3(I+(2s/3)T_n)\), and all rational functions of \(T_n\) commute,
\[
\begin{aligned}
F_n(s)
&=(3I+2sT_n)^{-1}(4R_n(s)-I)\\
&=4R_n(s)-3R_n(2s/3).
\end{aligned}
\]
For \(1\le i\le j\le n\), the Dirichlet resolvent has the Green-function formula
\[
(R_n(x))_{ij}=
\frac{\sinh(i\theta_x)\sinh((n+1-j)\theta_x)}
{x\sinh(\theta_x)\sinh((n+1)\theta_x)},
\qquad
\cosh\theta_x=1+\frac1{2x}.
\]
Put \(t=2s/3\), so \(0<\theta_s<\theta_t\), and define
\[
h_k=\frac{\sinh(k\theta_s)}{\sinh(k\theta_t)}.
\]
For \(1\le i\le j\le n\),
\[
\frac{(R_n(s))_{ij}}{(R_n(t))_{ij}}
=\frac23\frac{h_i h_{n+1-j}}{h_1h_{n+1}}.
\]
The continuous function
\[
\phi(x)=\log\sinh(x\theta_s)-\log\sinh(x\theta_t)
\]
is strictly decreasing and strictly concave on \((0,\infty)\). Indeed,
\[
\phi'(x)=\theta_s\coth(x\theta_s)-\theta_t\coth(x\theta_t)<0,
\]
because \(y\mapsto y\coth(xy)\) is increasing, while
\[
\phi''(x)=-\theta_s^2\operatorname{csch}^2(x\theta_s)+
\theta_t^2\operatorname{csch}^2(x\theta_t)<0,
\]
because \(y\mapsto y/\sinh(xy)\) is decreasing.

Since \(h_k=e^{\phi(k)}\) is decreasing, replacing \(i\) by \(j\) can only decrease \(h_i h_{n+1-j}\). The two resulting indices sum to \(n+1\). Concavity of \(\phi\) then shows that the product with this fixed sum is minimized at an endpoint. Therefore
\[
h_i h_{n+1-j}\ge h_1h_n,
\]
and hence
\[
\min_{1\le i,j\le n}
\frac{(R_n(s))_{ij}}{(R_n(t))_{ij}}
=\frac23\frac{h_n}{h_{n+1}},
\]
with equality at the two endpoint diagonal entries. Since \(R_n(t)\) is strictly positive entrywise,
\[
F_n(s)\ge0
\quad\Longleftrightarrow\quad
4\frac{(R_n(s))_{11}}{(R_n(t))_{11}}\ge3,
\]
which gives both stated finite-grid criteria.

For the semi-infinite Dirichlet path, write \(q_x\in(0,1)\) by
\[
x=\frac{q_x}{(1-q_x)^2}.
\]
The endpoint resolvent value is \((1-q_x)^2\). The limiting boundary condition is therefore
\[
4(1-q_s)^2\ge3(1-q_{2s/3})^2.
\]
At equality, set \(a=1-q_s\) and \(b=1-q_{2s/3}\). Positivity gives \(b=2a/\sqrt3\), while
\[
\frac{1-b}{b^2}=\frac23\frac{1-a}{a^2}.
\]
Solving yields
\[
a=\frac1{6\sqrt3-8},
\qquad
s=\frac{1-a}{a^2}=180-102\sqrt3.
\]
The boundary expression is positive for small \(s\) and negative beyond this crossing, giving the sharp semi-infinite frontier.

## Verification
The bundled checker uses only exact rational arithmetic for the \(n=2\), \(s=5/2\) witness. It reconstructs the backward-Euler resolvent, the BDF2 first-step operator in two algebraically equivalent ways, and verifies
\[
F_2(5/2)=\frac1{1904}
\begin{pmatrix}-11&45\\45&-11\end{pmatrix}.
\]
It also checks the exact \(n=2\) endpoint polynomial
\[
-4s^3+5s^2+8s+3,
\]
whose unique positive zero is approximately \(2.27435990957148\), so the rational witness lies strictly beyond the finite-grid positivity boundary.

## Relationship to prior work
Bonaventura and Della Rocca's archive-era TR-BDF2 study puts positivity, monotonicity, and discrete maximum principles in the absolute-monotonicity framework and motivates the distinction between stability and sign preservation. Hundsdorfer's BDF2 analysis more directly treats positivity and monotonicity, allows an implicit-Euler starting procedure, and develops general sufficient positivity conditions for linear semidiscrete systems. That general theory does not state the path-specific exact first-post-start reduction above: here the first BDF2 map is analyzed as a difference of two Dirichlet resolvents, and every entrywise sign constraint is shown to be dominated by the endpoint diagonal. The later Hundsdorfer--Ruuth--Spiteri work studies monotonicity-preserving multistep methods together with starting procedures at the method-class level rather than this exact heat-path Green-function criterion.

The closest published published-finding corpus item found in semantic search concerns backward-Euler-filtered Crank--Nicolson on heat lattices. It uses a different rational map and proves an unconditional lattice-kernel phenomenon; it neither states nor implies the BDF2 resolvent-difference endpoint reduction. A second nearby item concerns a stabilized Crank--Nicolson/Adams--Bashforth Allen--Cahn reversal threshold, again a different recurrence and nonlinear setting.

## Limitations
The theorem is specific to the one-dimensional homogeneous-Dirichlet nearest-neighbor heat matrix. It does not establish the same endpoint reduction for arbitrary Stieltjes matrices, nonuniform meshes, variable diffusion, finite elements, higher spatial dimensions, or later BDF2 steps. The semi-infinite constant is a boundary-limit result; no claim is made here that finite-grid critical values form a monotone sequence, although the exact scalar criterion permits them to be computed without testing all matrix entries. Older positivity literature for multistep discretizations is broad, so terminology differences remain a residual originality risk.

## References
1. L. Bonaventura, A. Della Rocca, “Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions,” arXiv:1510.04303, first submitted 14 October 2015.
2. W. Hundsdorfer, “Partially Implicit BDF2 Blends for Convection Dominated Flows,” *SIAM Journal on Numerical Analysis* 38(6), 1763–1783. DOI: 10.1137/S0036142999364741. The publisher records an online date of 26 July 2006; an earlier CWI report is month-dated December 1998.
3. W. Hundsdorfer, S. J. Ruuth, R. J. Spiteri, “Monotonicity-Preserving Linear Multistep Methods,” *SIAM Journal on Numerical Analysis* 41(2), 605–623. DOI: 10.1137/S0036142902406326.
4. C. Bolley, M. Crouzeix, “Conservation de la positivité lors de la discrétisation des problèmes d’évolution paraboliques,” *RAIRO Analyse Numérique* 12(3), 237–245 (1978).
