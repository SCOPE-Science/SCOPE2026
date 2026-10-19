# Exact heterogeneous-price conductance allocation on triangular bouquets

## Finding

Consider a **triangular bouquet** (friendship graph) consisting of \(m\ge2\) triangles sharing just one common vertex \(o\). Its number of vertices is \(N=2m+1\). The two spokes in petal \(i\) each have unit price per unit conductance; its edge joining the two noncentral vertices has independent price \(t_i>0\). Every edge conductance is an independently selectable nonnegative real number. Fix an exact expenditure budget \(B>0\), and minimize the sum of effective resistances over unordered pairs of distinct vertices; a disconnected design has infinite objective.

Define the common price boundary
\[
T_m=\frac{2N}{N-1}=2+\frac1m,
\]
and, for every petal \(i\),
\[
r_i=\begin{cases}
\frac12\left(\sqrt{\frac{N(4-t_i)}{(N-2)t_i}}-1\right),&0<t_i<T_m,\\
0,&t_i\ge T_m,
\end{cases}
\]
\[
G_i=\begin{cases}
2(N-2)+t_i+\sqrt{N(N-2)t_i(4-t_i)},&0<t_i<T_m,\\
4(N-1),&t_i\ge T_m.
\end{cases}
\qquad S=\sum_{j=1}^{m}\sqrt{G_j}.
\]

**Theorem.** The global minimizer is unique. In petal \(i\), both spokes have conductance
\[
a_i=\frac{B\sqrt{G_i}}{S(2+t_i r_i)},\]
and its noncentral edge has conductance \(c_i=r_i a_i\). The exact minimum total effective resistance is
\[
\boxed{\mathcal K_{\min}=\frac{S^2}{B}.}
\]
An edge joining the two noncentral vertices is present if and only if \(t_i<T_m\), independently of every other petal's price. The optimum spends
\[
z_i=2a_i+t_i c_i=\frac{B\sqrt{G_i}}S
\]
on petal \(i\). Consequently \(t_i<t_j<T_m\) implies \(z_i<z_j\), while prices at or above \(T_m\) have the same \(G_i=4(N-1)\). Hence the minimum admits all \(2^m\) possible sets of retained noncentral edges as prices vary, without any budget-dependent phase boundaries.

## Assumptions and scope

The graph is simple, finite, undirected, and exactly \(m\) triangles meeting in one common vertex, with no other edges. The cost is \(\sum_{i=1}^{m}(a_i^{(u)}+a_i^{(v)}+t_i c_i)=B\), with \(B>0\), \(t_i>0\), and conductances nonnegative. Zero conductance means that the corresponding allowed edge is omitted. Effective resistance is computed using the positive-conductance network. No symmetry of the decision variables is assumed. The theorem concerns the full Kirchhoff index, not a resistance to a single designated vertex. The formula for \(r_i\) uses \(4-t_i>0\) only on \(0<t_i<T_m\), where \(T_m<4\).

## Proof

**1. Exact resistance decomposition without symmetry.** In petal \(i\), write \(p_i,q_i\) for its independently chosen spoke conductances and \(c_i\) for its noncentral-edge conductance, and set
\[
\Delta_i=p_iq_i+p_ic_i+q_ic_i.
\]
Because the common vertex \(o\) is a cut vertex, currents between vertices of distinct petals travel through \(o\), and adding other petals does not change resistance within one triangle. The triangle's exact resistances are
\[
R(o,u_i)=\frac{q_i+c_i}{\Delta_i},\qquad
R(o,v_i)=\frac{p_i+c_i}{\Delta_i},\qquad
R(u_i,v_i)=\frac{p_i+q_i}{\Delta_i}.
\]
In the all-pairs sum, each of the first two rooted resistances is counted \(N-2\) times: once for its pair with \(o\), and once for each of the \(N-3\) vertices outside its own triangle. The resistance between the two leaf vertices is counted once. Hence, exactly,
\[
\mathcal K=\sum_{i=1}^{m}
\frac{(N-1)(p_i+q_i)+2(N-2)c_i}
{p_iq_i+p_ic_i+q_ic_i}.\tag{1}
\]
This identity holds for every connected feasible allocation, including allocations with a missing edge in a triangle, interpreted by continuity.

**2. Unrestricted uniqueness and petal symmetry.** For a connected weighted graph let \(L\) be its Laplacian and \(J=\mathbf1\mathbf1^{\mathsf T}/N\). Then
\[
\mathcal K=N\bigl(\operatorname{tr}(L+J)^{-1}-1\bigr).
\]
On positive-definite symmetric matrices, \(X\mapsto\operatorname{tr}(X^{-1})\) is strictly convex: for every nonzero symmetric \(H\), its second directional derivative is
\[
2\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})>0.
\]
The map from edge conductances to \(L\) is injective because each simple edge has a unique off-diagonal Laplacian entry. Thus the objective is strictly convex on the connected feasible domain. The finite-budget feasible simplex is compact; approaching disconnection sends the objective to infinity. The optimum therefore exists and is unique. Swapping the two noncentral vertices of any one triangle preserves both the objective and its edge prices. Unique optimality forces its two spoke weights to coincide: \(p_i=q_i=a_i>0\). The positivity follows because both spokes vanishing would disconnect that petal.

