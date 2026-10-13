# Gaussian cutoff and the critical-dephasing window for hypercube quantum walks

## Finding

The independently dephased continuous-time quantum walk on the \(n\)-dimensional hypercube has a sharp **Gaussian total-variation cutoff profile**, and its critical damping boundary has a logarithmic-logarithmic delay and a nontrivial finite-width crossover. The model and its one-coordinate evolution are those of Alagic and Russell (2005); the large-dimensional cutoff assertions below concern its measured vertex distribution.

Fix \(k>0\), start from vertex \(0^n\), let \(p_n\) be its decoherence parameter and write \(P_{n,p_n,t}\) for the position distribution at time \(t\), and \(U_n\) for the uniform distribution. Use the **normalized** total variation \(d_{\mathrm{TV}}(P,U)=\frac12\sum_x|P(x)-U(x)|\). Define \(\Phi\) to be the standard normal distribution function and \(G(c)=2\Phi(e^{-c}/2)-1\).

**Near-critical window.** For any sequence \(p_n\ge4k\) with
\[
\frac{(p_n-4k)(\log n)^2}{8k}\longrightarrow\theta^2,\qquad 0\le\theta<\infty,
\]
set \(g(\theta)=\sinh(\theta)/\theta\) when \(\theta>0\), and \(g(0)=1\). Let \(u_n>0\) be the unique solution
\[
(1+u_n)e^{-u_n}=n^{-1/2}.
\]
Then, for each fixed real \(c\),
\[
\boxed{\displaystyle
 d_{\mathrm{TV}}\!\left(P_{n,p_n,\frac{n}{2k}(u_n+c)},U_n\right)
 \longrightarrow 2\Phi\!\left(\frac{g(\theta)e^{-c}}{2}\right)-1.}
\]
Equivalently, using the shifted centering \(t_n(c)=\frac{n}{2k}(u_n+\log g(\theta)+c)\), the limiting profile is \(G(c)\). The critical center has the expansion
\[
\boxed{u_n=\tfrac12\log n+\log\log n-\log2+o(1).}
\]
Thus even at the exactly critical rate \(p_n=4k\), the additive delay \(\frac{n}{2k}\log\log n\) beyond the leading \(n\log n\) scale is necessary. The nonconstant function \(g(\theta)\) shows that the distinguished decoherence window has width \((\log n)^{-2}\).

**Fixed overdamping.** For every fixed \(p>4k\), put
\[
\alpha=\sqrt{p^2-16k^2},\qquad \lambda=\frac{p-\alpha}{2},\qquad A=\frac12\left(1+\frac{p}{\alpha}\right).
\]
Then the centered times \(t_n(c)=\frac n\lambda(\frac12\log n+\log A+c)\) satisfy
\[
\boxed{d_{\mathrm{TV}}(P_{n,p,t_n(c)},U_n)\longrightarrow G(c).}
\]
For \(0<\epsilon<1\), define \(c_\epsilon=-\log[2\Phi^{-1}((1+\epsilon)/2)]\). The first \(\epsilon\)-mixing time (which is also the all-later-times mixing time here) satisfies \(T_{n,p_n}(\epsilon)=\frac{n}{2k}(u_n+\log g(\theta)+c_\epsilon)+o(n)\) in the near-critical window, and \(T_{n,p}(\epsilon)=\frac n\lambda(\frac12\log n+\log A+c_\epsilon)+o(n)\) in fixed overdamping.

## Assumptions and scope

The dimension is an integer \(n\ge2\); time is continuous and nonnegative; \(k>0\) is fixed; each coordinate has Hamiltonian \(kX/n\) and independent computational-basis dephasing at rate \(p_n/n\). Explicitly, the density matrix satisfies
\[
\frac{d\rho}{dt}=-i\left[\frac{k}{n}\sum_{j=1}^n X_j,\rho\right]
 +\frac{p_n}{n}\sum_{j=1}^n(\Delta_j(\rho)-\rho),
\]
where \(\Delta_j\) dephases coordinate \(j\). The initial state is \(|0^n\rangle\langle0^n|\). Position means simultaneous measurement in the computational basis. Only \(p_n\ge4k\) is covered, including exactly critical, near-critical, and fixed-overdamped regimes; the dimension-dependent family in the first assertion need not have constant decoherence intensity. The hypotheses are quantified along **every** integer sequence \(n\to\infty\) meeting the displayed parameter conditions and for **each fixed** \(c\) or \(\epsilon\).

