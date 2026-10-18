# Weil--Cartier gap and canonical non-Cartierness of complete-graph perfect-matching toric varieties

## Finding
For every integer \(m\ge3\), let \(n=2m\), let \(E\) be the edges of the complete graph \(K_n\), and set \(P_m=\operatorname{conv}\{\chi_M\in\{0,1\}^{E}:M\text{ is a perfect matching}\}\). Write \(X_m=X(\mathcal N(P_m))\) for the normal projective toric variety of the **normal fan** of this polytope. For the lattice convention fixed below, the following simultaneous formulas hold:
\[
\begin{aligned}
\dim X_m&=m(2m-3),\\
\operatorname{Cl}(X_m)&\cong\mathbb Z^{4^{m-1}},\\
\operatorname{Pic}(X_m)&\cong\mathbb Z,\\
\operatorname{Cl}(U_M)&\cong\mathbb Z^{m(2^{m-1}-1)}
\end{aligned}
\]
for every maximal toric affine chart \(U_M\), indexed by any perfect matching \(M\). All displayed class groups are torsion-free. The canonical divisor of every \(U_M\) is **not** \(\mathbb Q\)-Cartier, so no torus-fixed point is \(\mathbb Q\)-Gorenstein or \(\mathbb Q\)-factorial. In contrast, at \(m=2\) the polytope is a lattice triangle and the corresponding toric surface is \(\mathbb P^2\).

For instance, the triples \((\dim X_m,\operatorname{rank Cl}(X_m),\operatorname{rank Cl}(U_M))\) at \(m=3,4,5\) are respectively \((9,16,9)\), \((20,64,28)\), and \((35,256,75)\). This separates the single Cartier-divisor direction from exponentially many global and local Weil-divisor directions in the same geometrically natural family.

## Assumptions and scope
Fix an algebraically closed ground field of arbitrary characteristic. Use the saturated lattice \(\Lambda=\{y\in\mathbb Z^E:\sum_{e\ni v}y_e=0\text{ for every }v\in[n]\}\) as the lattice of integral tangent differences of the ambient affine hull, and \(N=\operatorname{Hom}(\Lambda,\mathbb Z)\) as the lattice of normal-fan rays. These choices specify the toric variety even if a different unsaturated lattice convention is adopted elsewhere. All class groups are *Weil divisors modulo principal divisors*. The group \(\operatorname{Pic}\) concerns Cartier divisors, not the rank of \(\operatorname{Cl}\). A normal projective toric variety is complete, but need not be \(\mathbb Q\)-factorial.

## Proof
**Facet and lattice setup.** Let \(B\) be the unsigned vertex-edge incidence matrix, so the affine hull is \(Bx=\mathbf1\). Its rank is \(n\): if \(z_a+z_b=0\) for every edge of \(K_n\), any triangle forces all \(z_a=0\). The barycenter of all perfect matchings has \(x_e=1/(n-1)\) on every edge; on any odd cut with \(3\le |S|\le n-3\) it has total crossing weight \(|S|(n-|S|)/(n-1)>1\). Thus it strictly satisfies every nontrivial facet inequality and the relative affine hull is exactly \(Bx=\mathbf1\). Hence \(d=|E|-n=\binom n2-n=m(2m-3)\). Edmonds' perfect-matching-polytope theorem states that the inequalities \(x_e\ge0\) and \(x(\delta(S))\ge1\) for odd vertex sets, together with \(Bx=\mathbf1\), cut out exactly \(P_m\). In the complete graph with \(n\ge6\), the irredundant facets are precisely the \(|E|\) coordinate facets and the odd cuts with \(3\le |S|\le n-3\), where complementary sets index the same facet. This standard irredundant form can also be checked from alternating four-edge exchanges among perfect matchings: any weight constant on all matchings of a given proposed facet is a sum of vertex-degree weights and that facet's weight; and the strict barycenter of the remaining matchings violates no other facet. Thus every indicated facet has codimension one.

