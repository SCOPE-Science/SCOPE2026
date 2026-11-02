# Majority orbit transitions after deleting a matching from a complete graph

## Finding

Let \(E_{m,r}\) and \(Q_{m,r}\) denote the exact numbers of fixed configurations and primitive temporal two-cycle *orbits* of synchronous binary majority dynamics on the labelled graph \(G_{m,r}=K_{2m+r}\setminus M\), where \(M\) is a fixed matching of size \(m\). For every integer \(m\ge4\) and \(r\ge0\), writing \(n=2m+r\), the full recurrence census is

\[
(E_{m,r},Q_{m,r})=
\begin{cases}
\left(2+2^m,\frac12[\binom{2m}{m}-2^m]\right),&r=0,\\
\left(2,\frac12\binom{n}{n/2}\right),&r\ge2\text{ even},\\
\left(2,\binom{m}{\lceil m/2\rceil}\right),&r=1,\\
\left(2,\binom{m}{(n+1)/4}\right),&r\ge3\text{ odd},\ n\equiv3\pmod4,\ r\le 2m-1,\\
(2,0),&r\ge3\text{ odd and otherwise}.
\end{cases}
\]

There are no longer cycles. Every initial configuration enters its ultimate periodic orbit after at most three synchronous updates; for even \(n\), the bound improves to one. The bound of three is attained at \((m,r)=(5,3)\).

In particular, **every even-order** \(G_{m,r}\) has exactly \(2+\binom{n}{n/2}\) periodic configurations, the same as the complete graph on the same number of vertices. Deleting a *perfect* matching creates exactly \(2^m\) balanced fixed configurations, correspondingly reducing the number of primitive two-cycles by \(2^{m-1}\) relative to a complete even-order graph. With at least two unmatched vertices this fixed-point fusion disappears.

On **odd-order** graphs the change is starker: an undeleted odd clique has no primitive two-cycle, while deleting a near-perfect matching produces \(\binom{m}{\lceil m/2\rceil}\) such orbits. With three or more unmatched vertices, their presence is controlled jointly by the congruence \(n\equiv3\pmod4\) and the sharp inequality \(r\le2m-1\).

## Assumptions and scope

The graph is finite, undirected, simple and labelled. The first \(2m\) vertices are partitioned into \(m\) specified disjoint nonedges; the remaining \(r\) vertices are adjacent to everybody else. All spins are in \(\{-1,+1\}\). All vertices update at the same integer time, taking the sign of the sum of **neighbor** spins, except that a zero neighbor sum preserves the current vertex spin. A primitive temporal two-cycle means the unordered pair of two *distinct* labelled states mutually mapped to each other by one update. No vertex-relabeling quotient is taken. No assertion is made for differently chosen tie-breaking rules, asynchronous dynamics or nonmatching deleted edges.

## Proof

Set \(S=\sum_{v}s_v\). For a matched pair \(\{v,w\}\) the neighbor sum at \(v\) is \(S-s_v-s_w\), while for an unmatched vertex \(u\) it is \(S-s_u\). These are **all** local inputs, so the following cases exhaust every labelled configuration.

**Even order.** Here \(r\) and \(S\) are even. If \(|S|\ge2\), every spin becomes \(\operatorname{sgn}(S)\) in one update. This includes the boundary \(|S|=2\): a paired vertex initially agreeing with the sign may have a zero neighbor sum, but the tie rule preserves precisely the sign required. If \(S=0\), a homogeneous matched pair of two positive (respectively negative) spins changes to two negative (respectively positive) spins; a mixed pair is unchanged; every unmatched spin flips. The global sum remains zero and a second update restores the entire configuration. Thus every balanced state is periodic, and nonbalanced states reach one of the two unanimous fixed states in one update. The number of balanced states is \(\binom{n}{n/2}\). A balanced state is fixed exactly when every matched pair is mixed **and** no unmatched vertex is present, giving \(2^m\) fixed balanced configurations for \(r=0\) and none for \(r>0\). Since all remaining periodic states occur in disjoint pairs, the even-order formulas follow.

**Odd order: the periodic restriction.** Now \(r\) and \(S\) are odd. If \(|S|\ge3\), one update produces unanimity. At \(S=+1\), a matched \((+,+)\) pair becomes \((-,-)\), a \((-,-)\) pair becomes \((+,+)\), a mixed pair becomes \((+,+)\), and every unmatched vertex becomes positive. At \(S=-1\) the symmetric rules hold, with a mixed pair becoming \((-,-)\) and every unmatched vertex becoming negative. A mixed pair cannot reappear once homogenized. Thus a nonunanimous periodic configuration must have **all matched pairs homogeneous**, all unmatched vertices identical, and \(S=\pm1\). The two unanimous configurations are the only fixed points: every homogeneous pair switches sign in the small-sum regime.

**Odd order: cycle census.** In an \(S=+1\) periodic candidate let \(a\) count positive matched pairs and let \(u\) count positive unmatched vertices. Necessarily \(u\in\{0,r\}\), and

