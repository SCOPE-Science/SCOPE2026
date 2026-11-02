# Exact recurrent-class phase diagram for random-majority diffusion on \(K_{a,b,c}\)

## Finding

**Theorem.** Let \(a,b,c\) be positive integers, relabeled so that \(a\ge b\ge c\). On the finite complete tripartite graph \(K_{a,b,c}\), run synchronous binary neighbor-majority diffusion: every vertex observes all neighbors in the other two parts; at a strict majority it adopts that color; at a tie it independently chooses either color with probability \(1/2\). The finite Markov chain has the following **complete list of closed irreducible communicating classes**, and it reaches one of them in finite time almost surely from every initial coloring.

1. **Unique largest part, \(a>b\):** there are exactly three classes: the all-white fixed state, the all-blue fixed state, and the deterministic two-cycle whose states have the size-\(a\) part uniformly opposite to both other parts. The nonconsensus class has exactly \(2\) colorings, Markov period \(2\), and exactly \(a(b+c)\) bichromatic edges in either state.
2. **Exactly two equally largest parts, \(a=b>c\):** there are exactly three classes: the two monochromatic fixed states and one class in which the two size-\(a\) parts are uniformly opposite while the size-\(c\) part has arbitrary vertex colors. This class has exactly \(2^{c+1}\) labeled colorings and Markov period \(2\). The two large parts swap colors every round; each vertex of the small part receives a fresh independent fair color every round. Its unique stationary distribution is uniform on its \(2^{c+1}\) colorings, and every coloring in the class has exactly \(a(a+c)\) bichromatic edges.
3. **Three equal parts, \(a=b=c\):** the all-white and all-blue fixed states are the only closed classes. Thus consensus is reached almost surely from every initial coloring.

There are no other recurrent states. For the two nonconsensus regimes, the stationary proportions of bichromatic edges are respectively
\[
\frac{a(b+c)}{ab+ac+bc}\quad(a>b),
\qquad
\frac{a+c}{a+2c}\quad(a=b>c).
\]
In the tie-for-largest case the persistent nonconsensus class has exponentially many states even though its number of bichromatic edges is constant across all states.

## Assumptions and scope

The three parts are nonempty, the graph is simple and undirected, updates are simultaneous, no vertex observes its own color, and individual coin flips used to resolve simultaneous ties are mutually independent and unbiased across vertices and times. A closed irreducible communicating class is a maximal set of Markov states that is mutually reachable by positive-probability paths and has no positive-probability exit. The period of a class is the greatest common divisor of its possible return times; it should not be confused with its number of states. The statement concerns labeled individual-vertex colorings, not just the three counts of blue vertices.

## Proof

**1. Reduction and a positive path to homogeneous-part states.** Vertices in the same part have identical external neighborhoods. For any given coloring, each part's next opinions are therefore either all white (strict white majority), all blue (strict blue majority), or independent fair coins (tie). In the last case there is positive probability that all vertices of the part choose any prescribed common color. Consequently, from every state there is a positive-probability one-round transition to at least one *corner state* in which each of the three parts is monochromatic. There are only eight such corner states.

**2. Unique largest part.** Suppose \(a>b\ge c\), and denote the corner colors of the parts by \(A,B,C\). In a corner state, the next colors of parts \(B\) and \(C\) are deterministically \(A\): for either smaller part, the size-\(a\) part outweighs the remaining opposite part, regardless of its color. The next color of part \(A\) is determined by the colors of \(B,C\); if they disagree and \(b=c\), this part has a tie, in which event it can become uniformly either color with positive probability. Choose such a homogeneous outcome whenever needed. After one step the two smaller parts have the common old color of \(A\). In the next step the large part adopts that common color and the two small parts adopt the preceding new color of the large part. These two colors are either equal, yielding consensus, or different, yielding exactly the stated opposite-large-part two-cycle. Once in that cycle, all three part updates are strict majorities, because \(a>b,c\). Thus the cycle is closed, deterministic and irreducible, and each of its states has precisely the edges from the large part to the two small parts bichromatic.

**3. Two equally largest parts.** Suppose \(a=b>c\), with corner colors \(A,B,C\). At a corner, parts \(A\) and \(B\) deterministically adopt one another's previous colors, since each large part strictly outweighs the size-\(c\) part. If \(A=B\), part \(C\) also adopts this color and the next state is consensus. If \(A\ne B\), the new large parts remain opposite, while part \(C\) is tied: it sees \(a\) neighbors of each color. In fact this behavior holds from **every** state whose two large parts are monochromatic and opposite, regardless of how the small part is colored: each large part follows the other large part by strict majority, while each small-part vertex independently tosses a fair coin. Thus the specified \(2^{c+1}\)-state set is closed. Any small-part coloring can be reached in one step after swapping the large parts, and in two steps without swapping them, with positive probability. The class is therefore irreducible with period exactly \(2\). The transition redraws the small part uniformly and swaps the two phases, so the uniform measure on these states is stationary and, by irreducibility, unique. Every edge between the large parts (\(a^2\) edges) is bichromatic. Every one of the \(c\) small vertices disagrees with exactly \(a\) vertices of the two large parts, producing exactly \(a^2+ac\) bichromatic edges independent of its own color.

