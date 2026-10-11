# Parity-sharp fourth moments of the dyadic quadratic graph

## Finding
For every integer \(m\geq1\), write \(N=2^m\), \(R=\mathbb Z/N\mathbb Z\), and
\[
\mathcal E_m f(u,v)=\frac1N\sum_{t\in R}f(t)
\exp\!\left(\frac{2\pi i(ut+vt^2)}N\right),\qquad (u,v)\in R^2.
\]
For every nonzero complex-valued function \(f\) on \(R\), the sharp inequality is
\[
\boxed{\sum_{(u,v)\in R^2}|\mathcal E_m f(u,v)|^4
\leq C_m\left(\frac1N\sum_{t\in R}|f(t)|^2\right)^2,\qquad
C_m=\begin{cases}
2^{(m+1)/2},&m\text{ odd},\\
3\,2^{m/2-1},&m\text{ even}.
\end{cases}}
\]
For odd \(m=2k+1\), equality is attained by the indicator of any coset of \(2^kR\). For even \(m=2k\), equality is attained by the indicator of any coset of \(2^{k-1}R\). No assertion that these are all extremizers is made.

The uniform input \(f\equiv1\) has fourth-moment ratio exactly \(m+1\), hence is extremal precisely for \(1\le m\le3\); for every \(m\ge4\), it is strictly suboptimal.

## Assumptions and scope
The ambient group is the complete cyclic ring \(R=\mathbb Z/2^m\mathbb Z\); all Fourier sums run over the full group with counting measure in \(R^2\), while the input squared norm is normalized by \(N^{-1}\). The input coefficients may be arbitrary complex numbers, including zero. No primitivity restriction is imposed on Fourier characters. The value \(C_m\) is the fourth power of the \(L^2(R,\mathrm{avg})\) to \(\ell^4(R^2)\) norm.

## Proof
**1. Exact autocorrelation identity.** Put \(S=\sum_{t\in R}|f(t)|^2\), and let \(\mathscr Q\) be the number-weighted quartic form obtained by imposing two-sum equalities on the parabola:
\[
\mathscr Q(f)=\sum_{\substack{a,b,c,d\in R\\a+b=c+d\\a^2+b^2=c^2+d^2}}
f(a)f(b)\overline{f(c)f(d)}.
\]
Orthogonality of additive characters gives
\[
\sum_{u,v\in R}|\mathcal E_m f(u,v)|^4=N^{-2}\mathscr Q(f).
\]
Write \(a=x+h\), \(b=y\), \(c=x\), \(d=y+h\). Then the quadratic constraint is \(2h(x-y)=0\) in \(R\). For each \(h\in R\), define the additive subgroup
\[
K_h=\{z\in R:2hz=0\}.
\]
Summing over its cosets yields the nonnegative identity
\[
\mathscr Q(f)=\sum_{h\in R}\sum_{A\in R/K_h}
\left|\sum_{x\in A}f(x+h)\overline{f(x)}\right|^2.
\]
Cauchy--Schwarz on each coset, followed by rearrangement, gives
\[
\mathscr Q(f)\leq\sum_{x,y\in R}|f(x)|^2|f(y)|^2M_m(x-y),
\qquad
M_m(d)=\#\{h\in R:2h(d-h)=0\}.
\tag{1}
\]

**2. Complete dyadic collision count.** Let \(\nu_2(d)\) denote the truncated \(2\)-adic valuation, assigning \(m\) to zero. For \(m\ge2\), set \(\ell=m-1\) and \(r=\nu_2(d)\). Directly solving \(h(d-h)=0\pmod{2^\ell}\) gives
\[
M_m(d)=\begin{cases}
2^{r+2},&2r<\ell,\\
2^{m-\lceil\ell/2\rceil},&2r\ge\ell.
\end{cases}\tag{2}
\]
Indeed, when \(2r<\ell\), all solutions are in the two disjoint classes \(h\equiv0\) or \(h\equiv d\pmod{2^{\ell-r}}\), each having \(2^{r+1}\) lifts modulo \(2^m\). When \(2r\ge\ell\), exactly the multiples of \(2^{\lceil\ell/2\rceil}\) solve the congruence. For \(m=1\), \(M_1(d)=2\) for every \(d\).

**3. Odd exponents.** If \(m=2k+1\), (2) gives \(M_m(d)\le2^{k+1}\) for every \(d\). In (1), this implies \(\mathscr Q(f)\le2^{k+1}S^2\). For the subgroup \(H=2^kR\), one has \(2ab=0\) in \(R\) for all \(a,b\in H\), so the map \(t\mapsto(t,t^2)\) sends each coset of \(H\) onto an affine subgroup of \(R^2\). Its \(|H|=2^{k+1}\) points therefore have additive energy \(|H|^3\). Choosing \(f\) to be the coset indicator proves sharpness, including \(m=1\).

