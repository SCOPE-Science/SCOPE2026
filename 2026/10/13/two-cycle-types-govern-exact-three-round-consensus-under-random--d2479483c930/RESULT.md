# Two cycle types govern exact three-round consensus under random perfect matchings

## Finding

Consider eight agents on a complete undirected communication graph. In each synchronous round, choose a perfect matching uniformly from the \(105\) matchings of the eight labeled vertices, independently across rounds. Every pair of matched agents replaces its two real states by their arithmetic mean. Put \(J_8=\mathbf{1}\mathbf{1}^{\mathsf T}/8\). For matching \(M\), let \(S_M\) be its vertex-swap permutation matrix and \(P_M=(I+S_M)/2\). Universal exact consensus at round \(t\) is the matrix identity \(P_{M_t}\cdots P_{M_1}=J_8\), so the update succeeds for *every* initial real vector, not merely for a particular realization of the data.

**Theorem.** Three is the least feasible number of rounds. With three independent uniform perfect matchings, the exact probability of universal exact consensus is
\[
\Pr\bigl(P_{M_3}P_{M_2}P_{M_1}=J_8\bigr)=\frac{32}{735}.
\]
Conditional on any prescribed first matching, the second matching belongs to exactly one of the following classes:

1. It shares an edge with the first matching: \(45\) choices, each with \(0\) completing third matchings.
2. Their union is a pair of disjoint alternating four-cycles: \(12\) choices, each with \(24\) completing third matchings.
3. Their union is one alternating eight-cycle: \(48\) choices, each with \(4\) completing third matchings.

Thus, conditional on the second matching being edge-disjoint from the first, its alternating-cycle type produces a sharp six-to-one contrast in the probability of completion during the next random round: \(24/105\) versus \(4/105\).

## Assumptions and scope

The state space is \(\mathbb R^8\). The underlying graph is complete, so every unordered perfect matching of the eight labeled vertices is admissible and has probability \(1/105\) on every round. The random matchings are mutually independent. Matching updates happen simultaneously; every pair averages with weights \((1/2,1/2)\), using states from the *start* of that round. Success means equality of linear operators with \(J_8\), not a numerical-tolerance criterion and not the occurrence of consensus for a particular initial vector. The agents are labeled; cycle-type counts refer to these labeled matchings. The first matching may be fixed arbitrarily by relabeling symmetry.

## Proof

**Step 1 (minimal number of rounds and support criterion).** Each row of \(P_M\) initially contains support on exactly the two endpoints of its edge. After \(t\) rounds of pairwise averaging, any row of the product depends on at most \(2^t\) original coordinates, because each averaging operation merges at most two previously obtained supports. Every row of \(J_8\) depends on all eight original coordinates, so \(t\geq3\). After two rounds, every row depends on at most four original coordinates. A third-round pair can depend on all eight originals only when both of its second-round rows have support of size four and those supports are disjoint. Conversely, under this condition, every final coefficient equals \(1/8\): each size-four second-round support was formed by averaging disjoint first-round pairs with coefficient \(1/4\) per original coordinate, and the last average halves these coefficients. Hence universal exact consensus after three rounds is *equivalent* to every third-matching edge pairing two second-round states with disjoint four-element supports.

**Step 2 (classify the second matching).** Fix the first matching and contract each of its four edges to one supervertex. For the second perfect matching, an edge repeated from the first creates a two-element second-round support, making completion at round three impossible by Step 1. If the two matchings share no edge, their union is a loopless two-regular multigraph on four supervertices (each supervertex has two incident second-matching half-edges). Such a multigraph is either the union of two doubled superedges or a simple four-cycle. On the original agents these are, respectively, two alternating four-cycles or one alternating eight-cycle.

There are \(105=(8-1)!!\) possible second matchings. By inclusion-exclusion, the number that avoid all four edges of the first matching is
\[
\sum_{j=0}^{4}(-1)^j\binom4j(7-2j)!!
=105-60+18-4+1=60,
\]
where \((-1)!!=1\). The two-four-cycle class has \(3\) ways to partition the four first-round supervertices into two unordered pairs, and \(2\) ways to connect the original endpoints in each supervertex pair, for \(3\cdot2^2=12\) second matchings. The one-eight-cycle class therefore contains \(60-12=48\) matchings. Exactly \(105-60=45\) share an edge with the first matching.

