# Exponential random-majority metastability and recurrent classes on diameter-six trees

## Finding

**Theorem.** For every integer \(k\ge 2\) there are simple, connected, diameter-six trees supporting two contrasting phenomena under the same synchronous random-majority rule (each vertex adopts the strict neighbor majority, and independently chooses either color with probability \(1/2\) at a tie):

1. On a tree of exactly \(5k\) vertices, a specified initial coloring reaches the all-white absorbing state almost surely, yet its expected time to enter any absorbing communicating class is at least \(2^k\). The first exit time from the explicitly defined blue-hub metastable region is geometric with mean exactly \(2^k\). The expected absorption time is finite, and is at most \(3\cdot 2^{3k}\).
2. On a tree of exactly \(5k+2\) vertices, there is an absorbing communicating class of exactly \(2^k\) colorings, with every pair of states connected in one step with probability exactly \(2^{-k}\). Its stationary distribution is uniform.

The trees differ only by adding two pendant leaves at a central vertex. Thus neither acyclicity nor constant diameter excludes exponentially slow expected stabilization or an exponentially large recurrent state space for the random-majority model. The two statements concern separate trees and are not claims of a universal minimal diameter or vertex count.

## Assumptions and scope

All graphs are finite, simple, undirected, and unweighted. At integer time \(t\), all vertices update synchronously from colors at time \(t-1\), with independent fair coins at ties. No vertex is permanently pinned externally: the anchored colors below are protected by ordinary majority updates.

