# Odd-cycle parity obstruction for radical anticommuting pairs in truncated quiver algebras

## Finding

Let \(Q\) be a finite quiver, possibly with loops and parallel arrows, and \(A=kQ/J_Q^3\), where \(k=\mathbb F_q\) and \(J_Q\) is the arrow ideal of the path algebra. Write \(J\) for its image in \(A\). Let \(C_Q(q)\) and \(H_Q(q)\) be the counts of ordered pairs \((x,y)\in J\times J\) such that \(xy-yx=0\) and \(xy+yx=0\), respectively. Write \(E=Q_1\) and let \(p\) be the number of ordered composable pairs of individual arrows. The undirected transition graph \(G_Q\) has vertex set \(E\) and an edge between two arrows if they compose in either order, including a loop at any arrow that composes with itself. For \(S\subseteq E\), let \(b(S)\) and \(o(S)\) count the bipartite and nonbipartite connected components of \(G_Q[S]\), with a loop making its component nonbipartite. Isolates are bipartite components and both counts vanish for the empty support.

For odd \(q\), the anticommuting count is
\[
H_Q(q)=q^{2p}\sum_{S\subseteq E}(q-1)^{|S|}(q+1)^{b(S)}2^{o(S)}.
\]
In particular, \(H_Q(q)=C_Q(q)\) if and only if \(G_Q\) is bipartite; otherwise \(H_Q(q)<C_Q(q)\) for every odd prime power. In characteristic two the equations coincide for all quivers. If \(G_Q\) is bipartite, the commuting and anticommuting equations are identified by a linear change of variables over any field.

The comparison uses the **known** commuting census [1], reproduced below as an input and not as a new quiver-to-graph identification.

## Proof

An element of \(J\) has independent arrow and length-two-path coefficients. Write the arrow coefficients of \(x,y\) as \(a_e,b_e\). Since \(J^3=0\), the two sets of length-two coefficients contribute an entirely free factor \(q^{2p}\), and the coefficient of each composable path \(ef\) in \(xy+yx\) is \(a_e b_f+b_e a_f\). Path basis vectors are indexed by arrow identities, so there is no cancellation between distinct paths with the same endpoints.

On a fixed support \(S=\{e:(a_e,b_e)\neq(0,0)\}\), each nonzero vector determines a projective point \(L_e=[a_e:b_e]\); a choice of points has \((q-1)^{|S|}\) vector lifts. An equation involving an unsupported arrow is automatic. On each supported transition edge the anticommuting equation is precisely \(L_f=\tau(L_e)\) with \(\tau([a:b])=[a:-b]\). This remains true for loops and either composable order. A connected bipartite component propagates an arbitrary one of the \(q+1\) points according to parity. A connected nonbipartite component forces that point equal to its image under \(\tau\), by an odd cycle or loop. In odd characteristic exactly the two coordinate points are fixed; either provides a consistent assignment on the component. Taking the product over components and summing over supports proves the formula.

For the known commuting census [1], the path equations instead impose equality \(L_e=L_f\) and give \(C_Q(q)=q^{2p}\sum_{S\subseteq E}(q-1)^{|S|}(q+1)^{b(S)+o(S)}\). Loops make no difference to this sum because they do not change its component counts. This is an evaluation of the induced-subgraph component polynomial [2]. In odd characteristic each support contribution to \(C_Q(q)-H_Q(q)\) is nonnegative because \(q+1>2\). If the full transition graph is nonbipartite, the full support contribution is strictly positive. If it is bipartite, all induced supports are bipartite and the sums agree. For the linear identification pick signs \(\epsilon_e=\pm1\) opposite on adjacent vertices. The invertible substitution \(b_e\mapsto\epsilon_e b_e\) in the commuting equations gives nonzero scalar multiples of the anticommuting equations, with the length-two coefficients unchanged. In characteristic two the signs coincide and the identity suffices.

## Acyclic witness

In the displayed order, take the seven arrows \(0\to1,1\to2,2\to4,1\to3,3\to5,5\to4,4\to6\). The directed quiver is acyclic, while the arrow indices numbered from zero give the transition cycle \(0,1,2,6,5,4,3,0\), with no other edges and \(p=7\). Every proper induced support is bipartite, so the full support is the only contributor to the deficit: for odd \(q\),
\[
C_Q(q)-H_Q(q)=q^{14}(q-1)^8.
\]
For the oriented three-cycle the same reasoning gives \(q^6(q-1)^4\). Thus directed acyclicity alone cannot replace the bipartiteness criterion.

## Reproducibility and scope

The companion `check_pair_census.py` compares the path equations on arrow coordinates with the support formulas for finitely many quiver/field instances, including \(\mathbb F_4\); it uses the free factor for length-two coordinates. Its two odd-cycle deficit checks at \(q=3,5\) are algebraic checks of the formulas, not direct exhaustion of the seven-arrow odd-field instance. The all-quiver statement is proved above. The counts are of labelled ordered pairs in \(J\), not of elements of the full algebra, orbits, or similarity classes. No nonbipartite scheme or component classification is claimed.

## Relationship to prior work

The transition-graph reduction and support formula for commuting pairs were already given in [1]. The new comparison is for anticommutation in the fixed radical: an involution replaces equality on supported edges, so odd cycles restrict the component labels to the fixed points. This is a graph-homomorphism constraint with a target consisting of two looped points and disjoint two-vertex edges (one for each nontrivial involution orbit). The contribution is its application to count radical anticommuting pairs, the sharp odd-characteristic equality criterion, and the acyclic witness, not the component polynomial or a general signed-coloring theorem. Partly anti-commutative quiver algebras [3] concern anti-commutativity as a relation in a defining ideal rather than pairs satisfying a zero anticommutator in \(kQ/J_Q^3\). These distinctions do not assert universal historical priority.

## References

1. *Composability graphs determine radical commutator-rank spectra in truncated path algebras*, [RESULT.md](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-composability-graphs-determine-radical-commutator-rank-spectra-i--003c97167e0e/RESULT.md).
2. P. Tittmann, I. Averbouch, and J. A. Makowsky, *The enumeration of vertex induced subgraphs with respect to the number of components*, [arXiv:0812.4147](https://arxiv.org/abs/0812.4147).
3. E. Gawell and Q. Richey Xantcha, *Centers of partly (anti-)commutative quiver algebras and finite generation of Hochschild cohomology ring*, [arXiv:1504.00582](https://arxiv.org/abs/1504.00582).
