# Exact arboricity of joins of pseudotrees

## Result

Let \(G\) and \(H\) be finite simple connected pseudoforests (pseudotrees), of orders \(m\) and \(n\). Thus each factor is either a tree or a connected unicyclic graph. Put
\[
\varepsilon_G=|E(G)|-m+1\in\{0,1\},\qquad
\varepsilon_H=|E(H)|-n+1\in\{0,1\}.
\]
For a graph \(X\), write
\[
\gamma(X)=\max_{S\subseteq V(X),\ |S|\ge2}
\frac{|E(X[S])|}{|S|-1}
\]
for its Nash--Williams density. Then the full vertex set is density-maximizing in the join:
\[
\boxed{
\gamma(G*H)=
\frac{mn+m+n-2+\varepsilon_G+\varepsilon_H}{m+n-1}.
}
\]
Consequently the classical arboricity \(a\), and the reduced arboricity \(\operatorname{arb}=a-1\) used in Kuanyshov--Yeginbay (2026), are
\[
\boxed{
a(G*H)=
\left\lceil
\frac{mn+m+n-2+\varepsilon_G+\varepsilon_H}{m+n-1}
\right\rceil,
}
\]
\[
\boxed{
\operatorname{arb}(G*H)=
\left\lceil
\frac{mn+m+n-2+\varepsilon_G+\varepsilon_H}{m+n-1}
\right\rceil-1.
}
\]
In particular, the answer depends only on the two orders and on whether each factor contains a cycle, not on the shapes of the attached trees.

Equivalently, the three cases are
\[
\begin{array}{c|c}
\text{factors}&\gamma(G*H)\\ \hline
\text{tree, tree}&\dfrac{mn+m+n-2}{m+n-1}\\[2mm]
\text{tree, unicyclic}&\dfrac{mn+m+n-1}{m+n-1}\\[2mm]
\text{unicyclic, unicyclic}&\dfrac{mn+m+n}{m+n-1}.
\end{array}
\]

The join is also 1-balanced (uniformly dense in the graph-matroid sense): no connected subgraph has larger edge/rank density than the whole graph.

## Proof

It is enough in the Nash--Williams maximum to consider induced subgraphs, since adding available edges on a fixed vertex set can only increase the quotient. Let \(S=X\sqcup Y\), where \(X\subseteq V(G)\), \(Y\subseteq V(H)\), and put \(x=|X|\), \(y=|Y|\).

For every nonempty \(X\), a tree satisfies
\[
|E(G[X])|\le x-1,
\]
while a connected unicyclic graph, being a pseudoforest, satisfies
\[
|E(G[X])|\le x.
\]
Hence, whenever \(x,y\ge1\), with \(d=\varepsilon_G+\varepsilon_H\),
\[
|E((G*H)[S])|
=xy+|E(G[X])|+|E(H[Y])|
\le xy+x+y-2+d.
\]
Define
\[
\phi_d(x,y)=\frac{xy+x+y-2+d}{x+y-1}.
\]
A direct discrete difference gives
\[
\phi_d(x+1,y)-\phi_d(x,y)
=
\frac{y^2-y+1-d}{(x+y)(x+y-1)},
\]
and symmetrically
\[
\phi_d(x,y+1)-\phi_d(x,y)
=
\frac{x^2-x+1-d}{(x+y)(x+y-1)}.
\]

If \(d\le1\), both differences are nonnegative for all positive \(x,y\). Therefore every induced subgraph meeting both factors has density at most \(\phi_d(m,n)\), which is exactly the density of the full join because the edge counts of the two whole pseudotrees attain their respective bounds.

If \(d=2\), both factors are unicyclic and hence \(m,n\ge3\). For \(x,y\ge2\), both differences are positive, since \(y^2-y-1\ge1\) and likewise for \(x\). If \(x=1\), the crude unicyclic bound above overcounts the one-vertex internal graph: in fact \(|E(G[X])|=0\), so
\[
|E((G*H)[S])|\le y+y=2y,
\qquad
\frac{|E((G*H)[S])|}{|S|-1}\le2.
\]
The same holds when \(y=1\). But
\[
\phi_2(m,n)=\frac{mn+m+n}{m+n-1}>2
\qquad(m,n\ge3),
\]
so these boundary cases also cannot beat the whole graph.

It remains to consider a set contained entirely in one factor. A tree subgraph has density at most \(1\). A connected unicyclic subgraph is either a tree or has \(v\ge3\) vertices and at most \(v\) edges, hence density at most \(v/(v-1)\le3/2\). The full join density is at least \(1\) in the tree--tree case, at least \(2\) when exactly one factor is unicyclic, and greater than \(2\) when both are unicyclic. Thus a one-factor subgraph cannot be denser either. This proves the displayed formula for \(\gamma(G*H)\), and Nash--Williams gives the arboricity formulas by taking a ceiling.

For 1-balancedness in the usual matroid-rank definition, it suffices to check connected subgraphs: the density of a disconnected subgraph is a rank-weighted average of the densities of its nontrivial components. The connected cases are exactly those bounded above, so the whole join is 1-balanced.

## Extension: joining a pseudotree to an independent set

