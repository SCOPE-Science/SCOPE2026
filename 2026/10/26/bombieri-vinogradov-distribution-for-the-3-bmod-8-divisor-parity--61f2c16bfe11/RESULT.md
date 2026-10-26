# Bombieri–Vinogradov distribution for the \(3\bmod8\) divisor-parity reciprocal slice

## Finding
Let \(\sigma(n)\) denote the sum of the positive divisors of \(n\), with the constant coefficient of the series below set equal to one. In \(\mathbb F_2[[q]]\), define
\[
\Sigma(q)=1+\sum_{n\ge1}(\sigma(n)\bmod2)q^n,\qquad \Sigma(q)^{-1}=\sum_{n\ge0}c(n)q^n.
\]
Consider the naturally singled-out residue slice
\[
\mathcal B_3=\{n\ge1:n\equiv3\pmod8,\ c(n)=1\}.
\]
Write \(\operatorname{Li}(y)=0\) for \(y<2\), while \(\operatorname{Li}(y)=\int_2^y dt/\log t\) for \(y\ge2\). Let \(\pi(y;m,b)\) count primes not exceeding \(y\) in the reduced residue class \(b\pmod m\).

**Theorem (averaged level of distribution one half).** For every real \(R>0\), there is a number \(B_R>0\) such that, for all sufficiently large real \(X\), setting \(Q=X^{1/2}/(\log X)^{B_R}\),
\[
\sum_{\substack{m\le Q\\8\mid m}}
\max_{\substack{a\pmod m\\(a,m)=1\\a\equiv3\pmod8}}
\left|
\#\{n\in\mathcal B_3:n\le X,\ n\equiv a\pmod m\}
-\frac1{\varphi(m)}\sum_{\substack{k\ge1\ \mathrm{odd}\\(k,m)=1}}\operatorname{Li}(X/k^2)
\right|
\ll_R \frac{X}{(\log X)^R}.
\]
Every maximum is over a nonempty finite set, and the inner series is finite because of the convention on \(\operatorname{Li}\). Thus this thin residue slice inherits the classical Bombieri–Vinogradov level \(1/2\). One consequence is
\[
\#\{n\in\mathcal B_3:n\le X\}\sim \frac{\pi^2}{32}\frac{X}{\log X}.
\]

## Assumptions and scope
All moduli are positive integers divisible by \(8\); each permitted residue class is coprime to its modulus and congruent to \(3\pmod8\). The implied constant may depend on \(R\), but not on \(X\), the moduli, or the residue classes. No primality conjecture or generalized Riemann hypothesis is assumed. The public identification of \(\mathcal B_3\) from Cooper–Riasanovsky and OEIS A192717, explicitly recalled next, is an input, not a new theorem here.

## Proof
**1. Exact arithmetical reduction.** The source paper's Section 3, Proposition 16 and OEIS A192717 give
\[
\mathcal B_3=\{p^{4j+1}k^2:\ p\equiv3\pmod8\text{ prime},\ j\ge0,\ k\ge1\text{ odd},\ p\nmid k\}.
\]
This description is unique: the prime \(p\) is the unique prime with odd exponent in the factorization, and that exponent is congruent to one modulo four. Write \(N_{m,a}(X)\) for the counting function occurring in the theorem.

**2. Separate the principal prime–square stratum.** Terms with \(j\ge1\) number at most
\[
\sum_{p\ge3\text{ prime}}\sum_{j\ge1}\left\lfloor\sqrt{X/p^{4j+1}}\right\rfloor
\le\sqrt X\sum_{p\ge3}\frac{p^{-5/2}}{1-p^{-2}}=O(\sqrt X).
\]
Likewise, the spurious principal-stratum terms with \(p\mid k\), hence \(k=pu\), number at most
\[
\sum_{p\ge3}\left\lfloor\sqrt{X/p^3}\right\rfloor
\le\sqrt X\sum_{p\ge3}p^{-3/2}=O(\sqrt X).
\]
Both error bounds hold uniformly after restricting to any particular progression. Whenever \(8\mid m\) and \((a,m)=1\), an odd \(k\) in a unit class modulo \(m\) has \(k^2\equiv1\pmod8\); the residue \(a k^{-2}\pmod m\) is therefore automatically congruent to \(3\pmod8\). It follows that
\[
N_{m,a}(X)=\sum_{\substack{k\ge1\ \mathrm{odd}\\(k,m)=1}}\pi(X/k^2;m,a k^{-2})+O(\sqrt X),
\]
where a prime-counting function vanishes for upper limits below two. The error constant is absolute. The restriction \((k,m)=1\) is necessary: otherwise \(p k^2\) could not lie in a reduced residue class.

