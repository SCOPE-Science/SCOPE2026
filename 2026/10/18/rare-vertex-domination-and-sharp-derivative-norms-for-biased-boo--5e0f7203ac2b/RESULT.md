# Rare-vertex domination and sharp derivative norms for biased Boolean noise semigroups

## Finding

Let \(\mu=\bigotimes_{i=1}^n\mu_i\) be any strictly positive Bernoulli product probability measure on \(\Omega=\{0,1\}^n\). Write \(r_i\) for a less-probable symbol, with \(a_i=\mu_i(r_i)\le1/2\), and \(r=(r_i)\). Consider the resampling family
\[
K_\rho(x,y)=\prod_{i=1}^n\bigl[\rho\mathbf1_{x_i=y_i}+(1-\rho)\mu_i(y_i)\bigr],\qquad 0\le\rho\le1.
\]
The operator \(P_\rho f(x)=\sum_yK_\rho(x,y)f(y)\) acts on both real and complex \(L^1(\mu)\) and \(L^\infty(\mu)\). For every vertex \(x\) there is one **fixed, parameter-independent stochastic matrix** \(G_x\) such that
\[
K_\rho(x,\cdot)=K_\rho(r,\cdot)G_x\qquad\hbox{for every }\rho\in[0,1].
\]
Consequently, for any finite complex Borel measure \(\sigma\) on \([0,1]\) and \(R_\sigma=\int P_\rho\,d\sigma(\rho)\),
\[
\boxed{\|R_\sigma\|_{1\to1}=\|R_\sigma\|_{\infty\to\infty}=
\sum_{y\in\Omega}\left|\int K_\rho(r,y)\,d\sigma(\rho)\right|.}
\]
The same rare-vertex formula holds for \(\partial_\rho^kP_\rho\) for every \(k\ge0\), and for \(\partial_t^kP_{e^{-t}}\) for every \(t\ge0\), interpreting endpoint derivatives one-sided. These are *exact operator norms*, not upper estimates.

For equal rare masses \(a_i=a\le1/2\), put \(q=a+(1-a)\rho\) and define the binomial masses \(b_{m,q}(j)=\binom mjq^j(1-q)^{m-j}\), interpreted as zero when \(j\notin\{0,\ldots,m\}\). For integers \(1\le k\le n\),
\[
\boxed{\|\partial_\rho^kP_\rho\|_{1\to1}=(1-a)^k(n)_k
\sum_{j=0}^n\left|\sum_{\ell=0}^k(-1)^{k-\ell}\binom k\ell b_{n-k,q}(j-\ell)\right|,}
\]
where \((n)_k=n!/(n-k)!\). Higher derivatives with \(k>n\) vanish. The first derivative simplifies to a **single binomial boundary mass**:
\[
\boxed{\|\partial_\rho P_\rho\|_{1\to1}=2n(1-a)b_{n-1,q}\bigl(\min\{n-1,\lfloor nq\rfloor\}\bigr).}
\]
In physical time \(P_t=P_{e^{-t}}\), \(\|\partial_tP_t\|=e^{-t}\|\partial_\rho P_\rho\|_{\rho=e^{-t}}\).

The first-derivative profile has two distinct scales. At every fixed \(a\in(0,1/2]\) and fixed \(0\le\rho<1\),
\[
\|\partial_\rho P_\rho\|_{1\to1}\sim(1-a)\sqrt{\frac{2n}{\pi q(1-q)}}.
\]
More generally, for fixed \(k\ge1\), \(q\in(0,1)\), and a standard normal \(Z\),
\[
\boxed{\lim_{n\to\infty}n^{-k/2}\|\partial_\rho^kP_\rho\|_{1\to1}
=(1-a)^k[q(1-q)]^{-k/2}\mathbb E|\operatorname{He}_k(Z)|.}
\]
At the critical window \(q_n=1-\lambda/n\), \(\rho_n=(q_n-a)/(1-a)\) with fixed \(\lambda\ge0\),
\[
\boxed{\lim_{n\to\infty}n^{-1}\|\partial_\rho P_{\rho_n}\|_{1\to1}
=2(1-a)h(\lambda),}
\]
where \(h(0)=1\) and, for \(\lambda>0\),
\[
h(\lambda)=e^{-\lambda}\frac{\lambda^{\lceil\lambda\rceil-1}}{(\lceil\lambda\rceil-1)!}.
\]
At integer positive \(\lambda\), this formula equals the common height of the two Poisson modes. The critical limit is well-defined and continuous there.

