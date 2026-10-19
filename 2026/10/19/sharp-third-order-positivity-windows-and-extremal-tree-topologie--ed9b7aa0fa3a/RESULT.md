# Sharp third-order positivity windows and extremal tree topologies

## Finding
For the classical explicit three-stage, third-order Runge–Kutta completed step applied to unit-rate graph diffusion on **any finite tree**, the exact largest timestep preserving every nonnegative initial vector admits a local, linear-time certificate. Among trees of any fixed maximum degree, the star alone maximizes this timestep; the usual forward-Euler sufficient bound is attained exactly when a length-two path consists of three maximum-degree vertices.

Specifically, let the connected tree \(T\) have \(|V(T)|\ge 3\) and maximum degree \(\Delta\ge2\). For each vertex \(v\), set \(d_v=\deg_T(v)\) and \(s_v=\sum_{w\sim v}d_w\), and let \(r_v\) be the unique positive root of
\[
p_v(h)=1-d_vh+\frac{d_v(d_v+1)}2h^2-\frac{d_v^3+2d_v^2+s_v}{6}h^3.
\]
Set \(B(T)=\max_{u\sim v\sim w,\,u\ne w}(d_u+d_v+d_w)\). With \(L_T\) the combinatorial Laplacian and
\[
P_T(h)=I-hL_T+\frac{h^2}{2}L_T^2-\frac{h^3}{6}L_T^3,
\]
one has the **exact equivalence**
\[
P_T(h)\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad
0\le h\le H(T):=\min\left\{\min_{v\in V(T)}r_v,\frac3{B(T)}\right\}.
\]
Moreover, \(H(T)\ge1/\Delta\), with equality precisely when some length-two path has all three degrees equal to \(\Delta\). Among all such trees with maximum degree \(\Delta\), the unique maximizer is \(K_{1,\Delta}\), for which \(H=\rho_\Delta\), the unique positive zero of
\[
1-\Delta h+\frac{\Delta(\Delta+1)}2h^2-
\frac{\Delta(\Delta+1)^2}{6}h^3.
\]
Every nonstar tree with the same maximum degree satisfies \(H(T)<\rho_\Delta\). The lower bound is attained for every \(\Delta\ge2\), by a tree formed from a degree-\(\Delta\) three-vertex path with leaves attached to fill the remaining degrees.

