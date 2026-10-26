# Exact mean and universality-index distribution of shortest absent subsequences in binary words

## Finding
Fix the ambient alphabet \(\Sigma=\{0,1\}\). For a finite binary word \(w\), let \(\iota(w)\) be the largest nonnegative integer such that every binary word of length \(\iota(w)\) occurs as a scattered subsequence of \(w\). Let \(s(w)\) be the number of **distinct strings** of length \(\iota(w)+1\) that are absent as scattered subsequences of \(w\). These are the shortest absent subsequences, counted as strings rather than positional realizations. Define the bivariate weighted enumeration
\[
H(z,u)=\sum_{w\in\{0,1\}^{*}}s(w)z^{|w|}u^{\iota(w)}.
\]
Then the following identity holds as a formal power series:
\[
\boxed{H(z,u)=\frac{2}{1-z-uz^2(3-z)}.}
\]
In particular, for integers \(n,k\ge0\), setting
\[
T_{n,k}=\sum_{\substack{w\in\{0,1\}^{n}\\\iota(w)=k}}s(w),
\]
we have \(T_{n,k}=0\) when \(n<2k\), and otherwise
\[
\boxed{T_{n,k}=2\sum_{j=0}^{\min(k,n-2k)}(-1)^j\binom{k}{j}3^{k-j}\binom{n-k-j}{k}.}
\]
Consequently, at length \(2k\), the aggregate is \(T_{2k,k}=2\cdot3^k\), and the conditional mean among the \(2^k\) words with \(k\) arches is \(2(3/2)^k\).

Let \(T_n=\sum_{w\in\{0,1\}^n}s(w)\). Its ordinary generating function and recurrence are
\[
\boxed{\sum_{n\ge0}T_nz^n=\frac{2}{1-z-3z^2+z^3}},
\]
\[
T_0=2,\quad T_1=2,\quad T_2=8,\qquad
\boxed{T_{n+3}=T_{n+2}+3T_{n+1}-T_n\quad(n\ge0).}
\]
The initial values are \(2,2,8,12,34,62,152,304,698,1458\).

