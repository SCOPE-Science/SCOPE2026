# Exact ternary valuation levels and least periods for shifted Tribonacci numbers

## Finding
Let \(T_0=0\), \(T_1=T_2=1\), and \(T_{n+3}=T_{n+2}+T_{n+1}+T_n\). Put \(\nu_3(z)\) for the three-adic valuation of a nonzero integer, or its standard extension to \(\mathbb Z_3\). Let \(R=\{3,8,10\}\). For each \(r\in R\) there is a unique \(\alpha_r\in\mathbb Z_3\) specified by the congruences in the next section. Then, for all \(n=13m+r\ge0\) with \(0\le r<13\),
\[
\nu_3(T_n+1)=\begin{cases}0,&r\notin R,\\1+\nu_3(m-\alpha_r),&r\in R.\end{cases}
\]
In particular \(\alpha_{10}=-1\), so \(\nu_3(T_n+1)=1+\nu_3(n+3)\) whenever \(n\equiv10\pmod{13}\).

For every \(t\ge1\) the exact level \(\nu_3(T_n+1)=t\) consists of **six** residue classes modulo \(13\cdot3^t\), and **this is its least positive period**. The zero level occupies ten classes modulo \(13\) and has least period \(13\). If \(C_t(N)=\#\{0\le n<N:\nu_3(T_n+1)=t\}\), then
\[
\lim_{N\to\infty}\frac{C_t(N)}N=p_t,
\qquad p_0=\frac{10}{13},\qquad p_t=\frac6{13\cdot3^t}\quad(t\ge1),
\]
and \(\lvert C_t(N)-p_tN\rvert<6\) for every \(N,t\ge0\).

## Assumptions and scope
All integer indices \(n\) are nonnegative. The matrix construction below extends the sequence to negative indices solely to identify one three-adic root. The three-adic integers \(\mathbb Z_3\) are the inverse limit of \(\mathbb Z/3^k\mathbb Z\). Every \(\alpha_r\) is determined by the following **unique residue rule**, which also makes the valuation formula effective without relying on numerical approximations: for each \(k\ge0\), choose the unique \(a_{r,k}\in\{0,\ldots,3^k-1\}\) satisfying
\[
T_{13a_{r,k}+r}+1\equiv0\pmod{3^{k+1}},\qquad a_{r,0}=0.
\]
Then \(\alpha_r\equiv a_{r,k}\pmod{3^k}\). For \(r=3,8,10\), respectively, the residues for \(k=1,2,3,4\) are
\[
(1,0,2),\qquad(7,6,8),\qquad(16,24,26),\qquad(16,78,80).
\]
For \(t\ge1\), the six residue classes at level \(t\) are explicitly
\[
\bigcup_{r\in R}\bigl\{13(a_{r,t-1}+3^{t-1}j)+r\pmod{13\cdot3^t}:\;j\in\{0,1,2\},\;a_{r,t-1}+3^{t-1}j\ne a_{r,t}\bigr\}.
\]

## Proof
Let
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&1&1\end{pmatrix},\qquad v=\begin{pmatrix}0\\1\\1\end{pmatrix},\qquad e_1=\begin{pmatrix}1\\0\\0\end{pmatrix}.
\]
Thus \(T_n=e_1^{\mathsf T}M^nv\), and an exact matrix multiplication yields
\[
M^{13}=I+3B,\qquad B=\begin{pmatrix}91&141&168\\168&259&309\\309&477&568\end{pmatrix}.
\]
Because \(M^{13}\equiv I\pmod3\), the residue pattern of \(T_n+1\pmod3\) has period dividing thirteen. Computing \(T_0,\ldots,T_{12}\) shows that **exactly** \(r=3,8,10\) make \(T_r+1\equiv0\pmod3\). This proves the zero-valuation assertion outside \(R\).

