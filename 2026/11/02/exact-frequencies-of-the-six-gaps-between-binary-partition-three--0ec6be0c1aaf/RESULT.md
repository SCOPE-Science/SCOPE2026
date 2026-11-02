# Exact frequencies of the six gaps between binary-partition three-square exceptions

## Finding
Let \(b(m)\) count partitions of \(m\geq 0\) into powers of two, repetitions allowed, with \(b(0)=1\). Write
\[
E=\{n\geq 0:\ b(2n)\text{ is not a sum of three integer squares}\}
 =\{f_0<f_1<f_2<\cdots\}.
\]
For every \(N\geq1\) and \(g\in\{6,8,10,16,18,24\}\), define
\[
G_g(N)=\#\{0\leq i<N:\ f_{i+1}-f_i=g\}.
\]
Then
\[
G_g(N)=p_gN+O(1+\log N),
\qquad
\begin{array}{c|rrrrrr}
g&6&8&10&16&18&24\\\hline
p_g&1/4&1/4&1/16&3/16&3/16&1/16
\end{array}.
\]
The constants implied in the error estimate can be chosen uniformly over these six gaps. All six limiting frequencies are positive and sum to one. The limiting gap mean is \(12\); its second moment is \(176\) and its variance is \(32\).

Equivalently, for real \(X\geq2\),
\[
\#\{i:f_i<X,\ f_{i+1}-f_i=g\}
=\frac{p_g}{12}X+O(1+\log X).
\]

## Assumptions and scope
Use the classical binary-partition function \(b\), not the colored variants. By the three-square characterization of Sobolewski and Ulas (Corollary 3.3), if
\(t_n=(-1)^{s_2(n)}\) is the sign version of the Thue–Morse sequence, and \(T_n=(1-t_n)/2\), then the characteristic function \(\chi(n)=1_{n\in E}\) satisfies
\[
\chi(0)=0,\quad \chi(2n+1)=0,\quad
\chi(4n)=\chi(n),\quad
\chi(8n+2)=T_n,\quad\chi(8n+6)=0.
\]
The same result states
\[
E=\{2^{2k+1}(4s+1):k,s\geq0,\ t_s=-1\}.
\]
All asymptotics below involve ordinary initial segments of nonnegative integers; no random model or averaging assumption is used.

## Proof
**1. Digit statistics.** The Thue–Morse relations \(t_{2m}=t_m\), \(t_{2m+1}=-t_m\) imply
\(\sum_{0\leq m<M}t_m=O(1)\), since even-length prefixes cancel in adjacent pairs. Put
\(C(M)=\sum_{0\leq m<M}t_mt_{m+1}\). Directly splitting the summands into even and odd indices gives
\[
C(2M)=-M-C(M),\qquad C(2M+1)=-M-C(M)-1.
\]
Consequently \(R(M)=C(M)+M/3\) obeys
\(R(2M)=-R(M)\) and \(R(2M+1)=-R(M)-2/3\). Iteration over binary digits gives \(R(M)=O(1+\log M)\). The four ordered pair frequencies of consecutive signs are therefore
\[
\begin{array}{c|rrrr}
(t_m,t_{m+1}) &(+,+)&(+,-)&(-,+)&(-,-)\\\hline
\text{frequency}&1/6&1/3&1/3&1/6
\end{array},
\]
with \(O(1+\log M)\) counting errors for initial segments. Additionally, the explicit description of \(E\) yields
\[
\#(E\cap[0,M))
=\sum_{k\geq0}\#\{s\geq0:2^{2k+1}(4s+1)<M,\ t_s=-1\}
=M/12+O(1+\log M).
\]
Indeed the \(k\)-th summand is \(M/2^{2k+4}+O(1)\); only logarithmically many \(k\)'s contribute.

**2. Sixteen-site blocks.** Every block \([16n,16n+16)\) has one of the following four patterns of occupied offsets, obtained *directly* from the displayed recurrences for \(\chi\):
\[
\begin{array}{c|l|l}
\text{type}&\text{condition on }n&\text{occupied offsets}\\\hline
A&\chi(n)=1&\{0,10\}\\
B&\chi(n)=0,\ T_n=0&\{10\}\\
C&n\text{ even},\ T_n=1&\{2,8\}\\
D&n\text{ odd},\ T_n=1&\{2\}
\end{array}.
\]
In particular, if \(n\) is even and \(T_n=0\), it is either \(A\) or \(B\). The block-type frequencies are
\[
\begin{array}{c|rrrrr}
\text{type}&A&B\text{ even}&B\text{ odd}&C&D\\\hline
\text{frequency}&1/12&1/6&1/4&1/4&1/4
\end{array}
\]
with \(O(1+\log M)\) initial-segment errors. Here \(A\) has frequency \(1/12\) by Step 1, and the other entries follow from parity and Thue–Morse cancellation.

