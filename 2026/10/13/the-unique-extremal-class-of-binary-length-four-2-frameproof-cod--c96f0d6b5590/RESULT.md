# The unique extremal class of binary length-four \(2\)-frameproof codes
## Finding
A binary code \(C\subseteq\{0,1\}^4\) is \(2\)-frameproof when, for every pair \(P\subseteq C\) with \(|P|\le 2\), the descendant set
\[
\operatorname{desc}(P)=\{x\in\{0,1\}^4:x_i\in\{p_i:p\in P\}\text{ for every }i\}
\]
meets \(C\) exactly in \(P\).

The exact maximum is
\[
M_{4,2}(2)=5.
\]
There are exactly \(16\) labeled maximum codes. They are precisely the translates
\[
C_*+s,\qquad s\in\mathbb F_2^4,
\]
of
\[
C_*=\{1000,0100,0010,0001,1111\}.
\]
Hence all maxima form one class under the standard equivalence given by independently swapping the two symbols in each coordinate.

Exactly five maxima contain \(0000\). One is \(0000\) together with all four weight-three words. The other four are indexed by a coordinate \(i\): they contain \(0000\), the three weight-two words whose supports are \(\{i,j\}\) with \(j\ne i\), and the weight-three word supported on the complement of \(i\).

Every maximum code has pairwise Hamming-distance profile
\[
6\text{ pairs at distance }2,\qquad 4\text{ pairs at distance }3.
\]
The XOR of the five codewords of \(C_*+s\) is exactly \(s\), so the translation parameter is intrinsically recoverable from the labeled maximum.

## Assumptions and scope
Words are identified with vectors in \(\mathbb F_2^4\), and translation means coordinatewise XOR. A labeled code is a literal subset of the \(16\) binary words. The equivalence used here is the standard coordinatewise alphabet-symbol equivalence for binary frameproof codes; no coordinate permutation is needed for the uniqueness statement. Coordinate permutations may also be included, giving a natural group of order \(16\cdot24=384\).

## Proof
Translate any maximum candidate by one of its codewords. Translation preserves descendants, so it suffices first to analyze codes containing \(0000\). Identify each nonzero word with its support, a nonempty subset of \(\{1,2,3,4\}\), and let \(\mathcal F\) be the supports of the nonzero codewords.

If \(A,B\in\mathcal F\) with \(B\subsetneq A\), then the word supported on \(B\) lies in \(\operatorname{desc}(\{0000,A\})\), contradicting frameproofness. Thus \(\mathcal F\) is an antichain. If two members \(A,B\in\mathcal F\) are disjoint, then \(0000\in\operatorname{desc}(\{A,B\})\), again a contradiction. Thus \(\mathcal F\) is pairwise intersecting.

An intersecting antichain on a four-point set has at most four members. An elementary case analysis proves this. A singleton cannot occur together with any other member. Ignoring singletons and the full four-set, all members have size two or three. If there are no two-sets, there are at most the four three-sets. If there is one two-set, only two three-sets avoid containing it, so the total is at most three. If there are two intersecting two-sets, at most one three-set avoids containing either, again giving at most three. There can be at most three pairwise-intersecting two-sets. Three such pairs are either a triangle, which admits no antichain-compatible three-set, or a star, which admits exactly the complementary three-set. Hence \(|\mathcal F|\le4\), so \(|C|\le5\).

The code \(C_*\) is frameproof, so equality is attained. The equality cases in the preceding antichain argument are also forced: either \(\mathcal F\) consists of all four three-subsets, or it consists of the three edges of a star together with the three-subset complementary to the star center. These five normalized families are all frameproof by direct substitution into the descendant definition.

Moreover, these five normalized maxima are exactly the translates of \(C_*\) by its five codewords. Translation of \(C_*\) by \(1111\) gives \(0000\) plus all four weight-three words; translation by a unit vector gives the corresponding star-plus-complement family. Therefore every maximum code is a translate of \(C_*\). A nonzero translation has no fixed word and partitions \(\mathbb F_2^4\) into two-cycles, so it cannot stabilize an odd five-element set. Thus the translation orbit has size \(16\), proving the labeled count.

Finally, \(C_*\) has six unit-vector pairs at Hamming distance \(2\) and four unit-vector-to-\(1111\) pairs at distance \(3\). Translation preserves distance. Since the XOR of the five words of \(C_*\) is \(0000\) and five is odd, translating by \(s\) changes the total XOR by \(s\), proving the final assertion.

## Verification
The standalone `verify.py` independently checks all \(2^{16}=65536\) subsets of \(\mathbb F_2^4\) against the descendant definition. It confirms maximum size \(5\), exactly \(16\) labeled maxima, exactly five maxima containing \(0000\), the single translation orbit, the distance profile, the XOR indexing, and the natural order-\(384\) orbit with stabilizer order \(24\).

Fresh replay produced:
`VERIFY_OK vertices=16 maximum=5 labeled_maxima=16 normalized_maxima=5 translation_orbit=16 natural_group=384 stabilizer=24 hamming_profile=2x6,3x4 xor_index=true maxima_sha256=243c8672229ef0d1ab8c6599b28cebfcf77356c939433924a2f0647c4c1a5145`.

## Relationship to prior work
Guo, Stinson, and van Trung explicitly discuss the binary \(w=2\) case. Their Theorem 5.1 constructs, for every \(N\ge3\), an \(\operatorname{SHF}(N;N+1,2,\{1,2\})\) by adjoining an all-ones column to the identity matrix. At \(N=4\), this is exactly the representative \(C_*\) above. Their paper also records the equivalence between \(w\)-frameproof codes and separating hash families of type \(\{1,w\}\), and their cited general bound gives only \(6\) at these parameters. Their \(w=2\) discussion does not prove that five is optimal or classify equality cases.

Blackburn's foundational combinatorial treatment defines the same descendant condition and studies the maximum-cardinality problem, with emphasis on large alphabets. Later length-four work by Cheng, Jiang, and Wang improves upper bounds only for alphabet size greater than \(48\), while Rochanakul's later bound applies to odd alphabet size greater than \(10\). These do not imply the binary \(q=2\) equality classification.

## Limitations
The result is a complete finite classification only for binary alphabet, length four, and coalition size two. It does not determine \(M_{N,2}(2)\) for larger \(N\), nor does it address larger alphabets or coalition sizes. The literature search found no published statement of the exact \(16\)-code census or translation classification, but an obscure or unindexed small-parameter enumeration remains a residual priority risk.

## References
1. Chuan Guo, Douglas R. Stinson, and Tran van Trung, “On tight bounds for binary frameproof codes,” arXiv:1406.6920v1, 2014.
2. Simon R. Blackburn, “Frameproof Codes,” *SIAM Journal on Discrete Mathematics* 16(3), 499–510, 2003, DOI 10.1137/S0895480101384633.
3. Jessica N. Staddon, Douglas R. Stinson, and Ruizhong Wei, “Combinatorial properties of frameproof and traceability codes,” *IEEE Transactions on Information Theory* 47(3), 1042–1049, 2001, DOI 10.1109/18.915661.
4. Minquan Cheng, Jing Jiang, and Qiang Wang, “Improved bounds on 2-frameproof codes with length 4,” *Designs, Codes and Cryptography* 87(1), 97–106, 2019, DOI 10.1007/s10623-018-0490-5.
5. Penying Rochanakul, “New Bounds on 2-Frameproof Codes of Length 4,” *International Journal of Mathematics and Mathematical Sciences*, 2020, Article 4879108, DOI 10.1155/2020/4879108.
