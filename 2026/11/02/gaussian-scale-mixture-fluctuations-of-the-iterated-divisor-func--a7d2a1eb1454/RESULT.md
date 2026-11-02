# Gaussian scale-mixture fluctuations of the iterated divisor function

## Finding
For every positive integer \(n\), let \(\tau(n)\) be its number of positive divisors. Decompose
\[
 n=A(n)B(n),\qquad B(n)=\prod_{p^e\parallel n,\ e\ge2}p^e,
\]
so that \(A(n)\) is squarefree and \(\gcd(A(n),B(n))=1\). Define \(U(n)\ge0\) and the odd positive integer \(V(n)\) uniquely by \(\tau(B(n))=2^{U(n)}V(n)\), and put \(W(n)=\tau(V(n))\).

For real \(X>e\), take \(N_X\) uniformly from \(\{1,\ldots,\lfloor X\rfloor\}\), write \(L_X=\log\log X\), and set
\[
Z_X=\frac{\tau(\tau(N_X))/W(N_X)-L_X}{\sqrt{L_X}},\qquad
T_X=\frac{\tau(\tau(N_X))-W(N_X)L_X}{\sqrt{L_X}}=W(N_X)Z_X.
\]
Let \(\mathcal B\) be the positive powerful integers, including \(1\), and define
\[
\rho_\beta=\frac{1}{\zeta(2)\beta}\prod_{p\mid\beta}\frac{p}{p+1},\qquad
w_\beta=\tau\bigl(\operatorname{odd}(\tau(\beta))\bigr)\quad (\beta\in\mathcal B),
\]
where \(\operatorname{odd}(m)=m/2^{\nu_2(m)}\), and an empty product equals \(1\).

**Theorem.** The numbers \(\rho_\beta\) form a probability distribution. Let \(B_\infty\) have this distribution and let \(G\) be a standard normal variable independent of \(B_\infty\). Then, in the product of the discrete topology on \(\mathcal B\) and the usual topology on \(\mathbb R\),
\[
\boxed{(B(N_X),Z_X)\ \xrightarrow{d}\ (B_\infty,G).}
\]
Consequently,
\[
\boxed{(W(N_X),T_X)\ \xrightarrow{d}\ (w_{B_\infty},w_{B_\infty}G),}
\]
and the scalar centered fluctuations converge to the **non-Gaussian Gaussian scale mixture** with characteristic function
\[
\boxed{\lim_{X\to\infty}\mathbb E[e^{itT_X}]
 =\sum_{\beta\in\mathcal B}\rho_\beta
 \exp\!\left(-\frac{t^2w_\beta^2}{2}\right),\qquad t\in\mathbb R.}
\]
The mixing measure is not degenerate: \(\Pr(w_{B_\infty}=1)\ge1/\zeta(2)>0\), and \(\Pr(w_{B_\infty}=2)\ge1/(6\zeta(2))>0\). Its smallest-scale atom has the explicit Euler product
\[
\boxed{\Pr(w_{B_\infty}=1)=\prod_p
 \left(1-\frac1p\right)\left(\sum_{j=0}^{\infty}p^{-(2^j-1)}\right).}
\]
The product converges to a strictly positive value (numerically approximately \(0.68783\)).

## Assumptions and scope
All assertions concern positive integers and the fixed uniform sampling window \(1\le n\le X\) as \(X\to\infty\). No assumption of squarefreeness on the sampled integers is made. The conventions at \(n=1\) are \(A(1)=B(1)=V(1)=W(1)=1\), \(U(1)=0\). The theorem is about convergence in distribution, not convergence of second or higher moments of \(T_X\). Its mixing measure is explicitly atomic in the scale variable, but the resulting fluctuation law is continuous.

## Proof
**1. Exact decomposition.** Prime factorization gives \(\tau(n)=\tau(A(n))\tau(B(n))=2^{\omega(A(n))+U(n)}V(n)\). As \(V(n)\) is odd,
\[
\boxed{\tau(\tau(n))=(\omega(A(n))+U(n)+1)W(n).}\tag{1}
\]
This identity holds also at \(n=1\). It shows that the only unbounded first-order contribution is the number of prime factors of the squarefree part; the randomly varying powerful part fixes a multiplicative scale.

