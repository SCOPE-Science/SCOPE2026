# Exact adjacency–Dirac edge distance and its avoided-crossing asymptotics on triangular graphs

## Finding
Let \(J(n,2)\) be the graph of two-element subsets of \(\{0,\ldots,n-1\}\), adjacent when they intersect in exactly one element. For every integer \(n\ge5\), equip the complex Hilbert space \(\ell_2(V(J(n,2)))\) with the **unweighted adjacency Dirac operator** \(D\), and represent real vertex functions by diagonal multiplication operators. Write \(d_D\) for the resulting Connes distance. Every adjacent pair has the same distance, as follows.

Put \(m=n-3\), and, for real \(t\), set
\[
\begin{aligned}
 A_m(t)&=6+3m-2mt+mt^2,\\
 C_m(t)&=m-2mt+(7m+2)t^2,\\
 B_m(t)&=-2+8t-2t^2,\\
 \Phi_m(t)&=\frac{A_m(t)+C_m(t)+\sqrt{(A_m(t)-C_m(t))^2+4mB_m(t)^2}}{2}.
\end{aligned}
\]
Then \(\Phi_m\) is **strongly convex**, has a unique global minimizer \(t_m\), and
\[
\boxed{\quad d_D(\{0,1\},\{0,2\})=\frac{2}{\sqrt{\Phi_m(t_m)}}.\quad}
\]
The formula is an exact, uniquely specified one-variable algebraic prescription: \(t_m\) is the unique minimizer of the displayed elementary radical function, so no optimization over vertex functions or large matrices remains. Equivalently the minimum is the least possible top eigenvalue of the explicit two-by-two matrix \(\begin{psmallmatrix}A_m(t)&\sqrt m B_m(t)\\\sqrt m B_m(t)&C_m(t)\end{psmallmatrix}\).

There is also an explicit sharp **two-term high-degree expansion**. Put
\[
\begin{aligned}
 t_*&=1/\sqrt3, & L&=10/3-2/\sqrt3,\\
 a&=-2+2/\sqrt3,&c&=-2+14/\sqrt3,\\
 r&=-8/3+8/\sqrt3,& C_*&=\frac{2r\sqrt{-ac}}{c-a}.
\end{aligned}
\]
Here \(a<0<c\), \(r>0\). As \(m\to\infty\),
\[
\begin{aligned}
 t_m&=t_*-\frac{r(a+c)}{(c-a)\sqrt{-ac}}\,m^{-1/2}+O(m^{-1}),\\
 \Phi_m(t_m)&=mL+C_*\sqrt m+O(1),\\
 d_D(\{0,1\},\{0,2\})&=\frac{2}{\sqrt L}\,m^{-1/2}-\frac{C_*}{L^{3/2}}\,m^{-1}+O(m^{-3/2}).
\end{aligned}
\]
The first coefficient is approximately \(1.354995888\), and \(C_*\) is approximately \(1.277850663\). Thus the noncommutative length of a unit graph edge decays with graph order despite its graph-geodesic length remaining \(1\); the second term comes from coupling of two asymptotically crossing spectral modes.

## Assumptions and scope
The adjacency matrix has \(D_{xy}=1\) for distinct adjacent vertices and \(0\) otherwise. For real \(f:V\to\mathbb R\), let \(F=\operatorname{diag}(f)\) and \(L_D(f)=\|[D,F]\|_{\ell_2\to\ell_2}\). The distance is \(d_D(u,v)=\sup\{|f(u)-f(v)|:L_D(f)\le1\}\), with operator norm over the **complex** Hilbert space. Since \([D,F]\) is real skew symmetric, its complex and real operator norms agree. All assertions are for every integer \(n\ge5\), not for weighted graphs or alternative graph-Dirac constructions. Every edge is equivalent under permutations of the ground set.

## Proof
**1. An exact symmetry reduction, without loss in the original distance.** Fix \(u=\{0,1\}\) and \(v=\{0,2\}\). Average a feasible potential over permutations of \(R=\{3,\ldots,n-1\}\), then antisymmetrize under interchanging the labels \(1\) and \(2\). The objective \(f(u)-f(v)\) is preserved in both operations, and the commutator norm cannot increase: both operations average graph automorphism conjugates, with a sign in the antisymmetrization. Every resulting function has the form
\[
 f(u)=s,\quad f(v)=-s,\quad
 f(\{1,i\})=h,\quad f(\{2,i\})=-h\quad(i\in R),
\]
with all other vertex values zero. For \(s>0\), rescale to \(s=1\) and write \(t=h/s\). The exact distance therefore is \(2/\inf_{t\in\mathbb R}\|K_t\|\), where \(K_t=[D,F_t]\). Connectivity makes the infimum positive.

