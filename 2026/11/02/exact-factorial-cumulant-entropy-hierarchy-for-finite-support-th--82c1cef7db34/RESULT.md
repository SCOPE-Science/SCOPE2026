# Exact factorial-cumulant entropy hierarchy for finite-support thinning

## Finding

Let \(X\) be a nonnegative, integer-valued random variable with finite support and mean \(\lambda>0\). For independent copies \(X_1,X_2,\ldots\), define
\[
Y_n=T_{1/n}(X_1+\cdots+X_n),
\]
where \(T_a\) retains each of the underlying count's units independently with probability \(a\). Let \(\pi_\lambda\) denote the Poisson law of mean \(\lambda\). The factorial cumulants \(\kappa_j\) of \(X\) are defined locally by
\[
\log\mathbb E(1+z)^X=\sum_{j\ge1}\frac{\kappa_j}{j!}z^j,
\qquad \kappa_1=\lambda.
\]
Assume that for some integer \(r\ge2\), \(\kappa_2=\cdots=\kappa_{r-1}=0\) and \(\kappa_r\ne0\). Define the degree-\(r\) Poisson–Charlier polynomial
\[
C_r(k;\lambda)=\sum_{j=0}^r\binom rj(-\lambda)^{r-j}(k)_j,
\qquad (k)_j=k(k-1)\cdots(k-j+1),\quad(k)_0=1.
\]
Then the three following *exact leading asymptotics* hold as \(n\to\infty\):
\[
\boxed{\begin{aligned}
n^{2r-2}\chi^2(\mathcal L(Y_n)\Vert\pi_\lambda)&\longrightarrow\frac{\kappa_r^2}{r!\lambda^r},\\
n^{2r-2}D(\mathcal L(Y_n)\Vert\pi_\lambda)&\longrightarrow\frac{\kappa_r^2}{2r!\lambda^r},\\
n^{r-1}d_{\rm TV}(\mathcal L(Y_n),\pi_\lambda)&\longrightarrow
\frac{|\kappa_r|}{2r!\lambda^r}\,\mathbb E_{N\sim\pi_\lambda}|C_r(N;\lambda)|.
\end{aligned}}
\]
The Kullback–Leibler divergence uses natural logarithms, \(\chi^2(P\Vert Q)=\sum_k(P(k)-Q(k))^2/Q(k)\), and \(d_{\rm TV}=\frac12\sum_k|P(k)-Q(k)|\).

Every polynomial information-decay order is realized by a non-Poisson finite-support input. In particular, for every integer \(m\ge2\), the polynomial
\[
G_m(z)=\sum_{j=0}^{m}\frac{z^j}{j!}
\]
can be written \(G_m(z)=\mathbb E(1+z)^{X^{(m)}}\), where \(X^{(m)}\) is supported on \(\{0,\ldots,m\}\) with
\[
\Pr(X^{(m)}=k)=\frac1{k!}\sum_{h=0}^{m-k}\frac{(-1)^h}{h!}\ge0.
\]
Its mean is \(1\), its factorial cumulants \(\kappa_2,\ldots,\kappa_m\) vanish, and \(\kappa_{m+1}=-1\). For independent copies of this law,
\[
\boxed{\lim_{n\to\infty}n^{2m}
D\bigl(T_{1/n}(X_1^{(m)}+\cdots+X_n^{(m)})\Vert\operatorname{Poisson}(1)\bigr)
=\frac1{2(m+1)!}.}
\]
For example, \(\Pr(X=0)=\Pr(X=2)=1/2\) gives \(\lambda=1\), \(r=3\), and limit \(n^4D\to1/12\), whereas the law supported on \(\{0,1,3\}\) with probabilities \((1/3,1/2,1/6)\) gives \(n^6D\to1/48\).

## Assumptions and scope

All random variables are defined on an ordinary probability space; the observations \(X_i\) are independent and identically distributed; conditional on the count, each of its constituent units is retained independently. The support bound \(M=\max\{k:\Pr(X=k)>0\}\) is fixed as \(n\to\infty\), and \(\lambda=\mathbb EX>0\) is fixed. No ultra-log-concavity or full support is required. The integer \(r\) is the first index after the mean at which the factorial cumulant differs from that of the Poisson law. Every non-Poisson finite-support law with positive mean has such a finite index, because its factorial moment generating function is a polynomial rather than an exponential.

The theorem makes no uniform claim when \(M\), \(r\), or \(\lambda\) change with \(n\), and no claim for unbounded-support inputs. The construction gives one law for each *fixed* exponent; it does not assert a single non-Poisson input with superpolynomial convergence.

## Proof