**4. Three equal parts.** Suppose \(a=b=c\). Every corner other than unanimity has exactly two same-colored parts and one opposite-colored part. In the next round the odd part adopts the majority's common color deterministically; each of the other two parts sees equal-sized opposite-colored communities and hence each of its vertices independently tosses a fair coin. With strictly positive probability all these vertices adopt the majority color, producing a unanimous state in one step. Hence every nonunanimous corner has a positive-probability path to consensus.

**5. Exhaustiveness and almost-sure entry.** In each case the displayed sets are individually closed irreducible classes. By Step 1, every possible coloring has a positive-probability path to a corner; by Steps 2--4, every corner has a positive-probability path to one of these displayed classes. A further disjoint closed communicating class is therefore impossible: any state in it would have a positive-probability path outside it. The chain is finite, and from every transient state one can reach a displayed class. Standard finite-state Markov-chain decomposition gives almost-sure entry in finite time. There is no claim of a graph-size-independent bound on its expected duration.

**6. Disagreement fractions.** The complete tripartite graph has \(ab+ac+bc\) edges. Divide the counts from Steps 2--3 by this total. In the equal-parts case the eventual closed states are unanimous and have no bichromatic edges. This proves all claims.

## Verification

Run `python3 verification/verify.py` using Python 3 and the standard library, after extracting that embedded file. The checker independently constructs the support digraph of the lumped three-count Markov chain for all \(6^3=216\) ordered part-size triples with each size between \(1\) and \(6\); it calculates the sink strongly connected components and compares them against the theorem. It also constructs the **individual-coloring** Markov support graph and compares all closed classes for the \(3^3=27\) ordered triples with sizes between \(1\) and \(3\). Finally it performs \(104\) checks of phase swapping, independent fair small-part redraw and exact bichromatic-edge counts for tied-largest examples. These finite computations are corroboration only; Steps 1--6 give the all-size proof.

Representative individual-coloring class-size multisets from the independent computation are \(\{1,1\}\) for \(K_{1,1,1}\) and \(K_{3,3,3}\), \(\{1,1,2\}\) for \(K_{2,2,3}\), \(\{1,1,4\}\) for \(K_{1,2,2}\), and \(\{1,1,8\}\) for \(K_{2,3,3}\).

## Relationship to prior work

Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1, introduced the fair-tie synchronous random-majority model in the relevant form and investigated general graphs and cycles. Its Section 2.3 and Appendix A.4 explicitly construct some graphs with exponentially large absorbing sets, but do not give the complete tripartite three-regime classification above. The present result does **not** claim that exponential recurrent classes themselves are new; the addition is the exact classification, the part-size equality boundary, the stationary law, and the deterministic disagreement level in the natural complete-tripartite family.

Weber, Theisen and Motsch, *Stochastic versus deterministic consensus dynamics on graphs*, arXiv:1901.10756, concerns a distinct stochastic opinion-averaging/copying model; its abstract and model overview are not a statement about synchronous independently randomized **majority ties**. A separately derived complete-bipartite random-majority classification does not imply this result: introducing the third part creates an exponentially large recurrent component precisely when the two largest parts tie in size. Priority against undiscovered specialized tripartite treatments is not independently certified.

## Limitations

The theorem does not provide probabilities of entering each class from an arbitrary initial coloring, nor a uniform bound on absorption time. It assumes binary colors, exactly three nonempty parts, no within-part edges, synchronous updates and independent fair tie-breaking. It does not classify arbitrary multipartite graphs with four or more parts, biased or correlated tie choices, asynchronous updates, or social interpretation beyond the precise Markov model. No independent external audit has been carried out.

## References

- A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1, first submitted 2023-02-14, https://arxiv.org/abs/2302.06760.
- D. Weber, R. Theisen and S. Motsch, *Stochastic versus deterministic consensus dynamics on graphs*, arXiv:1901.10756v1, first submitted 2019-01-30, https://arxiv.org/abs/1901.10756. Different model; background comparison only.
- MSC2020 91D30, *Social networks; opinion dynamics*, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=91D30.
