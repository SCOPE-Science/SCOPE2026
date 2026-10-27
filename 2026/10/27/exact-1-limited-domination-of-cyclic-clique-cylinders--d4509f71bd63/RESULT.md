# Exact 1-limited domination of cyclic clique cylinders

## Finding

**Theorem.** For every pair of integers \(n,m\geq3\), the graph \(G=C_n\square K_m\) satisfies
\[
\gamma_1^{\mathrm L}(G)
=m\gamma_t(C_n)
=m\left(\left\lfloor\frac n2\right\rfloor+
\mathbf 1_{4\nmid n}\right).
\]
Here \(\gamma_1^{\mathrm L}\) is the minimum size of a 1-limited dominating set and \(\gamma_t\) denotes total domination. The formula holds uniformly for all clique widths at least three and exhibits a sharp four-periodic correction in the cycle length.

In particular, the general Cartesian-product upper bound of Tepeh is attained for every member of this natural two-parameter family. The analogous equality does not hold for clique width two: \(\gamma_1^{\mathrm L}(C_6\square K_2)=6<8=2\gamma_1^{\mathrm L}(C_6)\).

## Assumptions and scope

All graphs are finite, undirected, and simple. \(C_n\) has distinct vertices \(i\in\mathbb Z/n\mathbb Z\), with consecutive vertices adjacent; the clique \(K_m\) has vertex labels \(j\in\{1,\ldots,m\}\). The Cartesian product has edges between \((i,j)\) and \((i',j')\) precisely when either \(i=i'\) and \(j\ne j'\), or \(j=j'\) and \(i-i'\equiv\pm1\pmod n\). For \(n\ge3\), these are distinct neighbours.

A set \(D\subseteq V(G)\) is *1-limited dominating* if every vertex outside \(D\) has a neighbour in \(D\), and each vertex in \(D\) has **at most one** neighbour outside \(D\). Its minimum size is \(\gamma_1^{\mathrm L}(G)\). A *total dominating set* \(T\) of a graph is one in which every vertex, including every selected vertex, has a selected neighbour; its minimum size is \(\gamma_t\).

## Proof

Write \(H=\gamma_t(C_n)\). The standard cycle formula, independently witnessed and proved below, is
\[
H=\lfloor n/2\rfloor+\mathbf 1_{4\nmid n},
\qquad H\le 2n/3,\qquad H\le n/2+1.
\]
For an explicit total dominating set on the cyclic vertex list use the following **cyclic** binary words, where 1 means selected, 0 means omitted, and concatenation is literal. Writing \(n=4q+r\) with \(0\le r<4\), use \((1100)^q\) when \(r=0\), \(11100(1100)^{q-1}\) when \(r=1\), \(111100(1100)^{q-1}\) when \(r=2\), and \(110(1100)^q\) when \(r=3\). The first two nonzero cases require \(q\ge1\), as is automatic for \(n\ge3\). These have exactly \(H\) ones, and every zero and every one has a neighbouring one. For the matching lower bound on a cycle, read a total dominating set as a cyclic zero-one word. If it has zeros, each run of ones has length at least two (a lone selected vertex lacks a selected neighbour), and each run of zeros has length at most two (an interior zero would be undominated). If there are \(b\) selected vertices and \(a=n-b\) omissions, pairing runs gives \(b\ge a\). If equality holds, every selected run and omitted run has length exactly two, forcing \(4\mid n\). Therefore \(b\ge n/2\), with strict inequality unless \(4\mid n\). The integer lower bound is precisely \(\lfloor n/2
floor+\mathbf1_{4
mid n}\); if there are no zeros, all vertices are selected and the same bound holds. This is also the published formula (Božović et al., 2026, Corollary 8), not an asserted new result.

**Upper bound.** Select all \(m\) vertices in each clique fibre indexed by a total dominating set \(T\) of \(C_n\). Any omitted vertex lies in a fibre adjacent to a fully selected fibre and hence is dominated. Each selected vertex has at most one neighbouring omitted fibre because each vertex of \(T\) has a neighbour in \(T\); there are no omissions in selected fibres. Thus \(D=T\times V(K_m)\) is 1-limited and has \(|D|=mH\). This is also the special case of Tepeh's Cartesian-product upper bound.

**Lower bound.** Let \(D\) be any 1-limited dominating set in \(G\). For each cycle coordinate \(i\), let \(s_i\) be the number of selected vertices in its clique fibre. If \(s_i>0\), a selected vertex in that fibre has \(m-s_i\) omitted neighbours *within the clique*. Since it may have at most one omitted neighbour in total, \(s_i\ge m-1\). Thus each fibre is of one of three kinds: **zero** (\(s_i=0\)), **partial** (\(s_i=m-1\)), or **full** (\(s_i=m\)). Denote their counts by \(z,p,f\), respectively, so \(n=z+p+f\) and
\[
|D|=(m-1)p+mf
=\frac{mn}{2}+\frac m2(f-z)+\left(\frac m2-1\right)p.
\]