**1. The exact orthogonal identity.** For \(N\sim\pi_\lambda\), the generating function
\[
e^{-\lambda z}(1+z)^N=\sum_{j\ge0}C_j(N;\lambda)\frac{z^j}{j!}
\]
combined with
\[
\mathbb E_{\pi_\lambda}\bigl[e^{-\lambda(z+w)}(1+z)^N(1+w)^N\bigr]
=e^{\lambda zw}
\]
shows that \(\mathbb E_{\pi_\lambda}[C_jC_k]=\mathbf1_{j=k}j!\lambda^j\). Write \(p_n(k)=\Pr(Y_n=k)\), \(q(k)=e^{-\lambda}\lambda^k/k!\), and \(u_n=p_n/q-1\). The density \(p_n/q\) is in \(L^2(\pi_\lambda)\): since \(Y_n\) is stochastically dominated by \(\operatorname{Binomial}(nM,1/n)\), the factorial-moment Markov bound gives \(p_n(k)\le M^k/k!\); consequently \(p_n(k)/q(k)\le e^\lambda(M/\lambda)^k\), whose square is Poisson-integrable.

Let \(G(z)=\mathbb E(1+z)^X\) and \(H_n(z)=e^{-\lambda z}G(z/n)^n\). Writing \(H_n(z)=\sum_{j\ge0}a_{n,j}z^j\), we have \(a_{n,0}=1\) and \(a_{n,j}=\mathbb E[C_j(Y_n;\lambda)]/j!\). Therefore Parseval's identity for the Charlier orthogonal basis is
\[
\chi^2(\mathcal L(Y_n)\Vert\pi_\lambda)
=\sum_{j\ge1}\frac{j!}{\lambda^j}|a_{n,j}|^2.
\]
Equivalently, by orthogonality of complex monomials in the Gaussian plane,
\[
\chi^2(\mathcal L(Y_n)\Vert\pi_\lambda)
=\frac{\lambda}{\pi}\int_{\mathbb C}|H_n(z)-1|^2e^{-\lambda|z|^2}\,dA(z).
\]
The Charlier basis is complete: the generating function and polynomial density in the Poisson \(L^2\) space establish the identity without assuming finite expansions.

**2. Strong Charlier asymptotics.** Since \(G(0)=1\), \(G\) is nonzero on a sufficiently small disk about zero, and the analytic branch of \(L(z)=\log G(z)-\lambda z\) satisfies
\[
L(z)=\frac{\kappa_r}{r!}z^r+O(z^{r+1}).
\]
Thus for each fixed complex \(z\),
\[
n^{r-1}[H_n(z)-1]
=n^{r-1}[\exp(nL(z/n))-1]
\longrightarrow\frac{\kappa_r}{r!}z^r.
\]
This convergence also holds in the weighted planar \(L^2\) norm. Indeed, choose \(\delta>0\) such that \(|L(w)|\le C|w|^r\) for \(|w|\le\delta\). In the inner region \(|z|\le\delta n\), for all sufficiently large \(n\),
\[
|nL(z/n)|\le C\frac{|z|^r}{n^{r-1}}
\le \frac{\lambda}{16}|z|^2,
\]
because \(r\ge2\). The elementary inequality \(|e^w-1|\le|w|e^{|w|}\) then gives the integrable majorant
\[
n^{2r-2}|H_n(z)-1|^2e^{-\lambda|z|^2}
\le C^2|z|^{2r}e^{-7\lambda|z|^2/8}.
\]
Outside the disk, finite support implies \(|G(z/n)|\le\exp(M|z|/n)\), and hence \(|H_n(z)|\le\exp((M+\lambda)|z|)\). The Gaussian-weighted integral of \(n^{2r-2}(1+e^{(M+\lambda)|z|})^2\) over \(|z|>\delta n\) tends to zero exponentially. Dominated convergence on the inner disk and this tail estimate prove the claimed strong convergence.

Since the squared Gaussian-plane norm of \(z^r\) is \(r!/\lambda^r\), it follows that
\[
n^{2r-2}\chi^2(\mathcal L(Y_n)\Vert\pi_\lambda)
\longrightarrow \frac{\kappa_r^2}{r!\lambda^r}.
\]
Under the coefficient-isometry back to Poisson \(L^2\), the same argument gives the stronger statement
\[
n^{r-1}u_n\longrightarrow
\frac{\kappa_r}{r!\lambda^r}C_r(\,\cdot\,;\lambda)
\quad\text{in }L^2(\pi_\lambda).
\]
Here the placeholder dot in \(C_r(\,\cdot\,;\lambda)\) denotes the integer argument. The \(L^2\)-to-\(L^1\) implication and continuity of the \(L^1\) norm give the total-variation limit.

