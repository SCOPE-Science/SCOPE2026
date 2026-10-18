# Fractal census of maximum consecutive runs of \(b\)-prodigious integers

## Finding

For an integer base \(b\ge3\), let \(p_b(n)\) be the product of the **nonzero** digits in the base-\(b\) expansion of a positive integer \(n\). An integer is \(b\)-prodigious if \(p_b(n)\mid n\). Let \(\ell_b=\min\{j\ge1:j\nmid b\}\), and call an integer \(s\ge1\) an *extremal start* when the \(b+\ell_b\) consecutive integers \(s,\ldots,s+b+\ell_b-1\) are all \(b\)-prodigious. This is the maximum possible consecutive-run length [1].

Define
\[
L_b=\operatorname{lcm}(1,2,\ldots,b-1),\quad
M_b=\frac{L_b}{\gcd(L_b,b^2)},
\]
let \(M_{0,b}\) be the largest divisor of \(M_b\) composed only of primes dividing \(b\), let \(M_{1,b}=M_b/M_{0,b}\), and set
\[
r_b=\min\{r\ge0:M_{0,b}\mid b^r\}.
\]
Then \(\gcd(M_{1,b},b)=1\).

**Complete start criterion.** The extremal starts are exactly
\[
s=b^2c,\qquad c>0,\quad\text{all base-}b\text{ digits of }c\text{ lie in }\{0,1\},\quad M_b\mid c.
\]

**Sharp shell census.** Let \(E_b(m)\) be the number of extremal starts in \([b^{m+1},b^{m+2})\), for integral \(m\ge1\). It is zero when \(m\le r_b\). For \(m\ge r_b+1\), put \(h=m-r_b-1\). Then
\[
E_b(m)=\#\left\{(\varepsilon_0,\ldots,\varepsilon_{h-1})\in\{0,1\}^{h}:
M_{1,b}\mid b^{h}+\sum_{j=0}^{h-1}\varepsilon_jb^j\right\}.
\]
For \(M_{1,b}>1\), this has the explicit effective asymptotic
\[
\left|E_b(m)-\frac{2^{m-r_b-1}}{M_{1,b}}\right|
\le\frac{M_{1,b}-1}{M_{1,b}}
\left(2\cos\frac{\pi}{M_{1,b}}\right)^{m-r_b-1}.
\]
For \(M_{1,b}=1\), equality \(E_b(m)=2^{m-r_b-1}\) holds exactly. In the displayed error formula at exponent zero, the empty-product convention gives the power a value of one, including when \(M_{1,b}=2\).

**Fractal distribution and global oscillation.** Within each shell, put \(u=s/b^{m+1}\). Under the uniform counting measure on its extremal starts, \(u\) converges in distribution, as \(m\to\infty\), to
\[
U_b=1+\sum_{j=1}^{\infty}\xi_jb^{-j},\qquad
\Pr(\xi_j=0)=\Pr(\xi_j=1)=\tfrac12,
\]
with independent digits. The limiting support is the translated two-digit Cantor set, of Hausdorff dimension \(\alpha_b=\log_b2\). If \(T_b(X)\) is the number of extremal starts strictly below \(X\), then
\[
T_b(X)=X^{\alpha_b+o(1)},
\]
but \(T_b(X)/X^{\alpha_b}\) has **no** positive finite limit. More precisely,
\[
\lim_{m\to\infty}\frac{T_b(b^{m+2})}{(b^{m+2})^{\alpha_b}}
=\frac{2^{-r_b-2}}{M_{1,b}},
\]
whereas along \(X=b^{m+2}/(b-1)\) the limit equals
\[
\frac{2^{-r_b-2}}{M_{1,b}}(b-1)^{\alpha_b}.
\]
These are distinct for all \(b\ge3\).

## Assumptions and scope

All integers are positive unless stated otherwise. The base \(b\) is fixed and at least three; all asymptotic constants and rates may depend on \(b\). The integer \(m\) counts digits of \(c=s/b^2\), not digits of \(s\). No primality hypothesis on \(b\) is used. Product-of-nonzero-digits (prodigious), not product-of-all-digits (Zuckerman), is essential.

## Proof

