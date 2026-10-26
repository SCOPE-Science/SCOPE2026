# Prime-order formula for all cobalancing square-window GCDs

## Finding

Let the cobalancing numbers be defined by \(b_0=b_1=0\) and \(b_{n+2}=6b_{n+1}-b_n+2\) for every \(n\geq0\). For every integer \(k\geq1\), set
\[
H_k(n)=\sum_{j=1}^{k}b_{n+j}^{2},\qquad G(k)=\gcd\{H_k(n):n\geq0\}.
\]
For each odd prime \(p\geq7\), let \(r_p\) denote the multiplicative order of \(3+2z\) in the finite unit group of \((\mathbb Z/p\mathbb Z)[z]/(z^2-2)\). Then **for every** \(k\geq1\),
\[
\boxed{G(k)=2^{\max\{2,1+\nu_2(k)\}}\,
3^{\nu_3(k)\mathbf1_{12\mid k}}\,
5^{(1+\nu_5(k))\mathbf1_{6\mid k}}\!
\prod_{\substack{p\mid k,\ p\geq7\\r_p\mid k}}p^{\nu_p(k)}.}
\]
An empty product equals \(1\). In particular, the formula gives \(G(6)=20\), \(G(12)=120\), \(G(21)=28\), \(G(30)=100\), and \(G(136)=272\). This is a uniform local-prime classification of the complete infinite sequence of window GCDs, not merely a bounded computation.

## Assumptions and scope

All indices \(k\) are positive integers and the GCD ranges over **every** integer \(n\geq0\). The convention is \(\nu_p(k)=0\) when \(p\nmid k\). The quotient algebra defining \(r_p\) may be a field or a product of two finite fields; the element \(3+2z\) is invertible in either case because its norm is \(1\). The primary subject is the arithmetic of a second-order Pell-related sequence.

## Proof

**1. Odd-prime decomposition.** Work in the commutative \(p\)-adic algebra \(R_p=\mathbb Z_p[z]/(z^2-2)\), for any odd prime \(p\). Write \(\alpha=3+2z\) and \(\beta=3-2z=\alpha^{-1}\). For \(u_n=2b_n+1\), the initial values \(u_0=u_1=1\) and the homogeneous recurrence give
\[
u_n=A\alpha^n+B\beta^n,\quad
A=\frac{1-\beta}{\alpha-\beta},\quad B=\frac{\alpha-1}{\alpha-\beta},\quad AB=\frac18.
\]
The denominators, as well as \(\alpha\pm1\) and \(\alpha^{\pm2}-1\), are units of \(R_p\): their respective norms are supported only at \(2\). Consequently both \(A\) and \(B\) are units. Squaring gives the exact identity
\[
b_n^2=\frac5{16}+\frac{A^2}4\alpha^{2n}+\frac{B^2}4\beta^{2n}-\frac A2\alpha^n-\frac B2\beta^n.
\]
With \(S_k(w)=\sum_{j=1}^{k}w^j=w(w^k-1)/(w-1)\), this yields
\[
H_k(n)=\frac{5k}{16}+\frac{A^2}4\alpha^{2n}S_k(\alpha^2)+\frac{B^2}4\beta^{2n}S_k(\beta^2)
-\frac A2\alpha^nS_k(\alpha)-\frac B2\beta^nS_k(\beta).
\tag{1}
\]
For odd \(p\), \(w-1\) is a unit for \(w\in\{\alpha^{\pm1},\alpha^{\pm2}\}\). If the order \(r_p\) divides \(k\), the standard odd-prime binomial lifting lemma gives
\[
S_k(\alpha^{\pm1}),S_k(\alpha^{\pm2})\in p^{\nu_p(k)+1}R_p.
\tag{2}
\]
Indeed, \(r_p\) divides \(p-1\) or \(p+1\), so \(p\nmid r_p\), and \(\alpha^{r_p}\equiv1\pmod p\); expanding \((1+pX)^m\) proves the requisite lower bound. The same holds for the inverse and squared powers.

