# Sharp power-log deficit for weighted minimal-power divisor means

## Finding
For each fixed integer \(r\ge2\), let \(M_r(n)=\min\{m\in\mathbb Z_{\ge1}:n\mid m^r\}\), let \(d(n)\) count its positive divisors, and let \(\omega(n)\) count distinct prime factors (with \(\omega(1)=0\)). Set
\[
F_r(n)=\frac{d(M_r(n))}{2^{\omega(n)}},\qquad \theta=\frac1{r+1},
\]
\[
C_r=\prod_p\left(1+\frac1{2p(p^r-1)}\right),
\qquad
A_r=\frac{\sqrt{r+1}}{\sqrt\pi}
\prod_p\left(1-\frac1p\right)^{1/2}
\left(1+\frac1{2p(1-p^{-r/(r+1)})}\right).
\]
Both products converge absolutely and define strictly positive constants. For every fixed such \(r\), **as real \(x\to\infty\)**,
\[
\boxed{\sum_{n\le x}F_r(n)
=C_rx+\zeta(\theta)A_r\frac{x^\theta}{\sqrt{\log x}}
+o_r\!\left(\frac{x^\theta}{\sqrt{\log x}}\right).}
\]
Here \(\zeta(s)\) denotes the analytic continuation of the Riemann zeta function. Since \(0<\theta<1\), \(\zeta(\theta)<0\); hence the discrepancy \(C_rx-\sum_{n\le x}F_r(n)\) has the *sharp positive* order \(x^\theta/\sqrt{\log x}\). There is no claim of an explicit remainder beyond the stated little-oh term.

## Assumptions and scope
The index \(r\) is a fixed integer at least two, not a real variable tending to infinity with \(x\). The count includes \(n=1\), for which \(F_r(1)=1\). All sums over \(n\le x\) use integer \(n\ge1\), with real \(x\). Products range over all rational primes. No hypotheses about zeros of the zeta function are used. The constant \(C_r\) is the mean-value constant for the weight \(k=2\) in the earlier weighted-composition problem, not a newly defined incompatible normalization.

## Proof
**1. Positive divisor convolution.** Since \(M_r(p^a)=p^{\lceil a/r\rceil}\), for every \(a\ge1\) we have \(F_r(p^a)=(\lceil a/r\rceil+1)/2\). Subtracting adjacent coefficients in the local series yields
\[
\sum_{a\ge0}F_r(p^a)z^a
=\frac1{1-z}\left(1+\frac{z^{r+1}}{2(1-z^r)}\right),\qquad |z|<1.
\]
Therefore \(F_r=\mathbf{1}*h_r\), where \(\mathbf{1}(n)=1\) for all positive \(n\), \(h_r\) is multiplicative, \(h_r(1)=1\), and
\[
h_r(p^a)=\begin{cases}\tfrac12,&a=rj+1\text{ for some integer }j\ge1,\\0,&\text{otherwise}.\end{cases}
\]
In particular \(h_r(n)\ge0\), and the Dirichlet series of \(h_r\) is
\[
H_r(s)=\sum_{n\ge1}\frac{h_r(n)}{n^s}
=\prod_p\left(1+\frac{p^{-(r+1)s}}{2(1-p^{-rs})}\right).
\]
Its absolute convergence at \(s=1\) gives \(\sum h_r(n)/n=C_r\) with the claimed first Euler product. The exact convolution identity becomes
\[
\sum_{n\le x}F_r(n)=\sum_{d\le x}h_r(d)\left\lfloor\frac xd\right\rfloor.
\tag{1}
\]

