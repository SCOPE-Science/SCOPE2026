# Exact weak-endpoint maximal inequalities on crown graphs

## Finding

Let \(n\ge3\), and let \(\mathrm{Cr}_n\) be the *crown graph* obtained from the complete bipartite graph \(K_{n,n}\) by deleting the edges of a perfect matching. Give vertices counting measure and their unweighted shortest-path metric. For every function \(f\) on its \(2n\) vertices, the centered Hardy–Littlewood maximal operator \(M_n\) satisfies the sharp weak-type inequality
\[
\sup_{t>0}t\,\#\{v:M_nf(v)>t\}\le \frac{2(n-1)}n\sum_v|f(v)|.
\]
Equivalently, using decreasing rearrangement, \(\|M_n\|_{\ell^1\to\ell^{1,\infty}}=2(n-1)/n\). The bound is attained in the rearrangement-quasinorm formulation by mass distributed uniformly across either bipartition class.

In contrast, for the same vertex set with the deleted matching restored,
\[
\|M_{K_{n,n}}\|_{\ell^1\to\ell^{1,\infty}}=\frac{2n}{n+1},\qquad
\|M_{K_{n,n}}\|-\|M_n\|=\frac2{n(n+1)}.
\]
Thus deleting one perfect matching produces a strict, explicitly quantified reduction in the sharp weak-endpoint amplification.

## Assumptions and scope