## Proof

**1. Exact one-coordinate dynamics.** The Lindblad generator is a sum of commuting local generators and the input is a tensor product. Therefore the measured law is exactly the \(n\)-fold product of the Bernoulli law with probability \((1+z)/2\) of outcome zero. The single-qubit Bloch equation implies
\[
 z''(t)+\frac{p_n}{n}z'(t)+\frac{4k^2}{n^2}z(t)=0,
 \quad z(0)=1,\quad z'(0)=0.
\]
For \(p_n>4k\), with \(\alpha_n=\sqrt{p_n^2-16k^2}\), the unique solution is
\[
 z(t)=e^{-p_nt/(2n)}\left[\cosh\!\left(\frac{\alpha_nt}{2n}\right)
 +\frac{p_n}{\alpha_n}\sinh\!\left(\frac{\alpha_nt}{2n}\right)\right].
\]
At \(p_n=4k\), its continuous limit is \(z(t)=e^{-2kt/n}(1+2kt/n)\). These identities reproduce the explicit source solution, not an additional novelty claim.

**2. Gaussian product comparison.** Suppose \(0<z_n<1\) and \(\sqrt n\,z_n\to a\in(0,\infty)\). For a uniform binary string \(x\), write \(S_n=n^{-1/2}\sum_{j=1}^n(1-2x_j)\). The log likelihood of the biased product law relative to uniform is
\[
 \log L_n(x)=\sum_{j=1}^n\log(1+z_n(1-2x_j))
 =\sqrt n\,z_n S_n-\frac{n z_n^2}{2}+o_{U_n}(1).
\]
Under \(U_n\), \(S_n\) converges to \(N(0,1)\); under the biased product law, it converges to \(N(a,1)\), by the bounded triangular-array central limit theorem. The optimal likelihood-ratio test \(L_n\ge1\) therefore tends to the threshold \(S_n\ge a/2\). Taking the difference of its probabilities under the two laws proves
\[
 d_{\mathrm{TV}}(P_{n,z_n},U_n)\longrightarrow2\Phi(a/2)-1.
\]
This normal-shift limit is a standard probabilistic comparison; the contribution below is the exact dynamical centering and parameter crossover.

**3. The near-critical scaling.** Put \(L=\log n\), \(\delta_n=p_n-4k\), \(u=2kt/n\), and \(y=\alpha_n u/(4k)\). The exact bias from Step 1 can be rewritten, with \(\operatorname{sinhc}(y)=\sinh(y)/y\) and its continuous value one at zero, as
\[
 z=e^{-u}\exp\!\left(-\frac{\delta_n u}{4k}\right)
 \left[\cosh(y)+\frac{p_nu}{4k}\operatorname{sinhc}(y)\right].
\]
From \(\delta_nL^2/(8k)\to\theta^2\), we get \(\delta_nL\to0\), \(\alpha_n L/(8k)\to\theta\). The defining equation for \(u_n\) is equivalent to \(u_n-\log(1+u_n)=L/2\). Hence \(u_n/L\to1/2\) and then \(u_n=L/2+\log L-\log2+o(1)\). At \(u=u_n+b\) for fixed \(b\), we obtain \(y\to\theta\), \(\exp(-\delta_n u/(4k))\to1\), and
\[
 \frac{\cosh y+(p_nu/(4k))\operatorname{sinhc} y}{1+u_n}
 \longrightarrow g(\theta).
\]
Since \(e^{-u_n}(1+u_n)=n^{-1/2}\), it follows that \(\sqrt n\,z\to e^{-b}g(\theta)\). Choosing \(b=c\) or \(b=\log g(\theta)+c\) and applying Step 2 proves the two near-critical profile assertions, including the boundary \(\theta=0\).

**4. Fixed overdamping.** For fixed \(p>4k\), the bias from Step 1 is also
\[
 z=Ae^{-\lambda t/n}+Be^{-\mu t/n},\quad
 A=\frac12(1+p/\alpha),\quad B=\frac12(1-p/\alpha),\quad
 \mu=\frac{p+\alpha}{2}>\lambda>0.
\]
With \(t=\frac n\lambda(\frac12L+\log A+c)\), the first term has \(\sqrt n\)-scaled limit \(e^{-c}\); the second has limit zero because \(\mu/\lambda>1\). Step 2 proves the profile.

