# Exact disagreement polynomial for leaf-paired symmetric argumentation frameworks

## Finding

For every finite simple graph \(G=(V,E)\) on \(n\geq 1\) vertices, make a symmetric argumentation framework \(F(G)\) with one core argument \(v\) and one fallback argument \(v^*\) for every \(v\in V\). The mutual attacks are the core-core edges of \(G\) and the pairs \(\{v,v^*\}\), with no other attacks. A stable extension is a conflict-free set that attacks every argument outside it. Write \(\mathcal S(G)\) for its set of stable extensions, and define the ordered-pair disagreement polynomial
\[
D_G(t)=\sum_{A,B\in\mathcal S(G)}t^{|A\triangle B|}.
\]
For \(S\subseteq V\), let \(N_G(S)\) be the **external** open neighborhood of \(S\), let \(\kappa(H)\) count connected components of \(H\), including isolated vertices, and let \(i(H)\) count all independent vertex sets of \(H\), including the empty set. Put \(\kappa(\varnothing)=0\) and \(i(\varnothing)=1\). The following exact polynomial identity holds:
\[
\boxed{\displaystyle
D_G(t)=\sum_{\substack{S\subseteq V\\G[S]\,\mathrm{bipartite}}}
2^{\kappa(G[S])}\,i\!\left(G\left[V\setminus(S\cup N_G(S))\right]\right)t^{2|S|}.}
\]
Define the odd-cycle-transversal number \(\tau(G)=\min\{|T|:T\subseteq V,\ G[V\setminus T]\text{ is bipartite}\}\). The complete support of this polynomial is exactly
\[
\boxed{\{0,2,4,\ldots,2(n-\tau(G))\}.}
\]
In particular, the maximum stable-extension disagreement is \(2(n-\tau(G))\), and the **number of ordered pairs** attaining it is exactly
\[
\boxed{\displaystyle
[t^{2(n-\tau(G))}]D_G(t)=
\sum_{\substack{S\subseteq V,\ |S|=n-\tau(G)\\G[S]\,\mathrm{bipartite}}}
2^{\kappa(G[S])}.}
\]

## Assumptions and scope

The core \(G\) is any finite undirected simple graph; disconnected graphs and isolated vertices are allowed. Attacks in \(F(G)\) are symmetric in both directions and have no self-attacks. Fallback vertices are distinct, and each \(v^*\) is attacked only by its own core vertex \(v\). Distances count **all** \(2n\) arguments, not only core vertices. Ordered pairs, including identical extensions, are counted. Independent sets can be empty, and the empty induced graph has one proper two-coloring and one independent set.

The diversity metric and stable semantics follow the established definitions for abstract argumentation. The known equivalence of stable, preferred, and naive extensions on symmetric attack frameworks means that the same polynomial also describes pairwise distances under those two semantics for this family; that equivalence is not claimed as new.

## Proof

**1. Forced binary choices.** In a stable extension, at most one of \(v\) and \(v^*\) can occur because they attack one another. They cannot both be absent: the omitted fallback argument \(v^*\) would then have no attacker in the extension. Therefore exactly one member of each pair occurs. The chosen core arguments form an independent set \(I\subseteq V\). Conversely every independent set \(I\) determines the stable extension
\[
A_I=I\cup\{v^*:v\in V\setminus I\}.
\]
Indeed \(A_I\) is conflict-free, and each excluded argument is attacked by its included partner. This proves a bijection \(I\longleftrightarrow A_I\), without any maximality assumption on \(I\) inside \(G\).

**2. Disagreement encoding.** If \(I,J\) are independent core sets, then the two partners indexed by \(v\) both change membership when \(v\in I\triangle J\), and neither changes otherwise. Thus
\[
|A_I\triangle A_J|=2|I\triangle J|.
\]
Fix \(S=I\triangle J\). The sets \(I\setminus J\) and \(J\setminus I\) partition \(S\) into two independent sets, hence properly two-color the induced graph \(G[S]\). This is possible exactly when \(G[S]\) is bipartite, and then there are \(2^{\kappa(G[S])}\) ordered choices of the two color classes (each connected component, including an isolated vertex, can be flipped independently).

The shared set \(T=I\cap J\) must be independent and have no neighbors in \(S\); conversely any independent set \(T\subseteq V\setminus(S\cup N_G(S))\) can be added to **both** color classes without introducing an edge within either \(I\) or \(J\). Distinct triples \((S,\text{ordered coloring},T)\) give distinct ordered pairs \((I,J)\). This bijection proves the displayed polynomial, including its constant term \(i(G)\).