## Assumptions and scope

All finite-dimensional measures are strictly positive. Each coordinate is binary and is updated independently. There is no requirement that the biases coincide for rare-vertex domination; equality of biases is used only to obtain the closed binomial formulas and asymptotics. The parameter interval \(0\le\rho\le1\) is essential to stochasticity of the coupling channel, though its polynomial identity continues algebraically. Values of \(\lambda\) in the critical-window limit are fixed as \(n\to\infty\), and \(\rho_n\in[0,1]\) for all sufficiently large \(n\). Derivatives of \(P_\rho\) are with respect to the *correlation* parameter, rather than physical time, unless explicitly designated otherwise.

## Proof

**Step 1 — parameter-independent binary garbling.** Rename a coordinate's rare and common symbols \(R,C\), with \(\mu(R)=a\le1/2\). Define a Markov kernel \(G\) on these symbols by
\[
G(R,R)=0,\quad G(R,C)=1,\quad
G(C,R)=\frac a{1-a},\quad G(C,C)=\frac{1-2a}{1-a}.
\]
Every entry is nonnegative and rows sum to one. Starting a noisy coordinate at \(R\) yields probability \(q_\rho=a+(1-a)\rho\) of reporting \(R\), whereas starting at \(C\) yields \(a(1-\rho)\). The channel sends the former law to the latter because \((1-q_\rho)a/(1-a)=a(1-\rho)\), for every \(\rho\). At coordinates where \(x_i=R\) use the identity, and where \(x_i=C\) use \(G\). Their tensor product \(G_x\) proves \(K_\rho(x,\cdot)=K_\rho(r,\cdot)G_x\) with **no dependence on the parameter**. The endpoint \(a=1/2\) is allowed, when \(G\) is the symbol swap.

**Step 2 — exact endpoint norms.** Let \(u_\rho\) be any integrable complex parameter combination of the rows \(K_\rho(r,\cdot)\). The identity above gives \(u_x=u_rG_x\) for each \(x\). The triangle inequality and row-stochasticity give \(\sum_y|u_x(y)|\le\sum_y|u_r(y)|\), with equality at \(x=r\). This computes the \(\ell^\infty\)-operator norm as the maximum row total variation. The kernels satisfy detailed balance \(\mu(x)K_\rho(x,y)=\mu(y)K_\rho(y,x)\); hence every parameter combination and derivative is **symmetric under the weighted bilinear pairing** (complex combinations need not be Hilbert-space self-adjoint). Weighted transpose symmetry makes each normalized column total variation identical to its corresponding row total variation, hence the \(L^1\) norm equals the \(L^\infty\) norm. Derivatives preserve the channel identity by parameter independence, and \(t\)-derivatives are combinations of the \(\rho\)-derivatives through \(\rho=e^{-t}\).

**Step 3 — binomial differences.** For identical rare masses \(a\), the rare-start law is a product of Bernoulli laws with rare probability \(q=a+(1-a)\rho\). Aggregate by the number \(j\) of rare outputs, giving \(b_{n,q}(j)\). Its \(k\)-th derivative with respect to \(q\) obeys, for all integers \(k\le n\),
\[
\frac{d^k}{dq^k}b_{n,q}(j)=(n)_k\sum_{\ell=0}^k(-1)^{k-\ell}\binom k\ell b_{n-k,q}(j-\ell).
\]
This follows by differentiating the binomial probability generating function \((1-q+qz)^n\): the right-hand generating function is \((n)_k(z-1)^k(1-q+qz)^{n-k}\). Multiply by \((1-a)^k\) for \(\rho\)-derivatives. Every level \(j\) has a common sign and the correct binomial multiplicity, so summing absolute values gives the formula.

For \(k=1\), the signed difference is \(n[b_{n-1,q}(j-1)-b_{n-1,q}(j)]\). Unimodality means it changes sign at a mode \(m=\min\{n-1,\lfloor nq\rfloor\}\). The positive and negative total masses each telescope to \(n b_{n-1,q}(m)\), including a possible two-mode tie. Multiplying by \((1-a)\) yields the exact first-derivative formula.

