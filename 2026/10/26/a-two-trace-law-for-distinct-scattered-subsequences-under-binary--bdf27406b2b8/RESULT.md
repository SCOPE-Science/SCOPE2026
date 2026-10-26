# A two-trace law for distinct scattered subsequences under binary complement doubling

## Finding

Let \(u\) be any nonempty finite binary word. Define \(W_0=u\) and \(W_{m+1}=W_m\overline{W_m}\) for every integer \(m\geq0\), where the bar exchanges \(0\) and \(1\). Write \(N_m\) for the number of **distinct nonempty words** occurring as scattered subsequences of \(W_m\); multiplicities of embeddings are not counted.

Associate with the seed two positive integers \(s_0,t_0\) by the matrices in the next section. Then for all \(m\geq0\),

\[
N_m=s_m+t_m-2,\qquad
s_{m+1}=t_m^2+2,\qquad
t_{m+1}=s_mt_m.
\]

Thus the entire sequence is determined by just two seed statistics, regardless of seed length. In particular, \(t_{m+1}=t_m(t_{m-1}^2+2)\) for \(m\geq1\).

Moreover, the exponential growth rate per doubling exists and is explicit:

\[
h(u):=\lim_{m\to\infty}\frac{\log N_m}{2^m}
=\frac13\left(\log(t_0t_1)
+\sum_{j=0}^{\infty}2^{-j-1}
\log\left(1+\frac2{t_j^2}\right)\right).
\]

If the sum is truncated immediately before index \(r\geq0\), its contribution to \(h(u)\) has a positive error bounded by

\[
0\leq h(u)-\frac13\left(\log(t_0t_1)+
\sum_{j=0}^{r-1}2^{-j-1}\log(1+2/t_j^2)\right)
\leq\frac{8}{21\,2^r t_r^2}.
\]

For the Thue–Morse seed \(u=0\), the first terms \(N_0,N_1,\ldots\) are \(1,3,10,72,2664,3647088,6476006417760,\ldots\), and the exact series gives

\[
h(0)=0.450224804749611462926254\ldots,\qquad
\exp(h(0))=1.568664789150344337616438\ldots.
\]

In particular, the total number of distinct scattered subsequences of the length-\(2^m\) Thue–Morse prefix grows as \(\exp((h(0)+o(1))2^m)\). For a general seed the length is \(|u|2^m\), so the base per host symbol is \(\exp(h(u)/|u|)\).

## Assumptions and scope

Every \(u\in\{0,1\}^+\) is permitted, including monochromatic seeds; \(m\) is any nonnegative integer. For a binary word \(v=v_1\cdots v_{\ell}\), define the integral matrices

