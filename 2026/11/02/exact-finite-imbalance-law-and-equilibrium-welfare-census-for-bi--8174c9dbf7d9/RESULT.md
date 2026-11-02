# Exact finite imbalance law and equilibrium welfare census for binary Schelling swaps on cycles

## Finding

Let \(C_n\) be a labeled cycle with \(n=b+r\ge3\), containing exactly \(b\) blue and \(r\) red agents, where \(1\le b\le r\). Every vertex is occupied. An agent has utility one when at least one of its two adjacent vertices has the opposite type, and zero otherwise. Opposite-type agents can exchange vertices only if both strictly increase utility. Let \(W\) be the number of agents of utility one, also called the degree of integration (in unnormalized units).

Every equilibrium is characterized by **at least one color having no monochromatic run longer than two**. The smallest and largest achievable integration degrees are exactly

\[
W_{\min}^{\mathrm{eq}}=b+\left\lceil\frac b2\right\rceil+1,
\qquad W_{\max}=\min\{n,3b\}.
\]

The latter optimum is itself an equilibrium. Consequently the exact price of anarchy and price of stability for integration welfare are

\[
\operatorname{PoA}(b,r)=\frac{\min\{b+r,3b\}}{b+\lceil b/2\rceil+1},
\qquad \operatorname{PoS}(b,r)=1.
\]

The full finite equilibrium **welfare census** has a closed form. For integers \(s\ge k\ge1\), set

\[
R_{s,k}(z)=
\begin{cases}
z^k,&s=k,\\[3pt]
\displaystyle\sum_{t=1}^{\min\{k,s-k\}}
\binom{k}{t}\binom{s-k-1}{t-1}z^{k+t},&s>k.
\end{cases}
\]

Use the convention that \(\binom uv=0\) unless \(u\ge0\) and \(0\le v\le u\). Then the number of equilibria having exactly \(w\) integrated agents is the coefficient \([z^w]E_{b,r}(z)\), where

\[
\begin{aligned}
E_{b,r}(z)=\sum_{k=1}^{b}\frac nk\bigg(&
\binom{k}{b-k}z^bR_{r,k}(z)
+\binom{k}{r-k}z^rR_{b,k}(z)\\
&-\binom{k}{b-k}\binom{k}{r-k}z^n\bigg).
\end{aligned}
\]

Cycle vertices are distinguished, but agents of the same type are not. For individually labeled agents, multiply each coefficient by \(b!r!\). Examples are \(E_{4,4}(z)=16z^7+30z^8\) and \(E_{5,5}(z)=60z^9+72z^{10}\).

The optimum changes formula at the natural minority fraction \(b/n=1/3\); at fixed \(r/b\to q\ge1\), with \(b\to\infty\), the price of anarchy tends to \(\frac23\min\{1+q,3\}\). The balanced limit \(4/3\) and the existence of constructions approaching a ratio of two were already established in earlier work; they are not claimed as new. The contribution here is the exact all-population finite welfare classification and coefficientwise equilibrium census.

## Assumptions and scope

The graph is a simple undirected cycle on at least three distinct labeled vertices. All vertices are occupied, there are exactly two colors with fixed counts \(1\le b\le r\), and participants may swap across any distance if both strictly improve. Utilities depend only on whether any opposite-colored neighbor exists; the welfare is the unnormalized number of nonsegregated agents, not the number of mixed edges.

The identical equilibrium and integration statements hold in the model of Bilò, Bilò, Lenzner, and Molitor (2022) for single-peaked utility with peak \(\Lambda=1/2\). A closed neighborhood has three vertices, so the only possible own-color fractions are \(1/3,2/3,1\). Their symmetric single-peak assumption makes the first two fractions equally valuable and the last value zero. Thus the induced strict-improvement relation is the same as for binary utility. This reduction must not be extended to other peak parameters without renewed analysis.

## Proof

**Equilibrium criterion.** Call a vertex segregated when both its neighbors have its own color. Every integrated agent already has maximal utility, so only a pair of segregated agents could both improve in a swap. Such a pair must have opposite colors. Two segregated vertices of opposite colors cannot be adjacent. Exchanging their positions therefore leaves each with two opposite-colored neighbors, raising both utilities from zero to one. Conversely, without segregated vertices of both colors, no profitable swap exists. A segregated vertex occurs precisely at an interior position of a monochromatic cyclic run of length at least three. This proves the stated necessary and sufficient run criterion.

**Optimal welfare.** Each of the \(b\) blue vertices is integrated at most once and can integrate at most two red neighbors. Thus \(W\le\min\{n,3b\}\). If \(r\ge2b\), place the \(b\) blue agents singly among \(b\) red runs each of length at least two. Exactly the \(b\) blues and two endpoint reds of each red run are integrated, attaining \(3b\). If \(b\le r<2b\), place blues singly and partition the red agents into \(b\) nonempty runs of lengths at most two. Every vertex is then integrated, attaining \(n\). In both constructions no blue agent is segregated, so the optimum is an equilibrium.

**Worst equilibrium.** Suppose a color of size \(s\) has no segregated members. Its \(k\) cyclic runs have sizes one or two, so \(k\ge\lceil s/2\rceil\), and all its \(s\) agents are integrated. The other color of size \(t\) also has \(k\) runs. If \(t>k\), the other color contributes at least \(k+1\) integrated agents: at least one of its runs has size at least two and every run contributes \(\min\{\text{run length},2\}\). If \(t=k\), all runs of the other color are singletons and every vertex is integrated.