**3. Adjacent block types.** An even-indexed block with \(T_n=0\) is followed by \(D\); a block of type \(C\) is followed by \(B\). For odd \(n=2m+1\), we have \(t_n=-t_m\) and \(t_{n+1}=t_{m+1}\). The pair frequencies in Step 1, together with \(A\)'s frequency, give the complete transition table:
\[
\begin{array}{c|rrrrrrrr}
\text{transition}&A\to D&B\to D&B\to A&B\to B&B\to C&C\to B&D\to C&D\to B\\\hline
\text{frequency}&1/12&1/6&1/12&1/12&1/12&1/4&1/6&1/12
\end{array}.
\]
The entries refer to transitions from blocks numbered \(n\) to \(n+1\). The only point requiring care is that \(A\) cannot follow \(D\): if \(n+1=2^{2k+1}(4s+1)\in E\), then its predecessor \(n\) is odd and
\(t_n=-t_{4s}=-t_s=+1\), hence the preceding block is \(B\), not \(D\). The remaining odd-to-even transitions are determined by the preceding ordered Thue–Morse sign-pair table. Each transition count has error \(O(1+\log M)\) up to block index \(M\).

**4. Gap counting.** An \(A\) block has one internal gap of length \(10\); a \(C\) block has one internal gap of length \(6\). Every pair of adjacent blocks contributes exactly one interblock gap (the last occupied offset of one to the first occupied offset of the next). The eight transition types, in the table order above, contribute interblock lengths
\[
8,\ 8,\ 6,\ 16,\ 8,\ 18,\ 16,\ 24.
\]
Summing internal and interblock contributions yields, **per block index**, the frequencies
\[
\begin{array}{c|rrrrrr}
g&6&8&10&16&18&24\\\hline
\text{gaps per block}&1/3&1/3&1/12&1/4&1/4&1/12
\end{array}.
\]
Each such count across the first \(M\) blocks has error \(O(1+\log M)\). Since \(M\) blocks contain asymptotically \(4M/3\) points (and therefore the same number of gap starts), the gap frequencies **per starting index** are the previous row divided by \(4/3\): exactly the six claimed \(p_g\). More precisely, Step 1 gives
\(\#(E\cap[0,X))=X/12+O(1+\log X)\). Apply the block count at \(X=16M\) and bound the at-most-two boundary points to obtain the stated cutoff law for arbitrary \(X\). Inverting the monotone count yields \(f_N=12N+O(1+\log(N+2))\), and replacing \(X\) by \(f_N\) proves the assertion for the first \(N\) consecutive gaps. Direct weighted sums of the six rational \(p_g\)'s give the asserted moments. \(\square\)

## Verification
The standalone `verify.py` reconstructs \(\chi\) from the explicit binary-digit condition and independently through the recurrences; it also computes binary-partition values and applies Legendre's three-square exclusion criterion. It enumerates gap and block patterns, checks transition counts, and evaluates discrepancies at dyadic cutoffs. The recorded program output is only finite corroboration. The unbounded conclusions and logarithmic errors come from the formal recurrences and counting argument above.

## Relationship to prior work
Sobolewski and Ulas, Corollary 3.3, supply the exact exceptional-index characterization, and their Proposition 3.4 already identifies all six possible gap lengths and their infinite occurrence. Their Theorem 6.1 supplies the exceptional set's density and quantitative discrepancy. These are antecedents, **not** new claims here. The additional result is the **complete probability vector and logarithmic discrepancy for every gap type**. It uses pair correlations of Thue–Morse signs and a full transition-multiplicity calculation; a statement that gaps merely belong to the six-element set does not determine those frequencies. OEIS A363769 tabulates initial exceptional indices but does not provide the all-index frequency law.

## Limitations
This analysis does not decide whether the ordered gap word is automatic, whether the limiting frequencies of longer prescribed gap patterns have a particular structure, or whether the logarithmic error can be improved for individual gap types. The novelty assessment is bounded by accessible literature and may be superseded by an unlocated equivalent specialization of an automatic-sequence result. This work has had no independent scientific audit.

## References
1. B. Sobolewski and M. Ulas, *Values of binary partition function represented by a sum of three squares*, arXiv:2211.16622, first version dated 29 November 2022; *Results in Mathematics* 78 (2023), article 188, https://doi.org/10.1007/s00025-023-01966-8. In particular, Corollary 3.3, Proposition 3.4, Remark 3.5, and Theorem 6.1.
2. OEIS A363769, indices \(n\) for which \(b(2n)\) is not a sum of three squares, https://oeis.org/A363769.
3. OEIS A363770, exceptional indices for \(b(n)\), https://oeis.org/A363770.