**Step 4 — fixed-order Hermite scaling.** Let \(B_n\sim\mathrm{Bin}(n,q)\), fix \(q\in(0,1)\), and define the score polynomial \(S_{n,k}(B_n)=(d^k/dq^k)b_{n,q}(B_n)/b_{n,q}(B_n)\). Its generating function is
\[
F_n(z)=\left(1+\frac zq\right)^{B_n}\left(1-\frac z{1-q}\right)^{n-B_n},
\quad S_{n,k}=k![z^k]F_n(z).
\]
For \(z=u/\sqrt n\), the central limit theorem and Taylor's formula imply coefficientwise convergence in distribution to the generating series \(\exp(uZ/\sqrt{q(1-q)}-u^2/[2q(1-q)])\); thus
\[
n^{-k/2}S_{n,k}(B_n)\Longrightarrow[q(1-q)]^{-k/2}\operatorname{He}_k(Z).
\]
Absolute first moments also converge: an exact second-moment identity is obtained from \(\mathbb EF_n(z)F_n(w)=(1+zw/[q(1-q)])^n\), namely
\[
\mathbb E\bigl|S_{n,k}(B_n)\bigr|^2=\frac{k!(n)_k}{[q(1-q)]^k}.
\]
After normalization these moments remain bounded, giving uniform integrability. The operator norm is \((1-a)^k\mathbb E|S_{n,k}(B_n)|\). The Gaussian-Hermite limit follows, including the stated first-derivative constant \(\mathbb E|Z|=\sqrt{2/\pi}\).

**Step 5 — critical Poisson window.** Set \(q_n=1-\lambda/n\). The binomial boundary mass \(b_{n-1,q_n}(m_n)\) is the maximal mass of the count of common outcomes, which is distributed as \(\mathrm{Bin}(n-1,\lambda/n)\). This law converges in total variation to \(\mathrm{Pois}(\lambda)\). Its maximum point mass converges to the Poisson modal probability \(h(\lambda)\), with the two adjacent modes agreeing when \(\lambda\) is a positive integer. The exact first-derivative identity gives \(n^{-1}\|\partial_\rho P_{\rho_n}\|\to2(1-a)h(\lambda)\). For \(\lambda=0\), the identity already holds at every \(n\).

## Verification

The standalone `check.py` uses exact rational arithmetic to enumerate all rows for several nonidentical bias vectors, all derivative orders, and five correlation parameters, and independently checks the binomial finite-difference and first-derivative formulas for all depths through eight. It reports **1,698 exact comparisons passed**. A separate numerical large-\(n\) sanity check compared the first-derivative formula against its Gaussian and Poisson limits; ratios approached one. These finite checks do not replace Steps 1–5 and make no claim of verifying the infinite-size limits by enumeration.

## Relationship to prior work

The resampling noise operator and biased Walsh expansions are classical. Pisier (2007) considers hypercontractive operator-semigroup and operator-ideal questions; Keller (2010) establishes a biased-to-unbiased Fourier reduction and biased hypercontractivity; and O'Donnell (2014) systematically develops product-space noise operators. Those established facts do not state an exact endpoint-derivative norm simultaneously for every unequal product bias and every derivative order, nor the parameter-independent rare-to-common kernel channel. The previously reported rare-vertex result for **first-chaos multipliers** covers the special value \(\rho=0\) and derivative order one; the present result concerns full positive-time noise derivatives (containing all Walsh levels), arbitrary derivative order, and an explicit critical-time crossover. Uniform degree-two Walsh projection formulas likewise cover an order-two special endpoint at \(\rho=0\), not the asserted parameter-uniform stochastic domination. The comparisons do not establish exhaustive bibliographic priority.

## Limitations

This is an endpoint \(L^1/L^\infty\) theorem, not a sharp \(L^p\) statement for other exponents. The finite signed-measure comparison is valid on the whole parameter interval, but its positivity proof uses \(0\le\rho\le1\). The closed binomial/Hermite/Poisson formulas require equal biases. The fixed-order Hermite limit assumes \(q\) bounded away from zero and one; it is not asserted in the moving critical window. No independent review or exhaustive historical-priority verification is claimed.

## References

1. G. Pisier, *A Remark on Hypercontractive Semigroups and Operator Ideals* (first public preprint August 25, 2007), arXiv:0708.3423, https://arxiv.org/abs/0708.3423. See Theorem 1 and its operator-ideal conclusion.
2. N. Keller, *A Simple Reduction from a Biased Measure on the Discrete Cube to the Uniform Measure* (first public preprint January 7, 2010), arXiv:1001.1167, https://arxiv.org/abs/1001.1167. See Definition 1.1 and Proposition 1.3.
3. R. O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press, first published 2014. See the chapters on product probability spaces and noise operators, https://www.analysisofbooleanfunctions.org/.
