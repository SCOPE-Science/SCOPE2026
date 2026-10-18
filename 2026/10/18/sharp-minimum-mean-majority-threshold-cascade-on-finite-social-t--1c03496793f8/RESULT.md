# Sharp minimum mean majority-threshold cascade on finite social trees

## Finding

Fix an integer \(n\ge 4\). In a connected, undirected, simple tree \(T\) on \(n\) individuals, one uniformly chosen individual initially adopts. At every subsequent discrete round, an inactive individual adopts when **at least half** of its neighbors have adopted; an adopter never reverts. Write \(C_T(v)\) for the final count of adopters when \(v\) is the sole initial adopter, and \(M(T)=n^{-1}\sum_{v\in V(T)}C_T(v)\). Then

\[
\min_{|V(T)|=n}M(T)=2-\frac{\lfloor(n-2)/2\rfloor}{n}.
\]

**All minimizers** are exactly the trees with no degree-two vertices and with \(\lfloor(n-2)/2\rfloor\) vertices of degree at least three. Equivalently: if \(n\) is even, every nonleaf has degree three; if \(n\) is odd, precisely one nonleaf has degree four and every remaining nonleaf has degree three. Every such degree pattern is realizable, and the optimum tends to \(3/2\) as \(n\to\infty\).

The result is an exact finite-tree social-contagion extremum, not an empirical claim about behavior. In particular, for \(n=6\), the minimum mean cascade is \(5/3\), achieved by the tree with two adjacent degree-three nodes, whereas the star has mean \(11/6\).

## Assumptions and scope

The network is any simple undirected connected acyclic graph with \(n\ge4\) vertices; all individuals have the same **inclusive** fractional adoption threshold \(1/2\). The seed is uniformly sampled over all \(n\) vertices. Update all eligible inactive vertices simultaneously until stabilization. The eventual active set agrees with any fair asynchronous ordering because activation is irreversible and the update rule is monotone. Final cascade size counts the initial seed. Network links and thresholds are fixed; there is no probabilistic edge transmission.

## Proof

Call vertices of degree at least three **hubs**, with set \(H\). Let \(L=V(T)\setminus H\), consisting of vertices with degree at most two.

**Propagation lemma.** For any sole seed \(v\), the active set at every time is connected, since each newly activated vertex has an active neighbor. On a tree, an unseeded hub \(h\) can therefore never activate: while it is inactive, all currently active vertices lie in the unique component of \(T\setminus\{h\}\) containing the seed, so at most one neighbor of \(h\) is active; its degree is at least three and it requires at least two active neighbors. Conversely, within a path component of \(T[L]\), each unactivated vertex reached from an active neighbor has degree at most two and activates. Thus a seed in a component of \(T[L]\) activates **exactly** that entire component, and a seed in \(H\) activates itself together with every component of \(T[L]\) adjacent to it, but no other hubs.

If \(H=\varnothing\), the tree is a path and every seed eventually activates all \(n\) vertices, so \(\sum_v C_T(v)=n^2\). Otherwise let the path components of \(T[L]\) be \(K_1,\ldots,K_r\); write \(m_j=|K_j|\) and let \(b_j\) count their incident edges to \(H\). Since \(T\) is connected and \(H\neq\varnothing\), every \(b_j\ge1\). The propagation lemma gives the exact identity

\[
\sum_{v\in V(T)}C_T(v)=|H|+\sum_{j=1}^{r}(m_j^2+b_jm_j).
\]

Indeed, each seed in \(K_j\) generates \(m_j\) adopters, contributing \(m_j^2\); each hub contributes one for itself, and its adjacent low-degree components contribute in total \(\sum_j b_jm_j\). Because \(m_j\ge1\) and \(b_j\ge1\),

\[
\sum_v C_T(v)\ge |H|+2\sum_jm_j=2n-|H|.
\]

Equality holds **only** when every \(m_j=1\) and \(b_j=1\). These conditions mean precisely that all nonhub vertices are leaves, i.e. that there are no degree-two vertices.

