# Dyadic Thue–Morse shortest-absent-subsequence recurrence and entropy

## Finding
Let \(\tau_i\) be the parity of the number of ones in the binary expansion of \(i\), and let \(T_m=\tau_0\tau_1\cdots\tau_{2^m-1}\). For every integer \(m\ge1\), let \(A_m\) count distinct **shortest absent subsequences** of \(T_m\) over the ambient alphabet \(\{0,1\}\). Then every shortest absent subsequence has length \(2^{m-1}+1\), and
\[
\begin{gathered}
s_0=1,\quad t_0=2,\\
s_{r+1}=s_rt_r,\qquad t_{r+1}=s_r^2+2\quad(r\ge0),\\
A_m=s_{m-1}+t_{m-1}.
\end{gathered}
\]
This gives \(A_1,\ldots,A_7=3,5,12,74,2666,3647090,6476006417762\). In addition,
\[
\begin{aligned}
\lambda&=\lim_{m\to\infty}\frac{\log_2 A_m}{2^{m-1}}\\
&=\frac13+\sum_{j=0}^{\infty}\frac{\log_2(1+2/s_j^2)}{3\cdot2^{j+1}}\\
&=0.649537093097466\ldots,
\end{aligned}
\]
and \(\log_2 A_m=\lambda\,2^{m-1}+O(1)\). Per symbol of \(T_m\), the logarithmic exponent is \(\lambda/2=0.324768546548733\ldots\).

## Assumptions and scope
A subsequence is obtained by deleting zero or more positions while preserving the order of the remaining symbols; it need not be contiguous. Two candidate subsequences are counted once when their binary strings agree. Absent means not a subsequence of the indicated finite source word. The source is the standard Thue–Morse fixed point of \(0\mapsto01\) and \(1\mapsto10\), with its prescribed left-to-right order; neither arbitrary permutations of blocks nor other codings are included. Indices satisfy \(m\ge1\) and \(r\ge0\). The logarithm in the limit is base two.

## Proof
Write \(k=2^{m-1}\). The word \(T_m\) is the concatenation of \(k\) binary blocks of length two, with block \(j\) equal to \(\tau_j(1-\tau_j)\) for \(0\le j<k\). In particular, each block contains both letters. Every binary word of length \(k\) is therefore a subsequence by selecting the \(j\)-th letter (indexed from zero) from block \(j\) for \(0\le j<k\). However, \(T_m\) contains exactly \(k\) zeros, so \(0^{k+1}\) is absent. The shortest absent length is precisely \(k+1\).

Let \(v=v_0\cdots v_k\) be an arbitrary binary string of that length. Perform greedy subsequence matching in the sequence of length-two blocks. If a block consumes two required letters, the \(k\) blocks can jointly consume at least \(k+1\) letters: before that block each earlier block consumes at least one, and each later block can also consume at least one because it contains both letters. Conversely, if none consumes two letters, exactly \(k\) letters are consumed and the last is unmatched. Before the first two-letter consumption, block \(j\) starts from required symbol \(v_j\). Consequently block \(j\) consumes two letters precisely when the ordered adjacent pair \(v_jv_{j+1}\) equals the block \(\tau_j(1-\tau_j)\). Thus **the absent strings are exactly those that avoid the length-two pattern prescribed at each successive boundary**, in the sense that \(v_jv_{j+1}\ne\tau_j(1-\tau_j)\) for every \(0\le j<k\).

