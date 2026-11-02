# A parity obstruction to deadline-optimal edge coupon collection

## Finding

An **edge coupon collector** on a finite simple graph \(G=(V,E)\) independently samples an edge \(e\in E\) on each discrete round using a fixed probability law \(p=(p_e)_{e\in E}\). Both endpoints of the sampled edge are marked; marks persist. Write \(T_p\) for the first round at which every vertex is marked. A law is *deadline-universally optimal* if its completion probability \(\Pr(T_p\le t)\) is maximal over all fixed edge laws at every integer deadline \(t\ge0\).

**Theorem (bipartite optimum and odd-cycle obstruction).**

1. Let \(G=(A,B,E)\) be bipartite with no isolated vertices, \(1\le |A|=a\le |B|=b\), and a matching saturating \(A\). For every edge law \(p\) and every integer \(t\ge0\),

\[
\Pr(T_p\le t)\le \frac{b!\,S(t,b)}{b^t},
\]

where \(S(t,b)\) is a Stirling number of the second kind (zero for \(t<b\)). One fixed law attains equality for **all** deadlines simultaneously: choose \(b\) edges covering \(V\), each incident to a different vertex of \(B\), and sample them equally. Consequently \(\min_p\mathbb E T_p=bH_b\), where \(H_b=\sum_{j=1}^b 1/j\). If \(a=b\ge2\), the complete collection of deadline-universally optimal laws consists exactly of the uniform laws on perfect matchings of \(G\). In particular, every even cycle \(C_{2r}\) with \(r\ge2\) has precisely two such laws, each uniformly sampling one of the two alternating perfect matchings.

2. On every odd cycle \(C_{2m+1}\) with integer \(m\ge3\), there is **no** deadline-universally optimal fixed edge law. With \(n=2m+1\), uniform sampling \(u\) over all \(n\) cycle edges satisfies

\[
\Pr(T_u\le m+1)=\frac{(m+1)!}{n^m}.
\]

If \(s\) samples uniformly from the \(m+1\) edges of any minimum edge cover, then

\[
\Pr(T_s\le m+1)=\frac{(m+1)!}{(m+1)^{m+1}}
>\Pr(T_u\le m+1).
\]

Nevertheless every nonuniform law \(p\ne u\) eventually has a strictly smaller completion probability than \(u\): there exists an integer \(t_p\) such that \(\Pr(T_p\le t)<\Pr(T_u\le t)\) for all \(t\ge t_p\). Thus early-deadline and late-deadline objectives necessarily conflict on these odd cycles.

## Assumptions and scope

All graphs are finite, undirected, loopless and simple. In the bipartite theorem no vertex is isolated; in particular every vertex of the larger part has an incident edge. The sampling law is fixed before the process starts, may assign zero probability to some edges, and is used identically and independently across discrete rounds. Every chosen edge marks both endpoints whether previously marked or not. The law cannot change adaptively as vertices become marked. A *matching saturating* \(A\) uses distinct neighbors in \(B\) for every vertex of \(A\). For the odd-cycle assertion \(m\) is any integer at least three; the smaller odd cycles are not classified by this theorem.

## Proof

**1. Projection to one side.** On a bipartite graph each sampled edge has exactly one endpoint in \(B\). The sequence of its \(B\)-endpoints is an ordinary independent coupon collector with probabilities \(q_v=\sum_{e\ni v}p_e\), \(v\in B\). Since covering \(V\) implies collecting every \(B\)-coupon,

\[
\Pr(T_p\le t)\le \Pr(C(q)\le t).
\]

For any probability vector \(q\) on \(b\) coupons, the uniform vector \((1/b,\ldots,1/b)\) maximizes the probability of collecting all coupons at every fixed deadline. Here is a direct proof, including boundary cases. Fix two coordinates with sum \(s\). Condition on which rounds fall in these two categories, on the number \(k\) of such rounds, and on every draw in the other categories. The event that all *other* categories have appeared is now deterministic. If it holds, the conditional probability of observing both selected categories among their \(k\) draws, for \(s>0\), equals

\[
1-\left(\frac{q_i}{s}\right)^k-\left(\frac{q_j}{s}\right)^k
\]

for \(k\ge1\), and is zero for \(k=0\). This is maximized at \(q_i=q_j=s/2\), because the power-sum is minimized by equal arguments. When \(s=0\), neither coupon can ever appear; the same assertion is immediate. Repeated pairwise equalization, or equivalently the standard majorization chain converging to the uniform vector, establishes uniform optimality by continuity. Its full-collection probability is \(b!S(t,b)/b^t\).

**2. Attainability.** Take a matching from \(A\) into \(B\), choose its \(a\) edges, and for each remaining vertex in \(B\) choose one arbitrary incident edge. This is a set of exactly \(b\) distinct edges meeting every vertex, with precisely one edge incident to each \(B\)-vertex. Sampling these \(b\) edges uniformly makes collecting \(B\) exactly equivalent to covering all vertices. The completion time is the classical uniform \(b\)-coupon time, of expectation \(bH_b\). This proves both the sharp stochastic bound and the expectation statement.

**3. All optimizers in balanced bipartite graphs.** Suppose \(a=b\ge2\) and a law is optimal at every deadline. In particular, at the earliest possible deadline \(t=b\), its completion probability equals \(b!/b^b\). By the projection bound and the arithmetic-geometric mean inequality,

\[
\Pr(T_p\le b)\le b!\prod_{v\in B}q_v\le\frac{b!}{b^b}.
\]

