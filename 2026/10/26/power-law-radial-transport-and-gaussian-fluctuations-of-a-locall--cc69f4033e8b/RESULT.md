# Power-law radial transport and Gaussian fluctuations of a locally infinite quantum walk

## Finding
For the continuous-time walk on the graph of finite subsets of positive integers, with coordinate-flip weights \(w_k=c k^{-\alpha}\), \(c>0\) and \(\alpha>1\), let \(R_t\) denote the graph distance from the empty set of the measured vertex at time \(t>0\), starting from the empty-set basis state. Put \(\beta=1/\alpha\) and
\[
K_\alpha=2^{\beta-1}\Gamma(1-\beta)\cos(\pi\beta/2)>0.
\]
Then, as \(t\to+\infty\),
\[
\mathbb E R_t\sim K_\alpha(ct)^\beta,\qquad
\operatorname{Var}(R_t)\sim 2^{\beta-2}K_\alpha(ct)^\beta.
\]
Consequently the exact asymptotic Fano ratio is
\[
\lim_{t\to\infty}\frac{\operatorname{Var}(R_t)}{\mathbb E R_t}=2^{\beta-2}\in(1/4,1/2),
\]
and the radial position obeys
\[
\frac{R_t-\mathbb E R_t}{\sqrt{\operatorname{Var}(R_t)}}\ \Longrightarrow\ N(0,1),\qquad
\frac{R_t}{K_\alpha(ct)^\beta}\ \longrightarrow\ 1\quad\text{in probability}.
\]
In fact, the Kolmogorov distance of the standardized law from the standard normal is \(O(t^{-\beta/2})\). The radial spreading exponent \(1/\alpha\) and both constants are sharp asymptotic equivalents, rather than bounds with unspecified factors.

## Assumptions and scope
Let \(\Gamma\) consist of the finite subsets \(\sigma\subset\{1,2,\ldots\}\). The Hilbert space is \(\ell^2(\Gamma)\) with basis \(e_\sigma\), and the commuting, self-adjoint coordinate flips act by \(X_k e_\sigma=e_{\sigma\triangle\{k\}}\). For fixed \(\alpha>1\) and \(c>0\), define the bounded self-adjoint Hamiltonian
\[
A=\sum_{k=1}^{\infty} c k^{-\alpha} X_k,
\]
where the series converges in operator norm. Initialize \(\psi_0=e_\varnothing\), evolve \(\psi_t=e^{-itA}\psi_0\), and measure in the canonical vertex basis: \(\Pr_t\{\sigma\}=|\langle e_\sigma,\psi_t\rangle|^2\). The combinatorial graph connects vertices differing in exactly one coordinate, so \(R_t=|\sigma|\) for the measured vertex. Time is deterministic, no random temporal disorder is introduced, and all probability statements refer to this one-time Born distribution. Reindexing coordinates changes none of the results; the cited model numbers coordinates from zero.

## Proof
**1. Exact product law.** The finite-coordinate Hamiltonian \(A_n=\sum_{k=1}^n c k^{-\alpha}X_k\) has commuting involutory terms, hence
\[
e^{-itA_n}e_\varnothing=\prod_{k=1}^n\left(\cos(tck^{-\alpha})I-i\sin(tck^{-\alpha})X_k\right)e_\varnothing.
\]
As \(\sum_k ck^{-\alpha}<\infty\), \(A_n\to A\) in norm, and the finite-product states converge in Hilbert norm for every fixed \(t\). Their coordinate measurements are independent Bernoulli bits with parameters \(p_k(t)=\sin^2(tck^{-\alpha})\). Since \(\sum_kp_k(t)\le (ct)^2\sum_k k^{-2\alpha}<\infty\), the infinite product measure is supported on finite subsets. Convergence of finite Born distributions in total variation follows from Hilbert-norm convergence of the states (measurement contraction). Therefore the exact law of \(R_t\) is that of a sum of countably many independent Bernoulli variables, with generating function and moments
\[
\mathbb E z^{R_t}=\prod_{k\ge1}[1+(z-1)p_k(t)],\qquad
\mu_t:=\mathbb E R_t=\sum_{k\ge1}p_k(t),
\]
\[
V_t:=\operatorname{Var}(R_t)=\sum_{k\ge1}p_k(t)(1-p_k(t))=\frac14\sum_{k\ge1}\sin^2(2tck^{-\alpha})=\frac14\mu_{2t}.
\]
These statements remain valid even at times when some individual cosine factors vanish.

