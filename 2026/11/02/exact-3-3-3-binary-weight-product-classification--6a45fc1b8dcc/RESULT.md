# Exact \((3,3,3)\) binary-weight product classification

## Finding
Let \(s_2(t)\) be the number of ones in the base-two expansion of a positive integer \(t\). All unordered pairs of positive odd integers \((a,b)\), written with \(a\le b\), satisfying
\[
s_2(a)=s_2(b)=s_2(ab)=3
\]
are exactly
\[
\boxed{(a,b)\in\{(7,7),(7,19),(7,37),(11,35),(13,21),(21,49)\}.}
\]
The six corresponding products, in the same order, are \(49,133,259,385,273,1029\). In particular, the **sharp maximum product** is
\[
\boxed{\max ab=1029,\quad\text{attained only by }(a,b)=(21,49).}
\]
The classification is unconditional, but it uses the published upper-bound theorem of Kaneko and Stoll.

## Assumptions and scope
All variables are positive integers; \(a,b\) are odd, and pairs are unordered (\(a\le b\)). Repeated factors are allowed. Binary weight \(s_2(t)\) is the population count of the standard base-two expansion, without leading zeros. This is the first **symmetric three-bit factor** case of the sparse-product problem. The result makes no assertion about even factors, other digit weights, or other bases.

## Proof
**Global cutoff.** Kaneko and Stoll, *Products of integers with few nonzero digits* (arXiv:2112.03077v1), Theorem 2.2, establish that for odd positive integers \(a,b\) with \(s_2(a)=\ell\), \(s_2(b)=m\), \(s_2(ab)=3\), and \(\max\{\ell,m\}\ge3\), one has
\[
ab<2^{-13+4\ell m}.
\]
Substituting \(\ell=m=3\) gives the strict, finite cutoff \(ab<2^{23}\). The theorem's proof in the cited source treats the carry interactions and its stated hypotheses apply without an additional coprimality or distinctness condition.

**Exhaustive parameterization.** Since \(ab\) is odd and has exactly three binary ones, there are unique integers \(1\le i<j\) such that
\[
ab=1+2^i+2^j.
\]
The bound \(ab<2^{23}\) forces \(j\le22\). Conversely, each of the \(\sum_{j=2}^{22}(j-1)=231\) choices of \(1\le i<j\le22\) gives a positive odd three-bit integer below \(2^{23}\). To list all unordered factorizations \(ab\), it is sufficient to test odd divisors \(a\) with \(7\le a\le\lfloor\sqrt{ab}\rfloor\); the lower endpoint is the smallest positive odd integer with three binary ones. Retain exactly those divisors with \(s_2(a)=s_2((ab)/a)=3\). This is a complete finite test of every possible solution: the global cutoff removes the infinite tail, and unique binary expansion plus \(a\le b\) removes omissions and permutations.

**Exact finite certificate.** The accompanying standalone Python program `verify.py` implements the preceding product-first enumeration with only integer arithmetic. It checks exactly \(231\) three-bit products and \(5473\) eligible trial divisors, producing precisely
\[
(7,7,49),\ (7,19,133),\ (7,37,259),\
(11,35,385),\ (13,21,273),\ (21,49,1029).
\]
For an independent cross-check, the same program enumerates the uniquely parameterized factors \(1+2^u+2^v\), \(1\le u<v\le22\), directly, retaining \(a\le b\) and \(ab<2^{23}\). It checks exactly \(3672\) admissible unordered pairs and returns the identical six solutions. Both finite enumerations and all assertions in the certificate were executed against the package file.

Direct arithmetic gives
\[
\begin{aligned}
7\cdot7&=49=32+16+1,\\
7\cdot19&=133=128+4+1,\\
7\cdot37&=259=256+2+1,\\
11\cdot35&=385=256+128+1,\\
13\cdot21&=273=256+16+1,\\
21\cdot49&=1029=1024+4+1.
\end{aligned}
\]
Each factor also has three binary ones. The six products are distinct, and the last is the largest. This proves both the complete classification and the optimal product bound.

## Verification
Run `python3 verify.py` from the directory containing the standalone file; no external packages or input files are needed. The program prints `VERIFY_OK`, the two independent exhaustive-search counts (\(231\) products/\(5473\) divisor tests; \(3672\) factor-pair tests), the six triples and the sharp maximum. `verify.py` was run successfully from its actual package path. The infinite scope depends on the published bound cited above; neither bounded enumeration by itself nor an unsuccessful search would certify the absence of larger solutions.

## Relationship to prior work
Kaneko and Stoll (first preprint 6 December 2021) introduce sparse binary products and prove effective bounds, including the global \(2^{23}\) cutoff applicable here, but do not state the six-pair exact classification for \((s_2(ab),s_2(a),s_2(b))=(3,3,3)\). A previously published classification of the asymmetric weights \((3,2,3)\) determines exactly \((3,7)\) and \((5,7)\); its hypothesis \(s_2(a)=2\) cannot imply a classification in which both factors have weight three.

OEIS A080025 tabulates numbers admitting factor pairs whose binary weight equals the product's binary weight. Its displayed sequence already contains all six product values, so discovering their presence is **not** new. Its 10,000-term public table ends at \(2{,}928{,}786\), below the independently required \(2^{23}=8{,}388{,}608\) search cutoff, and it supplies neither the exact six-pair restriction nor proof of exclusion of all larger products in this three-bit slice. The contribution is the exhaustive *global* classification and the **sharp** maximum, not an unqualified novelty claim about those six integers. The possibility of an unindexed older exact classification remains.

## Limitations
The proof relies on Kaneko–Stoll Theorem 2.2 and does not reprove its deep carry bound. It classifies only odd factor pairs of binary weight three with three-bit product and does not establish a general digit-weight family. Enumeration becomes a proof only after the independent, published global bound is invoked. Exhaustive checks are finite and reproducible, but they do not constitute independent scientific review. Prior sequence tables contain the individual product values; novelty is limited to the global completeness and sharp bound in this slice.

## References
1. H. Kaneko and T. Stoll, “Products of integers with few nonzero digits,” arXiv:2112.03077v1, first publicly posted 6 December 2021, Theorem 2.2; *Uniform Distribution Theory* 17 (2022), 71–89. https://arxiv.org/html/2112.03077v1
2. “Exact \((3,2,3)\) binary-weight product classification,” publicly available mathematical record. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-3-2-3-binary-weight-product-classification--28456ef398f9
3. The On-Line Encyclopedia of Integer Sequences, A080025 and b-file. https://oeis.org/A080025 ; https://oeis.org/A080025/b080025.txt
