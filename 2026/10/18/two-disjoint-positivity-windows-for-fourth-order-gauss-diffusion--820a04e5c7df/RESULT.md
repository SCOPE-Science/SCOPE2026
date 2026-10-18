# Two disjoint positivity windows for fourth-order Gauss diffusion on double-star trees

## Finding

Let \(D_m\), for an integer \(m\ge2\), be the unweighted tree whose two adjacent hubs each have exactly \(m\) pendant leaves, and let \(L_m\) denote its combinatorial Laplacian. Consider the two-stage, fourth-order Gauss–Legendre Runge–Kutta endpoint map for graph heat diffusion,
\[
T_m(h)=(12I-6hL_m+h^2L_m^2)(12I+6hL_m+h^2L_m^2)^{-1},\qquad h\ge0.
\]
Define the two quartic polynomials
\[
H_m(h)=(h^2+6h+12)^2+m^2h^2(h^2-12),
\]
\[
P_m(h)=(h^2+6h+12)^2+m^2h^2(12-h^2)+2mh^2(24-h^2)+72mh.
\]
For every \(m\ge2\), \(P_m\) has exactly one positive root \(\eta_m\), and \(2\sqrt3<\eta_m<12\). If \(2\le m\le4\), the complete set of nonnegative timesteps is
\[
\{h\ge0:T_m(h)\ge0\ \text{entrywise}\}=[0,\eta_m].
\]
If \(m\ge5\), \(H_m\) has exactly two positive roots \(0<h_-(m)<2<h_+(m)<2\sqrt3\), and the complete positivity set is
\[
\boxed{[0,h_-(m)]\ \cup\ [h_+(m),\eta_m].}
\]
Both intervals have positive length, separated by a nonempty interval of negative matrix entries. Thus the smallest balanced double-star tree exhibiting this loss-and-recovery behavior has \(2m+2=12\) vertices. For this first case, \(m=5\), the three thresholds are approximately \(h_-=1.4482236063\), \(h_+=2.0807066361\), and \(\eta_5=4.7570266439\); exactly, \(H_5(2)=-16\), \(H_5(3)=846\), and \(P_5(5)=-2086\). For every \(h\ge0\), the map remains symmetric, strictly positive definite, and row-stochastic (row sums equal one); it loses only entrywise nonnegativity. The asymptotic locations of the transitions satisfy
\[
\lim_{m\to\infty}m h_-(m)=2\sqrt3,\quad
\lim_{m\to\infty}m^2(2\sqrt3-h_+(m))=
\frac{(24+12\sqrt3)^2}{2(2\sqrt3)^3},\quad
\lim_{m\to\infty}m(\eta_m-2\sqrt3)=3+2\sqrt3.
\]
In particular, the recovered positivity interval has length asymptotic to \((3+2\sqrt3)/m\).

## Assumptions and scope

The graph is simple, finite, undirected, and unweighted. Every hub has \(m\) private leaves, and the hubs are connected by one edge; there are no other edges. The step is the exact rational matrix function (not the exact heat semigroup). Positivity means every matrix entry is nonnegative, including at boundary timesteps. All inequalities and transition descriptions hold for every integer \(m\ge2\), and no symmetry of initial states is imposed. The denominator is nonsingular for all \(h\ge0\), as every Laplacian eigenvalue \(\lambda\ge0\) gives a positive scalar denominator \(12+6h\lambda+h^2\lambda^2\).

## Proof

