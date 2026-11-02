# Palindromic three-subsequence covers: exact DNA-alphabet census and a general pairwise criterion

## Finding

Let \(\Sigma_q=\{0,1,\ldots,q-1\}\) be a **labeled** alphabet of size \(q\ge1\). A scattered subsequence preserves order, but need not use adjacent positions. A word is *palindromic-three-covering* if it contains every \(aba\), for all ordered choices \(a,b\in\Sigma_q\), as a scattered subsequence (including the constants \(aaa\)).

**Theorem.** The shortest possible covering length is exactly \(3q\). Every shortest cover has three occurrences of every letter. For any such word, covering is equivalent to the following pairwise-projection condition: for every distinct \(a,b\), erasing the other letters yields a six-letter word containing three copies of each, **not** equal to any of

`aaabbb`, `aabbba`, `abbbaa`, `baaabb`, `bbaaab`, `bbbaaa`.

The number \(N_q\) of distinct indexed shortest covers can be calculated exactly by the finite recurrence below. Its first five values are

\[
(N_1,N_2,N_3,N_4,N_5)=(1,14,690,80016,17825160).
\]

In particular, over a four-symbol alphabet, **exactly \(80016\)** of the \(369600\) length-12 three-of-each-letter words cover all sixteen ordered palindromic length-three subsequences. Under arbitrary permutation of the four letter names these are \(3334\) inequivalent covers. This contrasts with the \(4!^3=13824\) length-12 words covering *every* ordered three-letter subsequence; palindromic-only coverage permits \(1667/288\) times as many shortest words.

## Assumptions and scope

Words are linear and positions are distinguished; reversal is not identified. The alphabet labels are distinct. In \(aba\) the endpoints are equal while the middle letter may equal them. The subsequence relation is existential, not multiplicity preserving. Enumeration counts source words, not distinct observations or cyclic classes. The full-alphabet recurrence holds for arbitrary positive integer \(q\); the displayed evaluations are for \(q\le5\). The four-letter case is natural for DNA-sequence motifs, but the claim is purely combinatorial and makes no biological performance assertion.

## Proof

**Minimal length.** Every covering word contains \(aaa\) for each \(a\), so has at least three copies of every letter and length at least \(3q\). For any permutation \(P\) of all \(q\) letters, the word \(PPP\) contains every \(aba\): if \(a=b\), use its copies from the three blocks, and if \(a\ne b\), use \(a\) from the first, \(b\) from the second, and \(a\) from the third. Thus length \(3q\) is attained. Equality in the lower bound forces exactly three occurrences of each letter.

**Projection criterion.** For distinct \(a,b\) let \(f_a\) and \(\ell_a\) be the first and last occurrences of \(a\). The subsequence \(aba\) exists if and only if at least one \(b\) occurs strictly between these endpoints. Since each letter appears three times, deleting all letters other than \(a,b\) gives exactly one of the \(\binom63=20\) binary multiset arrangements. Directly sorting the placements of three \(a\)'s shows that precisely the six displayed arrangements fail \(aba\) or \(bab\); all other fourteen contain both. Applying this criterion to each unordered letter pair proves the stated equivalence. The constant targets \(aaa\) were already guaranteed by the three-of-each condition.

**Exact recurrence.** Write \(c=(c_a)\in\{0,1,2,3\}^q\) for the occurrence counts in a partial word and \(M=(M_a)\) for subsets of \(\Sigma_q\setminus\{a\}\). Whenever the first \(a\) has appeared and the third has not, \(M_a\) records all *other* letters seen after its first occurrence. When the third \(a\) arrives, the frozen set is precisely the alphabet appearing strictly between the first and third \(a\). Let \(F_q(c,M)\) count permissible completions. Its base case is \(F_q((3,\ldots,3),M)=1\) for states reached by permissible transitions. For each \(b\) with \(c_b<3\), set \(c'=c+e_b\) and

\[
M'_a=\begin{cases}M_a\cup\{b\},&a\ne b\text{ and }1\le c_a\le2,\\M_a,&\text{otherwise}.\end{cases}
\]

The transition is permitted precisely when either \(c'_b<3\), or \(c'_b=3\) and \(M'_b=\Sigma_q\setminus\{b\}\). Then

\[
F_q(c,M)=\sum_{\substack{b:c_b<3\\\text{transition }b\text{ permitted}}}F_q(c+e_b,M'),\qquad
N_q=F_q((0,\ldots,0),(\varnothing,\ldots,\varnothing)).
\]

This is an exact finite recurrence, not a probabilistic estimate. Each partial word has a unique state update for each appended letter. Every complete word corresponds to exactly one root-to-terminal transition path; the final-letter condition is equivalent to every nonconstant palindromic target being present. Induction on \(3q-\sum_a c_a\) therefore proves that \(F_q\) counts precisely the claimed covers for every \(q\). The supplied standalone program evaluates this recurrence in exact integer arithmetic.

**Comparison with unrestricted three-universality.** A word contains every three-letter subsequence only if its greedy complete-alphabet factorization contains three arches, each using all \(q\) letters; equivalently, every three-letter pattern can be formed from those arches. At length \(3q\), each arch must therefore be a permutation. The unrestricted shortest-cover count is thus \((q!)^3\), giving the stated four-letter comparison. Since the action of alphabet relabeling on three-of-each words is free, dividing \(N_q\) by \(q!\) gives the number of label-permutation classes.

## Verification

Run `python3 verify_pal3.py` with the Python standard library. The independent recursive multiset-word enumerator inspects all \(\frac{(3q)!}{(3!)^q}\) length-\(3q\) words for each \(q\in\{1,2,3,4\}\), directly checks the first/last property, and agrees with the mask recurrence. At \(q=4\) this is a complete inspection of exactly \(369600\) words, not a sample. The mask recurrence additionally evaluates \(q=5\) using \(62388\) memoized states. Asserted values: \(1,14,690,80016,17825160\). A concrete shortest cover is \((0123)^3\).

## Relationship to prior work

D. Adamson, *Ranking and Unranking k-Subsequence Universal Words* (2023; arXiv:2304.04583) counts full-alphabet subsequence-universal words. Adamson–Fleischmann–Huch–Koß–Manea–Nowotka, *k-Universality of Regular Languages* (2023; arXiv:2311.10658), develops corresponding regular-language counting algorithms. Neither statement equates full three-pattern universality with covering only the palindromic targets, and the explicit full-universal shortest count here is strictly smaller already at \(q=2\). The separate 2019 OEIS A330022 concerns *contiguous* occurrences of palindromes, not scattered subsequences. Earlier finite binary-cover enumeration supplies \(N_2=14\), but does not determine the labeled four- or five-letter values.

## Limitations

The exact recurrence need not be efficient for large \(q\): its masks may require exponentially many distinct states. No closed-form or asymptotic formula for \(N_q\) is asserted. The present four- and five-letter counts are finite computational theorems supported by proved exhaustive recurrences; they do not imply a simple expression for all \(q\). Literature searches do not establish absolute novelty, and an equivalent enumeration of constrained three-occurrence words may exist under another name.

## References

1. D. Adamson, *Ranking and Unranking k-Subsequence Universal Words*, arXiv:2304.04583 (first public 2023-04-10), https://arxiv.org/abs/2304.04583.
2. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea and D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658 (first public 2023-11-17), https://arxiv.org/abs/2311.10658; ISAAC 2023, DOI 10.4230/LIPIcs.ISAAC.2023.4.
3. OEIS A330022, *Length of shortest binary string containing all palindromes of length n as substrings*, https://oeis.org/A330022 (a different contiguous-factor problem).
