# Sharp five-vertex onset of stochastic recurrent majority dynamics

## Finding

Consider synchronous binary random-majority dynamics on finite, simple, connected, undirected graphs, using all neighbors but not a vertex itself: strict neighbor majority determines the next opinion, and independent fair coins settle neighbor ties. An **absorbing recurrent class** is a terminal strongly connected component in the directed support graph of the finite-state Markov chain. Its size counts possible recurrent opinion configurations, not its temporal period.

**Sharp onset and complete first layer.** For every connected graph on between two and four vertices, every absorbing recurrent class has size at most two. At five vertices the sharp upper bound becomes four. Among the 728 connected labelled graphs on five specified vertices, exactly 135 possess an absorbing class of size four. Those 135 graphs comprise precisely three isomorphism classes, with 60, 60, and 15 labelled realizations. Each has exactly one four-state absorbing class, and no five-vertex graph has an absorbing class larger than four. The four-state classes all have Markov-chain period two, rather than period four.

The three canonical representatives have five, six, and eight edges, respectively. Number vertices from 0 through 4, list potential edges in lexicographic order, and use an integer bit mask to encode the edge set. Their canonical masks are `59`, `221`, and `495` respectively; `verify.py` prints all corresponding edge lists and their four-state classes.

**General mechanism.** For any finite simple graph admitting a partition \(V=A\sqcup B\sqcup\{u\}\) with nonempty \(A,B\), define \(d_X(v)=|N(v)\cap X|\). Suppose

\[
d_A(u)=d_B(u)>0,
\]

and for every \(a\in A\), \(b\in B\), respectively,

\[
d_B(a)>d_A(a)+\mathbf 1_{\{au\in E\}},\qquad
 d_A(b)>d_B(b)+\mathbf 1_{\{bu\in E\}}.
\]

Then the four configurations in which \(A\) and \(B\) are internally monochromatic and oppositely colored, while \(u\) has either opinion, form an absorbing strongly connected class of size four. The two blocks change opinion deterministically on every round, and \(u\) tosses an independent fair coin on every round. In its stationary law each of the four configurations has probability \(1/4\). The support-based claims also hold for any fixed independent tie-breaking bias strictly between zero and one, although the stationary weights need not then be equal.

## Assumptions and scope

Each graph is finite, undirected, loopless, unweighted and simple. In one synchronous round every vertex compares the numbers of its neighbors holding each of two opinions; strict majorities are compulsory, and neighbor ties are resolved independently at each vertex and time. Random ties have positive probabilities for both opinions. The finite census covers every labelled connected graph with \(2\le |V|\le5\), every initial binary opinion state, and every possible one-step transition. In particular, it makes no statement that an arbitrary initial state must enter the four-state class.

The general four-state construction requires the displayed strict neighbor-count conditions. It does not purport to classify every recurrent class on larger graphs, and it does not assert that all four-state classes in larger graphs have this form.

## Proof

**1. Exact transition support.** Encode a graph on \(n\) labelled vertices by a bit for each of the \(\binom n2\) potential edges, and a coloring by \(n\) bits. Given a source state \(s\), let \(P(s)\) be the vertices observing a strict blue majority, and \(T(s)\) those observing a tie. The possible next states are exactly

\[
\{P(s)\cup U:U\subseteq T(s)\}.
\]

Here the sets are interpreted as blue vertex sets. This is exact because all ties are resolved independently with both outcomes possible, while strict-majority decisions are forced. Thus the support graph, and consequently its absorbing components, are independent of the particular nondegenerate tie probabilities.

**2. Structural mechanism.** In a state with \(A\) blue and \(B\) white, every vertex in \(A\) sees a strict white majority even if \(u\) is blue, by the first strict inequality; every vertex in \(B\) sees a strict blue majority even if \(u\) is white, by the second. Hence the blocks swap colors regardless of \(u\). The equality of the two neighbor counts at \(u\) makes its update a free coin toss in either block phase. Exactly two target states occur from each of the four states, both in the opposite block phase; each occurs with positive probability. The four states therefore form a closed irreducible class with period two. At fair ties the transition matrix is doubly stochastic on this class, so its unique stationary measure is uniform.

