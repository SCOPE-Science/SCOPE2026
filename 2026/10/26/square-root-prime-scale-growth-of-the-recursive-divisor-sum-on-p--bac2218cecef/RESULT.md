# Square-root prime-scale growth of the recursive-divisor sum on primorials

## Finding
Let \(\kappa_1(1)=1\), and for every integer \(n\ge2\) define the recursive-divisor sum by
\[
\kappa_1(n)=n+\sum_{\substack{d\mid n\\1\le d<n}}\kappa_1(d).
\]
For real \(x\ge2\), put \(P(x)=\prod_{p\le x}p\), where all products indexed by \(p\) run over primes. Then
\[
\boxed{\lim_{x\to\infty}\frac{\log x}{\sqrt{x}}\log\!\left(\frac{\kappa_1(P(x))}{P(x)}\right)=2.}
\]
Equivalently, if \(p_k\) is the \(k\)-th prime and \(P_k=\prod_{i=1}^k p_i\), then
\[
\log\!\left(\frac{\kappa_1(P_k)}{P_k}\right)
=(2+o(1))\frac{\sqrt{p_k}}{\log p_k}\qquad(k\to\infty).
\]
All logarithms in the theorem and proof are natural. In particular, this is an asymptotic statement about the sum, *not* about the number, of recursive divisors.

## Assumptions and scope
The recurrence above is defined for every positive integer and is the \(x=1\) instance of Fink's recursive divisor function. The asymptotic uses the classical prime number theorem with its standard effective error term; it is unconditional. The theorem makes no uniform assertion for general, nonsquarefree integers. The exact identity in the next section is known as a specialization of the general Dirichlet-convolution series of Fink; the claimed contribution is the explicit leading asymptotic constant for the primorial subsequence.

## Proof
**1. Exact primorial series.** Write \({\bf1}(n)=1\), \(\mathrm{id}(n)=n\), and \(*\) for Dirichlet convolution. The defining recurrence is equivalent to
\[
\kappa_1=\tfrac12\mathrm{id}+\tfrac12({\bf1}*\kappa_1).
\]
Its convergent convolution expansion is
\[
\kappa_1=\sum_{r\ge0}2^{-r-1}\,{\bf1}^{*r}*\mathrm{id},
\]
where \({\bf1}^{*0}\) is the convolution identity. Indeed, for each fixed integer the coefficient of the \(r\)-th summand is a polynomial in \(r\), so the series converges absolutely and solves the recurrence. Both factors are multiplicative, and for a prime \(p\) the value of \({\bf1}^{*r}*\mathrm{id}\) is \(p+r\). Therefore for every real \(x\ge2\),
\[
\frac{\kappa_1(P(x))}{P(x)}
=\frac12\sum_{r=0}^{\infty}\exp(H_x(r)),\qquad
H_x(z)=\sum_{p\le x}\log\left(1+\frac{z}{p}\right)-z\log2,
\tag{1}
\]
for real \(z\ge0\). This exact identity is a reformulation of the known general convolution expansion, included here to fix the normalization used in the asymptotic.

**2. Two uniform prime-sum estimates.** For fixed \(0<a<b<\infty\), and \(z=t\sqrt{x}\) with \(t\in[a,b]\), we have uniformly as \(x\to\infty\)
\[
\begin{aligned}
\sum_{p\le x}\log(1+z/p)
 &=z(\log\log x-\log\log z)+\frac{z}{\log z}+o(z/\log z),\\
\sum_{p\le x}\frac1{p+z}
 &=\log\log x-\log\log z+o(1/\log z).
\end{aligned}\tag{2}
\]
Here are details of the constants and the error justification. The prime-number theorem in the effective form
\(\pi(y)=\operatorname{Li}(y)+O(y\exp(-c\sqrt{\log y}))\)
for some constant \(c>0\), followed by partial summation, gives
\[
\sum_{z<p\le x}\frac1p
=\log\log x-\log\log z+o(1/\log z)
\tag{3}
\]
uniformly in this range. Define integrable kernels
\[
\begin{aligned}
w(u)&=\log(1+u^{-1})-\mathbf1_{\{u>1\}}u^{-1},\\
v(u)&=(1+u)^{-1}-\mathbf1_{\{u>1\}}u^{-1}
\end{aligned}
\]
for \(u>0\). The prime-number theorem under the scaling \(p=zu\), together with partial summation, gives
\[
\sum_{p\le x}w(p/z)=\frac{z}{\log z}\int_0^\infty w(u)\,du+o(z/\log z),
\quad
\sum_{p\le x}v(p/z)=\frac{z}{\log z}\int_0^\infty v(u)\,du+o(z/\log z).
\tag{4}
\]
In the second equality the factor \(z^{-1}\) will be inserted to obtain a prime sum of reciprocals. To see that these are legitimate weighted limits rather than just bounded-interval approximations, first restrict \(u\) to \([\varepsilon,M]\), where uniform PNT and Riemann sums apply. At the origin, \(w(u)=O(1+|\log u|)\) and \(v(u)=O(1)\), giving an arbitrarily small normalized contribution when \(\varepsilon\downarrow0\). At infinity both kernels are \(O(u^{-2})\), giving an arbitrarily small contribution when \(M\uparrow\infty\). These estimates are uniform for \(t\in[a,b]\). Direct integration yields
\[
\begin{aligned}
\int_0^1\log(1+u^{-1})\,du&=2\log2,\\
\int_1^\infty(\log(1+u^{-1})-u^{-1})\,du&=1-2\log2,\\
\int_0^\infty v(u)\,du&=\log2-\log2=0.
\end{aligned}
\]
Consequently \(\int w=1\), \(\int v=0\). Subtracting the prime harmonic sum in (3) from the log sum gives the first relation (2) by (4). Applying (4) to \(v\), then dividing by \(z\) and using (3), gives the second. This proves both estimates with the leading constants shown.