**2. The full commutator norm collapses to two dimensions.** Let \(P\) be the permutation of the two-subsets induced by the transposition \((1\;2)\). Since \(PF_tP^*=-F_t\) and \(PDP^*=D\), \(PK_tP^*=-K_t\). Hence \(K_t\) exchanges the positive and negative eigenspaces of \(P\). An orthonormal basis of the negative eigenspace is
\[
 h_0=(e_{\{0,1\}}-e_{\{0,2\}})/\sqrt2,
 \qquad h_i=(e_{\{1,i\}}-e_{\{2,i\}})/\sqrt2\quad(i\in R).
\]
Directly counting the adjacency entries in \(K_t\) gives the Gram matrix \(G=(\langle K_th_i,K_th_j\rangle)\) indexed by \(\{0\}\cup R\):
\[
\begin{aligned}
 G_{00}&=A_m(t),&G_{0i}&=B_m(t),\\
 G_{ii}&=1-2t+(2m+7)t^2,&
 G_{ij}&=1-2t+5t^2\quad(i\ne j\in R).
\end{aligned}
\]
As \(K_t\) exchanges the parity subspaces and is skew-adjoint, \(\|K_t\|^2=\lambda_{\max}(G)\), with no missing singular values. The zero-sum subspace of \(\operatorname{span}\{h_i:i\in R\}\) has eigenvalue \((2m+2)t^2\) (multiplicity \(m-1\)). On its orthogonal complement, spanned by \(h_0\) and \(m^{-1/2}\sum_{i\in R}h_i\), the Gram matrix is
\[
 M_m(t)=\begin{pmatrix}A_m(t)&\sqrt m B_m(t)\\\sqrt m B_m(t)&C_m(t)\end{pmatrix}.
\]
For every real \(t\), \(C_m(t)-(2m+2)t^2=m(1-2t+5t^2)>0\), since \(1-2t+5t^2=5(t-1/5)^2+4/5\). Thus the top eigenvalue of \(G\) always comes from \(M_m(t)\), giving \(\|K_t\|^2=\Phi_m(t)\) and the exact distance formula.

**3. Uniqueness of the algebraic prescription.** There is a real matrix pencil \(T_0+tT_1\) whose two row Gram matrix is \(M_m(t)\): the two rows are the coefficients of \(K_t\) between the two invariant negative-parity modes and the five positive-parity orbit modes. The coefficient of \(t^2\) in \(M_m(t)\) is
\[
 H_m=\begin{pmatrix}m&-2\sqrt m\\-2\sqrt m&7m+2\end{pmatrix},
 \qquad \det H_m=m(7m-2)>0.
\]
For every unit \(z\in\mathbb R^2\), \(z^*M_m(t)z=\|(T_0+tT_1)^*z\|^2\) has second derivative at least \(2\lambda_{\min}(H_m)>0\). Taking the supremum over all such \(z\) preserves this uniform strong-convexity inequality. Hence \(\Phi_m=\lambda_{\max}(M_m)\) is strongly convex and coercive, with a unique minimizer. The exact prescription therefore has no ambiguous root choices.

**4. The avoided-crossing limit.** Dividing the explicit matrix by \(m\), its diagonal entries converge on compact \(t\)-intervals to
\[
 q_1(t)=3-2t+t^2,\qquad q_2(t)=1-2t+7t^2,
\]
while its off-diagonal entries are \(O(m^{-1/2})\). The limiting top-eigenvalue function \(\max\{q_1,q_2\}\) has a unique minimizer \(t_*=1/\sqrt3\): on \([0,t_*]\), \(q_1\) is decreasing, and on \([t_*,\infty)\), \(q_2\) is increasing; negative arguments give a strictly larger value. Its minimum is \(L\). The bound \(\Phi_m(t)\ge A_m(t)=m((t-1)^2+2)+6\) makes the minimizers uniformly bounded, proving \(t_m\to t_*\).

