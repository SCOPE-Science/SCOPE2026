# An all-index floor formula and a uniform residual bound for reciprocal fourth powers of Pell numbers

## Finding

Let \(P_0=0\), \(P_1=1\), and \(P_{j+2}=2P_{j+1}+P_j\) be the Pell sequence; let \(Q_0=Q_1=2\) and \(Q_{j+2}=2Q_{j+1}+Q_j\) be its companion sequence. For every integer \(n\ge1\), define
\[
S_n=\sum_{k=n}^{\infty}\frac1{P_k^4},\qquad
T_n=\frac{3P_{4n}-Q_{4n}}4+\frac{(-1)^n(2P_{2n}-Q_{2n})}{5}.
\]
Then the following *uniform, all-index* estimate holds:
\[
\boxed{\quad0<S_n^{-1}-T_n<\frac1{10}\quad(n\ge1).}\tag{1}
\]
Furthermore the fractional part of \(T_n\) is exactly \(9/10\), \(1/2\), or \(1/10\), according as \(n\equiv1\), \(2\), or \(0\pmod3\). Consequently
\[
\boxed{\quad\left\lfloor\left(\sum_{k=n}^{\infty}P_k^{-4}\right)^{-1}\right\rfloor=\left\lfloor\frac{3P_{4n}-Q_{4n}}4+\frac{(-1)^n(2P_{2n}-Q_{2n})}{5}\right\rfloor\quad(n\ge1).}\tag{2}
\]
The first seven exact integer parts are \(0,15,606,20127,686446,23303293,791717374\).

## Assumptions and scope

All indices are integers \(n\ge1\); all denominators are positive Pell numbers. The series converges by exponential growth of \(P_k\). No conjectural estimate or finite-experiment extrapolation is used in the proof. The bound is strict and uniform, not merely an asymptotic estimate. The result concerns *every* Pell index, rather than the balancing-number subsequence at even indices.

## Proof

**Step 1: exact analytic expansion.** Set \(\alpha=1+\sqrt2\), \(\beta=1-\sqrt2=-\alpha^{-1}\), \(a=\alpha^{-2}=3-2\sqrt2\), \(z=a^n\), and \(t=(-1)^n\). Binet's identity \(P_k=(\alpha^k-\beta^k)/(2\sqrt2)\) and the absolutely convergent binomial series give
\[
\begin{aligned}
S_n&=64z^2F,\\
F&=c_0+c_1tz+c_2z^2+H,\\
c_0&=\frac1{1-a^2},\quad c_1=\frac4{1+a^3},\quad c_2=\frac{10}{1-a^4},\\
H&=\sum_{j=3}^{\infty}\binom{j+3}{3}\frac{t^jz^j}{1-(-1)^ja^{j+2}}.
\end{aligned}
\tag{3}
\]
To see the factor, \(P_k^{-4}=64\alpha^{-4k}(1-(-1)^k\alpha^{-2k})^{-4}\); exchange the absolutely convergent sums over \(k\ge n\) and \(j\ge0\). The inner geometric denominator is \(1-(-1)^ja^{j+2}\).

**Step 2: explicit control of all omitted terms.** For \(n\ge3\), the elementary numerical inequalities \(0<a<173/1000\) and \(0<z\le a^3<1/190\) hold (by squaring positive expressions). Since \(\binom{j+4}{3}/\binom{j+3}{3}=(j+4)/(j+1)\le7/4\) for \(j\ge3\), and every geometric denominator in \(H\) exceeds \(1-a^5\), we have
\[
\frac{|H|}{c_0}\le\frac{20(1-a^2)z^3}{(1-a^5)(1-7z/4)}<21z^3.\tag{4}
\]
Define \(d_1=c_1/c_0\), \(d_2=c_2/c_0\), \(h=H/c_0\), and \(v=d_1tz+d_2z^2+h\). Direct substitution shows \(0<d_1<4\), \(0<d_2<10\); consequently
\[
|d_2z^2+h|<11z^2,\qquad |v|<4.1z.
\]
The algebraic identity
\[
\frac1{1+v}-\bigl(1-d_1tz+(d_1^2-d_2)z^2\bigr)
=-h+\frac{v^2-d_1^2z^2-d_1^2z^2v}{1+v}
\tag{5}
\]
is exact. The estimates \(|v^2-d_1^2z^2|<89z^3\), \(|d_1^2z^2v|<66z^3\), and \(|1+v|>1-4.1/190\) make the right side of (5) smaller than \(180z^3\) in absolute value. Thus, writing \(R_n=S_n^{-1}\),
\[
\left|R_n-(Az^{-2}+Btz^{-1}+C)\right|<180Az,
\tag{6}
\]
where exact arithmetic in \(\mathbb Q(\sqrt2)\) yields
\[
A=\frac1{64c_0}=-\frac14+\frac{3\sqrt2}{16},\quad
B=-\frac{c_1}{64c_0^2}=-\frac15+\frac{\sqrt2}{10},\quad
C=\frac{c_1^2/c_0^3-c_2/c_0^2}{64}=\frac{67\sqrt2}{1200}.
\tag{7}
\]

