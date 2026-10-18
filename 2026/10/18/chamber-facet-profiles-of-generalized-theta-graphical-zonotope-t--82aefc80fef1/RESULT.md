# Chamber-facet profiles of generalized-theta graphical-zonotope toric varieties

## Finding

For integers \(t\geq3\) and \(\ell_1,\ldots,\ell_t\geq2\), let \(G=\Theta(\ell_1,\ldots,\ell_t)\) consist of \(t\) internally vertex-disjoint paths between the same two terminal vertices, with path \(i\) containing \(\ell_i\) edges. Set \(E=\sum_i\ell_i\) and \(d=E-t+1\). Let \(Z_G\) be the graphical zonotope \(\sum_{uv\in E(G)}[0,e_u-e_v]\) in the root lattice, and let \(X_G\) be the normal projective toric \(d\)-fold of its normal fan, over an algebraically closed field of arbitrary characteristic.

For a torus-fixed point \(p\), let \(f(p)\) be the number of facets of its full-dimensional normal cone and set \(r(p)=E-f(p)\). The complete distribution of this local normal-cone invariant is

\[
R_{\boldsymbol\ell}(z):=\sum_{p\in X_G^T}z^{r(p)}
=\prod_{i=1}^{t}(2^{\ell_i}-2)
+2\left[\prod_{i=1}^{t}(2^{\ell_i}-1-\ell_i+\ell_i z)
-\prod_{i=1}^{t}(2^{\ell_i}-2-\ell_i+\ell_i z)\right].
\]

In particular, \(0\le r(p)\le t-1\), and \(p\) is smooth exactly when \(r(p)=t-1\). Thus the exact smooth and singular torus-fixed-point counts are

\[
\#(X_G^T\cap X_G^{\mathrm{sm}})
=2\sum_{j=1}^{t}\prod_{i\ne j}\ell_i,
\qquad
\#(X_G^T\cap\operatorname{Sing}X_G)
=2\prod_{i=1}^{t}(2^{\ell_i}-1)-\prod_{i=1}^{t}(2^{\ell_i}-2)
-2\sum_{j=1}^{t}\prod_{i\ne j}\ell_i.
\]

A fixed point is smooth if and only if the corresponding acyclic orientation has precisely one completely directed terminal-to-terminal path, and on every other path all edges are oriented against that complete path except for one edge oriented with it. Hence the proof gives an explicit parametrization of all smooth fixed points, not just their total count.

For the ordinary three-path theta graph of path lengths \((2,3,4)\), the polynomial is \(256+154z+52z^2\): there are \(462\) fixed points, of which \(52\) are smooth. The specialization \(\ell_1=\cdots=\ell_t=2\), the complete bipartite graph \(K_{2,t}\), is included as a known boundary comparison, not claimed as a new standalone classification.

## Assumptions and scope

Use the simple graph obtained from internally disjoint paths: the two terminals are shared, all internal vertices are distinct, and \(\ell_i\ge2\), so there are no parallel direct edges. Its \(E\) edges and \(V=E-t+2\) vertices give dimension \(V-1=d\). The torus acts on the projective toric variety of the **normal fan** of \(Z_G\), not the fan over its faces. The theorem is valid over arbitrary algebraically closed base fields; no analytic characteristic-zero argument is used. The invariant \(f(p)\) counts facets of the maximal normal cone, not rays or facets of the entire zonotope. The theorem makes no claim to classify all positive-dimensional singular strata.

## Proof

**1. Chambers and facet inequalities.** Acyclic orientations \(\mathcal O\) of any connected graph label the vertices of its graphical zonotope, hence the fixed points of \(X_G\). The corresponding maximal normal cone consists, modulo the diagonal line, of real vectors satisfying \(x_u\le x_v\) for every oriented edge \(u\to v\). Its irredundant inequalities are those of the transitive reduction (Hasse cover graph) of the orientation, as also expressed by Postnikov--Reiner--Williams, Proposition 3.5(8). Let \(h(\mathcal O)\) be the number of cover edges. Then \(f(p)=h(\mathcal O)\) and \(r(p)=E-h(\mathcal O)\), the number of transitive/redundant directed edges. Since the underlying cover graph is connected, \(h(\mathcal O)\ge V-1\), giving \(0\le r(p)\le E-(V-1)=t-1\).

**2. Directed cycles and the only possible transitive edges.** Orient and index each path from a common initial terminal \(s\) to a common final terminal \(u\). Any simple cycle in \(G\) is the union of exactly two of these paths. Thus a directed cycle exists if and only if at least one path is wholly directed \(s\to u\) and another is wholly directed \(u\to s\). Accordingly, an acyclic orientation has either no wholly directed path, or one or more wholly directed paths **all in the same direction** \(\varepsilon\).

Consider a directed edge \(e\) on path \(i\). Any alternative directed route between its endpoints, avoiding \(e\), must travel along one part of path \(i\) to one terminal, traverse some other path \(j\) completely, and return along the other part of path \(i\). Therefore \(e\) is transitive precisely when some other path \(j\) is wholly oriented in one terminal-to-terminal direction \(\varepsilon\), the edge \(e\) on path \(i\) points in that same direction, and every other edge on path \(i\) points in the reverse direction. In particular, with \(\ell_i\ge2\), a wholly directed path itself contains no transitive edge. Call a non-wholly-directed path *near-reverse* relative to \(\varepsilon\) when exactly one of its \(\ell_i\) edges points in direction \(\varepsilon\). It then contains exactly one transitive edge; all other non-wholly-directed paths contain none. If no path is wholly directed, none of the \(E\) edges is transitive.

