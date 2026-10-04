# Exact full-support insertion radius of subsequence universality
## Finding
Let \(\Sigma\) be a finite alphabet of size \(q\ge 2\). For \(k\ge 1\), call a word \(k\)-subsequence-universal when every word in \(\Sigma^k\) occurs in it as a subsequence. For a full-support word \(w\in\Sigma^n\), write \(I_k(w)\) for the minimum number of insertions required to reach a \(k\)-subsequence-universal supersequence.

For every \(n\ge q\),
\[
\max_{\substack{w\in\Sigma^n}{\operatorname{alph}(w)=\Sigma}} I_k(w)
=\max\{qk-n,(q-1)(k-1)\}.
\]
Thus the exact worst-case insertion distance has a phase transition at \(n=q+k-1\). If \(q\le n\le q+k-1\), the obstruction is the unavoidable target-length deficit and the radius is \(qk-n\). If \(n\ge q+k-1\), the radius stabilizes at \((q-1)(k-1)\).

For any ordering \(a_0,a_1,\ldots,a_{q-1}\) of the alphabet, the word
\[
w^\star=a_0^{\,n-q+1}a_1a_2\cdots a_{q-1}
\]
attains the maximum in every parameter range.

## Assumptions and scope
The alphabet is fixed and has \(q\ge2\) symbols; \(k\ge1\); and the starting word has length \(n\ge q\) and uses every symbol of \(\Sigma\). Only insertions are allowed, so the original word must remain as a subsequence of the target. The result concerns the maximum distance over the full-support length-\(n\) layer. It does not classify all maximizers, does not address words omitting alphabet symbols, and does not claim corresponding formulas for deletion or substitution distance.

For a contiguous block \(u\), let \(\operatorname{alph}(u)\) be its set of occurring symbols. Empty blocks are permitted and have empty alphabet.

## Proof
For a partition
\[
0=i_0\le i_1\le\cdots\le i_k=n,
\]
write \(w_j=w[i_{j-1}+1\mathbin{:}i_j]\), and define
\[
C_k(w)=\max_{0=i_0\le\cdots\le i_k=n}
\sum_{j=1}^k |\operatorname{alph}(w_j)|.
\]
We first establish the exact identity
\[
I_k(w)=qk-C_k(w). \tag{1}
\]
For the upper bound in (1), fix a partition attaining \(C_k(w)\). In block \(j\), insert one copy of each alphabet symbol absent from \(w_j\). The resulting \(j\)-th factor contains all \(q\) symbols. A concatenation of \(k\) full-support factors is \(k\)-subsequence-universal: for any requested word \(x_1x_2\cdots x_k\), choose \(x_j\) inside the \(j\)-th factor. The number of insertions is exactly \(qk-C_k(w)\).

For the reverse inequality, use the standard arch-factorization characterization of subsequence universality: a \(k\)-subsequence-universal word admits \(k\) consecutive factors, each containing all \(q\) alphabet symbols. Consider any universal supersequence of \(w\) obtained by insertions and such a factorization. The original symbols of \(w\), read in order, fall into \(k\) contiguous (possibly empty) blocks \(w_1,\ldots,w_k\). Factor \(j\) must contain at least \(q-|\operatorname{alph}(w_j)|\) inserted symbols, because every symbol missing from that original block must be supplied by an insertion in the factor. Summing gives at least \(qk-C_k(w)\) insertions. This proves (1).

It remains to minimize \(C_k(w)\) over full-support words. We claim that every such word satisfies
\[
C_k(w)\ge \min\{n,q+k-1\}. \tag{2}
\]
Start with the one-block partition, whose coverage is \(q\). Suppose the current partition has fewer than \(k\) blocks and total coverage is below \(n\). Then some block contains a repeated symbol: otherwise every block would have pairwise distinct letters and total coverage would equal the sum of block lengths, namely \(n\). Split a block between two occurrences of one repeated symbol. That symbol is then counted on both sides instead of once, so total coverage increases by at least one. Repeating this refinement, and adding empty blocks after all positions have become separated if necessary, yields (2).

Now take
\[
w^\star=a_0^{\,n-q+1}a_1a_2\cdots a_{q-1}.
\]
Across any \(k\)-block partition, each of \(a_1,\ldots,a_{q-1}\) occurs in exactly one block and therefore contributes exactly one to the total alphabet count. The symbol \(a_0\) can occur in at most \(\min\{k,n-q+1\}\) blocks. Hence
\[
C_k(w^\star)\le q-1+\min\{k,n-q+1\}=\min\{n,q+k-1\}.
\]
Together with (2), equality holds. Substitution into (1) gives
\[
I_k(w^\star)=qk-\min\{n,q+k-1\}
=\max\{qk-n,(q-1)(k-1)\}.
\]
Equation (2) and (1) give the same expression as an upper bound for every full-support \(w\), so the displayed value is the exact radius.

## Verification
The accompanying `verify.py` checks the theorem independently at three levels. First, on tiny instances it compares the partition formula with the literal definition by enumerating candidate supersequences and testing all length-\(k\) subsequences. Second, it exhaustively evaluates every full-support word for \(q\in\{2,3,4\}\) over parameter ranges up to \(n=9\) and verifies both the radius and the objectwise coverage lemma. Third, it checks the proposed extremal family over a larger grid through \(q=12\), \(n=q+17\), and \(k=12\). The replay output is:

`VERIFY_OK literal_cases=240 exhaustive_parameter_cases=69 full_support_words_checked=20644 witness_grid_cases=2376`

These finite checks corroborate the implementation and boundary cases; the all-parameter conclusion rests on the proof above, not on extrapolation.

## Relationship to prior work
Fleischmann, Kosche, Koß, Manea, Siemer, and collaborators introduced and analyzed the edit distance to \(k\)-subsequence universality. Their open STACS treatment gives polynomial-time algorithms for minimum insertion distance and, in its insertion-only section, a dynamic program whose segment cost is the number of missing alphabet symbols. That per-word optimization is the closest prior result inspected. The present statement instead solves the extremal optimization over every full-support word of a fixed length, with a closed form, an explicit extremal family, and a sharp transition between length and support-distribution obstructions.

The earliest public version located is arXiv:2007.09192, first posted on 2020-07-17. The open conference version is DOI:10.4230/LIPIcs.STACS.2021.25. A later journal version is DOI:10.1016/j.jcss.2025.103681. Exact-formula and alias searches for an insertion radius, covering-radius formulation, and the two closed-form terms did not locate a published statement equivalent to the theorem. An unindexed or differently phrased prior derivation remains possible.

## Limitations
The theorem is restricted to insertion distance and to starting words that use the full ambient alphabet. It gives one extremal family but not a classification of all extremizers. The verification program covers only finite parameter ranges and is supporting evidence rather than an infinite proof. The literature comparison cannot exclude inaccessible, unindexed, or differently phrased prior work.

## References
1. Pamela Fleischmann, Maria Kosche, Tore Koß, Florin Manea, Stefan Siemer, et al., *The Edit Distance to k-Subsequence Universality*, arXiv:2007.09192, first public version 2020-07-17.
2. Pamela Fleischmann, Maria Kosche, Tore Koß, Florin Manea, Stefan Siemer, et al., *The Edit Distance to k-Subsequence Universality*, STACS 2021, DOI:10.4230/LIPIcs.STACS.2021.25.
3. Later journal version: DOI:10.1016/j.jcss.2025.103681.
