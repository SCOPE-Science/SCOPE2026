# Exact equivalence automorphism group of the unique additive \( (7,2^5,5)_4 \) code
## Finding
Let \(C\subseteq\mathbb F_4^7\) be the unique additive code of parameters \( (7,2^5,5)_4 \) displayed by Grassl--Krotov--Sok--Solé. Under their equivalence notion, an automorphism may permute coordinates and then, independently in each coordinate, multiply by a nonzero field element and/or apply conjugation. The full equivalence automorphism group has order
\[
21,
\]
its coordinate action is faithful, and
\[
\operatorname{{Aut}}_{{\mathrm{{eq}}}}(C)\cong C_7\rtimes C_3,
\]
the nonabelian Frobenius group of order \(21\). Its subgroup consisting of pure coordinate permutations has order \(7\) and is precisely the cyclic shift subgroup.

The \(21\) codewords of weight \(5\) have pairwise distinct supports. Equivalently, their two-coordinate zero sets are exactly all \(\binom72=21\) unordered coordinate pairs. The \(21\) full automorphisms have coordinate-permutation orders distributed as one identity, fourteen elements of order \(3\), and six elements of order \(7\).

## Assumptions and scope
We use \(\mathbb F_4=\mathbb F_2(\omega)\) with \(\omega^2=\omega+1\), and the exact five-row additive generator printed in the source. “Additive” means \(\mathbb F_2\)-linear. The source equivalence fixes the zero symbol and permits, independently at each coordinate, the six maps
\[
x\longmapsto a x^{2^e},\qquad a\in\mathbb F_4^\times,\quad e\in\{{0,1}}.
\]
These are exactly all permutations of the three nonzero symbols.

The result concerns the automorphism group under that source equivalence. It also separately identifies the smaller subgroup obtained when every local symbol map is the identity.

## Proof
Encode \(0,1,\omega,\omega^2\) by \(0,1,2,3\). Addition is bitwise XOR in this representation. Taking the additive closure of the five displayed rows gives exactly \(32\) words with weight distribution
\[
1+21z^5+7z^6+3z^7,
\]
reproducing the source.

Among the \(21\) minimum words, the two zero coordinates are pairwise distinct and exhaust all unordered coordinate pairs. Hence a coordinate permutation \(p\in S_7\) forces the image of every minimum word: the word with zero pair \(\{{i,j\}}\) must go to the unique minimum word with zero pair \(\{{p(i),p(j)\}}\).

Fix a coordinate \(i\). Each of \(1,\omega,\omega^2\) occurs in coordinate \(i\) among minimum words. Therefore the forced images of the minimum words determine the local symbol map at \(i\) uniquely. A candidate \(p\) extends to a source-equivalence automorphism if and only if all seven forced local maps are permutations of \(\mathbb F_4^\times\) and the resulting transformation preserves all \(32\) codewords.

Exhausting the finite set \(S_7\) gives exactly \(21\) successful coordinate permutations. The local maps are uniquely determined, so the coordinate action is faithful. Their permutation orders have census
\[
1^1,\qquad 3^{{14}},\qquad 7^6.
\]
Thus the group is not cyclic. Its unique Sylow \(7\)-subgroup is normal, and the order census exhibits a subgroup of order \(3\); hence the group is the nontrivial semidirect product \(C_7\rtimes C_3\). Restricting all local maps to the identity leaves exactly seven coordinate permutations, the cyclic shift subgroup.

## Verification
The standalone `artifacts/verify.py` rebuilds the code from the printed generator using exact finite-field arithmetic. It checks the source weight distribution, proves that the minimum-word zero pairs are all \(21\) pairs, exhausts all \(7!=5040\) coordinate permutations, reconstructs the forced local maps, and directly tests the resulting transformations on all \(32\) codewords.

A successful replay prints `VERIFY_OK`, together with counts \(7\) and \(21\) for the pure and full automorphism groups and the order census above. No sampling or timeout inference is used.

## Relationship to prior work
Grassl--Krotov--Sok--Solé give this exact generator, prove uniqueness up to their equivalence, state that the code is cyclic, and give its weight distribution. They do not state the exact automorphism-group order, the faithful coordinate action, the Frobenius-group structure, or the complete minimum-support zero-pair incidence.

Focused searches for this exact parameter set, its weight distribution, “automorphism group,” “Frobenius group of order \(21\),” and the equivalent length-seven additive-code descriptions did not locate an indexed statement of the exact group. Earlier work determining automorphism groups of the length-eleven punctured dodecacode concerns a different code and does not imply the present stabilizer.

## Limitations
This is a finite structural result for the unique additive \( (7,2^5,5)_4 \) code from the cited classification. It does not determine automorphism groups of the full length-seven classification table or of the punctured dodecacode itself. The originality search cannot exclude an unindexed computation or software-internal classification of an equivalent representative.

The group identification depends on the source's additive-code equivalence, which permits independent conjugation in coordinates. Under pure coordinate permutations alone the group is only \(C_7\).

## References
1. M. Grassl, D. Krotov, L. Sok, and P. Solé, *The punctured dodecacode is unique*, arXiv:2601.08008v1, first public 12 January 2026; Mathematics and Education in Mathematics 55 (2026), 393--404, DOI 10.55630/mem.2026.55.393-404.
2. M. Shi, D. S. Krotov, and P. Solé, *A new distance-regular graph of diameter 3 on 1024 vertices*, Designs, Codes and Cryptography 87 (2019), 2091--2101, DOI 10.1007/s10623-019-00609-w.