By the tree degree-sum identity,

\[
\sum_{v\in V(T)}(\deg(v)-2)=-2,
\]

and every vertex of \(H\) contributes at least \(+1\) while each leaf contributes \(-1\). Consequently the number \(\ell\) of leaves obeys \(\ell\ge|H|+2\), so \(n\ge2|H|+2\) and

\[
|H|\le h_n:=\lfloor(n-2)/2\rfloor.
\]

Combining the bounds gives \(\sum_v C_T(v)\ge 2n-h_n\). The path case satisfies this bound strictly for \(n\ge4\).

For equality, both inequalities must be sharp: there are no degree-two vertices and \(|H|=h_n\). When \(n\) is even, leaf counting then requires each hub's degree to be exactly three. When \(n\) is odd, the degree excess over three totals exactly one: one hub has degree four, and all others have degree three. Conversely, start with any tree on \(h_n\) hubs (one vertex if \(h_n=1\)); attach enough leaves to each hub to attain the required hub degrees. Since the degree sum of a tree on the hubs is \(2(h_n-1)\), this uses exactly \(n-h_n\) leaves and realizes equality. All minimizers have therefore been characterized. Dividing the sharp sum by \(n\) proves the formula. \(\square\)

## Verification

The accompanying `check_cascades.py` independently simulates the irreversible half-threshold rule from every seed on every nonisomorphic tree with \(4\le n\le12\), verifies the component identity, and checks the predicted minimum and complete optimizer degree patterns. In a replay, all \(984\) nonisomorphic trees and \(11000\) single-seed experiments passed. This enumeration is a finite cross-check and not a substitute for the all-\(n\) proof.

## Relationship to prior work

Watts (2002) introduced the fractional-neighbor cascade model, including the one-step **vulnerable vertex** criterion (degree at most two at threshold one half), and studied random-network global cascade conditions. Gleeson and Cahalane (2007) derived mean avalanche-size relations for random graph ensembles with prescribed degree distributions and seed fractions. Whitney (2009) studied a finite random-network dynamic threshold process. Pei and colleagues (2017) analyzed seed-targeting algorithms on large networks. These works motivate the quantity and the propagation mechanism. The result here instead optimizes the uniform-one-seed mean **over every deterministic tree of exactly prescribed order** and characterizes every optimizer. No such universal extremal formula was located in the inspected material. That negative search result does not establish literature-wide uniqueness.

## Limitations

The extremal formula depends on the inclusive one-half rule, one initial seed, a tree, and uniform seed sampling. It need not hold on graphs with cycles, at other thresholds, with multiple seeds or heterogeneous thresholds, or under independent-edge transmission. It is not a statement about empirical diffusion interventions. The underlying vulnerable-component mechanism is well known; the claimed contribution is the sharp extremum and all equality cases for the specified functional. Related literature may contain an equivalent theorem not identified in the available sources. External review is not yet performed.

## References

1. D. J. Watts, “A simple model of global cascades on random networks,” *PNAS* **99** (2002), 5766–5771; DOI: 10.1073/pnas.082090499. Public manuscript: https://www.stat.berkeley.edu/~aldous/260-FMIE/Papers/watts.pdf
2. J. P. Gleeson and D. J. Cahalane, “Seed size strongly affects cascades on random networks,” *Physical Review E* **75** (2007), 056103; DOI: 10.1103/PhysRevE.75.056103. Public full text: https://pdodds.w3.uvm.edu/files/papers/others/2007/gleeson2007a.pdf
3. D. E. Whitney, “A dynamic model of cascades on random networks with a threshold rule,” arXiv:0911.4499 (2009); https://arxiv.org/abs/0911.4499
4. S. Pei et al., “Efficient collective influence maximization in cascading processes with first-order transitions,” *Scientific Reports* **7** (2017), 45240; DOI: 10.1038/srep45240.
