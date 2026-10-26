# Gap-four rational Hartogs triangles have four diagonal numerator roots inside the disk

## Finding

For every odd integer \(n\ge 5\), set \(m=n+4\) and
\[
H_{m/n}=\{(z_1,z_2)\in\mathbb C^2: |z_1|^m<|z_2|^n<1\}.
\]
Write the Bergman kernel in the standard rational-Hartogs form
\[
K_{m/n}(z,w)=\frac{P_{m,n}(s,t)}{m\pi^2(1-t)^2(t^n-s^m)^2},\qquad
s=z_1\overline{w_1},\quad t=z_2\overline{w_2},
\]
and define the diagonal numerator \(Q_{m,n}(s)=s^{1-2n}P_{m,n}(s,s)\). Then \(Q_{m,n}\) is a degree-eight palindromic polynomial with no zeros on \(|s|=1\). Consequently it has exactly four zeros in the open unit disk, counted with multiplicity, and each such zero gives a zero of \(K_{m/n}\) in \(H_{m/n}\times H_{m/n}\).

## Assumptions and scope

The parameter is \(n\in\mathbb Z\), odd and at least five, with \(m=n+4\). Thus \(\gcd(m,n)=1\) and \(1<m/n<2\). The claim concerns the diagonal numerator only: it does not locate its individual roots, assert that they are simple, classify the off-diagonal zero set, or settle the Lu Qi-Keng problem for other rational exponents.

## Proof

The rational Hartogs kernel expansion gives a finite diagonal numerator after the monomial series is summed and terms are collected. Put \(Q_{m,n}(s)=\sum_{j=0}^{8}q_js^j\). For \(n=4k+1\), where \(k\ge1\), the coefficients are palindromic, \((q_0,q_1,q_2,q_3,q_4,q_5,q_6,q_7,q_8)=(c_0,c_1,c_2,c_3,c_4,c_3,c_2,c_1,c_0)\), with
\[
\begin{aligned}
c_0&=\frac{(k+1)(k+2)(4k+3)}6,&
 c_1&=(k+1)(4k^2+11k+8),\\
c_2&=(k+1)(2k+3)(4k+5),&
 c_3&=(k+1)(12k^2+33k+22),\\
c_4&=\frac{44k^3+165k^2+217k+99}{3}.
\end{aligned}
\]
For \(n=4k+3\), where \(k\ge1\), the same coefficient order holds with
\[
\begin{aligned}
c_0&=\frac{(k+1)(k+2)(4k+9)}6,&
 c_1&=(k+2)(4k^2+13k+11),\\
c_2&=(k+2)(2k+3)(4k+7),&
 c_3&=(k+2)(12k^2+39k+31),\\
c_4&=\frac{44k^3+231k^2+415k+255}{3}.
\end{aligned}
\]

For \(|s|=1\), set \(x=s+s^{-1}=2\operatorname{Re}s\in[-2,2]\). The palindromic identity gives
\[
s^{-4}Q_{m,n}(s)=R(x),\quad
R(x)=c_0x^4+c_1x^3+(c_2-4c_0)x^2+(c_3-3c_1)x+(c_4-2c_2+2c_0).
\]
In the two residue classes, respectively, the last three coefficients simplify to
\[
(c_2-4c_0,c_3-3c_1,c_4-2c_2+2c_0)
=\left(\frac{(k+1)(16k^2+44k+33)}3,-2(k+1),4k+5\right)
\]
and
\[
(c_2-4c_0,c_3-3c_1,c_4-2c_2+2c_0)
=\left(\frac{(k+2)(16k^2+52k+45)}3,-2(k+2),4k+7\right).
\]