**2. Sharp mean asymptotic.** Set \(N=(ct)^\beta\) and \(f(x)=\sin^2(x^{-\alpha})\) for \(x>0\). Then \(\mu_t=\sum_{k\ge1}f(k/N)\). The function is bounded by one, continuous away from the origin, and satisfies \(f(x)\le x^{-2\alpha}\) for \(x\ge1\). For arbitrary \(0<\delta<1<L\), the terms with \(k<\delta N\) contribute at most \(\delta N+1\); the central interval \([\delta,L]\) has the standard Riemann-sum limit; and the normalized tail \(k>LN\) is bounded by \(L^{1-2\alpha}/(2\alpha-1)+o(1)\), using the integral bound on \(\sum k^{-2\alpha}\). The integral of \(f\) on \((0,\delta)\) is at most \(\delta\). Letting \(\delta\downarrow0\) and \(L\uparrow\infty\) proves
\[
\frac{\mu_t}{(ct)^\beta}\longrightarrow\int_0^\infty\sin^2(x^{-\alpha})\,dx.
\]
With \(u=x^{-\alpha}\), \(\beta=1/\alpha\), this integral equals
\[
\frac\beta2\int_0^\infty(1-\cos(2u))u^{-1-\beta}\,du
=2^{\beta-1}\Gamma(1-\beta)\cos(\pi\beta/2)=K_\alpha.
\]
For completeness, the evaluation uses integration by parts of the absolutely convergent \((1-\cos v)v^{-1-\beta}\) integral, followed by the classical Abel-regularized sine integral \(\int_0^\infty v^{-\beta}\sin v\,dv=\Gamma(1-\beta)\cos(\pi\beta/2)\), valid for \(0<\beta<1\). The prefactor after the substitution \(v=2u\) is \(2^{\beta-1}\), as stated.

**3. Variance and fluctuations.** The exact identity \(V_t=\mu_{2t}/4\) and the mean limit give \(V_t\sim2^{\beta-2}K_\alpha(ct)^\beta\), so \(V_t\to\infty\) and the Fano ratio follows. For each \(t\), write \(R_t=\sum_k B_{k,t}\) with independent \(B_{k,t}\in\{0,1\}\). Every centered summand has absolute value at most one, while the sum of their variances is \(V_t\to\infty\); hence the Lindeberg condition holds and the normalized sum converges weakly to \(N(0,1)\). The standard Berry--Esseen inequality for independent non-identical bounded summands also applies: because \(\sum_k\mathbb E|B_{k,t}-p_k(t)|^3\le\sum_k p_k(t)(1-p_k(t))=V_t\), its bound is \(C V_t^{-1/2}=O(t^{-\beta/2})\). Both arguments extend from finite truncations because for each fixed \(t\) their sums converge in \(L^2\). Finally \(V_t/\mu_t^2\to0\), and Chebyshev's inequality yields the law of large numbers in probability.

## Verification
The identities \(p(1-p)=\frac14\sin^2(2\theta)\) and \(V_t=\mu_{2t}/4\) can be checked algebraically. The appended standalone `verify.py` numerically tests these equalities on finite coordinate truncations and compares radial means and Fano ratios against the analytic large-time constants for several values of \(\alpha\). The calculations are diagnostic only. The infinite-dimensional support, Riemann-sum limit, gamma-integral evaluation, central limit theorem and rate are established by the proof above, not by finite samples or numerical logs.

## Relationship to prior work
Ce Wang, *Continuous-Time Quantum Walk on Locally Infinite Graph* (arXiv:2602.23970v1, first public 27 February 2026), introduces exactly the summable-weight coordinate-flip graph dynamics and proves operator-norm/spectral and time-reversal results. Its Sections 2--4 and the references were inspected. The present statement uses a natural positive power-law subclass of its weighted Hamiltonians and addresses a separate long-time observable: graph-distance expectation, fluctuations and exact asymptotic constants. The source does not state or prove these asymptotics. Ce Wang, *Abstract Model of Continuous-Time Quantum Walk Based on Bernoulli Functionals and Perfect State Transfer* (arXiv:2212.00020), studies finite-dimensional hypercubes and transfer, not this locally infinite power-law limit. The 2018 *Quantum Walk in Terms of Quantum Bernoulli Noise and Quantum Central Limit Theorem for Quantum Bernoulli Noise* (DOI:10.1155/2018/2507265) treats different discrete-time dynamics with a coin, not the present radial Born distribution. Generic independent-sum central limit principles are established background; the new calculation is their identification with, and explicit asymptotic evaluation for, this particular quantum walk.

## Limitations
This theorem requires \(\alpha>1\) so the defining positive weighted adjacency is bounded by absolute summability; no claim is made for \(\alpha\le1\), non-power-law weights, correlated initial states or quantum-observable fluctuations under repeated measurements. The radial variable is *combinatorial Hamming graph distance*, not an edge-weighted physical distance or a coordinate-resolved ballistic front. The Gaussian law is a one-time Born-measure limit, not a process-level invariance principle. The Berry--Esseen rate need not be sharp. Literature originality is best-knowledge rather than a proof of priority; related generic tensor-product techniques may imply intermediate identities without recording these final power-law asymptotics.

## References
1. Ce Wang, *Continuous-Time Quantum Walk on Locally Infinite Graph*, arXiv:2602.23970v1 (27 February 2026), https://arxiv.org/html/2602.23970v1.
2. Ce Wang, *Abstract Model of Continuous-Time Quantum Walk Based on Bernoulli Functionals and Perfect State Transfer*, arXiv:2212.00020 (2022), https://arxiv.org/abs/2212.00020.
3. C. Wang, C. Wang, Y. Tang and S. Ren, *Quantum Walk in Terms of Quantum Bernoulli Noise and Quantum Central Limit Theorem for Quantum Bernoulli Noise*, *Advances in Mathematical Physics* (2018), article 2507265, https://doi.org/10.1155/2018/2507265.
4. Classical Lindeberg--Feller central limit theorem, Berry--Esseen inequality for independent summands, and the Euler gamma sine-transform identity (standard results; their hypotheses are checked above).
