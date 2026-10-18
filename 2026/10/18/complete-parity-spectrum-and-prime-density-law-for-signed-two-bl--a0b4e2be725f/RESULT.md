# Complete parity spectrum and prime-density law for signed two-block odd partitions

## Finding

For a positive integer \(n\), let \(a(n)\) be the signed number of representations
\[
n=(2r+1)x+(2s+1)y,\qquad 1\le x<y,\quad r,s\in\mathbb Z_{\ge0},
\]
where each representation has weight \((-1)^{r+s}\). Write \(n=2^k m\), with \(k\ge0\) and \(m\) odd. Then \(a(n)\) is odd **if and only if** exactly one of the following holds:

1. \(m\) is not a square, its only prime occurring to an odd exponent is \(p\), and \(p\equiv3\) or \(5\pmod8\), with \(\nu_p(m)\equiv1\pmod4\). This criterion is independent of \(k\).
2. \(m=t^2\) for an odd \(t\), and either \(k\le1\) with \(t\equiv3,5\pmod8\), or \(k\ge2\) with \(t\equiv1,7\pmod8\).

In particular, the number of odd coefficients up to \(X\) satisfies the exact first-order density law
\[
\#\{1\le n\le X:a(n)\equiv1\pmod2\}
\sim\frac{\pi^2}{8}\frac{X}{\log X}\quad(X\to\infty).
\]
Thus the odd coefficients have natural density zero, with a positive, explicitly determined prime-scale counting constant.

## Assumptions and scope

The variables \(n,x,y,r,s,k,m,t\) are integers in the ranges stated above. The symbol \(\nu_p(m)\) denotes the prime-adic exponent, \(\sigma(m)=\sum_{d\mid m}d\) is the divisor sum, and \(\chi_4\) is the nonprincipal character modulo \(4\). Put \(\lambda(m)=\sum_{d\mid m}\chi_4(d)\). The source's signed count is used without changing its sign convention. The asymptotic is unconditional and relies on the classical prime number theorem for the two reduced residue classes \(3\) and \(5\) modulo \(8\).

## Proof

### 1. Reduction to odd arguments

The exact coefficient identity established by Merca is
\[
a(n)=\frac{\sigma(n)-\lambda(n)}4-\frac{\sigma(n/2)}2+\sigma(n/4),
\]
with divisor sums at nonpositive or nonintegral arguments interpreted as zero. For odd \(m\), it gives \(a(m)=(\sigma(m)-\lambda(m))/4\). Its dyadic specialization, also established in Merca's subsequent paper, is
\[
a(2^k m)=a(m)+(2^{k-1}-1)\sigma(m)\qquad(k\ge1).
\]
For \(k=1\), the correction vanishes; for every \(k\ge2\), it has odd coefficient. Since \(\sigma(m)\) is odd precisely when \(m\) is a square, the parity of \(a(2^k m)\) agrees with that of \(a(m)\) for nonsquares at every level, while it flips exactly at the levels \(k\ge2\) for squares.

### 2. Prime-power parity for odd arguments

For an odd prime \(p\) and integer \(e\ge0\), write \(S_{p,e}=\sigma(p^e)\) and \(L_{p,e}=\sum_{j=0}^e\chi_4(p)^j\). Both \(\sigma\) and \(\lambda\) are multiplicative. If \(p\equiv3\pmod4\), then \(L_{p,e}=0\) for odd \(e\) and \(L_{p,e}=1\) for even \(e\). If \(p\equiv1\pmod4\), then \(L_{p,e}=e+1\).

First suppose that \(\lambda(m)=0\), so some \(p\equiv3\pmod4\) occurs to an odd exponent. For odd \(e\), the two-adic lifting-the-exponent identity gives
\[
\nu_2(S_{p,e})=\nu_2(p+1)+\nu_2\!\left(\frac{e+1}{2}\right),
\]
whereas \(S_{p,e}\) is odd for even \(e\). In particular, the odd-exponent prime \(p\equiv3\pmod4\) contributes at least two factors of \(2\). Since \(a(m)=\sigma(m)/4\) in this case, \(a(m)\) is odd exactly when \(\nu_2(\sigma(m))=2\). This forces one and only one odd prime exponent in the factorization of \(m\), at a prime \(p\equiv3\pmod8\) with exponent \(e\equiv1\pmod4\). Conversely those conditions yield exactly valuation two.

Now suppose that \(\lambda(m)\ne0\). All primes \(q\equiv3\pmod4\) then have even exponents. Modulo \(8\), the local sums satisfy
\[
S_{p,e}\equiv L_{p,e}+4\delta_{p,e}\pmod8,
\]
where the parity of \(\delta_{p,e}\) is as follows: for \(p\equiv5\pmod8\), it is \(\lceil e/2\rceil\pmod2\); for \(p\equiv3\pmod8\) (necessarily even \(e\)), it is \(e/2\pmod2\); and for \(p\equiv1,7\pmod8\), it is zero. Expanding the product of these local congruences shows that
\[
a(m)\equiv\sum_{p^e\parallel m}\delta_{p,e}
\prod_{\substack{q^f\parallel m\\q\ne p}}L_{q,f}\pmod2.
\]
If two or more primes \(p\equiv1\pmod4\) occur to odd exponents, all summands vanish. If exactly one such prime exists, all terms except its own vanish; its contribution is odd precisely when \(p\equiv5\pmod8\) and \(e\equiv1\pmod4\). This yields the remaining nonsquare case.

