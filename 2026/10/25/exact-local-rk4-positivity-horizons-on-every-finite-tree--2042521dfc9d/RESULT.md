# Exact local RK4 positivity horizons on every finite tree

## Finding
Let \(T\) be any finite simple unweighted tree with at least two vertices, with degree \(d_v\), neighbor-degree sum \(s_v=\sum_{w\sim v}d_w\), and combinatorial Laplacian \(L\). The classical fourth-order Runge--Kutta endpoint matrix for graph heat flow is
\[
K_T(h)=I-hL+\frac{h^2L^2}{2}-\frac{h^3L^3}{6}+\frac{h^4L^4}{24}.
\]
For every edge \(uv\), put \(a=d_u\), \(b=d_v\), and
\[
A_{uv}=a+b,\quad B_{uv}=a^2+ab+b^2+a+b-1,
\]
\[
C_{uv}=(a+b)(a^2+b^2)+2(a^2+ab+b^2)-2(a+b)+s_u+s_v.
\]
Let \(r_{uv}\) be the unique positive root of
\[
p_{uv}(h)=1-\frac{A_{uv}h}{2}+\frac{B_{uv}h^2}{6}-\frac{C_{uv}h^3}{24}.
\]
For every simple path \(P=(v_0,v_1,v_2,v_3)\) of length three, set \(q(P)=\sum_{i=0}^3d_{v_i}\). Define \(H_3=\min_P4/q(P)\), with \(H_3=+\infty\) if no such path exists, and \(H_1=\min_{uv\in E(T)}r_{uv}\). Then the **entire** positivity set is
\[
\boxed{\ K_T(h)\ge0\text{ entrywise}\quad\Longleftrightarrow\quad 0\le h\le \min(H_1,H_3).\ }
\]
There is no positivity reentry. The only entries that can first become negative are edge transitions and transitions between vertices at distance three. All diagonal entries and all off-diagonal entries at distances two and four are strictly positive for every \(h>0\); entries at greater distances vanish identically. The exact horizon can be computed from local tree data in linear time, apart from fixed-degree cubic root evaluations.

Both possible first-failure mechanisms occur: on the path with five vertices, distance-three transitions control the horizon \(4/7\); on the six-vertex tree obtained by subdividing one edge of \(K_{1,4}\), the central-to-subdivision edge controls it at the unique root of \(1-3h+11h^2/2-29h^3/4\), approximately \(0.4891494251<1/2=H_3\).

