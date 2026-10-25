# The five-vertex onset and complete minimal classification of persistent randomness in majority opinion diffusion

## Finding

For the synchronous random majority model with independent fair-coin tie-breaking on **connected finite simple graphs of order at least two**, the smallest order permitting a genuinely stochastic absorbing communicating class is exactly **five**. Among the 21 connected unlabeled five-vertex graphs, precisely three have such a class: the **bull graph**, the **house graph**, and the **five-vertex wheel** \(W_5\). Each has a four-coloring absorbing communicating class on which a fair tie persists at every round; none of the other 18 isomorphism types has a stochastic absorbing class. Of the 728 connected *labeled* five-vertex graphs, 135 have this property: 60 bulls, 60 houses, and 15 wheels.

For every connected graph of order \(2\le n\le4\), every absorbing communicating class is a deterministic fixed point or a deterministic two-cycle. Conversely, **for each integer \(n\ge5\)** a connected \(n\)-vertex graph admits a stochastic absorbing class consisting of exactly four colorings. This last existence statement holds in particular for a family of trees with one added triangle, obtained by attaching pendant leaves to either of two designated bull vertices.

This is a complete minimum-order classification, not a claim that all graphs with at least five vertices have persistent randomness.

## Assumptions and scope

A graph \(G=(V,E)\) is finite, undirected, simple and connected with \(n=|V|\ge2\). At integer time \(t\), each vertex \(v\) carries an opinion \(X_t(v)\in\{0,1\}\). All vertices update simultaneously using the opinions of their **neighbors, excluding themselves**. If more neighbors hold opinion one than zero, the next opinion is one; if fewer do, it is zero; on equality, that vertex independently chooses one or zero with probability \(1/2\) each. Fresh choices are independent between vertices and rounds.

The resulting Markov chain has \(2^n\) colorings. For two colorings \(x,y\), a transition \(x\to y\) belongs to the *support digraph* exactly when its probability is positive. An absorbing communicating class is a maximal strongly connected subset of this digraph without outgoing edges. It is called **stochastic** here if at least one of its states has at least two different supported next states; otherwise it is deterministic. For a finite irreducible closed class containing a branching state, actual tie-breaking randomness recurs infinitely often with probability one whenever the chain starts in that class.

The primary MSC2020 classification is **91D30 (Social networks; opinion dynamics)**. Vertex labels in edge lists are \(0,1,2,3,4\); the notation \(ij\) denotes the unordered edge \(\{i,j\}\). A coloring is encoded by the integer \(\sum_{i=0}^{4}2^i X(i)\) for the five-vertex witnesses.

## Proof

**1. Exhaustive minimum-order certificate.** Every labeled undirected graph of order \(n\le5\) is encoded by a bitmask of its \(\binom n2\) potential edges. Enumerate every bitmask and retain exactly those passing a breadth-first connectivity test. For every retained graph, enumerate every one of its \(2^n\) colorings. If a vertex has a strict majority, its next bit is fixed; if tied, both next bits occur with positive probability. The Cartesian product of these local possibilities gives **the complete exact transition support**, with no random simulation or numerical rounding. An independent routine checks every candidate next coloring against the vertex-majority conditions; the two support constructions agree for every graph and coloring.

Obtain terminal strongly connected components of each transition digraph twice, by Tarjan's algorithm and independently by bitset transitive closure and mutual reachability. They agree for every input. For connected labeled graphs, the counts and largest terminal-component sizes are:

| Order | Connected labeled graphs | Connected unlabeled types | Largest terminal size 1 | Largest terminal size 2 | Largest terminal size 4 |
|:---:|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 0 | 1 | 0 |
| 3 | 4 | 2 | 1 | 3 | 0 |
| 4 | 38 | 6 | 12 | 26 | 0 |
| 5 | 728 | 21 | 188 | 405 | 135 |

For orders two through four every terminal component contains no branching state and has size at most two. At order five precisely 135 labeled graphs have a branching terminal component and its size is four; all others have deterministic terminal classes of size one or two. Canonicalization by all vertex permutations partitions the 728 labeled graphs into exactly 21 isomorphism classes and the 135 exceptional labeled graphs into **three** classes, with orbit sizes \(60,60,15\). The executable `verify.py` implements the entire finite exhaustion using only the standard Python library. This is a complete finite proof of the lower bound and five-vertex classification, not an extrapolation from samples.

**2. Explicit minimal witnesses.** Let the following three graphs have vertex set \(\{0,1,2,3,4\}\), with edges as defined above:

