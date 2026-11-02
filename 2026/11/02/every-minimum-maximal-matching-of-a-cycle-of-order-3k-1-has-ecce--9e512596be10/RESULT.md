# Every minimum maximal matching of a cycle of order \(3k+1\) has eccentricity \(\lfloor(3k+1)/2\rfloor\)

## Finding

Let \(k\ge2\), let \(n=3k+1\), and let \(C_n\) be the labelled simple cycle with edges \(e_0,\ldots,e_{n-1}\), indexed cyclically. A **minimum maximal matching** is an inclusion-maximal matching having the smallest possible cardinality. Define \(R_n\) to have these matchings as vertices, with two distinct matchings adjacent exactly when one cycle edge is replaced by one other cycle edge and the new set is again a minimum maximal matching. Write \(d_{R_n}\) for shortest-path distance and \(\operatorname{ecc}_{R_n}(M)=\max_N d_{R_n}(M,N)\).

**Theorem.** For every \(k\ge2\) and **every** minimum maximal matching \(M\) of \(C_{3k+1}\),
\[
\operatorname{ecc}_{R_{3k+1}}(M)=\left\lfloor\frac{3k+1}{2}\right\rfloor.
\]
Thus \(R_{3k+1}\) is connected and self-centered, with
\[
\operatorname{rad}(R_{3k+1})=\operatorname{diam}(R_{3k+1})=\left\lfloor\frac{3k+1}{2}\right\rfloor.
\]
The finding concerns **all eccentricities**, not only the largest one. In particular, the known distinction between degree-two and degree-four configurations does not produce an eccentricity distinction. The identification of the underlying reconfiguration graph with the earlier bracelet graphs is not claimed as new.

## Assumptions and scope

All graphs are simple and undirected; edges in the original cycle are labelled, and matching configurations are unordered sets. Exchanges must retain **minimum** cardinality and maximality after every step. For the stated family, a minimum maximal matching contains exactly \(k+1\) edges. The established cycle independent-domination/bracelet description below is used with a direct coordinate verification; no statement is made for larger matchings or for cycles of other congruence classes. Distances are ordinary unweighted graph distances.

Set \(h=k+1\), so \(n=3h-2\), and let \(\mathbb Z_n\) denote the cyclic ring of positions. The **separated-pair graph** \(T_{n,h}\) has vertices the unordered pairs \(\{a,b\}\subset\mathbb Z_n\) satisfying
\[
 h\le (b-a)\bmod n\le n-h
\]
when the representatives are ordered \(0\le a<b<n\). Adjacent pairs differ by moving exactly one point one unit clockwise or counterclockwise modulo \(n\), provided the new pair is still separated by at least \(h\) in both directions.

## Proof

**1. Reduction to two separated particles.** A matching in \(C_n\) is a stable set in its line graph, which is itself a labelled \(n\)-cycle. Inclusion-maximality is domination of the edge-cycle. The cyclic gaps between consecutively chosen positions consequently belong to \(\{2,3\}\). With exactly \(h=k+1\) positions and \(n=3h-2\), the total deficit from all-three gaps is two: exactly two gaps have length two. Mark the unselected intermediate position of each of these two short gaps, producing an unordered pair \(\{j,\ell\}\) of doubly dominated sites.

The earlier bracelet-coordinate analysis of Brewster, Mynhardt and Teshima establishes, and the preceding gap description independently explains, that allowable marked-position differences are precisely \(2+3s\pmod n\) for \(0\le s\le k-1\), and that any legal exchange moves one marked position by \(+3\) or \(-3\) modulo \(n\). In particular, an arbitrary one-edge replacement cannot skip a site: deleting one selected position merges its two adjacent gaps; reinserting a different position can split this merged gap into allowed gaps only when the original adjacent gaps were \(2,3\) or \(3,2\), exchanging these lengths and sliding one site.

As \(-3k\equiv1\pmod n\), multiplication of marked positions by \(-k\pmod n\) sends the possible differences \(2+3s\) to \(k+1+s\), precisely \(h,h+1,\ldots,n-h\), and sends the allowed \(\pm3\) moves to \(\pm1\) moves. Therefore
\[
 R_n\cong T_{n,h}.
\]
This known bracelet identification is part of the reduction, not the new metric assertion.

**2. Uniform upper bound.** Put \(q=\lfloor n/2\rfloor\). We prove that any two allowed pairs \(A,B\) in \(T_{n,h}\) are at distance at most \(q\). The separation between the two moving particles, measured clockwise, must always lie in the interval \([h,n-h]\). When both particles move monotonically in the same direction, one move increases this separation and the other decreases it. If the initial and final separations both lie in that interval, the prescribed moves can be interleaved to stay inside it: at a boundary, take a remaining move pointing inward; if no such move remains, the specified final separation could not have belonged to the interval.

If the pairs share a point, keep it fixed. The other point moves within an allowed arc of length \(n-2h=h-2\), so a path of at most \(h-2\le q\) moves exists.

Suppose all four points are distinct and alternate around the circle: \(A_1,B_1,A_2,B_2\), with successive positive clockwise arc lengths \(u,v,w,x\), so \(u+v+w+x=n\). Move both source points clockwise, \(A_1\to B_1\) through \(u\) steps and \(A_2\to B_2\) through \(w\) steps. By the preceding interleaving observation, this is an allowed path of length \(u+w\). Alternatively move both counterclockwise, \(A_1\to B_2\) through \(x\) steps and \(A_2\to B_1\) through \(v\) steps; this yields an allowed path of length \(x+v\). Hence the distance is at most \(\min(u+w,v+x)\le\lfloor n/2\rfloor=q\).

