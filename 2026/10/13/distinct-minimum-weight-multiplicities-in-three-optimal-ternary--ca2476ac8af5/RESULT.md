# Distinct minimum-weight multiplicities in three optimal ternary cyclic codes of length \(242\)

## Finding
For the three canonical ternary cyclic codes \(C_e\) with exponent \(e\in\{2,16,20\}\) and common parameters \([242,232,4]_3\), the exact numbers of minimum-weight codewords satisfy
\[
(A_4(C_2),A_4(C_{16}),A_4(C_{20}))=(24200,33880,43560).
\]
Consequently their numbers of distinct minimum-weight supports are \(12100\), \(16940\), and \(21780\), and they are pairwise monomially inequivalent. The cyclic code families and their distance-four parameters are established prior results; only the comparative counts and consequence are asserted here.

## Assumptions and scope
Work over \(K=\mathbb F_3[t]/(t^5+2t^4+1)\). The residue \(\alpha=t\) is primitive: repeated multiplication verifies that the \(242\) values \(1,\alpha,\ldots,\alpha^{241}\) are distinct and \(\alpha^{242}=1\). For \(e\in\{2,16,20\}\), index the coordinates by \(j=0,\ldots,241\) and define
\[
C_e=\left\{(c_j)\in\mathbb F_3^{242}:\sum_{j=0}^{241}c_j\alpha^j=\sum_{j=0}^{241}c_j\alpha^{ej}=0\right\}.
\]
Each pair of field-valued equations represents ten scalar parity-check equations over \(\mathbb F_3\). The dimension calculation below is for exactly these defining zeros, with no coordinate shortening, extension, or quotient.

## Proof
For each of the three exponents, the ten scalar rows formed by taking the coefficients of \(1,t,t^2,t^3,t^4\) in the two parity checks have rank \(10\) over \(\mathbb F_3\), as the included exact elimination computes. Thus \(\dim C_e=242-10=232\). Independent exhaustive checks establish \(A_3(C_e)=0\) and the stated strictly positive \(A_4(C_e)\). There is no nonzero word of weight one, because every first parity-check column is nonzero. There is no word of weight two: if two first-check terms cancel then their field ratio is \(\pm1\), so their distinct positions differ by \(121\); because each \(e\) is even, their second-check terms cannot cancel. Therefore the minimum distance is exactly \(4\).

Here is an exhaustive exact calculation of \(A_4\), rather than a statistical estimate. For a fixed exponent \(e\), define the two-component syndrome of a signed coordinate \((j,s)\), with \(s\in\{1,-1\}\subset\mathbb F_3\), by
\[
P_e(j,s)=(s\alpha^j,s\alpha^{ej})\in K^2.
\]
For all \(0\le i<j<242\) and all four sign choices, place the labeled unordered pair \((i,j;s,t)\) in the bucket with key \(P_e(i,s)+P_e(j,t)\). Match every bucket with its additive inverse, keeping only matched pairs whose four coordinate indices are distinct. Such matches are in bijection with a weight-four codeword together with a partition of its four positions into two unordered two-element parts and a choice of which part is enumerated first. Each word occurs exactly \(3\times2=6\) times. Thus the number of matches divided by \(6\) is exactly \(A_4\), with no unexamined supports or signs. The standalone Python verifier implements this counting identity over the indicated field and returns precisely \(24200\), \(33880\), and \(43560\).

As an algorithmically distinct cross-check, the included C++ verifier enumerates every three-element and four-element support directly, normalizing one nonzero coefficient to \(1\), testing all remaining \(2^{r-1}\) sign choices, and multiplying the resulting number of solutions by \(2\) to restore overall scalar sign. It constructs its own finite-field addition and multiplication tables from the stated polynomial. Its three-weight counts are all zero, and its four-weight counts match those above. This directly verifies the exhaustiveness and the sixfold pair-bucket normalization without using the pair-bucket procedure.

A code of distance \(4\) has no two linearly independent words supported on the same four coordinates: their suitable linear combination would cancel one coordinate and have weight at most \(3\). Hence each weight-four support accounts for exactly the two scalar multiples of a nonzero word, establishing the three support counts. Monomial equivalence over \(\mathbb F_3\) preserves Hamming-weight multiplicities; the three different coefficients \(A_4\) rule it out pairwise.

## Verification
Run `python3 verify.py` using Python's standard library; it checks primitivity, parity-check rank \(10\), and the exact signed-pair syndrome count for each exponent before printing `VERIFY_OK`. Compile `direct_check.cpp` with `g++ -O3 -std=c++17 direct_check.cpp -o direct_check` and run `./direct_check`; it independently checks all three- and four-coordinate supports, prints \(A_3=0\) and the exact \(A_4\) for each exponent, and ends in `VERIFY_OK`. All loops are finite and completely enumerate their specified domains. No numerical approximation or timeout is used as a proof.

## Relationship to prior work
Bao and Zou (2026, arXiv:2601.12427, Table 1) summarize the known exponent choices \(e=2,16,20\), giving their optimal distance-four parameters under conditions satisfied at \(m=5\). The 2013 paper of Li, Li, Helleseth, Ding, and Tang (arXiv:1309.1218) establishes the original \(e=16\) and \(e=20\) constructions and lists the \(m=5\) examples. These sources supply the already known common parameters, not the three explicit minimum-weight multiplicities compared here. Searches for these counts and for an equivalent complete weight-four comparison did not reveal an earlier covering statement; this is a scoped literature assessment, not a proof of global novelty.

## Limitations
The exact values concern only \(m=5\) and the listed three exponents; no claim is made about other odd extension degrees, entire weight enumerators, or monomial classifications across all known optimal exponent families. The counts do not claim improved minimum distance. Mathematical correctness is supported by independent exhaustive finite checks; a literature search cannot exclude unindexed earlier equivalent calculations, and independent external audit has not been performed.

## References
1. J. Bao and H. Zou, *Counterexamples, Constructions, and Nonexistence Results for Optimal Ternary Cyclic Codes*, arXiv:2601.12427v1, publicly posted 2026-01-18, especially Introduction and Table 1. https://arxiv.org/abs/2601.12427
2. N. Li, C. Li, T. Helleseth, C. Ding, and X. Tang, *Optimal Ternary Cyclic Codes with Minimum Distance Four and Five*, arXiv:1309.1218v1, 2013, especially the construction of the \(e=16\) and \(e=20\) families and their length-\(242\) examples. https://arxiv.org/abs/1309.1218
