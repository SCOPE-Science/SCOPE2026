# Factorial fragmentation of optimal cycle-burning schedules at one-site slack

## Finding

Let \(k\ge2\), let \(C_N\) be the labeled cycle with vertices \(\mathbb Z/N\mathbb Z\), and consider ordered, **proper** burning schedules \((x_1,\ldots,x_k)\): the ignition at step \(j\) must not have burned strictly before that step. Connect two schedules when they differ in exactly one coordinate and both remain proper optimal schedules. At the two sharp orders \(N=k^2\) and \(N=k^2-1\), the burning number equals \(k\) and the entire exchange geometry is as follows.

**Square order:** At \(N=k^2\), there are exactly \(k^2(k-1)!\) optimal schedules and no exchange edges.

**One-site deficit:** At \(N=k^2-1\), there are exactly \(Nk!\) optimal schedules, and their exchange graph has exactly \((k-2)!\) connected components, each with \(Nk(k-1)\) schedules. Its number of exchange edges is \(N(3k-4)(k-1)!\). Exactly \(2N(k-1)!\) schedules have degree \(2k-2\), and the remaining \(N(k-2)(k-1)!\) have degree \(2\) (for \(k=2\) the latter class is empty). Thus the first one-vertex relaxation of maximal cyclic burning capacity gives mobility without global connectivity once \(k\ge4\): component count grows factorially.

## Assumptions and scope

The cycles are undirected, simple, vertex-labeled graphs; \(N\ge3\). A length-\(k\) schedule is *proper* if
\[
\operatorname{dist}_{C_N}(x_i,x_j)\ge j-i\quad(1\le i<j\le k),
\]
and it burns every vertex precisely when
\[
\bigcup_{i=1}^{k}B_{k-i}(x_i)=V(C_N),\qquad B_r(x)=\{v:\operatorname{dist}(v,x)\le r\}.
\]
The convention allows an ignition to coincide with fire reaching the same vertex during its own round, but prohibits ignition at a vertex burned in an earlier round. The exchange graph keeps the time labels and cycle vertex labels; there is no quotient by rotation, reversal, or permutation of ignition times.

For \(N\in\{k^2-1,k^2\}\), the radii \(k-1,k-2,\ldots,0\) produce contiguous circular arcs of sizes \(2k-1,2k-3,\ldots,1\), whose total length is \(k^2\). The known identity \(b(C_N)=\lceil\sqrt N\rceil\) establishes optimality at both orders; alternatively, \(k-1\) rounds cover at most \((k-1)^2<N\) vertices, while the displayed arc configurations attain \(k\) rounds.

## Proof

**1. The square case.** At \(N=k^2\), the total available arc length equals the size of the cycle. Thus the \(k\) arcs of any successful schedule must be disjoint and partition the cycle. Conversely, such a circular tiling respects proper ignition, since different arcs have disjoint final-time coverage. Its \(k\) distinct, time-labeled arcs may have any cyclic order: there are \((k-1)!\) circular orders and \(N\) possible positions for one specified center. Hence there are \(N(k-1)!\) schedules. Every arc consists entirely of vertices it alone covers; changing its center while holding all others fixed leaves at least one vertex uncovered. The exchange graph is therefore edgeless.

**2. The one-site deficit and the two types.** Now set \(N=k^2-1\). The total arc length exceeds the cycle size by exactly one. Coverage forces exactly one vertex to belong to two arcs and all other vertices to belong to exactly one. In particular there can be no triple intersection or multiple overlaps. Let the \(m=k-1\) positive-radius arcs be indexed by ignition times \(1,\ldots,m\). Their lengths are the odd numbers from \(2k-1\) down to \(3\), totaling exactly \(N\). The radius-zero last arc is the singleton \(\{x_k\}\).

There are precisely two possibilities:

(A) The positive-radius arcs form a disjoint tiling of the cycle. Then \(x_k\) overlaps exactly one of them. Proper ignition makes \(x_k\) an endpoint of that arc, since the center-to-ignition distance must be at least its radius. Every positive arc has two distinct endpoints and the tiling has exactly \(2m\) such choices.

(B) The positive-radius arcs have exactly one shared endpoint and leave exactly one uncovered cycle vertex. The singleton must occupy that gap. Fixing the cyclic order of positive-radius arcs, the inter-center clockwise gaps relative to the disjoint-tiling gaps are zero except that exactly one boundary has deficit one (the shared endpoint) and a different boundary has surplus one (the uncovered vertex). There are \(m(m-1)\) ordered positions of these two defects.

Conversely every arrangement in (A) or (B) yields a proper burning schedule. The intervals cover the cycle; for any two time labels \(i<j\), their ball-center distance is at least \((k-i)+(k-j)\), which is at least \(j-i\). This remains true for the radius-zero ignition, including when it lies at the endpoint of an earlier arc. For \(k=2\), case (B) is empty and the sole positive-radius arc is the entire triangle; the same count and properness conclusion hold directly.

There are \((m-1)!\) cyclic orders of the positive-radius labels and \(N\) rotations of any fixed order. At each such choice, cases (A) and (B) contribute \(2m+m(m-1)=m(m+1)\) schedules. Therefore the total is
\[
N(m-1)!m(m+1)=Nk!.
\]