**2. Densities of powerful fibers.** Fix \(\beta\in\mathcal B\). The condition \(B(n)=\beta\) is equivalent to \(n=\beta a\) with \(a\) squarefree and \(\gcd(a,\beta)=1\). Standard squarefree counting with finitely many excluded primes gives
\[
\#\{a\le y:\mu(a)^2=1,\ (a,\beta)=1\}
 =\frac y{\zeta(2)}\prod_{p\mid\beta}\frac p{p+1}+o_\beta(y).
\]
Thus \(\Pr(B(N_X)=\beta)\to\rho_\beta\). To show these masses sum to one, factor the absolutely convergent series:
\[
\begin{aligned}
\sum_{\beta\in\mathcal B}\rho_\beta
 &=\frac1{\zeta(2)}\prod_p\left(1+\frac p{p+1}\sum_{e\ge2}p^{-e}\right)\\
 &=\frac1{\zeta(2)}\prod_p\left(1+\frac1{p^2-1}\right)=1.
\end{aligned}
\]
The tail is uniformly negligible because
\[
\Pr(B(N_X)>H)\le\sum_{\substack{\beta\in\mathcal B\\\beta>H}}\frac1\beta\longrightarrow0,
\]
and the last series converges: every powerful integer has a unique expression \(u^2v^3\) with \(v\) squarefree, so its reciprocal sum is bounded by \(\zeta(2)\zeta(3)\).

**3. Conditional Gaussian law.** Fix \(\beta\in\mathcal B\). On the fiber \(B(N_X)=\beta\), the variable \(A(N_X)\) is uniformly distributed among squarefree integers \(a\le X/\beta\) coprime to \(\beta\). The following fixed-exclusion squarefree form of the classical Erdős–Kac theorem applies:
\[
\frac{\omega(a)-\log\log y}{\sqrt{\log\log y}}\xrightarrow{d}G
\quad\text{as }y\to\infty
\]
when \(a\) is uniform among squarefree positive integers \(\le y\) coprime to a fixed \(\beta\). For clarity, its analytic justification is the factorization
\[
\sum_{\substack{a\ge1\\\mu(a)^2=1,\ (a,\beta)=1}}\frac{z^{\omega(a)}}{a^s}
 =\zeta(s)^z H_\beta(s,z),\qquad
 H_\beta(s,z)=\prod_p(1-p^{-s})^z(1+zp^{-s})
 \prod_{p\mid\beta}(1+zp^{-s})^{-1}.
\]
The Euler factors of \(H_\beta\) are \(1+O(p^{-2\operatorname{Re}s})\) away from the finitely many excluded primes. In a fixed complex neighborhood of \(z=1\), the standard Selberg–Delange estimate therefore yields
\[
\sum_{\substack{a\le y\\\mu(a)^2=1,\ (a,\beta)=1}}
 z^{\omega(a)}=y(\log y)^{z-1}\left(C_\beta(z)+O_\beta((\log y)^{-1})\right),
\]
with \(C_\beta(z)=H_\beta(1,z)/\Gamma(z)\) analytic and nonzero near \(1\). Substituting \(z=\exp(it/\sqrt{\log\log y})\), dividing by the \(z=1\) count and centering proves that the characteristic functions converge to \(\exp(-t^2/2)\). The finite excluded primes do not change this limit.

For fixed \(\beta\), \(\log\log(X/\beta)=L_X+o(1)\) and \(U(\beta)+1\) is constant. Identity (1) gives
\[
Z_X\bigm|\{B(N_X)=\beta\}
 =\frac{\omega(A(N_X))+U(\beta)+1-L_X}{\sqrt{L_X}}
 \xrightarrow{d}G.
\]

**4. Independence and mixture.** Let \(f:\mathcal B\times\mathbb R\to\mathbb R\) be bounded and continuous (with \(\mathcal B\) discrete). Split its expectation according to \(B(N_X)\le H\) and \(B(N_X)>H\). Each term of the finite sum converges by Steps 2 and 3; the remainder is uniformly bounded by \(\|f\|_\infty\sum_{\beta>H,\,\beta\in\mathcal B}\beta^{-1}\). Letting \(H\to\infty\) gives
\[
\lim_{X\to\infty}\mathbb E f(B(N_X),Z_X)
 =\sum_{\beta\in\mathcal B}\rho_\beta\,\mathbb E f(\beta,G).
\]
This is exactly joint convergence to an independent pair. The stated scaled mixture follows by the continuous mapping theorem, since \(W(n)=w_{B(n)}\) and \(T_X=W(N_X)Z_X\).

