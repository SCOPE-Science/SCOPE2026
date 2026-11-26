# Labelled geodesic packing census of complete split graphs

## Finding

Let \(G_{r,s}=K_r\vee\overline{K_s}\), with clique \(C\) of size \(r\ge1\) and independent set \(I\) of size \(s\ge2\). A maximal geodesic is a shortest path not properly contained as a contiguous subpath of another shortest path. A packing is an unordered collection of pairwise vertex-disjoint maximal geodesics. Let \(t\) count its three-vertex paths and \(u\) its two-vertex paths. Put \(h=\min(r,\lfloor s/2\rfloor)\). For \(0\le t\le h\) and \(0\le u\le\lfloor(r-t)/2\rfloor\), the number of such packings of type \((t,u)\) is
\[
A_{r,s}(t,u)=\binom rt\frac{s!}{2^t(s-2t)!}\frac{(r-t)!}{2^u u!(r-t-2u)!}.
\]
It is zero for all other nonnegative integer types. The full size distribution, including the empty packing, is
\[
 P_{r,s}(z)=\sum_{t=0}^{h}\sum_{u=0}^{\lfloor(r-t)/2\rfloor} A_{r,s}(t,u)z^{t+u}.
\]
In particular, with \(k=\lfloor(r+h)/2\rfloor\), the number of maximum packings is
\[
[z^k]P_{r,s}(z)=A_{r,s}\left(h,\left\lfloor\frac{r-h}{2}\right\rfloor\right)
+\mathbf1_{\{r+h\text{ odd}\}}A_{r,s}\left(h-1,\frac{r-h+1}{2}\right),
\]
where the second term is included only for odd \(r+h\). When \(s\ge2r\), this coefficient is \(s!/(2^r(s-2r)!)\). The census counts actual labelled packings, not merely which types are feasible. For example, for fixed \(r\) throughout \(s\ge2r\) the maximum cardinality remains \(r\), but the number of optimizers varies with \(s\).

## Assumptions and scope

Graphs are finite, simple and undirected, and vertices carry distinct labels. A path is counted without orientation; unused vertices are permitted. The finding concerns only the labelled packing distribution and its multiplicities. Maximal-path types, feasible packing types, the optimum size, and transversal facts below are specializations of existing complete-multipartite results, not separate contributions.

## Proof

**Maximal paths.** The graph has diameter two, realized by any two vertices of \(I\). Every length-two geodesic has distinct endpoints \(a,b\in I\) and a center \(c\in C\). Every such path \(a-c-b\) is maximal. Each clique edge is also maximal, since each endpoint is universal and any length-two path containing that edge has adjacent endpoints. Any clique–independent edge extends to a length-two geodesic by using a second independent endpoint, possible since \(s\ge2\); it is not maximal. Single vertices are not maximal since the graph has no isolated vertices. These are also the maximal-path types from the general complete-multipartite classification [1,2].

**Labelled multiplicities.** Select the \(t\) clique centers of three-vertex paths in \(\binom rt\) ways. A temporary order of these distinctly labelled centers lets one assign an ordered list of \(2t\) distinct vertices of \(I\) to them, two per center; switching the two endpoints at any center represents the same path. The number of assignments is \(s!/[2^t(s-2t)!]\). There is no division by \(t!\) because each pair is assigned to a specified center. A matching of size \(u\) among the remaining clique vertices then supplies the two-vertex paths; ordering its \(2u\) distinct vertices and dividing by the orders of matching edges and their endpoints gives \((r-t)!/[2^u u!(r-t-2u)!]\). Every packing uniquely determines these three choices. The resulting polynomial follows by grouping types according to \(t+u\).

**Maximum coefficient.** For fixed \(t\) the greatest possible size is \(t+\lfloor(r-t)/2\rfloor=\lfloor(r+t)/2\rfloor\). On \(0\le t\le h\) its maximum is \(k\); it attains \(k\) at \(h\), and only when \(r+h\) is odd does it also attain \(k\) at \(h-1\). Summing the corresponding multiplicities proves the coefficient formula. In the saturation range \(s\ge2r\), \(h=r\) and the only optimal type is \((r,0)\), giving the stated specialization.