If no prime has an odd exponent, \(m=t^2\) is an odd square. Every factor \(L_{p,e}\) is then odd, and the displayed parity becomes
\[
a(t^2)\equiv\sum_{p\equiv3,5\ (8)}\nu_p(t)
\equiv\frac{1-(2/t)}2\pmod2.
\]
Here \((2/t)\) is the Jacobi symbol, equal to \(-1\) precisely for \(t\equiv3,5\pmod8\). Combining with Step 1 proves the complete parity classification, including \(t=1\) and \(k=0,1,2\).

### 3. Prime-scale counting

Let \(F(Y)\) count the nonsquare odd integers \(m\le Y\) in the first branch. Their unique factorization is
\[
m=p^{4h+1}u^2,\qquad
p\equiv3,5\pmod8,\quad h\ge0,\quad u\ \text{odd},\quad p\nmid u.
\]
The contribution from \(h\ge1\) is \(O(\sqrt Y)\), because
\[
\sum_{\substack{p\ge3\text{ prime}\\h\ge1}}
\left\lfloor\sqrt{Y/p^{4h+1}}\right\rfloor=O(\sqrt Y).
\]
For \(h=0\), omitting \(p\nmid u\) adds at most \(O(\sqrt Y)\) terms: if \(p\mid u\), writing \(u=pv\) gives \(p^3v^2\le Y\). Let \(\pi_{3,5}(z)\) count primes not exceeding \(z\) in the two classes \(3,5\pmod8\). It follows that
\[
F(Y)=\sum_{\substack{u\ge1\\u\text{ odd}}}\pi_{3,5}(Y/u^2)+O(\sqrt Y).
\]
The prime number theorem in arithmetic progressions gives \(\pi_{3,5}(z)\sim z/(2\log z)\). Cutting the sum at \(u=(\log Y)^3\), the finite portion has a uniform prime-number-theorem estimate; the remaining tail is bounded by \(O(Y/(\log Y)^3)\), using \(\pi_{3,5}(z)\le z\). Since
\[
\sum_{u\text{ odd}}u^{-2}=\frac{\pi^2}{8},
\]
we obtain
\[
F(Y)\sim\frac{\pi^2}{16}\frac{Y}{\log Y}.
\]
The square branch contains at most \(O(\sqrt Y)\) odd arguments \(m\le Y\), regardless of its parity condition. The number of odd \(a(n)\) coefficients with \(n\le X\) therefore equals
\[
\sum_{k\ge0}F(X/2^k)+O(\sqrt X).
\]
Truncating at \(k=\lceil3\log_2\log X\rceil\), the tail is \(o(X/\log X)\); the preceding asymptotic is uniform in the retained range because \(X/2^k\ge X/(\log X)^3\) up to harmless constant factors. Consequently
\[
\sum_{k\ge0}F(X/2^k)
\sim\frac{\pi^2}{16}\frac{X}{\log X}\sum_{k\ge0}2^{-k}
=\frac{\pi^2}{8}\frac{X}{\log X}.
\]
This completes the proof.

## Verification

Run `python3 verify.py` using Python's standard library. The program independently enumerates all signed two-part-size representations for the first \(109\) arguments; checks the arithmetic coefficient formula and the complete parity classification for \(1\le n\le200000\); and displays a finite normalized count. The enumerations are supplementary finite checks. The infinite classification follows from the local factorization, and the counting limit from the prime number theorem in arithmetic progressions.

## Relationship to prior work

Merca's September 2026 paper supplies the full coefficient formula; his October 2026 paper supplies the dyadic identity and congruences modulo odd primes. Neither inspected work states the complete mod-\(2\) coefficient classification, its square-dependent dyadic flip, or the prime-scale constant. The exact prime-power pattern for the \(p\equiv3\pmod8\) nonsquare subfamily already appears as OEIS A192717 and is **not claimed as a new integer sequence**. The present assertion includes the \(p\equiv5\pmod8\) branch, all square arguments, all dyadic layers, and a global asymptotic for the signed partition coefficients. The known exact coefficient formula makes these conclusions theoretically derivable, but their uniform valuation analysis and prime-scale count are separate arithmetic consequences, not quoted results of the inspected papers.

## Limitations

No assertion is made about an independently validated proof or the optimal error term in the asymptotic. The parity theorem relies on Merca's exact coefficient identity as a stated published premise; its arithmetic deductions are proved here. The old sequence A192717 covers part of the nonsquare classification, so the new contribution is the complete partition-coefficient interpretation and counting law, not discovery of that old subsequence. Unindexed prior uses of the same coefficient identity or a complete implicit parity derivation remain possible originality risks.

## References

1. Mircea Merca, *The two-block odd partition function*, arXiv:2609.33770v1 (first public September 27, 2026), Theorem 1.1, https://arxiv.org/abs/2609.33770 ; Ramanujan Journal 71, article 23 (2026), https://doi.org/10.1007/s11139-026-01426-1 .
2. Mircea Merca, *Dyadic Structure of the Two-Block Odd Partition Function and Theta-Weighted Congruences for pod(n)*, arXiv:2610.05020v1 (first public October 4, 2026), Theorem 1.1 and Corollary 3.2, https://arxiv.org/abs/2610.05020 .
3. OEIS Foundation, A192717 (prime-square sequence and 2005/2013 references), https://oeis.org/A192717 .
4. Prime number theorem for arithmetic progressions modulo \(8\) and classical two-adic lifting-the-exponent lemma; standard results used in the proof.