Use row indices for \(v_j\) and column indices for \(v_{j+1}\). For a prescribed block \(01\), the three allowed pairs yield
\[
M_0=\begin{pmatrix}1&0\\1&1\end{pmatrix};
\]
for a prescribed block \(10\), they yield
\[
M_1=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
Define \(P_r=M_{\tau_0}M_{\tau_1}\cdots M_{\tau_{2^r-1}}\), and \(J=\begin{pmatrix}0&1\\1&0\end{pmatrix}\). The number of permitted paths equals the sum of the entries of \(P_{m-1}\), so
\[
A_m=\operatorname{tr}(P_{m-1})+\operatorname{tr}(P_{m-1}J).
\]
Put \(t_r=\operatorname{tr}(P_r)\) and \(s_r=\operatorname{tr}(P_rJ)\). Because \(P_0=M_0\), we have \((s_0,t_0)=(1,2)\). The Thue–Morse substitution obeys \(T_{r+1}=T_r\overline{T_r}\). Since \(JM_0J=M_1\), \(JM_1J=M_0\), we obtain
\[
P_{r+1}=P_rJP_rJ=(P_rJ)^2.
\]
The matrix \(P_rJ\) has determinant \(-1\) (each \(M_b\) has determinant one and \(\det J=-1\)). Cayley–Hamilton in dimension two then gives
\[
(P_rJ)^2=s_r(P_rJ)+I.
\]
Taking ordinary traces yields \(t_{r+1}=s_r^2+2\). Taking traces after multiplying on the right by \(J\) yields \(s_{r+1}=s_rt_r\), because \(\operatorname{tr}(J)=0\). This establishes the exact integer recurrence and \(A_m=s_{m-1}+t_{m-1}\) for all indicated indices.

For the limit, set \(a_r=\log_2 s_r\) and \(\varepsilon_r=\log_2(1+2/s_r^2)\). The recurrence entails
\[
a_0=0,\quad a_1=1,\qquad a_{r+2}=a_{r+1}+2a_r+\varepsilon_r.
\]
Solving the forced second-order recurrence with characteristic roots \(2\) and \(-1\) gives the exact identity
\[
a_r=\frac{2^r-(-1)^r}{3}+\sum_{j=0}^{r-2}\frac{2^{r-j-1}+(-1)^{r-j-2}}{3}\,\varepsilon_j
\]
(the sum is empty for \(r=0,1\)). Since \(t_r\ge2\), the first recurrence implies \(s_r\ge2^r\), so
\[
0\le\varepsilon_r\le\frac{2}{\ln2}\,4^{-r}.
\]
Therefore the indicated positive series for \(\lambda=\lim a_r/2^r\) converges absolutely, and the displayed finite identity implies \(a_r=\lambda2^r+O(1)\): its alternating correction is bounded, and its omitted series tail contributes \(O(2^r8^{-r})\). Finally, \(t_r=s_{r+1}/s_r\), hence
\[
\log_2t_r=a_{r+1}-a_r=\lambda2^r+O(1).
\]
For positive \(s_r,t_r\), the logarithm of their sum differs from the maximum logarithm by at most one; therefore \(\log_2(s_r+t_r)=\lambda2^r+O(1)\). Substituting \(r=m-1\) proves the claimed limit and asymptotic.

## Verification
The standalone `verify.py` implements four distinct calculations: the explicit two-integer recurrence; independent direct triangular-matrix multiplication; direct enumeration of every possible missing subsequence and direct greedy membership checking for \(m=1,\dots,5\); and distinct-subsequence dynamic programming with last-occurrence correction for \(m=1,\dots,9\). All three independent checks reproduce the recurrence's exact counts on their stated ranges. Invoke `python3 verify.py` in the directory containing this file; the last line is `ALL CHECKS PASS`. The infinite theorem rests on the proof above, not on finite verification. The numerical series can be evaluated by iterating \((s_r,t_r)\); its tail has the explicit geometric bound in the proof.

## Relationship to prior work
Kosche, Koß, Manea, and Siemer introduced systematic study of shortest absent subsequences and binary arch decompositions in *Absent Subsequences in Words* (2021). Their general characterization subsumes the membership framework used above but does not state the dyadic Thue–Morse recursion or entropy value. Adamson and coauthors (2024) study sharp bounds and enumeration of absent subsequences for fixed universality index, but not the complete count of shortest absent subsequences on the canonical dyadic Thue–Morse prefixes.

A separately published result titled *Fibonacci extremals for shortest absent subsequences of binary words* derives **the same two triangular transition matrices** for binary 01/10 block words and extremizes their products over the choice of blocks. Thus the transition-matrix representation itself is not claimed as new. Its fixed-length global Fibonacci maximum does not specify the Thue–Morse product, its quadratic renormalization, or its particular asymptotic exponent. The contribution here is the complete Thue–Morse-specific two-integer dynamics together with its explicit limiting entropy; the general transfer idea is prior work. A second published note on the *Closed-form law for binary subsequence universality* enumerates all binary words by their universality index, a different statistic from the number of shortest absent subsequences of a prescribed word.

## Limitations
The recurrence applies to binary dyadic Thue–Morse prefixes, not arbitrary prefix lengths, alphabets, or minimal absent subsequences of unrestricted lengths. The comparison with known universal matrix-transfer formulas is essential: the result is a specialization with an additional nontrivial self-similar trace law, not a newly invented transfer formalism. The primary literature and searched mathematical records did not supply this exact recurrence and entropy, but an older equivalent trace-map or continued-fraction formulation could exist outside the inspected sources. No independent mathematical audit is claimed.

## References
1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968v1 (first submitted 2021-08-31), https://arxiv.org/abs/2108.13968.
2. D. Adamson et al., *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599 (first submitted 2024-07-26), https://arxiv.org/abs/2407.18599.
3. *Fibonacci extremals for shortest absent subsequences of binary words*, research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-fibonacci-extremals-for-shortest-absent-subsequences-of-binary-w--1a6556f14d28.
4. *Closed-form law for binary subsequence universality*, research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37.
