# Nonlinear shortest-absent-subsequence law for dyadic Thue–Morse words

## Finding
Let \(T_m\) be the length-\(2^m\) binary word \(\mu^m(0)\), with \(\mu(0)=01\) and \(\mu(1)=10\). For \(m\ge1\), let \(H_m\) denote the **number of distinct shortest absent scattered subsequences** of \(T_m\), where a scattered subsequence need not use consecutive positions and the underlying alphabet is \(\{0,1\}\). All such absent words have length \(2^{m-1}+1\).

Define a positive integer sequence by
\[
a_0=1,\quad a_1=2,\qquad a_{j+2}=a_{j+1}(a_j^2+2)\quad (j\ge0).
\]
Then the exact count for **every** \(m\ge2\) is
\[
\boxed{H_m=a_{m-1}+a_{m-2}^{\,2}+2},\qquad H_1=3.
\]
The initial values for \(m=1,\ldots,7\) are
\[
3,\quad5,\quad12,\quad74,\quad2666,\quad3647090,\quad6476006417762.
\]
Moreover, the following asymptotic base exists:
\[
\lim_{m\longrightarrow\infty}H_m^{\,1/2^{m-1}}=\rho,
\qquad
\log\rho=\frac13\left(\log 2+\sum_{j\ge0}\frac{\log(1+2/a_j^2)}{2^{j+1}}\right).
\]
The convergent series yields \(\rho\approx1.5686647891503443<2\). Thus among all \(2^{2^{m-1}+1}\) binary words of the shortest absent length, the absent proportion decays exponentially in \(2^{m-1}\), with an exact exponential rate.

## Assumptions and scope
A word \(v=v_1\cdots v_r\) is a scattered subsequence of \(w\) when some strictly increasing positions \(i_1<\cdots<i_r\) satisfy \(v_j=w_{i_j}\). An absent subsequence is one which is not represented in this way; shortest means minimum length among absent words. The count is of literal binary words, not occurrence multiplicities or equivalence classes. The theorem concerns the finite, one-sided substitution iterates \(T_m\) for all integers \(m\ge1\), not all factors of the infinite fixed point.

For a binary word \(x=x_1\cdots x_k\), write \(E(x)=x_1\overline{x_1}\cdots x_k\overline{x_k}\), where \(\overline0=1\) and \(\overline1=0\). Each consecutive complementary pair is a complete binary alphabet. Therefore \(E(x)\) contains every binary word of length \(k\) as a subsequence (one selected symbol from each pair), but has only \(k\) occurrences of \(0\), so \(0^{k+1}\) is absent. Its shortest absent subsequences have length exactly \(k+1\). Since \(T_m=E(T_{m-1})\), this applies with \(k=2^{m-1}\).

## Proof
**1. Alignment lemma.** For any \(x\in\{0,1\}^k\) and \(v\in\{0,1\}^{k+1}\),
\[
v\text{ is a subsequence of }E(x)
\quad\Longleftrightarrow\quad
\exists j\in\{1,\ldots,k\}: (v_j,v_{j+1})=(x_j,\overline{x_j}).
\]
The reverse implication embeds the indicated adjacent pair in complementary block \(j\), every earlier letter in one block to its left, and every later letter in one block to its right.

For the forward implication, choose any subsequence embedding. Let \(e_i\in\{1,\ldots,k\}\) be the complementary block containing its \(i\)-th selected symbol. Then the block indices are nondecreasing, \(e_1-1\ge0\), and \(e_{k+1}-(k+1)\le-1\). Whenever \((e_{i+1}-(i+1))-(e_i-i)<0\), the block index has not advanced, so the difference equals \(-1\). At the first crossing from nonnegative to negative, necessarily \(e_i=i=e_{i+1}\). Both positions of block \(i\) must then have been selected, in their natural order. Hence the displayed adjacent-pair equality holds.

