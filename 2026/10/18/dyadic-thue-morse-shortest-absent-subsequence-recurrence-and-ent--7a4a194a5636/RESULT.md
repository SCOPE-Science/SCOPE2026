# Entropy and alternating leading constants for shortest absent subsequences of Thue–Morse prefixes

## Finding

Let \(T_m\) be the standard binary Thue–Morse prefix of length \(2^m\), and let \(A_m\) count its distinct shortest absent binary scattered subsequences, for \(m\ge1\). Write \(r=m-1\). Define the positive integers \(s_0=1,t_0=2\), \(s_{j+1}=s_jt_j\), \(t_{j+1}=s_j^2+2\), and put \(\varepsilon_j=\log_2(1+2/s_j^2)\). Set
\[
\lambda=\frac13+\sum_{j\ge0}\frac{\varepsilon_j}{3\cdot2^{j+1}},\qquad
C=\frac13\sum_{j\ge2}(-1)^j\varepsilon_j.
\]
Both series converge absolutely, and \(C>0\). With \(u=2^C\), the count has two different leading constants at the same exponential rate:
\[
\frac{A_{r+1}}{2^{\lambda 2^r}}=
\begin{cases}
u+u^{-2}+O(4^{-r}),&r\text{ even},\\
u^{-1}+u^2+O(4^{-r}),&r\text{ odd}.
\end{cases}
\]
In particular, the base-two logarithmic growth per symbol of \(T_m\) is \(\lambda/2=0.324768546548733\ldots\), but there is no single leading constant for the full sequence \(A_m\) at this rate. The exact count recurrence is an input to this asymptotic, not a separate novelty claim.

## Assumptions and scope

The alphabet is \(\{0,1\}\), and different embeddings of the same string count only once. A subsequence preserves order but need not be contiguous. Here \(T_0=0\), \(T_{m+1}=\mu(T_m)\), where \(\mu(0)=01\) and \(\mu(1)=10\). Thus \(T_m\) has bits given by parity of binary digit sum, and \(T_{m+1}=T_m\overline{T_m}\) with bitwise complement. The theorem concerns dyadic prefixes of this word only; it is not an asymptotic for absent factors or for minimal absent subsequences of all lengths.

## Proof

**Count recurrence.** Write \(k=2^{m-1}\). The prefix \(T_m\) consists of \(k\) ordered blocks \(01\) or \(10\). Every length-\(k\) word embeds by taking one symbol per block, but the prefix has only \(k\) zeros, so the shortest absent length is \(k+1\). For a candidate \(v=v_0\cdots v_k\), greedy matching must consume at least one symbol in each block until the candidate is exhausted. If some block consumes two, the candidate is fully matched by the end. Until the first such double consumption, the upcoming required pair at block \(j\) is \(v_jv_{j+1}\), which the block consumes exactly when that pair equals the block. Thus \(v\) is absent precisely when every pair differs from the block at its corresponding index.

