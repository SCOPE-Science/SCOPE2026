# Uniformly spaced subsequence universality: exact spectra and shortest hosts

## Finding

Fix a labeled alphabet \(\Sigma\) of size \(q\ge2\) and an integer spacing \(s\ge1\). A pattern \(a_1\cdots a_k\) is an \(s\)-spaced scattered subsequence of \(w=w_1\cdots w_n\) when there are indices \(1\le i_1<\cdots<i_k\le n\) with \(i_{j+1}-i_j\ge s\) and \(w_{i_j}=a_j\). Let \(\iota_s(w)\) be the largest \(k\) such that **every** member of \(\Sigma^k\) embeds this way (with the empty pattern always covered). Let \(C_{q,s}(n,k)\) count length-\(n\) indexed words with \(\iota_s(w)=k\).

Define the formal rational generating functions

\[
I_q(z)=\sum_{j=0}^{q-1}(-1)^{q-1-j}\binom qj\frac1{1-jz},
\qquad
F_q(z)=\frac{q!z^q}{\prod_{j=1}^{q-1}(1-jz)},
\]

\[
T_{q,s}(z)=\sum_{r=0}^{s-2}(qz)^r+(qz)^{s-1}I_q(z),
\]

where the sum is empty for \(s=1\). Then, for every \(q\ge2\) and \(s\ge1\),

\[
\boxed{\displaystyle
\sum_{n,k\ge0}C_{q,s}(n,k)z^nu^k
=I_q(z)+\frac{uF_q(z)T_{q,s}(z)}{1-u(qz)^{s-1}F_q(z)}.}
\]

In particular, for binary words and every integer \(s\ge1\),

\[
\boxed{\displaystyle
\sum_{n,k\ge0}C_{2,s}(n,k)z^nu^k
=\frac{1+z+2uz^2\sum_{r=0}^{s-2}(2z)^r}
{1-z-2^su z^{s+1}}.}
\]

The shortest word that contains every \(s\)-spaced pattern of length \(k\ge1\) has length exactly

\[
\boxed{L_{q,s}(k)=qk+(s-1)(k-1).}
\]

Every shortest host is, uniquely, \(P_1B_1P_2B_2\cdots B_{k-1}P_k\), where each \(P_j\) is a permutation of the entire alphabet and each spacer \(B_j\) is an arbitrary word of length \(s-1\). Thus their exact labeled count is

\[
\boxed{(q!)^k q^{(s-1)(k-1)}.}
\]

The contribution assessed as new is the **uniform positive minimum-spacing** case \(s\ge2\), especially the complete two-variable spectrum. The \(s=1\) formulas are classical or previously recorded specializations and are not claimed as original.

## Assumptions and scope

The host word is linear (not circular), positions are indexed, alphabet symbols are labeled, and the embedding may depend on the target pattern. A spacing \(s\) is the difference of selected positions, so \(s=1\) is ordinary subsequence embedding, while \(s=2\) forbids consecutive chosen positions. There is no upper bound on the distance. The empty host has index zero. Both \(n\) and \(k\) are nonnegative; assertions about shortest hosts require \(k\ge1\).

## Proof

**1. A spacing-aware arch lemma.** Scan \(w\) from position \(1\) until the first prefix containing all of \(\Sigma\). If it exists, call it arch \(A_1\), ending at position \(e_1\). Resume at \(e_1+s\), skipping exactly \(s-1\) intervening positions, and again scan to the first occurrence of all symbols. Continue with endpoints \(e_1,e_2,\ldots\). Every completed arch contains all \(q\) symbols, and its final symbol is absent from the preceding portion of that arch. Let the number of completed arches be \(h\).

For any length-\(h\) pattern, its leftmost admissible greedy embedding places its \(j\)-th letter no later than \(e_j\), by induction: after a position no later than \(e_{j-1}\), the next letter can be chosen from the full-alphabet block beginning at \(e_{j-1}+s\). Thus every pattern of length at most \(h\) embeds.

Conversely, let \(c_j\) be the last symbol of arch \(A_j\). Because \(c_j\) occurs nowhere earlier within that arch, the greedy embedding of \(c_1\cdots c_h\) must select exactly \(e_1,\ldots,e_h\). The remaining eligible suffix beginning at \(e_h+s\) (or the whole word if \(h=0\)) omits some letter \(b\), since no further complete arch exists. Hence \(c_1\cdots c_hb\) has no admissible embedding. No longer pattern with that prefix embeds either. Therefore \(\iota_s(w)=h\), without any assumption that source letters are independent.

