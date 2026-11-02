# Exact EFX orientation counts and a parity law for uniform multistars

## Finding
Let \(b,q\ge2\). Take a multistar with one center, \(b\) leaves, and exactly \(q\) separately labeled parallel edges from the center to each leaf. Each edge has value \(1\) to both endpoints and value \(0\) to every other agent. Every edge is oriented to one endpoint, and EFX uses the **all-goods** requirement: for every ordered pair of distinct agents and **every** edge in the second agent's bundle, deleting that edge removes envy.

Let \(N_q(b)\) be the number of labeled EFX orientations, set \(s=\lfloor q/2\rfloor\), and define
\[
P_q(z)=\sum_{h=0}^{s}\binom{q}{h}z^h,\qquad A_q=P_q(1).
\]
There is an exact finite formula for every \(b,q\ge2\):
\[
N_q(b)=\sum_{\substack{0\le y_1,\ldots,y_b\le s\\ \sum_i y_i+\min_i y_i\ge q-1}}
\prod_{i=1}^b\binom q{y_i}+3b\,\mathbf{1}_{\{q=3\}}. \tag{1}
\]
For \(b\ge\max\{2,q-1\}\) this simplifies to the polynomial correction of one exponential:
\[
N_q(b)=A_q^b-\sum_{t=0}^{q-2}[z^t]P_q(z)^b+3b\,\mathbf{1}_{\{q=3\}}. \tag{2}
\]
In particular, for every \(b\ge2\),
\[
N_2(b)=3^b-1,\qquad N_3(b)=4^b-1,
\]
and for \(b\ge3\),
\[
N_4(b)=11^b-1-10b-16\binom b2.
\]
Under independent fair-coin orientations of all \(bq\) edges, the exact exponential decay constant is
\[
\lim_{b\to\infty}\left(\frac{N_q(b)}{2^{bq}}\right)^{1/b}
=\frac{A_q}{2^q}=
\begin{cases}
\tfrac12,&q\text{ odd},\\
\tfrac12+\dfrac{\binom q{q/2}}{2^{q+1}},&q\text{ even}.
\end{cases} \tag{3}
\]
More precisely, at each fixed \(q\), \(N_q(b)=A_q^b-O_q(b^{q-2})\), with the correction in (2) explicit.

## Assumptions and scope
The center and the \(b\) leaves are distinct agents; every parallel edge is an individually distinct good. An orientation is complete and nonwasteful: an edge goes to exactly one of its two incident agents. Agent utility is additive with the stated \(0\)-\(1\) incidence values. There are no loops, other edges, or other goods. The quantified EFX notion includes deleting zero-valued-to-the-comparer goods; replacing it by a positive-good-only convention changes the answer. The result is a counting statement for this uniform multistar family, not a general graph counting formula.

## Proof
Write \(y_i\) for the number of edges directed to the center from leaf \(i\), \(x_i=q-y_i\) for those directed to leaf \(i\), and \(C=\sum_i y_i\) for the center's utility. For fixed numbers \((y_i)\), exactly \(\prod_i\binom q{y_i}\) labeled orientations realize them.

Two different leaves value each other's entire bundles at \(0\) and cannot strongly envy one another. The center comparing itself with leaf \(i\) is EFX precisely when \(C\ge x_i-1\), since every good in leaf \(i\)'s bundle is worth \(1\) to the center; the condition is vacuous if this bundle is empty, and the displayed inequality then holds automatically. Over all leaves this is equivalent to
\[
C+\min_i y_i\ge q-1.\tag{4}
\]

For leaf \(i\) comparing itself with the center, the center's bundle contains \(y_i\) goods worth \(1\) to leaf \(i\). If some \(y_j>0\) with \(j\ne i\), the center also owns a good worth \(0\) to leaf \(i\). Deleting that zero-valued good proves that the exact EFX condition is \(x_i\ge y_i\), or \(y_i\le\lfloor q/2\rfloor\). If the center owns no goods from another leaf, the most adverse deletion removes one of its \(y_i\) valuable goods, so the condition weakens to \(x_i\ge y_i-1\) (automatically true when \(y_i=0\)).