\[
E_0=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
E_1=\begin{pmatrix}1&0\\1&1\end{pmatrix},\quad
M(v)=E_{v_{\ell}}\cdots E_{v_1},\quad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Set \(s_0=\operatorname{tr}M(u)\) and \(t_0=\operatorname{tr}(PM(u))\). Here \(\operatorname{tr}(PM)\) is the sum of the off-diagonal entries. Both \(s_0\geq2\) and \(t_0\geq1\) for nonempty binary seeds. Scattered subsequences mean strictly increasing index selections; no contiguity condition is imposed.

## Proof

**1. An exact binary subsequence state.** After reading a word \(v\), let \(c_0(v)\) and \(c_1(v)\) be the numbers of its distinct nonempty scattered subsequences ending in \(0\) and \(1\), respectively. Put \(p(v)=(c_0(v)+1,c_1(v)+1)^{\mathsf T}\). Initially \(p(\varepsilon)=(1,1)^{\mathsf T}\). Appending \(0\) replaces every old subsequence (including the empty subsequence) by the distinct subsequence obtained by appending \(0\), so \(c_0(v0)=1+c_0(v)+c_1(v)\) while \(c_1(v0)=c_1(v)\). The analogous identities hold upon appending \(1\). Consequently \(p(v)=M(v)(1,1)^{\mathsf T}\) and

\[
N(v)=c_0(v)+c_1(v)
=(1,1)M(v)(1,1)^{\mathsf T}-2
=\operatorname{tr}M(v)+\operatorname{tr}(PM(v))-2.
\]

This is an identity about distinct subsequence **strings**, not numbers of embeddings.

**2. Complement doubling closes on two traces.** Direct multiplication gives \(PE_0P=E_1\) and \(PE_1P=E_0\), so \(M(\overline v)=PM(v)P\). Therefore, writing \(A_m=M(W_m)\),

\[
A_{m+1}=M(\overline{W_m})M(W_m)=PA_mPA_m=(PA_m)^2.
\]

Each \(A_m\) has determinant \(1\) and \(P\) has determinant \(-1\). For any \(2\times2\) matrix \(B\), \(\operatorname{tr}(B^2)=(\operatorname{tr}B)^2-2\det B\); hence \(s_{m+1}=t_m^2+2\). Furthermore,

\[
t_{m+1}=\operatorname{tr}(PA_{m+1})
=\operatorname{tr}(PA_m^2)
=\operatorname{tr}\bigl(P(s_m A_m-I)\bigr)
=s_mt_m,
\]

using Cayley–Hamilton for \(A_m\) and \(\operatorname{tr}P=0\). The count identity from Step 1 proves the first formula. Substituting \(s_m=t_{m-1}^2+2\) gives the stated scalar recurrence.

**3. Existence and evaluation of the exponential rate.** Since \(s_m\geq2\) and \(t_m>0\), we have \(t_{m+1}\geq2t_m\). Define \(y_m=\log t_m\) and \(\epsilon_m=\log(1+2/t_m^2)\). The scalar recurrence yields

\[
y_{m+2}=y_{m+1}+2y_m+\epsilon_m.
\]

With \(z_m=y_m+y_{m+1}\), this is \(z_{m+1}=2z_m+\epsilon_m\). Thus

\[
\frac{z_m}{2^m}=\log(t_0t_1)+
\sum_{j=0}^{m-1}2^{-j-1}\epsilon_j,
\]

whose right side converges absolutely because \(t_j\geq2^j t_0\). The elementary contraction \(2(y_{m+1}/2^{m+1})=(z_m/2^m)-(y_m/2^m)\) shows that \(\lim_{m\to\infty}y_m/2^m\) is one third of the displayed sum's limit.

It remains to replace \(t_m\) by \(N_m\). Put \(r_m=s_m/t_m\); then \(r_mr_{m+1}=1+2/t_m^2\) and

\[
\frac{r_{m+2}}{r_m}
=\frac{1+2/t_{m+1}^2}{1+2/t_m^2}.
\]

The sum of absolute logarithms of the right-hand ratios is finite. Therefore each parity subsequence of \(r_m\) remains bounded above and below by positive constants. Since \(N_m=t_m(1+r_m)-2\), it follows that \(\log N_m-\log t_m=O(1)\), proving the expression for \(h(u)\).

For the tail, \(t_{r+k}\geq2^k t_r\) and \(\log(1+x)\leq x\) for \(x\geq0\) give

\[
\frac13\sum_{j=r}^\infty2^{-j-1}\epsilon_j
\leq\frac{1}{3\,2^r t_r^2}\sum_{k=0}^{\infty}8^{-k}
=\frac{8}{21\,2^r t_r^2}.
\]

**4. Specialization.** For \(u=0\), \(M(u)=E_0\), so \((s_0,t_0)=(2,1)\). Repeated application of the recurrence gives the integer sequence above. Evaluating the convergent series with the explicit rigorous tail bound establishes the quoted decimal approximations. No finite enumeration is used to infer the infinite identities.

## Verification

A standalone standard-library Python script (`verify.py`) independently implements the classical last-occurrence dynamic program for distinct subsequences, direct set generation on short words, and separate multiplication of the letter matrices. It checks all \(126\) nonempty binary seeds of length at most \(6\), several self-complementary doubling iterations for each, the first \(13\) Thue–Morse blocks including a length-\(4096\) block, and an additional length-\(640\) seeded block. It compares the independently computed counts with the trace recurrence, and asserts the first seven stated Thue–Morse counts. Its expected final line is `VERIFY_OK exhaustive_seeds=126 Thue_Morse_prefix_length=4096`. The proof above, rather than these finite tests, establishes all quantified claims.

## Relationship to prior work

Lejeune, Leroy and Rigo (arXiv:1812.07330, first public version December 18, 2018) study the numbers of embeddings of specified scattered subwords and the \(k\)-binomial equivalence classes of *contiguous factors* of the infinite Thue–Morse word. Their Theorem 6 is an eventual periodicity formula for those equivalence classes, not the present distinct-support count. Berstel, Crochemore and Pin study congruences of embedding multiplicities for Thue–Morse prefixes. Shallit, Shur and Zorcic (arXiv:2310.15064) study avoidance of repetitions by complementary binary morphisms. The classical last-occurrence recurrence for distinct subsequences and the two letter-shear matrices are background; the asserted contribution is the exact two-trace complement-doubling law, its uniform arbitrary-seed form and the effective asymptotic growth formula. An equivalent derivation hidden in broader matrix-product or older shuffle literature remains a residual originality risk.

## Limitations

The formula counts distinct scattered subsequence strings of the *entire* complement-doubling block; it does not provide the distribution by subsequence length or count embeddings. It applies to complement-doubling, not arbitrary morphic words. The growth constant is given by an explicit convergent series, with no assertion of algebraicity, irrationality or transcendence. Primary-source comparisons are not a proof of global novelty. Scientific review is not an independent validation.

## References

- M. Lejeune, J. Leroy and M. Rigo, *Computing the \(k\)-binomial complexity of the Thue–Morse word*, arXiv:1812.07330 (first version December 18, 2018), https://arxiv.org/abs/1812.07330.
- J. Berstel, M. Crochemore and J.-É. Pin, *Thue-Morse sequence and p-adic topology for the free monoid*, Discrete Mathematics 76 (1989), 89–94; available manuscript https://www.irif.fr/~jep/PDF/ThueMorse.pdf.
- J. Shallit, A. Shur and S. Zorcic, *Power-free Complementary Binary Morphisms*, arXiv:2310.15064 (2023), https://arxiv.org/abs/2310.15064.
