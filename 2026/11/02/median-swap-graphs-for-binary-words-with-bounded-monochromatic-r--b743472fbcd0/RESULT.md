# Median swap graphs for binary words with bounded monochromatic runs

## Finding

**Theorem.** Fix integers \(n\ge1\), \(0\le k\le n\), and \(r,s\ge2\). Let \(\mathcal W_{n,k}(r,s)\) be the length-\(n\) binary words with exactly \(k\) ones, containing neither \(0^r\) nor \(1^s\) as a contiguous factor. Join two words when they differ by one adjacent interchange \(01\leftrightarrow10\) and both belong to \(\mathcal W_{n,k}(r,s)\). If this set is nonempty and \((r,s)\ne(2,2)\), its reconfiguration graph is a **median graph** and, more precisely, the cover graph of a finite distributive lattice. For two words, let \(p_1<\cdots<p_k\) and \(q_1<\cdots<q_k\) be the positions of their ones. Their exact graph distance is

\[
 d(w,v)=\sum_{i=1}^k|p_i-q_i|.
\]

This is the ordinary adjacent-interchange (earth-mover) lower bound: no extra moves are ever needed to maintain *both* run-length restrictions. In particular every nonempty sector is connected, and a shortest legal exchange sequence can be constructed by monotone coordinate moves. The diameter is \(\sum_i(\beta_i-\alpha_i)\), where \(\alpha\) and \(\beta\) are respectively the componentwise least and greatest feasible particle-position vectors; for the complementary-coordinate case below, use zero positions instead.

For three configurations, their unique graph median has the componentwise median of their ordered one-positions whenever \(r\ge3\), or of their ordered zero-positions when \(r=2,s\ge3\).

The exclusion of \((2,2)\) is sharp: at \(n=4,k=2\) the two legal words `0101` and `1010` are isolated, so their exchange graph is disconnected.

## Assumptions and scope

Positions are indexed \(1,\ldots,n\). A factor is a consecutive substring. Adjacent interchange means exchanging two unequal neighboring symbols in the *linear* word, not cyclically around its ends. A sector is a fixed pair \((n,k)\); no change of Hamming weight is permitted. Empty or one-vertex sectors are not asserted to contain paths between distinct vertices; every nonempty singleton is median. All parameters in the theorem are integers. We never identify words under rotation or reversal.

The proof uses \(r\ge3\) and \(s\ge2\), then invokes symbol complementation for \(r=2,s\ge3\). For \(k=0\) or \(k=n\) there is at most one word, so these cases are immediate. Henceforth assume \(1\le k<n\).

## Proof

**1. Exact positional model.** For \(r\ge3\), encode each word by the increasing positions \(p=(p_1,\ldots,p_k)\) of its ones. Absence of \(0^r\) is equivalent to

\[
 p_1\le r,\qquad p_{i+1}-p_i\le r\ (1\le i<k),\qquad p_k\ge n-r+1.
\]

Distinct positions impose \(p_1\ge1\), \(p_k\le n\), and \(p_{i+1}-p_i\ge1\). Absence of \(1^s\) is precisely

\[
 p_{i+s-1}-p_i\ge s\qquad (1\le i\le k-s+1),
\]

with no such inequalities if \(k<s\). These are necessary and sufficient: a run of \(s\) ones is equivalent to \(s\) successive one-positions occupying \(s\) consecutive sites. Every listed condition is an upper or lower *difference constraint* between coordinates (or a bound on a coordinate).

**2. Distributive lattice.** For any two feasible vectors \(p,q\), both their componentwise minimum \(p\wedge q\) and maximum \(p\vee q\) satisfy every constraint. Indeed, for a generic inequality \(x_i-x_j\le c\), \(\max(p_i,q_i)-\max(p_j,q_j)\le c\), by choosing the vector realizing the maximum at coordinate \(i\). Likewise \(\min(p_i,q_i)-\min(p_j,q_j)\le c\), choosing the vector realizing the minimum at coordinate \(j\). Reverse-index inequalities and coordinate bounds are handled identically. Thus feasible vectors form a finite distributive sublattice of the coordinatewise-ordered integer lattice.

**3. A monotone single-step path.** Let \(z\le p\) be feasible vectors, componentwise. If \(p\ne z\), some coordinate \(p_i>z_i\) can be decreased by one without losing feasibility. To prove this, suppose an eligible decrease is blocked. Only three kinds of tight constraints can block it:

- \(p_i-p_{i-1}=1\) (if \(i>1\)), forcing a decrease of coordinate \(i-1\) first;
- \(p_i-p_{i-s+1}=s\) (if \(i\ge s\)), forcing a decrease of coordinate \(i-s+1\) first;
- \(p_{i+1}-p_i=r\) (if \(i<k\)), forcing a decrease of coordinate \(i+1\) first.

In each case the indicated coordinate \(j\) also satisfies \(p_j>z_j\), because otherwise feasibility of \(z\) would be contradicted. A lower absolute bound cannot block an eligible decrease: if \(p_1=1\) or \(p_k=n-r+1\), then \(z\le p\) cannot be strictly smaller in that coordinate.

