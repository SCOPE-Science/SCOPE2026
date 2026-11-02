# Exact ternary length-five palindromic covers: 66 cyclic and 68 linear

## Finding

The length-five ternary instance is a natural first step beyond documented binary palindrome-superstring minima: a length-five palindrome is determined by its first three symbols, giving a complete, non-arbitrarily-selected family of \(27\) targets. Let the alphabet be \(\Sigma=\{0,1,2\}\) and let \(\mathcal P=\{abcba:a,b,c\in\Sigma\}\), containing \(27\) distinct length-five ordinary palindromes. The shortest **cyclic** word whose length-five cyclic factors include every member of \(\mathcal P\) has length exactly \(66\). The shortest **linear** word whose ordinary contiguous factors include every member has length exactly \(68\). Repetitions of required palindromes and other factors are allowed in the optimization; both exhibited optima happen to contain every required palindrome exactly once. Thus permitting cyclic boundary reads saves exactly two letters in this instance.

Explicit optimal cyclic representative (linear spelling, interpreted circularly):

```text
000001000121012021201020101011101111121112121222122222022202020002
```

Explicit optimal linear word:

```text
22122211121111101110001000002000202021202121210121010102010222022222
```

## Assumptions and scope

The alphabet has exactly three distinct symbols. A palindrome is a contiguous word equal to its reversal, not a reverse-complement palindrome or a scattered subsequence. A cyclic word of length \(N\) has \(N\) length-five windows, starting at every cyclic position and wrapping at the end. A linear word of length \(N\) has \(N-4\) ordinary length-five windows. A covering word need not have exactly one occurrence of a target. All lengths refer to numbers of alphabet symbols, not numbers of required factors.

## Proof

**1. Reduction to a directed Hamiltonian tour.** Enumerate \(\mathcal P\) lexicographically as \(p_0,\ldots,p_{26}\). For distinct patterns \(p_i,p_j\), define

\[
c_{ij}=5-\max\bigl(\{h\in\{1,2,3,4\}:\operatorname{suffix}_h(p_i)=\operatorname{prefix}_h(p_j)\}\cup\{0\}\bigr).
\]

Thus \(c_{ij}\) is a positive integer between \(1\) and \(5\), equal to the minimum positive shift placing \(p_j\) after \(p_i\) without a contradiction on their overlapping positions.

A cyclic covering word must have at least \(27\) positions, because it must supply \(27\) distinct length-five windows, so cyclic window semantics never require a word shorter than five. Take any cyclic covering word, and select **one** occurrence of each of the \(27\) required palindromes. Their distinct start positions have a cyclic order \(i_0,\ldots,i_{26}\). Let \(\delta_r\) be the clockwise gap between consecutive starts. If \(\delta_r<5\), the two selected windows overlap, forcing the suffix-prefix match and hence \(\delta_r\ge c_{i_r,i_{r+1}}\). If \(\delta_r\ge5\), the inequality holds because \(c_{ij}\le5\). Summing over all consecutive pairs (including the wraparound pair) gives

\[
N=\sum_r\delta_r\ge\sum_r c_{i_r,i_{r+1}}.
\]

Hence every cyclic cover is bounded below by the minimum cost of a directed Hamiltonian cycle through these \(27\) pattern vertices. This argument remains valid when the covering word contains extra copies of target factors.

For the **linear** case, every covering word necessarily has at least \(31\) positions because it supplies \(27\) distinct length-five windows. Order one chosen occurrence of each target by increasing start. Add one dummy vertex \(\star\); assign \(c_{\star j}=5\) and \(c_{i\star}=0\), and retain the overlap costs for distinct pattern vertices. A Hamiltonian cycle \(\star,i_0,\ldots,i_{26},\star\) has cost \(5+\sum_{r=0}^{25}c_{i_r,i_{r+1}}\). The chosen starts and the final five-letter window show that the linear source length is at least that tour cost.

**2. Exact degree-and-cut lower-bound certificates.** The accompanying machine-readable file `certificates.json` supplies, separately for cyclic and linear cases, half-integer rational degree potentials \(\alpha_i=\texttt{alpha2[i]}/2\), \(\beta_j=\texttt{beta2[j]}/2\), and nonnegative cut weights \(\gamma_S=\texttt{weight2}/2\) on explicitly listed nonempty proper vertex subsets \(S\). For **every** arc with distinct endpoints, the certificate satisfies