**3. Location and size of the maximum.** With \(z=t\sqrt{x}\) in a fixed compact positive interval,
\[
\log\log x-\log\log z
=\log2-\frac{2\log t}{\log x}+O_{a,b}((\log x)^{-2}).
\]
Substituting (2) into the definitions gives, uniformly on that interval,
\[
H_x(t\sqrt{x})
=\frac{2t\sqrt{x}}{\log x}(1-\log t)+o(\sqrt{x}/\log x),
\tag{5}
\]
and
\[
H'_x(t\sqrt{x})
=\sum_{p\le x}\frac1{p+t\sqrt{x}}-\log2
=-\frac{2\log t}{\log x}+o(1/\log x).
\tag{6}
\]
Since \(H''_x(z)=-\sum_{p\le x}(p+z)^{-2}<0\), the function is strictly concave. Equation (6) shows that for all sufficiently large \(x\), its derivative is positive at \(\tfrac12\sqrt{x}\) and negative at \(2\sqrt{x}\). Its unique real maximizer \(z_x\) therefore lies between these two numbers. More precisely, for every fixed \(\varepsilon\in(0,1)\), the derivative signs at \((1-\varepsilon)\sqrt{x}\) and \((1+\varepsilon)\sqrt{x}\) imply \(z_x/\sqrt{x}\to1\). By (5),
\[
\max_{z\ge0}H_x(z)=(2+o(1))\frac{\sqrt{x}}{\log x}.
\tag{7}
\]
The same leading maximum applies over nonnegative integers \(r\): rounding \(z_x\) changes \(H_x\) by \(o(\sqrt{x}/\log x)\), using (6) and concavity (or the bounded curvature of \(H_x\) near the peak).

**4. From the maximum to the series.** Put \(M_x=\max_{r\ge0}H_x(r)\). In (1), the terms \(0\le r\le 2\sqrt{x}+1\) number \(O(\sqrt{x})\), so their sum is at most \(O(\sqrt{x})e^{M_x}\). By (6) and strict concavity, every real \(z\ge2\sqrt{x}\) has derivative at most \(-c_0/\log x\) for some absolute \(c_0>0\) and large \(x\). The remaining discrete terms are thus bounded by a geometric tail of order \(O(\log x)e^{M_x}\). A term at a maximizing integer supplies the opposite lower bound \(e^{M_x}\). Hence
\[
\log\left(\tfrac12\sum_{r\ge0}e^{H_x(r)}\right)=M_x+O(\log x).
\]
Since \(\log x=o(\sqrt{x}/\log x)\), (7) and (1) give the asserted limit of 2. Replacing \(x\) by the \(k\)-th prime yields the equivalent form. \(\square\)

## Verification
The standalone standard-library Python program `verify.py` implements (i) the recursive definition on all squarefree divisors of the first ten primorials, (ii) a second computation using the exact ordered-Bell-moment expansion of (1), and (iii) finite diagnostic maxima of \(H_x\) at selected prime cutoffs. It checks agreement of the two *exact integer* calculations for every \(1\le k\le10\). Its finite diagnostics are not evidence for the limiting constant, which is established analytically by the effective prime-number theorem and the weighted estimates (2)--(6). Execute `python3 verify.py` from the package directory.

## Relationship to prior work
Thomas Fink introduced \(\kappa_x\) in *Recursively divisible numbers* (first public arXiv version 17 December 2019). Its open-question list explicitly asks for \(\kappa_1(n)\) when \(n\) is a product of the first \(k\) distinct primes. Fink's *Properties of the recursive divisor function and the number of ordered factorizations* (2023) already proves the general convolution identity and infinite series used in step 1; neither the recurrence nor that series is claimed here as new. His *Number of ordered factorizations and recursive divisors* (2023) gives general closed forms for \(\kappa_0\) and the ordered-factorization count, rather than the primorial growth of \(\kappa_1\). The contribution is the prime-scale asymptotic for the normalized primorial recursive-divisor **sum**, with explicit leading constant 2, obtained by a prime-number-theorem saddle-point argument.

## Limitations
The result is asymptotic as \(x\to\infty\), and does not claim an effective error constant or a closed finite expression simpler than the known convolution expansion. Convergence of the numerical ratio is slow at accessible cutoffs, and finite tests do not certify the asymptotic. No asymptotic is claimed for \(\kappa_0\), other \(\kappa_x\), or unrestricted integers. Priority remains subject to a broader literature search for potentially unindexed results about primorial recursive-divisor sums.

## References
1. T. M. A. Fink, *Recursively divisible numbers*, arXiv:1912.07979 (first public version 2019-12-17), https://arxiv.org/abs/1912.07979 ; journal text at https://lims.ac.uk/documents/recursive-divisible-numbers.pdf .
2. T. M. A. Fink, *Properties of the recursive divisor function and the number of ordered factorizations*, arXiv:2307.09140 (2023), https://arxiv.org/abs/2307.09140 .
3. T. M. A. Fink, *Number of ordered factorizations and recursive divisors*, arXiv:2307.16691 (2023), https://arxiv.org/abs/2307.16691 ; full text at https://lims.ac.uk/documents/paper-number-of-ordered-factorizations-and-recursive-divisors.pdf .
4. H. Davenport, *Multiplicative Number Theory*, third edition, revised by H. L. Montgomery (Springer, 2000): prime number theorem and effective error bounds.
