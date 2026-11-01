# Young-subgroup fixed spheres across the Johnson-graph Rips filtration

## Finding

Let \(k\ge1\), and let \(J(2k,k)\) be the Johnson graph on the \(k\)-element subsets of a fixed set \(A\sqcup B\), where \(|A|=|B|=k\). Its shortest-path metric is \(d(U,V)=k-|U\cap V|\). Let \(G=\mathfrak S_A\times\mathfrak S_B\) act by independently permuting the two blocks. For each real scale \(r\ge0\), let \(X_k(r)=\operatorname{VR}_{\le r}(J(2k,k))\), with simplices the sets of Johnson vertices of pairwise distance at most \(r\).

**Theorem.** For every integer \(0\le r<k\), the **geometric** fixed-point space is homotopy equivalent to exactly one sphere:

\[
\boxed{\ |X_k(r)|^G\simeq S^{\left\lfloor\frac{r}{2(k-r)}\right\rfloor}.\ }
\]

At \(r\ge k\) the fixed-point space is a simplex, hence contractible. At nonintegral scales, the complex equals that at the floor of the scale. More precisely, for integers \(0\le r<k\), put \(t=k-r\) and \(m=\lfloor r/2\rfloor+1\). Then \(|X_k(r)|^G\) is piecewise-linearly homeomorphic to the independence complex of the bipartite **band graph** \(F_{m,t}\), with vertices \(L_0,\ldots,L_{m-1},H_0,\ldots,H_{m-1}\) and precisely the edges \(L_iH_j\) for \(|i-j|<t\). This complex simplicially collapses to the boundary complex of the \(\lceil m/t\rceil\)-dimensional cross-polytope, realizing the asserted sphere.

In particular, the penultimate scale \(r=k-1\) yields the sphere \(S^{\lfloor(k-1)/2\rfloor}\), and these geometric fixed-space sphere dimensions grow without bound with \(k\).

## Assumptions and scope

All graphs, complexes, and group actions are finite. A simplex is admitted at exact distance \(r\). Geometric fixed points mean points in the topological realization fixed by every element of \(G\), **not** invariant homology classes and not just the subcomplex on individually fixed vertices. Homotopy equivalences are ordinary topological homotopy equivalences, with a stronger elementary-collapse model as stated. The theorem does not determine maps induced on homology between different filtration levels or the ambient Johnson-complex homotopy type.

## Proof

**1. Orbit simplices.** The \(G\)-orbits on the Johnson vertices are \(O_i=\{U:|U\cap A|=i\}\), for \(0\le i\le k\). If \(U\in O_i\) and \(V\in O_j\), choose their portions in \(A\) and \(B\) independently. The smallest achievable intersection cardinality is

\[
\min |U\cap V|=\max(0,i+j-k)+\max(0,k-i-j)=|i+j-k|.
\]

For \(i=j\), the same minimum is attained by distinct vertices whenever \(O_i\) contains more than one vertex. The singleton endpoint orbits also satisfy the resulting compatibility criterion. Thus \(O_i\) itself spans a Rips simplex precisely when \(|2i-k|\ge t\), and the union of admissible orbits \(O_i,O_j\) spans a simplex precisely when \(|i+j-k|\ge t\).

A point of an invariant simplex is fixed by \(G\) exactly when its barycentric coefficients are constant over each included \(G\)-orbit. Consequently the geometric fixed-point set has the canonical orbit-barycenter triangulation whose vertices are admissible \(O_i\)'s and whose faces consist of jointly admissible orbit collections. This is an exact piecewise-linear description, not an inference from fixed homology.

**2. The band graph.** The admissible indices are

\[
0\le i\le a\quad\text{or}\quad k-a\le i\le k,
\qquad a=\left\lfloor\frac{k-t}{2}\right\rfloor=\left\lfloor\frac r2\right\rfloor.
\]

Write the low-index orbit \(O_i\) as \(L_i\), and the high-index orbit \(O_{k-j}\) as \(H_j\), for \(0\le i,j\le a\). Each of the two sides is pairwise compatible, because the minimum intersection on a single side is at least \(t\). Across the sides, the pair \(L_i,H_j\) is incompatible exactly when \(|i-j|<t\). Therefore the orbit-barycenter complex is exactly \(\operatorname{Ind}(F_{m,t})\), where \(m=a+1\).

**3. Explicit folds.** For a graph \(Q\), if distinct vertices \(u,v\) have \(N_Q(u)\subseteq N_Q(v)\) (open neighborhoods), then \(u,v\) are nonadjacent and \(\operatorname{Ind}(Q)\) simplicially collapses onto \(\operatorname{Ind}(Q-v)\). To see this, pair each independent face containing \(v\) but not \(u\) with the face obtained by adding \(u\); these pairs form an acyclic elementary-collapse matching, performed in decreasing dimension.