| Type | Edge set | Four-coloring absorbing class |
|---|---|---|
| Bull | \(\{01,02,04,12,23\}\) | \(\{9,11,20,22\}\) |
| House | \(\{01,03,04,12,23,34\}\) | \(\{5,10,21,26\}\) |
| Wheel \(W_5\) | \(\{01,03,04,12,14,23,24,34\}\) | \(\{5,10,21,26\}\) |

For the bull, states 9 and 11 each transition to states 20 and 22 with probability \(1/2\) each, and states 20 and 22 each transition to states 9 and 11 with probability \(1/2\) each. Vertex 1 is the only tied vertex. For the house and wheel, states 5 and 21 each transition to states 10 and 26 with probability \(1/2\) each and vice versa; vertex 4 is the only tied vertex. In all cases every transition remains in the displayed set and all four states communicate. These computations can also be checked by direct neighbor counts, without using the classification enumeration.

**3. Every larger order.** Start with the bull graph with edges \(\{01,02,04,12,23\}\). Add any \(a\ge0\) pendant leaves adjacent only to vertex 0 and any \(b\ge0\) pendant leaves adjacent only to vertex 2. The resulting graph is connected and has \(n=5+a+b\) vertices. In phase A give vertex 0 opinion one and vertex 2 opinion zero; give every leaf adjacent to 0 opinion zero and every leaf adjacent to 2 opinion one. Let vertex 1 have either opinion. In phase B reverse all opinions except that vertex 1 again has either opinion.

At each update from A, vertex 0 has \(2+a\) opposite-opinion neighbors and at most one same-opinion neighbor, so it switches to zero regardless of vertex 1. Symmetrically, vertex 2 has \(2+b\) opposite-opinion neighbors and at most one same-opinion neighbor, so it switches to one. Every leaf copies its unique neighbor and therefore switches. Vertex 1 sees the two opposite-colored vertices 0 and 2 and chooses independently by a fair coin. The identical argument with opinions exchanged applies from B to A. Thus each of these four colorings transitions to both members of the opposite phase with positive probability and never leaves the four-coloring set. It is a stochastic absorbing communicating class for every \(n\ge5\). This proves the sharpness at every larger order.

## Verification

Run `python3 verify.py` using Python's standard library. The program exhausts all \(771\) connected labeled graphs on orders \(2\) through \(5\), checks each complete support digraph by two independently coded descriptions, and determines all terminal communicating classes by two independent algorithms. It checks all three named witness edge lists, their exact closed transition supports and their graph-isomorphism orbits; it also checks the arbitrary-leaf bull construction for each order from five through sixteen and every distribution of its added leaves. The final output is `CHECK_OK`. These finite tests establish the finite cutoff because **every** finite input through order five is included; they corroborate, rather than substitute for, the direct infinite-family argument.

## Relationship to prior work

Zehmakan's 2023 random-majority study introduced the independent random-tie model and analyzed convergence and absorbing components. Its fuller open-access journal version establishes that absorbing components can have exponentially many colorings (Theorem 2.6), and classifies cycles as ultimately monochromatic or deterministically alternating (Theorem 2.7). The large-graph existence theorem does not determine the minimum order or the entire first exceptional layer. The cycle theorem only excludes one of the five-vertex graph types and does not imply the bull, house and wheel classification. The finite sharp cutoff, exact isomorphism census, and bull-based four-state construction are the present claim.

Fountoulakis, Kang and Makai's majority-dynamics work concerns **retaining the previous opinion on ties**, not independently rerandomizing; it cannot cover these stochastic terminal components. The present result is an exact finite small-graph classification for one update rule and does not amend those separate models.

## Limitations

The exclusion of isolated vertices is essential: a one-vertex graph would randomize its opinion at every round under the stipulated tie rule. The theorem assumes synchronous updates, no self-neighbor vote, simple undirected connected graphs, binary opinions, and independent fair ties. It does not characterize stochastic terminal classes on all larger graphs, nor does it give expected hitting times from arbitrary initial states. The four-state classes have **Markov period two**, even though they contain four configurations; the phrase “four-state absorbing class” refers to class cardinality, not periodicity in the Markov-chain gcd sense. Publication priority beyond the inspected literature remains open to independent investigation.

## References

1. A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1 (first publicly posted 2023-02-14), https://arxiv.org/abs/2302.06760 .
2. A. N. Zehmakan, *Majority opinion diffusion: when tie-breaking rule matters*, Autonomous Agents and Multi-Agent Systems **38**, article 21 (2024), https://doi.org/10.1007/s10458-024-09651-y . In particular, Section 1.1, Theorems 2.6–2.7 and Section 6.
3. N. Fountoulakis, M. Kang and T. Makai, *Resolution of a conjecture on majority dynamics: Rapid stabilization in dense random graphs*, Random Structures & Algorithms **57** (2020), 1134–1156, https://doi.org/10.1002/rsa.20970 .
