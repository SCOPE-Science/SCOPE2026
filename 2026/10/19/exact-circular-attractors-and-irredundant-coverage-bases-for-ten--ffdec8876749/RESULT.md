# Exact circular attractors and irredundant coverage bases for ten dyadic paperfolding prefixes

## Finding

Let \(p_j\) be the regular paperfolding sequence, indexed by positive integers, with \(p_j=0\) if the odd part of \(j\) is congruent to \(1\pmod 4\), and \(p_j=1\) otherwise. Set \(P_k=p_1p_2\cdots p_{2^k}\), for \(1\le k\le10\). For a finite circular word \(w\), let \(\gamma_c(w)\) denote the smallest number of positions meeting a circular occurrence of every nonempty circular factor of length at most \(|w|\). Let \(h_c(w)\) be the number of **distinct inclusion-minimal position-coverage sets** of these factors.

**Finite exact theorem.** The complete profiles for the first ten dyadic stages are

\[
(\gamma_c(P_1),\ldots,\gamma_c(P_{10}))=(1,2,3,3,4,5,5,6,6,7)
\]

and

\[
(h_c(P_1),\ldots,h_c(P_{10}))=(1,2,6,12,17,23,31,39,47,55).
\]

The \(h_c\) constraints form the **unique irredundant subfamily of distinct factor-coverage sets** equivalent to the full circular-attractor condition for arbitrary selected sets of positions. In particular, the length-\(1024\) prefix has exactly \(868{,}847\) distinct nonempty circular factors but only \(55\) inclusion-minimal factor-coverage sets, and its minimum circular-attractor size is exactly \(7\).

The accompanying exact-rational certificate supplies all the following values and the corresponding explicit upper-bound sets (zero-based indices):

| \(k\) | \(|P_k|\) | \(\gamma_c(P_k)\) | \(h_c(P_k)\) | Distinct circular factors | Optimal witnessing positions | Dual lower value |
|---:|---:|---:|---:|---:|---|---:|
| 1 | 2 | 1 | 1 | 2 | `0` | \(1\) |
| 2 | 4 | 2 | 2 | 13 | `2,3` | \(2\) |
| 3 | 8 | 3 | 6 | 52 | `1,5,7` | \(7/3\) |
| 4 | 16 | 3 | 12 | 208 | `3,9,13` | \(3\) |
| 5 | 32 | 4 | 17 | 847 | `3,7,23,29` | \(7/2\) |
| 6 | 64 | 5 | 23 | 3,407 | `7,21,34,47,59` | \(9/2\) |
| 7 | 128 | 5 | 31 | 13,615 | `15,39,91,98,119` | \(5\) |
| 8 | 256 | 6 | 39 | 54,383 | `47,71,83,155,191,228` | \(23/4\) |
| 9 | 512 | 6 | 47 | 217,327 | `119,191,268,295,351,403` | \(6\) |
| 10 | 1,024 | 7 | 55 | 868,847 | `159,311,383,583,725,818,1004` | \(51/8\) |

## Assumptions and scope

The word \(P_k\) has **exactly** \(2^k\) positions, numbered \(0,1,\ldots,2^k-1\). For each length \(1\le\ell\le2^k\), the \(2^k\) circular substrings are read modulo \(2^k\), including those crossing the final-to-initial boundary. For a factor \(f\), define its **coverage**

\[
C(f)=\bigcup_{\substack{0\le s<|P_k|\\P_k[s\ldots s+|f|-1]_{\rm circular}=f}}
 \{s,s+1,\ldots,s+|f|-1\}\pmod{|P_k|}.
\]

An attractor \(T\) intersects every \(C(f)\). Our formula for \(p_j\) is an explicit standard paperfolding convention; complementing every bit leaves every coverage and attractor invariant after relabelling factors. The assertions are *finite*, restricted to the ten stated lengths. They do not claim an infinite formula for all dyadic stages, any asymptotic law, or counts of optimal position sets.

## Proof

**Finite coverage reconstruction.** For a length-\(n\) circular word \(w\), each factor is the literal substring of \(ww\) beginning at a start \(s\in\{0,\ldots,n-1\}\) and having length \(\ell\in\{1,\ldots,n\}\). Its occurrence covers exactly the consecutive cyclic positions \(s,\ldots,s+\ell-1\). The executable checker enumerates every one of these \(n^2\) pairs, groups factors by literal byte equality (not a probabilistic hash), and ORs the exact position masks. Consequently the resulting dictionary contains **all** distinct circular factors and the full coverage \(C(f)\) of each one, without truncating or sampling.

**Upper bounds.** For each of the ten prefixes, the positions listed in the table meet every computed coverage mask; this is checked against the entire dictionary, not merely a candidate subfamily. Hence each listed set is a genuine circular attractor.