**2. Unique decomposition.** A word of index zero is precisely one that misses at least one alphabet letter. For a word with index \(k\ge1\), its greedy decomposition consists of \(k\) minimal all-letter arches; each pair of consecutive arches is separated by exactly \(s-1\) unrestricted letters. After the final arch, either fewer than \(s-1\) letters remain (an incomplete spacer), or there is a full spacer of \(s-1\) letters followed by a word that misses some alphabet symbol. These cases are disjoint and exhaust the possibilities, including the empty tail.

**3. The component generating functions.** By inclusion–exclusion, the number of length-\(r\) words missing at least one letter is \(\sum_{j=0}^{q-1}(-1)^{q-1-j}\binom qj j^r\); its ordinary generating function is \(I_q\). A minimal all-letter arch consists of \(q\) successive first appearances; when exactly \(j\) letters have appeared, any number of repeats of those \(j\) letters may precede the first appearance of a new letter, which has \(q-j\) choices. Multiplying these geometric stages gives

\[
F_q(z)=\prod_{j=0}^{q-1}\frac{(q-j)z}{1-jz}.
\]

A full spacer has generating function \((qz)^{s-1}\), while the permitted terminal fragment has generating function \(T_{q,s}\) as displayed. Hence the index-\(k\) generating function is \(F_q(z)^k(qz)^{(s-1)(k-1)}T_{q,s}(z)\) for \(k\ge1\), and \(I_q(z)\) for \(k=0\). Geometric summation over \(k\) gives the claimed identity.

**4. Sharp minimum and enumeration.** Each complete arch uses at least \(q\) positions, and consecutive arches require \(s-1\) separate skipped positions. Therefore \(|w|\ge qk+(s-1)(k-1)\). Equality forces every arch to have exactly \(q\) positions, thus to be a permutation, every spacer to have exactly \(s-1\) positions, and no terminal letters. Conversely, any such concatenation has at least \(k\) complete arches, so is universal, and its length precludes more than \(k\). Permutations and spacers are independent choices, yielding \((q!)^kq^{(s-1)(k-1)}\).

**5. Binary simplification.** Substituting \(I_2(z)=(1+z)/(1-z)\) and \(F_2(z)=2z^2/(1-z)\) into the general generating function and canceling its common factor yields the stated binary rational form. The algebra applies for all positive integer \(s\), with empty finite sums interpreted as zero.

## Verification

A standalone Python 3 verifier `verify.py` evaluates the coefficient formula by inclusion–exclusion and convolution, independently enumerates every host word in eight parameter ranges, and tests every candidate pattern by literal greedy matching. It checks every index distribution, all total word counts, and every available shortest-host coefficient. Actual execution returned

`VERIFY_OK independent_literal_hosts=127594 alphabets=2..4 spacing=1..4 exact_bivariate_coefficients=TRUE shortest_hosts=TRUE`.

The ranges are \((q,s,n_{\max})=(2,1,12),(2,2,13),(2,3,12),(2,4,11),(3,1,9),(3,2,9),(3,3,8),(4,2,7)\). This is finite corroboration; the argument for all parameters is the preceding symbolic proof.

## Relationship to prior work

The classical arch factorization and ordinary subsequence universality are developed in Fleischmann et al. [2]. The present argument adapts the greedy obstruction to a **fixed positive minimum distance between selected positions**, including all spacer/terminal configurations, and counts every attainable index. Day et al. [1] study general gap-constrained subsequence matching and universality, emphasizing fine-grained and computational hardness for richer constraints; their results do not state the uniform lower-spacing generating function or shortest-host enumeration here. Adamson et al. [3] count ordinary subsequence-universal words in regular languages without this minimum-gap constraint. Previously recorded unrestricted binary index distributions cover only \(s=1\). An upper bound on allowed embedding jumps for shortest ordinary universal words is not equivalent to the present lower-bound requirement: the admissible embedding families and optimal host lengths differ.

## Limitations

The theorem assumes one uniform lower distance \(s\); varying bounds by pattern position, symbol-sensitive conditions, and simultaneous upper bounds are not covered. It counts indexed words rather than cyclic or symmetry classes. Finite tests are not substitutes for the proof. Although targeted literature and mathematical-record comparisons identified no statement implying the \(s\ge2\) spectrum, an equivalent presentation under different terminology or a more general weighted-automaton enumeration may exist. No independent scientific audit is claimed.

## References

1. J. D. Day, M. Kosche, F. Manea, and M. L. Schmid, *Subsequences With Gap Constraints: Complexity Bounds for Matching and Analysis Problems*, arXiv:2206.13896 (first public 2022-06-28), https://arxiv.org/abs/2206.13896.
2. P. Fleischmann, M. Kosche, T. Koß, F. Manea, and S. Siemer, *The Edit Distance to k-Subsequence Universality*, arXiv:2007.09192 (2020), https://arxiv.org/abs/2007.09192.
3. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, and D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658 (2023), https://arxiv.org/abs/2311.10658.
