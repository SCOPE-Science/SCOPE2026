# Cycle-rank best-edge balancing is geodesic on networks of parallel-path blocks

## Finding

Let a connected simple signed network have blocks consisting only of bridges and *parallel-path blocks*: each nontrivial block consists of \(r_B\ge2\) internally vertex-disjoint paths of lengths at least two between the same two terminals. Within each block, let \(k_B\) of its \(r_B\) path-sign products be negative and put \(d_B=\min\{k_B,r_B-k_B\}\).

Define **cycle-rank best-edge dynamics** as follows: choose any negative simple cycle, and flip a sign on any edge maximizing the number of negative simple cycles containing that edge, among the edges of the chosen cycle. Every permitted trajectory, including arbitrary choices and ties, reaches structural balance after **exactly**
\[
T=\sum_B d_B
\]
flips. This is the minimum number of individual edge-sign reversals required to reach any balanced signing, so *every trajectory is a shortest path to balance*. No cycle rank restriction is needed: the blocks can have arbitrarily many internally disjoint paths, and cycles within one block overlap extensively.

If \(E\) denotes the number of negative simple cycles, an update in a block with \(r=r_B\) and current minority count \(d=d_B>0\) strictly reduces \(E\) by exactly \(r-2d+1\). Hence there are no nonbalanced stationary states, blinker cycles, or energetically uphill moves on this network class under the specified rule.

Under the additional stochastic convention that the negative simple cycle is drawn uniformly among all currently negative simple cycles and, within it, a maximal-rank edge is chosen uniformly, consider a block initially tied with \(r=2k\) paths of each sign. Label its negative paths by \(i\) and its positive paths by \(j\), with path lengths \(\ell_i\). The probability that its final *common path-sign product* is positive is exactly
\[
\Pr(q_B=+1)=\frac1{k^2}\sum_{i:\,p_i=-1}\ \sum_{j:\,p_j=+1}\frac{\ell_i}{\ell_i+\ell_j}.
\]
Untied blocks retain their initial majority path sign with probability one. In particular, for four path lengths \((2,3,4,5)\), with the first and third paths initially negative, the positive final path-parity probability is \(134/315\), rather than \(1/2\).

## Assumptions and scope

The underlying graph \(U=(V,E_U)\) is finite, connected, simple and undirected. Every edge is assigned a sign \(s_e\in\{-1,+1\}\). Every non-bridge maximal two-vertex-connected block is a union of \(r\ge2\) simple paths between distinct terminals, where the paths have pairwise disjoint interiors and each has at least two edges. Different blocks may meet at cutvertices but have no common edge. An isolated bridge is itself a block and plays no part in the dynamics. The case of two paths includes ordinary cycle blocks.

For a path \(P_i\) in a block, its parity/sign is \(p_i=\prod_{e\in P_i}s_e\). A simple cycle is *negative* if the product of its edge signs is negative, and *positive* otherwise. A signing is structurally balanced if all simple cycles are positive. Each distinct undirected simple cycle is counted once, without orientation or basepoint multiplicity. At each step, define edge rank \(\rho(e)\) as the number of currently negative simple cycles containing \(e\). Select **one negative simple cycle**, arbitrarily or by a probability law; from its edges select one with largest \(\rho(e)\) and reverse its sign. No idle/non-flipping steps occur.

The final-path-sign probability formula additionally requires uniform sampling of a negative simple cycle at each step and uniform edge selection among the maximizing edges of that cycle, with fresh random choices. It concerns path-sign products, not a unique final assignment of signs to individual edges.

## Proof

**1. Exact cycle decomposition.** A simple cycle cannot use edges from two distinct blocks, because visiting two blocks would force it through their separating cutvertex twice. Within a parallel-path block, every simple cycle uses exactly two distinct terminal-to-terminal paths: there is no branching at an internal vertex, and after travelling from one terminal to the other it must return along a different path. Conversely, the union of any two distinct paths is a simple cycle. Thus the simple cycles in block \(B\) are precisely \(C_{ij}=P_i\cup P_j\) for \(i<j\).

**2. Rank and energy formulas.** The sign of \(C_{ij}\) is \(p_i p_j\), so \(C_{ij}\) is negative exactly when the two path signs differ. If \(k\) out of \(r\) paths have negative sign, the number of negative simple cycles in this block is exactly \(k(r-k)\). Every edge of a negative-sign path belongs to exactly \(r-k\) negative cycles, while every edge of a positive-sign path belongs to exactly \(k\). No cycle from another block contains this edge. Summing over the blocks gives
\[
E=\sum_B k_B(r_B-k_B).
\]

**3. Every allowed move removes exactly one minority path.** Take any negative selected cycle. It consists of one negative and one positive path. If \(k<r/2\), the negative path is the strict minority, and its edges have rank \(r-k>k\). The rule therefore flips an edge on the negative path, changing that path product to positive. If \(k>r/2\), the positive path is the strict minority and is flipped instead. If \(k=r/2\), both paths have equal rank, and flipping either resolves the tie to a strict majority; in both cases the new minority count is \(d-1\) where \(d=\min\{k,r-k\}\). No other block's count changes. Hence the integer potential \(D=\sum_B d_B\) drops by exactly one after every step. If \(D>0\), some block has opposite path signs and hence contains a negative simple cycle. Thus every legal sequence lasts exactly its initial \(D\) steps and terminates in a balanced signing.

The value of \(k(r-k)\) depends only on \(d\) and equals \(d(r-d)\). Its one-step decrement is
\[
d(r-d)-(d-1)(r-d+1)=r-2d+1\ge1,
\]
which establishes the exact strict descent of the negative-simple-cycle count.