**3. The small-square range and Bombieri–Vinogradov.** Fix \(R>0\) and write \(L=\log X\). Choose \(C=R+4\) and put \(K=L^C\). By the classical Bombieri–Vinogradov theorem in its \(\max_{y\le X}\) formulation, for any fixed \(T>0\) there is \(B_0(T)>0\) such that
\[
\sum_{m\le X^{1/2}/L^{B_0(T)}}\max_{(b,m)=1}\max_{2\le y\le X}
\left|\pi(y;m,b)-\frac{\operatorname{Li}(y)}{\varphi(m)}\right|
\ll_T X/L^T.
\]
For \(k\le K\), the error after taking the maximum over \(a\) and summing over \(8\mid m\le Q\) is at most \(K\) times this bound: the dependence of \(a k^{-2}\) on \(k\) is harmless because the theorem takes a maximum over every reduced class. Choose \(T=2R+10\) and \(B_R\ge B_0(T)\). The resulting contribution is \(O_R(X/L^{T-C})\), smaller than \(X/L^R\).

**4. Uniformly bound the large-square range.** For \(K<k\le\sqrt{X/2}\), the elementary estimate \(\pi(X/k^2;m,b)\le X/(mk^2)+1\) holds. Summing these bounds, first over \(k\) and then over the moduli, gives
\[
\sum_{\substack{8\mid m\\m\le Q}}\ \sum_{k>K}\pi(X/k^2;m,a k^{-2})
\ll\frac{X\log Q}{K}+Q\sqrt X.
\]
Here the expression on the left is understood with only odd \(k\) coprime to \(m\); the bound is uniform in the chosen class \(a\). The tail of the proposed main term is similarly
\[
\sum_{\substack{8\mid m\\m\le Q}}\frac1{\varphi(m)}\sum_{k>K}\operatorname{Li}(X/k^2)
\ll\frac{X\log Q}{K},
\]
using \(\operatorname{Li}(y)\ll y\) for \(y\ge2\), \(\sum_{k>K} k^{-2}\ll K^{-1}\), and \(\sum_{m\le Q}1/\varphi(m)\ll\log Q\). The initial reduction adds \(O(Q\sqrt X)\) on summation. Finally choose \(B_R\ge R+4\). Since \(Q\sqrt X\le X/L^{B_R}\), and \(\log Q\ll L\), all tails are \(O_R(X/L^R)\), completing the theorem.

**5. Total-count consequence.** Taking \(m=8\), \(a=3\) yields the main term \(\frac14\sum_{k\ \mathrm{odd}}\operatorname{Li}(X/k^2)\). By fixed-\(k\) prime-number asymptotics, truncation at logarithmic \(k\), and \(\sum_{k\ \mathrm{odd}}k^{-2}=\pi^2/8\), this is asymptotic to \((\pi^2/32)X/\log X\), with a smaller error from the theorem.

## Verification
The included `verify.py` performs two independent finite coefficient computations: a direct inverse of the odd-divisor-sum generating series over \(\mathbb F_2\) and a prime-factor classification for all indices up to \(20000\). It also compares the first twenty known terms of OEIS A192717 and residue-class counts for moduli \(8,16,24,40,56,80,120\). The analytic theorem is proved by reduction to the standard Bombieri–Vinogradov theorem, not by finite computation. To reproduce, run `python3 verify.py` using Python's standard library.

## Relationship to prior work
Cooper–Riasanovsky's 2013 paper provides the exact characterization of the \(3\pmod8\) reciprocal support and proves that this slice has natural density zero (Proposition 16). OEIS A192717 records that same classification, its alternate quadratic-form parity description, and finite terms. Those facts are **not** new claims. The classical Bombieri–Vinogradov theorem provides averaged equidistribution of primes. The additional conclusion here transfers it, uniformly at level \(1/2\), through the canonical square-factor decomposition of this particular lacunary binary reciprocal. Neither inspected source states this combined quantitative theorem. A literature search is not a proof of historical uniqueness.

## Limitations
The result addresses only the residue class \(3\pmod8\), not the conjecturally positive-density \(7\pmod{16}\) slice. It establishes an average over moduli \(8\mid m\), not a pointwise uniform error for every modulus near \(X^{1/2}\). Its proof inherits all dependencies of the classical Bombieri–Vinogradov theorem. Because the convolution is simple once the known characterization is available, independently located prior formulations remain a substantive originality risk. No independent audit or validation is claimed.

## References
1. J. N. Cooper and A. W. N. Riasanovsky, *On the Reciprocal of the Binary Generating Function for the Sum of Divisors*, Journal of Integer Sequences 16 (2013), Article 13.1.8, https://cs.uwaterloo.ca/journals/JIS/VOL16/Cooper/cooper3.html ; full freely accessible text https://arxiv.org/html/1409.2909v1 .
2. OEIS A192717, *Positive integers of the form ...*, https://oeis.org/A192717 , author-dated 2012-12-31.
3. Classical Bombieri–Vinogradov theorem; an explicit \(\max_{y\le x}\) statement with \(\pi(y;m,a)\) and \(\operatorname{Li}(y)\) is Theorem 2.3 in B. Cloitre, *Primes in LCM recurrences*, https://arxiv.org/html/2510.18891v3 (2026). This reference supplies the standard theorem, not a result about the reciprocal series.
