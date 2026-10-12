# Exact distortion of an isospectral binary code family in dimension three

## Finding
For every integer \(t\geq0\), there are two nondegenerate, permutation-inequivalent binary linear codes \(C_t,D_t\) of the same parameters \([6+7t,3]\), with identical ordinary Hamming-weight enumerator
\[
W_t(z)=1+3z^{4t+2}+3z^{4t+4}+z^{4t+6},
\]
whose **exact minimum linear code distortion** is
\[
\boxed{\mathcal D(C_t,D_t)=\left(\frac{2t+2}{2t+1}\right)^2.}
\]
In particular they remain inequivalent for every \(t\), but their minimum distortion tends to \(1\); the precise gap is \(\mathcal D-1=(4t+3)/(2t+1)^2\).

## Assumptions and scope
Work over \(\mathbb F_2\). Identify the seven nonzero column vectors of \(\mathbb F_2^3\) with labels \(1,\dots,7\), whose ordinary three-bit binary expansions give coordinates and whose addition is bitwise XOR. For an integer multiplicity vector \(a=(a_1,\dots,a_7)\), define \(C(a)\) as the row span of the matrix whose columns contain exactly \(a_p\) copies of column \(p\). Define
\[
a_t=(t,t,t,t+1,t+1,t+1,t+3),\qquad
b_t=(t,t,t,t,t+2,t+2,t+2),
\]
and set \(C_t=C(a_t)\), \(D_t=C(b_t)\). Each has length \(6+7t\). At \(t=0\), the columns of \(C_t\) include labels \(4,5,6,7\), while those of \(D_t\) include \(5,6,7\); each spans \(\mathbb F_2^3\). Thus both have dimension three for every \(t\).

For a linear isomorphism \(T:C_t\to D_t\), let
\[
\mathcal D_T=\frac{\max_{x\in C_t\setminus\{0\}}\operatorname{wt}(Tx)/\operatorname{wt}(x)}{\min_{x\in C_t\setminus\{0\}}\operatorname{wt}(Tx)/\operatorname{wt}(x)};
\qquad \mathcal D(C_t,D_t)=\min_T\mathcal D_T.
\]
The minimization is over all invertible linear maps between the codes, rather than over coordinate permutations or nonlinear bijections.

## Proof
For a nonzero message \(u\in\mathbb F_2^3\), the word in \(C(a)\) has Hamming weight \(w_a(u)=\sum_{p:u\cdot p=1}a_p\). In increasing message-label order \(u=1,\ldots,7\), direct evaluation gives
\[
\begin{aligned}
(w_{a_t}(u))_{u=1}^7&=(4t+4,4t+4,4t+2,4t+6,4t+2,4t+2,4t+4),\\
(w_{b_t}(u))_{u=1}^7&=(4t+4,4t+4,4t+4,4t+6,4t+2,4t+2,4t+2).
\end{aligned}
\]
This proves equality of the stated weight enumerators.

Every isomorphism \(T\) acts on the seven nonzero messages by an element of \(\mathrm{GL}_3(\mathbb F_2)\). The minimum-weight message triples are \(L_C=\{3,5,6\}\) and \(L_D=\{5,6,7\}\). The triple \(L_C\) is dependent, because \(3\oplus5\oplus6=0\), whereas \(L_D\) is independent, because \(5\oplus6\oplus7=4\neq0\). Hence **no** linear isomorphism sends \(L_C\) onto \(L_D\). As both triples have three elements, every such map sends at least one minimum-weight message of \(C_t\) to a message of \(D_t\) of weight at least \(4t+4\), and also sends some message of \(C_t\) of weight at least \(4t+4\) to a minimum-weight message of \(D_t\). Setting \(r=(4t+4)/(4t+2)\), its seven positive weight ratios therefore have a member at least \(r\) and another at most \(1/r\). It follows that \(\mathcal D_T\geq r^2\).

Conversely, the identity map on message vectors \(u\mapsto u\) is an isomorphism from \(C_t\) to \(D_t\). Its seven weight ratios, in label order, are \((1,1,r,1,1,1,1/r)\). Therefore its distortion is exactly \(r^2\), proving the displayed formula for all \(t\geq0\). Since \(r>1\), the two codes are not Hamming-isometric. More directly, a coordinate permutation inducing code equivalence would preserve the minimum-message dependency pattern, which differs between them. Finally, algebra gives \(r^2-1=(4t+3)/(2t+1)^2\).

## Verification
The standalone `verify.py` independently constructs all \(168\) invertible maps of \(\mathbb F_2^3\), derives the two weight vectors from column multiplicities, checks the dependent/independent minimum-message triples, and calculates every resulting distortion exactly as a rational number for \(t\in\{0,1,2,3,5,10,100\}\). It confirms the formula and records \(60\) attaining isomorphisms at each tested parameter. Execute `python3 verify.py` (Python standard library); successful output is `VERIFY_OK`. This finite computation corroborates but is **not** the proof for unbounded \(t\); the preceding argument is independent of computation.

## Relationship to prior work
Bennett, Fox and Morrell introduced and investigated the Code Distortion Problem, including a general enumeration algorithm, approximation algorithms and hardness results (arXiv:2607.26261; APPROX/RANDOM 2026, Article 24). The definition here agrees with theirs. The longstanding fact that code equivalence is finer than ordinary weight-enumerator equality is not new and is not claimed as such. The present result specifically computes, for every nonnegative integer \(t\), the optimal quantitative distortion of a dimension-three **isospectral but inequivalent** pair. A generic finite-dimensional distortion algorithm alone does not specify this closed formula or the dependency obstruction proving its optimality.

## Limitations
The statement concerns only the displayed family, binary alphabet, dimension three, **linear** code isomorphisms and Hamming weight. It gives no classification of all isospectral code pairs, no global minimum distortion among inequivalent codes at fixed length, and no claim about nonlinear mappings. Similar equal-enumerator examples predate the motivating paper. An earlier unpublished or unindexed exact family formula cannot be excluded; independent literature verification remains desirable.

## References
1. H. Bennett, M. Fox and B. Morrell, *The Code Distortion Problem*, arXiv:2607.26261 (initial public version 2026-07-28); *LIPIcs APPROX/RANDOM 2026*, Article 24, DOI 10.4230/LIPIcs.APPROX/RANDOM.2026.24, especially Sections 1, 2.4–2.5 and 4.1.
2. P. J. Cameron, *Cycle Index, Weight Enumerator, and Tutte Polynomial*, *Electronic Journal of Combinatorics* 9 (2002); DOI 10.37236/1663. General background on the weight enumerator and equivalent-code invariants; not cited for the new quantitative formula.