If \(z=0\), then \(|D|\ge(m-1)n\ge mH\), using \(m\ge3\) and \(H\le2n/3\).

If \(p=0\), the nonempty fibres are full. The full-fibre indices must totally dominate \(C_n\): an empty fibre needs a full neighbour to dominate its vertices, and a full fibre must have a full neighbour or each of its vertices would have two omitted neighbours (one in each adjacent fibre). Therefore \(f\ge H\) and \(|D|=mf\ge mH\).

Finally suppose \(p>0\) and \(z>0\). A zero fibre cannot neighbour a partial fibre: each selected vertex in the latter would have its one omission inside the clique *and* another in the zero fibre. Each nonzero neighbour of a zero fibre must be full. A full fibre directly neighbouring a zero fibre cannot neighbour a partial fibre on its other side, because one coordinate would then be omitted in both adjacent fibres. To avoid a subtlety with consecutive zero fibres, group all zero fibres into maximal cyclic zero-runs. Every zero-run has length one or two: a run of three zeros would contain a vertex without any selected neighbour. Every intervening run of nonzero fibres between two consecutive zero-runs has at least two full fibres, one at each endpoint; indeed a one-fibre separation would place a full fibre between two zero fibres and violate the 1-limited constraint. If such an intervening run contains any partial fibre, it must contain at least **two full fibres before its first partial and two after its last partial**, since a partial neighbour of a zero-adjacent full fibre would violate the 1-limited constraint. There must be at least one such run because \(p>0\).

Let there be \(b\ge1\) maximal zero-runs. Because their lengths are at most two, \(z\le2b\). The separating nonzero runs contribute at least \(2b+2\) full fibres: two per run and two extra in at least one run containing a partial fibre. Hence \(f\ge z+2\). In the displayed cardinality identity, \(m\ge3\) and \(p>0\) now imply
\[
|D|\ge\frac{mn}{2}+m\ge mH,
\]
using \(H\le n/2+1\).

The three cases exhaust all possible \(D\), so the lower bound and constructive upper bound match. This proves the theorem. \(\square\)

## Verification

The file `verify_clique_cycles.py` performs three scientifically distinct finite checks: full labelled-vertex-subset enumeration on eight instances up to 18 vertices without clique-fibre pruning, exact cyclic triple-state transfer minimization for every \(3\le m\le8\) and \(3\le n\le42\), and direct vertexwise verification of optimal explicit constructions for all \(3\le m\le30\) and \(3\le n\le160\). Output is in `verification_output.txt`. Running the verifier produces `VERIFY_OK`.

These calculations test the proof and catch boundary errors but do **not** establish the infinite theorem. The infinite claim is established by the three-case argument above and the known exact total domination formula for cycles.

## Relationship to prior work

The foundational 2026 study of \(k\)-limited domination proves the exact cycle case \(\gamma_1^{\mathrm L}(C_n)=\gamma_t(C_n)\). Tepeh's 2026 Cartesian-product theorem gives the general upper bound \(\gamma_1^{\mathrm L}(G\square H)\le\gamma_1^{\mathrm L}(G)|V(H)|\), which for these graphs gives precisely the upper bound above. Its general lower bound is only half the product order, and its specific exact results address rook graphs, Cartesian products of paths, and other families, not arbitrary \(C_n\square K_m\) for \(m\ge3\). In the residue class \(4\mid n\), known upper and lower bounds already agree, so that subcase is covered by those results; the content beyond prior implications is the other three residue classes and the uniform optimality proof for all widths.

Radić and Tepeh's later cubic-graph study concerns a different graph regime and Goldberg snarks, and does not imply this result for clique width at least three. Other mathematical records concerning \(C_n\square K_m\) pertain to topological Vietoris–Rips invariants rather than restricted domination. Priority is not independently certified, and equivalent terminology such as \((0,1)\)-pitchfork domination or \((1,m)\)-domination should remain bibliographic search risks.

## Limitations

The theorem requires \(m\ge3\). In particular, its multiplicativity statement is false for some prisms with \(m=2\). It concerns 1-limited domination, not arbitrary \(k\)-limited variants or products with noncomplete fibres. Neither optimal-set uniqueness nor the complete number of minimizers is claimed. The result has received self-review only; no independent mathematical audit has been performed.

## References

- Božović et al., *On k-limited domination in graphs*, 2026. Available at `https://link.springer.com/article/10.1007/s40314-026-03902-2` and first posted as arXiv:2606.22422; Corollary 8 gives the cycle formula.
- Aleksandra Tepeh, *On k-limited domination: complexity and Cartesian products*, arXiv:2606.22428v1 (first posted 2026-06-21), revised v2 (2026-10-01); Theorem 7 gives universal Cartesian-product bounds and Section 4 treats special exact product families.
- Goran Radić and Aleksandra Tepeh, *On 1-limited and (1,2)-domination in cubic graphs*, arXiv:2610.01796v1 (2026-10-01); separate cubic-graph context.
