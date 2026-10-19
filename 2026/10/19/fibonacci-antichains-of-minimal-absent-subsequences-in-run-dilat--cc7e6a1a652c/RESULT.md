# Fibonacci antichains of minimal absent subsequences in run-dilated binary words

## Finding

Let \(r\ge 2\), and let \(w=b_1^{\ell_1}\cdots b_r^{\ell_r}\) be a binary word, where successive symbols alternate and every run length satisfies \(\ell_j\ge 2\). A **minimal absent subsequence** (MAS) is a binary word that is not a scattered subsequence of \(w\), although every proper scattered subsequence is. Write \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\).

**Theorem.** For every choice of the run lengths, the number of distinct MAS is exactly
\[
|\operatorname{MAS}(w)|=F_{r+2}.
\]
More precisely, exactly \(F_r\) members of \(\operatorname{MAS}(w)\) end in the symbol of the last run, and exactly \(F_{r+1}\) end in the other symbol. Thus inserting further copies into any existing run (while each run remains of length at least two) preserves both counts. The first values for \(r=2,3,4,5,6,7\) are \(3,5,8,13,21,34\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). The word has \(r\ge2\) maximal alternating constant-symbol runs, all of length at least two. There is no restriction on the relative magnitudes of the run lengths; neither equality nor boundedness is assumed. Subsequence means position-preserving **scattered** subsequence, not contiguous factor. Different MAS are counted as distinct words, not as distinct embeddings.

Write \(L_j\) and \(R_j\) for the first and last 1-based positions of run \(j\), with \(R_0=0\). Thus \(L_j=R_{j-1}+1\). A prefix of a candidate MAS is greedily embedded at its earliest possible positions.

## Proof

**1. Exact characterization of admissible paths.** The greedy-embedding criterion of Kosche, Koß, Manea and Siemer (Theorem 3.1 of *Absent Subsequences in Words*) states the following. Let \(u=u_1\cdots u_{m+1}\) and greedily embed its first \(m\) letters at positions \(0=p_0<p_1<\cdots<p_m\le |w|\). Then \(u\) is an MAS precisely when \(u_{m+1}\) does not occur after \(p_m\), while each \(u_k\) with \(2\le k\le m+1\) occurs in the interval of source positions \((p_{k-2},p_{k-1}]\). Greediness itself rules out intervening occurrences of \(u_k\) between \(p_{k-1}\) and \(p_k\).

The criterion can be checked directly: for any deletion of \(u_k\), the subsequent letters can be shifted one greedy block to the left by using the required occurrence in \((p_{k-2},p_{k-1}]\); conversely, minimality of \(u\) forces these occurrences. This is a known criterion, used here as a starting lemma, not claimed as new.

Construct an acyclic path count on pairs \((a,p)\), where \(a\) is the penultimate and \(p\) the last greedy source position of a prefix of an MAS; use \(a=0\) for a one-letter prefix. Such a pair can be extended by a symbol \(c\) exactly when \(c\) appears somewhere in \((a,p]\). If there is a next occurrence of \(c\) after \(p\), continue to \((p,\operatorname{next}(p,c))\). Otherwise, terminate and output an MAS ending in \(c\). Each edge is letter-labeled and each prefix determines its greedy positions uniquely. Thus the number of accepting paths equals the number of **distinct words** in the MAS set, without overcounting embeddings.

**2. Classification of all nonterminal states.** Initially the two possible one-letter prefixes reach \((0,L_1)\) and \((0,L_2)\), each once. In the first two runs, every interior position \(p>L_j\) is reached only in state \((p-1,p)\), with multiplicity one.

For run \(j\ge3\), induction on the pairs shows that precisely the following states have nonzero multiplicity:

* A state \((R_{j-2},L_j)\) of multiplicity \(F_{j-2}\).
* A state \((L_{j-1},L_j)\) of multiplicity \(F_{j-1}\).
* For every \(L_j<p\le R_j\), a state \((p-1,p)\) of multiplicity \(F_j\).