## Assumptions and scope
All graphs are finite, simple, connected, unweighted trees, with one unit diffusion rate per edge. The evolution is \(y'(t)=-L_Ty(t)\); nonnegativity is for the **completed** linear Runge–Kutta one-step map for **every** nonnegative initial vector, not for its internal stage values. Degrees and path lengths are ordinary unweighted graph notions. Step sizes are real and nonnegative. The claim excludes isolated vertices and the two-vertex tree, which can be handled separately. This result does not assert unconditional positivity on general graphs, weighted graphs, or arbitrary nonlinear dynamics.

## Proof
**1. Local matrix identities.** Write \(d=d_u\), \(e=d_v\), and \(s_u=\sum_{w\sim u}d_w\). On a tree, ordinary multiplication of \(L=D-A\) gives the following complete list, classified by graph distance:

- Distance zero: \((L^2)_{uu}=d^2+d\), \((L^3)_{uu}=d^3+2d^2+s_u\), so \(P_{uu}(h)=p_u(h)\).
- Adjacent distinct \(u,v\): \((L^2)_{uv}=-(d+e)\), and \((L^3)_{uv}=-(d^2+de+e^2+d+e-1)\). Therefore
\[
P_{uv}(h)=h\left[1-\frac{d+e}{2}h+\frac{d^2+de+e^2+d+e-1}{6}h^2\right].
\]
The bracket is strictly positive for every real \(h\). Indeed, writing \(M=d^2+de+e^2+d+e-1\), one has \(M\ge\frac34(d+e)^2+(d+e)-1>\frac34(d+e)^2\); hence its discriminant \((d+e)^2/4-2M/3\) is strictly negative.
- Distance two, with unique middle vertex \(v\): \((L^2)_{uw}=1\), \((L^3)_{uw}=d_u+d_v+d_w\), hence
\[
P_{uw}(h)=\frac{h^2}{6}\bigl[3-(d_u+d_v+d_w)h\bigr].
\]
- Distance three: \((L^2)_{uw}=0\), \((L^3)_{uw}=-1\), so \(P_{uw}(h)=h^3/6\).
- Distance at least four: \(P_{uw}(h)=0\).

These identities use the uniqueness of paths in trees. For instance, the distance-two cubic term is the sum of the three possible diagonal insertions along the unique two-edge path; the distance-three term is minus the unique three-edge walk.

**2. Exact threshold.** Since every vertex has at least one neighbor, \(s_v\ge d_v\), and
\[
p'_v(h)=-d_v+d_v(d_v+1)h-\frac{d_v^3+2d_v^2+s_v}{2}h^2
\le -d_v\left(1-(d_v+1)h+\frac{(d_v+1)^2h^2}{2}\right)<0
\]
for every \(h\ge0\). The final strict inequality follows from \(1-z+z^2/2>0\) for real \(z\). Thus \(p_v(0)=1\) decreases to minus infinity and has exactly one positive root \(r_v\). The formulas of step 1 show that the only sign-changing obstructions are a diagonal zero or a distance-two zero. Each becomes strictly negative above its own cutoff, proving the exact if-and-only-if formula and excluding any later regained positivity.

**3. The sharp universal bound and its equality case.** Put \(F(h)=I-hL_T\). For \(0\le h\le1/\Delta\), \(F(h)\ge0\) entrywise and
\[
P_T(h)=\frac13I+\frac12F(h)+\frac16F(h)^3\ge0.
\]
At \(h=1/\Delta\), all diagonals remain positive (at least \(1/3\)), all adjacent entries and distance-three entries are positive, and only distance-two entries can vanish. Their formula gives zero precisely for a three-vertex path with degrees \(\Delta,\Delta,\Delta\). If such a path exists its entry becomes negative immediately above \(1/\Delta\), proving equality. Otherwise every entry that is not identically zero is strictly positive at \(1/\Delta\), and finiteness and continuity give a strictly larger valid interval, proving strictness.

**4. Unique maximum at the star.** The star center has \(d=\Delta\), \(s=\Delta\), so its diagonal is precisely the polynomial defining \(\rho_\Delta\). The polynomial is strictly decreasing, and direct substitution shows
\[
p_{\mathrm{center}}\left(\frac3{\Delta+2}\right)
=-\frac{4\Delta^3+3\Delta^2-9\Delta-16}{2(\Delta+2)^3}<0
\]
for every integer \(\Delta\ge2\). Consequently \(\rho_\Delta<3/(\Delta+2)\), and at \(h=\rho_\Delta\) all leaf-to-leaf distance-two entries are nonnegative. The center diagonal is zero; by \(P_T(h){\bf1}={\bf1}\), each center–leaf entry equals \(1/\Delta\). The leaf diagonal is
\[
1-\frac1\Delta-(\Delta-1)c(h),\qquad
c(h)=\frac{h^2}{2}-\frac{\Delta+2}{6}h^3.
\]
Throughout \(0\le h\le3/(\Delta+2)\), one has \(0\le c(h)\le2/[3(\Delta+2)^2]<1/\Delta\), so every leaf diagonal is strictly positive. Thus \(P_{K_{1,\Delta}}(\rho_\Delta)\ge0\). The already proved exact-threshold formula implies the star cutoff is \(\rho_\Delta\).

For any other connected tree with the same maximum degree, choose a vertex \(v\) of degree \(\Delta\). If all its neighbors were leaves, the entire tree would be the star; hence at least one neighbor has degree at least two, so \(s_v>\Delta\). Its diagonal polynomial obeys
\[
p_v(\rho_\Delta)=p_{\mathrm{center}}(\rho_\Delta)
-\frac{(s_v-\Delta)\rho_\Delta^3}{6}<0.
\]
Consequently \(H(T)<\rho_\Delta\), establishing unique maximality. The explicitly constructed three-hub tree has a length-two path of full-degree vertices and proves sharpness of the lower bound.

**5. Computational size.** Compute degrees and neighbor-degree sums in linear time. At each vertex the two largest degrees among its neighbors determine the worst centered two-edge path; their maximum, including that center degree, gives \(B(T)\) in total linear work. Each unique positive cubic root can be approximated to a specified precision by monotone bisection. Hence the local certificate has linear graph-processing complexity (and one scalar root computation per vertex).

## Verification
The standalone `check_tree_coefficients.py` performs an exhaustive integer-arithmetic comparison of the displayed formulas against direct Laplacian powers \(L^2\) and \(L^3\) for **all 18,248 labelled trees of orders two through seven** (one, three, sixteen, 125, 1,296, and 16,807 respectively). It additionally evaluates the completed step at \(h=1/\Delta\), using an integer common denominator, checks all entries are nonnegative, and confirms that the distance-two zeros occur exactly at paths of three maximum-degree vertices. Finite checks supplement but do **not** prove the universal statement; the proof above supplies the arbitrary-tree argument. Symbolic substitution independently verifies the displayed star-root inequality.

## Relationship to prior work
Horváth (2005) provides general Runge–Kutta positivity-radius and sharp class-wise timestep results and discusses semidiscrete diffusion on a one-dimensional mesh; it does not identify the exact step window for every finite tree or the star/extremal degree-pattern classification. Gottlieb, Grant, and Higgs (2014) develop strong-stability-preserving Runge–Kutta analysis and distinguish generic method coefficients from problem-specific bounds; this work specializes to the completed cubic step on trees and proves the **sharp graph-dependent** bound. Horváth, Song, and Terlaky (2014) derive general polyhedral invariance step thresholds from polynomial inequalities, whereas the present theorem converts the particular graph problem into explicit local degrees, a complete classification of obstructions, and unique extremal topology. Related studies of fourth-order Runge–Kutta positivity on graphs of maximum degree two and Padé graph-step positivity concern different update polynomials and do not imply this all-tree third-order extremal theorem.

## Limitations
The formula applies only to the final third-order step on simple, unit-weight, undirected trees. Intermediate Runge–Kutta stages may obey different positivity conditions. Finite enumerations do not prove any universal statement; the exact algebra and inequalities above are needed. Numerical computation of cubic roots incurs approximation error; all defining inequalities and uniqueness statements are exact. Priority is assessed against the cited accessible primary material and targeted mathematical literature comparisons, not independently audited or guaranteed against every inaccessible, unpublished, or unindexed source.

## References
1. Z. Horváth, “On the positivity step size threshold of Runge–Kutta methods,” *Applied Numerical Mathematics* 53 (2005), 341–356. First available online 27 October 2004. DOI: https://doi.org/10.1016/j.apnum.2004.08.026.
2. S. Gottlieb, Z. Grant, and D. Higgs, “Optimal explicit strong stability preserving Runge–Kutta methods with high linear order and optimal nonlinear order,” arXiv:1403.6519 (initially posted 25 March 2014). https://arxiv.org/abs/1403.6519.
3. Z. Horváth, Y. Song, and T. Terlaky, “Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron,” arXiv:1406.6755 (initially posted June 2014). https://arxiv.org/abs/1406.6755.
4. S. Blanes, A. Iserles, and S. Macnamara, “Positivity-preserving methods for population models,” arXiv:2102.08242 (2021), broader context concerning graph-Laplacian positivity and order barriers. https://arxiv.org/abs/2102.08242.
