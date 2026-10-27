# Lucky-car enumerators for ordered clique bouquets under largest-neighbor parking

## Finding

Let \(r\ge 1\) and \(m_1,\ldots,m_r\ge1\). Form the vertex-labeled clique bouquet \(H=K_1\vee(K_{m_1}\sqcup\cdots\sqcup K_{m_r})\): its common hub has label \(1\), and the vertices of each peripheral clique receive consecutive labels, in the order of the cliques. Set \(N=1+\sum_{i=1}^{r}m_i\). A word of length \(N\) is *increasing* if its preferences are weakly increasing. Let \(\mathcal P^\uparrow(H)\) be the increasing words for which all cars park using the largest-neighbor rule, and let \(\ell(a)\) be the number of cars that park at their preferred vertices.

Put \(s_0=0\) and \(s_j=\sum_{i=1}^{j}(m_i-1)\). **Theorem:** the complete lucky-car polynomial is
\[
L_{m_1,\ldots,m_r}(u):=\sum_{a\in\mathcal P^\uparrow(H)}u^{\ell(a)}
=u+\sum_{j=1}^{r}u^{j}(1+u)^{s_{j-1}}\bigl((1+u)^{m_j}-1\bigr).
\]
In particular, the exact number of weakly increasing largest-neighbor parking functions is
\[
L_{m_1,\ldots,m_r}(1)=1+\sum_{j=1}^{r}2^{s_{j-1}}(2^{m_j}-1).
\]

For adjacent clique sizes \(m_j=a\) and \(m_{j+1}=b\), let \(L_{\ldots,a,b,\ldots}\) and \(L_{\ldots,b,a,\ldots}\) correspond to swapping their *positions in the label order*. Then
\[
L_{\ldots,a,b,\ldots}(u)-L_{\ldots,b,a,\ldots}(u)
=u^j(1+u)^{s_{j-1}}\bigl((1+u)^{a-1}-(1+u)^{b-1}\bigr).
\]
Therefore placing larger peripheral cliques first maximizes the entire lucky-car polynomial **coefficientwise** among all orders of any fixed multiset of clique sizes; increasing size order minimizes it. Each swap of unequal adjacent sizes produces a nonzero coefficientwise improvement in the asserted direction.

The family interpolates between stars \((m_1=\cdots=m_r=1)\), for which \(L(u)=u+u^2+\cdots+u^{r+1}\), and complete graphs \((r=1)\), for which \(L(u)=u(1+u)^{m_1}\). For friendship graphs with hub label \(1\) and consecutively labeled pairs \((m_1=\cdots=m_r=2)\), the total count is \(3\cdot2^r-2\). Label order genuinely matters: the same unlabeled bouquet with clique sizes \((2,3)\) has \(18\) such words, versus \(20\) in the order \((3,2)\); the polynomial difference is \(u^2+u^3\).

## Assumptions and scope

Graphs are finite, simple, and labeled by \(\{1,\ldots,N\}\). The cliques are disjoint except for the added common hub, which is not itself a vertex of any \(K_{m_i}\); all \(m_i\) are positive and \(r\ge1\). Labels inside a peripheral clique form a consecutive integer interval, and those intervals occur in the prescribed order above label \(1\). The *largest-neighbor rule* is: a car starts at its preferred vertex; if empty, it parks. Otherwise, at its occupied current vertex it parks at the largest unoccupied neighbor of greater label if one exists; if none exists, it moves to the smallest neighbor of greater label and repeats, failing if no greater-labeled neighbor exists. A car is *lucky* precisely when it parks at its original preferred vertex. The polynomial counts words with named vertex preferences, not words modulo graph symmetries.

## Proof

**1. Increasing complete-clique lemma.** Consider a complete graph on an integer interval of \(t\ge1\) available vertices, processed by \(t\) cars with weakly increasing preferences in the same interval. Successful words are exactly those whose distinct preferred labels form a nonempty initial segment of the interval. To see necessity, the smallest vertex must be preferred, since moves only increase labels. If a label is omitted between two used preferred labels, then cars with lower preferences can fill that omitted position only by moving to the largest currently empty position, which would require all larger positions to be occupied; a subsequent car preferring a larger label must then fail. If the omitted position is not filled earlier, later preferences cannot reach it. Hence there can be no gap.

For sufficiency, take any increasing word whose distinct preferences form the first \(k\) labels, each used at least once. Process it from left to right. Inductively, after \(i\) distinct labels have appeared and \(d\) repeated occurrences have been processed, the occupied vertices are the first \(i\) positions and the highest \(d\) positions, disjoint. The next *new* preferred label occupies the next vertex of the initial segment; the next *repeated* preferred label occupies the largest remaining vertex. In either case this is possible because a word of length \(t\) with all \(k\) first labels present has \(t-k\) total repetitions and the required blocks do not overlap before the last car. Each new distinct preference is lucky, each repeat is not. Thus words with exactly \(k\) lucky cars correspond bijectively to compositions of \(t\) into \(k\) positive multiplicities, numbering \(\binom{t-1}{k-1}\). The complete-clique lucky polynomial is \(u(1+u)^{t-1}\); for \(t=0\) its empty-word contribution is \(1\).

