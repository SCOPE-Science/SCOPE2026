# Scale-two Rips homotopy types of finite circular ladders

## Finding
Let \(P_n=C_n\mathbin{\square}K_2\) be the cyclic prism graph, with every edge of length one and the shortest-path metric on its **finite vertex set**. For every integer \(n\ge3\), the inclusive scale-two Vietoris–Rips complex has the complete homotopy classification
\[
\operatorname{VR}_{\le}(V(P_n);2)\simeq
\begin{cases}
*,&n=3,\\
S^3,&n=4,\\
S^2,&n=5,\\
\bigvee^3 S^2,&n=6,\\
S^1,&n\ge7.
\end{cases}
\]
For every \(n\ge7\), the complex in fact **simplicially collapses** onto either rim cycle. The natural inclusion from scale one to scale two has image of rank \(0\) on integral first homology when \(3\le n\le6\), and rank \(1\) when \(n\ge7\). These statements concern only scales one and two and do not assert the complete later-scale persistence barcode.

## Assumptions and scope
The vertices are \((i,a)\) with \(i\in\mathbb Z/n\mathbb Z\) and \(a\in\{0,1\}\); horizontal edges join \((i,a)\) to \((i+1,a)\), and rungs join \((i,0)\) to \((i,1)\). The graph-product distance is
\[
d((i,a),(j,b))=\min\{|i-j|,\,n-|i-j|\}+\mathbf1_{a\ne b},
\]
where the representative of \(i-j\) is taken in \(\{0,\dots,n-1\}\). The simplices of \(\operatorname{VR}_{\le}(V(P_n);2)\) are **all** vertex subsets with every pair at graph distance at most two. There are no points in edge interiors. The original graph at scale one has first Betti number \(n+1\).

## Proof
**The small exceptional complexes.** At \(n=3\), the graph has diameter two, so its scale-two complex is a simplex. At \(n=4\), the graph is the three-cube \(Q_3\). Its squared graph is the complement of four disjoint antipodal pairs, so its flag complex is the boundary of the four-dimensional cross-polytope, homeomorphic to \(S^3\). This cube case is already known in the graph-Rips literature and is included here to delimit the complete prism classification.

At \(n=5,6\), the exact elementary-collapse pairs listed in `cert_small.json` delete all cells above dimension two (respectively 25 and 18 verified free-face pairs). The finite input complexes have face vectors (from dimension zero upward)
\[
\begin{array}{c|l|c}
 n& (f_0,f_1,f_2,\ldots)&\chi\\ \hline
5&(10,35,50,25,2)&2\\
6&(12,42,52,18)&4.
\end{array}
\]
Each length-four square of the prism is filled by two triangles at scale two. Further, each scale-two edge not already in the original graph is homotopic across a triangle to a two-edge shortest path. Thus the original graph surjects on the scale-two fundamental group, and after killing the squares only an outer-rim loop can remain. For \(n=5\), every outer-row vertex pair is at distance at most two, so that rim is null-homotopic. For \(n=6\), the four outer-row triangles on column triples \((0,1,2)\), \((2,3,4)\), \((4,5,0)\), and \((0,2,4)\) form a simplicial disk bounding the rim. Hence both complexes are simply connected. They collapse to connected two-dimensional CW complexes, and their Euler characteristics give free second homology of ranks one and three. The Hurewicz theorem and the homological Whitehead theorem identify them respectively with \(S^2\) and \(\bigvee^3 S^2\). This is a homotopy conclusion, not a claim of an elementary collapse to spheres.

**Uniform facets when \(n\ge7\).** The distance equation shows that every maximal scale-two clique is exactly one of the following \(3n\) four-vertex sets (all column indices modulo \(n\)):
\[
T_i^a=\{(i-1,a),(i,a),(i+1,a),(i,1-a)\},\quad a\in\{0,1\},
\]
\[
U_i=\{(i,0),(i+1,0),(i,1),(i+1,1)\}.
\]
Indeed, each same-row pair lies within cyclic distance two, each cross-row pair within cyclic distance one, and this forces any mixed-row maximal clique to be one of these three kinds. The initial complex therefore has face vector \((2n,7n,8n,3n)\).

**A nine-orbit simplicial collapse.** Identify each entry \((j,a)\) below with the vertex whose column is \(j\pmod n\) and whose row is \(a\). For each phase in the table, translate both the free face \(A\) and its unique coface \(B\) by **all** column shifts \(t\in\mathbb Z/n\mathbb Z\), removing each \((A+t,B+t)\) as an elementary simplicial collapse. Execute phase zero completely before phase one, and so on. The entries are literal integer-offset coordinate pairs; they may be independently replayed from `cert_orbits.json`.