**3. Exact distribution.** Without wholly directed paths, path \(i\) admits \(b_i=2^{\ell_i}-2\) orientations; all such orientations are acyclic, have \(r=0\), and contribute \(\prod_i b_i\). Otherwise choose the common complete-path direction \(\varepsilon\) in two ways. Relative to it, path \(i\) can be wholly directed in exactly one way; it can be near-reverse in exactly \(\ell_i\) ways, contributing one to \(r\); or it can be non-wholly-directed and not near-reverse in \(b_i-\ell_i=2^{\ell_i}-2-\ell_i\) ways, contributing zero. The product enumerator allowing these three alternatives on each path is \(\prod_i(1+b_i-\ell_i+\ell_i z)\). To insist that at least one path be wholly directed, subtract the product in which no path is wholly directed: \(\prod_i(b_i-\ell_i+\ell_i z)\). Multiply by two directions and add the no-wholly-directed term. This is the displayed formula for \(R_{\boldsymbol\ell}(z)\), and its evaluation at \(z=1\) yields the total fixed-point count \(2\prod_i(2^{\ell_i}-1)-\prod_i(2^{\ell_i}-2)\).

**4. Smoothness and lattice normalization.** For a fixed orientation, the normal cone is \(d\)-dimensional, pointed, and has one facet per Hasse edge. It is simplicial if and only if the Hasse cover graph has exactly \(V-1\) edges, i.e. is a spanning tree. If it is a spanning tree, the corresponding integral difference functionals \(x_u-x_v\) form a \(\mathbb Z\)-basis of the dual of \(\mathbb Z^V/\mathbb Z(1,\ldots,1)\): this is the integral unimodularity of any oriented tree incidence matrix. Hence the cone is actually regular/unimodular, not merely simplicial. A cone with more than \(d\) facets is not simplicial and its fixed point is singular. Consequently smoothness is exactly \(r=t-1\).

To have \(t-1\) transitive edges there must be exactly one wholly directed path, and every other path must be near-reverse: if there were two wholly directed paths, at most \(t-2\) other paths could contribute a transitive edge. For each choice of unique wholly directed path \(j\), two choices of direction and \(\prod_{i\ne j}\ell_i\) positions for the exceptional edges produce distinct orientations. This proves the smooth-count formula and the claimed explicit parametrization.

## Verification

The supplementary Python program `theta_general_checker.py` independently enumerates all \(2^E\) edge orientations for nine small generalized-theta graphs, rejects directed cycles by topological sorting, independently computes each transitive edge by searching for an alternative directed route after its deletion, and compares the entire \(r\)-distribution with the coefficient formula. It also compares the explicit smooth-orientation characterization with the exact Hasse tree test for **every** enumerated acyclic orientation. Representative verified distributions \(([z^0]R,[z^1]R,[z^2]R)\) are \((10,12,24)\) for \((2,2,2)\), \((32,38,32)\) for \((2,2,3)\), and \((256,154,52)\) for \((2,3,4)\). For \((2,2,2,2)\), the full distribution is \((18,16,48,64)\). All tests return `VERIFY_OK`.

These finite checks test the formulas and implementations but do not replace the general proof in the preceding section.

## Relationship to prior work

Postnikov--Reiner--Williams, *Faces of Generalized Permutohedra* (2006 preprint; 2008 publication), Section 3, Proposition 3.5, establishes the poset-cone dictionary and Hasse-tree simpliciality criterion; Section 5, Proposition 5.2, characterizes when a **whole** graphical zonotope is simple. The argument above uses their general criterion but establishes a new parameterized local chamber-facet distribution by a path-by-path classification, not merely a restatement of global simplicity.

Grujić, *Counting Faces of Graphical Zonotopes* (2016 preprint), Theorem 1.1, computes the global \(f\)-polynomial from the \(q\)-chromatic symmetric function. This is a face count indexed by dimensions, not a vertex-by-vertex count by the number of incident facets, and that theorem does not directly supply the displayed local distribution. Previously worked special graphs include cycles and \(K_{2,t}\); those restrictions do not cover a general multipath subdivision with an arm of length at least three. Other exact formulations may exist under “simplicial graphical arrangement chambers” terminology; no global literature uniqueness claim is made.

## Limitations

This classifies maximal-cone facet counts and smooth versus singular torus-fixed points, **not** complete singular-locus components, singularity multiplicities, or local analytic types. It does not claim that the known global Hasse-tree criterion or the all-length-two \(K_{2,t}\) specialization is new. Novelty depends on comparison with published work using equivalent arrangement-chamber or oriented-matroid terminology; unindexed sources remain a risk. Independent validation has not been performed.

## References

1. A. Postnikov, V. Reiner, L. Williams, *Faces of Generalized Permutohedra*, arXiv:math/0609184 (first posted 2006-09-06), especially Proposition 3.5 and Section 5. https://arxiv.org/abs/math/0609184 ; full text https://math.mit.edu/~apost/papers/genpermfaces.pdf
2. V. Grujić, *Counting Faces of Graphical Zonotopes*, arXiv:1604.06931 (first posted 2016-04-23), especially Theorem 1.1 and Section 5. https://arxiv.org/abs/1604.06931