**3. Entropy has half the quadratic coefficient.** Define
\[
\psi(t)=\begin{cases}
\dfrac{(1+t)\log(1+t)-t}{t^2},&t\ne0,\\
\frac12,&t=0.
\end{cases}
\]
On \([-1,\infty)\), \(\psi\) is nonnegative, bounded and continuous, including at \(-1\) by continuity of \(x\log x\). Since \(\mathbb E_{\pi_\lambda}u_n=0\),
\[
D(\mathcal L(Y_n)\Vert\pi_\lambda)
=\mathbb E_{\pi_\lambda}[u_n^2\psi(u_n)].
\]
The strong convergence above implies \(u_n\to0\) in \(\pi_\lambda\)-probability, and that the family \(n^{2r-2}u_n^2\) is uniformly integrable. Hence
\[
n^{2r-2}D\longrightarrow
\frac12\mathbb E_{\pi_\lambda}
\left[\left(\frac{\kappa_r}{r!\lambda^r}C_r\right)^2\right]
=\frac{\kappa_r^2}{2r!\lambda^r}.
\]
This controls the infinite Poisson tail and does not rely on a pointwise Taylor expansion without uniform integrability.

**4. Every order occurs.** Expanding \(G_m(s-1)\) in powers of \(s\) gives exactly the stated masses. Every alternating partial sum of \(e^{-1}\) is nonnegative, so these masses define a probability distribution. Its factorial generating function is \(G_m(z)\), and \(G_m(z)-e^z=-z^{m+1}/(m+1)!+O(z^{m+2})\). Consequently
\[
\log G_m(z)-z=-\frac{z^{m+1}}{(m+1)!}+O(z^{m+2}),
\]
proving \(\kappa_{m+1}=-1\) and all intervening vanishing cumulants. Apply the general theorem with \(r=m+1\) and \(\lambda=1\).

## Verification

The included `verify.py` is a standalone Python standard-library checker; its recorded output is `verification_output.json`. It checks exact rational masses, exact factorial moments and truncated Charlier generating coefficients for \(2\le m\le10\), \(1\le n\le20\), as well as high-precision discrete KL and \(\chi^2\) values for \(m=2,3,4\) and \(n=20,40,80\). In the recorded execution, all \(1368\) assertions passed. At \(n=80\), the scaled relative entropies for \(m=2,3,4\) were approximately \(0.0833909632\), \(0.0208439494\) and \(0.0041693810\), approaching \(1/12\), \(1/48\), and \(1/240\), respectively. These are finite checks; the universal and asymptotic conclusions follow from the proof above.

To reproduce: run `python3 verify.py` from a directory containing `verify.py` and compare the printed JSON object with `verification_output.json`. No external packages, data, or unpublished software are needed.

## Relationship to prior work

Kavvadias, *Thinning Operation via the Poisson–Föllmer Process* (arXiv:2608.02927, public August 3, 2026), gives information-theoretic thinning results and an \(n^2\)-scaled divergence upper bound under a bounded-density condition; it does not give a general exact leading \(n^{2r-2}\) coefficient when lower factorial cumulants cancel. The earlier Harremoës–Johnson–Kontoyiannis *Thinning and Information Projections* (arXiv:1601.04255, Theorem 22) gives the corresponding all-order **lower bound** for the information divergence, not equality for finite-support inputs. Their higher-order Poisson–Charlier viewpoint and lower bound are essential antecedents, not claimed here as new.

Zacharovas and Hwang, *A Charlier–Parseval Approach to Poisson Approximation and Its Applications* (arXiv:0810.4756, Sections 1–5), establish the foundational orthogonal identity and important second-order approximations, notably for Poisson-binomial laws. The present proof uses this established identity; its specific contribution is the strong \(L^2\) thinning limit, the exact relative-entropy and total-variation constants across every cancellation order, and finite-support witnesses realizing arbitrarily high orders. Classical general Poisson expansion techniques may yield related estimates; no claim of exclusive method or definitive historical priority is made.

## Limitations

This statement is confined to a fixed finitely supported input distribution and to independent thinning with parameter \(1/n\). It does not establish the same sharp entropy coefficient for arbitrary unbounded-support inputs with merely finitely many moments. The historical-priority assessment is provisional: stronger older general Charlier expansions might imply some special cases even without the same formulation. Finite arithmetic tests are not proofs of the limiting statement. Independent mathematical validation has not been performed.

## References

1. I. Kavvadias, *Thinning Operation via the Poisson–Föllmer Process*, arXiv:2608.02927, first posted 2026-08-03. https://arxiv.org/abs/2608.02927
2. P. Harremoës, O. Johnson, I. Kontoyiannis, *Thinning and Information Projections*, arXiv:1601.04255, Theorem 22. https://arxiv.org/abs/1601.04255
3. V. Zacharovas, H.-K. Hwang, *A Charlier–Parseval Approach to Poisson Approximation and Its Applications*, arXiv:0810.4756. https://arxiv.org/abs/0810.4756
4. P. Harremoës, O. Johnson, I. Kontoyiannis, *Thinning, Entropy, and the Law of Thin Numbers*, arXiv:0906.0690. https://arxiv.org/abs/0906.0690
