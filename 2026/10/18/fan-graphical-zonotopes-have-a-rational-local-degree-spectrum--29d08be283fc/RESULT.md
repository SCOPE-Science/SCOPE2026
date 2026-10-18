# Fan graphical zonotopes have a rational local-degree spectrum

## Finding
For each integer \(m\ge 1\), let \(F_m=K_1\vee P_m\) be the fan graph with hub \(0\) and path vertices \(1,\ldots,m\), and let
\[
Z_m=\sum_{\{i,j\}\in E(F_m)}[0,e_i-e_j]
\subset\{(t_0,\ldots,t_m)\in\mathbb R^{m+1}:\textstyle\sum_i t_i=0\}
\]
be its graphical zonotope. Its normal fan defines a normal projective toric variety \(X_m\) over any algebraically closed field. For a torus-fixed point \(p\), let \(d(p)\) be the number of torus-invariant irreducible curves through \(p\), equivalently the number of edges of \(Z_m\) through its corresponding vertex, and define the **edge excess** \(\delta(p)=d(p)-m\).

The **entire** edge-excess distribution, as \(m\) varies, is
\[
\boxed{\displaystyle\sum_{m\ge1}z^m\sum_{p\in X_m^T}u^{\delta(p)}
=\frac{2z}{1-3z+(1-u)z^2}.}
\]
In particular, the number of smooth torus-fixed points is \(2F_{2m}\), where \(F_0=0,F_1=1\) and \(F_{j+2}=F_{j+1}+F_j\). There are \(2\cdot3^{m-1}\) fixed points altogether. For \(m\ge3\), the mean and variance of \(\delta\) over uniformly selected torus-fixed points are respectively \((m-2)/9\) and \((6m-10)/81\). The proportion of smooth fixed points therefore decays exponentially, at rate \(((3+\sqrt5)/2)/3\) to the power \(m\), up to a positive constant.

For illustration the coefficient polynomials \(Q_m(u)=\sum_p u^{\delta(p)}\) are \(Q_3=16+2u\), \(Q_4=42+12u\), \(Q_5=110+50u+2u^2\), \(Q_6=288+180u+18u^2\), and \(Q_7=754+600u+102u^2+2u^3\). For every \(m\), the maximum edge excess is \(\lfloor(m-1)/2\rfloor\). The conclusions are characteristic-independent.

## Assumptions and scope
The lattice of the zonotope is the root lattice \(M=\{(a_0,\ldots,a_m)\in\mathbb Z^{m+1}:\sum_i a_i=0\}\), with dual \(N=\mathbb Z^{m+1}/\mathbb Z(1,\ldots,1)\). All cones are in \(N_\mathbb R\); no alternative face-fan convention is used. The sum of segments may have either orientation without changing the normal fan. Invariant curves are one-dimensional torus-orbit closures. The excess is a **degree/simplicity defect** and is **not asserted to equal the local divisor-class-group rank**. The result counts torus-fixed points and their incident invariant curves; it does not classify all positive-dimensional singular strata. No characteristic-zero hypothesis is needed.

## Proof
**1. Acyclic orientations and degree.** Maximal cones of the graphical-arrangement normal fan are in bijection with acyclic orientations of \(F_m\). The cone for an orientation is cut out by the directed-edge inequalities \(x_i\le x_j\). Its irredundant facets correspond precisely to covering relations in the transitive-closure partial order (equivalently, to directed edges with no alternate directed path). Since a facet of a vertex normal cone is dual to an edge of the zonotope at that vertex, \(d(p)\) equals the number of Hasse covers. This correspondence is described in Postnikov–Reiner–Williams, Proposition 3.5(8) and the proof of Proposition 5.2.

**2. Run decomposition.** Classify each path vertex as \(A\) if its spoke is directed toward the hub and \(B\) if its spoke is directed away from the hub. An adjacent path edge between \(A\) and \(B\) must point from \(A\) to \(B\), since the opposite direction would complete a directed triangle with the hub. Conversely, choosing any \(A/B\) word and orienting the path edges within each maximal constant run arbitrarily yields an acyclic orientation: a path starting from a \(B\) vertex cannot enter an \(A\) vertex, so no directed cycle through the hub exists, and the path alone is acyclic.

Write the constant-run lengths \(L_1,\ldots,L_r\), so \(\sum_j L_j=m\). Internal edges of every run are Hasse covers: any alternate path would have to leave and re-enter that run, which is impossible because each boundary edge goes from \(A\) to \(B\) and spokes are one-way. Each boundary edge is not a cover, owing to its alternate two-spoke path through the hub. Within an \(A\)-run, the spokes that remain covers are precisely the spokes at **sinks of the oriented path**; a nonsink reaches another path vertex that has its own spoke to the hub. Within a \(B\)-run the surviving spokes are precisely those at **sources**, by reversing all arrows. If \(s_j\) is this number for run \(j\), then
\[
d(p)=\sum_{j=1}^{r}(L_j-1+s_j)
=m+\sum_{j=1}^{r}(s_j-1),\qquad
\delta(p)=\sum_{j=1}^{r}(s_j-1).
\]

