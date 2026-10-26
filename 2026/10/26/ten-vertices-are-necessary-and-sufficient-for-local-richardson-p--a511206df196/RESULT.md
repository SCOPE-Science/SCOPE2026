# Ten vertices are necessary and sufficient for local Richardson positivity failure at graph diameter three

## Finding
Let \(G\) be a finite connected, simple, **unweighted** graph on \(n\ge2\) vertices, with combinatorial Laplacian \(L=D-A\). Consider the completed, standard two-level Richardson extrapolate of backward Euler for \(y'=-Ly\):
\[
T_G(h)=2(I+hL/2)^{-2}-(I+hL)^{-1},\qquad h\ge0.
\]
Call the update *locally positive* if there is an \(\varepsilon>0\) such that every entry of \(T_G(h)\) is strictly positive whenever \(0<h<\varepsilon\).

**Sharp graph-order cutoff.** Every such graph with diameter at most \(3\) and at most \(9\) vertices has a locally positive extrapolated update. There is a connected simple unweighted **10-vertex graph of diameter exactly \(3\)** whose extrapolated update has a negative off-diagonal entry for all sufficiently small positive \(h\). Thus \(10\) is the minimum graph order for this kind of diameter-three local-positivity failure.

The underlying combinatorial statement is sharp on both sides of the cutoff. For any vertices \(u,v\) at distance exactly \(3\),
\[
|V(G)|\le9\quad\Longrightarrow\quad (L^4)_{uv}\le-1,
\qquad
|V(G)|\le10\quad\Longrightarrow\quad (L^4)_{uv}\le4.
\]
Both inequalities admit equality on connected, simple, unweighted graphs of diameter \(3\). In the ten-vertex equality example, the extrapolated entry is
\[
(T_G(h))_{uv}=-\frac32h^4+O(h^5)\quad(h\downarrow0).
\]
All statements concern *sufficiently small* time steps, not positivity at every time step.

## Assumptions and scope
The graph is undirected, finite, connected, loopless, and has no multiple edges. Every edge has conductance \(1\); this restriction matters to the order cutoff. The Laplacian is the ordinary unnormalized matrix \(L=D-A\), not a normalized or mass-matrix Laplacian. Matrix powers and inverses are taken in exact real arithmetic. The time-step parameter \(h\) is nonnegative. We make no claim that the cutoff holds for arbitrary positive edge weights or for refinement factors other than \(2\).

At graph distance \(1\), the off-diagonal update has a positive linear leading term; at distance \(2\), a positive quadratic leading term. At distance \(3\), the cubic coefficient cancels under this extrapolation and the sign is decided by a fourth Laplacian power. At distance at least \(4\), there are other small-step sign obstructions; restricting to diameter at most \(3\) isolates the first nontrivial size-dependent one.

## Proof
### 1. The decisive Taylor coefficient
The scalar stability function is
\[
R_2(z)=2(1+z/2)^{-2}-(1+z)^{-1}
=1-z+\frac12z^2+0z^3-\frac38z^4+O(z^5).
\]
Because \(G\) is finite, substitution of \(z=hL\) is legitimate for sufficiently small \(h\):
\[
T_G(h)=I-hL+\frac12h^2L^2-\frac38h^4L^4+O(h^5).
\]
For different vertices \(u,v\), the leading off-diagonal term is positive if their distance is \(1\) or \(2\). For distance exactly \(3\), \(L_{uv}=(L^2)_{uv}=0\), so
\[
(T_G(h))_{uv}=-\frac38(L^4)_{uv}h^4+O(h^5).
\]
The diagonal entries tend to \(1\) as \(h\downarrow0\). It therefore suffices to bound \((L^4)_{uv}\) at distance \(3\).

### 2. Exact fourth-power identity
Fix \(u,v\) at distance \(3\). Write \(U=N(u)\), \(V=N(v)\), and \(W=V(G)\setminus(\{u,v\}\cup U\cup V)\). These sets are disjoint, and \(a=|U|\ge1\), \(b=|V|\ge1\), \(c=|W|\ge0\) satisfy \(a+b+c=n-2\). Let \(t\ge1\) be the number of edges between \(U\) and \(V\). For \(i\in U\), put \(p_i=|N(i)\cap V|\); for \(j\in V\), put \(q_j=|N(j)\cap U|\). For \(w\in W\), put \(x_w=|N(w)\cap U|\) and \(y_w=|N(w)\cap V|\).

There is no walk of fewer than three edges from \(u\) to \(v\). Expanding \(L^4=(D-A)^4\), the only contributing words have either four adjacency factors or three adjacency factors and one degree factor. The former count four-edge walks; the latter count each three-edge path \(u-i-j-v\) with weight \(d_u+d_i+d_j+d_v\). Thus
\[
(L^4)_{uv}=(A^4)_{uv}-\sum_{\substack{i\in U,j\in V\\ij\in E}}(d_u+d_i+d_j+d_v).
\]
Expanding the four-edge walk count through its midpoint and cancelling contributions from edges within \(U\) and within \(V\) yields the exact identity
\[
\begin{aligned}
(L^4)_{uv}={}&-(a+b+2)t-\sum_{i\in U}p_i^2-\sum_{j\in V}q_j^2\\
&+\sum_{w\in W}\left(x_wy_w-\sum_{i\in U\cap N(w)}p_i-\sum_{j\in V\cap N(w)}q_j\right).
\end{aligned}
\]
This identity is valid regardless of the other edges of \(G\).

### 3. Reduction to one connecting edge
Consider removing an edge between \(U\) and \(V\) while keeping all other edges fixed, provided at least one such edge remains. Then \(t\) decreases, one \(p_i\) and one \(q_j\) decrease, and every term of the displayed identity either increases or stays unchanged. In particular \((L^4)_{uv}\) **strictly increases**. Thus the maximum for fixed \(U,V,W\) and fixed nonconnecting edges is bounded above by the case with only one remaining cross edge, say \(i_0j_0\). In that case \(t=1\), the only nonzero \(p_i\) and \(q_j\) are \(p_{i_0}=q_{j_0}=1\), and
\[
(L^4)_{uv}=-(a+b+4)+\sum_{w\in W}\left(x_wy_w-\mathbf1_{i_0\in N(w)}-\mathbf1_{j_0\in N(w)}\right).
\]
For each \(w\), independently of other neighbors, the parenthesis is at most
\[
F(a,b)=\max\{0,ab-2\}.
\]
To see this, if both distinguished bridge endpoints are neighbors, the bound is \(ab-2\); if neither is, at most \((a-1)(b-1)\); if exactly one is, at most \(a(b-1)-1\) or \((a-1)b-1\). Each is bounded by \(\max\{0,ab-2\}\); choosing no such neighbors or all \(a+b\) neighbors attains the maximum. Therefore
\[
(L^4)_{uv}\le c\max\{0,ab-2\}-(a+b+4).
\]
Write \(s=a+b\). Since \(ab\le\lfloor s^2/4\rfloor\), and \(c=n-2-s\),
\[
\boxed{(L^4)_{uv}\le(n-2-s)\max\{0,\lfloor s^2/4\rfloor-2\}-(s+4),\quad 2\le s\le n-2.}
\]

### 4. Exact finite order bounds
For \(n\le9\), the right-hand side is bounded by the case \(n=9\), because its first factor is nonnegative. Evaluating the six possible values \(s=2,3,4,5,6,7\) at \(n=9\) gives, respectively,
\[
-6,\ -7,\ -2,\ -1,\ -3,\ -11.
\]
Hence \((L^4)_{uv}\le-1\). At \(n=10\), the seven possible values \(s=2,\ldots,8\) give
\[
-6,\ -7,\ 0,\ 3,\ 4,\ -1,\ -12.
\]
Hence \((L^4)_{uv}\le4\). These are complete short integer evaluations of an analytic upper bound, not sampling over graphs.

To attain equality at ten vertices, take distinct vertices \(u,v\), three vertices \(U=\{a,a_1,a_2\}\), three vertices \(V=\{b,b_1,b_2\}\), and two vertices \(W=\{w_1,w_2\}\). Join \(u\) to every member of \(U\), \(v\) to every member of \(V\), join \(a\) to \(b\), and join each \(w_i\) to all six vertices in \(U\cup V\). There are no other edges. This graph is connected and has diameter exactly \(3\): the only distance-three pair requiring the bridge is \(u,v\); every other pair has distance at most \(3\). For \(u,v\), the identity gives
\[
(L^4)_{uv}=2(3\cdot3-2)-(3+3+4)=4.
\]
Replacing the three-element set \(U\) by a two-element set in the same construction gives a nine-vertex diameter-three graph with \((L^4)_{uv}=2(2\cdot3-2)-(2+3+4)=-1\), establishing sharpness of the nine-vertex bound.

Finally the Taylor expansion makes \((T_G(h))_{uv}=-3h^4/2+O(h^5)<0\) in the ten-vertex graph. For every graph with at most nine vertices and diameter at most three, all off-diagonal leading coefficients are strictly positive, and every diagonal tends to one; finiteness yields a common positive interval \((0,\varepsilon)\) for the whole matrix. This completes the proof.

## Verification
Run `python verify.py` using a standard Python interpreter. The program constructs the specified ten-vertex graph, verifies its diameter and the exact integer identity \((L^4)_{uv}=4\), and checks the complete sharp upper-bound lists for nine and ten vertices. It computes the extrapolated matrix with exact rational Gaussian elimination at four positive step sizes \(h=1/75,1/100,1/200,1/1000\); the witness entry is strictly negative in all four cases. It also reconstructs \((L^4)_{uv}\) both from matrix multiplication and from the exact combinatorial identity on 2,499 randomly generated distance-three vertex pairs of graphs on four through twelve vertices (fixed random seed), including size-dependent bounds where applicable. The analytic proof, not random testing, establishes the universal statement.

## Relationship to prior work
Lawson and Morris's 1977 Waterloo technical report, Section 2, equations (2.1)–(2.6), gives exactly this two-level extrapolation of the fully implicit method. Its page 9 also observes the classical negative **scalar** amplification beyond \(2(1+\sqrt2)\). Constantinescu and Sandu's July 2008 technical report, Section 2, supplies the general extrapolation tableau and studies order and stability. These are prior constructions; neither inspected report establishes a graph-order lower bound for local matrix-entry positivity or the exact fourth-Laplacian pairwise bound here.

A public investigation titled *Richardson acceleration creates a sharp positivity barrier for backward Euler* also proves a scalar positivity cutoff for every refinement factor. That scalar statement neither determines the signs of graph-distance-three transition entries nor implies the sharp order-ten graph classification. A related higher-dimensional counterexample exists; the new result proves the missing **minimum** size and the size-nine universal protection instead of just supplying a different witness.

## Limitations
The cutoff applies only to finite connected **simple unweighted** graphs with diameter at most three, and only to the standard two-substep extrapolation and sufficiently small positive time steps. It is not a universal all-time-step monotonicity theorem. A weighted graph, directed generator, longer graph diameter, different refinement factor, or nonlinear system can have a different obstruction. The random reproducibility checks are not exhaustive graph enumeration and are not part of the infinite proof. Existing extrapolation literature is large; an equivalent graph-specific minimality bound outside the inspected literature cannot be ruled out by database searches alone.

## References
1. J. D. Lawson and J. Ll. Morris, *The Extrapolation of First Order Methods for Parabolic Partial Differential Equations I*, University of Waterloo Research Report CS-77-20 (July 1977), Section 2, https://cs.uwaterloo.ca/research/tr/1977/CS-77-20.pdf; later SIAM Journal on Numerical Analysis 15 (1978), 1212–1224, DOI 10.1137/0715082.
2. Emil M. Constantinescu and Adrian Sandu, *Achieving Very High Order for Implicit Explicit Time Stepping: Extrapolation Methods*, Virginia Tech Technical Report TR-08-13 (July 18, 2008), https://eprints.cs.vt.edu/archive/00001037/01/ExImex.pdf; journal version *Extrapolated Implicit-Explicit Time Stepping*, SIAM Journal on Scientific Computing 31 (2010), 4452–4477, DOI 10.1137/080732833.
3. *Richardson acceleration creates a sharp positivity barrier for backward Euler* (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-richardson-acceleration-creates-a-sharp-positivity-barrier-for-b--c9c2b9f6d7e1.
