# An exact longest-edge positivity law for consistent-mass heat steps on metric trees

## Finding
For every finite metric tree with at least three vertices, the consistent-mass piecewise-linear finite-element backward-Euler heat update is entrywise nonnegative precisely at time step zero and at all positive steps at least one-sixth of the **square of the longest edge length**:
\[
P(t)\geq0\quad\Longleftrightarrow\quad t=0\ \text{or}\ t\geq\frac16\max_{e\in E}h_e^2.
\]
For each edge longer than the admissible step scale, a **strictly negative entry at graph distance two** certifies failure. In contrast, every diagonal and adjacent-vertex entry remains strictly positive for every positive step. A single-edge tree is exceptional: all its entries remain nonnegative for every step.

## Assumptions and scope
Let \(G=(V,E)\) be an arbitrary finite, simple, connected, acyclic graph with \(n=|V|\geq3\), and choose an arbitrary length \(h_e>0\) independently for every edge \(e\in E\). On each edge use the continuous, affine nodal functions for the standard unit-diffusivity heat equation, with continuity at junctions, Kirchhoff flux balance, and natural Neumann endpoint conditions. Assemble the **consistent**, not lumped, mass matrix \(M\) and stiffness matrix \(K\) from the respective local two-by-two matrices
\[
M_e=\frac{h_e}{6}\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad
K_e=\frac1{h_e}\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]
Both matrices are indexed by all vertices, with no eliminated Dirichlet unknowns. The matrix \(M\) is positive definite, \(K\) is positive semidefinite with \(K\mathbf1=0\), and for \(t\geq0\) the backward-Euler map is \(P(t)=(M+tK)^{-1}M\). Inequality \(P(t)\geq0\) means **every entry** is nonnegative, equivalently every nonnegative nodal input remains nonnegative after one step. The claim makes no assertion for graphs with cycles, Dirichlet elimination, coefficient jumps, or nonstandard quadrature.

## Proof
Write \(H=M+tK\). For an edge \(e=ab\), put
\[
\alpha_e=\frac{h_e}{6}>0,\qquad
\beta_e=\frac{h_e}{6}-\frac{t}{h_e}.
\]
Thus the off-diagonal entry \(H_{ab}\) is exactly \(\beta_e\) when \(ab\in E\), and zero otherwise. Fix \(t>0\), a vertex \(b\), and its column \(x=P(t)e_b\). For each neighbor \(a\) of \(b\), delete the edge \(ab\), and let \(T_a\) denote the component containing \(a\). Define
\[
g_a=\bigl(H_{T_a}^{-1}\bigr)_{aa}>0,
\]
where \(H_{T_a}\) is the indicated principal submatrix of \(H\). The principal matrix is positive definite. Crucially, for every vector supported on \(T_a\), its quadratic form contains the **parent edge's diagonal contribution** \((h_{ab}/3+t/h_{ab})x_a^2\) and nonnegative positive-semidefinite contributions from all edges internal to \(T_a\). The Schur minimum for \(x_a=1\) therefore gives
\[
\frac1{g_a}\geq\frac{h_{ab}}3+\frac{t}{h_{ab}} > -\beta_{ab}\quad\text{whenever }\beta_{ab}<0.
\]
Consequently \(1+\beta_{ab}g_a>0\) regardless of the sign of \(\beta_{ab}\).

The restricted right-hand side \((Me_b)|_{T_a}\) equals \(\alpha_{ab}e_a\). Solving on the component gives
\[
x_a=g_a(\alpha_{ab}-\beta_{ab}x_b).
\]
Eliminating the neighboring components in the equation at \(b\) yields \(x_b=N_b/S_b\), where
\[
S_b=\sum_{a\sim b}\left(\frac{h_{ab}}3+\frac{t}{h_{ab}}-\beta_{ab}^2g_a\right)>0,
\qquad
N_b=\sum_{a\sim b}\left(\frac{h_{ab}}3-\alpha_{ab}\beta_{ab}g_a\right).
\]
Here \(S_b\) is the positive Schur complement of \(H\). Every summand of \(N_b\) is positive: if \(\beta_{ab}\leq0\), this is immediate, while if \(\beta_{ab}>0\), then \(\beta_{ab}\leq\alpha_{ab}\) and
\[
\alpha_{ab}\beta_{ab}g_a\leq\frac{(h_{ab}/6)^2}{h_{ab}/3+t/h_{ab}}<\frac{h_{ab}}{12}<\frac{h_{ab}}3.
\]
Moreover
\[
S_b-N_b=t\sum_{a\sim b}\frac{1+\beta_{ab}g_a}{h_{ab}}>0.
\]
Therefore \(0<x_b<1\), proving strict positivity of every diagonal entry. For adjacent vertices \(a\sim b\),
\[
P(t)_{ab}=x_a=g_a\left[\alpha_{ab}(1-x_b)+\frac{t}{h_{ab}}x_b\right]>0.
\]
These diagonal and adjacency statements hold for **every** positive step and every positive edge-length assignment.