**Block reduction and entry formulas.** There are five orbits of off-diagonal matrix entries: hub–hub, hub–a leaf at that hub, hub–a leaf at the other hub, two distinct leaves at the same hub, and leaves at opposite hubs. The two-dimensional symmetric and antisymmetric representations of the Laplacian on hub/leaf-mean coordinates are
\[
A_m=\begin{pmatrix}m&-m\\-1&1\end{pmatrix},\qquad
B_m=\begin{pmatrix}m+2&-m\\-1&1\end{pmatrix}.
\]
Let \(R_h(X)=(12I-6hX+h^2X^2)(12I+6hX+h^2X^2)^{-1}\), \(S=R_h(A_m)\), and \(U=R_h(B_m)\). Differences among leaf coordinates have eigenvalue \(1\) and scalar step \(r(-h)=(h^2-6h+12)/(h^2+6h+12)\). The five off-diagonal entries, in the order just listed, are
\[
\frac{S_{11}-U_{11}}2,\qquad
\frac{S_{12}+U_{12}}{2m},\qquad
\frac{S_{12}-U_{12}}{2m},\qquad
\frac{S_{22}+U_{22}-2r(-h)}{2m},\qquad
\frac{S_{22}-U_{22}}{2m}.
\]
Set the positive denominator factors
\[
D_1=h^2+6h+12,\quad
D_S=(m+1)^2h^2+6(m+1)h+12,
\]
\[
D_A=h^4+3(m+3)h^3+3(m^2+6m+11)h^2+18(m+3)h+36.
\]
Direct \(2\times2\) inversion simplifies the five off-diagonal entries to
\[
\frac{3hH_m(h)}{D_SD_A},\quad
\frac{3hP_m(h)}{D_SD_A},\quad
\frac{3h^2C_m(h)}{D_SD_A},\quad
\frac{3h^2Q_m(h)}{D_1D_SD_A},\quad
\frac{3h^3E_m(h)}{D_SD_A},
\]
where the following polynomials are strictly positive for positive \(h\), except that \(Q_m\) is only asserted positive for \(0<h\le12\):
\[
C_m(h)=(m^2+2m+3)h^3+(12m+24)h^2+(24m+72)h+72,
\]
\[
E_m(h)=(m^2+4m+5)h^2+(12m+24)h+24,
\]
\[
\begin{aligned}
Q_m(h)={}&(3-m^2)h^5+(6m^2+24m+42)h^4\\
&+(12m^3+84m^2+228m+252)h^3\\
&+(144m^2+648m+792)h^2+(576m+1296)h+864.
\end{aligned}
\]
Because \(m\ge2\), all coefficients of \(Q_m\) other than its negative leading coefficient are positive, and Descartes' sign rule gives one positive root. Furthermore,
\[
Q_m(12)=864(24m^3+48m^2+1148m+2527)>0;
\]
therefore that root is greater than \(12\), so \(Q_m>0\) throughout the range potentially allowed by \(P_m\).

**Root counts and support intervals.** The coefficient sequence of \(P_m\), from highest degree down, is negative then positive, positive, positive, positive: its leading coefficient is \(1-m^2-2m<0\), and every other coefficient is strictly positive. Thus Descartes' sign rule gives exactly one positive root, since \(P_m(0)=144>0\) and \(P_m(h)\to-\infty\). At \(s=2\sqrt3\),
\[
P_m(s)=(24+6s)^2+288m+72ms>0,
\]
and \(P_m(12)=51984-19008m^2-33696m<0\). Hence \(s<\eta_m<12\), and the hub–own-leaf entry is nonnegative exactly for \(0\le h\le\eta_m\).

For \(h\ge s\), \(H_m(h)>0\). For \(0<h<s\) and \(2\le m\le4\), \(H_m(h)\ge H_4(h)\), and
\[
H_4(h)=17h^4+12h^3-132h^2+144h+144.
\]
The arithmetic–geometric mean inequality gives \(17h^4+144\ge24\sqrt{17}\,h^2\) and \(12h^3+144h\ge48\sqrt3\,h^2\). Since \(24\sqrt{17}+48\sqrt3>132\), \(H_4(h)>0\). Thus no hub–hub sign loss occurs for \(m\le4\).