Thus every ordinary allowed vector satisfies \(0\le y_i\le s\) for all leaves, together with (4). A vector violating \(y_i\le s\) can pass the leaf test only if all other center receipts vanish, and then only when \(q=2s+1\) is odd and \(y_i=s+1\). Since \(b\ge2\), (4) reduces in this case to \(s+1\ge2s\), hence \(s\le1\). With \(q\ge2\) this happens only at \(q=3\), with exactly one exceptional leaf receiving \(y_i=2\) center-directed edges. There are \(b\binom32=3b\) such labeled orientations. This proves (1), without double counting.

If \(b\ge q-1\) and the total \(t=\sum_i y_i\) is less than \(q-1\), some \(y_i=0\) by the pigeonhole principle, and (4) fails. Conversely, totals \(t\ge q-1\) automatically satisfy (4) because \(\min_i y_i\ge0\). Subtracting from all ordinary vectors the weighted counts of totals \(t\le q-2\) proves (2). Expanding low-degree coefficients yields the stated formulas at \(q=2,3,4\).

For each fixed \(q\), the omitted coefficients in (2) are polynomials in \(b\) of degree at most \(q-2\): a monomial of total degree at most \(q-2\) selects nonzero contributions from at most \(q-2\) factors. Hence they are \(O_q(b^{q-2})\), including the exceptional \(3b\) correction when \(q=3\). Since \(A_q>1\), the exponential base in (3) is \(A_q/2^q\). Binomial symmetry gives \(A_q=2^{q-1}\) for odd \(q\), and \(A_q=2^{q-1}+\binom q{q/2}/2\) for even \(q\). This proves (3).

## Verification
The accompanying standalone Python program `verify.py` independently enumerates the full \(2^{bq}\) labeled orientations and tests EFX directly by evaluating each ordered agent pair and each possible deleted good. It compares these results to (1) over thirteen small parameter pairs, and separately checks the coefficient formula (2), including several values outside its stable range through (1). Its actual run returned:

`VERIFY_OK exact_labeled_orientation_cases= 13 binomial_profiles= 56`

This computation checks finite instances only; the preceding argument proves the formulas for every \(b,q\ge2\).

## Relationship to prior work
Afshinmehr, Danaei, Kazemi, Mehlhorn, and Rathi determine **existence** of EFX orientations for multistars and larger bipartite multigraph classes; their Proposition 3.1 and Proposition 4.3 produce multistar orientations for arbitrary valuations, but do not count all labeled fair orientations. Hsu establishes general bi-valued multigraph orientability and hardness results, not an exact unit-multistar census. Kanellopoulos, Nemery, Pergaminelis, Sotiriou, and Vasilakis investigate parameterized EFX orientation **decision** algorithms, including bounded treewidth and maximum shared value; they do not imply the particular closed-form enumeration or parity-dependent random-orientation base. The present statement concerns exact counting and typical-case probability of already-existing fair orientations, not improved existence or complexity guarantees.

## Limitations
These formulas require uniform parallel multiplicity, identical unit valuations, and all-goods EFX. They do not classify heterogeneous multiplicities, nonuniform weights, all EFX allocations (as opposed to orientations), or efficient sampling. Comparison with indexed literature and available related full texts cannot exclude equivalent unpublished or unindexed formulas. No independent audit has been performed.

## References
1. S. Kanellopoulos, E. Nemery, C. Pergaminelis, M. M. Sotiriou, and M. Vasilakis, *EF(X) Orientations: A Parameterized Complexity Perspective*, arXiv:2512.25033 (first posted 2025-12-31), https://arxiv.org/abs/2512.25033.
2. M. Afshinmehr, A. Danaei, M. Kazemi, K. Mehlhorn, and N. Rathi, *EFX Allocations and Orientations on Bipartite Multi-graphs: A Complete Picture*, arXiv:2410.17002 (first posted 2024-10-22), https://arxiv.org/abs/2410.17002; published in *Autonomous Agents and Multi-Agent Systems* 40 (2026), https://doi.org/10.1007/s10458-026-09754-8.
3. K. Hsu, *EFX Orientations of Multigraphs*, arXiv:2410.12039 (first posted 2024-10-15), https://arxiv.org/abs/2410.12039; ECAI 2025 proceedings, https://doi.org/10.3233/FAIA251259.
4. G. Christodoulou, A. Fiat, E. Koutsoupias, and A. Sgouritsa, *EFX Allocations on Graphs*, EC 2023, https://doi.org/10.1145/3580507.3597764.