**Step 3: comparison with the integral recurrence expression.** Put \(A'=-1/4-3\sqrt2/16\) and \(B'=-1/5-\sqrt2/10\). Expanding \(P_{4n},Q_{4n},P_{2n},Q_{2n}\) by Binet gives the *exact*, all-index identity
\[
T_n=Az^{-2}+Btz^{-1}+A'z^2+B'tz.
\tag{8}
\]
The bounds \(0<A<1/64\), \(|A'|<13/25\), and \(|B'|<7/20\) imply from (6)–(8) that
\[
|R_n-T_n-C|<\frac{180}{64\cdot190}+\frac7{20\cdot190}+\frac{13}{25\cdot190^2}<\frac{17}{1000}
\quad(n\ge3).\tag{9}
\]
As \(78/1000<C<80/1000\), (9) implies \(0<R_n-T_n<1/10\) for all \(n\ge3\).

**Step 4: first two indices without extrapolation.** Direct recurrence evaluation gives \(T_1=9/10\), \(T_2=31/2\). Since \(P_k\ge2^{k-1}\),
\[
1<S_1<\frac{16}{15},\qquad\frac{15}{16}<R_1<1,
\]
so \(0<R_1-T_1<1/10\). For \(n=2\), use \(P_2=2\), \(P_3=5\), \(P_4=12\) and \(P_{k+1}>2P_k\):
\[
\frac{5}{78}<\frac1{16}+\frac1{625}+\frac1{20736}
<S_2<\frac1{16}+\frac1{625}+\frac{16}{15\cdot20736}<\frac2{31}.
\]
Therefore \(31/2<R_2<78/5=15.6\), proving (1) also for \(n=2\).

**Step 5: a three-class fractional-part obstruction.** The recurrence for \(P_{4n}\) implies \(P_{4n}\equiv0\pmod4\), and \(Q_{4n}\equiv2\pmod4\), so the first term in \(T_n\) always has fractional part \(1/2\). Because \((1+\sqrt2)^6=99+70\sqrt2\equiv-1\pmod5\) in \(\mathbb Z[\sqrt2]\), the sequence
\[
r_n=(-1)^n(2P_{2n}-Q_{2n})\pmod5
\]
has period three and residues \(2,0,3\) for \(n\equiv1,2,0\pmod3\), respectively. Thus \(\{T_n\}=9/10,1/2,1/10\), respectively. All are positive and at most \(9/10\), so (1) cannot carry the fractional part across the next integer, proving (2).

## Verification

Run \(\texttt{python3 verify.py}\) using Python's standard library. The checker derives the Pell and companion sequences using integer recurrence, computes forty independently bracketed infinite tails using exact rational arithmetic and a geometric upper bound, verifies the three-class residues, and confirms the surd coefficients \(A,B,C\) by exact rational arithmetic in \(\mathbb Q(\sqrt2)\). Expected output: \(\texttt{VERIFY_OK: 40 exact rational reciprocal-tail brackets; 40 residue checks; Pell congruence; surd coefficients}\). The checker is supporting finite evidence; Steps 1–5 prove the assertion for infinitely many indices.

## Relationship to prior work

Xu and Wang (2013) explicitly formulated the Pell reciprocal-power integer-part problem and solved exponent three, while identifying exponent four and above as difficult. Crucially, Li, Yang, and Yuan (2025, Theorem 2.4) already give a *generalized-Lucas fourth-power asymptotic* that specializes to the exact **same** \(T_n\) plus the constant \(C=67\sqrt2/1200\), with an \(o(1)\) remainder. Thus neither the asymptotic expression nor the eventual integer-part identity is claimed as new: combined with the periodic fractional parts, their result already implies the formula for all sufficiently large indices, albeit without an explicit threshold. The distinct proved claim here is the strict global \((0,1/10)\) residual enclosure and resulting all-index floor identity, including every small index, with an explicit uniform error proof. Hwang, Park, and Song (2022) prove a fourth-power floor result for Fibonacci, not Pell. The 2026 balancing-number result studies an even-index Pell subsequence, not the full Pell tail.

## Limitations

The quantitative bound \(1/10\) is not claimed sharp, and the argument does not extend automatically to other Lucas recurrences or powers. Prior generalized-Lucas asymptotic literature substantially covers the large-index expansion; an unindexed direct all-index Pell formula remains an originality risk. Self-review is not independent validation.

## References

1. Z. Xu and T. Wang, “The infinite sum of the cubes of reciprocal Pell numbers,” *Advances in Difference Equations* **2013**, 184, published 26 June 2013. DOI: 10.1186/1687-1847-2013-184. https://link.springer.com/article/10.1186/1687-1847-2013-184
2. H. Li, K. Yang, and P. Yuan, “The asymptotic behavior of the reciprocal sum of generalized Fibonacci numbers,” *Electronic Research Archive* **33** (2025), 409–432, Theorem 2.4. DOI: 10.3934/era.2025020. https://www.aimspress.com/aimspress-data/era/2025/1/PDF/era-33-01-020.pdf
3. W. Hwang, J.-D. Park, and K. Song, “On the reciprocal sum of the fourth power of Fibonacci numbers,” *Open Mathematics* **20** (2022), 1642–1655. DOI: 10.1515/math-2022-0525.
4. “On the infinite sum of reciprocals of the fourth powers of balancing numbers,” arXiv:2609.31548 (2026). https://arxiv.org/abs/2609.31548