**5. Mixing times.** At critical damping, \(z=e^{-u}(1+u)\) is positive and strictly decreasing in \(u>0\). For \(p>4k\), differentiation gives \(z'(t)=-\frac{4k^2}{\alpha n}(e^{-\lambda t/n}-e^{-\mu t/n})<0\) for \(t>0\). A binary symmetric channel maps a larger positive bias to any smaller positive bias while fixing uniform; tensorization and data processing make the total-variation distance nonincreasing. The limiting profile \(G(c)\) is continuous, strictly decreasing from one to zero. Bracketing the first \(\epsilon\)-crossing between the centered times with \(c=c_\epsilon\pm\eta\) for each \(\eta>0\) proves the stated \(o(n)\) mixing-time expansions.

## Verification

The standard-library-only program `verify.py` reconstructs the exact one-coordinate bias, solves the critical center by bisection, evaluates finite-dimensional total variation by the exact binomial likelihood-ratio tail, and checks monotonicity. It covers dimensions \(512,2048,8192\), damping \(p=4k\), fixed \(p>4k\), and a near-critical sequence with \(\theta=1/2\), at three positions in each cutoff window. The program reports `VERIFY_OK`. The finite checks are **not** an exhaustive proof of the asymptotic limits; Steps 1–5 provide that proof. Relatively slow convergence at critical damping is expected from corrections of order \(\log\log n/\log n\).

## Relationship to prior work

Alagic and Russell (2005) derive the local qubit evolution and prove \(\Theta(n\log n)\) spatial mixing for fixed \(p\ge4k\), including the critical defective-root solution. The new claim does **not** reassert their exact dynamics as original. It specifies the sharp Gaussian profile, cutoff centering, \(\log\log n\) delay, all fixed tolerances, and the window \(p_n-4k\asymp(\log n)^{-2}\), which are not contained in their order bound.

Drezgich, Hines, Sarovar and Sastry (2008/2009) treat arbitrary qubit decoherence axes and bound variation using Hellinger comparison. Section IV expressly does not attempt the dependence on growing \(n\); their global dynamical generality does not imply this dimension-dependent cutoff profile or double scaling. Strauch (2008/2009) analyzes a distinct *vertex* dephasing model that loses tensor-product factorization, rather than the present subspace model. Marquezino and collaborators (2007/2008) analyze a discrete-time walk with random link breaking. Classical Bernoulli local asymptotic normality underlies Step 2 and is not claimed as new.

## Limitations

The result applies to the normalized total variation of the *measured vertex distribution*, not trace-distance mixing of the full quantum state. It assumes independent computational-basis dephasing with the prescribed rate normalization and an initial cube corner. It does not describe the underdamped regime \(p_n<4k\), general decoherence axes, or the intermediate regime in which \((p_n-4k)(\log n)^2\) diverges while \(p_n\to4k\). No conclusion is made about an optimal dephasing strength or algorithmic speedup. The classification of originality is literature-dependent and awaits independent priority review.

## References

- G. Alagic and A. Russell, *Decoherence in quantum walks on the hypercube*, arXiv:quant-ph/0501169 (initial public version 2005-01-28); Phys. Rev. A 72, 062304 (2005). https://arxiv.org/abs/quant-ph/0501169
- M. Drezgich, A. P. Hines, M. Sarovar and S. Sastry, *Complete Characterization of Mixing Time for the Continuous Quantum Walk on the Hypercube with Markovian Decoherence Model*, arXiv:0811.4472 (2008). https://arxiv.org/abs/0811.4472
- F. W. Strauch, *Reexamination of decoherence in quantum walks on the hypercube*, arXiv:0808.3403 (2008). https://arxiv.org/abs/0808.3403
- F. L. Marquezino, R. Portugal, G. Abal and R. Donangelo, *Mixing Times in Quantum Walks on the Hypercube*, arXiv:0712.0625 (2007). https://arxiv.org/abs/0712.0625
- V. Kendon, *Decoherence in quantum walks — a review*, Math. Struct. Comput. Sci. 17 (2007), Section 6.3, doi:10.1017/S0960129507006354. https://doi.org/10.1017/S0960129507006354