**Step 3 (complete the last round).** For two disjoint alternating four-cycles, the second round produces four states supported uniformly on each of two disjoint four-element blocks of original agents. Every third-round pair must cross between the two blocks. There are \(4!=24\) perfect matchings that do so.

For one alternating eight-cycle, the second-round four averaging pairs carry the supports of the four *edges* of a simple cycle on the four first-round supervertices. Each of those edge-support types occurs twice, once at each endpoint of its second-matching edge. The only complementary support types are opposite edges of that simple four-cycle. The third matching must bijectively pair the two states of each edge-support type with the two states of its opposite edge-support type. These choices number \((2!)^2=4\). Any other third matching overlaps at least one constituent support and fails Step 1.

**Step 4 (the exact law).** For every first matching there are consequently \(12\cdot24+48\cdot4=480\) successful ordered choices of the second and third matchings, among \(105^2=11025\) equally likely pairs. All first matchings are related by relabeling, giving the unconditional probability \(480/11025=32/735\). The number of completions in the two nontrivial classes is \(24\) versus \(4\), establishing the sixfold contrast. Both are positive, proving that the minimum of three rounds is attainable. \(\square\)

## Verification

The standalone `verify.py` enumerates all \(105\) perfect matchings by an exact recursive pairing algorithm. After three rounds, it stores each row of the *unnormalized* product \(8P_{M_3}P_{M_2}P_{M_1}\) as eight integers and checks the identity against the all-ones matrix, with no floating-point arithmetic. For an arbitrarily fixed first matching it exhaustively tests \(105^2=11025\) second/third choices and separately classifies every second matching by the alternating-cycle type. It checks exactly \(45,12,48\) second-matching choices and \(0,288,192\) successful completions, giving \(480\) total; a second choice of first matching independently repeats the \(480\) total. Run with `python verify.py` from the directory containing that file. The analytic counting argument above, not this finite computation, establishes the mathematical claim.

## Relationship to prior work

Loizou and Richtárik introduced a sketch-and-project interpretation of randomized gossip; their §3.4 identifies block Kaczmarz gossip as averaging within the connected components of a randomly selected edge subgraph, encompassing disjoint simultaneous pair averaging. Their convergence guarantees are spectral/in-expectation rather than the exact three-round probability for iid uniform perfect matchings. Ko's earlier finite-time average-consensus analysis constructs optimal hypercube schedules and establishes power-of-two restrictions; its deterministic construction does not give this matching-distribution law. Shi, Anderson, and Johansson treat almost-sure finite-time consensus for stochastic graph processes; their existence criteria and bounds do not determine the three-round probability or the distinct alternating-cycle completion counts. Boyd and colleagues analyze randomized gossip and synchronous/asynchronous averaging times, not the same exact uniform-perfect-matching enumeration.

## Limitations

The result concerns eight labeled agents on a complete graph, independently sampled *uniform perfect matchings*, equal-weight exact arithmetic, and universal exact consensus. It does not classify nonuniform matching laws, other graph constraints, other network sizes or convergence to within a positive tolerance. Some special initial vectors can reach consensus earlier, including vectors that are initially constant; those events are not covered by the universal operator identity. Although the exact count is proved, unindexed combinatorial enumerations or alternative presentations might already contain this particular probability.

## References

1. N. Loizou and P. Richtárik, “Revisiting Randomized Gossip Algorithms: General Framework, Convergence Rates and Novel Block and Accelerated Protocols,” arXiv:1905.08645, first submitted 2019-05-20, §3.4. https://arxiv.org/abs/1905.08645 ; https://arxiv.org/html/1905.08645v2
2. C.-K. Ko, “On Matrix Factorization and Scheduling for Finite-Time Average-Consensus,” Caltech thesis, 2010, Chapter 4. https://thesis.caltech.edu/5763/01/consensus.pdf
3. G. Shi, B. D. O. Anderson, and K. H. Johansson, “Consensus over Random Graph Processes: Network Borel-Cantelli Lemmas for Almost Sure Convergence,” arXiv:1112.1336, first submitted 2011-12-06, Theorem 5 and Appendix C. https://arxiv.org/abs/1112.1336 ; https://arxiv.org/html/1112.1336v5
4. S. Boyd, A. Ghosh, B. Prabhakar, and D. Shah, “Randomized Gossip Algorithms,” IEEE Transactions on Information Theory 52 (2006), 2508–2530. https://web.stanford.edu/~boyd/papers/pdf/gossip.pdf
