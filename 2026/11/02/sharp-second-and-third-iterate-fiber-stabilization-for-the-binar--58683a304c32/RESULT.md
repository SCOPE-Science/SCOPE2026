# Sharp second- and third-iterate fiber stabilization for the binary Rudin–Shapiro word

## Finding
Let \(\mathbf r\) be the binary Rudin–Shapiro infinite word, let \(\mathcal F_n\) be its set of distinct length-\(n\) factors, and let \(T\) be the binary Defant–Kravitz tortoise map. For each \(k\in\{2,3\}\), define the **relative stabilization threshold**
\[
 b_k=\min\{N\ge1:\ \forall n\ge N\ \forall u,v\in\mathcal F_n,\quad T^k(u)=T^k(v)\iff T(u)=T(v)\}.
\]
Then both thresholds exist, and their exact values are
\[
\boxed{b_2=14,\qquad b_3=18.}
\]
Equivalently, two and three successive tortoise passes create no additional identifications beyond the first pass on all sufficiently long Rudin–Shapiro factors. Both thresholds are sharp: a new identification occurs at length \(13\) for two passes and at length \(17\) for three passes. The result asserts **equality of complete equivalence relations**, not merely equality of their numbers of classes.

## Assumptions and scope
Use the four-letter substitution \(\varphi\) and coding \(\tau\):
\[
\begin{aligned}
 \varphi(0)&=01,&\varphi(1)&=02,&\varphi(2)&=31,&\varphi(3)&=32,\\
 \tau(0)&=\tau(1)=0,&\tau(2)&=\tau(3)=1.
\end{aligned}
\]
The infinite binary word is \(\mathbf r=\tau(\varphi^\omega(0))\). For a binary finite word \(w\) containing a \(1\), \(T(w)\) removes the *first* \(1\) and appends a \(1\); it fixes an all-zero word. This is the binary restriction of the original tortoise operator, not the hare map. Iterates are compositions \(T^k\). Factors are taken at arbitrary positions of the one-sided infinite word. Only depths two and three are asserted; higher depths need not share the same equivalence classes.

## Proof
**1. Exhaustive finite description of all factors.** The complete list of adjacent pairs of symbols in \(\mathbf u=\varphi^\omega(0)\) is
\[
 \mathcal B=\{01,02,10,13,20,23,31,32\}.
\]
Indeed, internal pairs in substitution images are \(01,02,31,32\), while substitution-image boundaries of the pairs in \(\mathcal B\) are among \(10,13,20,23\). Thus no other pair can appear by induction on substitution depth. Conversely, all eight occur in the explicitly computable word \(\varphi^4(0)=0102013101023202\). For any \(n\ge1\), select \(h\) with \(2^h\ge n\). Since \(\mathbf u=\varphi^h(\mathbf u)\), each length-\(n\) factor of \(\mathbf r\) lies inside the binary coding of two consecutive \(\varphi^h\)-blocks. Therefore the **exact**, not sampled, set \(\mathcal F_n\) is the union of the length-\(n\) factors of
\[
 \tau\bigl(\varphi^h(ab)\bigr),\qquad ab\in\mathcal B.
\]
The converse follows because every pair in \(\mathcal B\) occurs in \(\mathbf u\). This gives a finite, elementary certificate of all factor sets required below.

**2. A relative prefix-inheritance lemma.** Let \(\mathcal L\) be the factor language of *any* infinite binary word. Fix integers \(k\ge1\) and \(N\ge k\). Assume every factor in \(\mathcal L\) of length \(N\) contains at least \(k\) ones, and assume that for all length-\(N\) factors \(p,q\),
\[
 T^k(p)=T^k(q)\implies T(p)=T(q).
\]
Then the same implication holds for **every** factor length \(n\ge N\). Prove the conclusion by induction on factor length. The length-\(N\) assertion is the hypothesis. For the induction step, take length-\(n+1\) factors \(u=pa\), \(v=qb\), with length-\(n\) prefixes \(p,q\) for some \(n\ge N\), and suppose \(T^k(u)=T^k(v)\). Each prefix contains at least \(k\) ones because its first \(N\) positions form a factor of that length. Let \(D_j(w)\) denote the word obtained by deleting its first \(j\) ones (well-defined here because each prefix contains at least \(k\) ones). Direct iteration of the binary tortoise map gives
\[
 T^k(pa)=D_k(p)a\,1^k,\qquad T^k(qb)=D_k(q)b\,1^k.
\]
Equality forces \(D_k(p)=D_k(q)\) and \(a=b\), by comparing the first \(N-k\) and subsequent letters before the common final \(k\) ones. It also yields \(T^k(p)=D_k(p)1^k=T^k(q)\), whence \(T(p)=T(q)\) by the induction hypothesis. Finally,
\[
 T(pa)=D_1(p)a1=D_1(q)b1=T(qb).
\]
The reverse implication \(T(u)=T(v)\Rightarrow T^k(u)=T^k(v)\) is automatic. Thus equality of the two equivalence relations at one adequate length propagates to every greater length.