**5. Non-Gaussianity and smallest-scale atom.** The fiber \(\beta=1\) has \(w_1=1\) and mass \(1/\zeta(2)\); the fiber \(\beta=4\) has \(w_4=\tau(3)=2\) and mass \(1/(6\zeta(2))\). Hence the scale distribution has at least two distinct atoms. By uniqueness of Laplace transforms, a nontrivial mixture of centered normal characteristic functions with different variances cannot be a single centered Gaussian. Finally, \(w_\beta=1\) precisely when the odd part of \(\tau(\beta)\) is \(1\); equivalently every prime exponent \(e\ge1\) in a sampled integer is of the form \(2^j-1\) with \(j\ge1\). At each prime \(p\), exponent \(e\) occurs with natural density \((1-1/p)p^{-e}\). Multiplying the independent local densities gives the stated Euler product. Its factors equal \(1+O(p^{-2})\), so the product converges positively.

## Verification
The supplementary Python program `verify.py` performs independent direct divisor counting and factorization, rather than reusing the asymptotic proof. On integers \(1\le n\le200000\) it verified identity (1) exactly in all \(200000\) cases, enumerated \(886\) observed powerful fibers, and compared eight fixed-fiber frequencies against their exact predicted densities. A prime-truncated Euler product for the event \(W=1\) gave approximately \(0.687827\), versus empirical frequency \(0.687870\) in this finite range. The finite experiment cannot establish the conditional Erdős–Kac law, weak convergence, or novelty.

Run: `python3 verify.py --bound 200000` using Python 3 standard library only.

## Relationship to prior work
John M. Campbell, *On divisor sums due to Erdős and Ramanujan*, arXiv:2605.00695 (initially public 1 May 2026), establishes a first-order asymptotic for the reciprocal of \(\tau(\tau(n))\). Its Lemmas 7–9 give the exact squarefree/powerful decomposition, density of each powerful part, and mean control of the reciprocal after scaling by \(\log\log X\). Those findings establish neither the conditional centered Gaussian fluctuations at the \(\sqrt{\log\log X}\) scale nor the joint independence and non-Gaussian scale-mixture law here. The exact decomposition itself is not claimed as new; the new conclusion uses the classical Erdős–Kac/ Selberg–Delange mechanism on each fixed powerful fiber and a uniform tail argument.

The earlier work of Buttkewitz, Elsholtz, Ford, and Schlage-Puchta, *A problem of Ramanujan, Erdős and Kátai on the iterated divisor function* (arXiv:1108.1815), addresses maximal order rather than this centered probabilistic limit. The unrestricted Erdős–Kac theorem and its fixed-exclusion squarefree variant supply the standard Gaussian input, not the mixture formula for iterated divisors.

## Limitations
The theorem provides weak convergence only. It gives neither a quantitative uniform Berry–Esseen rate over unbounded powerful factors nor moment convergence for the unstudentized mixture. The Gaussian component uses the classical Selberg–Delange/Erdős–Kac theorem as a cited analytic input. The priority check is best-knowledge, not an independent literature certification; a different formulation in older probabilistic-number-theory work could overlap. Numeric finite checks are corroborative only.

## References
1. J. M. Campbell, *On divisor sums due to Erdős and Ramanujan*, arXiv:2605.00695v1 (1 May 2026) and arXiv:2605.00695v2 (16 October 2026), https://arxiv.org/abs/2605.00695.
2. P. Erdős and M. Kac, *The Gaussian Law of Errors in the Theory of Additive Number Theoretic Functions*, American Journal of Mathematics **62** (1940), 738–742, https://doi.org/10.2307/2371483.
3. Y. Buttkewitz, C. Elsholtz, K. Ford, and J.-C. Schlage-Puchta, *A problem of Ramanujan, Erdős and Kátai on the iterated divisor function*, arXiv:1108.1815, https://arxiv.org/abs/1108.1815.
4. G. Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, Selberg–Delange and Erdős–Kac results (standard analytic input).
