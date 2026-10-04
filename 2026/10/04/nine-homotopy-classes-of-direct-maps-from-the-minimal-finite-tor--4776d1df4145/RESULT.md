# Nine homotopy classes of direct maps from the minimal finite torus to the four-point circle
## Finding
Let \(C\) be the four-point minimal finite circle, with two minimal points, two maximal points, and every minimal point below every maximal point. Let \(T=C\times C\) have the coordinatewise order. Then the finite mapping poset \(\operatorname{Map}(T,C)\), ordered pointwise, has exactly \(2836\) elements and exactly nine connected components.

One component has \(2828\) maps. It contains all four constant maps and consists exactly of those maps inducing the zero homomorphism on \(H_1(T;\mathbb Z)\cong\mathbb Z^2\). The remaining eight components are singletons. Their maps are precisely
\[
\alpha\circ\pi_i,\qquad i\in\{1,2\},\quad \alpha\in\operatorname{Aut}(C),
\]
where \(\pi_i:T\to C\) is a coordinate projection. Therefore
\[
\lvert[T,C]\rvert=9.
\]
In the basis of \(H_1(T;\mathbb Z)\) supplied by the two circle factors, the induced homomorphisms are exactly
\[
(0,0),\quad (1,0),\quad (-1,0),\quad (0,1),\quad (0,-1).
\]
The zero homomorphism is represented by the single \(2828\)-map homotopy component, while each nonzero homomorphism is represented by two distinct singleton homotopy classes.

## Assumptions and scope
The source is the product model \(T=C\times C\), the standard sixteen-point finite torus obtained as the product of two four-point minimal finite circles. The target is the same four-point circle \(C\). Continuous maps between finite \(T_0\)-spaces are identified with order-preserving maps between their specialization posets, and the compact-open mapping-space order is the pointwise order.

The statement concerns direct maps from this unsubdivided source. It does not assert that these nine classes exhaust classical homotopy classes after subdivision, nor does it concern the other sixteen-point minimal finite torus model.

## Proof
Write the two minimal target points as \(0,1\) and the two maximal target points as \(2,3\). For an order-preserving map \(f:T\to C\), put
\[
D=f^{-1}(\{0,1\}).
\]
Because \(\{0,1\}\) is a down-set in \(C\), \(D\) is an order ideal of \(T\). If two points of \(D\) are joined by a comparability edge, order preservation forces them to have the same image, since the two minimal target points are incomparable. Thus \(f\) is constant on each comparability-connected component of \(D\). The same argument applied to \(T\setminus D\) shows that \(f\) is constant on each comparability-connected component of the complement, now with value in \(\{2,3\}\).

Conversely, every order ideal \(D\subseteq T\), together with an arbitrary choice of one of the two minimal target points on each comparability-connected component of \(D\) and one of the two maximal target points on each comparability-connected component of \(T\setminus D\), determines an order-preserving map. Hence, if \(c(D)\) and \(c(T\setminus D)\) denote the corresponding numbers of comparability components,
\[
\lvert\operatorname{Map}(T,C)\rvert
 =\sum_{D\text{ an order ideal}}2^{c(D)+c(T\setminus D)}.
\]
There are exactly \(430\) order ideals. Their component-count profile is
\[
\begin{array}{c|rrrrrrrrrr}
(c(D),c(T\setminus D))&(0,1)&(1,0)&(1,1)&(1,2)&(1,3)&(1,4)&(2,1)&(2,2)&(3,1)&(4,1)\\
\hline
\#D&1&1&228&82&16&1&82&2&16&1.
\end{array}
\]
Substitution gives \(2836\) maps.

It remains to identify homotopy components. Two comparable maps lie in the same component of the mapping poset. Moreover, if \(f<g\), choose a maximal source point \(x\) among those with \(f(x)\ne g(x)\). Replacing only \(f(x)\) by \(g(x)\) remains order preserving: below \(x\) the inequalities factor through \(f(x)\le g(x)\), while above \(x\) maximality of \(x\) in the difference set gives \(f(z)=g(z)\). Iterating decomposes every comparability step into valid one-coordinate raises. Thus mapping-poset components are exactly the components of the graph whose edges are valid one-coordinate raises.

