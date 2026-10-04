# A sharp half-order bound for Sylvester--Gallai dimension of connected graphs
## Finding
For every finite connected simple graph \(G\) on \(n\ge 3\) vertices,
\[
\operatorname{SGdim}(G)\le \left\lfloor\frac{n-1}{2}\right\rfloor.
\]
The bound is sharp at every order. In fact, every tree \(T\) on \(n\ge3\) vertices satisfies
\[
\operatorname{SGdim}(T)=\left\lfloor\frac{n-1}{2}\right\rfloor.
\]

## Assumptions and scope
Graphs are finite and simple. A special-line realization of \(G\) is a set of distinct real points \(\{p_v:v\in V(G)\}\) such that, for every edge \(uv\), the line through \(p_u,p_v\) contains at least one further point of the configuration. The Sylvester--Gallai dimension \(\operatorname{SGdim}(G)\) is the maximum affine dimension of such a realization. The upper bound assumes only connectedness. The equality statement concerns all trees, not merely a subclass of trees.

## Proof
Fix a special-line realization \(P\) of a connected \(n\)-vertex graph \(G\). For every edge of \(G\), retain the geometric line determined by its two endpoints, and discard duplicate lines. Each retained line contains at least three points of \(P\). Because \(G\) is connected, these retained lines form a connected intersection system when intersections are required to occur at configuration points: along any edge-path in \(G\), consecutive edge-lines contain the point belonging to their common graph vertex. Every point of \(P\) lies on at least one retained line because a connected graph of order at least three has no isolated vertex.

Order the distinct retained lines as \(L_1,\ldots,L_m\) so that every \(L_j\) with \(j>1\) contains a configuration point already lying on \(L_1\cup\cdots\cup L_{j-1}\). The first line contains at least three configuration points and spans one affine dimension. Consider a later line \(L_j\). If it contains at least two previously seen configuration points, then the whole line lies in the affine span already generated, so it adds no affine dimension. If it contains exactly one previously seen configuration point, it can raise the affine dimension by at most one; because \(L_j\) is special, it then introduces at least two new configuration points. Therefore every affine dimension after the first consumes at least two points beyond the first three. If the final affine dimension is \(d\), then
\[
n\ge 3+2(d-1),
\]
so
\[
d\le 1+\left\lfloor\frac{n-3}{2}\right\rfloor=\left\lfloor\frac{n-1}{2}\right\rfloor.
\]
This proves the connected-graph upper bound.

It remains to attain the bound for every tree. We give a direct induction, reconstructing the lower bound rather than treating it as a black box. For \(n=3\) or \(n=4\), place all vertices on one line; the affine dimension is \(1=\lfloor(n-1)/2\rfloor\).

Let \(T\) be a tree of order \(n\ge5\), and take an endpoint \(v_0\) of a diametral path \(v_0v_1v_2\cdots\). Every neighbor of \(v_1\) other than \(v_2\) is a leaf, since otherwise the diametral path could be extended. If \(\deg(v_1)=2\), delete \(v_0,v_1\); if \(\deg(v_1)\ge3\), delete any two leaf-neighbors of \(v_1\). In either case the remaining graph \(T'\) is a tree on \(n-2\) vertices. By induction, realize \(T'\) in affine dimension \(\lfloor(n-3)/2\rfloor\). Embed that realization in one higher-dimensional affine space and choose a new line through the surviving attachment vertex whose direction is not contained in the old affine span. Put the two deleted vertices at two distinct new points of this line. In the degree-two case the line contains \(v_2,v_1,v_0\), making both new tree edges special. In the sibling-leaf case it contains \(v_1\) and the two deleted leaves, making both new edges special. All old edge-lines remain special, and the new line raises the affine dimension by exactly one. Hence
\[
\operatorname{SGdim}(T)\ge 1+\left\lfloor\frac{n-3}{2}\right\rfloor=\left\lfloor\frac{n-1}{2}\right\rfloor.
\]
Together with the universal connected upper bound, equality follows for every tree.

## Verification
The proof of the upper bound is deductive and uses only line uniqueness, connectedness, and affine-span dimension. The tree lower bound is also deductive. As a finite stress test of the only combinatorial induction step, `verify.py` enumerates every nonisomorphic tree of orders \(3\) through \(12\), repeatedly applies the diametral-path reduction used in the proof, checks that the remainder is a tree of order two smaller, and verifies that the accumulated dimension increment equals \(\lfloor(n-1)/2\rfloor\). It checks \(985\) tree types and does not substitute for the infinite proof.

## Relationship to prior work
Dvir introduced \(\operatorname{SGdim}\) in 2026. The initiating paper proves general lower bounds and, for forests, explicitly records the lower bound \(\operatorname{SGdim}(G)\ge\lfloor(n-1)/2\rfloor\), leaving its simple induction as an exercise. Its general quantitative upper bound gives \(\operatorname{SGdim}(G)\le12(n-1)/D\) when the minimum degree is at least \(D\), which does not yield the sharp half-order bound when only connectedness is assumed. The paper does not state a connected-graph half-order upper bound or an exact theorem for all trees.

The closest published exact follow-up found in the checked database determines \(\operatorname{SGdim}(K_{2,n})=1+\lfloor n/4\rfloor\) by a family-specific two-hub incidence graph. That result is neither equivalent to nor stronger than the present connected-graph bound and does not determine trees. The present line-intersection charging argument instead applies to every connected graph and makes the forest lower bound exact on the full tree class.

## Limitations
The half-order upper bound is generally not an exact formula outside trees; denser connected graphs can have much smaller Sylvester--Gallai dimension. No characterization is claimed for all connected graphs attaining equality. The literature is unusually recent, so a residual risk remains that a very recent or poorly indexed note contains the same elementary line-intersection argument; targeted primary-text, web, and semantic-database searches found no such statement.

## References
1. Z. Dvir, *The Sylvester--Gallai dimension of graphs*, arXiv:2608.15967v1, first posted 2026-08-16. Definition 1.1 defines the parameter; Theorem 1.2 gives the quantitative minimum-degree upper bound; the discussion after Theorem 1.5 records the forest lower bound.
2. *Exact Sylvester--Gallai dimension of \(K_{2,n}\)*, published published-finding corpus record dated 2026-09-17. The record gives the exact two-hub complete-bipartite formula and a family-specific incidence-component proof.