**3. Maximum and gap-free support.** By the preceding bijection, \(I\triangle J\) always induces a bipartite graph. Thus \(|I\triangle J|\leq n-\tau(G)\). Conversely any induced bipartite subset of maximum size has two independent color classes; taking these as \(I,J\) attains equality. To realize every intermediate size, begin with any such pair and erase any chosen vertex from whichever one of \(I\) or \(J\) contains it. Independence is preserved, while the symmetric difference shrinks by exactly one. Iterating produces pairs of every core disagreement size from zero to \(n-\tau(G)\). Multiplying by two yields the exact even support claimed.

**4. Leading coefficient.** If \(S\) is a largest induced bipartite subset and \(v\in V\setminus(S\cup N_G(S))\), then adding the nonadjacent \(v\) preserves bipartiteness, contradicting maximality. Hence \(V\setminus(S\cup N_G(S))\) is empty for every maximizing \(S\). The shared-set factor in the polynomial is therefore one, leaving exactly the stated sum of powers of two. This argument includes disconnected graphs and graphs with isolated vertices.

## Verification

The accompanying standalone `checker.py` requires only Python 3's standard library. Running `python3 checker.py` independently generates every labelled simple graph on one through five vertices (\(1+2+8+64+1024=1099\) graphs), plus 20 deterministic six-vertex samples. It directly enumerates stable sets in the \(2n\)-vertex attack graph, compares them to the independent-set normal form, enumerates their ordered-pair distances, independently computes the bipartite-subgraph formula, and checks the largest-distance coefficient. All 1,119 checks passed. The full arbitrary-order identity is established by the preceding proof, not inferred from enumeration.

As additional exact calibrations, when \(G=K_n\) with \(n\ge2\), the polynomial is
\[
D_{K_n}(t)=(n+1)+2nt^2+n(n-1)t^4.
\]
For a cycle of odd length \(n\ge3\), the maximum diversity is \(2(n-1)\), attained by \(2n\) ordered extension pairs. For an even cycle \(n\ge4\), maximum diversity is \(2n\), attained by two ordered pairs.

## Relationship to prior work

Fichte, Hecher, Mahmood and Wang (2026, arXiv:2605.13332v1) introduce symmetric-difference extension diversity and analyze decision and exact-maximal-value complexity for general argumentation frameworks. Their full preprint, including the complexity-reduction appendix, gives no leaf-paired graph disagreement polynomial, gap-free support theorem, or odd-cycle-transversal formula. Their symmetric shadow-copy reduction has different attack edges from the pendant/fallback construction used here.

Coste-Marquis, Devred and Marquis (2005) establish that stable, preferred and naive semantics coincide for symmetric attack frameworks. This known result underlies the general symmetric-attack interpretation here but does not supply the distance polynomial. Galby, de Lima, Munaro and Nikabadi (2026, arXiv:2609.30900) study odd-cycle transversals and maximum induced bipartite subgraphs; their graph optimization results motivate the precise parameter appearing at the disagreement endpoint. Earlier work on corona independence polynomials, including Levit and Mandrescu (2013), counts independent sets but does not in the inspected description enumerate pairwise stable-extension distances. The claim is the combined all-distances representation and sharp leading term for this argumentation construction, **not** the novelty of the component combinatorial notions.

## Limitations

This theorem is restricted to symmetric attacks with exactly one private fallback leaf per core vertex; it makes no statement about arbitrary attack frameworks or asymmetric attack edges. The complete polynomial is finite but can require exponentially many terms to compute from its subset sum. Determining its degree exactly is at least as hard as odd-cycle transversal on unrestricted input graphs; no fast algorithm for general graphs is claimed. General two-replica hard-core partition-function representations could encode the same polynomial, and an equivalent earlier enumeration under different terminology remains a priority risk. The 2026 odd-cycle-transversal work was compared at abstract and stated-result level rather than line-by-line throughout its full text. No independent audit or priority certification has been performed.

## References

1. J. K. Fichte, M. Hecher, Y. Mahmood, and Z. Wang, *Diversity of Extensions in Abstract Argumentation*, arXiv:2605.13332v1, first submitted 2026-05-13; https://arxiv.org/abs/2605.13332.
2. S. Coste-Marquis, C. Devred, and P. Marquis, *Symmetric Argumentation Frameworks*, ECSQARU 2005; https://www.cril.univ-artois.fr/~coste/Articles/coste-etal-ecsqaru05.pdf.
3. E. Galby, P. T. de Lima, A. Munaro, and A. Nikabadi, *Odd Cycle Transversal on H-free graphs*, arXiv:2609.30900v1, 2026-09-25; https://arxiv.org/abs/2609.30900.
4. V. E. Levit and E. Mandrescu, *On f-Symmetries of the Independence Polynomial*, arXiv:1303.2564v1, 2013-03-11; https://arxiv.org/abs/1303.2564.