For \(m\ge5\), \(H_m(0)=144>0\), \(H_m(2)=784-32m^2<0\), and \(H_m(s)=(24+6s)^2>0\). The coefficients of \(H_m\), from leading to constant, have signs \(+,+,-,+,+\), allowing at most two positive roots. Thus there are exactly two, one in \((0,2)\) and one in \((2,s)\), and \(H_m\ge0\) precisely outside the open interval between these roots. Combining the five off-diagonal signs proves the stated positivity sets.

**Diagonal entries and normalization.** As \(L_m\) is symmetric positive semidefinite, every eigenvalue of \(T_m(h)\) is \(r(-h\lambda)>0\): the numerator \((h\lambda-3)^2+3\) and denominator are positive. Consequently all diagonal entries are strictly positive. Moreover \(L_m\mathbf1=0\) and \(r(0)=1\), so every row sum is one. These observations complete the all-entry proof.

**Scaling of switching boundaries.** For \(h=c/m\), \(H_m(h)=144-12c^2+o(1)\), giving \(m h_-\to s\). For \(h=s-d/m^2\), \(H_m(h)=(24+6s)^2-2s^3d+o(1)\), yielding the stated limit for \(s-h_+\). Finally \(h=s+c/m\) in \(P_m\) gives, after division by \(m\), \(-2s^3c+288+72s+o(1)\), so \(c=(288+72s)/(2s^3)=s+3\). Uniqueness of the positive roots and their bracketing above justify these limits.

## Verification

The standalone `artifacts/check_double_star.py` checks all five rational identities symbolically in the parameters \(m,h\), checks the exact threshold-factor evaluations, and independently constructs full Laplacian matrices for \(m=2,\ldots,10\) at eight rational step sizes. It verifies the five entry categories, row sums, and matrix symmetry using exact arithmetic. Execute `python artifacts/check_double_star.py` with SymPy installed. Finite full-matrix checks illustrate the proof; the polynomial signs, symmetry decomposition, and root arguments above establish the theorem for every integer parameter.

## Relationship to prior work

The classical theory of absolute monotonicity explains why high-order rational Runge–Kutta steps need not preserve positivity uniformly over all positive generators. Zappavigna, Colaneri, Kirkland, and Shorten (2012) construct positive-system counterexamples using triangular Metzler matrices; their framework does not classify the balanced reversible double-star heat generator. Ketcheson, Macdonald, and Gottlieb (2009) discuss the order and SSP constraints of implicit Runge–Kutta methods, including the fourth-order two-stage method. Prior explicit positive-step classifications for regular two-row rook graphs concern Cartesian products of cliques, not this family of nonregular trees: neither graph family includes the other. The distinctive statement here is the **complete, two-interval positivity classification on every balanced double star**, with the sharp transition at twelve vertices and the two different asymptotic window scales; the Runge–Kutta method and general non-SSP phenomenon are not new.

## Limitations

The classification is only for unit-weight balanced double-star trees and the completed two-stage Gauss–Legendre step. It does not assert stagewise positivity, positivity for arbitrary trees, nonnegative floating-point arithmetic, or a global minimum number of vertices across all reversible generators. No infinite family of exact heat semigroups has disconnected positivity times: the phenomenon belongs to the rational approximation. Independent external mathematical review has not been performed. Equivalent graph-specific claims in unindexed literature remain possible.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “Essentially negative news about positive systems,” *Linear Algebra and its Applications* **436** (2012), 3425–3442. DOI: 10.1016/j.laa.2011.12.021. Full-text repository: https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf.
2. D. I. Ketcheson, C. B. Macdonald, S. Gottlieb, “Optimal implicit strong stability preserving Runge–Kutta methods,” *Applied Numerical Mathematics* **59** (2009), 373–392. Public preprint: https://www.davidketcheson.info/assets/papers/2009_implicit_ssp.pdf.
3. L. Lóczi, D. I. Ketcheson, “Rational functions with maximal radius of absolute monotonicity,” *LMS Journal of Computation and Mathematics* **17** (2014), 159–205. DOI: 10.1112/S1461157013000326.