Here is the full transition check. From an interior state, the interval \((a,p]\) contains only the symbol of its run. It moves one position to the right inside the same run; if \(p=R_j\), its next permitted occurrence is \(L_{j+2}\). Hence the first state of run \(j+2\) receives \(F_j\) paths from \(R_j\). From either first-position state of run \(j\ge3\), the interval \((a,L_j]\) contains both symbols: the preceding run has a surviving position in that interval because its length is at least two. It therefore allows one transition to \(L_j+1\) and one to \(L_{j+1}\). The latter receives the sum \(F_{j-2}+F_{j-1}=F_j\), while the former, and all subsequent interior positions of the current run, receive the same sum. The special first-position state of run \(2\), \((0,L_2)\), also has both symbols in its interval, giving the base \(F_1=F_2=1\) and \(F_3=2\). The first-position state of run \(1\) has only its own symbol, as required. These cases exhaust all available next occurrences, proving the state classification for arbitrary run lengths.

**3. Count the terminal edges.** For \(r\ge3\), a terminating edge ending in the last run's symbol can arise only at \(p=R_r\), with multiplicity \(F_r\). A terminating edge ending in the other symbol can arise only at \(p=R_{r-1}\) (multiplicity \(F_{r-1}\)) or at \(p=L_r\) (the two first-position states with combined multiplicity \(F_r\)). In the latter case that other symbol is present in \((a,L_r]\) by the two-letter-run hypothesis, but absent from the suffix after \(L_r\). At other interior positions of the last run, that other symbol is not present in the permitted interval; at earlier runs both symbols reappear later. The total for the other symbol is therefore \(F_{r-1}+F_r=F_{r+1}\).

For \(r=2\), the three terminal paths are the constant-zero, constant-one, and reverse-run-order words, in the appropriate binary labeling; one ends in the last-run letter and two in the opposite letter, agreeing with \(F_2=1\) and \(F_3=2\). Finally \(F_r+F_{r+1}=F_{r+2}\). This proves the theorem. \(\square\)

## Verification

The accompanying standalone `verify_mas_fibonacci.py` compares two independently implemented constructions: explicit generation of all distinct subsequences followed by the deletion-minimality test, and the greedy pair-state dynamic program. Every length tuple in \(\{2,3\}^r\) for \(2\le r\le6\) is tested by both constructions (124 cases), including counts grouped by final symbol and bit-complement symmetry. Twenty-four further nonuniform cases with up to 25 runs, and individual run lengths between 2 and 14, verify the exact state-count formula using dynamic programming without brute-force enumeration. These tests corroborate the proof but do not replace its arbitrary-parameter induction.

Run `python3 verify_mas_fibonacci.py` from the directory containing the file. Expected final line: `ALL_FIBONACCI_RUN_MAS_CHECKS_PASSED independent_direct_cases 124 nonuniform_large_run_cases 24`.

## Relationship to prior work

Kosche, Koß, Manea and Siemer (arXiv:2108.13968, original public preprint 31 August 2021) supply the **general** greedy criterion and enumeration framework for MAS, including the two-run example \(0011\). Those are reused rather than claimed as new. The present theorem is the explicit arbitrary-run-length Fibonacci count and exact terminal-letter split for every binary word with all run lengths at least two; the inspected general characterization and examples do not state this specialization. Adamson and collaborators (arXiv:2407.18599) count absent subsequences of prescribed length under universality-index constraints, not the minimal absent antichain of a prescribed run structure. The later algorithmic enumeration paper arXiv:2504.21471 likewise addresses general enumeration complexity rather than this run-invariant formula. A known exact MAS length spectrum for \((01)^k\) concerns *single-letter runs* and does not imply the present theorem.

## Limitations

The proof uses both the binary alphabet and the condition that every run contains at least two letters; it does **not** claim the same formula when one-letter runs are allowed, for larger alphabets, or for contiguous minimal absent factors. A general greedy criterion from prior literature is essential to the proof. The result classifies **counts and terminal-letter counts**, not the complete length-resolved MAS spectrum. Published-index comparisons cannot establish uniqueness; an equivalent run-specific formula in unindexed literature remains possible. No independent audit has been performed.

## References

1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, first version 2021-08-31, Theorem 3.1 and Example 3.3. https://arxiv.org/abs/2108.13968
2. D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599, first version 2024-07-26. https://arxiv.org/abs/2407.18599
3. F. Manea, T. Ringleb, S. Siemer, M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471. https://arxiv.org/abs/2504.21471