Equivalently, the formal bivariate exponential generating function of these block counts is
\[
\sum_{r,s\ge0}P_{r,s}(z)\frac{x^ry^s}{r!s!}
=\exp\!\left(x+y+\frac{z}{2}x^2+\frac{z}{2}xy^2\right).
\]
The four block types are unused clique vertices, unused independent vertices, clique edges, and three-vertex paths with one clique center. This uses the block-counting extension of the coefficients outside the stated graph domain.

## Known specializations used for comparison

Viewing \(G_{r,s}\) as the complete multipartite graph with one part \(I\) of size \(s\) and \(r\) singleton parts, the feasibility theorem in [1] reduces to \(2u+t\le r\) and \(2t\le s\). Indeed, its additional total-vertex bound \(2u+3t\le r+s\) follows from these two inequalities. This gives the support of the census and the optimal size, not the number of packings on that support.

For transversals (sets meeting every maximal geodesic), [2] classifies their complements: in this family a complement is either contained in \(I\) or has at most one element of \(I\) and at most one vertex of \(C\). The maximal complements are therefore \(I\) and the pairs \(\{i,c\}\) with \(i\in I,c\in C\). Their complements give the inclusion-minimal transversal polynomial \(T_{r,s}(z)=z^r+rs\,z^{r+s-2}\), with multiplicities added when \(s=2\). The geodesic transversal number is \(r\), so the packing–transversal gap is \(\lceil(r-h)/2\rceil\) and vanishes exactly when \(s\ge2r\). These transversal and gap statements are included as comparison checks; the claimed advance is the labelled packing count.

## Verification

The included `verify_split_geodesics.py` (Python 3 standard library) constructs shortest paths directly, tests maximality by contiguous-subpath containment and enumerates disjoint packings by vertex-mask dynamic programming. The recorded run checked all 22 graph profiles with \(1\le r\le5\), \(2\le s\le6\), \(r+s\le9\), including the complete packing polynomial and the known transversal comparisons. The recorded arithmetic sweep over \(1\le r\le50\), \(2\le s\le100\) tests packing-size and saturation identities. These finite checks corroborate selected instances; the combinatorial proof establishes the exact coefficients on the full domain.

## Relationship to prior work and limitations

The complete-multipartite packing theorem [1] gives sharp existence constraints for each path-type pair and a scalar maximum; the complete-multipartite transversal theorem [2] classifies all transversals and therefore already implies every transversal assertion above. The work on geodesic packing by Manuel, Brešar and Klavžar [3] supplies the packing framework. A related complete-multipartite packing-polynomial calculation [4] assumes every part has at least two vertices and so does not address this singleton-part family, where maximal geodesics include clique edges. For the scalar geodesic transversal problem on joins, see also Peterin and Semanišin [5]. No general multipartite census, result for arbitrary split graphs, statement for \(s<2\), or priority claim beyond the comparisons made here is asserted.

## References

1. *Geodesic packings of complete multipartite graphs: three sharp capacity constraints*, Resultary record `483fcd9cfba1`, Finding and Proof §§1–4.
2. *All geodesic transversals of complete multipartite graphs*, Resultary record `e5c4e05a4d10`, Finding and Proof.
3. P. Manuel, B. Brešar, and S. Klavžar, *Geodesic packing in graphs*, arXiv:2210.15325; *Applied Mathematics and Computation* 459 (2023), 128277.
4. *Geodesic-packing polynomials of complete multipartite graphs and reentrant purity for doubleton parts*, Resultary record `e3ceab8f39fe`, Assumptions and scope.
5. I. Peterin and G. Semanišin, *Geodesic transversal problem for join and lexicographic product of graphs*, *Computational and Applied Mathematics* 41 (2022), article 128, doi:10.1007/s40314-022-01834-1.