**3. Exact finite certificates.** Apply Step 1 with \(h=4\) at lengths \(13,14\), and with \(h=5\) at lengths \(17,18\). For each factor, compute \(T,T^2,T^3\) exactly, partitioning the factor set by equal images. Direct finite enumeration yields:

| Length \(n\) | Factors | Classes under \(T\) | Classes under \(T^k\) | \(k\) | Partitions equal? | Minimum number of ones |
|---:|---:|---:|---:|---:|---|---:|
| 13 | 96 | 88 | 87 | 2 | No | 3 |
| 14 | 104 | 96 | 96 | 2 | Yes | 3 |
| 17 | 128 | 120 | 119 | 3 | No | 4 |
| 18 | 136 | 128 | 128 | 3 | Yes | 5 |

Equality of the *partitions*, rather than merely the class counts, is checked by comparing canonical sets of fibers. There is also a theoretical short-cut: since \(T^k\) factors through \(T\), identical numbers of classes imply identical partitions. The class counts and the exact partition comparisons were both checked.

The failure at length \(13\) is witnessed by
`0000100101110` and `0100100001110`: their \(T^2\)-images coincide, but their respective \(T\)-images are `0000001011101` and `0001000011101`. The failure at length \(17\) is witnessed by `00010000100101110` and `01000100100001110`: their \(T^3\)-images coincide, while their respective \(T\)-images are `00000001001011101` and `00001001000011101`.

At length \(14\), every factor has at least three ones, exceeding the two required by Step 2; at length \(18\), every factor has at least five ones, exceeding the three required. Applying the inheritance lemma proves equality at **all** lengths \(n\ge14\) for \(k=2\) and \(n\ge18\) for \(k=3\). The explicit preceding-length failures prove minimality of these thresholds. This completes the proof.

## Verification
The accompanying Python programs `verify_stability.py` and `verify_arithmetic.py` are standalone and use only the standard library. The first constructs the complete factor sets through the proved morphic-block exhaustion, directly compares complete partitions, checks the minimum-one hypotheses and the exceptional prior lengths; it prints `VERIFY_STABILITY_OK`. The second independently generates Rudin–Shapiro bits by parity of adjacent `11` digits in the binary integer expansion, constructs factors by sliding windows, and compares the partitions over a range of lengths; it prints `ARITHMETIC_STABILITY_OK`.

The second program tests finitely many lengths; the *all-length* conclusion depends on the proved prefix-inheritance lemma and the fully exhaustive finite certificates at lengths \(14\) and \(18\). No experimental extrapolation is used.

## Relationship to prior work
Defant and Kravitz introduced the word-tortoise operation. Campbell and Rampersad's 2026 work develops tortoise-equivalence complexity for the paperfolding and Thue–Morse words and asks for behavior of its iterates. The Rudin–Shapiro word is a standard, separately defined automatic sequence. The present result treats **relative fiber stabilization for its second and third iterates**; it neither claims the definition of tortoise nor the ordinary factor complexity as new. A one-pass factor-image census, even when known, does not imply these two- or three-pass equivalence statements: the new proof requires finite partition comparisons and the inheritance lemma.

## Limitations
Nothing here asserts that the first tortoise pass is injective, or that all higher iterates stabilize. The values \(14\) and \(18\) are the first lengths after which the extra equivalences disappear permanently; smaller isolated lengths can have coincident partitions without affecting the thresholds. The theorem is specific to this binary coding of the standard Rudin–Shapiro word. No claim is made about generalized Rudin–Shapiro words, arbitrary alphabets, or complete counts of equivalence classes for other iterate depths. Independent mathematical review and exhaustive publication-priority confirmation have not been performed.

## References
1. C. Defant and N. Kravitz, *Stack-sorting for Words*, Australasian Journal of Combinatorics 77 (2020), 51–68. Open preprint: https://arxiv.org/abs/1809.09158.
2. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811 (first posted April 28, 2026; v2 October 5, 2026). https://arxiv.org/abs/2604.25811.
3. J.-P. Allouche and M. Bousquet-Mélou, *Facteurs des suites de Rudin-Shapiro généralisées*, Bull. Belg. Math. Soc. Simon Stevin 1 (1994), 145–164. Background on Rudin–Shapiro factors; no result from this reference is required for the finite factor-set lemma above.