**1. Locating every extremal start.** Gohn et al. [1, Lemmas 7–8 and Theorem 9] prove the following boundary classification for \(b>2\): a maximal consecutive prodigious block of length at least \(b+1\) begins at \(1\), at \(cb^2\), or at \(cb^2+b\); the one beginning at \(1\) has length \(b+\ell_b-1\), while one beginning at \(cb^2+b\) has length at most \(b+1\). Their Corollary 4 establishes that no run is longer than \(b+\ell_b\). Since \(\ell_b\ge2\), any extremal block therefore starts at \(cb^2\) with \(c>0\). Conversely, a run of this maximum length is automatically maximal at both endpoints.

For \(1\le j<b\), the base-\(b\) digits of \(cb^2+j\) consist of those of \(c\), a zero digit, and the final digit \(j\), so
\[
p_b(cb^2+j)=p_b(c)j.
\]
Since adjacent members \(cb^2+1\) and \(cb^2+2\) are prodigious, their common factor \(p_b(c)\) divides both integers, hence their difference \(1\), forcing \(p_b(c)=1\). (For \(b=3\), the same argument uses the digits \(1,2\), which both exist.) Thus every digit of \(c\) is \(0\) or \(1\). For these \(c\), membership of all \(cb^2+j\), \(1\le j<b\), is equivalent to \(j\mid cb^2\) for each \(j\), or \(L_b\mid cb^2\), or \(M_b\mid c\). The term \(cb^2\) is automatically prodigious. For the remaining members \(cb^2+b+j\), \(0\le j<\ell_b\), the nonzero-digit product is \(1\) for \(j=0\) and \(j\) for \(j>0\). By minimality of \(\ell_b\), each such \(j\) divides \(b\), hence also \(cb^2+b+j\). This proves both necessity and sufficiency of the criterion.

**2. Removing the prime powers supported on the base.** Write \(c=b^t v\), where its \(t\) least significant base-\(b\) digits are zero and its next digit is one. Then \(v\equiv1\pmod p\) for every prime \(p\mid b\), whence \(\nu_p(c)=t\nu_p(b)\). Consequently \(M_{0,b}\mid c\) if and only if \(t\ge r_b\). Writing \(c=b^{r_b}d\), the remaining condition \(M_{1,b}\mid c\) is equivalent to \(M_{1,b}\mid d\), since the two moduli are coprime to \(b\). For a \(c\) with exactly \(m\) base-\(b\) digits, \(d\) has exactly \(m-r_b\) such digits, leading digit one. Expanding its remaining \(h=m-r_b-1\) digits proves the finite shell-count formula.

**3. Exponential equidistribution.** Fix \(M=M_{1,b}>1\), write \(\zeta=\exp(2\pi i/M)\), and use the elementary Fourier identity \(\mathbf1_{M\mid d}=M^{-1}\sum_{t=0}^{M-1}\zeta^{td}\). Then
\[
E_b(m)=\frac{1}{M}\sum_{t=0}^{M-1}\zeta^{tb^h}
\prod_{j=0}^{h-1}(1+\zeta^{tb^j}).
\]
The \(t=0\) term is \(2^h/M\). For every nonzero \(t\pmod M\) and every \(j\ge0\), coprimality \(\gcd(b,M)=1\) gives \(tb^j\not\equiv0\pmod M\), hence \(|1+\zeta^{tb^j}|\le2\cos(\pi/M)<2\). Bounding the remaining \(M-1\) Fourier terms proves the displayed error. When \(M=1\), all \(2^h\) digit choices are admissible.

**4. Cantor distribution.** Fix any first \(K\) digits after the leading one in the base-\(b\) expansion of \(d\). For fixed \(K\) and large \(h\), the other \(h-K\) binary digits contribute one of \(2^{h-K}\) choices. The same Fourier argument, now with an arbitrary fixed residue offset, gives \(2^{h-K}/M+o(2^h)\) admissible completions, uniformly over the \(2^K\) choices of fixed prefix. Dividing by \(E_b(m)\sim2^h/M\) yields limiting probability \(2^{-K}\) for each prefix. Convergence on all finite digit cylinders gives the stated weak limit. Standard disjoint-cylinder covering and the uniform Bernoulli mass bound show its support has Hausdorff dimension \(\log_b2\) (the two length-\(b^{-K}\) child intervals remain disjoint for \(b\ge3\)).

