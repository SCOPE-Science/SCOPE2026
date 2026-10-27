# Transition matchings and the joint subsequence-universality law for binary words

## Finding
For a finite binary word \(w=w_1\cdots w_n\), let \(t(w)\) be its number of unequal adjacent pairs, and let \(\iota(w)\) be the largest \(k\) such that every binary length-\(k\) word is a scattered subsequence of \(w\). Define a graph \(G_w\) on the positions \(1,\ldots,n\), retaining path edge \(\{i,i+1\}\) exactly when \(w_i\ne w_{i+1}\). Then
\[
\boxed{\iota(w)=\nu(G_w),}
\]
where \(\nu\) is the maximum-matching cardinality. Equivalently, if the maximal consecutive runs of unequal-adjacency indicators have lengths \(\ell_1,\ldots,\ell_s\), then \(\iota(w)=\sum_{j=1}^s\lceil\ell_j/2\rceil\). The empty word has index zero.

Let \(N_{n,t,k}\) count indexed length-\(n\) binary words with exactly \(t\) transitions and universality index \(k\). The complete joint distribution is
\[
\boxed{\sum_{n,t,k\ge0}N_{n,t,k}z^ny^tu^k
=1+\frac{2z(1+zyu)}{1-z-z^2yu(1+y)}.}
\]
For \(n\ge1\), \(k\ge1\), the coefficient formula is
\[
\boxed{N_{n,t,k}=2\left[\binom{k-1}{t-k}\binom{n-k}{k}
+\binom{k-1}{t-k-1}\binom{n-k-1}{k}\right],}
\]
using zero for out-of-range binomial coefficients. The remaining cases are \(N_{0,0,0}=1\), \(N_{n,0,0}=2\) for \(n\ge1\), and zero otherwise. For \(n\ge2\) and \(1\le t\le n-1\), the attainable indices are **exactly** the integers
\[
\left\lceil\frac t2\right\rceil\le k\le\min\left(t,\left\lfloor\frac n2\right\rfloor\right).
\]

For a uniformly sampled length-\(n\) word conditioned to have exactly \(t\) transitions, put \(m=n-1\ge1\). Its exact conditional mean is
\[
\boxed{\mathbb E[\iota\mid t]=(m-t+1)
\sum_{\substack{1\le r\le t\\r\text{ odd}}}\frac{\binom tr}{\binom mr}.}
\]
If \(t=t_n\) is any deterministic transition budget such that \(t_n/(n-1)\to\rho\in[0,1]\), then the conditional random-word universality index obeys
\[
\boxed{\frac{\iota(W_n)}n\ \longrightarrow\ \frac{\rho}{1+\rho}
\quad\text{in probability}.}
\]
The conditional concentration has exponential tails on the \(\sqrt n\) scale.

## Assumptions and scope
The ambient alphabet is exactly \(\{0,1\}\), including when a word uses only one letter. Scattered subsequences preserve order but need not be contiguous. Words are indexed, not identified under cyclic shifts, reversal, or complementation. The graph \(G_w\) has all \(n\) positional vertices, including isolated ones. The conditional ensemble fixes the exact number of unequal adjacent pairs, not the number of zeros or ones. In the length-zero case only the empty word occurs. For the conditional mean assume \(n\ge2\) and \(0\le t\le n-1\).

## Proof
**Greedy arches and matchings.** Cut a binary word repeatedly at the earliest next appearance of both symbols, leaving a final suffix containing at most one symbol. Each complete arch uniquely has the form \(a^r\bar a\), with \(r\ge1\). If there are \(h\) complete arches, then every length-\(h\) target embeds by choosing its successive symbols from the respective arches. Conversely, write \(b_j\) for the final letter of arch \(j\) and choose a letter \(c\) absent from the residual suffix. The greedy leftmost embedding of \(b_1\cdots b_h\) ends precisely at the \(h\)-th arch boundary, since \(b_j\) does not occur in its arch before the final position. Therefore \(b_1\cdots b_hc\) does not embed. Hence \(\iota(w)=h\).

An arch always closes on an unequal-adjacency edge, and a further arch cannot close on an edge sharing an endpoint with the preceding closing edge. It does close on the earliest subsequent nonoverlapping unequal-adjacency edge. This is precisely the left-to-right maximum-matching greedy rule for a path: choose its first present edge and skip the next edge. On a component consisting of \(\ell\) consecutive present edges this rule selects \(\lceil\ell/2\rceil\), which is optimal because the component has \(\ell+1\) vertices. Summing over components proves the displayed graph identity and run formula.

**Generating function and exact coefficients.** After the initial symbol, use two states: \(P\) is the ongoing, not-yet-complete arch; \(E\) means that the latest letter closed an arch. Let \(P(z,y,u)\) and \(E(z,y,u)\) enumerate possible remaining suffixes from these states, with \(z\) marking letters, \(y\) marking transitions, and \(u\) marking completed arches. From \(P\), a repeated bit leaves state \(P\), whereas an opposite bit closes an arch and enters \(E\). From \(E\), either bit starts a new arch; the opposite bit additionally contributes one transition. Thus
\[
P=1+zP+zyuE,\qquad E=1+z(1+y)P.
\]
Solving gives \(P=(1+zyu)/(1-z-z^2yu(1+y))\). There are two choices for the first bit, so the full series is \(1+2zP\), proving the rational formula. For \(k\ge1\), the coefficient of \(u^k\) is
\[
\frac{2z^{2k}y^k(1+y)^{k-1}(1+zy)}{(1-z)^{k+1}},
\]
which expands to the stated two-binomial expression. The allowed powers of \(y\) and \(z\) in these two terms give the exact feasible range \(\lceil t/2\rceil\le k\le\min(t,\lfloor n/2\rfloor)\); every integer in that range has a strictly positive coefficient (the endpoint cases follow from whichever binomial term is nonzero).

