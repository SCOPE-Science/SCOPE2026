# Rank-max amalgamation and linear-time forbidden-subsequence minimal supersequences

## Finding

Let \(\Sigma\) be any finite alphabet, let \(P=p_1\cdots p_r\in\Sigma^r\) be nonempty, and let \(W_1,\ldots,W_k\in\Sigma^*\) with \(k\ge1\). Write \(X\preceq Y\) when \(X\) is an order-preserving, not necessarily contiguous subsequence of \(Y\), and define
\[
\rho_P(X)=\max\{t\in\{0,\ldots,r\}:p_1\cdots p_t\preceq X\}.
\]
Then the **rank-max amalgamation identity** is
\[
\boxed{\min_{S:\,W_i\preceq S\ (1\le i\le k)}\rho_P(S)=\max_{1\le i\le k}\rho_P(W_i).}
\]
In particular, a \(P\)-avoiding inclusion-minimal common supersequence exists **if and only if** every input word avoids \(P\). Put \(N=\sum_i(|W_i|+1)\), counting one delimiter per input word (including empty words). Feasibility and a \(P\)-avoiding common supersequence of length at most \(N\) can be obtained in \(O(N+r)\) time; an inclusion-minimal one can be obtained in \(O(kN+r)\) time and \(O(N+r)\) space. For two inputs these are linear-time and linear-space bounds.

## Assumptions and scope

The forbidden pattern is a single **nonempty** word and avoidance is of **scattered subsequences**, not consecutive factors. Empty input words and arbitrary repeated symbols are allowed. Alphabet size is not assumed constant; equal-symbol comparisons and input-symbol storage use the ordinary unit-cost alphabet model. An inclusion-minimal common supersequence means a common supersequence from which no position can be deleted while still containing all inputs; it is not required to have globally minimum length.

## Proof

**1. Rank is monotone.** If \(X\preceq Y\), then \(\rho_P(X)\le\rho_P(Y)\), by transitivity of the subsequence relation. Hence every common supersequence has rank at least \(T=\max_i\rho_P(W_i)\). When \(T=r\), concatenating all input words attains rank \(r\), establishing the identity but making avoidance impossible. Assume henceforth \(T<r\).

**2. Greedy phase decomposition.** Greedily scan each \(W_i\) against successive symbols of \(P\). With \(t_i=\rho_P(W_i)\), the scan partitions the word uniquely into
\[
W_i=U_{i,0}p_1 U_{i,1}p_2\cdots p_{t_i}U_{i,t_i},
\]
where \(U_{i,j}\) has no occurrence of the single symbol \(p_{j+1}\), for \(0\le j\le t_i<r\). Put \(U_{i,j}=\varepsilon\) for \(j>t_i\), with \(\varepsilon\) the empty word. For each phase \(j\), concatenate the \(U_{i,j}\) over all inputs in input order to form \(V_j\), and define
\[
S=V_0p_1V_1p_2\cdots p_TV_T.
\]
For each input \(W_i\), its blocks \(U_{i,0},\ldots,U_{i,t_i}\) occur in order in these same phases and its marked occurrences \(p_1,\ldots,p_{t_i}\) can all use the corresponding single shared occurrences in \(S\). Thus \(W_i\preceq S\). Before the displayed \(p_{j+1}\), all letters in \(V_j\) are different from \(p_{j+1}\), since each contributing block has that property. The greedy matcher of \(P\) in \(S\) therefore advances exactly once at each displayed marked symbol, and does not advance within a \(V_j\). It finishes at rank precisely \(T<r\). Hence \(P\not\preceq S\), proving the identity and the feasibility criterion. The construction shares marked occurrences across inputs, so \(|S|\le\sum_i|W_i|\le N\).

**3. Linear-time phase amalgamation.** Greedily scan the inputs once, appending each unmarked symbol to its current phase bucket and advancing the bucket number only when the next pattern symbol is encountered. Emit buckets in increasing phase order, inserting one copy of \(p_{j+1}\) between consecutive buckets. All bucket operations and emissions take \(O(N+r)\) time and \(O(N+r)\) storage. If any input reaches rank \(r\), report impossibility. No optimization over all possible interleavings is needed.