**2. An exact matrix product.** By the lemma, a word of length \(k+1\) is absent exactly when it avoids the transition \(0\to1\) at every index \(j\) with \(x_j=0\), and avoids \(1\to0\) at every index \(j\) with \(x_j=1\). With rows and columns indexed by \(0,1\), the corresponding allowed-transition matrices are
\[
A_0=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad
A_1=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
If \({\bf1}=(1,1)^{\mathsf T}\), the exact absent count for \(E(x)\) equals \({\bf1}^{\mathsf T}A_{x_1}\cdots A_{x_k}{\bf1}\). In particular, let \(P_j=A_{t_1}\cdots A_{t_{2^j}}\) for \(T_j=t_1\cdots t_{2^j}\); then \(H_m={\bf1}^{\mathsf T}P_{m-1}{\bf1}\).

**3. Renormalization and scalar recurrence.** Put \(J=\begin{pmatrix}0&1\\1&0\end{pmatrix}\). Since \(A_{\overline b}=JA_bJ\) and \(T_{j+1}=T_j\overline{T_j}\),
\[
P_0=A_0,\qquad P_{j+1}=P_jJP_jJ.
\]
Each \(P_j\) is unimodular with determinant \(1\). Write \(P_j=\begin{pmatrix}u_j&v_j\\w_j&z_j\end{pmatrix}\), and set \(d_j=u_j+z_j\), \(s_j=v_j+w_j\). The matrix \(P_jJ\) has trace \(s_j\) and determinant \(-1\). By its characteristic equation, \((P_jJ)^2=s_j(P_jJ)+I\), so
\[
P_{j+1}=s_jP_jJ+I,\qquad
 d_{j+1}=s_j^2+2,\qquad s_{j+1}=s_jd_j.
\]
The initial values are \(d_0=2,s_0=1\). Hence \(s_1=2\), \(s_{j+2}=s_{j+1}(s_j^2+2)\), and \(s_j=a_j\) for all \(j\ge0\). For \(m\ge2\), \(H_m=d_{m-1}+s_{m-1}=2+a_{m-2}^2+a_{m-1}\), as claimed; \(H_1=d_0+s_0=3\).

**4. Exponential rate.** Let \(b_j=\log(a_ja_{j+1})\). The exact nonlinear recurrence gives
\[
 b_{j+1}=2b_j+\log(1+2/a_j^2),\qquad b_0=\log 2.
\]
Therefore \(2^{-j}b_j\) increases to the finite limit
\[
L=\log2+\sum_{i\ge0}2^{-i-1}\log(1+2/a_i^2),
\]
because \(0\le\log(1+2/a_i^2)\le\log3\). Setting \(v_j=2^{-j}\log a_j\) gives the contractive relation
\[
v_{j+1}=\tfrac12\bigl(2^{-j}b_j-v_j\bigr),
\]
whose limit is \(L/3\). Since \(d_j=a_{j-1}^2+2\) for \(j\ge1\), both \(2^{-j}\log d_j\) and \(2^{-j}\log s_j\) tend to \(L/3\). Consequently \(2^{-j}\log(d_j+s_j)\to L/3\). Taking \(j=m-1\) proves the displayed asymptotic rate. Finally \(L\le\log6<3\log2\), which rigorously gives \(\rho<2\).

## Verification
The standalone, standard-library-only file `verify.py` is run with `python3 verify.py`. It checks the alignment lemma by exhaustive enumeration for all binary block specifications through seven blocks; constructs dyadic words by both digit parity and repeated substitution; counts absent subsequences through direct enumeration for the first five nontrivial substitution blocks; and compares two further independent exact counting implementations—greedy-subsequence state dynamics and matrix multiplication—with the scalar recurrence through \(m=9\). The code also recomputes the exponential-rate constant with an explicit monotone tail bound.

Successful execution prints:
`VERIFY_OK ThueMorse-SAS: arbitrary_complementary_arches_k<=7; two_generators_m<=9; three_count_engines_m<=9; direct_absent_subsequences_m<=5; exact_nonlinear_recurrence; rho_in_[1.568664789150, 1.568664789150]`

The finite tests support the argument but do not establish the infinite result; the complete proof is the alignment lemma, substitution-matrix identity, and scalar recurrence above.

## Relationship to prior work
The early study of scattered-subsequence statistics of the Thue–Morse word includes Rigo and Salimov's 2013 work on binomial equivalence. It counts multiplicities of fixed short subsequences among **contiguous factors**, a different invariant from the number of shortest absent subsequences of finite dyadic prefixes.

Kosche, Koß, Manea, and Siemer (first publicly available in 2021) established the shortest-absent-subsequence framework, arch factorization, and a gluing principle for concatenated 1-universal components. A subsequently available result on Fibonacci extremals for binary shortest absent subsequences evaluates a maximizing choice of binary arches using the same matrices. Those general transfer tools are prior; the new contribution here is the **nonperiodic Thue–Morse product evaluation** in a two-term nonlinear integer recurrence and its explicit sub-binary exponential growth constant for every dyadic prefix. These claims do not follow from the Fibonacci maximum alone; the specific substitution and its unimodular renormalization are required.

## Limitations
The result counts shortest absent scattered subsequences, not all minimal absent subsequences or absent contiguous factors. It concerns dyadic Thue–Morse prefixes only and does not claim a formula for arbitrary prefix lengths. The transfer matrices are classical prior tools, not a new generic subsequence algorithm. Existing results on automatic matrix products may admit equivalent formulations; the inspected papers and accessible indexed searches did not identify this exact Thue–Morse recurrence or exponential constant. Independent mathematical validation has not been performed.

## References
1. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words* (author preprint publicly available 27 May 2013), https://orbi.uliege.be/handle/2268/149313 .
2. M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968v1, first submitted 31 August 2021; *Fundamenta Informaticae* 189 (2023), 199–240, https://fi.episciences.org/12396 .
3. *Fibonacci extremals for shortest absent subsequences of binary words*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-fibonacci-extremals-for-shortest-absent-subsequences-of-binary-w--1a6556f14d28 .
4. OEIS A010060, *Thue–Morse sequence*, https://oeis.org/A010060 .