**2. Primes \(p\geq11\).** The norms of \(\alpha^j-1\) for \(j=1,2,3,4\) are respectively \(-4,-32,-196,-1152\). Thus for \(p\geq11\), \(r_p>4\). The five bases \(\alpha^{-2},\alpha^{-1},1,\alpha,\alpha^2\) are pairwise distinct with unit differences modulo \(p\). Their five-row Vandermonde matrix is invertible in \(R_p\). If every \(H_k(n)\) were zero modulo \(p\), the coefficients in (1) would each vanish modulo \(p\). The \(\alpha^n\)-coefficient forces \(r_p\mid k\), and the constant coefficient forces \(p\mid k\). Conversely, when these two divisibilities hold, (1) and (2) imply every \(H_k(n)\) is divisible by \(p^{\nu_p(k)}\). As the constant term has precisely valuation \(\nu_p(k)\), while all nonconstant terms have at least one higher valuation, **every** \(H_k(n)\) has exactly this valuation. Hence
\[
\nu_p(G(k))=\begin{cases}\nu_p(k),&p\mid k\text{ and }r_p\mid k,\\0,&\text{otherwise},\end{cases}\qquad p\geq11.
\]

**3. The exceptional prime \(5\).** Here \(r_5=6\), so the same five-row Vandermonde matrix is invertible modulo \(5\). If \(6\nmid k\), the coefficient of \(\alpha^n\) in (1) is a unit modulo \(5\), and not every window is divisible by \(5\). If \(6\mid k\), the identity
\[
\alpha^6-1=19600+13860z=5(3920+2772z)
\]
has **exact** \(5\)-adic valuation \(1\) in \(R_5\), because its quotient by \(5\) is congruent to \(2z\not=0\) modulo \(5\). Therefore each of the four nonconstant coefficients of (1) is divisible by \(5^{\nu_5(k)+1}\), and its \(\alpha^n\)-coefficient has **exactly** that valuation. The constant coefficient also has valuation \(\nu_5(k)+1\). All windows have at least that valuation, and after dividing by this power, invertibility of the five-row Vandermonde matrix shows that not all windows can vanish modulo \(5\). Therefore
\[
\nu_5(G(k))=(1+\nu_5(k))\mathbf1_{6\mid k}.
\]

**4. The exceptional primes \(3\) and \(7\).** Reducing the defining recurrence yields exact periodic patterns:
\[
(b_n^2\bmod3)_{n\geq0}=(0,0,1,1)^\infty,\qquad
(b_n^2\bmod7)_{n\geq0}=(0,0,4)^\infty.
\]
In the first case, all \(k\)-windows vanish modulo \(3\) precisely when \(4\mid k\) and \(3\mid k/4\), equivalently \(12\mid k\). In the second, all windows vanish modulo \(7\) precisely when \(3\mid k\) and \(7\mid k/3\), equivalently \(21\mid k\). The relevant orders are \(r_3=4\) and \(r_7=3\). Whenever the indicated divisibility holds, (1)–(2) show that the constant term \(5k/16\) has valuation exactly \(\nu_p(k)\) and every nonconstant term has higher valuation. Consequently
\[
\nu_3(G(k))=\nu_3(k)\mathbf1_{12\mid k},\qquad
\nu_7(G(k))=\nu_7(k)\mathbf1_{21\mid k}.
\]
The \(7\)-formula agrees with the \(p\geq7\) product in the theorem.

**5. The prime \(2\).** Every \(b_n\) is even. Put \(t_n=b_n/2\); then \(t_0=t_1=0\) and \(t_{n+2}=6t_{n+1}-t_n+1\). Modulo \(2\) the sequence \(t_n\) is \((0,0,1,1)^\infty\). If \(4\nmid k\), some length-\(k\) window has an odd sum of \(t_n^2\), so \(\nu_2(G(k))=2\).