All graphs are finite, simple, unweighted, and have counting measure. Label the two bipartition classes \(A_1,\ldots,A_n\) and \(B_1,\ldots,B_n\), with \(A_i\) adjacent precisely to \(B_j\) for \(j\ne i\). For a center \(v\), the graph ball \(B(v,r)\) consists of vertices at graph distance at most \(r\), including \(v\) itself. Define \(Mf(v)=\max_{r\ge0}|B(v,r)|^{-1}\sum_{w\in B(v,r)}|f(w)|\). The weak quasinorm on \(2n\) points is \(\|g\|_{1,\infty}=\max_{1\le k\le2n}k g^*(k)\), with \(g^*\) decreasing rearrangement. It equals \(\sup_{t>0}t\#\{v:|g(v)|>t\}\), interpreted as a supremum (not necessarily an attained strict level). All assertions concern \(n\ge3\); the order-two crown is disconnected.

## Proof

Write \(x_i=|f(A_i)|\), \(y_i=|f(B_i)|\), \(X=\sum_i x_i\), \(Y=\sum_i y_i\), and \(T=X+Y\). We may assume \(T>0\). Crown graph balls have sizes \(1,n,2n-1,2n\). Their four averages at \(A_i\) are
\[
x_i,\quad \frac{x_i+Y-y_i}{n},\quad \frac{T-y_i}{2n-1},\quad\frac{T}{2n},
\]
and symmetrically those at \(B_i\) are
\[
y_i,\quad \frac{y_i+X-x_i}{n},\quad \frac{T-x_i}{2n-1},\quad\frac{T}{2n}.
\]
The two radius-one balls centered at a matched pair \(A_i,B_i\) are disjoint and partition the vertices.

Fix a threshold \(t>0\) and let \(k=\#\{v:Mf(v)\ge t\}\). It suffices to show \(kt\le 2(n-1)T/n\), since the threshold can be chosen at any rearrangement coordinate. If \(t\le T/(2n-1)\), the elementary bound \(kt\le 2nT/(2n-1)\le 2(n-1)T/n\) works for \(n\ge3\). Hence assume \(t>T/(2n-1)\), so all covered vertices must be covered by the singleton ball (call these *self-covered*) or the radius-one ball. Assign a vertex to the self-covered class whenever its own value is at least \(t\); all remaining covered vertices are assigned to radius one and necessarily have own value strictly below \(t\).

If no covered vertex is radius-one-only, all covered vertices have their own value at least \(t\), so \(kt\le T\) and the required bound is immediate.

**Radius-one centers on both sides.** If some \(A_i\) and some \(B_j\) are covered only at radius one, then \(x_i<t\), \(x_i+Y-y_i\ge nt\), and likewise \(y_j<t\), \(y_j+X-x_j\ge nt\). Thus \(Y>(n-1)t\), \(X>(n-1)t\), and \(T>2(n-1)t\). For \(n\ge4\),
\[
\frac{kt}{T}<\frac{2n}{2(n-1)}=\frac n{n-1}\le\frac{2(n-1)}n.
\]
For \(n=3\), the same estimate works whenever \(k\le5\), since \(kt/T<5/4<4/3\). When \(n=3,k=6\), every matched pair is covered at both vertices. Both members of a matched pair cannot be radius-one-only, because their complementary radius-one balls would give \(T\ge2nt\), contradicting \(T<(2n-1)t\). Thus the partner \(B_i\) of a radius-one-only \(A_i\) is self-covered, so \(y_i\ge t>x_i\); the radius-one inequality at \(A_i\) forces \(Y>nt\). Analogously the partner of a radius-one-only \(B_j\) forces \(X>nt\), an impossibility. This completes the mixed-side case.

**Radius-one centers on one side only.** By symmetry suppose they are \(B_i\) with indices in a nonempty set \(H\) of cardinality \(h\). Let \(U\) be the self-covered \(A\)-indices (cardinality \(r\)), and let \(V\) be the self-covered \(B\)-indices (cardinality \(b\)). Here \(H\cap V=\varnothing\), \(r\le n\), \(h+b\le n\), and \(k=r+h+b\).

There is a mass-preserving simplification. For each \(i\in H\), move any mass \(y_i\) to a vertex \(A_j\) with \(j\ne i\); the radius-one sum at \(B_i\) is unchanged, and that at every other \(B\)-center can only increase. At each \(i\in V\), retain mass \(t\) and move the excess to the \(A\)-side; it does not contribute to the radius-one sums of the selected \(B\)-centers, because \(V\cap H=\varnothing\). Move any remaining \(B\)-mass to the \(A\)-side. All selected coverage conditions survive, the total mass stays \(T\), and now the \(B\)-side has value exactly \(t\) on \(V\) and zero elsewhere. Consequently, for the modified nonnegative \(A\)-values \(x_i\),
\[
T=X+bt,\qquad x_i\ge t\ \ (i\in U),\qquad X-x_i\ge nt\ \ (i\in H).
\]
In particular \(X\ge nt\). If \(k\le2n-2\), immediately \(kt/T\le(2n-2)/n\).

If \(k=2n-1\) and \(b\ge1\), then \(T\ge(n+1)t\). If \(b=0\), the inequalities \(r+h=2n-1\), \(r,h\le n\) imply \(U\cap H\ne\varnothing\). Any \(i\) in that intersection satisfies \(x_i\ge t\) and \(X-x_i\ge nt\), again giving \(T=X\ge(n+1)t\). In either case \(kt/T\le(2n-1)/(n+1)\le2(n-1)/n\).

If \(k=2n\), then \(r=n\) and \(h+b=n\). When \(b\ge1\), choose \(i\in H\). Since \(i\in U\), the same two inequalities yield \(X\ge(n+1)t\), hence \(T\ge(n+2)t\) and \(kt/T\le 2n/(n+2)\le2(n-1)/n\). When \(b=0\), all \(B\)-vertices are radius-one-covered and all \(A\)-vertices self-covered. Sum \(X-x_i\ge nt\) over all \(i\): \((n-1)X\ge n^2t\). Thus \(T=X\ge n^2t/(n-1)\), and \(kt/T\le2(n-1)/n\). This proves the upper bound in every case.

For sharpness set \(x_i=1/n\) and \(y_i=0\). Then \(T=1\), all \(A\)-vertices satisfy \(Mf(A_i)\ge1/n\), and every \(B\)-vertex has \(Mf(B_i)=(n-1)/n^2\). The weak quasinorm is at least \(2n(n-1)/n^2=2(n-1)/n\), as required.

Finally, in \(K_{n,n}\) every nontrivial proper ball has \(n+1\) vertices, and the whole ball has \(2n\). If \(t>T/(n+1)\), only singleton averages can reach \(t\), whence \(kt\le T\). Otherwise \(kt\le 2nT/(n+1)\). Uniform mass on one bipartition attains the latter sharp factor. Subtracting the two rational constants yields \(2/[n(n+1)]\).

## Verification

The included `verify.py` independently constructs both graph metrics by breadth-first search rather than relying on the displayed ball formulas. It computes all four possible graph-ball averages using exact rational arithmetic and confirms the extremal examples and the rational difference for orders \(3\) through \(13\). It also checks the matched-pair ball partition, tests 550 deterministic rational random vectors at each order \(3\) through \(18\), and exhaustively tests integer compositions of total mass ten on six vertices and total mass seven on eight vertices. In its recorded execution, all 15,796 assertions passed. These finite tests provide reproducibility checks; the universal result is proved by the case analysis above.

## Relationship to prior work

Soria and Tradacete (2014) define this centered graph maximal operator, calculate general strong-type bounds, and prove geometric weak-type estimates via dilation and overlap indices. Their full arXiv text, particularly the weak-type section, does not supply the exact crown-graph weak constant. The general overlap bound gives no immediate equality with the strict factor here. González-Riquelme and Madrid (2020), in two related preprints, focus on variation inequalities and strong-type norms for complete and star graphs, not the present exact weak endpoint on matching-deleted balanced bicliques. Graph-metric and crown-graph results with different invariants do not imply the stated distribution-function estimate. The possible existence of an equivalent older formula under cycle or neighborhood-averaging terminology remains an originality risk.

## Limitations

No claim is made for arbitrary deletion patterns, unequal bipartition sizes, weighted vertices, noncentered balls, or strong-type \(\ell^p\) norms. The sharp result is specific to uniform counting measure, integer graph-distance balls and \(n\ge3\). The comparison with the complete bipartite graph concerns sharp operator constants, not pointwise ordering of the two maximal operators for every input. Bibliographic priority is provisional; no independent mathematical or bibliographic audit has been performed.

## References

1. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204 (first public 2014-10-22), especially Section 4 on weak-type estimates. https://arxiv.org/abs/1410.6204
2. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146 (2020). https://arxiv.org/abs/2005.03146
3. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630 (2020). https://arxiv.org/abs/2011.02630