**2. Transfer to a squarefree-weight mean.** Let \(b(m)=\mu(m)^2/2^{\omega(m)}\). Its series is \(K(t)=\prod_p(1+\tfrac12p^{-t})\). Define a signed arithmetic function \(j_r\) by
\[
J_r(s):=\frac{H_r(s)}{K((r+1)s)}
=\prod_p\left[1+
\frac{\tfrac12\sum_{j\ge2}p^{-(rj+1)s}}
{1+\tfrac12p^{-(r+1)s}}\right]
=\sum_{u\ge1}\frac{j_r(u)}{u^s}.
\tag{2}
\]
The local quotient admits an absolutely convergent geometric expansion whenever \(\Re(s)>0\). Its first nonconstant term has exponent \(2r+1\). Thus, choosing any positive \(\delta<1/(r+1)-1/(2r+1)\), the *absolute Dirichlet series of the coefficients* satisfies
\[
\sum_{u\ge1}\frac{|j_r(u)|}{u^{\theta-\delta}}<\infty.
\tag{3}
\]
This follows directly from summing the absolute local geometric series: the local excess is \(O_r(p^{-(2r+1)(\theta-\delta)})\), and its prime sum converges. Comparing Dirichlet coefficients of (2) gives the exact representation
\[
h_r(n)=\sum_{um^{r+1}=n}j_r(u)b(m).
\tag{4}
\]

**3. The counting law for the convolution kernel.** The standard Selberg–Delange theorem at exponent \(1/2\) applies to \(b\), because
\[
K(t)=\zeta(t)^{1/2}G(t),\qquad
G(t)=\prod_p(1-p^{-t})^{1/2}(1+\tfrac12p^{-t}),
\]
with \(G\) analytic near \(t=1\) and \(G(1)>0\). Therefore
\[
B(y):=\sum_{m\le y}b(m)
\sim\frac{G(1)}{\sqrt\pi}\frac{y}{\sqrt{\log y}}.
\tag{5}
\]
Use (4) to express \(N_r(x):=\sum_{n\le x}h_r(n)\) as \(\sum_{u\le x}j_r(u)B((x/u)^\theta)\). For \(u\le\sqrt x\), the argument of \(B\) is at least \(x^{\theta/2}\). Formula (5) is uniform in that region, and dominated convergence, with (3), gives the normalized contribution
\[
\frac{x^\theta}{\sqrt{\log x}}
\frac{G(1)}{\sqrt{\pi\theta}}
\sum_{u\ge1}\frac{j_r(u)}{u^\theta}
+o_r\left(\frac{x^\theta}{\sqrt{\log x}}\right).
\]
For \(u>\sqrt x\), the elementary inequality \(B(y)\le y\) and (3) give the negligible bound \(O_r(x^{\theta-\delta/2})\). Hence
\[
N_r(x)\sim A_r\frac{x^\theta}{\sqrt{\log x}},
\qquad
A_r=\frac{G(1)J_r(\theta)}{\sqrt{\pi\theta}}.
\tag{6}
\]
At \(s=\theta\) we have \((r+1)s=1\). Multiplication of the local factors in \(G(1)J_r(\theta)\) cancels \(1+\tfrac1{2p}\) and produces exactly the claimed formula for \(A_r\). Each resulting factor differs from one by \(O_r(p^{-(2r+1)/(r+1)}+p^{-2})\), so the product is absolutely convergent and positive.

