# A persistent interior saddle omitted from a tripartite green-innovation game
## Finding
For the tripartite replicator equations
\[
\dot x=x(1-x)g_x,\qquad
\dot y=y(1-y)g_y,\qquad
\dot z=z(1-z)g_z,
\]
printed by Su, Jia, and Xin, the payoff-difference brackets are
\[
g_x=(u_1-u_2)yz+u_2-c_0,
\]
\[
g_y=(s_1+f_1)x+(aR-2d_1)z+d_1-C_1-l_1,
\]
\[
g_z=(s_2+f_2)x+\bigl((1-a)R-2d_2\bigr)y+d_2-C_2-l_2.
\]
The article lists the eight pure-strategy vertices and later states that there is no internal equilibrium. The printed equations do admit robust interior equilibria.

For
\[
a=\frac12,\quad R=4,\quad
s_1=f_1=s_2=f_2=1,\quad
d_1=d_2=\frac12,
\]
\[
C_1=C_2=l_1=l_2=1,\qquad
u_1=3,\quad u_2=1,\quad c_0=\frac32,
\]
the exact interior equilibrium is
\[
(x^*,y^*,z^*)=\left(\frac12,\frac12,\frac12\right).
\]
It persists under all sufficiently small parameter perturbations and is a hyperbolic saddle.

Moreover, at every interior equilibrium of the printed constant-\(R\) model,
\[
\operatorname{tr}J=0.
\]
Therefore every hyperbolic interior equilibrium is saddle-type. Mixed equilibria are not absent, although a hyperbolic one cannot be an asymptotically stable ESS.

## Assumptions and scope
The variables \(x,y,z\in[0,1]\) have the strategy-proportion meanings used in the source. All cost, subsidy, penalty, risk, and payoff parameters in the explicit example are positive, and \(a=1/2\) is a valid benefit-distribution ratio.

The source defines effective costs \(C_1\) and \(C_2\) from positive component costs and sensitivity parameters. The example requires only the effective values \(C_1=C_2=1\), which have many positive realizations.

The proof concerns the source's printed constant-\(R\) system. It does not cover the optional nonlinear extension \(R=R_0+\lambda yz\). The constructed vector is an admissible model example, not the source's numerical calibration.

## Proof
At an interior point, the three factors \(x(1-x)\), \(y(1-y)\), and \(z(1-z)\) are positive. Hence an interior equilibrium is exactly a solution of
\[
g_x=g_y=g_z=0.
\]
For the displayed parameters,
\[
g_x=2yz-\frac12,\qquad
g_y=2x+z-\frac32,\qquad
g_z=2x+y-\frac32.
\]
All three vanish at \((1/2,1/2,1/2)\).

The derivative of the bracket map \(G=(g_x,g_y,g_z)\) there is
\[
M=
\begin{pmatrix}
0&1&1\\
2&0&1\\
2&1&0
\end{pmatrix},
\qquad \det M=4.
\]
The implicit-function theorem therefore gives a unique nearby solution of \(G=0\) after every sufficiently small parameter perturbation. Since the reference point lies strictly inside the unit cube, sufficiently nearby solutions remain interior.

At any interior equilibrium, each payoff bracket vanishes and is independent of its own strategy coordinate. Thus the three diagonal entries of the full replicator Jacobian vanish and
\[
\operatorname{tr}J=0.
\]
If the equilibrium is hyperbolic, no eigenvalue has zero real part. Since the real parts sum to zero, at least one is positive and at least one is negative, so the equilibrium is saddle-type.

For the explicit example,
\[
J=\frac14
\begin{pmatrix}
0&1&1\\
2&0&1\\
2&1&0
\end{pmatrix}.
\]
Its characteristic polynomial factors as
\[
\left(\lambda+\frac14\right)
\left(\lambda^2-\frac14\lambda-\frac14\right),
\]
with eigenvalues
\[
-\frac14,\qquad
\frac{1-\sqrt{17}}8,\qquad
\frac{1+\sqrt{17}}8.
\]
Exactly one is positive and two are negative.

## Verification
The bundled `verification/verify.py` checks the exact bracket residuals, the determinant \(4\), the characteristic polynomial, and the eigenvalues using rational arithmetic and the Python standard library. The persistence claim is analytic and follows from the implicit-function theorem.

## Relationship to prior work
The motivating 2026 article prints the three replicator equations, lists eight pure-strategy equilibria, and later states that there is no internal equilibrium while immediately referring to an internal equilibrium as an unstable saddle. The present result resolves that tension directly from the printed equations.

Mixed equilibria are standard possibilities in tripartite evolutionary games. Li et al. (2021) explicitly report internal equilibria in a different subsidy-and-punishment game, while Liang et al. (2023) retain a mixed-strategy equilibrium in a different collaborative-innovation game. Those papers do not contain this source's payoff brackets, the exact equilibrium above, the persistence determinant, or its exact spectrum.

## Limitations
The result does not alter the source's pure-strategy eigenvalue calculations at the cube vertices and does not assert that the source's numerical calibration has an interior equilibrium.

A saddle's stable manifold can organize basin boundaries in bistable systems, but no global separatrix theorem is claimed here. Nonhyperbolic interior equilibria are not classified by the trace-zero observation alone.

## References
1. N. Su, S. Jia, Y. Xin, “Tripartite Evolutionary Game Model and Stability Analysis for Collaborative Innovation in Traditional Energy Enterprises,” Mathematics 14 (2026), 1968. DOI: 10.3390/math14111968.
2. J. Li et al., “Analysis of a Multiparticipant Game under a Subsidy and Punishment Mechanism: An Evolutionary Theory Perspective,” Mathematical Problems in Engineering 2021 (2021), 1984676. DOI: 10.1155/2021/1984676.
3. J. Liang et al., “Analysis of Public Technology Collaborative Innovation Based on Private Technology: A Tripartite Evolutionary Game Approach,” Complexity 2023 (2023), 1700651. DOI: 10.1155/2023/1700651.