For uniform independent fair binary letters and a length-\(n\) random word \(W_n\), let \(r\) be the unique root in \((0,1/2)\) of \(1-z-3z^2+z^3=0\). Put \(\lambda=1/r\), and \(Q(z)=1-z-3z^2+z^3\). Then
\[
\boxed{\mathbb E[s(W_n)]\sim
\frac{-2}{rQ'(r)}\left(\frac{\lambda}{2}\right)^n.}
\]
Numerically, \(\lambda\approx2.17008648662603\), \(\lambda/2\approx1.08504324331302\), and the positive prefactor is approximately \(1.38760048180046\). Thus the **mean number of shortest absent subsequence strings grows exponentially**, despite the universality index itself growing only linearly.

## Assumptions and scope
The ambient alphabet is always exactly \(\{0,1\}\), even if \(w\) is unary or empty. In particular, \(s(\varepsilon)=2\); each nonempty unary word has \(s(w)=1\). A scattered subsequence may omit arbitrary positions but must preserve order. The sum defining \(H\) is over all labeled binary source words; it does not identify words up to reversal or complementation. Variables \(z,u\) are formal, and \(n,k\) are nonnegative integers. The asymptotic is for the uniform independent binary source, not a biased source or an arbitrary larger alphabet.

## Proof
**Greedy arches and universality.** Repeatedly remove the shortest nonempty prefix containing both binary symbols. Such a prefix is a *greedy arch*, necessarily of the form \(a^m\bar a\), where \(a\in\{0,1\}\), \(m\ge1\), and \(\bar a\) is the opposite symbol. When no further arch exists, the remaining suffix is empty or unary. Hence each word admits a unique decomposition
\[
w=a_1^{m_1}\bar a_1\cdots a_k^{m_k}\bar a_kv,
\]
where \(v\) is empty or unary. The number of arches is \(\iota(w)=k\). One direction follows because choosing one symbol from each successive arch embeds any binary word of length \(k\); the other follows because the rest is missing one symbol, and the standard greedy-arch universality characterization proves no \((k+1)\)-universal embedding is possible.

**A first-letter-resolved transfer.** Define the column vector
\[
S(w)=\begin{pmatrix}s_0(w)\\s_1(w)\end{pmatrix},
\]
where \(s_a(w)\) counts shortest absent subsequence strings whose first letter is \(a\). For a word \(w=a^m\bar av\) starting with one complete arch, put \(j=\iota(v)\). Shortest absent strings of \(w\) have length \(j+2\). If a candidate begins with \(\bar a\), its first greedy match occurs at the last letter of the first arch, leaving the source suffix \(v\). Therefore it is absent precisely when its remaining length-\((j+1)\) word is absent from \(v\), and
\[
s_{\bar a}(w)=s_0(v)+s_1(v).
\]
If a candidate begins with \(a\), its first greedy match is at the first position, leaving \(a^{m-1}\bar av\). When \(m\ge2\), this suffix contains an entire new arch followed by the \(j\) arches of \(v\), and therefore contains every binary subsequence of length \(j+1\). No length-\((j+2)\) candidate beginning with \(a\) can be absent; thus \(s_a(w)=0\).

When \(m=1\), the suffix after the first \(a\) is \(\bar av\). Every length-\((j+1)\) word beginning with \(\bar a\) occurs in \(\bar av\), because the remaining \(j\) symbols occur in \(v\). For a length-\((j+1)\) word beginning with \(a\), its greedy match in \(\bar av\) starts in \(v\), and it occurs in \(\bar av\) exactly when it occurs in \(v\). Therefore the absent suffixes of \(\bar av\) are exactly the length-\((j+1)\) shortest absent subsequences of \(v\) beginning with \(a\), and \(s_a(w)=s_a(v)\).

It follows that, for \(m=1\), the two possible leading arches act on \(S(v)\) through
\[
A_{01}=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad
A_{10}=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\]
and, for each \(m\ge2\), through
\[
B_{0^m1}=\begin{pmatrix}0&0\\1&1\end{pmatrix},\qquad
B_{1^m0}=\begin{pmatrix}1&1\\0&0\end{pmatrix}.
\]
This transfer is exact, not merely an upper bound; it also holds when \(v\) is empty or unary.

**Summing all arches.** Mark every arch by \(u\) and every source letter by \(z\). The weighted transfer matrix summed over all possible leading arches is
\[
\begin{aligned}
\mathcal T(z,u)
&=uz^2(A_{01}+A_{10})
 +u\sum_{m\ge2}z^{m+1}(B_{0^m1}+B_{1^m0})\\
&=u\left[z^2\begin{pmatrix}2&1\\1&2\end{pmatrix}
 +\frac{z^3}{1-z}\begin{pmatrix}1&1\\1&1\end{pmatrix}\right].
\end{aligned}
\]
For an empty word, \(S(\varepsilon)=(1,1)^{\mathsf T}\). For a positive unary word of zeros, \(S=(0,1)^{\mathsf T}\), and for a positive unary word of ones, \(S=(1,0)^{\mathsf T}\). Summing the residual contributions gives
\[
\mathcal B(z)=\sum_{\substack{v\text{ empty}\\\text{or unary}}}z^{|v|}S(v)
 =\frac{1}{1-z}\begin{pmatrix}1\\1\end{pmatrix}.
\]
The vector \((1,1)^{\mathsf T}\) is an eigenvector of \(\mathcal T\), with eigenvalue
\[
\eta(z,u)=u\left(3z^2+\frac{2z^3}{1-z}\right)
 =\frac{uz^2(3-z)}{1-z}.
\]
All leading arches contribute a factor of degree at least two in \(z\), so the formal series \((I-\mathcal T)^{-1}=\sum_{k\ge0}\mathcal T^k\) is well-defined. Summing both coordinates therefore yields
\[
\begin{aligned}
H(z,u)
&=(1,1)(I-\mathcal T(z,u))^{-1}\mathcal B(z)\\
&=\frac{2}{1-z}\frac{1}{1-uz^2(3-z)/(1-z)}\\
&=\frac{2}{1-z-uz^2(3-z)}.
\end{aligned}
\]

**Coefficient extraction.** Taking coefficient of \(u^k\) gives
\[
[u^k]H(z,u)=\frac{2z^{2k}(3-z)^k}{(1-z)^{k+1}}.
\]
Expand \((3-z)^k\) by the binomial theorem and use \([z^m](1-z)^{-k-1}=\binom{m+k}{k}\) for \(m\ge0\). This produces exactly the stated \(T_{n,k}\) finite sum, including the zero range \(n<2k\). Taking \(u=1\) gives \(2/Q(z)\) and the all-length recurrence by matching coefficients.

**Mean exponential growth.** The cubic \(Q(z)=1-z-3z^2+z^3\) has exactly three real roots, one in \((-1,-1/2)\), one in \((0,1/2)\), and one in \((3,4)\), by the respective sign changes and the degree bound. Hence the positive root \(r\in(0,1/2)\) is the unique pole of smallest modulus, and it is simple. The partial-fraction contribution of that pole is
\[
\frac{-2}{rQ'(r)}r^{-n},
\]
while contributions of the other two roots are exponentially smaller. There are \(2^n\) equiprobable source words, so dividing by \(2^n\) proves the asserted asymptotic mean. Because \(r<1/2\), its base \(1/(2r)\) is strictly greater than one.

## Verification
The standalone pure-Python program `verify.py` constructs actual sets of distinct scattered subsequences by length and counts missing words of length \(\iota(w)+1\) from the binary pattern universe; it does not use the matrix formulas to obtain these observations. It exhaustively checks all \(32,767\) binary words of lengths \(0\) through \(14\), compares all \(64\) permissible \((n,k)\) cells with the coefficient formula, and checks \(8,166\) individual first-arch transfer instances against those independently constructed sets. Separately it verifies the scalar recurrence through index \(60\) and checks the initial coefficients through length \(16\). Successful execution prints `VERIFY_OK complete_words=32767 max_length=14 one_arch_transfers=8166 bivariate_cells=64 scalar_recurrence_through=60`.

These bounded checks detect many possible algebraic or convention errors. They do not certify the statements for arbitrarily long source words; that conclusion comes from the formal-power-series proof above.

## Relationship to prior work
Kosche, Koß, Manea, and Siemer introduced shortest absent subsequences and developed their greedy-arch characterization and gluing machinery. Fleischmann and collaborators studied how many length-\(k\) subsequences a given source word omits. Adamson and collaborators obtained bounds on numbers of absent subsequences at prescribed universality indices. These are the mathematical foundations and nearby comparison objects, but the inspected statements do not supply the all-source-word weighted sum \(H(z,u)\), the exact bivariate total \(T_{n,k}\), or its random-source exponential growth rate.

The pre-existing OEIS entry **A087955** has terms \(1,2,2,8,12,34,62,\ldots\) and the same third-order recurrence, derived there from a different nonlinear partial-sum construction. In fact, if \(a(n)\) is that listed sequence, then \(T_n=a(n+1)\). Thus the scalar recurrence and its numeric series are **not claimed to be new integer-sequence data**. The new mathematical assertion is the binary shortest-absent-subsequence interpretation together with the exact two-variable, universality-refined identity, for which the OEIS entry supplies no stated implication.

The published *Closed-form law for binary subsequence universality* gives an **unweighted** length/index enumerator \((1+z)/(1-z-2uz^2)\), whereas the present sum weights every word by its number of shortest absent strings; the difference is substantive because that number varies among words at the same length and universality index (for instance, source words `0101` and `0110` each have index two but have four and five shortest absent subsequences, respectively). The published *Fibonacci extremals for shortest absent subsequences of binary words* maximizes the count across source words of each length, rather than summing it over every source word. Neither formula implies the stated weighted mean by substitution alone. The transfer method has antecedents in both lines of work; the claim here is the exact **summatory** law and its consequences, not invention of arch decomposition or the underlying SAS machinery.

## Limitations
The theorem assumes a fixed two-letter ambient alphabet; changing the alphabet convention for unary or empty words changes boundary terms. The explicit exponential mean is derived only for a uniform binary source, and a growing mean alone does not describe concentration or typical behavior. Earlier literature contains closely related matrix and arch methods, making independent derivation of this particular summatory formula possible; the comparison of inspected sources and searchable records is not proof of global novelty.

## References
1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968v1 (first public 2021-08-31). https://arxiv.org/abs/2108.13968
2. P. Fleischmann, L. Haschke, A. Huch, A. Mayrock, D. Nowotka, *m-Nearly k-Universal Words — Investigating Simon Congruence*, arXiv:2202.07981v1 (first public 2022-02-16). https://arxiv.org/abs/2202.07981
3. P. Fleischmann, J. Höfer, A. Huch, D. Nowotka, *α-β-Factorization and the Binary Case of Simon's Congruence*, arXiv:2306.14192v1 (first public 2023-06-25). https://arxiv.org/abs/2306.14192
4. D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599v1 (first public 2024-07-26). https://arxiv.org/abs/2407.18599
5. *Closed-form law for binary subsequence universality*, public research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37
6. *Fibonacci extremals for shortest absent subsequences of binary words*, public research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-fibonacci-extremals-for-shortest-absent-subsequences-of-binary-w--1a6556f14d28
7. OEIS Foundation, *A087955*, https://oeis.org/A087955 (record originating 2003).