**4. The exact fractional-part deficit.** From (1) and \(C_r=\sum h_r(d)/d\), with \(\{t\}=t-\lfloor t\rfloor\),
\[
C_rx-\sum_{n\le x}F_r(n)
=\sum_{d\le x}h_r(d)\left\{\frac xd\right\}
+x\sum_{d>x}\frac{h_r(d)}d.
\tag{7}
\]
Both terms are nonnegative. By summation by parts and (6), using \(0<\theta<1\),
\[
x\sum_{d>x}\frac{h_r(d)}d
\sim\frac\theta{1-\theta}A_r\frac{x^\theta}{\sqrt{\log x}}.
\tag{8}
\]
The counting law (6) is regularly varying of index \(\theta\). Hence the probability measures assigning weight \(h_r(d)/N_r(x)\) to each point \(d/x\), for \(1\le d\le x\), converge weakly on \([0,1]\) to the continuous measure with cumulative distribution \(t^\theta\). The bounded function \(t\mapsto\{1/t\}\), defined arbitrarily at \(t=0\), has discontinuities only at \(0\) and \(1/j\) for positive integers \(j\); the limiting measure charges none of them. Consequently
\[
\sum_{d\le x}h_r(d)\left\{\frac xd\right\}
\sim A_r\frac{x^\theta}{\sqrt{\log x}}
\theta\int_0^1\left\{\frac1t\right\}t^{\theta-1}\,dt.
\tag{9}
\]
For \(0<s<1\), the standard fractional-part integral representation of the analytically continued zeta function is
\[
\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\frac{\{v\}}{v^{s+1}}\,dv.
\]
Upon substituting \(v=1/t\), equations (7)–(9) show that the discrepancy coefficient is
\[
A_r\left(\frac\theta{1-\theta}+\theta\int_0^1\{1/t\}t^{\theta-1}\,dt\right)
=-\zeta(\theta)A_r.
\]
Lastly, \(\zeta(s)=\eta(s)/(1-2^{1-s})<0\) for \(0<s<1\), because the alternating Dirichlet eta sum is positive and the denominator negative. This proves the sign, nonvanishing, and sharp order of the asserted asymptotic. \(\square\)

## Verification
The independent finite identities checked by the included `verify.py` cover \(r=2,3,4,5\) and every integer \(1\le n\le3000\): prime-power coefficients, exact convolution \(F_r=\mathbf{1}*h_r\), and the fractional-part identity (7) for five integer cutoffs per parameter. The script performs exact rational arithmetic and prints `VERIFY_OK`. These tests **do not** establish the infinite asymptotic; that step depends on the proof, notably Selberg–Delange at exponent \(1/2\) and the regular-variation passage in (9).

## Relationship to prior work
M. Bouderbala, *On the Mean Value of a Weighted Composite Arithmetic Function* (first public arXiv submission 2026-02-17; primary MSC 11A25), studies exactly \(d(M_r(n))/k^{\omega(n)}\). Its Theorem 1.1 gives the leading mean with error \(O_{r,k}(x(\log x)^{2/k-2})\). At \(k=2\), its error is \(O_r(x/\log x)\). Its remark on additional inverse-logarithm expansion near the leading pole does not give this separate, nonintegral power-log deficit. The preceding theorem instead establishes its *sharp signed* size and explicit zeta/Euler-product coefficient, for every fixed \(r\ge2\).

The 2022 paper *On a sum of a multiplicative function linked to the divisor function over the set of integers B-multiple of 5* discusses the different, uncomposed divisor/unitary-divisor quotient and a digit-restricted sum; it does not settle this power-composition discrepancy. The classical Selberg–Delange theorem for squarefree weights is an explicitly used ingredient, not a new result. The possibility of a more general previously unnoticed theorem implying this case is not excluded.

## Limitations
The conclusion holds for each **fixed** integer \(r\ge2\), with a little-oh term not claimed uniform in \(r\). The proof relies on the known Selberg–Delange asymptotic for a standard squarefree multiplicative weight. The result does not address the weighted parameter \(k\ne2\), where a different leading singularity occurs. The numerical tests are finite. Originality comparisons cannot establish absolute uniqueness and an implicit statement in broader tauberian or summatory-function literature remains possible. Independent mathematical validation has not been performed.

## References
1. M. Bouderbala, *On the Mean Value of a Weighted Composite Arithmetic Function*, arXiv:2602.16027 (initially submitted 2026-02-17), Theorem 1.1, Sections 1–3, and Remark 3.2. https://arxiv.org/abs/2602.16027
2. M. Bouderbala, *On a sum of a multiplicative function linked to the divisor function over the set of integers B-multiple of 5* (2022). https://cm.episciences.org/10467/pdf
3. G. Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, classical Selberg–Delange theorem (standard version at exponent \(1/2\)).
4. E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, the classical fractional-part integral representation of \(\zeta(s)\).