For \(|A|=|B|=2\), the hub \(u\) is adjacent to exactly one member of each block, or to all four. In the former case the two neighbors of \(u\) must each link to both opposite-block vertices and have no same-block edge, leaving the one cross edge between the other two block members optional. This gives the five-edge and six-edge graphs. In the latter case every cross edge is compulsory and both within-block edges are forbidden; this gives the eight-edge graph. All three satisfy the mechanism's hypotheses.

**3. Exhaustive sharpness and classification.** It remains to exclude non-mechanism counterexamples of smaller order and other five-vertex isomorphism classes. The standalone `verify.py` supplies a complete exact finite proof by exhaustive state-graph enumeration. It enumerates every mask from zero to \(2^{\binom n2}-1\), rejects disconnected masks by full graph reachability, and independently constructs the full Markov support both by enumerating tie subsets and by testing every ordered pair of opinion states against the majority rule. It independently computes terminal strongly connected components by Boolean transitive closure and by Kosaraju's graph algorithm, asserting exact agreement in every case. It then obtains:

| Vertices | Connected labelled graphs | Largest recurrent class size: graph counts |
|---:|---:|---|
| 2 | 1 | size 2: 1 |
| 3 | 4 | size 1: 1; size 2: 3 |
| 4 | 38 | size 1: 12; size 2: 26 |
| 5 | 728 | size 1: 188; size 2: 405; size 4: 135 |

For each five-vertex graph exhibiting size four, the program takes the minimum edge mask over all \(5!\) vertex permutations. The resulting complete canonical-mask count is `59:60`, `221:60`, `495:15`; no other canonical mask occurs. Each such graph has one four-state class. The program checks its asserted exact census independently at every stage, so no unexamined configurations remain in the stated finite domain. This proves both the smallest admissible order and the complete first-layer classification.

## Verification

Run `python3 verify.py` with Python 3.8 or later. The program has no external dependencies or data files. It prints the graph counts, size-distribution table, canonical masks, edge sets, and representative four-state class masks before ending in `ALL EXACT CHECKS PASSED`. Computations involve integer arithmetic and exact graph reachability, not Monte Carlo simulation. The two independently expressed one-step support constructions and two SCC algorithms cross-check the critical finite computation; the structural four-state lemma is proved symbolically above.

## Relationship to prior work

Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes* (arXiv:2302.06760v1, first submitted 14 February 2023), defines precisely the random-tie majority model here. Its Theorem 2.6 and Appendix A.4 construct families with exponentially large absorbing classes, and Theorem 2.7 classifies the cycle case. Those theorems establish neither the smallest network with a class larger than two nor the first-order census and the three isomorphism classes. The published expanded article, *Majority opinion diffusion: when tie-breaking rule matters* (2024), was also checked in its full accessible HTML form, including its periodicity and cycle sections. Earlier deterministic majority convergence results bound true deterministic orbit length by two; they do not imply a bound on the number of states in a random-tie absorbing class.

## Limitations

This is an exact small-graph classification coupled with a general sufficient construction, not a classification of every large-graph recurrent class or the probability that a random initial configuration enters the four-state class. A four-state recurrent class is a genuine stochastic communicating set whose Markov period is two; it is **not** a deterministic four-cycle. A fully exhaustive literature review has not been performed; the existence of an equivalent but unindexed small-graph classification cannot be categorically excluded.

## References

- A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1 (14 February 2023), https://arxiv.org/html/2302.06760v1. In particular Sections 1.1, 2.3 and Appendix A.4.
- A. N. Zehmakan, *Majority opinion diffusion: when tie-breaking rule matters*, Autonomous Agents and Multi-Agent Systems **38**, Article 21 (2024), https://doi.org/10.1007/s10458-024-09651-y, Sections 1 and 2.3.
- N. Fountoulakis, M. Kang and T. Makai, *Resolution of a conjecture on majority dynamics: Rapid stabilization in dense random graphs*, Random Structures & Algorithms (2020), https://doi.org/10.1002/rsa.20970. This concerns deterministic retention of ties, not the random-tie support graph.