**3. Exchange invariant.** A change of a positive-radius center can be valid only if that arc shares the unique duplicated vertex with another arc. Its other \(\ell-1\) or \(\ell\) vertices are uniquely covered; to retain them, the new arc of the same odd length must be the original arc shifted exactly one cycle step away from the shared endpoint. This is the only alternative center. A radius-zero change does not move any positive-radius center. For \(k\ge3\), distinct positive-radius centers are separated by at least two cycle steps, so such single-step moves never change their cyclic order; the \(k=2\) case has just one positive center. Thus the \((m-1)!=(k-2)!\) cyclic orders label distinct exchange components.

**4. Connectivity within each fixed order.** Fix one cyclic order of the positive-radius centers. Every type-(B) schedule has a unique surplus boundary and a unique deficit boundary. Shift the positive-radius center immediately clockwise after the deficit boundary one step clockwise. This transfers the deficit to the next boundary, leaving the surplus (and its singleton occupant) in place; all intermediate schedules are valid. Iterating until the deficit reaches the surplus cancels both and gives a type-(A) tiling. Thus every (B) schedule reaches (A).

For a fixed tiling, all \(2m\) type-(A) choices of \(x_k\) are mutually adjacent, because only the last coordinate changes. To translate a tiling by one cycle step clockwise, put \(x_k\) at the left endpoint of one positive-radius arc. Move the center of that arc one step clockwise, then that of the next arc clockwise, continuing around the cyclic order. At intermediate stages the singleton covers the unique gap and the unique overlap travels clockwise; after all \(m\) centers move, the positive arcs again form a tiling shifted by one step. This gives a path of valid schedules. Repeated translation connects every tiling of the prescribed cyclic order, hence all schedules of that order lie in one component. So the number of components is exactly \((k-2)!\), each of size \(Nk(k-1)\).

**5. Degrees and edges.** In type (A), changing \(x_k\) to any of the other \(2m-1\) permitted endpoints is a valid exchange. Exactly one positive-radius arc has an endpoint at \(x_k\); shifting that arc away from that endpoint is the sole additional move. Hence type (A) has degree \(2m=2k-2\). In type (B), the singleton is forced to occupy the unique uncovered vertex, while each of the two arcs incident to the duplicated endpoint can be shifted once; no other move is legal. Hence type (B) has degree two. Across all orders, the numbers of the two types are respectively \(2Nm!=2N(k-1)!\) and \(Nm!(m-1)=N(k-2)(k-1)!\). The handshake lemma gives
\[
|E|=\tfrac12\bigl(2N(k-1)!(2k-2)+N(k-2)(k-1)!\cdot2\bigr)
 =N(3k-4)(k-1)!.
\]
This completes the proof.

## Verification

The accompanying `verify_cycle_burning.py` requires Python 3 and only its standard library. Run `python3 verify_cycle_burning.py` in the directory containing the file. For \(k=2,3,4\), a direct \(N^k\)-tuple search uses graph distances independently of the arc parametrization and confirms the entire sets at both orders. For \(2\le k\le7\), a second generator forms schedules from the circular order of arcs and checks the predicted counts, degrees, connected-component sizes and edge totals by exhaustive adjacency construction. For \(k\le5\), every generated near-square schedule is additionally checked against the distance conditions. The output ends with `VERIFY_OK`.

The finite checks corroborate the theorem at those parameters; the all-parameter proof is the interval-overlap and defect-transport argument above.

## Relationship to prior work

Bonato, Janssen and Roshanbin (arXiv:1507.06524, first public 2015-07-23), *How to burn a graph*, develop graph burning, give the ball-covering characterization and establish \(b(C_N)=\lceil\sqrt N\rceil\). Their scalar burning-number theorem is used here and is not new. Bessy, Bonato, Janssen and Rautenbach (arXiv:1511.06023, first public 2015-11-18), *Bounds on the Burning Number*, explain the equivalent distance-and-ball formulation and study bounds, not component counts of optimal schedules. Fitzpatrick and Wilm (arXiv:1706.03106, first public 2017-06-09), *Burning Circulant Graphs*, examine other circulant burning numbers. The presently stated precise near-square enumeration, factorial components and degree distribution are not supplied by the inspected primary texts. Searches of mathematical record summaries and phrase-level literature did not locate an equivalent theorem; that observation does not establish absolute novelty.

## Limitations

Only the two near-maximal orders \(N=k^2\) and \(N=k^2-1\) are classified. The exchange rule changes one ignition location while retaining all time labels and requiring properness; conclusions do not automatically apply to lengthening, time-reordering, rotating/quotienting configurations, allowing already-burned ignitions, or cycles farther below the square. Although two directly relevant primary texts were inspected, unindexed prior work remains a risk.

## References

1. A. Bonato, J. Janssen, E. Roshanbin, *How to burn a graph*, arXiv:1507.06524 (first submitted 2015-07-23). https://arxiv.org/abs/1507.06524
2. S. Bessy, A. Bonato, J. Janssen, D. Rautenbach, *Bounds on the Burning Number*, arXiv:1511.06023 (first submitted 2015-11-18). https://arxiv.org/abs/1511.06023
3. S. L. Fitzpatrick, L. Wilm, *Burning Circulant Graphs*, arXiv:1706.03106 (first submitted 2017-06-09). https://arxiv.org/abs/1706.03106