**3. Exact local shape optimization.** Set \(c_i=r a_i\) with \(r\ge0\) and let its expenditure be \(z_i=a_i(2+t_i r)>0\). Formula (1) becomes
\[
\mathcal K=\sum_i\frac{F_{t_i}(r_i)}{z_i},\qquad
F_t(r)=\frac{(2+tr)[2(N-1)+2(N-2)r]}{1+2r}.
\]
Direct differentiation gives
\[
(1+2r)^2 F'_t(r)
=2(N-1)t-4N+4t(N-2)(r+r^2).\tag{2}
\]
The right-hand side increases strictly with \(r\ge0\). If \(t\ge T_m=2N/(N-1)\), the unique minimum is \(r=0\), with \(F_t(0)=4(N-1)\). If \(0<t<T_m\), the right-hand side is initially negative and has a unique positive zero; solving its quadratic gives
\[
r=\tfrac12\left(\sqrt{N(4-t)/[(N-2)t]}-1\right).
\]
Substitution into \(F_t\), using \((1+2r)^2=N(4-t)/[(N-2)t]\), yields
\[
\min_{r\ge0}F_t(r)=2(N-2)+t+\sqrt{N(N-2)t(4-t)}=G(t).
\]
At \(t=T_m\) the two formulas agree; equation (2) still has exactly one minimizer \(r=0\). Thus all equality cases are covered.

**4. Optimal budget distribution.** The remaining problem is to minimize \(\sum_iG_i/z_i\) over \(z_i>0\) with \(\sum_i z_i=B\). Cauchy–Schwarz gives
\[
\sum_i\frac{G_i}{z_i}\ge\frac{(\sum_i\sqrt{G_i})^2}{\sum_i z_i}=\frac{S^2}{B},
\]
with equality uniquely when \(z_i=B\sqrt{G_i}/S\). Substituting into \(a_i=z_i/(2+t_i r_i)\) and \(c_i=r_i a_i\) proves the theorem.

**5. Compensatory allocation.** For \(0<t_1<t_2<T_m\), evaluate the local function at the positive minimizer for \(t_2\). Because \(F_t(r)\) strictly increases in \(t\) for fixed \(r>0\), one obtains \(G(t_1)<G(t_2)\). For \(t\ge T_m\), \(G\) is constant. Therefore petals with more expensive noncentral edges receive weakly greater total optimal expenditure, and strictly greater expenditure whenever the lower price is in the active-edge region. Since each \(c_i>0\) precisely when \(t_i<T_m\), all \(2^m\) retention patterns occur.

## Verification

The standalone \`verify.py\` can be run with Python 3, NumPy, SciPy, and SymPy. It reconstructs the full weighted Laplacian from independent spoke and noncentral-edge weights, compares matrix-inverse Kirchhoff indices to (1), checks exact rational identities, verifies derivative and reduction formulas, tests boundary cases, and checks the claimed optimum against nonsymmetric feasible allocations and numerical constrained optimization. In the reported run it passed **549** checks. Exact symbolic identities and the complete proof above, not finite experiments, establish the unbounded family.

## Relationship to prior work

Ghosh, Boyd, and Saberi (2006/2008) established strict-convexity and general optimality principles for minimum-total-effective-resistance conductance allocation, and analyzed trees, wheels and barbell graphs. Their examples and general framework do not state the present heterogeneous-price triangular-bouquet allocation law. Sardar and Xu (first available online 2024; journal 2025) studied resistance and Kirchhoff indices of windmill graphs with each edge replaced by a unit resistor; that unit-weight evaluation does not itself select independent budgeted conductances. Bhoite and coauthors (2026) treat heterogeneous edge costs in a mixed-integer augmentation model with fixed pre-existing weights and numerical relaxations, not a closed-form optimization of all bouquet weights.

General optimality conditions for a tree with optional chords also recover the *high-price edge-deletion condition* for a star with the triangle-closing edges as optional chords; this boundary by itself is not asserted as a new independent theorem. What is characterized here in addition is **every mixed-price optimal conductance, interpetal budget share, exact objective value, and complete independence of the individual phase changes**. A direct keyword search is not a proof of bibliographic novelty.

## Limitations

The theorem applies only to triangular bouquets with a common vertex, unit spoke prices within each petal, and one variable noncentral-edge price per petal. It does not cover arbitrary cactus graphs, arbitrary unequal prices between the two spokes, directed networks, or alternative diffusion objectives. The strict-convexity argument establishes unique optimal conductances under these assumptions, not uniqueness of a topology among all possible underlying graphs. Sardar and Xu's full paper was not accessible for inspection; its available abstract explicitly assumes one-ohm edges, but an uninspected ancillary comparison remains a bibliographic risk. Equivalent unindexed specialized results or a worked-out consequence in other literature remain possible. There is no independent scientific validation of the present package.

## References

1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, Mathematical Theory of Networks and Systems, Kyoto, July 2006; expanded *SIAM Review* 50 (2008), 37–66. https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf ; https://web.stanford.edu/~boyd/papers/eff_res.html
2. M. S. Sardar and S.-J. Xu, *Resistance Distance and Kirchhoff Index in Windmill Graphs*, *Current Organic Synthesis* 22 (2025), 159–168, DOI:10.2174/0115701794299562240606054510. https://pubmed.ncbi.nlm.nih.gov/39962956/
3. O. Bhoite, V. S. Dhuli, S. Werner, K. Kansanen, *Budget-Constrained Graph Augmentation for Robust Network Design via Kirchhoff Index Minimization*, arXiv:2609.29790 (2026). https://arxiv.org/pdf/2609.29790