The odd-set inequality is equivalent to \(x(E(S))\le (|S|-1)/2\). Its inward normal in \(N\) is the restriction of \(-\sum_{e\in E(S)} e_e^*\); denote it by \(u_S\). The coordinate normal is \(u_e=e_e^*|_\Lambda\). Both are primitive: a perfect-matching four-edge exchange realizes a unit change of a coordinate, and choosing matchings with one versus three crossing edges realizes a unit change of \(\sum_{e\in E(S)}x_e\). The two primitive normals for complementary odd subsets agree in \(N\) because the difference is a linear combination of the degree equations. The number of distinct odd facets is \(2^{n-2}-n\), giving \(r=|E|+2^{n-2}-n=d+2^{n-2}\) fan rays.

**Global Weil class group.** The toric divisor exact sequence is \(0\to\Lambda\to\mathbb Z^{r}\to\operatorname{Cl}(X_m)\to0\), where the first map evaluates the primitive ray normals. Already all coordinate normals \(u_e\) span \(N\) *integrally*, because a homomorphism on the primitive sublattice \(\Lambda\subseteq\mathbb Z^E\) extends to \(\mathbb Z^E\). Therefore the cokernel has no torsion, and its rank is \(r-d=2^{n-2}=4^{m-1}\).

**Local Weil class group.** Fix a perfect matching \(M\). Exactly \(|E|-m=2m(m-1)\) coordinate facets contain \(\chi_M\). An odd facet \(S\) contains it precisely when \(M\) has exactly one edge crossing its cut. Such a set comprises \(j\) complete matching pairs and one endpoint of a further matching pair, with \(|S|=2j+1\). Counting all admissible \(j\) and identifying complements gives
\[
\#\{\text{incident odd facets}\}
=\frac12\sum_{j=1}^{m-2}\binom mj\,2(m-j)
=m(2^{m-1}-2).
\]
Thus its full-dimensional normal cone has \(r_M=2m(m-1)+m(2^{m-1}-2)\) rays, and the local class rank is \(r_M-d=m(2^{m-1}-1)\). The coordinate normals \(u_e\) with \(e\notin M\) already span \(N\) integrally: on \(\Lambda\), for each matched pair \(ab\in M\), the degree equation gives \(y_{ab}=-\sum_{c\ne a,b}y_{ac}\), an integer combination of off-matching coordinates. Hence \(\operatorname{Cl}(U_M)\) also has no torsion.

**Picard rank.** Let \(h_e\) and \(h_S\) be arbitrary rational values of a putative Cartier support function on the coordinate and odd-cut rays. At the maximal cone of \(M\), its linear form \(y_M\in\Lambda\otimes\mathbb Q\) is forced to satisfy \((y_M)_e=h_e\) for all \(e\notin M\). Define \(H_a=\sum_{e\ni a}h_e\). For every matched pair \(ab\in M\), the degree equations force \((y_M)_{ab}=h_{ab}-H_a=h_{ab}-H_b\); since every pair occurs in some perfect matching, this demands \(H_a=H\) independent of \(a\). Conversely, if these vertex sums agree, \(y_M=h-H\chi_M\) defines an element of \(\Lambda\otimes\mathbb Q\) for every \(M\). On an incident odd facet \(S\) of size \(2j+1\), the condition is necessarily and sufficiently \(h_S=jH-\sum_{e\subseteq S}h_e\), independent of which incident matching is chosen. Therefore the rational space of Cartier support functions has dimension \(|E|-(n-1)=d+1\). Quotienting by globally linear support functions (dimension \(d\)) gives \(\operatorname{rank Pic}(X_m)=1\). The Picard group is torsion-free for a normal toric variety, and projectivity ensures a nonzero ample Cartier class, so \(\operatorname{Pic}(X_m)\cong\mathbb Z\).

