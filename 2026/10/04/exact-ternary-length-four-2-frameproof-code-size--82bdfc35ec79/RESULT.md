# Exact ternary length-four 2-frameproof code size

## Finding
Let \(Q=\{0,1,2\}\). For \(X\subseteq Q^4\), define
\[
\operatorname{desc}(X)=\{z\in Q^4: \text{for every coordinate }i,\ z_i=x_i\text{ for some }x\in X\}.
\]
A code \(C\subseteq Q^4\) is 2-frameproof when \(\operatorname{desc}(X)\cap C=X\) for every \(X\subseteq C\) with \(|X|\le 2\). The exact maximum is
\[
M_{2,4}(3)=M_{4,2}(3)=12,
\]
where the two notations correspond to the coalition-length and length-coalition conventions used in the literature.

## Assumptions and scope
The alphabet is exactly \(Q\), codewords are ordered words of length four, and descendants use the standard coordinatewise marking assumption. The result concerns ordinary 2-frameproof codes, not secure frameproof codes, traceability codes, identifiable-parent codes, or wide-sense variants.

Chee and Zhang's archive source defines \(M_{c,\ell}(q)\), notes that exact values beyond the trivial regime were generally unknown, and constructs length-four 2-frameproof codes as part of an asymptotic program. Rochanakul later exhibited the concrete ternary 12-word code used below while treating the length-four upper-bound problem; that paper does not prove its optimality.

## Proof
The lower bound is witnessed by the following 12 codewords, displayed as Example 1 by Rochanakul:

```text
0000 0122 0212 0221
1111 1200 1002 1020
2222 2011 2101 2110
```

Direct checking shows that no third listed codeword belongs to the descendant of two distinct listed codewords, so the code is 2-frameproof and the maximum is at least \(12\).

For the upper bound, consider all \(3^4=81\) words. For three distinct words \(x,y,z\), call \(\{x,y,z\}\) forbidden when one member lies in the coordinatewise descendant of the other two. Exhaustive construction gives exactly \(18{,}792\) such unordered triples. A 2-frameproof code is exactly a vertex subset containing no forbidden triple.

It remains to rule out a forbidden-triple-free 13-set. The property is invariant under independent permutations of the three alphabet symbols in each coordinate and under permutations of the four coordinates. Given any hypothetical 13-set, map one chosen word to \(0000\). The stabilizer of \(0000\) can map a second word to a word containing only \(0\) and \(1\), and then permute coordinates so that this second word is exactly one of
\[
1000,\quad 1100,\quad 1110,\quad 1111.
\]
These four cases correspond to the Hamming weight of the second word and exhaust all possibilities.

For each canonical root pair, an exact include/exclude search considers every possible extension. When a candidate \(v\) is included, every remaining candidate \(u\) for which \(\{x,v,u\}\) is forbidden for some already selected \(x\) is removed. A branch is pruned only when too few candidates remain to reach \(13\). This direct exhaustive search returns no 13-set in any of the four canonical cases. Therefore every ternary length-four 2-frameproof code has size at most \(12\), completing the proof.

## Verification
`artifacts/verify.py` reconstructs all \(81\) words and all \(18{,}792\) forbidden triples from the descendant definition. It verifies the 12-word witness directly. It then performs the symmetry-complete upper-bound search twice: once by a fixed-order exhaustive include/exclude recursion and once by a differently ordered recursion with an additional safe incompatibility-clique partition bound. Both refute size \(13\) in all four canonical second-word cases.

```text
VERIFY_OK
words 81
forbidden_triples 18792
witness_size 12
canonical_second_word_cases 4
engine_a_nodes 500400
engine_b_nodes 14548
upper_bound_no_size_13 True
exact_M_4_2_3 12
```

The verification is finite and exhaustive; no asymptotic extrapolation or randomized search is used.

## Relationship to prior work
Chee and Zhang, arXiv:1206.5863, first posted on 2012-06-26, define the same frameproof-code extremal function and emphasize the nontrivial length-greater-than-coalition regime. Their length-four construction gives the standard odd-alphabet lower-bound family but does not state the ternary exact value.

Cheng, Jiang, and Wang, DOI:10.1007/s10623-018-0490-5, improve upper bounds for length-four 2-frameproof codes only for large alphabet sizes. Rochanakul, DOI:10.1155/2020/4879108, gives the explicit 12-word ternary example, records Blackburn's general upper bound \(M_{4,2}(q)\le 2q^2-2\), and proves a sharper bound only for odd \(q>10\). Thus at \(q=3\) the inspected literature supplies a lower bound of \(12\) and a general upper bound of \(16\), not the equality proved here.

Searches under both extremal-function conventions, ternary and 3-ary terminology, the exact parameter \(M_{4,2}(3)\), and separating-hash terminology found no inspected source stating or implying the exact value \(12\). The 2017 paper “A Class of 2-FP Codes” concerns a binary family of growing lengths and does not cover this ternary parameter.

## Limitations
The upper bound is computer-assisted and finite. It resolves only the ternary length-four, coalition-two parameter and does not give a general formula for \(M_{2,4}(q)\). The originality conclusion is best-of-knowledge: an unindexed or non-digitized small-parameter computation could in principle predate this result, although the directly relevant 2020 paper presents the 12-word ternary example without an optimality theorem.

## References
1. Y. M. Chee and X. Zhang, “Improved Constructions of Frameproof Codes,” arXiv:1206.5863, first posted 2012-06-26; IEEE Transactions on Information Theory 58(8) (2012), 5449–5453.
2. M. Cheng, J. Jiang, and Q. Wang, “Improved bounds on 2-frameproof codes with length 4,” Designs, Codes and Cryptography 87 (2019), 97–106, DOI:10.1007/s10623-018-0490-5.
3. P. Rochanakul, “New Bounds on 2-Frameproof Codes of Length 4,” International Journal of Mathematics and Mathematical Sciences 2020, Article 4879108, DOI:10.1155/2020/4879108.
4. S. R. Blackburn, “Frameproof Codes,” SIAM Journal on Discrete Mathematics 16 (2003), 499–510, DOI:10.1137/S0895480101384633.
