# Exact conflict laws and sharp variance envelopes for cyclic fair division

## Finding

Consider independent uniform cyclic shifts of successive equal-size blocks of goods in a round-robin EF1 allocation. The number \(Z\) of soft-conflict edges whose endpoints reach the same agent has an exact variance decomposition, sharp attainable conditional variance bounds, and a complete probability-generating function expressed by circulations on the graph of interacting blocks. The same construction demonstrates pairwise independence without joint independence when the block graph has cycles.

In detail, fix \(n\ge2\) agents and \(q\ge1\) blocks, each containing \(n\) goods. For each pair of blocks \(a<b\), let \(c_{ab}(d)\), \(d\in\mathbb Z/n\mathbb Z\), count conflict edges from position \(i\) of block \(a\) to position \(j\) of block \(b\) with \(i-j\equiv d\pmod n\). Write \(E_{ab}=\sum_d c_{ab}(d)\). Then

\[
\mathbb EZ=\sum_{a<b}\frac{E_{ab}}n,\qquad
\operatorname{Var}(Z)=\sum_{a<b}\left(\frac1n\sum_d c_{ab}(d)^2-\frac{E_{ab}^2}{n^2}\right).
\]

For each fixed integer \(0\le E_{ab}\le n^2\), write \(E_{ab}=nt_{ab}+r_{ab}\) with \(0\le r_{ab}<n\). The individual summand \(V_{ab}\) obeys the sharp bounds

\[
\frac{r_{ab}(n-r_{ab})}{n^2}\ \le\ V_{ab}\ \le\
\frac{t_{ab}n^2+r_{ab}^2}{n}-\frac{E_{ab}^2}{n^2}.
\]

The lower equality holds precisely when the \(n\) offset counts differ by at most one. The upper equality holds precisely when, after rearrangement, they comprise \(t_{ab}\) entries of \(n\), at most one additional entry of \(r_{ab}>0\), and zeros. Every combination of the pairwise lower or upper extremizers is simultaneously realizable by a simple conflict graph on the goods. In particular, \(\operatorname{Var}(Z)=0\) exactly when all offset counts are constant for each block pair.

Let \(H\) be the simple *interaction graph* of blocks: its vertices are \(0,\ldots,q-1\), with an oriented edge \(a\to b\) whenever \(a<b\) and \(E_{ab}>0\). Define the edge polynomials \(f_{ab}(d;z)=z^{c_{ab}(d)}\), and with \(\omega=e^{2\pi i/n}\), their transforms

\[
\widehat f_{ab}(h;z)=\frac1n\sum_{d=0}^{n-1}f_{ab}(d;z)\omega^{-hd}.
\]

A flow \(h\) is an assignment of residues \(h_{ab}\in\mathbb Z/n\mathbb Z\) to the oriented edges of \(H\), with incoming residues summing to outgoing residues at each vertex. Its zero-divergence constraint is taken modulo \(n\). The exact probability-generating polynomial of \(Z\) is

\[
\boxed{\ \mathbb E[z^Z]=\sum_{\substack{h\text{ on }E(H)\\ \operatorname{div}h=0}}\ \prod_{ab\in E(H)}\widehat f_{ab}(h_{ab};z).\ }
\]

There are exactly \(n^{|E(H)|-|V(H)|+\kappa(H)}\) such flows, where \(\kappa(H)\) counts components, including isolated vertices. In particular, for any forest \(H\),

\[
\mathbb E[z^Z]=\prod_{ab\in E(H)}\left(\frac1n\sum_{d=0}^{n-1}z^{c_{ab}(d)}\right).
\]

Thus the block-pair conflict costs are jointly independent on a forest, although they remain merely pairwise independent on an arbitrary interaction graph.

## Assumptions and scope

Goods have identical, nonnegative additive values for all agents and are sorted by nonincreasing value. In each block of \(n\) consecutive goods, indexed \(i=0,\ldots,n-1\), assign good \((a,i)\) to agent \(i+S_a\pmod n\), with independent uniform shifts \(S_a\in\mathbb Z/n\mathbb Z\). The conflict graph on goods is undirected and simple. Conflicts within a single block cannot be violated, so they do not enter \(Z\) or the interaction graph; they may be present without affecting the conclusions. The random process is an unbiased baseline, not the deterministic greedy choice of the cyclic-shift algorithm in the motivating paper. Each realized allocation is EF1: for any two agents, delete the other agent's good from the first block, then compare the other agent's later-block goods with the first agent's earlier-block goods, term by term.

## Proof

**Reduction to block differences.** A conflict edge between \((a,i)\) and \((b,j)\) is violated if and only if \(i+S_a\equiv j+S_b\pmod n\), equivalently \(S_b-S_a\equiv i-j\pmod n\). Consequently

\[
Z=\sum_{ab\in E(H)}c_{ab}(S_b-S_a).
\]

Each difference \(D_{ab}=S_b-S_a\) is uniform. For two distinct unordered block pairs, their differences are jointly uniform in \((\mathbb Z/n\mathbb Z)^2\): with disjoint endpoints this follows from independence; with one common endpoint, condition on its shift and then use the independent shifts of the two other endpoints. Thus the corresponding edge costs are pairwise independent. Summing their expectations and variances gives the two displayed formulas, without assuming joint independence.

