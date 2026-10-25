# Sharp subquadratic positivity threshold on a one-defect periodic finite-element ring

## Finding
Consider a periodic interval split into five successive finite elements of lengths \(h,1,1,1,1\), with \(h\geq1\). For continuous piecewise-linear finite elements, unit heat diffusivity, consistent mass \(M\), stiffness \(K\), and backward Euler timestep \(t\geq0\), define \(P_h(t)=(M+tK)^{-1}M\). Put
\[
F_h(t)=(216h+864)t^3+(576-36h^2)t^2+(96-132h^2-18h)t+2h-13h^2.
\]
The cubic has exactly one positive zero \(\rho(h)\), and
\[
P_h(t)\geq0\text{ entrywise}\quad\Longleftrightarrow\quad t=0\ \text{or}\ t\geq\rho(h).
\]
For \(h=1\), \(\rho(1)=1/6\). For every \(h>1\),
\[
\frac16<\rho(h)<\frac{h^2}{6},\qquad
\rho(h)=\frac h6+3+o(1)\quad(h\longrightarrow\infty).
\]
Thus the elementary condition that every off-diagonal entry of \(M+tK\) be nonpositive, namely \(t\geq h^2/6\), is not necessary: on a ring with one very long element the sharp threshold grows only linearly, not quadratically, in the stretching ratio. At \(h>1,t=\rho(h)\), exactly two directed update entries vanish; all other entries are strictly positive.

## Assumptions and scope
Vertices are labeled cyclically \(0,1,2,3,4\); element \(0\)--\(1\) has length \(h\), and the other four edges have length \(1\). For an edge of length \(\ell\) with endpoints \(i,j\), assemble the local matrices
\[
M_e=\frac{\ell}{6}\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad
K_e=\frac1\ell\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]
All five nodal unknowns are retained, with periodic boundary conditions and no mass lumping. The normalization sets the four equal lengths and diffusivity to one. For general common short length \(a\) and diffusivity \(\kappa\), the dimensionless step in the theorem is \(t=\kappa\Delta t/a^2\) and \(h\) is the long-to-short length ratio. The output is a single backward-Euler step; no statement about arbitrary meshes or higher-order time integrators is made.

## Proof
Set \(R=6h(M+tK)\), \(S=6hM\), and \(D=\det R\). Direct exact determinant expansion yields
\[
D=6h^4\bigl(36ht^2+60ht+7h+144t^2+60t+4\bigr)Q,
\]
where \(Q=12h^2t+4h^2+36ht^2+60ht+7h+144t^2+48t\). Both factors are strictly positive for \(h\geq1,t\geq0\). By the adjugate identity \(P_h(t)=R^{-1}S\), two decisive entries are
\[
(P_h(t))_{0,3}=\frac{36h^4t(6t-1)Q}{D},\qquad
(P_h(t))_{0,2}=\frac{36h^4t F_h(t)}{D}.
\]
Thus \(0<t<1/6\) produces a negative entry. The equality \(F_h(1/6)=-36(h-1)(h+1)\) shows that for \(h>1\), nonnegativity also fails throughout the interval from \(1/6\) to the positive zero of \(F_h\).

To prove that these are the only obstructions, use the reflection of the five-cycle interchanging \(0\leftrightarrow1\), \(2\leftrightarrow4\), and fixing \(3\). The following gives exactly one representative of each orbit of **directed off-diagonal** positions. Every numerator is \(h^4t\) times the displayed expression (the common positive denominator is \(D\)):

| Position | Multiplier |
|---|---|
| \((0,1)\) | \(18(h+1)H\) |
| \((0,2)\) | \(36F_h\) |
| \((0,3)\) | \(36(6t-1)Q\) |
| \((0,4)\) | \(36G\) |
| \((2,0)\) | \(18(h+1)(6t-1)J\) |
| \((2,1)\) | \(18(h+1)W\) |
| \((2,3)\) | \(36(3h+6t+2)Q\) |
| \((2,4)\) | \(36(6t-1)U\) |
| \((3,0)\) | \(18(h+1)(6t-1)Q\) |
| \((3,2)\) | \(36(3h+6t+2)Q\) |