For any \(r\in R\), define the convergent three-adic analytic interpolation
\[
f_r(z)=1+e_1^{\mathsf T}M^r(I+3B)^zv
=1+T_r+\sum_{j\ge1}3^j\binom zj e_1^{\mathsf T}M^rB^jv,
\qquad z\in\mathbb Z_3.
\]
For every nonnegative integer \(m\), \(f_r(m)=T_{13m+r}+1\). The linear coefficient after dividing by three is
\[
c_r=e_1^{\mathsf T}M^rBv=(T_{13+r}-T_r)/3,
\]
whose exact values for \(r=3,8,10\) are \((1922,40457,136865)\); each is congruent to \(2\pmod3\). The constants \(1+T_r\) are divisible by three. Set \(g_r=f_r/3\). For \(j\ge2\), the integer polynomial \((z)_j=z(z-1)\cdots(z-j+1)\) satisfies \((a)_j-(b)_j\in(a-b)\mathbb Z_3\) for all \(a,b\in\mathbb Z_3\). Also \(j-\nu_3(j!)\ge2\), so
\[
3^j\left(\binom aj-\binom bj\right)\in9(a-b)\mathbb Z_3\quad(j\ge2).
\]
Consequently \(g_r(a)-g_r(b)=(a-b)(c_r+3u)\) for some \(u\in\mathbb Z_3\), and \(c_r+3u\) is a three-adic unit. Hence
\[
\nu_3(g_r(a)-g_r(b))=\nu_3(a-b),\qquad g_r(z)\equiv g_r(0)+2z\pmod3.
\]
The affine map modulo three is bijective. The exact valuation identity implies each root modulo \(3^k\) lifts uniquely to a root modulo \(3^{k+1}\), so completeness gives a unique \(\alpha_r\in\mathbb Z_3\) with \(g_r(\alpha_r)=0\). Taking \(b=\alpha_r\) yields the asserted formula \(\nu_3(T_{13m+r}+1)=1+\nu_3(m-\alpha_r)\) and the residue rule. The recurrence matrix is invertible over \(\mathbb Z\); extending backward gives \(T_{-3}=-1\). Substituting \(z=-1\) into \(f_{10}\) thus gives zero; uniqueness proves \(\alpha_{10}=-1\).

Fix \(t\ge1\). Within each \(r\in R\), the valuation equals \(t\) precisely when \(m\equiv a_{r,t-1}\pmod{3^{t-1}}\) but \(m\not\equiv a_{r,t}\pmod{3^t}\). There are exactly two allowed residues modulo \(3^t\). The three disjoint choices of \(r\) therefore give six classes modulo \(q=13\cdot3^t\). To prove least period, note that any period must preserve the three-element support \(R\pmod{13}\), so its residue modulo thirteen is zero (the only translation preserving a proper nonempty subset of the prime cyclic group is zero). Shifting by \(q/3\) cyclically permutes the three lifts of \(a_{r,t-1}\) and changes their two-element complement, hence is not a period. Shifting by \(q/13=3^t\) changes the support modulo thirteen, so it is also not a period. Because any proper divisor of \(q\) divides \(q/3\) or \(q/13\), the least period is \(q\). The level zero is the complement of three nontrivial residue classes modulo thirteen, also with least period thirteen.

The count of a union of \(h\) distinct classes modulo \(q\) has natural density \(h/q\), with absolute discrepancy from \(hN/q\) strictly smaller than \(h\) for every \(N\). This proves the densities and bound \(<6\) for positive levels; for level zero, use the complement of three classes to obtain \(<3\). The proofs apply to every nonnegative index and valuation level.

## Verification
The standalone `verify_tribonacci_shift_three.py` needs Python 3 and no dependencies. Run `python3 verify_tribonacci_shift_three.py`. It reconstructs \(M^{13}\), initial residues, exact unit-slope coefficients, Hensel root residues through seven levels, and least-period tests for six positive levels. Its independently iterated recurrence checks 125000 consecutive indices modulo \(3^7\) against the lifted formula. The reproducible check returned `VERIFY_OK matrix_power=13 roots_mod13=3,8,10 derivative_mod3=2,2,2 lifted_levels=7 least_period_levels=6 direct_terms=125000 explicit_integer_root=-1`. These finite checks corroborate **premises and consequences**, not the infinite proof itself.

## Relationship to prior work
Bilu, Luca, Nieuwveld, Ouaknine and Worrell (first available 30 October 2022) study three-adic and other prime-adic valuations of **unshifted** Tribonacci numbers and the possibility of nonintegral three-adic zeros. Young (published 25 October 2024) studies shifted Tribonacci valuations **at prime 47**, pointing out the pitfalls of a previous shifted two-adic claim; his Proposition 1 does not give the present prime-three formula. Antony and Barman (first available 28 February 2024) analyze unshifted third-order recurrences and do not supply this shifted-plus-one frequency and least-period law. The present result gives an effective new shift/prime combination with a complete periodic level distribution, rather than asserting a universal formula for all primes.

## Limitations
The theorem concerns only the shifted value \(T_n+1\) and the prime three. No statement about a different prime or arbitrary third-order recurrence follows. The two nonexplicit roots are defined uniquely by congruence lifts, not claimed to be rational integers. The literature comparison is best knowledge, not proof of absolute priority; equivalent unindexed work remains possible. No independent audit has been performed.

## References
1. Y. Bilu, F. Luca, J. Nieuwveld, J. Ouaknine, J. Worrell, *On the p-adic zeros of the Tribonacci sequence*, arXiv:2210.16959 (first posted 2022-10-30), https://arxiv.org/abs/2210.16959.
2. P. T. Young, *On the Brocard–Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), article A92, published 2024-10-25; https://math.colgate.edu/~integers/y92/y92.pdf.
3. D. Antony, R. Barman, *On the p-adic valuation of third order linear recurrence sequences*, arXiv:2402.18279 (first posted 2024-02-28), https://arxiv.org/abs/2402.18279.
