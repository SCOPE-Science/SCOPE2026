# Shortest-absent-subsequence spectra of repeated permutation arches

## Finding
For integers \(q,t\ge1\), let \(I_q=(1,2,\ldots,q)\) be a word of distinct alphabet symbols and let \(\pi\) be any permutation of those symbols. Write \(W=I_q^t\pi\). Every shortest absent subsequence of \(W\) has length \(t+2\). For a proposed subsequence \(x_1\cdots x_{t+2}\), absence holds **exactly when**
\[
x_1\ge x_2\ge\cdots\ge x_{t+1}\quad\text{and}\quad p_\pi(x_{t+1})\ge p_\pi(x_{t+2}),
\]
where \(p_\pi(v)\) is the index of \(v\) in \(\pi\). The resulting number is
\[
A_{q,t}(\pi)=\sum_{v=1}^{q}\binom{q-v+t}{t}p_\pi(v).
\]
For \(t=2\), exact exhaustive permutation enumeration yields the following complete finite spectra. An interval with listed exclusions denotes *every integer* in the interval except the exclusions.

| \(q\) | Range of \(A_{q,2}\) | Excluded integers | Attained values |
| --- | --- | --- | --- |
| 1 | 1–1 | none | 1 |
| 2 | 5–7 | 6 | 2 |
| 3 | 15–25 | 16, 19, 20, 21, 24 | 6 |
| 4 | 35–65 | 36, 40, 44, 47, 48, 52, 53, 56, 60, 64 | 21 |
| 5 | 70–140 | 71, 79, 87, 91, 119, 123, 131, 139 | 63 |
| 6 | 126–266 | 127, 265 | 139 |
| 7 | 210–462 | 211, 461 | 251 |

Thus \(q=6\) is the first alphabet size **among \(q\ge3\)** for which the nonlinear \(t=2\) spectrum has no gaps other than the two immediate-neighbor gaps at the endpoints, and this property persists at \(q=7\). No conclusion is drawn for larger alphabets.

## Assumptions and scope
Subsequence always means order-preserving scattered subsequence, not contiguous substring. All \(q\) symbols are distinct and totally ordered in the first \(t\) copies. Symbols are tokens, not digits; repetition means word concatenation. A shortest absent subsequence (SAS) is an absent word of minimum possible length over the same \(q\)-symbol alphabet. The analytic result holds for every positive \(q,t\), and the exhaustive spectrum statement is restricted to \(t=2\) and \(1\le q\le7\).

## Proof
Every length-\(t+1\) word embeds in \(W\): choose its first \(t\) symbols in successive copies of \(I_q\), and its last symbol from \(\pi\). Yet the word consisting of \(t+2\) consecutive copies of a single symbol is absent, since each symbol occurs exactly \(t+1\) times. Therefore SAS length is exactly \(t+2\).

A prefix \(x_1\cdots x_{t+1}\) embeds into \(I_q^t\) if any adjacent pair is strictly increasing. Indeed, partition this prefix just after every weak descent; at most \(t\) increasing blocks result when at least one of its \(t\) comparisons is increasing. Place the consecutive blocks into distinct increasing copies of \(I_q\). Conversely, if every comparison is weakly decreasing, each pair of consecutive symbols requires a new increasing copy; the prefix needs \(t+1\) copies and cannot embed in \(I_q^t\).

If the prefix fits in \(I_q^t\), the final symbol embeds in \(\pi\), so the proposed word occurs. Hence absence forces the entire prefix to be weakly decreasing. In this situation the first \(t\) symbols can be placed, one per copy of \(I_q\). The remaining last two symbols fit in \(\pi\) exactly when their positions there are strictly increasing. If they fit, the whole word occurs. If they do not, no embedding can exist: placing just the final symbol in \(\pi\) would require an impossible \(t+1\)-symbol prefix in \(I_q^t\), while placing three or more suffix symbols in \(\pi\) would in particular require the final two to be in increasing \(\pi\)-position order. This proves the absence criterion in both directions.

Fix \(v=x_{t+1}\). There are \(\binom{q-v+t}{t}\) weakly decreasing choices for the first \(t\) letters from \(\{v,\ldots,q\}\), by combinations with repetition. Exactly \(p_\pi(v)\) choices of the final letter satisfy the second weak inequality. Multiplication followed by summation over \(v\) gives the displayed count.

For the finite spectrum, the included source `verify.py` visits all \(q!\) permutations for each \(1\le q\le7\), computes the exact binomial weighted sum using integer arithmetic, and reports precisely the table's endpoints, omissions and support sizes. This is an exhaustive finite proof of the bounded spectrum claim, not a sampling experiment. The source also independently tests direct subsequence enumeration on all \(99\) triples \((q,t,\pi)\) with \(1\le q\le4\), \(1\le t\le3\), for additional consistency of the analytic formula.

The extremal endpoints are independently determined from the rearrangement inequality because \(\binom{q-v+t}{t}\) strictly decreases with \(v\): the minimum is attained at the identity, and the maximum at reversal. In the \(t=2\) case the minimum simplifies to \(\binom{q+3}{4}\), as verified by the hockey-stick identity.

## Verification
Run `python3 verify.py` using only the Python standard library. Expected terminal assertion is `ALL_SAS_ARCH_SPECTRUM_CHECKS_PASSED`. The program's deterministic exhaustive enumeration proves the finite spectra conditional on the transparent integer arithmetic implementation; no computer search is used as a substitute for the universal counting proof.

## Relationship to prior work
Kosche, Koß, Manea and Siemer developed the formal SAS/MAS framework and general combinatorial characterizations, including a maximum-count result. The present claim does not assert novelty for the SAS definition, general enumeration algorithms, or the extremal rearrangement principle. Barker and collaborators developed scattered-factor universality and arch decompositions. The first linear-weight case \(t=1\) reduces to a classical rank-displacement statistic; the full attainable support of that statistic is already described by Vořechovský (2012, Section 3.4.1). **The contribution considered here is the all-\(t\) closed weighted formula together with the exact first nonlinear \(t=2\) finite spectrum and its sharp alphabet-size-six gap transition.**

## Limitations
No claim is made about the attainable-value spectrum for \(q\ge8\), for arbitrary unrelated successive permutations, or for general words outside \(I_q^t\pi\). The accessible published material was inspected for close implications, but unindexed results about triangular-weight permutation sums could subsume the finite spectrum; independent review remains necessary. The 2012 rank support law covers the \(t=1\) specialization, which is excluded from the originality assertion.

## References
1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (first public preprint 2021-08-31), https://arxiv.org/pdf/2108.13968 ; journal version Fundamenta Informaticae 189 (2023), DOI 10.3233/FI-222159.
2. M. Barker et al., *Scattered Factor-Universality of Words*, arXiv:2003.04629, https://arxiv.org/pdf/2003.04629.
3. M. Vořechovský, *Correlation control in small sample Monte Carlo type simulations II*, Probabilistic Engineering Mechanics 29 (2012), pp. 105–120, Section 3.4.1, https://www.fce.vutbr.cz/stm/vorechovsky.m/papers/19j.pdf.