**5. Power-law scale and obstruction to a global constant.** Summing the shell asymptotics gives
\[
T_b(b^{m+2})=\sum_{j=1}^{m}E_b(j)
\sim\frac{2^{m-r_b}}{M_{1,b}}.
\]
The sum of error terms is \(o(2^m)\) because its exponential base is strictly less than two. Every extremal start in shell \([b^{m+1},b^{m+2})\) is at most
\[
b^2\frac{b^m-1}{b-1}<\frac{b^{m+2}}{b-1}.
\]
The next shell begins at \(b^{m+2}\). Hence \(T_b(b^{m+2}/(b-1))=T_b(b^{m+2})\) for all sufficiently large \(m\). Division by the two distinct powers yields the two asserted subsequential constants. Bounds between successive shell endpoints give \(T_b(X)=X^{\alpha_b+o(1)}\).

## Verification

The accompanying `verify.py` performs exact integer checks for bases \(3\le b\le12\), every digit length \(1\le m\le8\), and prodigious membership up to \(\min(300000,b^8)\). It independently compares the digit-criterion count with shell enumeration, checks the explicit Fourier bound for tested shell lengths, tests every detected maximum run against the start criterion, and checks all predicted starts whose full blocks lie in the tested range. All checks passed. Run with `python verify.py`. Numerical checks are finite evidence only; Steps 1–5 prove the infinite assertions.

## Relationship to prior work

Gohn, Harrington, Lebiere, Samamah, Shappell, and Wong [1] proved the maximum consecutive-run length \(b+\ell_b\) and studied allowable maximal-run lengths. Their boundary classification is used explicitly in Step 1. The present quantitative result determines *every* extremal starting point, gives its exact digital shell census with an explicit leading constant and error, and establishes the resulting fractal limit and absence of a global constant in the counting asymptotic. These quantitative conclusions are not asserted in [1].

Banks and Shparlinski [2] studied arithmetic statistics of numbers with restricted digits, including residue distribution; it gives relevant broader background for Step 3, but does not connect those sets to extremal prodigious blocks. He and Sanna [3] count the distinct object of integers divisible by the product of **all** digits (Zuckerman numbers) and discuss prodigious numbers as related background, without extremal run start counts. OEIS A055471 [4] lists base-ten prodigious integers but provides no equivalent shell or Cantor limit theorem. The arithmetic-progression literature about Niven numbers concerns digit *sums* rather than the required nonzero digit products.

## Limitations

The exact leading constant concerns digit-length shells, not a simple global \(C X^{\alpha_b}\) asymptotic: in fact, the latter is disproved. The result concerns only *maximum* consecutive-run length, not the distribution of shorter runs or of all prodigious numbers. It relies on the published maximum-run boundary classification [1], which was inspected in full text. Exponential convergence of shell counts can be slow for bases with large \(M_{1,b}\). Broader restricted-digit equidistribution is pre-existing; the specific arithmetic connection, census, and oscillation for extremal prodigious blocks are the claimed contribution. Independent mathematical validation has not been performed.

## References

1. M. Gohn, J. Harrington, S. Lebiere, H. Samamah, K. Shappell, and T. W. H. Wong, *Arithmetic Progressions of b-Prodigious Numbers*, Journal of Integer Sequences 25 (2022), Article 22.8.7, published October 25, 2022. https://cs.uwaterloo.ca/journals/JIS/VOL25/Wong/wong42.pdf
2. W. D. Banks and I. E. Shparlinski, *Arithmetic properties of numbers with restricted digits*, Acta Arithmetica 112 (2004), 313–332. DOI: 10.4064/aa112-4-1. https://www.impan.pl/shop/publication/transaction/download/product/83200
3. Q. He and C. Sanna, *Counting numbers that are divisible by the product of their digits*, arXiv:2403.14812, first posted March 21, 2024. https://arxiv.org/html/2403.14812v1
4. OEIS Foundation, sequence A055471, *Numbers divisible by the product of their nonzero decimal digits*. https://oeis.org/A055471
