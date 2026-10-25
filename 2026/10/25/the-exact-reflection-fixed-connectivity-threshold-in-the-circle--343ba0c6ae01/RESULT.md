# The exact reflection-fixed connectivity threshold in the circle Rips filtration

## Finding

Let \(S^1=\mathbb{R}/2\pi\mathbb{Z}\) carry its geodesic distance, and let \(K_r=\operatorname{VR}_{<r}(S^1)\) be the abstract simplicial complex whose simplices are finite subsets of diameter strictly less than \(r\). Let \(C_2=\{1,\rho\}\) act by reflection \(\rho(\theta)=-\theta\). For every \(r>0\), the geometric fixed-point locus \(|K_r|^{C_2}\) is disconnected exactly when

\[
0<r\leq \frac{2\pi}{3},
\]

and is connected for every \(r>\frac{2\pi}{3}\). In particular, when \(0<r\leq 2\pi/3\), the equivariant path fibration has no equivariant path from the fixed vertex \(0\) to the fixed vertex \(\pi\); under the standard definition, \(\operatorname{TC}_{C_2}(|K_r|)=\infty\). No value of equivariant topological complexity is asserted on the connected side.

## Assumptions and scope

The circle has circumference \(2\pi\), the action is the reflection \(\theta\mapsto-\theta\), and the Rips convention is strict: a finite vertex set is a simplex precisely when its diameter is \(<r\). The geometric realization is taken with its usual simplicial topology. The statement concerns connectivity of the fixed-point locus, not the full equivariant homotopy type of \(|K_r|\). The strict inequality matters at the threshold \(r=2\pi/3\).

## Proof

Write \(p=0\) and \(q=\pi\) for the two fixed vertices. Every nonfixed vertex belongs to an orbit \(O_\theta=\{\theta,-\theta\}\), with \(0<\theta<\pi\). The orbit contributes a vertex to the fixed-point cell structure exactly when \(\{\theta,-\theta\}\) is a simplex, namely when

\[
2\min\{\theta,\pi-\theta\}<r.
\]

Thus every such orbit is of one of two types: a low orbit with \(\theta<r/2\), or a high orbit with \(\theta>\pi-r/2\). The fixed-point part of an invariant simplex is the simplex spanned by the barycentres of its vertex orbits. Consequently, connectivity of \(|K_r|^{C_2}\) is determined by the graph whose vertices are \(p,q\) and the admissible orbit barycentres, with an edge whenever the union of the corresponding orbits is a simplex of \(K_r\).

Every low orbit is joined to \(p\), because \(\{0,\theta,-\theta\}\) has diameter \(2\theta<r\). Every high orbit is joined to \(q\), because \(\{\pi,\theta,-\theta\}\) has diameter \(2(\pi-\theta)<r\). The fixed vertices \(p,q\) are not joined directly when \(r\leq2\pi/3\), since their distance is \(\pi\).

Now take a low orbit parameter \(\theta<r/2\) and a high orbit parameter \(\phi>\pi-r/2\). The two cross-distances between the orbits equal

\[
\min\{\theta+\phi,2\pi-\theta-\phi\},
\]

and each is strictly greater than \(\pi-r/2\). If \(r\leq2\pi/3\), then \(\pi-r/2\geq r\), so no simplex can contain both a low and a high orbit. Hence there is no edge between the two orbit types. All fixed-point cells belong to the component of \(p\) or the component of \(q\), and these components are distinct. This proves disconnection for \(0<r\leq2\pi/3\), including equality.

Conversely, suppose \(2\pi/3<r\leq\pi\). Choose

\[
0<\theta<\min\left\{\frac r2,\frac{3r}{2}-\pi\right\}
\]

and then choose \(\phi\) with

\[
\pi-\frac r2<\phi<r-\theta.
\]

These intervals are nonempty because \(r>2\pi/3\). The orbit vertices \(O_\theta,O_\phi\) exist. The sets \(\{0,\theta,-\theta\}\) and \(\{\pi,\phi,-\phi\}\) are simplices, and \(O_\theta\cup O_\phi=\{\theta,-\theta,\phi,-\phi\}\) is a simplex: the within-orbit distances are below \(r\), while the cross-distances are bounded by \(\theta+\phi<r\) and \(\phi-\theta<r\). Therefore the fixed-point graph contains the path

\[
p\;--\;O_\theta\;--\;O_\phi\;--\;q.
\]

Every low orbit is joined to \(p\), every high orbit is joined to \(q\), and the displayed path joins those two components. The fixed-point locus is connected. Finally, if \(r>\pi\), every finite subset of the circle has diameter \(<r\), so \(K_r\) is a full simplex and its fixed-point locus is contractible. This completes the proof for all \(r>2\pi/3\).

For the equivariant topological-complexity consequence, an equivariant path between fixed endpoints must remain in the fixed-point locus. When that locus has separate components containing \(p\) and \(q\), no such path exists, so the equivariant path fibration cannot admit a section cover of the whole product.

## Verification

The threshold and its equality case follow from strict distance inequalities, not finite sampling. The lower-side cross-distance estimate is \(d>\pi-r/2\geq r\) for \(r\leq2\pi/3\); the upper-side construction uses a nonempty pair of open intervals when \(r>2\pi/3\). No numerical experiment is used as an infinite proof. The proof does not classify the homotopy type of the fixed-point locus or the value of \(\operatorname{TC}_{C_2}\) for \(r>2\pi/3\).

## Relationship to prior work

The recent framework for equivariant persistent topological complexity studies reflection actions on Vietoris–Rips filtrations of spheres, while the foundational equivariant topological-complexity literature explains why disconnected fixed-point sets obstruct equivariant motion planning. Neither inspected source states the exact \(2\pi/3\) transition for the reflection-fixed locus of the continuous circle's Rips filtration. The present statement supplies that geometric threshold; it does not claim a new classification of the non-equivariant homotopy types of circle Rips complexes.

## Limitations

The result uses the geodesic metric on the full continuous circle and the strict-diameter Rips convention. It does not automatically transfer to finite samples, chordal distance, or a convention using diameter \(\leq r\). It determines fixed-point connectivity and the resulting infinite-value obstruction only; it does not determine equivariant homotopy types or finite values of equivariant topological complexity on the connected side.

## References

1. N. Daundkar, A. Sarkar, and B. Singh, “Equivariant persistence topological complexity,” arXiv:2609.29759 (first posted 2026-09-24), especially the discussion of equivariant persistent invariants and the reflection-sphere examples.
2. H. Colman and M. Grant, “Equivariant topological complexity,” *Algebraic & Geometric Topology* 12 (2012), no. 4, 2299–2316; arXiv:1205.0166; DOI: 10.2140/agt.2012.12.2299, Example 5.9.