**4. Global shortest-path optimality.** One edge reversal changes the product of exactly one path within exactly one nontrivial block; a bridge reversal changes no cycle parity. In order for a block to become balanced, all of its path products must agree, requiring at least \(\min\{k_B,r_B-k_B\}=d_B\) path changes from the initial signing, regardless of the intermediate moves. Since different blocks are edge-disjoint, any edge-reversal sequence ending in a balanced signing requires at least \(\sum_B d_B\) flips. The constructed dynamics achieves that lower bound, proving exact optimality.

**5. Stochastic tie law.** Suppose a given block initially has \(k\) negative and \(k\) positive paths. Before the first update in this block, its path signs are unchanged, even if other blocks have updated. Conditional on the first selected cycle lying in this block, the uniformly sampled negative cycle is a uniformly selected pair \((i,j)\) of one negative and one positive path, among \(k^2\) choices. Both constituent paths have equal edge rank \(k\), so every edge of their union is a maximizer. If their lengths are \(\ell_i,\ell_j\), the probability that the first change flips a negative path is \(\ell_i/(\ell_i+\ell_j)\). Once this happens, the positive paths form a strict majority, and the deterministic rank comparison ensures that every subsequent local flip converts another negative path to positive; the final common product is therefore positive. Conversely, a first flip on a positive path yields a final negative common product. Averaging these conditional probabilities over the \(k^2\) pairs proves the formula. Every initially imbalanced block is eventually selected because the global integer potential reaches zero after finitely many steps. The formula is unaffected by how updates in different blocks interleave.

## Verification

The accompanying standalone `verify_banana.py` uses only the Python standard library. It enumerates undirected simple cycles independently by depth-first search on the assembled graph, checks their equality with all predicted two-path unions, enumerates every signing of seven small single- or two-block hosts, and for every legal maximal-rank move recomputes the global shortest reversal distance by an exhaustive Hamming search over balanced signings. It verifies both the strict decrease of negative cycles and the exact shortest-path property. The script also independently enumerates the tie choices with rational arithmetic.

Run from the directory containing this document and the checker:

```text
python verify_banana.py
```

The reported exhaustive coverage is 9,168 sign states and 77,792 legal maximal-rank transitions across seven host specifications, together with three exact tie-probability cases. These are finite checks only; the all-size theorem relies on the preceding cycle decomposition and rank proof, not on finite testing.

## Relationship to prior work

Chatterjee, Svoboda, Žikelić, Pavlogiannis and Tkadlec (2022) introduce best-edge dynamics based on imbalanced *triangles* in complete signed networks, prove almost-sure convergence there, and explicitly identify general sparse-network extensions as an open direction. The rule studied here is a **separately specified cycle-based variant**, using all negative simple cycles and their edge-incidence ranks; it is not the original triangle-only rule on arbitrary sparse networks. The present claim establishes all-choice, shortest-path convergence and a stochastic outcome law on the stated noncomplete block class; neither follows from the cited complete-network theorem.

Giscard, Rochet and Wilson (2016) develop exact and sampled counts of signed simple cycles, not this update rule. Cappello and Steffen (2022) investigate frustration-critical signed graphs and switching equivalence, providing relevant structural background but not the claimed all-trajectory greedy optimality. Global frustration-index optimization predates these works; the formula for minimum flips alone is not claimed to originate here. Katai and Iwai (1978) consider minimum balancing processes by blocks on general graphs, a plausible older antecedent for the optimization component. Only its accessible abstract was examined, so no claim is made that its full text excludes specialized trajectory results. The combination of all-tie-break geodesicity, strict cycle-count descent on unbounded overlapping-cycle networks, and length-dependent tie law is the contribution assessed here.

## Limitations

The theorem requires the specified parallel-path block structure, unit counting of all distinct negative simple cycles, and a single sign reversal per step. It does not establish convergence on arbitrary sparse graphs, for the original triangle-only best-edge rule in the absence of triangles, or for cycle-length-weighted and vertex-weighted selection ranks. The final edge-level signing is generally not unique; the tie law concerns path products only. Full-text priority verification against Katai–Iwai (1978) remains incomplete. Independent mathematical validation has not been performed.

## References

1. K. Chatterjee, J. Svoboda, Đ. Žikelić, A. Pavlogiannis, and J. Tkadlec, "Social balance on networks: Local minima and best-edge dynamics," *Physical Review E* **106**, 034321 (2022), DOI: https://doi.org/10.1103/PhysRevE.106.034321; public preprint https://arxiv.org/abs/2210.02394.
2. P.-L. Giscard, P. Rochet, and R. C. Wilson, "Evaluating balance on social networks from their simple cycles" (2016), https://arxiv.org/abs/1606.03347.
3. C. Cappello and E. Steffen, "Frustration-critical signed graphs," *Discrete Applied Mathematics* **322**, 183–193 (2022), https://arxiv.org/abs/2112.02664.
4. O. Katai and S. Iwai, "Studies on the balancing, the minimal balancing, and the minimum balancing processes for social groups with planar and nonplanar graph structures," *Journal of Mathematical Psychology* **18**, 140–176 (1978), https://doi.org/10.1016/0022-2496(78)90060-3 (abstract inspected; full text not verified).
5. G. Facchetti, G. Iacono, and C. Altafini, "Computing global structural balance in large-scale signed social networks," *PNAS* **108**, 20953–20958 (2011), https://doi.org/10.1073/pnas.1109521108.