Moreover \(\Phi_m(t_*)=mL+O(\sqrt m)\), whereas \(\Phi_m(t)\ge m\max\{q_1(t),q_2(t)\}\), up to bounded additive terms on a fixed neighborhood. Since the two curves cross with nonzero and opposite slopes \(a,c\), it follows that \(t_m=t_*+O(m^{-1/2})\). Set \(t=t_*+z/\sqrt m\). Uniformly for bounded real \(z\), the top eigenvalue expands as
\[
 \Phi_m(t)=mL+\sqrt m\left[\frac{a+c}{2}z+
 \sqrt{\frac{(c-a)^2}{4}z^2+r^2}\right]+O(1).
\]
The bracket has a unique minimizer
\[
 z_*=-\frac{r(a+c)}{(c-a)\sqrt{-ac}},
\]
and its minimum is \(C_*=2r\sqrt{-ac}/(c-a)\). The spectral gap in the bracket is positive because \(r>0\); smooth expansion of the first-order optimality equation near \(z_*\) yields \(z_m=z_*+O(m^{-1/2})\). Comparing upper and lower expansions at these bounded minimizing \(z_m\) proves \(\Phi_m(t_m)=mL+C_*\sqrt m+O(1)\). Taylor expansion of the reciprocal square root yields the stated distance expansion with remainder \(O(m^{-3/2})\).

## Verification
Run the included Python 3 standard-library script `verify.py`. It builds the **actual full adjacency commutator** for \(5\le n\le10\) and nine rational parameters per graph; it verifies the complete anti-parity Gram entries, the exactly decomposed scalar and two-dimensional blocks, skew-adjointness, and the parity relation with integer/rational arithmetic. Recorded replay: `CHECK_OK: exact rational Gram blocks, parity, and norm domination; 89685 assertions across 54 graph/parameter cases`. For orientation, the edge distance is approximately \(0.6055665637\) at \(n=5\), \(0.5477117937\) at \(n=6\), and \(0.5040296107\) at \(n=7\). These are numerical illustrations, not certificates of the infinite theorem. The full-dimension count in Step 2 and the analytic limit argument establish the unrestricted statements.

## Relationship to prior work
Iochum, Krajewski and Martinetti established foundational finite spectral-distance constructions and examples (1999/2001); Besnard surveyed graph Connes distances, general graph-geodesic comparisons, and bounds (2021). Clare, Li, Poon and Swartz (first public September 6, 2024) analyzed finite graph spectral distances and gave complete formulas for paths; Swartz (October 2026) studied their behavior under edge and vertex deletion. The checked full-text sections do **not** assert the two-subset Johnson-graph edge formula, its exact two-dimensional reduction, or its spectral avoided-crossing expansion. Those general theories supply the *definition* and some universal inequalities, not a quantitatively equivalent answer. The earlier complete-graph formula is for the different graph \(K_N\), not the line graph \(L(K_n)\). This is a source-bounded originality assessment, not a claim of exhaustive historical uniqueness.

## Limitations
This theorem determines the edge orbit, not the distance between disjoint two-subsets. It uses a specific adjacency Dirac operator and does not apply to the alternative graph-Dirac constructions that recover shortest-path distance. The exact finite-\(n\) formula retains a uniquely specified scalar algebraic minimization rather than a uniform elementary expression in radicals of \(n\). The finite checker corroborates the Gram calculation, not the full infinite asymptotic argument. Independent mathematical validation and exhaustive historical priority confirmation have not been performed.

## References
1. B. Iochum, T. Krajewski, P. Martinetti, *Distances in Finite Spaces from Noncommutative Geometry*, first public 1999-12-22, arXiv:hep-th/9912217.
2. F. Besnard, *Estimating noncommutative distances on graphs*, first public 2021-05-19, arXiv:2105.09056.
3. P. Clare, C.-K. Li, E. Poon, E. Swartz, *Noncommutative distances on graphs: An explicit approach via Birkhoff-James orthogonality*, first public 2024-09-06, arXiv:2409.04146.
4. E. Swartz, *The effect of edge deletion on noncommutative distances on graphs*, first public 2026-10-06, arXiv:2610.07718 (later context, not dating source).