The auxiliary polynomials, recorded in the executable exact certificate, are
\[
\begin{aligned}
H={}&216ht^3+324ht^2+234ht+23h+864t^3+1296t^2+432t+32,\\
G={}&180h^2t^2+228h^2t+29h^2+216ht^3+864ht^2+342ht+26h+864t^3+576t^2+96t,\\
J={}&h^2(6t-1)+36ht^2+42ht+4h+144t^2+72t+8,\\
W={}&108h^2t^2+108h^2t+15h^2+216ht^3+648ht^2+342ht+32h+864t^3+864t^2+216t+8,\\
U={}&3h^3+12h^2t+4h^2+36ht^2+60ht+4h+144t^2+48t.
\end{aligned}
\]
All of \(Q,H,G,J,W,U\) are strictly positive for \(h\geq1,t\geq1/6\). For \(J\), the only potentially negative term, \(h^2(6t-1)\), is nonnegative on that range. The three reflection-distinct diagonal numerator polynomials have strictly positive coefficients in \(h,t\); their complete exact checks are in `verify.py`. Consequently every entry except the reflected pair \((0,2),(1,4)\) is nonnegative whenever \(t\geq1/6\), and is strictly positive if \(t>1/6\).

For \(h\geq1\), the coefficient of \(t^3\) in \(F_h\) is positive, while its linear and constant coefficients are strictly negative. Regardless of the sign of its quadratic coefficient, Descartes' rule gives exactly one sign change; together with \(F_h(0)<0\) and \(F_h(t)\to+\infty\), this proves one positive zero, with \(F_h(t)\geq0\) exactly for \(t\geq\rho(h)\). Also
\[
F_h(h^2/6)=h(h-1)^2(h+1)^3(h+2),\qquad
F_1(t)=(6t-1)(180t^2+120t+11).
\]
These identities prove the claimed strict bounds and the uniform-mesh endpoint. Finally, for fixed real \(c\),
\[
F_h(h/6+c)=6(c-3)h^3+O_c(h^2).
\]
Evaluating at \(c=3-\varepsilon\) and \(c=3+\varepsilon\) and using the unique positive root proves \(\rho(h)-h/6\to3\). At \(t=0\), the matrix is the identity. This completes the classification.

## Verification
Running `python verify.py` with SymPy checks, in exact rational arithmetic, the full determinant factorization, all 20 directed off-diagonal numerator identities, all five diagonal-positive coefficient expansions, the two boundary factorizations, the large-stretch coefficient, and 30 direct rational matrix-sign comparisons for six mesh ratios. The verification output is provided in `verify_output.txt`. These computations verify the displayed finite polynomial identities; the sign and uniqueness arguments above establish the theorem for all real \(h\geq1\) and \(t\geq0\). The smallest-stretch comparison \(h=1\) is a known uniform-mesh boundary case, not a separate originality claim.

## Relationship to prior work
Li and Huang (2012/2013) establish general sufficient mesh and timestep bounds for maximum principles of linear finite-element discretizations. The standard \(M\)-matrix bound here is \(t\geq h^2/6\), but their general sufficient condition does not supply this exact parameterized positivity set. The heat-equation positivity analyses of Thomée and Wahlbin (2008) and Chatzipantelidis, Horváth and Thomée (2015) give the wider conceptual setting. Closely related results for uniform periodic meshes, nonuniform Dirichlet chains, arbitrary four-element rings, and alternating six-element rings do not imply the one-stretched-element five-ring formula without a new calculation and sign classification. The present result isolates a case in which a bypass path makes the classical sufficient timestep bound asymptotically overconservative by a factor growing linearly with mesh stretch.

## Limitations
Only the five-element periodic ring with four equal short cells and one long cell is classified. The result does not establish threshold monotonicity as a function of the stretch, a formula for arbitrary periodic meshes, or semigroup positivity. Exact historical completeness is not asserted: some plausible specialized primary papers could not be inspected in their entirety. All calculations are same-source algebraic verifications, not independent external validation.

## References
1. X. Li and W. Huang, *Maximum principle for the finite element solution of time dependent anisotropic diffusion problems*, arXiv:1209.5657, initially posted 2012-09-25; later *Numerical Methods for Partial Differential Equations* 29 (2013), 1963–1985. DOI: 10.1002/num.21784.
2. V. Thomée and L. B. Wahlbin, *On the existence of maximum principles in parabolic finite element equations*, *Mathematics of Computation* 77 (2008), 11–19. DOI: 10.1090/S0025-5718-07-02021-2.
3. P. Chatzipantelidis, Z. Horváth, and V. Thomée, *On Preservation of Positivity in Some Finite Element Methods for the Heat Equation*, *Computational Methods in Applied Mathematics* 15 (2015), 417–437. DOI: 10.1515/cmam-2015-0018.