| Phase | Free face \(A\) | Unique coface \(B\) |
| ---: | --- | --- |
| 0 | `[(0,1),(1,1),(2,1)]` | `[(0,1),(1,0),(1,1),(2,1)]` |
| 1 | `[(0,0),(1,1),(2,0)]` | `[(0,0),(1,0),(1,1),(2,0)]` |
| 2 | `[(0,0),(0,1),(1,0)]` | `[(0,0),(0,1),(1,0),(1,1)]` |
| 3 | `[(0,1),(2,1)]` | `[(0,1),(1,0),(2,1)]` |
| 4 | `[(0,0),(-1,1)]` | `[(0,0),(0,1),(-1,1)]` |
| 5 | `[(0,1),(1,1)]` | `[(0,0),(0,1),(1,1)]` |
| 6 | `[(0,0),(1,1)]` | `[(0,0),(1,0),(1,1)]` |
| 7 | `[(0,0),(2,0)]` | `[(0,0),(1,0),(2,0)]` |
| 8 | `[(0,1)]` | `[(0,0),(0,1)]` |

Here is an exact, parameter-independent free-face check, not an inference from finitely many values of \(n\). Choose in each \(A\) a vertex \((0,a)\). Every simplex properly containing \(A\) lies in a maximal facet through this vertex. The list \(T_i^a,U_i\) restricts such facets to the six locally possible facets with center in \(\{-1,0,1\}\), all supported in columns \([-2,2]\). Every previously removed translated face that contains \((0,a)\) arises by aligning one of its listed vertices \((u,a)\) with column zero; it is then supported within columns \([-3,3]\). For \(n\ge7\), this seven-column band embeds injectively modulo \(n\), and exact finite subset comparison is valid uniformly in \(n\). Checking each of the nine rows against these six facets and all earlier translations leaves precisely the two faces \(A\) and \(B\) among faces containing \(A\); hence \(B\) is its unique remaining proper coface. The complete nine-row symbolic set comparison is carried out by `symbolic_phase_check()` in `verify_prism.py`, with no substituted value of \(n\). Within each phase the translates of \(A\) and \(B\) are pairwise distinct, so the orbit collapses may be executed successively. After the \(9n\) pairs are removed, precisely the \(n\) vertices and \(n\) edges of the row-zero cycle remain. Therefore
\[
\operatorname{VR}_{\le}(V(P_n);2)\searrow C_n\simeq S^1
\qquad(n\ge7).
\]

**Integral first-homology map.** At scale one, the complex is the prism graph. For \(n\le6\), its scale-two target is simply connected, so the induced \(H_1\)-map vanishes. For \(n\ge7\), the explicit collapse retains the outer cycle and the inclusion of that cycle from scale one induces the generator of the scale-two \(H_1\); hence the image has rank one. No higher-scale maps are asserted.

## Verification
The package contains exact standalone `cert_small.json`, `cert_orbits.json`, and `verify_prism.py`. The checker reconstructs the scale-two graph directly from the distance formula, enumerates every maximal clique and every simplex, independently computes reduced homology over \(\mathbf F_2\) for \(3\le n\le6\), and verifies every free-face pair from the small certificates. It checks the facet description and all \(9n\) elementary collapses for \(7\le n\le30\). More importantly, `symbolic_phase_check()` verifies the **nine all-parameter local freeness identities on integer offsets**; its proof of applicability for all \(n\ge7\) is the seven-column injection argument given above. The all-parameter conclusion depends on the explicit facet classification and this local argument, not on finite homology experiments. The checker does not verify results at scales above two.

## Relationship to prior work
Adamaszek–Adams classified Rips complexes of subsets of a metric circle; the cyclic prism has two rows and rung edges, so this classification is not a substitution into a one-circle theorem. Adamaszek's graph-power paper supplies the graph-power language and the cycle-power examples, but its high-girth collapse does not apply because the prism has squares, and its cycle-only classification does not describe the two-row complex. Its cycle-six disk is consistent with the explicit rim filling used above. The graph-Rips theorem for the three-cube already covers our \(n=4\) special case, which is not claimed separately as new.

The most closely motivated comparison is Adamaszek and collaborators' *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings*, Section 5, Question 1 and Example 2. That article discusses circular ladders with the full **continuous metric graph** and provides a partial description under restricted scale conditions, whereas this theorem concerns only the finite vertex sample and the **inclusive integer threshold two**. Its supremum-metric result does not apply to shortest-path sum distance. Thus the present all-\(n\) finite-vertex statement is not entailed by that example. Likewise the known low-degree homology formulas for sum-metric products do not yield these full homotopy types or their explicit simplicial collapses.

## Limitations
This result does not classify the Rips filtration after threshold two, does not treat interior edge points, unequal rung lengths, wider circular ladders, or irregular spacing, and does not resolve the continuous-metric-graph question. The cube subcase is known. Absence of a matching statement in indexed searches cannot establish absolute priority; an unindexed equivalent result could exist.

## References
1. M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, first arXiv version 2015-03-12, arXiv:1503.03669; *Pacific Journal of Mathematics* 290 (2017), 1–40, DOI 10.2140/pjm.2017.290.1. Published classification: primary 55U10 (also primary 05E45).
2. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, *Israel Journal of Mathematics* 196 (2013), 295–319.
3. M. Adamaszek et al., *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings*, arXiv:1712.06224, especially Section 5, Question 1 and Example 2.
4. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040, cube scale-two special case.
5. G. Carlsson and B. Filippenko, *Persistent homology of the sum metric*, arXiv:1905.04383, low-degree product comparison.
