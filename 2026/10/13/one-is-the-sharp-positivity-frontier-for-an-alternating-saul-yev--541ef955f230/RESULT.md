# One is the sharp positivity frontier for an alternating Saul'yev diffusion pair

## Finding
Consider the one-dimensional diffusion equation
\[
u_t=D u_{xx},
\qquad D>0,
\]
on a uniform grid with \(n\ge1\) interior nodes and homogeneous Dirichlet boundary values. Put
\[
r=\frac{D\Delta t}{\Delta x^2},
\qquad
\beta=\frac{r}{1+r},
\qquad
\gamma=\frac{1-r}{1+r}.
\]

A left-to-right Saul'yev sweep is
\[
v_j
=
\beta v_{j-1}
+
\gamma u_j
+
\beta u_{j+1},
\qquad
j=1,\ldots,n,
\]
with
\[
v_0=0,\qquad u_{n+1}=0.
\]
The following right-to-left sweep is
\[
w_j
=
\beta v_{j-1}
+
\gamma v_j
+
\beta w_{j+1},
\qquad
j=n,\ldots,1,
\]
with
\[
v_0=0,\qquad w_{n+1}=0.
\]
Let \(P_n(r)\) denote the completed two-sweep map \(u\mapsto w\).

For one interior node,
\[
P_1(r)=[\gamma^2],
\]
so the alternating pair is positivity preserving for every \(r\ge0\).

For every \(n\ge2\),
\[
\boxed{
P_n(r)\ge0\text{ entrywise}
\quad\Longleftrightarrow\quad
0\le r\le1.
}
\]
Hence two interior nodes are minimal for pointwise sign loss after a complete alternating pair.

The obstruction is explicit:
\[
(P_n(r))_{n1}
=
\frac{2r^{\,n-1}(1-r)}
{(1+r)^{n+1}}.
\]
It is negative for every finite \(r>1\).

At
\[
r=2,\qquad n=2,
\]
the nonnegative initial vector
\[
u=
\begin{pmatrix}
1\\
0
\end{pmatrix}
\]
is mapped by the alternating pair to a vector whose second component is exactly
\[
-\frac4{27}.
\]

## Assumptions and scope
The result concerns the classical one-dimensional Saul'yev diffusion formulas with constant diffusion coefficient, uniform spatial mesh, homogeneous Dirichlet boundary values, exact arithmetic, and two successive sweeps in opposite directions using the same mesh ratio
\[
r=D\Delta t/\Delta x^2.
\]

The statement is about entrywise nonnegativity of the completed two-step alternating map. It does not assert positivity of each intermediate one-sided sweep when \(r>1\). It does not cover periodic boundaries, variable coefficients, nonuniform meshes, nonlinear diffusion, later group-explicit variants, or modified Saul'yev coefficients.

The result uses the historical alternation in which the left-to-right and right-to-left formulas are applied on successive time levels. It is not a statement about a Strang-style composition in which each directional factor uses half of one global time step.

## Proof
Let \(L_n(r)\) be the matrix of the left-to-right sweep and \(R_n(r)\) the matrix of the right-to-left sweep, so
\[
P_n(r)=R_n(r)L_n(r).
\]

If
\[
0\le r\le1,
\]
then
\[
\beta\ge0,\qquad\gamma\ge0.
\]
The left-to-right recurrence therefore maps every nonnegative input vector to a nonnegative output vector by induction on \(j\). The right-to-left recurrence has the same property by reverse induction. Hence
\[
P_n(r)\ge0
\]
entrywise for every \(n\ge1\).

Now suppose
\[
r>1.
\]
Then
\[
\beta>0,\qquad
\gamma<0,\qquad
1+\gamma=\frac2{1+r}>0.
\]

For the first basis vector \(e_1\), the left sweep satisfies
\[
(L_n e_1)_j
=
\beta^{\,j-1}\gamma,
\qquad
j=1,\ldots,n.
\]
The last component of the following right sweep depends only on the last two components of the left-sweep vector:
\[
(P_n e_1)_n
=
\beta(L_n e_1)_{n-1}
+
\gamma(L_n e_1)_n.
\]
For \(n\ge2\), substitution gives
\[
(P_n)_{n1}
=
\beta^{\,n-1}\gamma(1+\gamma)
=
\frac{2r^{\,n-1}(1-r)}
{(1+r)^{n+1}}
<0.
\]
Thus the pair is not entrywise nonnegative for any \(r>1\) once there are at least two interior nodes.