**4. Inclusion-minimal reduction.** Let \(S\) be the constructed common supersequence, of length \(L\le N\). For each \(W_i\), compute its **rightmost embedding** positions \(R_i(0),\ldots,R_i(|W_i|-1)\) in \(S\) by scanning \(S\) backward. During a left-to-right scan of \(S\), maintain the already-retained prefix \(K\), and let \(q_i\) be the length of the longest prefix of \(W_i\) greedily embedded in \(K\). At position \(h\) (zero-based), delete \(S[h]\) exactly if for every input either \(q_i=|W_i|\) or \(R_i(q_i)>h\). The condition is equivalent to all \(W_i\) embedding in \(K S[h+1:]\): greedy embedding of \(K\) maximizes the input prefix already matched, and the rightmost embedding tests whether the remaining suffix embeds strictly after \(h\). Consequently each deletion preserves all inputs. If a position is retained, deleting it already made some input impossible at that moment even with the entire unprocessed suffix; subsequent deletions cannot restore an embedding. Every retained position is therefore essential in the final word, which is an inclusion-minimal common supersequence. Finally, subsequence deletion cannot introduce \(P\), so avoidance is preserved. Computing all rightmost embeddings costs \(O(kL+N)\) time, and the sweep costs \(O(kL)\), giving \(O(kN+r)\) overall and \(O(N+r)\) space.

**5. Why a shortest-supersequence shortcut fails.** For every integer \(m\ge2\), take \(A=0^m1\), \(B=10^m\), \(P=11\). The unconstrained shortest common supersequence \(10^m1\) has length \(m+2\), but any avoiding supersequence may use only one \(1\), forcing at least \(m\) zeros on each side of it. The unique inclusion-minimal avoiding supersequence is \(0^m10^m\), of length \(2m+1\). Thus an arbitrary shortest common supersequence need not solve the constrained problem.

## Verification

The accompanying standard-library script `checker.py` implements the phase amalgamation and the rightmost-embedding reduction, together with a slower deletion-based reference method. Exhaustive binary two-string tests cover \(3150\) combinations with each input length at most \(3\) and pattern length at most \(3\); existence is compared against enumeration of all words through the sum of input lengths. Another \(39200\) exhaustive tests cover up to four binary inputs of length at most \(2\); a further \(2000\) seeded quaternary tests check longer inputs. The output is in `tests_output.txt`. These are finite corroborations, not proofs of the unrestricted theorem; the proof is the phase decomposition and deletion argument above.

## Relationship to prior work

Sopp, Liyanage, Gong and Zhu (2026), Section 7, explicitly pose the question whether an inclusion-minimal common supersequence can be found while avoiding a given subsequence \(P\). Their Sections 4 and 6 give unconstrained minimization algorithms, but the inspected work does not supply the feasibility criterion or rank-max amalgamation. The present argument answers that precise single-forbidden-pattern question and constructs the witness without enumerating minimal supersequences. Dondi's (2013) constrained *shortest* common supersequence concerns bounds on **symbol occurrence counts**, not avoidance of a scattered forbidden word. McDevitt and Ruškuc (2021) examine joint embedding for avoidance under **consecutive** subword containment, a different order from scattered-subsequence containment.

## Limitations

This theorem permits exactly one forbidden scattered-subsequence pattern; it does not assert that a family of multiple forbidden patterns has the same property. It constructs inclusion-minimal, not globally shortest-length, common supersequences. The originality comparison is limited to the directly inspected primary source, relevant literature abstracts/metadata, and targeted literature checks; unindexed or unexamined literature might contain an equivalent amalgamation statement. Independent validation is not claimed.

## References

1. Braeden Sopp, Adiesha Liyanage, Mingyang Gong, and Binhai Zhu, *Computing and Enumerating Minimal Common Supersequences Between Two Strings*, arXiv:2603.22591v1, first posted 2026-03-23. https://arxiv.org/html/2603.22591v1 (especially §§4, 6–7).
2. Riccardo Dondi, *The constrained shortest common supersequence problem*, Journal of Discrete Algorithms **21** (2013), 11–17. DOI: 10.1016/j.jda.2013.03.004.
3. Matthew McDevitt and Nik Ruškuc, *Atomicity and Well Quasi-Order for Consecutive Orderings on Words and Permutations*, SIAM Journal on Discrete Mathematics **35** (2021), 495–520. DOI: 10.1137/20M1338411.