For integers \(k\ge2\) and \(s\ge1\), construct the tree \(T(k,s)\) as follows. Take a hub \(h\) with \(s\) pendant neighbors \(b_1,\ldots,b_s\). For each \(i\in\{1,\ldots,k\}\), add a path \(h-y_i-w_i\) and attach two pendant neighbors \(z_i,z'_i\) to \(w_i\). No other edges are present. The vertex count is \(1+s+4k\); the graph is connected with \(s+4k\) edges and diameter six (two distinct branches provide a distance-six path between the corresponding \(z\)-leaves).

Call the coloring **anchored** when every \(w_i,z_i,z'_i\) is white. This property remains true forever: each \(w_i\) sees two white leaves among three neighbors and each leaf copies \(w_i\). The \(y_i\) vertices are called floating vertices; when the hub is blue they independently update to unbiased blue/white colors, because each sees one blue and one white neighbor. When the hub is white they all become white.

For the first tree put \(s=k-1\), and initially color \(h\), every \(b_j\), and every \(y_i\) blue, while the anchors and their leaves are white. For the second tree put \(s=k+1\), and consider all anchored colorings with blue \(h,b_j\) and arbitrary \(y_i\) colors. An absorbing communicating class means a closed strongly connected class of the finite-state Markov chain; its size, not its Markov-chain period, is the reported recurrent-state count. Stabilization time means the first entrance time into an absorbing communicating class.

## Proof

**Geometry and invariance.** There are \(1+s+4k\) vertices. Every vertex lies within distance three of \(h\); leaves in different \(w_i\) branches have distance six. The graph is a tree by its construction. A white \(w_i\) cannot change while its two leaves are white, and those leaves copy \(w_i\); hence the entire anchoring is invariant.

**Metastable tree, \(s=k-1\).** Define \(U\) to consist of anchored configurations in which the hub and its \(k-1\) leaves are blue and at least one floating vertex is blue. The hub has degree \(2k-1\). If exactly \(x\) floating vertices are blue, it sees \(k-1+x\) blue neighbors, so it remains blue precisely when \(x\ge1\). Its pendant leaves remain blue, and all floating vertices independently toss fresh fair coins. Thus from every state of \(U\), the next state leaves \(U\) if and only if all \(k\) floating coins are white, an event of probability \(2^{-k}\). Since the specified initial state belongs to \(U\), the first exit time \(\tau_U\) has \(\mathbb P(\tau_U>m)=(1-2^{-k})^m\) for integers \(m\ge0\), and \(\mathbb E\tau_U=2^k\).

To see that \(U\) contains no recurrent state in the anchored subchain, observe that from *any* anchored configuration, it is possible to make every floating vertex white for three successive updates. This event has conditional probability at least \(2^{-3k}\), even if the hub changes, because a white hub makes the floating vertices white deterministically and a blue hub gives independent fair ties. If floating vertices at times \(t+1,t+2,t+3\) are all white, then the hub at \(t+2\) is white: its \(k-1\) pendant-neighbor colors at time \(t+1\) are uniform (copied from the hub at \(t\)) and are too few to form a majority without any blue floating vertices. Similarly the hub at \(t+3\) is white; its pendant leaves at \(t+3\) are white, and so is every vertex of the tree. The all-white coloring is absorbing. Repeating this three-round opportunity from any anchored state gives almost-sure all-white absorption and the finite bound \(\mathbb E\tau_{\rm abs}\le 3\cdot2^{3k}\). Because all-white is reachable from every anchored state, no other closed communicating class exists in this invariant anchored subchain. In particular, no state in \(U\) is recurrent; \(\tau_{\rm abs}\ge\tau_U\), proving \(\mathbb E\tau_{\rm abs}\ge2^k\).

**Recurrent-class tree, \(s=k+1\).** The hub has degree \(2k+1\) and sees its \(k+1\) blue pendant leaves at every update, a strict majority even if all floating vertices are white. Its leaves therefore remain blue. All anchors and their leaves remain white. Every floating vertex has one permanently blue and one permanently white neighbor and independently adopts either color with probability \(1/2\). Consequently the \(2^k\) anchored colorings with blue hub and blue hub-leaves form a closed class, and the transition probability from any such coloring to each other one (including itself) is \(2^{-k}\). This proves irreducibility, absorption, and the uniform stationary distribution. The respective vertex counts are \(5k\) and \(5k+2\). \(\square\)

## Verification

The accompanying standalone `verify.py` constructs the graph and exact rational transition kernel of the invariant anchored subsystem, checks connectivity, tree edge counts, diameter six, all transition normalizations and the one-step probability identities, and computes absorbing strongly connected component sizes for \(2\le k\le7\) in both regimes. Its output was reproduced from the embedded file. These finite checks are diagnostic only; the complete infinite-family assertions follow from the preceding proof.

## Relationship to prior work

Zehmakan's paper *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes* (first posted February 14, 2023; expanded open-access journal version 2024) establishes exponential stabilization and recurrent-state classes on **general graphs**. Its exponential-time construction has multiple degree-two vertices joined to the same pair of star centers, hence contains four-cycles; its exponential recurrent-class construction attaches a path between two nontrivial cliques. Those proofs do not impose a tree, let alone diameter six. The present construction replaces shared anchors by independently protected pendant-star anchors, leaving the full stochastic coin freedom while making every connection acyclic. The quantitative tree and diameter restriction, explicit two regime comparison, and precise transition probabilities are the proposed distinctions; the general exponential phenomena and definitions are not claimed as new.

Benjamini, Zakharov and Zhukovskii study majority dynamics on finite trees with **odd degrees and deterministic updates**, without random ties, so their finite stabilization bounds do not apply to floating degree-two vertices. Literature checks did not identify a prior theorem already covering exponential random-tie majority behavior on trees of constant diameter, but indexing may be incomplete.

## Limitations

The lower bound is an expectation for a specially prepared initial coloring, not a typical-initial-state result. The recurrent-state count is the cardinality of a closed Markov communicating class, not an orbit of deterministic least period \(2^k\). Hub degrees grow linearly with \(k\), so this does not establish exponential behavior on bounded-degree trees. The two trees are separate and no universal minimality of the depth, tree order, or leaf support is asserted. The bibliography search cannot exclude an equivalent unindexed construction; independent review has not been performed.

## References

1. Ahad N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1, first publicly posted 2023-02-14, https://arxiv.org/html/2302.06760v1, Sections 1.1, 2.1 and 2.3.
2. Ahad N. Zehmakan, *Majority opinion diffusion: when tie-breaking rule matters*, Autonomous Agents and Multi-Agent Systems 38 (2024), article 21, https://doi.org/10.1007/s10458-024-09651-y, Sections 2.1 and 2.3.
3. Itai Benjamini, Georgii Zakharov and Maksim Zhukovskii, *Majority Dynamics on Finite Trees*, arXiv:2507.04714 (2025); Random Structures & Algorithms 69 (2026), https://doi.org/10.1002/rsa.70092 (deterministic odd-degree tree setting).
4. Maryam Bahrani, Nicole Immorlica, Divyarthi Mohan and S. Matthew Weinberg, *Asynchronous Majority Dynamics in Preferential Attachment Trees*, ICALP 2020, https://doi.org/10.4230/LIPIcs.ICALP.2020.8 (different asynchronous protocol; abstract inspected).