For necessity, suppose some edge \(uv\) satisfies \(0<t<h_{uv}^2/6\); equivalently \(\beta_{uv}>0\). Since \(n\geq3\), at least one of its endpoints, say \(u\), has a second neighbor \(w\ne v\). For column \(x=P(t)e_w\), the just-proved adjacency result gives \(x_u>0\). The component \(T_v\) cut off by deleting \(uv\) contains no vertex in the support of \(Me_w\), because the graph is a tree and \(d(v,w)=2\). Its equations reduce to \(H_{T_v}x_{T_v}=-\beta_{uv}x_u e_v\). Thus
\[
P(t)_{vw}=x_v=-\beta_{uv}\bigl(H_{T_v}^{-1}\bigr)_{vv}P(t)_{uw}<0.
\]
This gives an explicit **distance-two negative witness for every overlong element**, not merely an asymptotic or numerical obstruction.

For sufficiency, assume \(t\geq \max_{e\in E}h_e^2/6\). Then every \(\beta_e\leq0\), so the symmetric positive-definite matrix \(H\) is a Stieltjes matrix and \(H^{-1}\geq0\) entrywise. Since \(M\geq0\), the update \(P(t)=H^{-1}M\geq0\). At \(t=0\), the update is exactly the identity. If \(n=2\), no distance-two witness exists, while the same diagonal and adjacency argument proves that every entry is positive when \(t>0\). This completes all cases.

## Verification
The accompanying standalone `verify.py` uses Python's standard-library exact rational arithmetic, assembles both local element matrices independently, solves \((M+tK)P=M\) by rational Gauss-Jordan elimination, and checks the row-sum identity, diagonal and adjacency positivity, every stipulated negative distance-two witness, the sharp boundary step, and the two-vertex exception. Its deterministic run reports **57 distinct metric-tree configurations and 411 exact rational matrix/step checks**. The finite checks support the derivation; the proof above, not enumeration, covers arbitrary finite tree size, edge grading, and positive real step.

## Relationship to prior work
Schatz, Thomée and Wahlbin (2010) analyze positivity in finite-element time stepping and describe the Stieltjes-matrix time-step sufficiency mechanism for polygonal-domain heat equations. Jin, Lazarov, Thomée and Zhou's arXiv version of 9 October 2015 develops nonnegativity questions and sufficient positivity thresholds for standard Galerkin and related methods on polygonal planar domains, including fractional diffusion. The present result concerns **Kirchhoff-coupled metric trees**, supplies a necessary-and-sufficient scalar threshold for **every** finite tree with arbitrary positive element lengths, and forces a definite negative entry at two-hop distance below that threshold. The standard Stieltjes sufficiency observation is an antecedent, not the full tree-specific necessity result. A separate exact Dirichlet interval-mesh calculation concerns path geometry after elimination of boundary degrees of freedom; it does not imply the junction-and-Neumann all-tree claim here.

## Limitations
Only one backward-Euler step for unit diffusivity, consistent piecewise-linear mass, and finite tree geometry is treated. The time step zero is an isolated nonnegative point. Nonnegative does not mean that the update is entrywise strictly positive at the sharp endpoint, and no claim about cycles, nonlinear equations, arbitrary damping, or higher-order time integrators follows. While the displayed matrix identities and argument establish the stated mathematics, a separate independent audit has not been performed. A specialized historical treatment of metric-tree consistent-mass positivity could still overlap with this formulation.

## References
1. A. H. Schatz, V. Thomée, L. B. Wahlbin, *On Positivity and Maximum-Norm Contractivity in Time Stepping Methods for Parabolic Equations*, Computational Methods in Applied Mathematics **10** (2010), 421–443, doi:10.2478/cmam-2010-0025.
2. B. Jin, R. Lazarov, V. Thomée, Z. Zhou, *On Nonnegativity Preservation in Finite Element Methods for Subdiffusion Equations*, arXiv:1510.02825v1 (first public posting 2015-10-09), https://arxiv.org/abs/1510.02825.
3. P. Chatzipantelidis, Z. Horváth, V. Thomée, *On Preservation of Positivity in Some Finite Element Methods for the Heat Equation*, Computational Methods in Applied Mathematics **15** (2015), 417–437, doi:10.1515/cmam-2015-0018.