**3. Exact run enumeration.** An oriented path on \(L\) vertices has exactly \(\binom{L}{2s-1}\) orientations with \(s\) sinks. Indeed, encode each of its \(L-1\) directed edges by a plus sign for rightward and a minus sign for leftward, and adjoin an initial plus sign and final minus sign. Each transition from plus to minus corresponds to precisely one sink (including endpoints). If there are \(s\) such transitions, there are \(s-1\) transitions in the other direction, making \(2s-1\) sign changes among \(L\) adjacent pairs; choosing their positions uniquely fixes all signs. The same distribution holds for sources by reversing arrows. Thus the excess polynomial of a single run has generating series
\[
T(z,u)=\sum_{L\ge1}z^L\sum_{s\ge1}\binom L{2s-1}u^{s-1}
=\sum_{s\ge1}u^{s-1}\frac{z^{2s-1}}{(1-z)^{2s}}
=\frac{z}{(1-z)^2-uz^2}.
\]
Any composition of \(m\) into run lengths occurs in exactly two \(A/B\) words (choice of the first letter), with independent internal orientations. Therefore
\[
\sum_{m\ge1}Q_m(u)z^m
=2\sum_{r\ge1}T(z,u)^r
=\frac{2z}{1-3z+(1-u)z^2},
\]
which proves the principal formula. It also gives \(Q_1(u)=2\), \(Q_2(u)=6\), and \(Q_m(u)=3Q_{m-1}(u)-(1-u)Q_{m-2}(u)\) for \(m\ge3\).

**4. Smoothness and numerical consequences.** Every run has at least one sink or source, so \(\delta\ge0\). A torus-fixed point is smooth only if its full-dimensional normal cone is simplicial, which requires exactly \(m\) facets, hence \(\delta=0\). Conversely, if \(\delta=0\), the \(m\) Hasse covers form a spanning tree on the \(m+1\) graph vertices. Their primitive edge-difference normals are an integral basis of \(M\): deletion of one row of the oriented tree-incidence matrix has determinant \(\pm1\), inductively by stripping leaves. The maximal normal cone is therefore unimodular, so the toric point is smooth in any characteristic. Setting \(u=0\) produces \(2z/(1-3z+z^2)\), whose \(z^m\) coefficient is \(2F_{2m}\). Setting \(u=1\) produces \(2z/(1-3z)\) and \(2\cdot3^{m-1}\) total orientations. Differentiating in \(u\) once and twice, then dividing by the total coefficient, yields the stated mean and variance for \(m\ge3\). The maximal degree of \(Q_m\) in \(u\) follows either from the recurrence with its positive run interpretation or from \(2s-1\le L\), giving \(\lfloor(m-1)/2\rfloor\); alternating sign sequences attain this bound.

## Verification
The standalone `check_fan.py` uses exhaustive enumeration of **all** orientations of the \(2m-1\) edges of \(F_m\) for each \(1\le m\le8\), rejecting cyclic orientations by topological sorting, computing each cover by deletion-and-reachability, and comparing the resulting degree-excess histogram against the rational-function recurrence. It separately enumerates oriented paths of lengths \(1\) through \(10\) and checks the binomial sink-count identity. For \(1\le m\le7\), it also checks the total zonotope edge count by an independent contraction identity, \(f_1(Z_m)=\sum_{e\in E(F_m)}a(F_m/e)\), against half the weighted sum of the computed vertex degrees. Every check passed with output `VERIFY_OK`. These finite checks support the symbolic all-parameter argument, not replace it.

## Relationship to prior work
Postnikov, Reiner and Williams, *Faces of Generalized Permutohedra* (first publicly posted 2006), prove the general Hasse-poset/facet and tree/simplicial criteria; their Proposition 5.2 addresses which **entire graphical zonotopes** are simple. The present formula refines this general criterion in a natural nonsimple family: it gives the exact number of vertices of **every degree**, hence the full fixed-point smoothness distribution. Grujić, *Counting Faces of Graphical Zonotopes* (first publicly posted 2016), obtains the global face polynomial by a chromatic-symmetric-function specialization and works out cycles and block products, not this fan-graph local-degree spectrum. The fan-graph entry in Forcey's Hedra Zoo records total vertex and facet numbers, but no vertex-degree distribution. The numerical Fibonacci sequence alone is not a claim of novelty; its interpretation as the smooth-fixed-point count together with the full degree distribution is the contribution.

## Limitations
The term *degree* means degree in the zonotope's one-skeleton, not algebraic degree of a subvariety. The edge excess is the number of incident invariant curves **minus the toric dimension**, not a local divisor-class-group rank, Hilbert–Samuel multiplicity, tangent-space dimension, or number of extremal rays of a normal cone. The theorem neither classifies the entire singular locus nor establishes uniqueness against all unindexed historical mathematical sources. The originality comparison is bounded by inspected literature and search coverage.

## References
1. A. Postnikov, V. Reiner, L. Williams, *Faces of Generalized Permutohedra*, arXiv:math/0609184 (first posted 2006-09-06), especially Proposition 3.5, Section 5 and Proposition 5.2. https://arxiv.org/abs/math/0609184
2. V. Grujić, *Counting Faces of Graphical Zonotopes*, arXiv:1604.06931 (first posted 2016-04-23), Theorem 1.1 and Section 5. https://arxiv.org/abs/1604.06931
3. S. Forcey, *Hedra Zoo: Acyclotope (fan graph)*, total fan-graph zonotope vertex/facet enumeration. https://sforcey.github.io/sf34/hedra/fanacyc.htm
