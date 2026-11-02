# Welfare-optimal swap equilibria and an exact convergence clock on equal-part networks

## Finding

**Theorem (balanced-community equilibrium and two-seat clock).** Let \(m\geq3\) and \(k\geq2\) be integers. Consider the complete \(m\)-partite graph \(G=K_{k,\ldots,k}\), with each of the \(mk\) vertices occupied by exactly one agent of one of two colors. There are \(R\) red agents and \(B=mk-R\) blue agents, for any integer \(0\leq R\leq mk\). Each agent's utility is the proportion of its graph neighbors of its own color. Agents of different colors may exchange locations if **both** obtain strictly greater utility after the exchange.

Write \(R=mq+s\) with integers \(0\leq s<m\), \(0\leq q\leq k\). If \(r_i\) is the number of red vertices in part \(i\), a placement is a swap equilibrium **if and only if** \(\max_i r_i-\min_i r_i\leq1\). These and only these placements globally maximize total agent utility, so every equilibrium is socially optimal. The exact number of equilibrium colorings on distinguishable vertices is

\[
E_{m,k,R}=\binom ms\binom{k}{q+1}^{s}\binom{k}{q}^{m-s},
\]

where the factor involving \(q+1\) is omitted when \(s=0\). For distinguishable individual agents of each color, multiply by \(R!B!\).

Every improving swap from a red-rich part \(i\) to a red-poor part \(j\) changes their occupancies by \(r_i\mapsto r_i-1\), \(r_j\mapsto r_j+1\), and increases total social welfare by exactly

\[
\Delta W=\frac{4(r_i-r_j-1)}{(m-1)k}>0.
\]

**Sharp convergence law when \(k=2\).** Set \(n=2m\) and \(b=\min(R,n-R)\), and let \(T\) denote the number of initially monochromatic pairs of the *minority* color, where pairs are the independent parts of size two. From **every** initial placement, every maximal improving-swap path has exactly \(T\) swaps: its length is independent of the order of improvements. The final welfare is exactly \(W_{\mathrm{initial}}+2T/(m-1)\).

If the initial minority positions are chosen uniformly from the \(\binom{2m}{b}\) subsets of size \(b\), the full equilibrium-hitting-time distribution is

\[
\Pr(T=t)=\frac{m!\,2^{b-2t}}{t!(b-2t)!(m-b+t)!\binom{2m}{b}},
\qquad 0\leq t\leq\lfloor b/2\rfloor.
\]

In particular,

\[
\mathbb E T=\frac{b(b-1)}{2(2m-1)},\qquad
\operatorname{Var}(T)=mp_2(1-p_2)+m(m-1)(p_4-p_2^2),
\]

where \(p_2=b(b-1)/[(2m)(2m-1)]\), and \(p_4=(b)_4/(2m)_4\) for \(b\geq4\) (otherwise \(p_4=0\)), with \((x)_4=x(x-1)(x-2)(x-3)\). The law includes the trivial minority sizes \(b=0,1\).

## Assumptions and scope

The network is a simple, undirected, unweighted complete multipartite graph with \(m\) **equal** parts, each of size \(k\). There are exactly two colors, no vacant vertices, no location preferences, no immobile agents, and no self-loops. Neighbors **inside the same part are absent**. Swaps require strict improvement for both participants; indifferent swaps do not count. Social welfare is the *sum* of the agents' own-color-neighbor fractions, not an integration or diversity metric. In the stochastic initial-state statement the color assignment, not a strategic sequence, is uniform; the swap path itself may be selected adversarially.

The number of agents can be zero in either color. The formula counts color patterns on labeled network vertices, and not quotient classes under graph isomorphisms. The initial-state distribution keeps the population counts fixed.

## Proof

Put \(N=mk\) and \(d=(m-1)k\), the common degree of each vertex. If a red agent is in part \(i\), its utility is \((R-r_i)/d\); the utility of a blue agent in part \(j\) is \([B-(k-r_j)]/d\). Two agents within one part see the same external neighbors, so swapping them cannot strictly benefit either one. For a red agent in part \(i\) and a blue agent in another part \(j\), after exchanging locations the red agent's utility is \((R-r_j-1)/d\), and the blue agent's utility is \([B-(k-r_i+1)]/d\). Consequently **both** individual gains are exactly

\[
\frac{r_i-r_j-1}{d}.
\]

Such an improving exchange therefore exists exactly when some occupancies satisfy \(r_i\geq r_j+2\). The rich part necessarily contains a red vertex and the poor part necessarily has a blue vertex because \(0\leq r_i,r_j\leq k\); hence these inequalities are sufficient, not merely necessary. Equilibrium is precisely \(\max r_i-\min r_i\leq1\).

Since \(\sum_i r_i=R\), the equilibria necessarily have \(m-s\) parts with \(q\) reds and \(s\) parts with \(q+1\) reds; conversely every such arrangement is an equilibrium. Choose which \(s\) parts have \(q+1\) reds, then choose the actual red vertices independently in each part. This gives the stated exact enumerator.

Every red-red directed neighbor pair contributes one red utility unit before division by \(d\), and likewise for blue-blue pairs. Hence

\[
W=\frac{R^2+B^2-\sum_{i=1}^m\bigl[r_i^2+(k-r_i)^2\bigr]}{d}
=\frac{R^2+B^2-mk^2+2kR-2\sum_i r_i^2}{d}.
\]