**Sharp variance envelopes.** Fix a block pair and put \(x_d=c_{ab}(d)\). Each integer \(x_d\) is between \(0\) and \(n\), because at a prescribed offset exactly \(n\) distinct inter-block goods pairs are possible. Also \(\sum_d x_d=E_{ab}\). The variance equals \(n^{-1}\sum_d x_d^2-(E_{ab}/n)^2\). Transferring one unit from an entry at least two larger than another strictly reduces the sum of squares; therefore a minimum is achieved exactly by entries \(t_{ab}\) or \(t_{ab}+1\), with \(r_{ab}\) of the latter. Conversely, transferring one unit from a smaller positive entry into a larger entry below \(n\) strictly increases the sum of squares. Hence a maximum has \(t_{ab}\) full entries \(n\), at most one additional residual entry \(r_{ab}\), and all others zero. These characterizations give the displayed values, including the endpoints \(E_{ab}=0,n^2\). Offset classes partition the \(n^2\) possible edges between a given block pair, each into \(n\) edges, so any admissible counts can be realized. Different block pairs use disjoint sets of potential edges; choose their histograms independently to attain every pairwise bound simultaneously. Nonnegative summands vanish exactly when each vector of offset counts is constant.

**Complete distribution.** Fourier inversion on \(\mathbb Z/n\mathbb Z\) yields \(f_{ab}(d;z)=\sum_{h=0}^{n-1}\widehat f_{ab}(h;z)\omega^{hd}\). Substitute \(d=S_b-S_a\) in the product \(z^Z\) and expand. Independence and uniformity of the shifts imply that the expectation of each character product is one if its exponent at every block vertex vanishes modulo \(n\), and zero otherwise. Exactly the zero-divergence flows survive. Choosing a spanning forest, the values of flows on the nonforest edges determine all remaining flow values uniquely, proving the stated number of flows. A forest has no nonzero flows, so its generating function factors into the zero-frequency edge polynomials. This factorization is precisely independence of its edge costs.

**Cycles really matter.** Take \(n=2\), three blocks, and one conflict edge joining the position-\(0\) goods for each of the three block pairs. Then all three histograms are \((1,0)\). Among the eight equally probable shift triples, two have all three shifts equal and contribute \(Z=3\); the other six have exactly one equal pair and contribute \(Z=1\). Hence \(\Pr(Z=3)=1/4\), \(\Pr(Z=1)=3/4\), while each cost is Bernoulli with probability \(1/2\). Their joint law is not that of three independent Bernoulli variables, despite the variance formula remaining valid.

## Verification

Run `python3 verify.py` in the same directory. This dependency-free exact-arithmetic script exhaustively checks both variance envelopes for all feasible histograms at \(n=2,3,4\), checks formulas against full shift enumeration for randomly generated weighted block-interaction instances through four blocks, checks forest factorization, and checks pairwise difference independence for all distinct block-pair combinations on four blocks through \(n=5\). It also verifies the three-block cycle counterexample. The test produces `VERIFICATION_OK 1353 exact checks; triangle distribution {3: 2, 1: 6}`. These are finite corroborations; the unrestricted theorem follows from the preceding proof, not from enumeration.

## Relationship to prior work

Yoneda and Yoneda (2026), especially Lemmas 5–6 and Theorem 7, establish the EF1 round-robin construction and show how the \(|E|/n\) expectation supports deterministic conflict control. The mean behavior is therefore prior work; it is not claimed as new. The present result fixes the *independent uniform shifts* distribution and derives exact covariance cancellation, sharp variance extremizers for prescribed inter-block conflict totals, a flow-based full law, and the forest-versus-cycle dependence boundary. Finite-group character orthogonality and flow expansions are standard methods in statistical mechanics; see, for example, Huijben, Patel, and Regts (2023). The asserted contribution is their specifically quantified application to cyclic EF1 soft-conflict allocations, not a new generic Fourier or Potts-model identity. A previously known equivalent distribution formula under a different allocation terminology cannot be ruled out completely.

## Limitations

The model assumes identical nonnegative additive valuations, independent uniform cyclic shifts, and a simple unweighted conflict graph. The sharp upper and lower variances fix the *number* of conflicts between each pair of blocks but permit those edges to be chosen freely. For a fully specified conflict graph, the histogram itself determines the exact variance, and these conditional extrema need not be attained by changing only the random shifts. Inter-block histograms are not assumed equal. Forest independence does not extend to arbitrary cyclic interaction graphs. The Fourier-flow identity supplies a complete finite law, not a general polynomial-time algorithm when the interaction cycle rank grows. No independent external validation or generalization to unequal valuations is asserted.

## References

1. H. Yoneda and M. Yoneda, *Fair Division with Soft Conflicts*, arXiv:2602.20929v1, posted 24 February 2026. https://arxiv.org/abs/2602.20929 ; full accessible preprint: https://arxiv.org/html/2602.20929v1 .
2. C. Huijben, V. Patel, and G. Regts, *Sampling from the low temperature Potts model through a Markov chain on flows*, *Random Structures & Algorithms* (2023), DOI: 10.1002/rsa.21089, https://doi.org/10.1002/rsa.21089 .
