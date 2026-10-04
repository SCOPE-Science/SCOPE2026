# Exact ternary length-three strong multimedia IPP code size
## Finding
For alphabet \(Q=\{0,1,2\}\), every \(2\)-strongly multimedia identifiable parent property code of length \(3\) has at most \(11\) codewords, and the bound is attained. Thus the exact maximum is \(11\).

One attaining code is
\[
\begin{aligned}
C=\{&(0,0,0),(0,0,1),(0,1,1),(0,1,2),(0,2,2),\\
&(1,0,0),(1,0,2),(1,2,1),(2,0,2),(2,1,0),(2,2,2)\}.
\end{aligned}
\]

## Assumptions and scope
For a subcode \(A\subseteq C\subseteq Q^3\), define
\[
\operatorname{desc}(A)=A(1)\times A(2)\times A(3),
\]
where \(A(j)\) is the set of symbols occurring in coordinate \(j\). For \(A\subseteq C\), let
\[
S(A)=\{B\subseteq C:\operatorname{desc}(B)=\operatorname{desc}(A)\}.
\]
The code \(C\) is a \(2\)-SMIPPC when
\[
\bigcap_{B\in S(A)}B\ne\varnothing
\]
for every nonempty \(A\subseteq C\) with \(|A|\le2\). This is the definition used by Jiang, Cheng, Miao and Wu.

The claim is only for alphabet size \(3\), length \(3\), and coalition bound \(2\). It does not assert an extremal formula for other alphabet sizes.

## Proof
For a pair \(A=\{u,v\}\subseteq C\), put
\[
X=C\cap\operatorname{desc}(A).
\]
A word \(x\in X\) belongs to every member of \(S(A)\) if and only if some coordinate-symbol of \(x\) occurs exactly once in that coordinate among the words of \(X\). Indeed, a unique coordinate-symbol forces every set with descendant \(\operatorname{desc}(A)\) to contain \(x\). Conversely, if \(x\) has no unique coordinate-symbol in \(X\), then \(X\setminus\{x\}\) has the same three coordinate projections as \(X\), so it is a member of \(S(A)\) that omits \(x\). Hence the \(2\)-SMIPPC condition can be checked exactly by this local uniqueness criterion for every pair.

The archive source proves the general upper bound
\[
|C|\le q^2+\frac{q(q-1)}2.
\]
At \(q=3\), this gives \(|C|\le12\). It therefore remains only to rule out size \(12\).

The bundled exhaustive proof does so without a solver. A non-SMIPPC violation is hereditary upward: once a pair has no member forced into every parent set, adding more codewords cannot restore a unique coordinate-symbol inside that pair's descendant box. The verifier enumerates every minimal forbidden subset inside each pair-descendant box. There are exactly \(459\) such minimal obstructions, all of size \(4\) or \(5\).

Suppose a size-\(12\) ternary code existed. Independent symbol permutations in the three coordinates can send one chosen codeword to \((0,0,0)\). After permuting coordinates and, independently, the two nonzero symbols in each coordinate, a second codeword can be normalized according to its Hamming weight to one of
\[
(1,0,0),\qquad(1,1,0),\qquad(1,1,1).
\]
These operations preserve the \(2\)-SMIPPC property. For each of the three normalized cases, the verifier performs complete branch-and-bound enumeration of subsets avoiding all minimal obstructions. No branch reaches size \(12\). Thus \(|C|\le11\).

Finally, the displayed \(11\)-word code satisfies the local uniqueness criterion for every pair, so it is a \(2\)-SMIPPC. Therefore the exact maximum is \(11\).

## Verification
Run `python3 verify.py`. It uses only the Python standard library. It reconstructs all \(27\) ternary words, generates the complete family of minimal forbidden subsets from the definition, directly checks the displayed witness, and exhausts the three symmetry-normalized size-\(12\) cases.

The expected terminal line is:

`VERIFY_OK maximum=11 witness=11 minimal_obstructions=459 sizes=4,5 symmetry_reps=3 nodes=21227,31563,30388`

The finite search is exhaustive for this exact parameter set; it is not sampling and no timeout is used as a mathematical conclusion.

## Relationship to prior work
The first public version of *Multimedia IPP Codes with Efficient Tracing* was posted as arXiv:1411.6841v1 on 2014-11-25. It defines \(t\)-SMIPPCs, proves for length \(3\) and strength \(2\) the upper bound
\[
M\le q^2+\frac{q(q-1)}2,
\]
and constructs optimal length-three codes for \(q\equiv0,1,2,5\pmod 6\). For \(q=3\), its bound is \(12\), while its construction theorem does not cover the case.

The 2024 paper *Constructions of t-strongly multimedia IPP codes with length t+1* revisits the same length-three problem. Its conclusion states that optimal \(2\)-SMIPPCs of length \(3\) are constructed for every positive integer \(q\not\equiv3,4\pmod6\). Thus the smallest omitted congruence-class case is \(q=3\). The exact value \(11\) found here is one below the general upper bound.

The journal article *Multimedia IPP codes with efficient tracing* is classified primarily under MSC \(94A62\), with \(94B25\) also listed, placing the underlying fingerprinting-code problem in information and communication theory.

## Limitations
This is an exact finite result only for \(q=3\), length \(3\), and strength \(2\). It does not settle the next omitted congruence class, does not classify all size-\(11\) codes up to equivalence, and does not improve the general asymptotic bounds. A residual originality risk is an unindexed small-parameter computation stated outside the literature and databases inspected.

## References
1. J. Jiang, M. Cheng, Y. Miao, D. Wu, *Multimedia IPP Codes with Efficient Tracing*, arXiv:1411.6841v1, 2014-11-25.
2. J. Jiang, Y. Gu, M. Cheng, *Multimedia IPP codes with efficient tracing*, Designs, Codes and Cryptography 88 (2020), 851--866. DOI:10.1007/s10623-020-00717-y.
3. J. Jiang, F. Pei, C. Wen, M. Cheng, H. D. L. Hollmann, *Constructions of t-strongly multimedia IPP codes with length t+1*, Designs, Codes and Cryptography 92 (2024), 2949--2970. DOI:10.1007/s10623-024-01422-w.
