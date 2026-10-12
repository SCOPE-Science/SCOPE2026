# Exact minimum discrepancy for ternary de Bruijn sequences of order five

## Finding
For a cyclic de Bruijn sequence \(B\) of order \(5\) on \(\Sigma=\{0,1,2\}\), let \(\mathcal C(B)\) consist of every cyclic consecutive factor of length at most \(3^5=243\). For distinct symbols \(i,j\), let \(\#_i(U)\) count occurrences of \(i\) in \(U\). Define
\[
\operatorname{disc}(B)=\max_{i\ne j}\max_{U\in\mathcal C(B)}\big|\#_i(U)-\#_j(U)\big|.
\]
Then the smallest attainable discrepancy is **exactly \(5\)**:
\[
\min_{B\in\mathcal B_3(5)}\operatorname{disc}(B)=5.
\]
The file `witness.txt` specifies a complete \(243\)-symbol witness; `verify.py` independently checks every length-\(5\) circular factor and all circular substring imbalances.

## Assumptions and scope
The alphabet consists of three **distinct** symbols \(0,1,2\). A de Bruijn sequence of order \(5\) is a cyclic word of length \(243\) in which every word in \(\Sigma^5\) occurs exactly once as a length-\(5\) circular factor. Discrepancy compares counts of **each pair of different symbols** over every circular factor, including wraparound factors. There is no claim about different alphabets or orders.

## Proof
**Lower bound.** Every such word contains the factor \(00000\). On this factor the difference between the numbers of \(0\)'s and \(1\)'s is \(5\), hence \(\operatorname{disc}(B)\ge 5\) for every admissible \(B\).

**A matching finite witness.** The file `witness.txt` is a length-\(243\) word over \(\Sigma\) with exactly \(81\) occurrences of each symbol. The exhaustive, finite certificate implemented by `verify.py` forms the \(243\) circular windows of length \(5\) at positions \(0,\ldots,242\), checks their pairwise distinctness, and thus certifies that all \(3^5=243\) words are present exactly once.

For a fixed pair \(i,j\), define prefix balance \(H_{ij}(t)=\#_i(B[0:t])-\#_j(B[0:t])\) for \(0\le t\le 243\). The exact verified extrema are:

| Pair \((i,j)\) | Minimum of \(H_{ij}\) | Maximum of \(H_{ij}\) | Difference |
|---|---:|---:|---:|
| \((0,1)\) | \(-4\) | \(1\) | \(5\) |
| \((0,2)\) | \(-4\) | \(1\) | \(5\) |
| \((1,2)\) | \(-2\) | \(3\) | \(5\) |

Because every symbol appears \(81\) times, \(H_{ij}(243)=H_{ij}(0)=0\). For a nonwrapping factor beginning at \(a\) and ending at \(b\), the count difference equals \(H_{ij}(b)-H_{ij}(a)\). A wrapping factor is the complement of a nonwrapping factor, so its signed count difference is the negative of the complementary factor's signed count difference. Therefore, the maximum absolute count difference over **all cyclic factors** equals \(\max_t H_{ij}(t)-\min_t H_{ij}(t)\). The three recorded widths are all \(5\), proving \(\operatorname{disc}(B)=5\). Together with the lower bound this proves the stated minimum.

## Verification
Run `python3 verify.py` using a standard Python \(3\) interpreter. The checker is self-contained; it embeds the exact witness while `witness.txt` supplies the same human-readable word. It verifies the period, alphabet, symbol frequencies, uniqueness of all \(243\) order-\(5\) windows, the three prefix ranges, and **all \(243^2\) circular factors** by independent direct scanning of every starting position and length. Its expected terminal output begins `VERIFY_OK` and displays the three pair ranges. These are finite exhaustive checks: the universal optimization statement relies additionally on the explicit lower-bound argument, not on sampling or extrapolation.

## Relationship to prior work
Álvarez, Becher, Mereb, Pajor, and Soto (arXiv:2407.17367, public from July \(24\), \(2024\)) establish the general nonbinary upper bound of order plus one and conjecture that the lower bound is attained outside the two identified order-\(2\) exceptions. The subsequently circulated author-hosted version, *De Bruijn Sequences with Minimum Discrepancy* (July \(2025\), sections \(5.1\)–\(5.2\), Table \(2\)), lists exact ternary values through order \(4\) but leaves the ternary order-\(5\) cell empty. This finite witness determines precisely that previously unlisted natural case. The older Gabric–Sawada paper concerns primarily **binary** sequences and does not imply the ternary result. Numerical agreement or absence from a search index is not by itself a claim of global priority.

## Limitations
This establishes one natural finite extremal value, not a uniform construction for all alphabet sizes/orders, nor an algorithm guaranteed to optimize general instances. External independent validation and exhaustive priority verification have not been performed; an unindexed equivalent or subsequently published construction may exist. The checker establishes an exact finite certificate and does not certify any general conjecture beyond this specified parameter.

## References
1. N. Álvarez, V. Becher, M. Mereb, I. Pajor, C. M. Soto, *De Bruijn Sequences with Minimum Discrepancy*, arXiv:2407.17367v1, first made public \(2024\)-\(07\)-\(24\).
2. Same authors, expanded author-hosted version, July \(2025\), `https://staff.dc.uba.ar/becher/papers/optimal.pdf`, sections \(5.1\), \(5.2\), Table \(2\).
3. D. Gabric and J. Sawada, *Investigating the discrepancy property of de Bruijn sequences*, Discrete Mathematics \(345\) (\(2022\)), article \(112780\), DOI:10.1016/j.disc.2021.112780.