Exhaustion of this finite graph yields one component of size \(2828\) and eight singleton components. The singleton maps are exactly the eight maps \(\alpha\circ\pi_i\) with \(i\in\{1,2\}\) and \(\alpha\in\operatorname{Aut}(C)\). Since \(\operatorname{Aut}(C)\cong S_2\times S_2\), there are four target automorphisms for each projection.

To distinguish the components homologically, orient the standard four-edge cycle in the order complex of \(C\) and evaluate the induced one-cycle against a fixed integral edge cocycle. Restricting a map to the two factor-circle slices gives its two coefficients on \(H_1(T;\mathbb Z)\cong\mathbb Z^2\). The exhaustive calculation gives the exact profile
\[
(0,0):2828,\qquad
(1,0):2,\qquad
(-1,0):2,\qquad
(0,1):2,\qquad
(0,-1):2.
\]
All four constant maps lie in the \(2828\)-map component, so that component is null-homotopic and every map in it induces zero on first homology. The eight isolated maps have precisely the four displayed nonzero homology maps, two representatives for each. This proves the classification.

## Verification
The accompanying `verify.py` reconstructs \(C\) and \(T\) from their orders. It performs two independent counts of maps: recursive enumeration of all order-preserving functions and the order-ideal weighted sum above. It then constructs the one-coordinate-raise graph, checks the complete component-size multiset, computes the induced first-homology coefficient pair for every map, and checks that the isolated maps are exactly the projection-after-automorphism maps.

A replay from the packaged bytes terminates with:

`VERIFY_OK maps=2836 ideals=430 components=2828+8x1 degree_profile=2828,2,2,2,2 isolated=8_projections`

The finite enumeration is a complete verification of this particular mapping poset. The conceptual order-ideal argument and one-coordinate-raise lemma explain why the enumerated objects and edges are exactly the required maps and homotopies.

## Relationship to prior work
Barmak and Minian develop minimal finite models and the four-point minimal circle model. Cianci and Ottina identify the product of two such circles as one of the sixteen-point minimal finite torus models. May's finite-space notes state that homotopy classes of maps can be read from connected components of the finite function space and emphasize that finite models may have too few direct maps, with subdivision needed to recover general classical maps.

Those structural results do not determine the present mapping-poset cardinality, its nine components, or the exact induced-homology profile. The result makes the general scarcity phenomenon quantitative for a canonical finite torus: classically, maps from the torus to the circle are classified by \(H^1(T^2;\mathbb Z)\cong\mathbb Z^2\), whereas the unsubdivided finite model realizes only zero and the four signed coordinate classes, with each nonzero induced homomorphism split into two finite-space homotopy classes.

## Limitations
The theorem is specific to the product sixteen-point torus model and the four-point circle. It does not determine the mapping space from the other sixteen-point minimal torus model, does not determine the minimum subdivision depth needed to realize a prescribed classical cohomology class, and does not claim a general formula for products of larger finite circle models.

The originality comparison included a bibliographic-level check of Stong's foundational finite-space paper, but the full paper was not available through the inspected access path. This leaves a residual possibility of an unindexed historical special-case computation, although the detailed accessible finite-space sources inspected do not state the present classification.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1, first public 2006-11-06.
2. N. Cianci and M. Ottina, *Poset splitting and minimality of finite models*, arXiv:1512.06088v1, first public 2015-12-18.
3. J. P. May, *Finite Spaces and Simplicial Complexes*, notes dated Summer 2003 and later revised.
4. R. E. Stong, *Finite topological spaces*, Transactions of the American Mathematical Society 123 (1966), DOI 10.1090/S0002-9947-1966-0195042-2.
