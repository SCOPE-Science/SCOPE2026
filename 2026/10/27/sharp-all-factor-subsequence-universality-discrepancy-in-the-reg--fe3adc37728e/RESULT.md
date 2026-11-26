# Sharp all-factor subsequence-universality discrepancy in the regular paperfolding word

## Finding

Let \(p=p_0p_1\cdots\) be the binary regular paperfolding word, with \(p_n=0\) if the odd part of \(n+1\) is \(1\pmod4\), and \(p_n=1\) if it is \(3\pmod4\). For a finite word \(v\), let \(\iota(v)\) be the largest \(k\ge0\) for which every binary word of length \(k\) is a scattered subsequence of \(v\). Then for every \(a\ge0\) and \(N\ge1\),
\[
-11\le 8\iota(p_a\cdots p_{a+N-1})-3N\le7.
\]
Both endpoints are attained: \(p_7\cdots p_{23}=\mathtt{00011011000100111}\) and \(p_2\cdots p_{12}=\mathtt{10011000110}\) have index five and discrepancies \(-11\) and \(7\), respectively. In particular the density \(3/8\) holds uniformly in the starting position, with the displayed optimal two-sided bound. The contribution is the sharp discrepancy for **arbitrary factors**, not the previously known exact prefix law or the aligned dyadic formula implied by its proof.

## Assumptions and scope

The alphabet for universality is always \(\{0,1\}\), even if a factor contains only one symbol. Factors are contiguous and indices are zero-based. Complementing the infinite word does not change any universality index. The result is for the regular paperfolding word, not arbitrary fold instructions.

## Proof

Greedily end a block (an *arch*) at the first position at which both bits have appeared since the last cut. Track the incomplete arch by its state \(q\in\{\emptyset,0,1\}\), where a bit denotes the only letter seen. The number of completed arches is \(\iota\): choosing one requested symbol in each arch embeds every word of the corresponding length, whereas choosing the closing letters of successive arches and appending a bit absent from the rest gives a word that does not embed. Indeed the earliest possible match of those closing letters reaches the last arch end.

**Known aligned-block calculation.** Put \(B_j=p_{8j}\cdots p_{8j+7}\). The odd-part rule gives \(B_j=\mathtt{001}\,(j\bmod2)\,\mathtt{011}\,p_j\): among the first seven positions only the fourth depends on \(j\), and the odd part at the eighth equals that of \(j+1\). The four possibilities are \(\mathtt{00100110},\mathtt{00100111},\mathtt{00110110},\mathtt{00110111}\). The earlier exact-prefix proof [1, Proof §2] gives the transfer from states \(\emptyset,1\), with increment \(3-p_j+\mathbf1_{\{q=1\}}\) and outgoing state \(s(p_j)\), where \(s(0)=\emptyset\) and \(s(1)=1\). Starting with pending \(0\) has the same effect as starting empty: after the first bit \(0\), both states are \(0\) and neither has completed an arch. This extends the transfer to all three incoming states.

For \(K\ge1\) complete blocks ending at \(B_h\), the transfer adds \(3K-p_h+\mathbf1_{\{q=1\}}\) arches and ends in \(s(p_h)\); cancellation follows because the previous outgoing status contributes exactly the previous last bit. This recovers the earlier exact formula \(\iota(p_0\cdots p_{8J-1})=3J-p_{J-1}\). It also implies the aligned dyadic formula: for \(m\ge3\) take \(K=2^{m-3}\), start at block \(jK\), and use \(p_{(j+1)K-1}=p_j\) by the odd-part rule. The resulting index is \(3K-p_j\). Neither consequence is a separate novelty claim here.

**Arbitrary endpoints.** A factor wholly in one block is some \(B[r:s]\) with \(0\le r<s\le8\). If it touches two adjacent blocks it is \(B[r:8]C[0:s]\), with \(0\le r<8\), \(1\le s\le8\). Otherwise write it as the same two endpoint fragments with \(K\ge1\) complete blocks in between. Let \((c,q)\) be the arch count and final state on the initial suffix, read from empty; let \(z\) be the last bit of the final complete interior block; and let \(t\) be the arch count for the terminal prefix read from \(s(z)\). The discrepancy then equals
\[
8\bigl(c+\mathbf1_{\{q=1\}}-z+t\bigr)-3(8-r+s).
\]
The full-block length cancels, so this can be evaluated by inserting a single complete block ending in \(z\), regardless of the actual value of \(K\). For each regime, the following exhaustive upper-envelope computation treats the endpoint block words and, in the third regime, \(z\) as independent. All actual intervals are represented; not every tuple need occur.

| Regime | Number of cases | Minimum | Maximum |
|---|---:|---:|---:|
| One block | 144 | −10 | 6 |
| Two adjacent blocks | 1024 | −11 | 7 |
| Complete blocks in between | 2048 | −11 | 7 |

To obtain the table, form the four block words above. In the first row loop over every nonempty substring of each. In the second row loop over all ordered pairs of block words and every nonempty suffix of the left and prefix of the right. For the third row use the second row's loops and insert \(\mathtt{00100110}\) and \(\mathtt{00100111}\) in turn. For each resulting word \(v\), repeatedly remove its initial constant run together with the next bit (if that bit exists), count the removals \(h\), and compute \(8h-3|v|\). This is the greedy arch rule. The four words and the two representatives suffice by the block transfer, so the enumeration is not a finite-prefix extrapolation. Direct use of the odd-part rule gives the two factors in the finding. Their five completed arches verify sharpness and complete the proof.

## Reproducibility and limitations

The accompanying standalone `verify.py` calculates the same finite transfer and endpoint tables with a three-state scanner and checks both witnesses. Its longer finite-prefix tests are supplementary. The theorem supplies the optimal uniform bounds, not the full distribution of indices at each length. Literature comparison cannot rule out unindexed equivalent results.

## Relation to earlier work

The exact prefix record [1] already contains the eight-letter block identity, its two-state transfer and all prefix indices. Record [2] gives dyadic prefix indices for the broader class of generalized paperfolding words. Here the new calculation is the all-start boundary analysis giving sharp constants; an exact prefix law by itself does not give these constants. Schnoebelen and Veron [3] establish general arch methods; Shallit and Xu [4] treat repetition factorizations of regular paperfolding factors, a different statistic. Adamson et al. [5] study regular-language universality, not these sharp bounds for paperfolding factors.

1. *Exact scattered-subsequence universality of every regular paperfolding prefix*, <https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-exact-scattered-subsequence-universality-of-every-regular-paperf--44b326d79dc6/RESULT.md>, Proof §2–4.
2. *Dyadic scattered-subsequence universality of generalized paperfolding prefixes*, <https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-dyadic-scattered-subsequence-universality-of-generalized-paperfo--52dc399f6375/RESULT.md>.
3. P. Schnoebelen and J. Veron, *On arch factorization and subword universality for words and compressed words*, <https://arxiv.org/abs/2304.11932>.
4. J. Shallit and X. Xu, *Repetition factorization of automatic sequences*, <https://arxiv.org/abs/2311.14961>.
5. D. Adamson et al., *k-Universality of Regular Languages*, <https://arxiv.org/abs/2311.10658>.