**Exact fixed-transition mean.** A binary word is determined by its first bit and its \(m=n-1\) transition indicators. Conditioned on \(t\) transitions, the indicator set is uniformly distributed over all \(t\)-subsets of \(\{1,\ldots,m\}\). The matching greedy algorithm selects the first, third, fifth, and subsequent odd-positioned edges in each maximal run of present edges. Fix an odd positive integer \(r\le t\). The probability that the first \(r\) edge indicators are present is \(\binom tr/\binom mr\). For any later position, the event that its indicator is the \(r\)-th consecutive present indicator since the most recent absent indicator has probability \((m-t)\binom tr/((m-r)\binom mr)\), whenever \(r<m\). There are \(m-r\) such later positions; for \(r=m=t\), only the initial-position term exists. Thus the expected number of selected edges in odd offset \(r\) is \((m-t+1)\binom tr/\binom mr\). Sum over odd \(r\) to obtain the stated exact conditional expectation.

**Limit law.** Suppose first \(0<\rho<1\). For every fixed \(r\), \(\binom{t_n}r/\binom{m}r\to\rho^r\), and the ratio is at most \((t_n/m)^r\). A geometric dominating sequence therefore gives
\[
\frac{\mathbb E[\iota\mid t_n]}m\longrightarrow
(1-\rho)\sum_{j\ge0}\rho^{2j+1}=\frac{\rho}{1+\rho}.
\]
For \(\rho=0\), use \(0\le\iota\le t_n\). For \(\rho=1\), use \(\lceil t_n/2\rceil\le\iota\le\lfloor n/2\rfloor\), giving a limit of \(1/2\).

It remains to pass from the mean to convergence in probability. Sample the uniform \(t\)-element edge set as the first \(t\) values of a uniform permutation of the \(m\) path-edge labels. Swapping a chosen and an unchosen edge changes the graph's maximum-matching number by at most one: remove both exceptional edges to obtain a common subgraph, and observe that adding either one increases its matching number by at most one. In the permutation-revelation martingale, conditioning on two possible next choices is coupled by such a swap, so its successive conditional expectations differ by at most one (a weaker constant two also suffices). Bounded martingale differences yield, for example, \(\Pr(|\iota-\mathbb E\iota|\ge s\mid t)\le2\exp(-s^2/(8m))\). Taking \(s\) proportional to \(n\) proves the limit in probability for every prescribed transition-density sequence.

## Verification
Run `python3 verify.py` with the standard library only. The verifier compares (i) the defining collection of scattered subsequences, (ii) direct greedy arch counts, and (iii) a separate maximum-matching dynamic program for every binary word of length at most ten. It then enumerates every indexed binary word through length sixteen and checks the joint counts and exact index ranges. An independent two-state polynomial transfer recurrence checks the coefficient formula through length ninety. Enumerating all subsets of transition positions through eleven positions checks the exact conditional-mean identity. Expected successful output: `TRANSITION_MATCHING_UNIVERSALITY_PASS direct_n<=10 words_n<=16 transfer_n<=90 means_m<=11`. These finite checks corroborate the proof; they do not certify its infinite quantifiers.

## Relationship to prior work
The greedy arch theorem is foundational, not claimed as new; see Barker, Fleischmann, Harwardt, Manea, and Nowotka. Adamson's 2023 study counts subsequence-universal words with algorithmic methods and raises closed-form enumeration questions. Schnoebelen and Veron study arch factorization and circular and compressed-word universality. The already published *Closed-form law for binary subsequence universality* determines precisely the \(y=1\) specialization of the joint generating function above, namely \((1+z)/(1-z-2uz^2)\). That unrefined count is explicitly prior work. The present result concerns the **joint** transition-index distribution, the matching interpretation, the exact fixed-transition law, and its transition-density limit. General methods for counting regular-language universality do not by themselves state these exact refinements.

## Limitations
The theorem concerns binary words and exactly their adjacent unequal-pair count, not symbol counts, q-ary words, or cyclic transition counts. The first-moment formula and limit law condition on transitions, not on a Bernoulli parameter. Classical enumerations of path-subgraph maximum matching numbers, possibly under different graph terminology, may overlap with the joint formula; available source comparisons do not establish absolute uniqueness. The proof and finite verifier do not constitute an independent external audit.

## References
1. Laura Barker, Pamela Fleischmann, Katharina Harwardt, Florin Manea, Dirk Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1, March 10, 2020. https://arxiv.org/abs/2003.04629
2. Duncan Adamson, *Ranking and Unranking k-Subsequence Universal Words*, arXiv:2304.04583v1, April 10, 2023. https://arxiv.org/abs/2304.04583
3. Philippe Schnoebelen, Julien Veron, *On Arch Factorization and Subword Universality for Words and Compressed Words*, arXiv:2304.11932v1, April 24, 2023. https://arxiv.org/abs/2304.11932
4. Pamela Fleischmann, Jonas Höfer, Annika Huch, Dirk Nowotka, *α-β-Factorization and the Binary Case of Simon's Congruence*, arXiv:2306.14192v1, June 25, 2023. https://arxiv.org/abs/2306.14192
5. Duncan Adamson, Pamela Fleischmann, Annika Huch, Tore Koß, Florin Manea, Dirk Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658v1, November 17, 2023. https://arxiv.org/abs/2311.10658
6. *Closed-form law for binary subsequence universality*, publicly available mathematical finding, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37
