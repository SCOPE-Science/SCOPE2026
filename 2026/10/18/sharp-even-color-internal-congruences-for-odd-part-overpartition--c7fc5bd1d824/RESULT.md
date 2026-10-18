# Sharp even-color internal congruences for odd-part overpartition tuples

## Finding

Let \(a_m(n)\) be the number of ordered \(m\)-tuples of overpartitions whose total is \(n\) and whose parts are all odd; put \(a_m(0)=1\). For every **even** \(m\ge2\), define \(t=\nu_2(m)\), and for each integer \(i\ge i_0(m)\) set
\[
i_0(m)=\begin{cases}3,&t=1,\\2,&t\ge2,\end{cases}
\qquad E(m,i)=\begin{cases}3i-4,&t=1,\\3i+2t-5,&t\ge2.\end{cases}
\]
Then for every integer \(n\ge0\),
\[
\boxed{a_m(2^in)-a_m(2^{i-1}n)
\equiv 2^{E(m,i)}\,\mathbf{1}_{\{n=(2k+1)^2,\ k\in\mathbb Z_{\ge0}\}}
\pmod{2^{E(m,i)+1}}.}
\]
In particular, the exact minimum \(2\)-adic valuation of these differences, over positive \(n\), is \(E(m,i)\); equality occurs precisely at odd squares. The sharp exponent depends on \(m\) only through \(\nu_2(m)\). In the polynomial language defined below, this also proves all three valuation assertions of Conjecture 6.2 in Saikia--Talukdar [1] for every even \(m\), not only its previously conditional coefficient consequence.

## Assumptions and scope

All generating functions are formal power series with integer coefficients. Write
\[
 A(q)=\prod_{j\ge1,\ j\text{ odd}}\frac{1+q^j}{1-q^j},\qquad
 A(q)^m=\sum_{n\ge0}a_m(n)q^n.
\]
For a series \(H(q)=\sum h_nq^n\), let \(\mathcal U H=\sum h_{2n}q^n\). Set \(\xi=A^4\), so \(\xi\in1+8q\mathbb Z[[q]]\) and its coefficient of \(q\) equals \(8\). For polynomials \(P\in\mathbb Z[x]\), introduce the \(\mathbb Z\)-linear operator \(\mathcal S\) by \(\mathcal S(x^j)=T_{2j}(x)\), where \(T_j\) is the usual Chebyshev polynomial of the first kind. Define \(\Theta(P)=\mathcal S((x-1)P)/(x-1)\). The quotient is in \(\mathbb Z[x]\) because \(\mathcal S(F)(1)=F(1)\).

For even \(m\), the auxiliary polynomials of [1, Section 6] satisfy \(R_{i+1}^{(m)}=\Theta(R_i^{(m)})\) and
\[
\mathcal U^i(A^m)-\mathcal U^{i-1}(A^m)
 =(\xi-1)R_i^{(m)}(\xi),
\]
for \(i\ge2\) when \(m\equiv2\pmod4\), or \(i\ge1\) when \(4\mid m\). These identities follow from \(A(-q)=A(q)^{-1}\), symmetrization and \(\mathcal U(\xi^j)=T_{2j}(\xi)\) [1]. The assertions concern only these integer-coefficient objects, not analytic convergence.

## Proof

**1. A stable polynomial invariant.** Put \(y=x-1\). The Chebyshev definitions and \(T_j((z+z^{-1})/2)=(z^j+z^{-j})/2\) give, for \(h\ge0\),
\[
\Theta(y^{2h})=2^{2h+1}y^h(x+1)^{h+1}U_{2h}(x),
\]
and, for \(h\ge1\),
\[
\Theta(y^{2h-1})=2^{2h}y^{h-1}(x+1)^hT_{2h}(x),
\]
where \(U_j\) is the Chebyshev polynomial of the second kind. Indeed substitute \(x=(z+z^{-1})/2\) into \(\mathcal S(y^k)\), expand \((z^2-1)^k+(z^{-2}-1)^k\), then divide by \(y\). In particular,
\[
\Theta(1)=4+2y,\quad
\Theta(y)=8+36y+32y^2+8y^3,
\quad\Theta(y^k)\in2^{k+1}\mathbb Z[y]\ (k\ge2).
\]
Also, \([y]\Theta(y^2)=96\), \([y]\Theta(y^3)=64\), and \([y]\Theta(y^k)=0\) for \(k\ge4\), where \([y]\) extracts the coefficient of \(y\).

