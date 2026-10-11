# Stong-core classification for ordered two-point configurations of complete height-two finite spaces
## Finding
For integers \(p,q\ge2\), let \(P_{p,q}=A_p\oplus B_q\) be the finite \(T_0\)-space whose minimal level is \(A_p=\{a_1,\ldots,a_p\}\), whose maximal level is \(B_q=\{b_1,\ldots,b_q\}\), and in which \(a_i<b_j\) for every \(i,j\). Define the ordered two-point configuration space
\[
F_2(P_{p,q})=\{(x,y)\in P_{p,q}^2:x\ne y\}
\]
with the coordinatewise order.

No same-level configuration is a beat point. A mixed configuration \((a_i,b_j)\) or \((b_j,a_i)\) is a down beat point exactly when \(p=2\), and an up beat point exactly when \(q=2\). Hence the Stong core is completely determined:
\[
\operatorname{core}F_2(P_{p,q})\cong
\begin{cases}
F_2(P_{p,q}),&p,q\ge3,\\
P_{2,q(q-1)},&p=2,\\
P_{p(p-1),2},&q=2.
\end{cases}
\]
At \(p=q=2\) the last two descriptions both give \(P_{2,2}\). In particular, for \(p,q\ge3\) the ordered configuration space is already a finite-space core with exactly \((p+q)(p+q-1)\) points.

## Assumptions and scope
A beat point is used in Stong's finite-space sense: \(x\) is an up beat point when its strict upper set has a minimum, and a down beat point when its strict lower set has a maximum. A core is a beat-point-free strong deformation retract. The theorem concerns ordered configurations of two distinct points and ordinary finite-space homotopy, not only weak homotopy of order complexes. The parameter range is exactly \(p,q\ge2\).

The spaces \(P_{p,q}\) are the complete height-two finite graph models appearing in Barmak--Minian: their order complexes are complete bipartite graphs and hence model wedges of \((p-1)(q-1)\) circles.

## Proof
There are four types of points in \(F_2(P_{p,q})\):
\[
AA=(a_i,a_k),\quad AB=(a_i,b_j),\quad BA=(b_j,a_i),\quad BB=(b_j,b_\ell),
\]
with unequal indices in the same-level types.

For \(x=(a_i,b_j)\), its strict lower set is exactly
\[
\{(a_i,a_k):k\ne i\},
\]
and its strict upper set is exactly
\[
\{(b_\ell,b_j):\ell\ne j\}.
\]
The members of each displayed set are pairwise incomparable. Therefore the strict lower set has a maximum exactly when \(p-1=1\), and the strict upper set has a minimum exactly when \(q-1=1\). Thus \((a_i,b_j)\) is down beat exactly for \(p=2\) and up beat exactly for \(q=2\). The same calculation for \((b_j,a_i)\) gives strict lower set \(\{(a_k,a_i):k\ne i\}\) and strict upper set \(\{(b_j,b_\ell):\ell\ne j\}\), so the identical criterion holds.

Now take an \(AA\)-point \((a_i,a_k)\). For every \(j\), the two strict upper elements \((a_i,b_j)\) and \((b_j,a_k)\) are incomparable. Since \(q\ge2\), its strict upper set cannot have a minimum; its strict lower set is empty. Hence no \(AA\)-point is a beat point. Dually, every \(BB\)-point has incomparable strict lower elements and no strict upper elements, so no \(BB\)-point is a beat point.

If \(p,q\ge3\), the mixed points have at least two incomparable points both below and above them, and the preceding paragraph handles the same-level points. Thus there are no beat points at all, proving that \(F_2(P_{p,q})\) is already its core.

Suppose \(p=2\). Every mixed point has a unique strict lower point, so every mixed point is a down beat point. Deleting mixed points one at a time preserves that unique lower point, so all \(2pq\) mixed points can be removed by strong deformation retractions. What remains consists of the two ordered \(AA\)-points and the \(q(q-1)\) ordered \(BB\)-points. Every remaining \(AA\)-point lies below every remaining \(BB\)-point, with no other comparabilities. The remainder is therefore exactly \(P_{2,q(q-1)}\). Because \(q(q-1)\ge2\), both levels have at least two points, so this remainder has no beat point and is the core. The case \(q=2\) is the order-dual argument, giving \(P_{p(p-1),2}\). At \(p=q=2\), both formulas give \(P_{2,2}\).

## Verification
The standalone checker `artifacts/verify.py` reconstructs \(F_2(P_{p,q})\) directly from the product order. For all \(49\) pairs \(2\le p,q\le8\), it exhaustively verifies the complete beat-point classification, replays the stated deletion sequence when a level has size two, checks the resulting complete height-two core, and verifies that the final space has no beat points. Its packaged output is stored in `artifacts/verification_output.txt`.

The finite replay is corroborative only; the theorem for all \(p,q\ge2\) follows from the explicit strict-upper and strict-lower set calculation above.

## Relationship to prior work
Barmak and Minian give the finite-space beat-point/core framework and use complete height-two spaces \(P_{p,q}\) as canonical finite models of graph weak types. Their inspected source does not study ordered configuration spaces of these models or classify their Stong cores.

Farber and Hanbury prove that the classical graph configuration space \(F(K_{p,q},2)\), for \(p,q\ge3\), has first and second Betti numbers \(2(p-1)(q-1)\) and \((p^2-3p+1)(q^2-3q+1)\), respectively. That result is important stronger coverage for weak invariants, but it does not imply a Stong-core classification: finite-space homotopy and core cardinality are not determined by homology or by the weak homotopy type of an order complex. The present claim is specifically the exact beat-point structure and core of the finite configuration space.

## Limitations
The theorem is about ordered two-point configurations only. It does not classify unordered quotients, configurations of three or more points, or minimal-cardinality models within a weak homotopy class. Here “core” means the unique beat-point-free strong deformation retract up to homeomorphism, not a claim of smallest cardinality among all weakly equivalent finite spaces. The originality assessment cannot exclude an older result phrased as a deleted-product or finite-poset configuration statement that escaped the searched terminology.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1, first submitted 2006-11-06. See Definition 2.2 for beat points/core terminology and Section 4 for complete height-two graph models.
2. M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300; Algebraic & Geometric Topology 10 (2010), 2203--2227. See Proposition 22 and Corollary 24 for the classical complete-bipartite graph configuration comparison.