**4. Even exponents.** Let \(m=2k\), \(k\ge1\). The collision count (2) implies the pointwise estimate
\[
M_m(d)\le 2^k\Big(1+\mathbf 1_{d\in 2^{k-1}R\setminus2^kR}\Big).
\tag{3}
\]
Normalize \(p(x)=|f(x)|^2/S\). Partition the residue classes modulo \(2^k\) into paired daughters \(a\) and \(a+2^{k-1}\), indexed by \(a\pmod{2^{k-1}}\), with total masses \(x_a\) and \(y_a\). For independent \(X,Y\) with law \(p\),
\[
\Pr\big(X-Y\in2^{k-1}R\setminus2^kR\big)
=2\sum_a x_a y_a
\le\frac12\sum_a(x_a+y_a)^2\le\frac12.
\]
Inserting (3) into (1) gives \(\mathscr Q(f)\le 3\,2^{k-1}S^2\).

For sharpness, take \(H=2^{k-1}R\) and \(f=\mathbf1_H\). Every \(x-y\in H\) has the form \(2^{k-1}D\). Writing \(h=2^{k-1}T\), the condition \(2h(x-y-h)=0\pmod{2^{2k}}\) becomes \(T(D-T)\equiv0\pmod2\). It has \(2^{k+1}\) choices of \(h\in H\) when \(D\) is odd and \(2^k\) choices when \(D\) is even. Exactly half the ordered pairs \((x,y)\in H^2\) belong to each case. Consequently,
\[
\mathscr Q(\mathbf1_H)
=|H|^2\left(\tfrac12\,2^{k+1}+\tfrac12\,2^k\right)
=3\,2^{k-1}|H|^2,
\]
which proves equality in the even formula.

**5. Uniform-input comparison.** For \(f\equiv1\),
\[
\frac{\mathscr Q(1)}{S^2}
=\frac1N\sum_{d\in R}M_m(d)
=\frac1N\sum_{h\in R}\gcd(N,2h)=m+1.
\]
The last identity counts the zero term once and each of the \(m\) possible valuations of nonzero \(h\) once with total contribution \(N\). Comparing this value with \(C_m\) shows equality only for \(m=1,2,3\), and strict inequality for \(m\ge4\).

## Verification
The standalone `checker.py` enumerates every solution of the dyadic quadratic congruence for \(1\le m\le10\), checks formula (2), and checks the sharp coset witnesses by exact integer two-sum fiber counts. It also tests arbitrary Gaussian-integer coefficient vectors on small groups without floating-point comparisons. Running `python3 checker.py` returned `CHECK_PASS 2122`. These finite checks are corroborative; the proof for all \(m\) is in the valuation argument and inequalities above.

## Relationship to prior work
Hickman and Wright study Fourier restriction for polynomial graphs over \(\mathbb Z/N\mathbb Z\); their 2018 article establishes uniform estimates in selected exponent ranges, with a parabola result for odd \(N\) and prime-power statements requiring primes greater than the curve degree. The present result concerns the exact fourth-power norm for the previously excluded dyadic moduli. González-Riquelme and Oliveira e Silva establish sharp inequalities over finite **fields**, rather than dyadic local rings. Kingsbury-Neuschotz studies a different restriction regime for **squarefree** moduli. A separate exact prime-power parabola result for odd primes does not determine the dyadic constants; substituting two for an odd prime gives different values in both exponent parities. No claim of exhaustive novelty is made.

## Limitations
The equality examples are explicit, but a complete classification of all maximizing functions is not proved. The theorem is restricted to moduli that are powers of two and to the fourth output moment; neither general composite moduli nor higher moments are addressed. The bibliographic comparison may miss older results phrased in quadratic-congruence or local harmonic-analysis terminology. Computational checks do not certify the infinite-family argument independently.

## References
1. J. Hickman and J. Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo N*, arXiv:1801.03176v1, first posted 2018-01-09; *Discrete Analysis* 2018:11, sections 2 and 7. https://arxiv.org/abs/1801.03176
2. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, first posted 2024-05-26, Theorems 1.1--1.4. https://arxiv.org/abs/2405.16647
3. N. Kingsbury-Neuschotz, *On a Restriction Problem of Hickman and Wright for the Parabola over Z/NZ for Squarefree N*, arXiv:2509.09885, first posted 2025-09-11, Theorem 1.1 and Lemma 2.2. https://arxiv.org/abs/2509.09885