When \(n=1\), the left and right sweeps each multiply the sole interior value by \(\gamma\). Therefore
\[
P_1(r)=\gamma^2\ge0
\]
for every \(r\ge0\). This establishes the minimal-dimension statement.

For the concrete witness
\[
r=2,
\]
one has
\[
\beta=\frac23,\qquad
\gamma=-\frac13.
\]
At \(n=2\),
\[
(P_2)_{21}
=
\beta\gamma(1+\gamma)
=
-\frac4{27}.
\]
Taking \(u=e_1\) proves the displayed sign failure.

## Verification
The embedded `verify.py` constructs the two one-sided sweep matrices from their defining recurrences using exact rational arithmetic. It verifies the closed corner formula for several dimensions and rational values of \(r\), checks entrywise nonnegativity throughout representative values with \(0\le r\le1\), and replays the exact \(n=2\), \(r=2\) witness.

The all-\(n\) result is analytic. The finite replay does not replace the induction and corner-entry proof.

## Relationship to prior work
Saul'yev introduced asymmetric explicit diffusion formulas in the 1950s. A modern full-text treatment by Chin writes the classical coefficients as
\[
\gamma=\frac{1-r}{1+r},
\qquad
\beta=\frac{r}{1+r},
\]
states that the two one-sided algorithms are unconditionally stable, and records Saul'yev's recommendation to apply the left-to-right and right-to-left algorithms alternately to reduce error. Chin also explicitly notes that \(\gamma\) can become negative while unconditional stability persists.

The inspected full text analyzes Fourier amplification, splitting structure, accuracy, and convergence. Searches within that document for pointwise positivity, nonnegativity, monotonicity, and a maximum principle did not locate a theorem equivalent to the present entrywise classification.

Campbell and Yin analyze stability of alternating-direction explicit methods for advection-diffusion equations. The accessible abstract emphasizes stability conditions and directional alternation; its complete body was not available in the inspected retrieval path, so it remains a specific originality risk rather than evidence of noncoverage.

A 2013 stochastic alternating-direction explicit paper classifies Saul'yev-type finite-difference methods under MSC \(65M06\), together with stochastic PDE classifications. It is used here only to confirm the numerical-PDE subject classification, not as evidence for the positivity theorem.

The new content is the completed-pair cone-invariance classification: the exact threshold \(r=1\), the closed negative corner for every \(n\ge2\), and the fact that one interior node is exceptional while two are already sufficient for failure.

## Limitations
The theorem does not challenge unconditional Fourier stability of the classical Saul'yev sweeps. Stability and entrywise positivity are different properties.

The boundary conditions matter. The proof uses fixed homogeneous Dirichlet data, exactly the setting in which the directional recurrences are explicitly evaluable from one boundary toward the other.

The result concerns the historical full-step alternation. If two directional factors are instead used with half steps inside a single composed step, the dimensionless parameter entering each factor changes and so does the corresponding positivity condition.

The original 1957 Russian article and the full 2007 Campbell-Yin article were not completely inspected. Older literature may therefore contain an equivalent pointwise criterion under terminology such as monotonicity or a discrete maximum principle.

## References
1. V. K. Saul'yev, “On a method of numerical integration of a diffusion equation,” Doklady Akademii Nauk SSSR 115 (1957), 1077–1079.
2. B. K. Larkin, “Some Stable Explicit Difference Approximations to the Diffusion Equation,” Mathematics of Computation 18 (1964), 196–202.
3. L. J. Campbell and B. Yin, “On the stability of alternating-direction explicit methods for advection-diffusion equations,” Numerical Methods for Partial Differential Equations 23 (2007), 1429–1444. DOI 10.1002/num.20233.
4. S. A. Chin, “Symplectic finite-difference methods for solving partial differential equations,” arXiv:1206.1743v1, submitted 8 June 2012.
5. S. A. Chin, “Understanding Saul'yev-type unconditionally stable schemes from exponential splitting,” Numerical Methods for Partial Differential Equations 30 (2014), 1961–1983. DOI 10.1002/num.21885.
6. A. R. Soheili and M. Arezoomandan, “Approximation of stochastic advection diffusion equations with stochastic alternating direction explicit methods,” Applications of Mathematics 58 (2013), 439–471. DOI 10.1007/s10492-013-0022-6.