Draw a directed dependency \(i\to j\) for every possible blocking constraint. Place a barrier between indices \(t,t+1\) precisely when \(p_{t+1}-p_t=r\). Every **forward** dependency \(i\to i+1\) crosses a barrier. Every **backward** dependency stays within a barrier-free block. The short one-step backward dependency has gap \(1<r\). A long backward dependency has total separation exactly \(s\) across \(s-1\) positive gaps; if any were \(r\ge3\), this total would be at least \(r+s-2\ge s+1\), impossible. Consequently, directed dependencies progress forward only across barriers and backward only within a block. They have no directed cycle. Among eligible coordinates there is therefore a sink, with no blocking dependency; decreasing it is legal.

Iterate until \(z\). Each step decreases exactly one coordinate by one, so the resulting path has length \(\sum_i(p_i-z_i)\).

**4. Distances and median.** Given two feasible vectors \(p,q\), their meet \(z=p\wedge q\) is feasible. Apply Step 3 to obtain legal monotone paths from \(p\) to \(z\) and from \(q\) to \(z\), reversing the second. Their total length is

\[
 \sum_i(p_i-z_i)+\sum_i(q_i-z_i)=\sum_i|p_i-q_i|.
\]

An adjacent swap moves one ordered one-position by exactly one; therefore every path has at least this length. This proves the exact distance formula and connectivity. Since any coordinatewise-comparable pair admits the monotone path, a covering relation in the feasible-vector lattice necessarily moves just one coordinate by one. Conversely, each legal move is such a cover. Thus the reconfiguration graph is its undirected Hasse graph.

The coordinatewise median of three feasible vectors is feasible by Step 2 (it is a lattice expression in meets and joins). The proved \(\ell^1\) distance formula shows that this vertex lies on shortest paths between each pair. It is unique because, in each integer coordinate, the intersection of the three pairwise numerical intervals is the singleton containing the middle value. Hence the graph is median. Every feasible coordinate lies between the least vector \(\alpha\) and greatest vector \(\beta\), so the distance upper bound \(\sum_i(\beta_i-\alpha_i)\) is attained by these two and equals the diameter.

**5. Complementation and sharp boundary.** If \(r=2,s\ge3\), interchange zero and one in every word. This exchanges the two run bounds and fixes adjacency, putting the problem into Steps 1–4 with \(s\ge3\) as its zero-run bound. The earth-mover sum using zero positions equals the one-position sum: both equal the sum, over cuts between successive word sites, of the absolute difference in the number of ones to the left of each cut. Finally, if \(r=s=2\), the length-four words `0101` and `1010` are the two feasible words of weight two, and no adjacent swap from either avoids `00` and `11`. This proves the stated sharp exception.

## Verification

The standalone Python program `verify_descent.py` reconstructs feasible particle vectors, checks closure under meet and join, and constructs a legal monotone descent for every comparable pair obtained from every two states, for lengths through \(10\) and run bounds \(2\) through \(5\) excluding the documented exceptional pair. The independently implemented C++17 program `verify_bfs.cpp` constructs the complete bitmask exchange graph and performs an exhaustive breadth-first search from every word through length \(11\), independently comparing every graph distance with the positional earth-mover formula. Both also check the exceptional length-four case. They are finite corroboration, not the proof for arbitrary parameters.

Reproduce using `python verify_descent.py` and `g++ -O2 -std=c++17 verify_bfs.cpp -o verify_bfs && ./verify_bfs` in a directory containing those files.

## Relationship to prior work

Bilotta, Pergola and Pinzani (2011) study enumeration and constructive generation of binary words avoiding a *single different* block pattern; their results do not supply an exchange graph or its metric for words simultaneously avoiding both monochromatic runs. Demaine and coauthors (2014) study token-sliding reachability in independent sets on trees, whose feasible objects impose separation but not the simultaneous upper/lower run constraints here. Avis and Hoang (2022/2023) study graph classes and structural properties of independent-set token-slide graphs and mention connectedness for ordinary independent sets of paths; neither such connectedness nor its methods establishes median geometry and exact geodesics under the additional no-long-zero-run constraint.

The elementary fact that the cover graph of a finite distributive lattice is median is classical, and the usual adjacent-swap earth-mover lower bound is classical. The contribution asserted here is **not** either general fact: it is the run-bound-specific proof that the physically permitted adjacent swaps realize *all* lattice covers and preserve every pairwise shortest distance for all nonexceptional integer parameters. An equivalent result could appear under constrained lattice paths, height functions, bounded-gap exclusion, or distributive reconfiguration terminology; this is an unresolved literature risk.

## Limitations

The words are linear, not cyclic. Multiple-symbol alphabets, arbitrary forbidden-pattern families, weighted exchanges, and non-adjacent moves are not covered. A uniform formula for the number of valid words at each fixed weight is not claimed. The breadth-first search checks are finite and do not substitute for the general proof.

## References

1. S. Bilotta, E. Pergola, and R. Pinzani, *Pattern \(1^j0^i\) avoiding binary words*, Electronic Proceedings in Theoretical Computer Science **63** (2011), 53–64. First arXiv posting 2011-08-18, arXiv:1108.3621v1, DOI: 10.4204/EPTCS.63.9.
2. E. D. Demaine et al., *Polynomial-Time Algorithm for Sliding Tokens on Trees*, ISAAC 2014, 389–400; arXiv:1406.6576, first posted 2014-06-25. See also the 2015 journal version, *Linear-Time Algorithm for Sliding Tokens on Trees*.
3. D. Avis and D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861 (2022), published in Graphs and Combinatorics (2023).
