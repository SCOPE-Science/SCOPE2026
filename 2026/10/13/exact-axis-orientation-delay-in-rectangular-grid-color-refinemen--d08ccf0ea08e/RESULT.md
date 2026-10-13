# Exact axis-orientation delay in rectangular grid color refinement

## Finding
For integers \(2\le m<n\), let \(G_{m,n}=P_m\square P_n\) be the unlabelled simple rectangular grid on \(\{0,\ldots,m-1\}\times\{0,\ldots,n-1\}\). Let \(u=(1,0)\) and \(v=(0,1)\), the two vertices adjacent to the same corner in the perpendicular directions. Starting with one uniform vertex colour, let \(c_r\) be the result after \(r\) simultaneous rounds of ordinary colour refinement. Then

\[
c_r(u)=c_r(v)\quad(0\le r\le m-2),\qquad c_{m-1}(u)\ne c_{m-1}(v).
\]

More precisely, if \(A\) is the adjacency matrix and \(b(w)=4-\deg(w)\), then

\[
(A^k b)(u)-(A^k b)(v)=
\begin{cases}
0,&0\le k<m-2,\\
1,&k=m-2.
\end{cases}
\]

Consequently the stabilization round \(\rho(G_{m,n})\), measured from the uniform colouring, satisfies \(\rho(G_{m,n})\ge m-1\). In the two-variable first-order graph language with counting quantifiers, where a counting quantifier contributes depth one, the least quantifier rank of a unary formula distinguishing these two pointed vertices in \(G_{m,n}\) is likewise \(m-1\).

## Assumptions and scope
\(P_k\) denotes the path with exactly \(k\) vertices, with adjacent integers joined. The grid has no vertex labels, coordinates in the statement are a way to name its vertices, and no coordinate predicates are present in the logical language. Colour refinement uses
\[
c_{r+1}(w)=\left(c_r(w),\ \operatorname{Multiset}\{c_r(z):z\sim w\}\right),
\]
with colours renamed canonically between rounds; only equality of colour signatures matters. The case \(m=2\) is included. Stabilization means the first round whose partition equals the following round's partition.

## Proof
**1. Indistinguishability through round \(m-2\).** Embed the grid as an induced subgraph of the quadrant \(Q=\mathbb Z_{\ge0}^2\), whose edges change one coordinate by one. Transposition \(\sigma(i,j)=(j,i)\) is an automorphism of \(Q\) sending \(u\) to \(v\). For every \(r\le m-2\), every length-at-most-\(r\) walk in \(Q\) starting at either \(u\) or \(v\), and every walk obtained by applying \(\sigma\), lies inside \(G_{m,n}\): the first coordinate never exceeds \(m-1\) and the second never exceeds \(m-1<n\). Thus transposition is a bijection of the two rooted depth-\(r\) walk-unfolding trees. By the recursive definition of colour refinement, isomorphic rooted walk-unfolding trees of depth \(r\) have equal \(r\)-round colours. This proves the first equality, including the endpoint \(r=m-2\).

**2. The first boundary signal.** In the quadrant put \(b_Q(i,j)=\mathbf1_{i=0}+\mathbf1_{j=0}\). On the finite grid,
\[
b(i,j)=b_Q(i,j)+\mathbf1_{i=m-1}+\mathbf1_{j=n-1}.
\]
For \(0\le k\le m-2\), the length-\(k\) walks from \(u\) or \(v\) are exactly their quadrant walks. The \(b_Q\)-weighted walk sums agree by transposition. The distance from \(u\) to the far short side \(i=m-1\) is \(m-2\), whereas from \(v\) it is \(m-1\). The distances from \(u\) and \(v\) to the far long side \(j=n-1\) are respectively \(n-1\) and \(n-2\), both greater than \(m-2\). Therefore none of the far-side indicators contributes before \(k=m-2\); at \(k=m-2\), exactly one walk from \(u\) reaches a far side, namely the straight positive-first-coordinate walk. Its endpoint contributes one unit to \(b\), while no corresponding walk from \(v\) does. Since \((A^k b)(w)\) sums \(b\) over length-\(k\) walks from \(w\), the displayed moment identity follows.

**3. Detectability and stabilization.** The first-round colour determines degree, hence \(b\). Inductively, the \((k+1)\)-st colour of a vertex determines \((A^k b)\) there: for the induction step it records the multiset of the neighbouring \(k\)-th colours, and hence the sum of their preceding walk-defect moments. The difference of one at \(k=m-2\) therefore forces \(c_{m-1}(u)\ne c_{m-1}(v)\). As a stable partition cannot subsequently split, stabilization before round \(m-1\) is impossible.

**4. Logical depth.** On a fixed finite graph, unary formulas of two-variable counting logic of quantifier rank at most \(r\) are constant on \(c_r\)-colour classes. This is proved by induction: a formula with both variables free reduces to Boolean combinations of unary formulas and the binary atoms of equality and adjacency; when one variable is counted, the required number of neighbours and non-neighbours of each previous unary type is determined by the next refinement colour together with global type totals. Conversely, each \(r\)-round colour is definable by a unary counting formula of rank \(r\), recursively testing its previous colour and the numbers of neighbours of each previous colour. Thus the equality and inequality of the two point colours established above yield exactly the stated least unary counting quantifier rank.

## Verification
The standalone script `verify_grid.py` independently constructs the grids and applies the simultaneous multiset refinement and adjacency-walk recurrences. Executing it in Python verified the separation round and moment difference for every \(2\le m<n\le22\), a total of 204 parameter pairs. Finite testing is supplementary; the proof above covers all integers in the stated domain.

## Relationship to prior work
Krebs and Verbitsky, first public version of arXiv:1407.3175 on 2014-07-11, establish the correspondence between truncated universal covers and refinement colours (Lemma 2.6) and between refinement colours and two-variable counting formulas (Section 4). Their paper studies general worst-case depth, not the pointed rectangular-grid boundary calculation above. Arvind, Köbler, Rattan and Verbitsky (arXiv:1502.01255) study graph classes identifiable by refinement. Kiefer and McKay (arXiv:2005.10182) establish sharp global worst-case iteration bounds. Those broader results give context but do not themselves supply the displayed exact first-separation round for the specified two vertices. Searches of these full texts and related records did not locate the pointed-grid formula; this is not a proof of worldwide novelty.

## Limitations
The finding concerns one natural pair of vertices and supplies a lower bound, not a formula for the full stabilization round of every rectangular grid. It is not a claim about grids with labels, initial degree colours, or arbitrary starting partitions. No independent review has been performed; absence of an exact prior statement in the checked literature cannot exclude overlooked or unpublished equivalent results.

## References
- Andreas Krebs and Oleg Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 2014-07-11, https://arxiv.org/html/1407.3175v2, DOI:10.1109/LICS.2015.69.
- V. Arvind, Johannes Köbler, Gaurav Rattan and Oleg Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 2015-02-04, https://arxiv.org/html/1502.01255v3.
- Sandra Kiefer and Brendan D. McKay, *The Iteration Number of Colour Refinement*, arXiv:2005.10182, first posted 2020-05-20, https://arxiv.org/html/2005.10182v1.