Otherwise, up to cyclic rotation and relabelling, the order is \(A_1,A_2,B_1,B_2\), with consecutive arc lengths \(\alpha,\beta,\gamma,\delta\). Feasibility gives \(\alpha,\gamma\ge h\). Move \(A_1\) counterclockwise to \(B_2\) through \(\delta\) steps and \(A_2\) clockwise to \(B_1\) through \(\beta\) steps. The clockwise separation from the first particle to the second only increases from \(\alpha\) to \(n-\gamma\), with both endpoints in \([h,n-h]\). These moves are therefore legal and take \(\beta+\delta=n-\alpha-\gamma\le n-2h=h-2\le q\). This completes the upper bound.

**3. A witness at distance \(q\) from every starting pair.** Rotational symmetry lets the arbitrary starting pair be \(A=\{0,d\}\) with \(h\le d\le n-h\). Choose nonnegative integers \(u,w\) satisfying \(u+w=q\): normally set \(u=\lfloor q/2\rfloor\), \(w=\lceil q/2\rceil\). In the sole exceptional boundary case when \(q\) is odd and \(d=n-h\), reverse these two choices. Let \(B=\{u,d+w\}\), with the displayed representatives interpreted as integers before reducing modulo \(n\). Elementary bounds using \(n=3h-2\), \(h\ge3\), show
\[
 0<u<d<d+w<n,\qquad h\le d+w-u\le n-h.
\]
Thus \(B\) is allowed. Write \(\delta_n(a,b)=\min\{(a-b)\bmod n,(b-a)\bmod n\}\) for the underlying circle distance. The two possible assignments of the particles in \(A\) to those in \(B\) have total circular lengths
\[
 \delta_n(0,u)+\delta_n(d,d+w)=u+w=q,
\]
\[
 \delta_n(0,d+w)+\delta_n(d,u)=(n-d-w)+(d-u)=n-q\ge q.
\]
The displayed equality for the second assignment uses \(d+w\ge n/2\) and \(d-u\le n/2\), immediate from the same bounds. In any legal sequence, each move moves one particle one circle edge. Tracking its identity through the sequence proves that the number of moves is at least the minimum circular assignment length. Therefore \(d_{T_{n,h}}(A,B)\ge q\). The upper bound from Step 2 shows equality. As \(A\) was arbitrary, **every** vertex has eccentricity \(q\), as asserted. \(\square\)

## Verification

Two complete standard-library Python programs accompany this result.

`verify_direct.py` constructs the original labelled cycle and enumerates every minimum-cardinality maximal matching directly by combinatorial subsets for \(n=7,10,13,16,19,22\). It builds the exchange graph without assuming that a legal exchange is a token slide, checks the complete vertex/edge correspondence to the separated-pair model, and computes every eccentricity by breadth-first search. Its final line is `CYCLE_MATCHING_DIRECT_ALL_PASS`.

`verify_two_token.py` independently constructs the separated-pair graph by coordinate moves for every \(n=3k+1\) with \(2\le k\le20\), checks connectivity and every eccentricity, verifies the explicit farthest-pair construction for every start, and for \(n\le25\) also checks the circular assignment-distance formula against exhaustive shortest paths (that stronger empirical formula is **not** asserted as a theorem here). Its final line is `TWO_TOKEN_ALL_ECCENTRICITIES_PASS`.

Execute `python verify_direct.py` and `python verify_two_token.py` from a directory containing the supplied files. The infinite-family proof is Steps 1–3; these finite checks provide independent implementation tests, not a substitute for proof.

## Relationship to prior work

Kamiński, Medvedev and Milanič (2010) developed token-sliding reconfiguration of independent sets. Suzuki, Mouawad and Nishimura (2014) studied reconfiguration of dominating sets, including the relevance of distances and diameter. These are historical motivation, not exact predecessors of the theorem. Teshima (2022 thesis, publicly deposited January 2023), and Brewster, Mynhardt and Teshima (March 2023), **already proved** the complete bracelet-graph description of minimum independent dominating sets of cycles, including the two-defect coordinate model and its adjacency. The earlier graph structure, component classification, configuration counts, and degrees are fully credited. The current proof adds the sharp, uniform **eccentricity** formula and its explicit farthest-configuration witness, which were not present in the inspected cycle sections of those sources.

## Limitations

The result applies only to the minimum maximal-matching sector of cycles of order \(3k+1\) with \(k\ge2\); it makes no claim for general graphs or nonminimum matching sectors. The underlying bracelet adjacency is previously published. A historical equivalent of the specific eccentricity theorem under other particle-configuration terminology remains possible, and no independent scholarly audit has been performed.

## References

1. M. Kamiński, P. Medvedev and M. Milanič, *Shortest paths between shortest paths and independent sets*, first posted August 26, 2010, arXiv:1008.4563, https://arxiv.org/abs/1008.4563.
2. A. Suzuki, A. E. Mouawad and N. Nishimura, *Reconfiguration of Dominating Sets*, first posted January 22, 2014, arXiv:1401.5714, https://arxiv.org/abs/1401.5714.
3. L. E. Teshima, *The i-Graph and Other Variations on the γ-Graph*, 2022 doctoral thesis, publicly deposited January 3, 2023, http://hdl.handle.net/1828/14602; especially Chapter 4, Sections 4.3–4.5.
4. R. C. Brewster, C. M. Mynhardt and L. E. Teshima, *The i-Graphs of Paths and Cycles*, first posted March 14, 2023, arXiv:2303.08190, https://arxiv.org/abs/2303.08190; especially Section 3.