Equality forces every \(q_v=1/b\) and requires that *every* selection of one positively weighted incident edge for each \(v\in B\) covers all of \(A\). The supported neighbors of distinct \(B\)-vertices must then be disjoint: otherwise pick the same \(A\)-neighbor for two distinct \(B\)-vertices and arbitrary supported edges for all other \(B\)-vertices; at most \(b-1\) vertices of \(A\) would be covered, a contradiction. There are \(b\) pairwise disjoint nonempty supported-neighbor sets inside \(A\), which itself has \(b\) vertices. Hence each set is a distinct singleton, and the support is a perfect matching with weight \(1/b\) per edge. The converse was proved in step 2.

**4. Earliest completion on odd cycles.** Put \(n=2m+1\) and \(k=m+1\). Since every edge marks at most two vertices, at least \(k\) distinct edges are necessary to cover \(n\) vertices, so completion in \(k\) rounds uses \(k\) distinct edges forming a minimum edge cover. The complement of such a cover is a matching of size \(m\) on \(C_n\). There are exactly \(n\) such maximum matchings: choose the unique unmatched cycle vertex, after which the remaining path has a unique perfect matching. Thus uniform edge sampling has exactly \(n\,k!\) successful ordered \(k\)-tuples among \(n^k\) equiprobable tuples, giving \(\Pr(T_u\le k)=k!/n^m\). Under uniform sampling on a fixed minimum edge cover, the probability of seeing all its \(k\) edges in \(k\) rounds is \(k!/k^k\).

The strict inequality \(n^m>(m+1)^{m+1}\) holds for all \(m\ge3\): the ratio \((2m+1)/(m+1)\) is at least \(7/4\), and the bound \((7/4)^m>m+1\) follows by induction from \((7/4)^3>4\) and \((7/4)(m+1)>m+2\) for \(m\ge3\).

**5. Eventually the uniform law beats every nonuniform one.** Index the cycle edges modulo \(n\) so edge \(i\) joins vertex \(i\) to vertex \(i+1\). For any edge law \(p\), the chance that a given vertex \(i\) is marked in one round is

\[
s_i=p_{i-1}+p_i,
\qquad \frac1n\sum_{i=0}^{n-1}s_i=\frac2n.
\]

If every \(s_i=2/n\), subtract consecutive equations to obtain \(p_i=p_{i-2}\). Since \(n\) is odd, the step-two permutation is transitive, so every edge weight is \(1/n\). Hence for every nonuniform \(p\), some vertex has \(s_i<2/n\). The probability this vertex remains unmarked after \(t\) rounds gives

\[
\Pr(T_p>t)\ge(1-s_i)^t,
\]

whereas a union bound for uniform sampling gives

\[
\Pr(T_u>t)\le n(1-2/n)^t.
\]

Since \((1-s_i)/(1-2/n)>1\), the first right-hand side eventually exceeds the second. The uniform law thus eventually outperforms every nonuniform law; but step 4 supplies a nonuniform law beating uniform at the first feasible deadline. No law can maximize all deadline probabilities simultaneously. \(\square\)

## Verification

Run `python3 check.py` with Python's standard library. It performs 864 exact-rational assertions: direct finite-state edge-cover probabilities on several complete bipartite graphs, comparisons with the Stirling-number coupon formula, exhaustive minimum-edge-cover counts for four odd cycles, early- and late-deadline comparisons, and odd-cycle marginal checks. The finite tests are consistency checks only; the preceding proof establishes the general infinite families and eventual-order claim.

## Relationship to prior work

Schilling and Henze's 2021 group-drawing collector paper proves limit theorems for uniformly and approximately uniformly chosen fixed-size coupon packages; the graph-constrained, all-deadline optimization and its nonexistence dichotomy are not consequences of the stated limit theorems. Betken and Thäle (2022 preprint) analyze normal and Poisson approximations for uniform group draws, likewise not optimization over graph edges. Berend and Sher (2025 preprint) study expected-time comparisons between uniform, near-decomposition and consecutive-package drawings; their results and classical coupon-collection facts motivate our question, but the explicitly inspected theorems are about expected waiting times and do not imply the simultaneous deadline optimum or parity nonexistence. The standard fact that a uniform single-coupon law is stochastically optimal is used as a lemma and is not claimed as new.

The difference in logical strength is essential: exhibiting a mean-improving group distribution does not decide whether a single law maximizes \(\Pr(T_p\le t)\) at *every* deadline, nor show why a nonuniform law must lose at every sufficiently late deadline on an odd cycle. The contribution is the graph-constrained paired classification and parity obstruction, not the coupon-collector formula alone.

## Limitations

The conclusions apply only to independent identically distributed, fixed edge-sampling laws. They do not classify graph designs with isolated vertices or without a saturating matching, odd cycles of length three or five, all nonbipartite graphs, adaptive edge-selection policies, or the expected-time optimizer on odd cycles. Claims of historical priority remain provisional; a relevant 2021 paper on distributional optimization was not available in complete text during the comparison.

## References

1. J. Schilling and N. Henze, *Two Poisson limit theorems for the coupon collector's problem with group drawings*, Journal of Applied Probability 58 (2021), 966–977, https://doi.org/10.1017/jpr.2021.15. First verified public online date: 2021-11-22.
2. C. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, arXiv:2202.07485, first posted 2022-02-15, https://arxiv.org/abs/2202.07485.
3. D. Berend and T. Sher, *On a Conjecture on Uniform Group Drawings in the Coupon Collector Problem*, arXiv:2509.17201, first posted 2025-09-21, https://arxiv.org/abs/2509.17201.
4. J. Schilling, *Results and conjectures on the role of the uniform distribution in the coupon collector's problem with group drawings*, Information Processing Letters 169 (2021), article 106112, https://doi.org/10.1016/j.ipl.2021.106112. Full text was not available for this comparison.