If the nonsegregated color is blue and \(r>k\), this yields \(W\ge b+\lceil b/2\rceil+1\). If \(r=k\), then \(b=r=k\) and all vertices are integrated, which still satisfies the same bound for the permitted \(n\ge3\). If the nonsegregated color is red and \(b>k\), then \(W\ge r+\lceil r/2\rceil+1\ge b+\lceil b/2\rceil+1\). If \(b=k\), every vertex is integrated, again giving the required bound. To attain the bound, let \(k=\lceil b/2\rceil\), partition the blue count into \(k\) run lengths one or two, and partition the reds into \(k-1\) singleton runs and one run of length \(r-k+1\). The latter has length at least two (since \(r\ge b\) and \(k\le b\)), all blues are integrated, and exactly \(k+1\) reds are integrated. Hence \(W=b+k+1\).

**Counting all welfare levels.** Every two-color cycle placement has the same number \(k\) of blue runs and red runs, with \(1\le k\le b\). Marking the start of a blue run produces \(k\) marked versions of each placement. Conversely, choose that marked vertex in \(n\) ways, and choose ordered positive blue and red run lengths with totals \(b,r\), giving an \(n/k\) factor. The number of compositions of \(b\) into \(k\) terms of size at most two is \(\binom{k}{b-k}\). The unrestricted red run composition contributes \(z^{\sum_j\min\{\ell_j,2\}}\), where \(\ell_j\) are its run lengths. When \(r>k\), precisely \(t\) runs of length at least two may be chosen in \(\binom{k}{t}\) ways and the \(r-k\) surplus positions are distributed as \(t\) positive parts in \(\binom{r-k-1}{t-1}\) ways. This gives the definition of \(R_{r,k}(z)\); the case \(r=k\) has exponent \(k\). Therefore the placements whose blue runs all have length at most two contribute \(\frac{n}{k}\binom{k}{b-k}z^bR_{r,k}(z)\). The symmetric count for red-bounded runs is the second term. Their intersection has both colors completely integrated and contributes exactly the subtracted term. Inclusion-exclusion establishes \(E_{b,r}(z)\).

## Verification

The accompanying `verification.py` uses only the Python standard library. It independently generates every type assignment for \(3\le n\le16\) and \(1\le b\le\lfloor n/2\rfloor\). On sizes through \(n=15\), it tests all opposite-color pairs and their two participant utilities to determine stability directly. Separately it checks the run criterion, exact minimum and maximum equilibrium welfare, exact total equilibrium count, and the entire coefficientwise polynomial through size \(n=16\). These are finite checks supporting, not replacing, the proofs for arbitrary sizes. Run `python3 verification.py` to reproduce the results.

## Relationship to prior work

Bilò, Bilò, Lenzner, and Molitor (2022) introduce the normalized single-peaked swap model and degree of integration. Their Lemma 5 proves the necessary prohibition on segregated agents of opposite colors, and their Theorem 8 constructs cycle instances with price of anarchy tending to two at ratio \(n/b=3\). Their paper does not provide the all-size, all-imbalance equilibrium generating polynomial or this exact finite optimum/worst-equilibrium formula.

Li, Narayanan, Opatrny, and Xu (2025) explicitly study the equivalent binary-utility swap rule. Their Observation 1 gives the segregated-type necessary condition, and Theorem 5.1 proves the already-known balanced asymptotic price of anarchy \(4/3\) on cycles. They restrict the analyzed type populations to equitable partitions and do not state the arbitrary-imbalance finite welfare census. Neither the run criterion alone nor these asymptotic bounds specifies the number of equilibria at each integer welfare level. The generating polynomial and all-population sharp formulas are the distinct contribution claimed here.

The single-peaked **jump** setting of Friedrich, Lenzner, Molitor, and Seifert (2023), unlike this fully occupied swap game, has vacant nodes and one-person moves. Earlier monotone-preference games are also non-equivalent.

## Limitations

The claim does not cover three or more colors, vacant vertices, jumps, locality-restricted swaps, nonbinary diversity utilities, or single-peak parameters other than \(1/2\). The formula counts colorings of labeled cycle positions, not rotational equivalence classes. The finite tests are not exhaustive for arbitrary cycle length. The two known asymptotic values and the segregated-type criterion are credited to prior literature, not counted as independent advances. An equivalent specialized enumeration outside the inspected publications cannot be excluded.

## References

- Davide Bilò, Vittorio Bilò, Pascal Lenzner, and Louise Molitor, *Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games*, first public version 2022-04-26, arXiv:2204.12599v1, https://arxiv.org/abs/2204.12599 . Particularly model definition, Lemma 5, Theorem 8.
- Yaqiao Li, Lata Narayanan, Jaroslav Opatrny, and Yi Tian Xu, *Diversity-seeking swap games in networks*, first public version 2025-02-19, arXiv:2502.13375v1, https://arxiv.org/html/2502.13375v1 . Particularly Observation 1, Theorem 5.1.
- Tobias Friedrich, Pascal Lenzner, Louise Molitor, and Lars Seifert, *Single-Peaked Jump Schelling Games*, first public version 2023-02-23, arXiv:2302.12107v1, https://arxiv.org/abs/2302.12107 .
- Aishwarya Agarwal, Edith Elkind, Jiarui Gan, Ayumi Igarashi, Warut Suksompong, and Alexandros A. Voudouris, *Schelling games on graphs*, Artificial Intelligence 301 (2021), 103576, https://doi.org/10.1016/j.artint.2021.103576 .