**2. Conditioning on the hub preference.** In a successful word the hub must be occupied. Cars move only to greater labels, so at least one car must prefer \(1\). As preferences increase, exactly the first \(c\) cars prefer \(1\), for some \(1\le c\le N\). The first parks at the hub. Each of the next \(c-1\) cars parks at the largest currently unoccupied peripheral vertex: every such vertex is an upward neighbor of the hub. Thus exactly the largest \(c-1\) peripheral vertices are occupied and the remaining vacancies form the initial prefix of \(t=N-c\) peripheral labels, where \(0\le t\le N-1\).

**3. Independent residual clique words.** Let \(t_i\) be the number of positions in peripheral clique \(i\) among these \(t\) vacancies. The occupied vertices outside that prefix cannot be used by any subsequent car; from a peripheral vertex, every greater-labeled neighbor is in its own clique, never the hub or another clique. Consequently, precisely \(t_i\) later cars must prefer and park within the still vacant prefix of clique \(i\). Preferences outside that prefix are impossible: they are already occupied and have no greater vacant neighbor in their clique. Within the prefix, the process is exactly complete-clique largest-neighbor parking; filling the larger suffix in advance does not change which greater *vacant* neighbors are accessible. Thus the allowed words in different cliques contribute independently. Their preference intervals occur in increasing order, so no interleaving or multinomial factor is present. The first hub car contributes one lucky car; the other hub-preferring cars are unlucky. For this value of \(t\), the polynomial is therefore
\[
u\prod_{i:t_i>0}u(1+u)^{t_i-1}.
\]

**4. Summation.** If \(t=0\), the word is all ones and contributes \(u\). Otherwise, for a unique \(j\) there are \(m_i\) vacancies in each clique \(i<j\), between \(1\) and \(m_j\) vacancies in clique \(j\), and none later. Writing the partial size as \(h\in\{1,\ldots,m_j\}\), its contribution is \(u^{j+1}(1+u)^{s_{j-1}+h-1}\). Summing this finite geometric progression over \(h\) gives \(u^j(1+u)^{s_{j-1}}((1+u)^{m_j}-1)\). Summing over the unique partial clique proves the displayed polynomial and evaluation at \(u=1\).

**5. Reordering.** Only the two swapped summands change; all later exponents \(s_i\) depend on the same total size. Expanding and canceling their difference gives the displayed exchange identity. If \(a>b\), then \((1+u)^{a-1}-(1+u)^{b-1}=(1+u)^{b-1}((1+u)^{a-b}-1)\), which has nonnegative coefficients and is not zero. Repeated adjacent swaps establish both coefficientwise extrema and their strictness for unequal neighboring sizes.

## Verification

The included standalone Python program `verify.py` constructs the labeled graph and implements the specified parking procedure independently of the closed formula. It exhaustively checks every weakly increasing word for **all 127 ordered positive compositions whose total peripheral order is at most seven**. It separately validates **35 prefilled-suffix complete-clique instances** and **12 adjacent-swap identities**. Three independent coefficient calculations (direct parking, block-prefix convolution, and binomial expansion of the closed form) agree, returning `VERIFY_OK local_prefix_clique_cases=35 exhaustive_ordered_compositions=127 exchange_checks=12`.

Run `python3 verify.py` with Python 3 and no third-party packages. This finite verification checks examples and boundary handling; the infinite assertion is justified by the proof above, not extrapolated from the checks.

## Relationship to prior work

Hallam, Molebash, and Porter introduced this largest-neighbor parking rule for labeled graphs. Their Proposition 2.3 and Corollary 2.4 count increasing words on a complete graph, and their Section 3 treats entire parking-word totals on stars and describes disjoint-union shuffling. They explicitly ask in Questions 4.3–4.4 about combining graphs and counting graph-specific subfamilies including increasing words and lucky cars. Those prior results are credited, and the complete-clique lemma is included above for self-containment. The present result treats a connected common-hub gluing (rather than a disjoint union), determines a lucky-car polynomial for all positive block-size profiles, and establishes coefficientwise effects of label order. Directed graph parking and chip-firing \(G\)-parking functions in earlier literature use different rules and are not identified with this process.

## Limitations

The formula requires the hub to carry the smallest label and every peripheral clique to form an uninterrupted interval in the given order. Other labelings of the same unlabeled graph may have different results. It concerns only weakly increasing preference words; it does not enumerate arbitrary words on clique bouquets, nor does it resolve general graph-product questions. The proof and program have not been independently mathematically audited. Historical priority beyond the examined records is not certified.

## References

1. Joshua Hallam, Jenson Molebash, Chris Porter, *Parking with Frustrated Drivers*, arXiv:2609.35638v1 (first posted 28 September 2026), Sections 2.2, 3, and 4. https://arxiv.org/abs/2609.35638
2. Westin King and Catherine H. Yan, *Parking Functions on Directed Graphs and Some Directed Trees*, Electronic Journal of Combinatorics **27**(2), P2.48 (2020). https://doi.org/10.37236/9051
3. Brian Benson, Deeparnab Chakrabarty, Prasad Tetali, *G-parking functions, acyclic orientations and spanning trees*, Discrete Mathematics **310** (2010), 1340–1353. https://doi.org/10.1016/j.disc.2010.01.002