Apply this to \(F_{m,t}\). First remove \(L_1,\ldots,L_{\min(t-1,m-1)}\), each dominated in the stated neighborhood sense by \(L_0\): initially \(N(L_0)=\{H_j:0\le j<\min(t,m)\}\subseteq N(L_i)\) for all such \(i\). After those removals, \(N(H_0)=\{L_0\}\subseteq N(H_i)\), so remove \(H_1,\ldots,H_{\min(t-1,m-1)}\). This leaves one isolated edge \(L_0H_0\) and, when \(m>t\), the induced band graph on indices \(t,\ldots,m-1\), which is isomorphic to \(F_{m-t,t}\). Repeat the same two-sided folds on that smaller graph.

After \(b=\lceil m/t\rceil\) rounds, the residual graph is a disjoint union of exactly \(b\) edges. Its independence complex is the join of \(b\) copies of \(S^0\), hence is the boundary of the \(b\)-dimensional cross-polytope and is homeomorphic to \(S^{b-1}\). Finally,

\[
b-1=\left\lfloor\frac{m-1}{t}\right\rfloor
=\left\lfloor\frac{\lfloor r/2\rfloor}{k-r}\right\rfloor
=\left\lfloor\frac{r}{2(k-r)}\right\rfloor.
\]

This proves the claim for every integer \(0\le r<k\). For \(r\ge k\), the diameter of \(J(2k,k)\) is \(k\), so the entire Rips complex is a simplex. Its fixed space is the simplex on the barycenters of the \(k+1\) vertex orbits.

## Verification

The accompanying standalone Python program `verify.py` uses only the standard library. Running `python3 verify.py` tests all orbit-distance extrema for \(1\le k\le6\), the explicit open-neighborhood fold sequence for \(1\le m,t\le60\), and independent finite mod-two simplicial boundary ranks for every \(1\le k\le12\) and \(0\le r<k\). On execution, it reported 83 orbit-index comparisons across 21 parameter scales, 198,880 validated fold deletions across 3,600 band graphs, and 78 independent homology computations, all passing. These finite computations support but do not replace the all-parameter proof above.

## Relationship to prior work

Bendersky, Elia and Grbić (arXiv:2605.00705v1, May 1, 2026) analyze Vietoris–Rips complexes of binary hypercubes using independence-complex and cohomological techniques. Kratica, Čangalović and Kovačević-Vujčić (arXiv:2605.06837v1, May 7, 2026) study metric dimensions of Johnson and Kneser graphs and explicitly record the Johnson distance formula used here; they do not study Rips fixed spaces. Galetto, Montaño and Wellner (arXiv:2606.20784v1, June 18, 2026) analyze equivariant homology representations of hypercube Rips complexes, not geometric fixed spaces of the constant-weight Johnson slice.

Shuldiner and Oldford (arXiv:2208.12710) classify Johnson-graph maximal cliques; their statement concerns scale-one clique structure, not geometric fixed points throughout the Rips filtration. The closest identified published Johnson Rips result determines ordinary scale-one homotopy types, not the fixed spaces under the two-block Young subgroup. The orbit-barycenter reduction and all-scale spherical classification here are different statements: the ordinary homotopy type or an ambient homology character alone does not imply them. The elementary open-neighborhood folding rule is standard and is not claimed as new; its uniform band-graph application is part of the presented proof.

## Limitations

This classification concerns the equal-block Young subgroup \(\mathfrak S_k\times\mathfrak S_k\) of the Johnson graph \(J(2k,k)\). It does not classify arbitrary subgroups, other Johnson-slice sizes, all inclusion-induced persistence maps, or ambient complexes. Searches and comparison of accessible full text do not establish exhaustive novelty: an equivalent result under alternate terminology or in an unindexed thesis remains possible. Independent mathematical validation has not been performed.

## References

1. M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris–Rips complex of a hypercube graph*, arXiv:2605.00705v1 (2026-05-01), https://arxiv.org/abs/2605.00705.
2. J. Kratica, M. Čangalović and V. Kovačević-Vujčić, *The strong and doubly metric dimensions of Johnson and Kneser graphs*, arXiv:2605.06837v1 (2026-05-07), https://arxiv.org/abs/2605.06837.
3. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784v1 (2026-06-18), https://arxiv.org/abs/2606.20784.
4. P. Shuldiner and R. W. Oldford, *The Clique Structure of Johnson Graphs*, arXiv:2208.12710 (2022), https://arxiv.org/abs/2208.12710.
5. *Sphere-wedge collapse of scale-one Johnson-graph Rips complexes*, published mathematical research record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sphere-wedge-collapse-of-scale-one-johnson-graph-rips-complexes--c10287ed1518.
