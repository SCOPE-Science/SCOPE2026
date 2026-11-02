# Exact maximal two-tortoise fiber spectrum of Thue–Morse factors

## Finding
Let \(\mathbf t=011010011001\cdots\) be the binary Thue–Morse word, and let \(T(w)\) move the first occurrence of \(1\) in a finite binary word to the end, fixing the all-zero word. For every \(n\ge1\), set
\[
M_2(n)=\max_{y\in\{0,1\}^n}\#\{w\in\operatorname{Fact}_n(\mathbf t):T^2(w)=y\}.
\]
Then
\[
(M_2(1),\ldots,M_2(10))=(1,2,3,6,6,6,5,3,3,2),
\qquad M_2(n)=2\quad(n\ge10).
\]
The stabilization threshold ten is sharp: the maximum at length nine is three, while all lengths at least ten have maximum exactly two.

## Assumptions and scope
The substitution is \(\mu(0)=01\) and \(\mu(1)=10\). Its one-sided fixed point beginning with zero is \(\mathbf t=\lim_{j\to\infty}\mu^j(0)\). The factor set \(\operatorname{Fact}_n(\mathbf t)\) consists of **distinct** contiguous words of length \(n\), not their occurrences. The maximum ranges over all output words of length \(n\); an empty fiber contributes zero. The map \(T\) is the binary Defant–Kravitz tortoise map, with precisely two iterations here.

## Proof
**Finite completeness.** For any integer \(1\le n\le10\), choose \(m=\lceil\log_2 n\rceil\). The word \(\mathbf t\) is a concatenation of blocks \(\mu^m(0)\) and \(\mu^m(1)\), each having length \(2^m\ge n\). Every length-\(n\) factor lies in at most two consecutive such blocks, so it occurs inside \(\mu^m(ab)\) for a length-two factor \(ab\) of \(\mathbf t\). All four binary length-two words occur in \(\mathbf t\) (e.g., in the prefix `01101001`), and so **the union of all length-\(n\) windows in the four words \(\mu^m(00),\mu^m(01),\mu^m(10),\mu^m(11)\) is exactly \(\operatorname{Fact}_n(\mathbf t)\)**. The standalone verifier enumerates these full sets without sampling, then groups by \(T^2\). The factor counts for lengths one through ten are \((2,4,6,10,12,16,20,22,24,28)\), and the corresponding maximum group sizes are \((1,2,3,6,6,6,5,3,3,2)\). As a separate exact length-ten certificate, all 28 distinct length-ten factors contain at least four ones. The verifier cross-checks each complete set against an independently generated length-16384 substitution prefix; this is corroboration, while the four-block argument supplies completeness.

**Length-ten inheritance.** Every factor of length at least ten begins with a length-ten factor, and hence has at least three ones within its first ten positions. Write it uniquely as
\[
w=0^a1\,0^b1\,0^c1\,v,
\qquad a,b,c\ge0.
\]
Directly from the definition,
\[
T^2(w)=0^{a+b+c}1\,v\,11.
\]
Suppose two length-\(n\) factors \(w,w'\), with \(n\ge10\), have equal \(T^2\)-images. Their third ones occur at the same position \(a+b+c+2\), and the suffixes \(v\) following the third ones are equal. Truncate both factors to length ten. Because the common third-one position is at most ten, their two truncated factors also have equal \(T^2\)-images: they have the same zero-prefix length and the same truncated post-third-one suffix. Moreover, mapping a word in this length-\(n\) fiber to its first ten symbols is injective: the common image uniquely fixes its entire suffix after the third one, so equal length-ten prefixes imply equal original words. Consequently each length-\(n\) two-tortoise fiber injects into a length-ten two-tortoise fiber. The exact length-ten enumeration gives
\[
M_2(n)\le M_2(10)=2\qquad(n\ge10).
\]

**Matching lower bound.** Campbell and Rampersad [1, Theorem 6] prove that the Thue–Morse one-tortoise complexity has a deficit of two or four relative to ordinary factor complexity for **every** \(n\ge10\). Hence distinct length-\(n\) factors have equal one-step images for every such length; applying \(T\) a second time preserves that equality. Thus \(M_2(n)\ge2\) for every \(n\ge10\), completing the proof.

## Verification
Run `python3 verify.py` using Python 3's standard library. The complete finite enumeration prints `VERIFY_OK`. The verifier independently compares the four-block enumeration with a length-16384 substitution prefix for lengths one through ten, confirms each maximum and the minimum number of ones at length ten, and tests illustrative larger lengths. The infinite upper and lower bounds are mathematical implications proved above, not extrapolations from the longer-length tests. `verification-output.txt` preserves the recorded run output.

## Relationship to prior work
Campbell and Rampersad [1], first public on 28 April 2026, define iterated tortoise complexity and prove exact Thue–Morse **one-step** complexity in Theorem 6. Their Section 6 and conclusion explicitly invite analogous calculations for higher iteration counts. The present result concerns the **maximum cardinality of a two-step fiber**, not the number of one-step classes or the complete number of two-step classes. Its lower bound invokes their theorem rather than claiming it as new. Defant and Kravitz [2] originally defined the sorting operation on arbitrary finite words, but their general preimage methods are not a length-uniform maximum-fiber classification for factors of this automatic word. The \(k\)-binomial equivalence of Lejeune, Leroy and Rigo [3] is a different equivalence relation and does not imply the statement.

## Limitations
The claim concerns only the binary Thue–Morse fixed point and exactly two tortoise iterations. It does not determine the full second-tortoise complexity sequence or the identity of all fibers at long lengths. The finite tables are fully exhaustively certified within the morphic four-block model; the all-length lower bound uses the published one-step theorem as an external mathematical premise. Publication priority and independent audit are not certified.

## References
[1] J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811 (first submitted 28 April 2026), especially Definition 1, Theorem 6 and Section 7. https://arxiv.org/html/2604.25811v2

[2] C. Defant and N. Kravitz, *Stack-sorting for words*, Australas. J. Combin. 77 (2020), 51–68. https://arxiv.org/abs/1809.09158

[3] M. Lejeune, J. Leroy and M. Rigo, *Computing the k-binomial complexity of the Thue–Morse word*, J. Combin. Theory Ser. A 176 (2020), 105284. https://arxiv.org/abs/1812.07330