## Assumptions and scope
The tree is finite, connected, simple, unweighted and has at least two vertices; the state obeys \(y'=-Ly\) and the classical four-stage RK4 endpoint update is used. The inequality is entrywise. No assertion is made about arbitrary graphs, weighted trees, intermediate Runge--Kutta stages, nonlinear flows, or independence of verification. The theorem applies to every nonnegative initial state, since matrix entrywise positivity is equivalent to invariance of the coordinate nonnegative cone for a linear endpoint map.

## Proof
Write \(A\) for adjacency and \(D\) for degree diagonal, so \(L=D-A\). The tree is bipartite. Products contributing to \(L^k_{uv}\) can be classified by the number of genuine edge moves and stationary degree factors. At distance greater than four, every term of \(K_T\) vanishes. At distance four, the unique four-edge walk gives \((K_T)_{uv}=h^4/24>0\).

For distance three, there is a unique path \(P=(u,x,y,v)\). Its only contributing terms up to degree four have three edge moves, with either no or one inserted degree factor. Thus
\[
(K_T)_{uv}=\frac{h^3}{6}\left(1-\frac{h}{4}\sum_{z\in P}d_z\right).
\]
This is nonnegative precisely through \(4/q(P)\) and strictly negative thereafter.

For distance two, let \(u,x,v\) be the unique connecting path. Put \(S=d_u+d_x+d_v\) and \(P_2=\sum_{0\le i\le j\le2}d_{v_i}d_{v_j}\) with \((v_0,v_1,v_2)=(u,x,v)\). The four-edge walk count \(W_4=(A^4)_{uv}\) is nonnegative. Direct expansion gives
\[
(K_T)_{uv}=\frac{h^2}{2}-\frac{Sh^3}{6}+\frac{(P_2+W_4)h^4}{24}.
\]
Since \(P_2=(S^2+d_u^2+d_x^2+d_v^2)/2\ge 2S^2/3\), the discriminant of the bracketed quadratic in \(h\) is strictly negative: \(S^2/36-(P_2+W_4)/12\le -S^2/36<0\). The distance-two entry is therefore strictly positive for all \(h>0\).

For an edge \(uv\), a closed walk of three edge moves from \(u\) to \(v\) must backtrack, so \((A^3)_{uv}=a+b-1\). Expanding powers of \(D-A\) shows
\[
L_{uv}=-1,\quad (L^2)_{uv}=-(a+b),\quad (L^3)_{uv}=-B_{uv},\quad(L^4)_{uv}=-C_{uv}.
\]
The one-edge/three-degree terms in \(-(L^4)_{uv}\) sum to \((a+b)(a^2+b^2)\); the three-edge/one-degree terms give the remainder \(2(a^2+ab+b^2)-2(a+b)+s_u+s_v\), which is nonnegative as a walk sum. Consequently \((K_T)_{uv}=h p_{uv}(h)\). Since \(a,b\ge1\),
\[
B_{uv}=(a+b)^2-(a-1)(b-1)\le(a+b)^2,
\qquad C_{uv}\ge(a+b)(a^2+b^2)\ge\frac{(a+b)^3}{2}.
\]
The derivative \(p'_{uv}(h)=-A_{uv}/2+B_{uv}h/3-C_{uv}h^2/8\) has discriminant
\[
\frac{B_{uv}^2}{9}-\frac{A_{uv}C_{uv}}4
\le (a+b)^4\left(\frac19-\frac18\right)<0.
\]
It is strictly negative for all real \(h\); thus \(p_{uv}\) decreases from one to negative infinity and has one positive root, being nonnegative exactly up to that root.

Finally, every eigenvalue of \(L\) is nonnegative. For all real \(z\ge0\),
\[
24R_4(-z)=(z^2-2z+2)^2+4((z-2)^2+1)>0.
\]
By the spectral theorem, \(K_T(h)\) is positive definite and every diagonal entry is strictly positive for all \(h\ge0\). These exhaust the possible vertex distances and prove the equivalence. The linear-time observation follows by precomputing all \(d_v\) and \(s_v\), then evaluating one cubic per edge and maximizing length-three path degree sums with the two largest neighbor degrees at each vertex (excluding the opposite endpoint of the central edge).

For the path on five vertices the largest length-three path degree sum is seven; direct edge cubics have positive roots above \(4/7\). For the indicated six-vertex subdivided star, the critical edge has \((A,B,C)=(6,33,174)\), giving the stated cubic; its root lies strictly between \(0.48\) and \(0.49\), while all other edge roots exceed \(0.5\). These witnesses show the two mechanisms are genuinely distinct.

## Verification
The standalone `verify.py` constructs graph Laplacian powers independently using exact integer matrix products, enumerates all labelled trees with at most six vertices and additional deterministically sampled trees up to 23 vertices, and checks every off-diagonal coefficient identity and elementary inequality. It reports `VERIFY_OK 1696 trees, 50631 exact unordered vertex-pair coefficient identities, tree-class inequalities, broom edge switch`. The proof above, not finite enumeration, establishes the theorem for every admissible tree. Run `python verify.py` using Python 3 standard library; no external packages or other files are required.

## Relationship to prior work
Gottlieb, Shu and Tadmor (2001) develop general strong-stability-preserving time-integration theory; Gottlieb and Gottlieb (2003) analyze linear constant-coefficient operators; Blanes, Iserles and Macnamara (2022) study positivity-preserving methods for Laplacian-structured flows. Their methods and scopes provide motivation, but the inspected materials do not state the exact arbitrary-tree local edge/distance-three classification above. Specialized analyses of particular tree families or lower-order RK formulas do not imply this all-tree theorem. The conclusion of no identified covering prior theorem is limited to the records and literature actually checked.

## Limitations
This is an exact theorem for linear *endpoint* positivity, not an SSP guarantee for intermediate stages or a graph-independent CFL bound. It does not cover edge weights, general bipartite graphs with cycles, directed networks, or nonlinear differential equations. Literature coverage is incomplete: an equivalent exact local characterization in uncatalogued or inaccessible specialized sources remains possible. Independent mathematical review has not been performed.

## References
1. S. Gottlieb, C.-W. Shu and E. Tadmor, "Strong Stability-Preserving High-Order Time Discretization Methods," *SIAM Review* **43** (2001), 89–112, DOI:10.1137/S003614450036757X; first electronically published 2001-02-02. Author-hosted full text: https://www.math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf.
2. S. Gottlieb and L.-A. J. Gottlieb, "Strong Stability Preserving Properties of Runge-Kutta Time Discretization Methods for Linear Constant Coefficient Operators," *Journal of Scientific Computing* **18** (2003), 83–109, DOI:10.1023/A:1020338228736. Public full-text transcription: https://www.researchgate.net/publication/220395769_Strong_Stability_Preserving_Properties_of_Runge-Kutta_Time_Discretization_Methods_for_Linear_Constant_Coefficient_Operators.
3. S. Blanes, A. Iserles and S. Macnamara, "Positivity-Preserving Methods for Ordinary Differential Equations," arXiv:2102.08242, version dated 2022-05-02, https://arxiv.org/pdf/2102.08242.