\[
4a-2m+2u-r=1.
\]

After one update, all matched-pair signs reverse, all \(r\) unmatched vertices become positive, and the new total spin is \(S'=2u-1\). If \(u=0\), then \(S'=-1\); the next update returns exactly to the original state. The equation forces \(a=(2m+r+1)/4=(n+1)/4\), an integer in \([0,m]\) precisely when \(n\equiv3\pmod4\) and \(r\le2m-1\). Every such orbit has exactly one phase with total spin \(+1\), so this gives \(\binom{m}{(n+1)/4}\) two-cycles.

If \(u=r\), then \(S'=2r-1\). For \(r\ge3\), the next state is unanimous, so no further periodic state arises. For \(r=1\), \(S'=+1\), and the equation requires \(a=m/2\), hence even \(m\). The phases of each resulting cycle both have total spin \(+1\); they give \(\frac12\binom{m}{m/2}\) orbits. The global spin reversal gives another \(\frac12\binom{m}{m/2}\) cycles whose phases have spin \(-1\). If \(r=1\) and \(m\) is odd, the preceding \(u=0\) case instead gives \(\binom{m}{(m+1)/2}\) cycles. These cases are disjoint and yield exactly the stated odd-order formulas.

**Transient bound.** If an odd-order initial state has \(|S|\ge3\), it reaches unanimity in one step. Otherwise, after its first update every matched pair is homogeneous and all unmatched vertices have the same spin. If the new total spin has magnitude at least three, the second update yields unanimity. If it is \(\pm1\), the preceding exhaustive analysis shows either a nonunanimous periodic configuration or, after at most one further nonunanimous update, a state of total-spin magnitude at least three. Therefore a periodic state is reached by update three. Sharpness is witnessed when \((m,r)=(5,3)\): place positive spins on six paired vertices (three full positive pairs) and on one unmatched vertex, with every other spin negative. Under the natural labelling, the successive bitmask states, with the positive spins as set bits, are \(1087\), \(8128\), \(7231\), and \(8191\); the last is the first periodic state.

This argument is exact for all stated integers; finite verification is supplementary, not the basis for the infinite classification.

## Verification

The embedded Python program `check_matching_majority.py` constructs the actual open-neighborhood sets and directly computes the simultaneous map on every binary state for each pair of parameters with \(4\le2m+r\le16\) and \(m\ge1\). It compares the measured fixed-state count and primitive two-cycle count with the formulas, verifies the three-step eventual-periodicity property for every tested configuration, and checks the three-step witness above. A fresh replay prints `PASS 62 graph parameter pairs; 961184 configurations examined`. The exhaustive computation covers finite orders only; the complete classification for arbitrary \(m\) and \(r\) rests on the preceding proof.

To reproduce from the separately extracted files, run `python3 check_matching_majority.py`; expected output is embedded as `verification_output.txt`.

## Relationship to prior work

Goles and Olivos established eventual period at most two for general finite symmetric threshold dynamics. Benjamini, Chan, O'Donnell, Tamuz and Tan restate this general theorem and study broader majority dynamics on random and unimodular graphs. That result does **not** count the recurrent configurations or their two-cycle orbits for these deleted-matching cliques. Voutsadakis studies limit cycles of threshold networks on complete digraphs with symmetric local functions; its complete-neighborhood update structure is not this missing-partner input structure. Adams, Brass, Stokes and Troxell examine **irreversible** conversion on complete multipartite graphs, so their dynamical assumption differs. Previously recorded special cases on complete tripartite and complete split graphs do not give the two-parameter deleted-matching classification in the stated range \(m\ge4\). Searches using the labels *cocktail-party graph*, *clique with a matching removed*, *complement of a matching*, and *complete multipartite with parts of size one and two* did not identify a source asserting the same orbit formulas; this is a best-knowledge comparison, not an assertion that absence of indexing proves priority.

## Limitations

The conclusion is specific to synchronous, reversible, strict open-neighborhood majority with retention on ties and a deleted matching. Historical literature may use equivalent representations not recovered in searches. Some older primary sources were not available for full-text inspection; their relevance and the residual priority risk are recorded in the accompanying review. Small exhaustive computations do not establish an infinite theorem. Scientific validation beyond the embedded reproducibility checks and self-review is not supplied.

## References

1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, 11 May 2014. https://arxiv.org/abs/1405.2486v1.
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI:10.1016/0012-365X(80)90121-1.
3. G. Voutsadakis, *On the limit cycle structure of threshold Boolean networks over complete graphs*, International Journal of Neural Systems 14 (2004), 209–215. https://www.voutsadakis.com/RESEARCH/PUBLISHED/limcyc.pdf.
4. S. S. Adams, Z. Brass, C. Stokes and D. S. Troxell, *Irreversible k-threshold and majority conversion processes on complete multipartite graphs and graph products*, arXiv:1102.5361, 25 February 2011. https://arxiv.org/abs/1102.5361.