Let \(B_j(u)=\binom4j u^j(1-u)^{4-j}\), for \(0\le u\le1\). The Bernstein coefficients of \(R(-2u)\), in increasing index order, are
\[
\begin{cases}
\left(4k+5,\ 5k+6,\ \frac{32k^3+120k^2+208k+129}{9},\ \frac{8k^3+30k^2+61k+42}{3},\ 4k+5\right),&n=4k+1,\\[2pt]
\left(4k+7,\ 5k+9,\ \frac{32k^3+168k^2+352k+279}{9},\ \frac{8k^3+42k^2+97k+87}{3},\ 4k+7\right),&n=4k+3.
\end{cases}
\]
The Bernstein coefficients of \(R(2u)\) are
\[
\begin{cases}
\left(4k+5,\ 3k+4,\ \frac{32k^3+120k^2+172k+93}{9},\ \frac{(4k+5)(14k^2+35k+24)}3,\ (4k+5)^3\right),&n=4k+1,\\[2pt]
\left(4k+7,\ 3k+5,\ \frac{32k^3+168k^2+316k+207}{9},\ \frac{(4k+7)(14k^2+49k+45)}3,\ (4k+7)^3\right),&n=4k+3.
\end{cases}
\]
Every displayed coefficient is strictly positive for \(k\ge1\). Since each \(B_j(u)\ge0\) and \(\sum_{j=0}^4B_j(u)=1\), both \(R(-2u)\) and \(R(2u)\) are positive on \([0,1]\). Hence \(R(x)>0\) on \([-2,2]\), proving that \(Q_{m,n}\) has no unit-circle roots.

The coefficient list also gives \(Q_{m,n}(s)=s^8Q_{m,n}(1/s)\), with nonzero leading and constant coefficient \(c_0>0\). Its roots therefore occur in reciprocal pairs, with multiplicities preserved. Since no root lies on the unit circle, exactly four of its eight roots lie in \(\mathbb D\), counted with multiplicity. Such a root \(\zeta\) is nonzero and satisfies \(|\zeta|^m<|\zeta|^n<1\). At \(s=t=\zeta\), the numerator vanishes because \(P_{m,n}(\zeta,\zeta)=\zeta^{2n-1}Q_{m,n}(\zeta)=0\), while the denominator is nonzero: \(1-\zeta\ne0\) and \(\zeta^n-\zeta^m=\zeta^n(1-\zeta^4)\ne0\). The pair \((s,t)=(\zeta,\zeta)\) is realizable by points in \(H_{m/n}\): if \(r=|\zeta|\), take \(z=(\sqrt r,\sqrt r)\) and \(w=(\overline\zeta/\sqrt r,\overline\zeta/\sqrt r)\). Both points belong to the domain and have \(z_j\overline{w_j}=\zeta\). Thus the Bergman kernel has a zero in the stated product domain.

## Verification

The symbolic proof is the positivity of the two displayed Bernstein coefficient lists for every integer \(k\ge1\); it does not infer an infinite statement from finite sampling. The accompanying pure-Python checker recomputes the finite numerator coefficients from the integer ceiling formula and compares them with the closed forms for 199 odd parameters \(5\le n\le401\). That finite check is a reproducibility sanity check only. It does not replace the all-parameter algebraic proof. The denominator and domain conditions are checked explicitly above.

## Relationship to prior work

The 2022 public kernel-series source supplies the rational Hartogs monomial expansion and monomial norms from which the diagonal numerator can be collected. Edholm and Mathew's 2025 preprint gives a more explicit numerator formula and proves palindromicity; its stated root-count theorem treats gaps \(m-n=1\) and \(m-n=2\), not gap four. The known zero results for exponents at least two do not cover this family because \(m/n=1+4/n\in(1,2)\) for odd \(n\ge5\). Database comparisons returned nearby results for gaps three, five, and seven through seventeen, and for integer-slope families, but none implies the gap-four statement for this parameter range. This result fills that specific arithmetic slice; it is not a classification for all rational exponents.

## Limitations

No individual root locations or simplicity statement is established. The result concerns the diagonal numerator and yields existence of kernel zeros; it does not describe the complete off-diagonal zero set. The comparison with the 2025 preprint used its abstract, introduction, explicit numerator formula, palindromicity theorem, and stated gap-one/gap-two theorem; later proof pages were not fully inspected, so an unobserved special-case discussion remains a residual literature risk.

## References

1. Public kernel-series source for the Bergman projection on generalized Hartogs triangles, arXiv:2204.08715, first public version 2022-04-19.
2. Luke D. Edholm and Vikram T. Mathew, “Arithmetic properties and zeros of the Bergman kernel on a class of quotient domains,” arXiv:2505.20489, version 1 posted 2025-05-26.
3. Edholm–McNeal's earlier results on Bergman kernels of rational Hartogs triangles, as summarized in the introduction of reference 2; their known zero result for exponents at least two is not applicable to the parameter range here.