For fixed \(m,k,R\), maximizing \(W\) is equivalent to minimizing \(\sum_i r_i^2\) over integral \(0\leq r_i\leq k\) with fixed sum \(R\). If \(r_i\geq r_j+2\), the transfer \(r_i\mapsto r_i-1, r_j\mapsto r_j+1\) reduces that sum by \(2(r_i-r_j-1)>0\). Iterating terminates exactly at the balanced occupancy vectors; no other vector minimizes the sum. Thus every equilibrium, and only equilibria, attain the global optimum. Substitution yields the asserted welfare increment.

Now take \(k=2\). Every part's red count belongs to \(\{0,1,2\}\), so a profitable exchange is possible exactly between a part with two red vertices and one with no red vertices. It turns these into two mixed-color parts, without modifying any other part. If red is the minority, the number \(T\) of double-red parts decreases by precisely one at every step; if blue is the minority, the number of double-blue parts decreases by one instead. Every nonterminal state with \(T>0\) also contains at least one all-opposite-color part, because the minority occupies at most \(m\) vertices. Thus a move always exists while \(T>0\), and every maximal path consists of precisely \(T\) moves. The welfare increment is \(4/(2m-2)=2/(m-1)\) per move.

To obtain the distribution, suppose exactly \(t\) pairs are minority-minority. Then \(b-2t\) pairs are mixed and the remaining \(m-b+t\) pairs are majority-majority. Choose the types of all \(m\) labeled pairs in \(m!/[t!(b-2t)!(m-b+t)!]\) ways, and orient the minority vertex in each mixed pair in \(2^{b-2t}\) ways. Divide by the total \(\binom{2m}{b}\) equally likely initial placements. This proves the distribution.

For the moments, write \(T=\sum_{i=1}^m I_i\), where \(I_i\) is the indicator that pair \(i\) is entirely minority. Uniform sampling without replacement gives \(\mathbb E I_i=p_2\) and \(\mathbb E(I_iI_j)=p_4\) for distinct pairs; summing variances and covariances gives the displayed formulas. The preceding deterministic argument makes these the exact moments of the number of swaps under **any** choice of profitable exchanges.

## Verification

The included `verify.py` uses rational-number arithmetic and direct independent utility comparisons after every possible opposite-color exchange. Run with Python 3 using `python verify.py` in the directory containing the file. It exhaustively checked **10,048** labeled color placements across **63** equal-part parameter-and-population classes, matching the equilibrium test, enumerator, and global welfare optimum. For the two-seat case, it separately checked **3,353** placements across **22** parameter classes, including **23,520** profitable swap instances, and verified the exact hitting-time frequencies, mean, variance, and one-step decrease of \(T\). An exhaustive seven-vertex unequal-part comparison confirmed the boundary witness below. The infinite-family theorem rests on the algebraic proof, not these finite computations.

## Relationship to prior work

Agarwal, Elkind, Gan, and Voudouris (2019/2020) defined the fully occupied, bilateral-improvement Schelling swap game and established the social price of **stability** equal to one for regular networks; their potential-method result guarantees an optimal equilibrium but **does not** imply that all equilibria are optimal. Bilò, Bilò, Lenzner, and Molitor (2022), in their full open-access analysis of topology and locality, bounded regular-graph inefficiency and recorded the general finite improvement property, but their general regular-graph results do not entail the equal-part occupancy criterion, exact count, or choice-independent two-seat hitting-time distribution. Kreisel, Boehmer, Froese, and Niedermeier (2021/2024) analyzed complexity and robustness of the same family of models, not these formulas. General concentration and occupancy counting alone do not give the bilateral-swap characterization or the welfare-optimality equivalence.

## Limitations

Equal part sizes and two agent colors are essential to the identical two-agent gain formula. With unequal part sizes, even the stronger claim that every equilibrium is socially optimal can fail: on \(K_{1,3,3}\) with \(R=3\), the red occupancies \((0,2,1)\) give an equilibrium with welfare \(13/4\), while the global maximum is \(10/3\), attained at \((1,1,1)\). These values are directly reproducible with the verifier. The exact order-independent number of exchanges is special to two-vertex parts: on \(K_{3,3,3}\), the initial occupancies \((3,1,0)\) can reach a balanced state in one profitable exchange, or in two, depending on which pair is chosen. No assertion is made about arbitrary multipartite sizes, more than two colors, nonlinear preferences, vacant sites, or unilateral moves. The current literature comparison does not establish priority against all possible specialist work; independent external review has not been performed.

## References

1. A. Agarwal, E. Elkind, J. Gan, and A. A. Voudouris, *Swap Stability in Schelling Games on Graphs*, arXiv:1909.02421, first publicly posted 2019-09-05. https://arxiv.org/abs/1909.02421
2. D. Bilò, V. Bilò, P. Lenzner, and L. Molitor, *Topological Influence and Locality in Swap Schelling Games*, *Autonomous Agents and Multi-Agent Systems* 36 (2022), article 47. https://doi.org/10.1007/s10458-022-09573-7
3. L. Kreisel, N. Boehmer, V. Froese, and R. Niedermeier, *Equilibria in Schelling Games: Computational Hardness and Robustness*, arXiv:2105.06561, first publicly posted 2021-05-13. https://arxiv.org/abs/2105.06561