**Uniform canonical obstruction.** If \(K_{U_M}\) were \(\mathbb Q\)-Cartier, a rational character would take the same value \(1\) on every primitive ray of the normal cone at \(M\) (the opposite sign gives the equivalent convention). At all off-matching coordinate rays this forces \(y_e=1\). The degree equations then force \(y_{ab}=-(n-2)\) for every matched edge \(ab\in M\). Choose \(S=\{a,b,c\}\) with \(ab\in M\), while \(c\) belongs to another matched pair; its blossom facet is incident to \(M\). Evaluation of its primitive normal gives
\[
u_S(y)=-y_{ab}-y_{ac}-y_{bc}=(n-2)-2=n-4=2m-4,\]
which differs from \(1\) for all \(m\ge3\). Thus no canonical rational Cartier character exists at any maximal cone. Since \(r_M>d\), these cones are also nonsimplicial, proving the non-\(\mathbb Q\)-factorial assertion. For \(m=2\), the three perfect matchings of \(K_4\) give the standard lattice triangle, explaining the exceptional smooth case.

## Verification
The included standalone Python program `CHECK.py` enumerates every perfect matching for \(n=6,8\), checks the rank of every coordinate and nontrivial odd-cut facet by exact modular elimination, computes the active facet and local class counts, and constructs **all** rational Cartier compatibility equations at **every** torus-fixed point to verify Picard rank one. It also tests the canonical-height contradiction. Extract the `CHECK.py` file and run `python CHECK.py` with ordinary Python 3; the expected terminal line is `VERIFY_OK`. These finite tests corroborate the all-parameter proof, rather than replacing it. Rank calculations modulo a prime certify independence in these checked cases; they are not an infinite argument or a substitute for the lattice proofs.

## Relationship to prior work
Edmonds' matching-polytope theorem supplies the facet description, not the divisor class calculations. Beck--Haase--Sam and Tagami study perfect-matching polytopes, principally of bipartite graphs, with Gorensteinness meaning the **Ehrhart semigroup algebra** is Gorenstein. That is a different property from \(\mathbb Q\)-Gorensteinness of the normal-fan toric variety proved to fail here. Higashitani--Padrol--Sanyal (2026) give a broad Minkowski-indecomposability theorem for \(0/1\)-polytopes; it is relevant to the one-dimensional Cartier direction and is **not** claimed to be new general indecomposability theory. Their theorem does not specify these integral global and local class groups or canonical Cartier obstructions. General toric divisor exact sequences are standard. The claim here is the simultaneous precise arithmetic of those groups and the all-parameter local obstruction, not the generic toric definitions themselves.

## Limitations
The result is for the **normal fan**, not the projective toric variety associated to the semigroup cone over the polytope. No local analytic determinantal model, singular-scheme structure, or independent validation is asserted. The irredundancy of matching facets and toric divisor presentation are established background inputs; the novelty claim is conditional on the absence of equivalent specialized calculations under alternative terminology. The combinatorial experiments cover only \(n=6,8\), whereas the proof is symbolic for all \(m\ge3\).

## References
1. J. Edmonds, “Maximum Matching and a Polyhedron With 0,1 Vertices,” *J. Res. Nat. Bur. Standards* **69B** (1965), 125--130. (Matching inequalities.)
2. M. Beck, C. Haase, and S. V. Sam, “Grid graphs, Gorenstein polytopes, and domino stackings,” arXiv:0711.4151 (first publicly posted 2007-11-26). https://arxiv.org/abs/0711.4151
3. M. Tagami, “Gorenstein Polytopes Obtained from Bipartite Graphs,” arXiv:0803.1033 (first publicly posted 2008-03-07). https://arxiv.org/abs/0803.1033
4. A. Higashitani, A. Padrol, and R. Sanyal, “Indecomposability of 0/1-polytopes,” arXiv:2605.22594 (2026). https://arxiv.org/abs/2605.22594
5. D. Cox, J. Little, and H. Schenck, *Toric Varieties*, AMS Graduate Studies in Mathematics 124 (2011), Chapter 4.