Let \(G\) be a pseudotree of order \(m\), let \(\varepsilon_G\in\{0,1\}\) be as above, and let \(\overline K_n\) be an independent set with \(n\ge1\). Then again the whole join is Nash--Williams density-maximizing and
\[
\boxed{
\gamma(G*\overline K_n)=
\frac{mn+m-1+\varepsilon_G}{m+n-1},
}
\]
so
\[
\boxed{
\operatorname{arb}(G*\overline K_n)=
\left\lceil\frac{mn+m-1+\varepsilon_G}{m+n-1}\right\rceil-1.
}
\]

Indeed, for \(x\ge1\) selected vertices of \(G\) and \(y\ge1\) selected vertices of the independent side,
\[
|E|\le xy+x-1+\varepsilon_G.
\]
Writing
\[
\psi_\varepsilon(x,y)=\frac{xy+x-1+\varepsilon}{x+y-1},
\]
its coordinate differences have numerators \(y^2-\varepsilon\) and \((x-1)^2-\varepsilon\), respectively. For a tree they are always nonnegative. For a unicyclic factor, monotonicity holds once \(x\ge2\); when \(x=1\), the actual internal edge count is zero and the density is exactly \(1\). Subgraphs lying only in \(G\) are bounded as in the preceding proof. Thus the full set is extremal.

This extension simultaneously gives exact formulas for every fan \(K_1*P_m\), every wheel \(K_1*C_m\), every tree joined with an independent set, and every unicyclic graph joined with an independent set. It also recovers the recent computation \(P_4*\overline K_3\): the full density is \(15/6=5/2\), so its classical arboricity is \(3\) and its reduced arboricity is \(2\).

## Simplicial geometric category

Fernández-Ternero, Macías-Virgós, Minuz and Vilches proved that the simplicial geometric category of a connected graph equals its reduced arboricity. Since every nontrivial join above is connected, all of the formulas immediately transfer to \(\operatorname{gscat}\). In particular,
\[
\operatorname{gscat}(G*H)
=
\left\lceil
\frac{mn+m+n-2+\varepsilon_G+\varepsilon_H}{m+n-1}
\right\rceil-1.
\]

## Relation to the literature

Kuanyshov and Yeginbay (arXiv:2609.20606, submitted 17 September 2026) derive general upper and lower bounds for arboricity under graph joins. Their Theorem 23 gives, in their reduced convention,
\[
\max\{\operatorname{arb}(G),\operatorname{arb}(H),B\}
\le \operatorname{arb}(G*H)
\le \operatorname{arb}(G)+\operatorname{arb}(H)+B+1,
\]
where \(B=\lceil mn/(m+n-1)\rceil-1\). The same paper computes complete bipartite graphs, fans, one instance \(P_4*\overline K_3\), and wheels, but does not state an exact formula for joins of arbitrary trees, unicyclic graphs, or pseudotrees. The theorem above turns that bounded regime into a shape-independent exact formula and explains the listed examples through one density mechanism.

Older work of Hobbs, Kannan, Lai, Lai and Weng (2010) studies constructions preserving 1-balancedness, especially generalized Cartesian products built from equal-size modules linked by regular bipartite graphs. Accessible publisher text was inspected and does not state the pseudotree-join formulas above. Some equal-order special cases may nevertheless be obtainable from those more general construction techniques. The complete article was not checked line-by-line, so this is the main residual originality risk. The present originality claim is therefore limited to the explicit arbitrary-order pseudotree join theorem, its unicyclic cases (whose factors need not themselves be 1-balanced), and the independent-set extension, to the best of our knowledge.

Searches also used the synonymous terminology `graph sum`, `complete sum`, `uniformly dense`, `strongly balanced`, and `1-balanced`, in addition to `graph join`, `arboricity`, `fractional arboricity`, `pseudotree`, `pseudoforest`, and `unicyclic`. No source located in those searches stated the formulas above.

## Verification

The accompanying verifier uses NetworkX 3.6.1's graph atlas. It selects every connected tree or unicyclic graph on at most six vertices, forms joins, and exhaustively maximizes \(e(S)/(|S|-1)\) over all vertex subsets. It checks 440 pseudotree-pair instances (with total order at most 11) and 191 pseudotree--independent-set instances; every observed maximum equals the displayed full-graph formula. This finite check supports, but does not replace, the proof.

## Limitations

The theorem treats connected pseudoforests (trees and unicyclic graphs), not arbitrary pseudoforests with several components or connected graphs of larger cyclomatic number. The independent-set extension has only one pseudotree factor. The 2010 1-balanced-construction paper is the principal residual literature risk because only accessible publisher text and theorem excerpts, not a complete line-by-line reading of the article, were inspected. No independent validation or independent audit is asserted.

## References

1. N. Kuanyshov and I. Yeginbay, *Arboricity and Simplicial Geometric Category of Wedges and Joins of Graphs*, arXiv:2609.20606 (2026). https://arxiv.org/abs/2609.20606
2. C. St. J. A. Nash-Williams, *Decomposition of finite graphs into forests*, Journal of the London Mathematical Society 39 (1964), 12. https://doi.org/10.1112/jlms/s1-39.1.12
3. D. Fernández-Ternero, E. Macías-Virgós, E. Minuz and J. A. Vilches, *Simplicial Lusternik--Schnirelmann category*, Publicacions Matemàtiques 63 (2019), 265--293. https://doi.org/10.5565/PUBLMAT6311909
4. A. M. Hobbs, L. Kannan, H.-J. Lai, H. Lai and G. Weng, *Balanced and 1-balanced graph constructions*, Discrete Applied Mathematics 158 (2010), 1511--1523. https://doi.org/10.1016/j.dam.2010.05.004