For \(h\geq0\), define \(L_h=4\cdot2^h\) and \(T_h(n)=\sum_{i=1}^{L_h}t_{n+i}^2\). The transition matrix for \((t_n,t_{n+1},1)^\mathsf T\) is
\[
C=\begin{pmatrix}0&1&0\\-1&6&1\\0&0&1\end{pmatrix},\qquad
C^4=I+2K,\quad K=\begin{pmatrix}-18&102&21\\-102&594&123\\0&0&0\end{pmatrix}.
\]
Here \(K^2\equiv0\pmod2\), and modulo \(2\) the first two rows of \(K\) are \((0,0,1)\). Successive squaring proves
\[
C^{L_h}\equiv I+2^{h+1}K\pmod{2^{h+2}},\quad
 t_{n+L_h}-t_n\equiv2^{h+1}\pmod{2^{h+2}}
\tag{3}
\]
for all \(h,n\geq0\). Expanding \((t_{n+L_h})^2-t_n^2\) using (3), after division by \(2^{h+2}\) the result is congruent modulo \(2\) to \(t_n+1\) when \(h=0\), and to \(t_n\) when \(h\geq1\). In any block of length \(L_h\), the number of odd \(t_n\) is even. Therefore
\[
T_h(n+L_h)\equiv T_h(n)\pmod{2^{h+3}}.
\]
The base case is \(T_0(n)\equiv2\pmod4\), since exactly two of any four consecutive \(t_n\) are odd. The identity \(T_{h+1}(n)=T_h(n)+T_h(n+L_h)\) then proves inductively
\[
T_h(n)\equiv2^{h+1}\pmod{2^{h+2}}\quad(h,n\geq0).
\]
If \(4\mid k\), write \(k=4\cdot2^h u\) for odd \(u\). Every length-\(k\) block is a sum of \(u\) consecutive length-\(L_h\) blocks, each congruent to \(2^{h+1}\pmod{2^{h+2}}\). Thus every sum of \(t_n^2\) over that length has valuation \(h+1=\nu_2(k)-1\). Multiplying by \(4\),
\[
\nu_2(G(k))=\max\{2,1+\nu_2(k)\}.
\]
Combining the prime-by-prime evaluations proves the displayed formula without any restriction on \(k\). \(\square\)

## Verification

The accompanying standalone `verify.py` uses exact integer arithmetic. It independently computes GCDs of ten consecutive actual window sums (without a modulus) for each \(1\leq k\leq350\), and compares twelve shifted windows modulo \(40k\) with the predicted factorization for \(351\leq k\leq2500\). It checks multiplicative orders in the quadratic residue algebra, the transition-block congruences for eight successive powers of two and forty shifts each, and the exact \(5\)-adic first lift. The computation is a finite consistency check; the proof above establishes all infinite assertions.

## Relationship to prior work

Mbirika, Schrader, and Spilker (first submitted January 13, 2023) defined the six related square-window GCDs and explicitly asked for closed forms, giving only the divisibility-by-four observation for the cobalancing-square GCD (Question 30). An earlier partial cobalancing study supplied a finite exact evaluation procedure for each \(k\), the bound \(G(k)\mid40k\), and values along \(k=12\cdot2^r\); these are not newly claimed here. The new result instead classifies **every prime divisor with its exact exponent**, including the order criterion at all primes \(p\geq7\) and the exceptional factor at \(5\). It provides a uniform structural factorization, rather than the previous per-input GCD procedure or one parameter subfamily. Classical binomial lifting, a Vandermonde argument, and a separate dyadic block induction explain the arithmetic classification.

## Limitations

The formula applies to squared cobalancing numbers with precisely the stated initialization and all positive window lengths. It does not assert comparable classifications for Lucas-cobalancing squares, other powers, or arbitrary second-order recurrences. Evaluating \(r_p\) requires order computation in a finite quadratic algebra, but this is a finite explicit invariant for each prime. The proof and computational checks have not undergone independent audit. Publication priority remains subject to potentially unindexed literature or general congruence theorems not located in the searches.

## References

- aBa Mbirika, Janee Schrader, and Jürgen Spilker, *Pell and associated Pell braid sequences as GCDs of sums of k consecutive Pell, balancing, and related numbers*, arXiv:2301.05758v1 (2023-01-13), revised v3 (2023-06-28), Journal of Integer Sequences 26 (2023), Article 23.6.4; particularly Section 2, Question 30 and the full squared-sums discussion. https://arxiv.org/html/2301.05758v3
- aBa Mbirika and Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626 (2022), Fibonacci Quarterly 60 (2022), 255–269. https://arxiv.org/abs/2204.12626
- OEIS A053141, cobalancing numbers, https://oeis.org/A053141