For a block \(01\) or \(10\) the allowed pair matrices in the state order \((0,1)\) are
\[
M_0=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad M_1=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
Let \(P_r\) be the product of these matrices along the bits of \(T_r\), in their written order, and \(J=\begin{pmatrix}0&1\\1&0\end{pmatrix}\). The sum of the entries of \(P_r\) is \(A_{r+1}=s_r+t_r\), where \(s_r=\operatorname{tr}(P_rJ)\) and \(t_r=\operatorname{tr}(P_r)\). Because \(JM_0J=M_1\) and \(T_{r+1}=T_r\overline{T_r}\), one has \(P_{r+1}=(P_rJ)^2\). The determinant of \(P_rJ\) is \(-1\); Cayley–Hamilton gives \(P_{r+1}=s_rP_rJ+I\). Taking traces with and without a final \(J\) yields the two updates in the Finding, with the initial values from \(P_0=M_0\).

**Entropy and the leading constants.** Put \(a_r=\log_2 s_r\). The updates imply \(a_0=0,a_1=1\) and
\[
a_{r+2}=a_{r+1}+2a_r+\varepsilon_r.
\]
The roots of the homogeneous recurrence are \(2\) and \(-1\), so substitution, or convolution with the impulse response, gives
\[
a_r=\frac{2^r-(-1)^r}{3}
+\sum_{j=0}^{r-2}\frac{2^{r-j-1}+(-1)^{r-j-2}}{3}\varepsilon_j.
\]
The sum is empty for \(r=0,1\). Since \(t_j\ge2\), \(s_j\ge2^j\), hence \(0<\varepsilon_j\le (2/\ln 2)4^{-j}\). Extending both sums to infinity gives
\[
a_r=\lambda 2^r+(-1)^r C+O(4^{-r}).
\]
Indeed, the leading-mode tail is \(O(2^r8^{-(r-1)})\) and the alternating-mode tail is \(O(4^{-(r-1)})\). The alternating coefficient is \((-1+\sum_{j\ge0}(-1)^j\varepsilon_j)/3\). Since \(\varepsilon_0-\varepsilon_1=\log_2 3-\log_2(3/2)=1\), this is the stated \(C\). The \(s_j\) are strictly increasing, hence the \(\varepsilon_j\) strictly decrease; grouping the terms of the tail in pairs starting at \(j=2\) shows \(C>0\).

Now \(\log_2 t_r=a_{r+1}-a_r=\lambda 2^r-2(-1)^r C+O(4^{-r})\). Exponentiating and adding the two terms in \(A_{r+1}=s_r+t_r\) yields the displayed ratio. Its odd limit minus its even limit is
\[
(u-u^{-1})(u+u^{-1}-1)>0.
\]
The exact asymptotic therefore cannot be written with one constant times \(2^{\lambda 2^r}\) and relative error tending to zero.

## Verification

The accompanying `verify.py` checks the integer count recurrence by direct transfer-matrix products, short-word greedy membership enumeration, and distinct-subsequence dynamic programming on bounded dyadic prefixes. It does not establish the limiting behavior or the alternating constants; those follow from the estimates above. For numerical evaluation of \(\lambda\) the omitted tail after summing through \(j=J\) is at most \(8\cdot8^{-(J+1)}/(21\ln 2)\). The corresponding error in the alternating sum defining \(C\) is bounded by the first omitted \(\varepsilon_j/3\).

## Relationship to prior work and limitations

General arch descriptions of shortest absent subsequences are given by Kosche et al. The same triangular matrices for binary complementary blocks occur in *Fibonacci extremals for shortest absent subsequences of binary words*. *Quadratic recurrence for shortest absent subsequences of Thue–Morse prefixes* gives the same count dynamics in the coordinates \((s_j+t_j,s_j)\) with the prefix index shifted by one. The catalog dates do not establish priority. Eliminating \(s_j\) gives the classical Thue–Morse trace map \(t_{j+2}=t_j^2(t_{j+1}-2)+2\); the growth exponent here is the escape exponent of its particular positive orbit, converted to base two and measured on the half-length scale. The asymptotic claim retains both modes of the logarithmic recurrence and gives the two explicit and provably unequal limits for the shortest-absent-string count. The comparison with prior work is bounded; no novelty is asserted for the transfer framework, the exact count recurrence, or the trace map itself.

## References

1. M. Kosche, T. Koß, F. Manea, and S. Siemer, *Absent Subsequences in Words*, [arXiv:2108.13968](https://arxiv.org/abs/2108.13968).
2. *Fibonacci extremals for shortest absent subsequences of binary words*, [Resultary](https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-fibonacci-extremals-for-shortest-absent-subsequences-of-binary-w--1a6556f14d28/RESULT.md).
3. *Quadratic recurrence for shortest absent subsequences of Thue–Morse prefixes*, [Resultary](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-quadratic-recurrence-for-shortest-absent-subsequences-of-thue-mo--9824aedbf416/RESULT.md).
4. Q. Liu and Y. Qu, *Iteration of polynomial pair under Thue–Morse dynamic*, [arXiv:1403.2257](https://arxiv.org/abs/1403.2257), equation (1).