\[
\alpha_i+\beta_j+\sum_{S:\,i\in S,\,j\notin S}\gamma_S\le c_{ij}.
\]

Any directed Hamiltonian cycle uses exactly one arc leaving each vertex, exactly one entering each vertex, and at least one arc leaving every nonempty proper subset \(S\). Summing the preceding verified inequalities over its edges yields

\[
\operatorname{tour\ cost}\ge \sum_i\alpha_i+\sum_j\beta_j+\sum_S\gamma_S.
\]

The exact certificate totals are \(66\) for the cyclic \(27\)-vertex graph and \(68\) for the linear \(28\)-vertex dummy-augmented graph. The standalone `verify.py` checks each of all \(702\), respectively \(756\), distinct-endpoint arc inequalities by exact doubled-integer arithmetic; it also checks that the weights sum to the stated bounds. These provide universal lower bounds, not numerical solver estimates or merely finite observations of short words.

**3. Optimal constructions.** The same certificate supplies a permutation `order` of the \(27\) pattern indices for each case. Place consecutive target patterns at the minimum compatible shifts \(c_{ij}\). For the cyclic case close the last pattern to the first with its overlap shift; for the linear case terminate after the final five-letter pattern. The program checks all overlap equations, every symbol position, and the presence of all \(27\) length-five palindromes. The constructed lengths are \(66\) cyclic and \(68\) linear, meeting the two lower bounds.

This proves both exact minima and their two-symbol difference.

## Verification

`certificates.json` and `verify.py` form a standalone, standard-library Python 3 proof checker. Put them in one directory and run:

```sh
python3 verify.py
```

The checker derives all target palindromes from the alphabet, reconstructs both weighted complete directed graphs, verifies every degree-and-cut dual inequality and objective sum using only integer operations, checks the pattern orders, constructs the exact source words, checks overlap consistency, and checks that every required palindrome occurs. Expected final line: `VERIFICATION_OK`. The certified arc counts are \(27\cdot26=702\) and \(28\cdot27=756\); there are \(10\) and \(12\) positive cut weights respectively. No external solver, library, or precomputed optimality assertion is required to validate these finite certificates.

## Relationship to prior work

Chen, Kitaev, and Sun (2019), *On the probability of existence of a universal cycle or a universal word for a set of words*, study exact-once universal cycles and words under deletions from all words of a fixed length. Their principally two-deleted-word results do not give the optimization for the \(27\)-element ternary palindrome subset here. OEIS A330022 records shortest **binary linear** superstrings of all fixed-length ordinary palindromes, including a standard overlap-Hamiltonian-path formulation; it does not supply these ternary cyclic or linear values. Simpson (2014), *Palindromes in circular words*, bounds the number of distinct palindromes in a circular word across lengths, not the minimum length to contain all palindromes of one fixed length over a ternary alphabet. General shortest-common-superstring approximation results address arbitrary collections but do not establish these numerical optima.

## Limitations

These are exact **finite** results for a three-letter alphabet and targets of length five. They make no assertion about other alphabet sizes, other palindrome lengths, optimal-cover counts, or structural rigidity of **all** minimizers. The dual weights are finite exact arithmetic certificates whose mathematical soundness rests on the explicitly proved degree-and-cut argument; the reader can independently check every inequality. General superstring theory or unindexed tables might contain an equivalent finite instance, so literature novelty should be understood relative to the sources listed, not as an assertion that no equivalent statement could exist.

## References

1. H. Z. Q. Chen, S. Kitaev, B. Y. Sun, *On the probability of existence of a universal cycle or a universal word for a set of words*, arXiv:1908.01116, first posted 2019-08-03. https://arxiv.org/abs/1908.01116
2. J. Shallit and subsequent OEIS contributors, OEIS A330022, *Length of shortest binary string containing all palindromes of length n as substrings*, created 2019-11-27. https://oeis.org/A330022
3. J. Simpson, *Palindromes in circular words*, Theoretical Computer Science 550 (2014), 66–78. https://doi.org/10.1016/j.tcs.2014.07.012
4. S.-H. Teng and F. F. Yao, *Approximating Shortest Superstrings*, SIAM Journal on Computing 26 (1997), 410–417. https://doi.org/10.1137/S0097539794286125