**Exact rational lower bounds.** In `paperfolding_certificates.json` the entry for each stage contains a positive integer denominator \(D\) and triples `[length,start,numerator]`. Each triple names the actual circular factor starting at `start` and gives it the nonnegative rational weight \(a_f/D\). The checker reconstructs the factor's **complete** coverage from the dictionary and verifies, separately for every position \(i\),

\[
\sum_{f:\,i\in C(f)}a_f\le D.
\]

For any circular attractor \(T\), double counting gives

\[
\sum_f a_f
\le\sum_{i\in T}\sum_{f:\,i\in C(f)} a_f
\le D|T|.
\]

The verified weighted sums are the rational values in the final table column. Their ceilings equal the sizes of the explicit upper witnesses in every row. Thus no smaller attractor is possible. In the largest case only \(21\) weighted circular factors are necessary, with total \(51/8\); since every selected position carries at most weight \(1\), six positions cannot suffice.

**Canonical irredundant coverage bases.** Form the set \(\mathcal C\) of distinct coverage masks for every circular factor. Sort them by increasing number of set bits. Retain \(M\in\mathcal C\) exactly when no previously retained mask is a subset of \(M\). This produces **all and only** inclusion-minimal masks: any strict subset would have appeared earlier, and every nonminimal mask contains a minimal one. Counting the retained masks gives the second sequence above, verified for all ten cases. Every selection hitting these masks hits every member of \(\mathcal C\). Moreover no retained mask can be dropped: for a particular minimal mask \(M\), its complement intersects all other retained masks, by incomparability, but misses \(M\). Hence this distinct factor-derived coverage basis is irredundant.

All finite claims therefore follow from exact operations explicitly reconstructed in the standalone checker and the embedded certificate. There is no appeal to extrapolation from the displayed prefix lengths.

## Verification

Run `python3 verify_paperfolding.py` alongside `paperfolding_certificates.json` using Python 3 and its standard library only. The program regenerates the paperfolding prefix from the odd-part rule; enumerates every circular factor from literal bytes; reconstructs all position-coverages; checks each claimed factor count, each attractor witness, every weighted-cover inequality, each strict lower bound, and the canonical inclusion-minimal coverage count. It prints `ALL TEN EXACT CERTIFICATES VERIFIED` after all assertions pass. The actual recorded execution appears in `verification_output.txt`.

The verification is exhaustive for **each of the ten specified finite words**, including the length-\(1024\) word. It is not an exhaustive search over all larger dyadic words and not an independent audit.

## Relationship to prior work

The circular-attractor definition is that of Mantaci, Restivo, Romana, Rosone, and Sciortino (2021), with the checking formulation developed by Romana (2023). Faro, Marino, and Pavone (first public version October 7, 2026) determine minimal factor-coverages for **ordinary (noncircular) Thue–Morse** words; their structural question motivates computing the distinct canonical coverages of a different automatic word in the circular setting. Schaeffer and Shallit study ordinary attractors of automatic sequences; Banbara and collaborators study smallest **ordinary** attractors for Fibonacci and period-doubling words.

An accessible pre-existing calculation of dyadic **ordinary** paperfolding attractors supplies some numerically matching cardinalities, including values \(5,6,6,7\) at lengths \(128,256,512,1024\). These numerical coincidences are acknowledged as prior data. Already at length \(8\), however, the previously reported ordinary minimum is \(2\) while the circular minimum proved here is \(3\). The ordinary figures do **not** imply the present circular claim: a circular word has different factors, additional wraparound occurrences, and different coverage masks, and the two attractor notions are not generally ordered. The contribution here is the exact circular profile and its irredundant coverage basis, not rediscovery of the ordinary minima or a general factor-coverage lemma.

## Limitations

The complete numerical classification ends at length \(1024\). The apparent pattern in the canonical counts for the last several stages is not asserted for subsequent stages. Although the certificate proves every displayed finite value, it does not supply a symbolic all-\(k\) recurrence for the coverage hypergraphs. The exact optimal position sets are not all classified: one optimum witness per prefix is provided. Literature coverage may be incomplete, particularly for unindexed computations of circular paperfolding factors. Independent verification by another researcher has not been undertaken.

## References

1. S. Faro, F. P. Marino, and A. Pavone, *Smallest String Attractors and Minimal Coverage Certificates of Thue–Morse Words*, arXiv:2610.10950v1 (first public October 7, 2026), https://arxiv.org/abs/2610.10950.
2. G. Romana, *Algorithmic View on Circular String Attractors*, ICTCS 2023, https://ceur-ws.org/Vol-3587/9885.pdf.
3. S. Mantaci, A. Restivo, G. Romana, G. Rosone, and M. Sciortino, *A Combinatorial View on String Attractors*, Theoretical Computer Science 850 (2021), 236–248, doi:10.1016/j.tcs.2020.11.006.
4. L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840 (2020), https://arxiv.org/abs/2012.06840.
5. M. Banbara and collaborators, *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, arXiv:2602.16152v1 (first public February 18, 2026), https://arxiv.org/abs/2602.16152.