Write \(Q(1+y)=\sum_{j\ge0}c_jy^j\). Suppose \(c_1\) is odd and \(c_0+2c_1\equiv4\pmod8\). Then \(c_0\equiv2\pmod4\), so every coefficient of \(\Theta(Q)\) is divisible by \(8\). For \(Q_+=\Theta(Q)/8\), direct substitution gives
\[
Q_+(1)=\frac{c_0}{2}+c_1,\qquad
Q_+'(1)=\frac{c_0+18c_1+48c_2+32c_3}{4},
\]
and
\[
Q_+(1)+2Q_+'(1)
=c_0+10c_1+24c_2+16c_3\equiv4\pmod8.
\]
In particular \(Q_+(1)\equiv2\pmod4\) and \(Q_+'(1)\) is odd. The same invariant therefore persists. Since the derivative is odd, the quotient \(Q_+\) has a unit coefficient and \(\nu_2(\Theta(Q))=3\) whenever \(Q\) satisfies the invariant.

We also need an elementary seed observation: if \(B(1)\) is odd, then \(\Theta(B)\) has exact polynomial valuation \(1\). Indeed its \(y\)-coefficient is \(2B(1)+36B'(1)+96c_2+64c_3\equiv2\pmod4\), whereas all coefficients are even. Moreover \(\Theta(B)/2\) satisfies the invariant: its constant is \(2B(1)+4B'(1)\), its linear coefficient is \(B(1)+18B'(1)+48c_2+32c_3\), and the constant plus twice the linear coefficient is \(4B(1)+40B'(1)+96c_2+64c_3\equiv4\pmod8\).

**2. Seeds for all even colors.** There are three disjoint cases.

When \(m=2u\) with \(u\) odd, let \(P_1=T_u\), \(P_2=\mathcal S(P_1)\), and \(R_2=(P_2-P_1)/(x-1)\) as in [1]. Modulo \(2\), \(T_u\equiv x\) and \(\mathcal S(T_u)\equiv T_u(1)=1\), so \(R_2\equiv1\pmod2\). Thus \(R_2(1)\) is odd; applying the seed observation gives
\[
R_3=2Q_3,\quad \nu_2(R_3)=1,
\]
with \(Q_3\) satisfying the stable invariant.

When \(m=4u\) and \(u\) is odd, let \(P_0=x^u\), \(P_1=\mathcal S(P_0)=T_{2u}\), and \(R_1=(P_1-P_0)/(x-1)\). As \(T_{2u}\equiv1\pmod2\), one has \(R_1\equiv1+x+\cdots+x^{u-1}\pmod2\), hence \(R_1(1)\equiv u\equiv1\pmod2\). The seed observation yields \(R_2=2Q_2\) with exact valuation \(1\) and stable invariant.

Finally suppose \(m=4u\) with \(u\) even, and put \(r=2u=m/2\), \(s=\nu_2(r)\ge2\), \(w=r/2^s\) odd. The polynomial \(T_r-1\) is divisible by \(2^{2s-1}\): first \(T_{2^s}-1\in2^{2s-1}\mathbb Z[x]\) follows by induction from \(T_2=2x^2-1\) and \(T_{2v}=2T_v^2-1\); then use \(T_r=T_w(T_{2^s})\) and \(T_w(1)=1\). With \(P_1=T_r\) and \(P_2=\mathcal S(T_r)\), this implies
\[
R_2=\frac{\mathcal S(T_r)-T_r}{x-1}\in2^{2s-1}\mathbb Z[x].
\]
Using \(T_r'(1)=r^2\), \(T_r''(1)=r^2(r^2-1)/3\), the standard higher Chebyshev derivative formulas and \(\mathcal S(x^j)=T_{2j}\), direct differentiation gives
\[
R_2(1)=\frac{r^2(4r^2+5)}3,\qquad
R_2'(1)=\frac{r^2(4r^2-1)(r^2+3)(4r^2+101)}{630}.
\]
The latter formula has exact valuation \(2s-1\), since every factor other than \(r^2\) and the single factor of \(2\) in \(630\) is odd. Hence \(\nu_2(R_2)=2s-1\). Writing \(Q_2=R_2/2^{2s-1}\), reduction of the displayed expressions modulo \(8\) gives
\[
Q_2(1)\equiv6\pmod8,\qquad Q_2'(1)\equiv3\pmod8.
\]
Therefore \(Q_2\) satisfies the invariant.

**3. Induction and the sharp support.** Every seed in Step 2 satisfies \(R_j=2^{v_j}Q_j\), where \(Q_j\) satisfies Step 1's invariant and
\[
(j,v_j)=\begin{cases}
(3,1),&\nu_2(m)=1,\\
(2,2\nu_2(m)-3),&\nu_2(m)\ge2.
\end{cases}
\]
Iterating Step 1 yields, for all permissible \(i\),
\[
\nu_2(R_i)=v_i=E(m,i)-4,
\quad \nu_2(R_i(1))=v_i+1,
\quad\nu_2(R_i'(1))=v_i,
\quad v_{i+1}=v_i+3.
\]
Thus every assertion of [1, Conjecture 6.2] holds for all even \(m\). Moreover
\[
\frac{\mathcal U^i(A^m)-\mathcal U^{i-1}(A^m)}{2^{E(m,i)}}
=\frac{\xi-1}{8}\,\frac{Q_i(\xi)}2.
\]
The right side has integer coefficients: \(Q_i(1)\) is even and \(\xi\equiv1\pmod8\), so \(Q_i(\xi)/2\equiv Q_i(1)/2\equiv1\pmod2\). Finally, write \(a=(A-1)/2\). The identities \(\xi-1=8(a+a^2)(1+2a+2a^2)\) and \(a\equiv\sum_{j\ge1}(q^{j^2}+q^{2j^2})\pmod2\), derived from the Jacobi theta product (or [1, Lemma 2.2]), give
\[
\frac{\xi-1}{8}\equiv a+a^2
\equiv\sum_{k\ge0}q^{(2k+1)^2}\pmod2.
\]
This proves the displayed congruence, including its exact odd-square support and sharpness. \(\square\)

## Verification

Compile the standalone verifier with `g++ -std=c++17 -O2 -Wall -Wextra opt_even_verify.cpp -o opt_even_verify` and run `./opt_even_verify`. It performs exact coefficient arithmetic modulo \(2^{35}\) independently of the Chebyshev-polynomial proof, then compares the asserted congruence for twelve even color counts through coefficient index \(2048\). The saved verifier returned `VERIFY_OK cases=10116 odd_square_witnesses=364 colors=12 range_max=2048`. Selected symbolic base valuations were also checked by exact polynomial arithmetic for \(m=2,4,6,8,10,12,14,16,18,20,24\). Such finite tests corroborate, but do not prove, the infinite result.

## Relationship to prior work

Saikia and Talukdar [1, Theorem 1.1] establish the analogous congruence for odd \(m\), while [1, Section 6, Conjecture 6.2] explicitly predicts the threefold growth for even \(m\), and [1, Corollary 6.3] is conditional. This result proves that conjecture unconditionally for **every even \(m\)**, determines its constant as \(-4\) for \(\nu_2(m)=1\) and \(2\nu_2(m)-5\) otherwise, and identifies all sharp coefficients.

Adiga and Ranganatha [2, Theorem 1.2] previously established stronger congruences for individual coefficients of the two-color case; in particular, their formulas imply the **two-color coefficient** case above for sufficiently high indices. That special-case congruence is NOT claimed as an independently new numerical theorem. The present new assertions are the full even-color classification and the polynomial-dynamical statements resolving [1, Conjecture 6.2], which do not follow from [2]'s statements concerning only the two-color coefficients. Tang [3] addresses high-power congruences for even-colored overpartitions; its full text could not be assessed here, so possible implicit overlap remains a limitation.

## Limitations

The proof covers even color counts only and the explicitly stated lower bounds on \(i\). It does not assert corresponding sharp formulas at the omitted initial levels, or extend the result to arbitrary other partition families. The coefficient specialization for two colors has substantial earlier coverage [2]. Prior published results, especially the full inaccessible body of [3], may contain further implicit special cases; no claim of exhaustive literature uniqueness is made. The proof is a self-review, not independent expert certification.

## References

[1] M. P. Saikia and P. Talukdar, *Internal congruences modulo powers of 2 for overpartition tuples with odd parts*, arXiv:2609.11806v1 (first public 2026-09-10), particularly Sections 2, 3, 6. https://pdfs.assets.alphaxiv.org/2609.11806v1.pdf

[2] C. Adiga and R. Dasappa, *On overpartition pairs into odd parts modulo powers of 2*, Discrete Mathematics **341** (2018), 3141–3147, DOI:10.1016/j.disc.2018.08.002; author-uploaded full text https://www.researchgate.net/publication/326775876_On_Overpartition_Pairs_into_Odd_Parts_Modulo_Powers_of_2

[3] D. Tang, *Congruences modulo powers of 2 for k-colored overpartitions into odd parts*, Ramanujan Journal **70** (2026), article 5, DOI:10.1007/s11139-026-01379-5; publisher abstract https://link.springer.com/article/10.1007/s11139-026-01379-5

[4] Z. Ahmed, R. Barman and C. Ray, *Congruences modulo powers of 2 for overpartition pairs into odd parts*, Journal of the Korean Mathematical Society **57** (2020), 471–487, DOI:10.4134/JKMS.J190143.
