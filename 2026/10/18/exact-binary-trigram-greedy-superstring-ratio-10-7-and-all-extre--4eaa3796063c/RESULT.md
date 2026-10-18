# Exact binary trigram greedy-superstring ratio \(10/7\) and all extremizers

## Finding

Let \(\Sigma=\{0,1\}\), and let \(S\) range over all nonempty subsets of \(\Sigma^3\); input words are distinct and have length exactly three. The maximum-overlap greedy shortest-common-superstring algorithm repeatedly chooses any **ordered** pair of remaining words realizing the largest suffix-prefix overlap, merges the pair and continues until one word remains. Ties are unrestricted; a zero-overlap pair is allowed. A complete shorter-word suffix-prefix overlap is permitted. Let \(G(S)\) be the largest terminal length among all tie-breaking sequences and let \(O(S)\) be the shortest possible length of a common superstring.

The sharp fixed-binary, fixed-length approximation ratio is

\[
\max_{\varnothing\ne S\subseteq\{0,1\}^3}\frac{G(S)}{O(S)}=\frac{10}{7}.
\]

Exactly four input sets attain equality:

```
{000,001,010,011,100}
{000,001,010,100,110}
{001,011,101,110,111}
{011,100,101,110,111}
```

These form one orbit under reversal of all input words and simultaneous exchange of symbols 0 and 1. More finely, when \(|S|=t\), the exact maxima for \(t=1,2,\ldots,8\) are respectively

\[
1,\ 1,\ \frac75,\ \frac43,\ \frac{10}7,\ \frac{11}8,\ \frac43,\ \frac75.
\]

## Assumptions and scope

The alphabet is exactly binary and inputs are sets of distinct three-character words. A suffix-prefix overlap of \(a\) and \(b\) is any integer \(h\) between zero and \(\min\{|a|,|b|\}\) for which the last \(h\) symbols of \(a\) equal the first \(h\) of \(b\). Their greedy merge is \(a\) followed by \(b\) with the overlapped prefix omitted. The algorithm chooses an ordered pair whose overlap is maximum over all distinct active indices. The theorem concerns the worst permitted choice among all ties, not a particular deterministic tie rule. It neither asserts the same ratio for longer input words nor for alphabets with more than two symbols.

## Proof

A finite exhaustive certificate is given in `verify.py`; its finite loops and recurrence provide a complete proof rather than statistical tests.

**Optimal lengths.** Encode each of the eight binary trigrams by a bit in a coverage mask. Enumerate *all* binary words of lengths \(3,4,\ldots,10\). For each such word, form the bit mask of its contiguous trigrams and update the shortest containing length for every nonzero submask. This searches exactly \(\sum_{j=3}^{10}2^j=2040\) binary candidate words. The word `0001011100` contains all eight binary trigrams, so every possible input set admits a common superstring of length at most ten. Consequently this finite enumeration determines \(O(S)\) exactly for every one of the \(2^8-1=255\) input sets. Independently, an overlap-graph Hamiltonian-path dynamic program obtains the same optimum in every case.

**All greedy tie sequences.** For a sorted multiset \(Q\) of currently active words, set \(F(Q)=|a|\) when \(Q\) contains only \(a\). Otherwise compute \(h=\max_{i\ne j}\operatorname{ov}(Q_i,Q_j)\), and set

\[
F(Q)=\max_{\substack{i\ne j\\ \operatorname{ov}(Q_i,Q_j)=h}}
F\bigl(\operatorname{sort}((Q\setminus\{Q_i,Q_j\})\uplus\{Q_i\cdot Q_j[h:]\})\bigr).
\]

The indices are distinct even if two active words have identical contents. Each recursion reduces the number of active words by one. It therefore terminates, and induction on the number of active words shows that \(F(Q)\) is **exactly** the worst terminal length across every legal greedy tie-breaking sequence. Memoizing the resulting finite recursion yields 7405 distinct active states across all nonempty initial masks; the complete recurrence is implemented without pruning or approximations in `verify.py`.

For each of the 255 sets, divide the resulting exact \(F(S)\) by the independently enumerated exact \(O(S)\), compare these fractions by exact rational arithmetic, and retain all maximizers. The checker asserts the displayed length ratios, the four extremal sets, their common orbit, and the entire cardinality-refined sequence. Thus no unexamined binary trigram input or legal tie-breaking branch remains.

**Explicit sharpness witness.** For \(S=\{000,001,010,011,100\}\), the word `0100011` contains all inputs and has length seven. This is optimal by the complete shortest-superstring enumeration. A legal greedy sequence is

```
001 + 010      overlap 2 -> 0010
100 + 0010     overlap 2 -> 10010
10010 + 011    overlap 1 -> 1001011
000 + 1001011  overlap 0 -> 0001001011
```

At each step the indicated overlap is globally maximal among active ordered pairs. The resulting word has length ten, proving the lower bound independently of the full ratio table. 

## Verification

From a directory containing the included `verify.py`, run `python3 verify.py` using Python 3 and no nonstandard dependencies. The included `verification_output.txt` records a completed exact run with 255 input sets, 7405 memoized greedy states, four extremizers, and the predicted ratio and cardinality profile. The checker includes an independent Hamiltonian-path dynamic-programming comparison for every optimal length. The computation is exhaustive for the declared finite domain; it makes no claim about other alphabets, lengths, or input models.

## Relationship to prior work

Chukhin, Kulikov, Mihajlin and Smal (arXiv:2608.20018, first public August 20, 2026) prove that the worst approximation ratio over all alphabets for words of length three is \(9/5\). Their unrestricted-alphabet bound implies only the nonsharp upper bound \(9/5\) for the binary subproblem; it does not, on its own, imply the sharp binary value \(10/7\) or identify its four extremizers. Nikolaev (arXiv:2407.20422) studies strengthened locally greedy and per-symbol metrics. Kalugin and Nikolaev (SOSA 2024) establish a general compression guarantee, not this exact binary length-three spectrum. No novelty is claimed for greedy superstring algorithms, overlap dynamic programming, or exhaustive finite-state enumeration techniques themselves.

## Limitations

The certified scope is the 255 nonempty subsets of the eight distinct binary trigrams. It does not quantify alphabet-size-three behavior or worst cases at longer lengths. The 2026 length-three preprint was available through its abstract and public technical descriptions, not full text; overlapping appendix or unindexed prior calculations remain an originality risk. Results are reproducible finite calculations, not independent external validation.

## References

1. N. Chukhin, A. S. Kulikov, I. Mihajlin and A. Smal, *The Greedy Superstring Algorithm Achieves Ratio 2 for Strings of Length 6 Already*, arXiv:2608.20018 (first submitted August 20, 2026), https://arxiv.org/abs/2608.20018.
2. M. Nikolaev, *Greedy Conjecture for the Shortest Common Superstring Problem and its Strengthenings*, arXiv:2407.20422 (2024), https://arxiv.org/abs/2407.20422.
3. P. E. Kalugin and M. S. Nikolaev, *The greedy algorithm for the Shortest Common Superstring problem is a 1/2-approximation in terms of compression: a simple proof*, SOSA 2024, https://doi.org/10.1137/1.9781611977936.9.
