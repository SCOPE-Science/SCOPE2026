# Sharp parity frontier for iid integration times in two-mode ideal Gaussian HMC

## Finding
Fix an oscillator frequency \(\omega>0\), an integer \(m\ge2\), and the Gaussian target
\[
\pi=\mathcal N\!\left(0,\operatorname{diag}(\omega^{-2},(m\omega)^{-2})\right).
\]
At every step of *ideal* Hamiltonian Monte Carlo (HMC), redraw momentum from \(\mathcal N(0,I_2)\), evolve the exact Hamiltonian flow for a nonnegative time \(T\), and discard momentum. Let the integration times be independent and identically distributed (iid), with an otherwise unrestricted probability law \(\nu\) on \([0,\infty)\), independent of the momenta and the state. Consider the squared Euclidean discrepancy in a synchronous coupling that uses identical times and identical refreshed momenta.

Define the sharp uniform one-step mean-square factor
\[
R_m=\inf_{\nu}\max\{\mathbb E_\nu[\cos^2(\omega T)],\mathbb E_\nu[\cos^2(m\omega T)]\}.
\]
Then, exactly,
\[
\boxed{R_m=\begin{cases}0,&m\text{ odd},\\[2pt]
\sin^2\!\left(\frac{\pi}{2(m+1)}\right),&m\text{ even}.\end{cases}}
\]
For odd \(m\), the complete class of optimizing laws consists of those supported on \(\omega T\equiv\pi/2\pmod\pi\). For even \(m\), all and only optimizing laws are supported on the two phase classes
\[
\omega T\equiv\frac\pi2\pm\frac{\pi}{2(m+1)}\pmod\pi.
\]
In particular, a *single deterministic integration time* achieves the optimum for every \(m\); iid randomizing the integration duration cannot yield a strictly better worst-initial-direction mean-square coupling factor. With the same iid law for \(K\ge1\) steps, the corresponding sharp worst-direction factor is exactly \(R_m^K\).

For frequency ratio \(m=2\), the optimum is \(R_2=1/4\), attained at \(T=\pi/(3\omega)\). For \(m=4\), it is \(R_4=(3-\sqrt5)/8\), attained at \(T=2\pi/(5\omega)\). For odd \(m\), a single step with \(T=\pi/(2\omega)\) gives an exact, fresh draw from the two-dimensional Gaussian target.

## Assumptions and scope
The two frequencies are precisely \(\omega\) and \(m\omega\) with integer \(m\ge2\). The kinetic energy is Euclidean, the mass matrix is the identity, and the potential is the exact positive-definite quadratic \(\tfrac12\omega^2x_1^2+\tfrac12m^2\omega^2x_2^2\). The refreshed momenta are independent standard normals. The same law is used independently at each iteration and is independent of all chain randomness. There is no time-budget or upper-duration constraint. The objective is the worst-direction, normalized synchronous-coupling *expected squared Euclidean distance*, not integrated autocorrelation, total variation, implementation cost, or optimal Wasserstein coupling.

All times are allowed, including arbitrary multiples of oscillator periods. The optimizer classes are characterized modulo \(\pi\) in the phase \(\omega T\), with the additional requirement \(T\ge0\).

## Proof
**Step 1: exact coupling identity.** The equations for mode \(i\) are \(\dot x_i=p_i\) and \(\dot p_i=-\omega_i^2x_i\), with \(\omega_1=\omega\) and \(\omega_2=m\omega\). Exact integration for time \(T_k\) and fresh standard normal \(Z_{k,i}\) gives
\[
x_{k+1,i}=\cos(\omega_iT_k)x_{k,i}+\omega_i^{-1}\sin(\omega_iT_k)Z_{k,i}.
\]
The target is invariant: the variance of each updated coordinate is \(\omega_i^{-2}(\cos^2+\sin^2)=\omega_i^{-2}\), and cross-coordinate covariance remains zero after conditional independent Gaussian momentum refreshment (or, equivalently, by exact Hamiltonian preservation for every fixed integration time).

Couple two chains by using the same \(T_k\) and \(Z_{k,i}\). For their deterministic initial discrepancy \(d\), momentum terms cancel and
\[
D_{K,i}=d_i\prod_{k=0}^{K-1}\cos(\omega_iT_k).
\]
Thus independence of the times yields the *exact* identity
\[
\mathbb E\|D_K\|_2^2=|d_1|^2a^K+|d_2|^2b^K,
\quad a=\mathbb E\cos^2(\omega T),\quad b=\mathbb E\cos^2(m\omega T).
\]
The supremum over \(d\ne0\), normalized by \(\|d\|_2^2\), is \(\max(a,b)^K\). There is no unjustified interchange of an expectation with an optimization: the diagonal expression gives the supremum exactly.

**Step 2: odd ratios.** If \(m\) is odd, \(\omega T=\pi/2\pmod\pi\) makes both cosines zero. As a nonnegative squared expectation vanishes exactly when its integrand vanishes almost surely, \(a=0\) forces this same phase condition. Hence \(R_m=0\) and all its optimizers are precisely the stated distributions. Both coordinates then consist only of their fresh Gaussian momentum terms, so the position is an independent draw from \(\pi\) after one step.

**Step 3: a sharp even-frequency inequality.** For even integer \(m\ge2\), put
\[
\delta=\frac{\pi}{2(m+1)},\qquad c=\sin^2\delta.
\]
We prove the pointwise supporting inequality, including its equality cases,
\[
\boxed{m\cos^2\theta+\cos^2(m\theta)\ge(m+1)c,}
\]
with equality if and only if \(\theta\equiv\pi/2\pm\delta\pmod\pi\).

Let \(s\in[0,\pi/2]\) be the distance of \(\theta\) from \(\pi/2\) modulo \(\pi\). By evenness of \(m\), the left side equals
\[
F(s)=m\sin^2s+\cos^2(ms).
\]
On \(0<s<\pi/(2m)\), differentiate:
\[
F'(s)=m(\sin2s-\sin2ms)
=-2m\sin((m-1)s)\cos((m+1)s).
\]
The first factor is positive. The cosine changes sign exactly once, at \(s=\delta\), in this interval. Hence \(F\) decreases strictly until \(\delta\), then increases strictly until \(\pi/(2m)\). At that unique local minimum,
\[
F(\delta)=m\sin^2\delta+\cos^2(m\delta)
=(m+1)\sin^2\delta=(m+1)c,
\]
because \(m\delta=\pi/2-\delta\).

It remains to exclude all later lobes. If \(s\ge\pi/(2m)\), then \(F(s)\ge m\sin^2(\pi/(2m))\). The function \(g(u)=\sin^2u/u\) is strictly increasing on \((0,\pi/4]\):
\[
g'(u)=\frac{\sin u\,(2u\cos u-\sin u)}{u^2}>0,
\]
where \(\tan u\le 4u/\pi<2u\) for \(0<u\le\pi/4\) by convexity of tangent (its graph lies below the secant from \((0,0)\) to \((\pi/4,1)\)). For clarity, the strict comparison can be checked directly: \(\tan u/u\) increases from \(1\) to \(4/\pi<2\), so \(2u>\tan u\). Therefore, since \(\delta<\pi/(2m)\le\pi/4\),
\[
m\sin^2\!\left(\frac\pi{2m}\right)
=\frac\pi2g\!\left(\frac\pi{2m}\right)
>\frac\pi2g(\delta)
=(m+1)c.
\]
This proves the inequality globally, with equality exclusively at \(s=\delta\), or the two stated phase classes.

**Step 4: exact minimax and all optimizers.** Integrating the pointwise inequality against any probability measure on \(T\) gives \(ma+b\ge(m+1)c\), whence \(\max(a,b)\ge c\). At either equality phase, \(\cos^2\theta=\cos^2(m\theta)=c\), so any law supported on those phases attains \(a=b=c\). Conversely, if \(\max(a,b)=c\), then the weighted inequality must be an equality after integrating a nonnegative function. This is possible only when its pointwise equality set has probability one. Thus the stated phase condition is necessary and sufficient. The exact \(K\)-step factor follows from Step 1 and monotonicity of raising nonnegative numbers to the \(K\)-th power. This completes the proof.

## Verification
Run `python3 verify.py` using the standalone standard-library script included with this finding. It independently evaluates the claimed optimizer for integer frequency ratios from \(2\) through \(32\), checks the weighted inequality on dense phase grids for even ratios, checks the radical identities for ratios \(2\) and \(4\), and compares against finitely supported random duration mixtures. These finite checks are consistency evidence only; the universal bound, all-law quantifier, phase optimizer classification, and all-step conclusion are established by the proof above.

## Relationship to prior work
Wang and Wibisono, *Accelerating Hamiltonian Monte Carlo via Chebyshev Integration Time* (arXiv:2207.02189, first public July 5, 2022), analyze prescribed iteration-dependent Chebyshev integration-time sequences and Gaussian convergence. Their nonstationary cosine-product bounds do not identify an optimizer among all *iid* time laws for a two-frequency, integer-ratio spectrum.

Apers, Gribling, and Szilágyi, *Hamiltonian Monte Carlo for efficient Gaussian sampling: long and random steps* (arXiv:2209.12771, first public September 26, 2022), establish multidimensional TV mixing guarantees using a particular random-time distribution and explicitly derive products of cosine factors. Their results motivate the exact cosine-risk optimization, but their displayed arguments do not supply the integer-parity minimax law or its complete equality cases.

Jiang, *On the Dissipation of Ideal Hamiltonian Monte Carlo Sampler* (arXiv:2209.07438, first public September 15, 2022), studies quadratic dissipation using fixed integration time and partial velocity refreshment; those transition matrices and objectives do not imply this arbitrary-iid-law minimax. Bou-Rabee and Sanz-Serna, *Randomized Hamiltonian Monte Carlo* (arXiv:1511.09382), examine random durations, ergodicity, and sampling efficiency rather than the exact unrestricted two-frequency mean-square optimum. Established ideal-HMC harmonic-flow and cosine-product formulas are used as background, not claimed as new.

## Limitations
This is a closed-form result for **two** commensurate oscillator frequencies with an **integer** ratio, fresh full Gaussian momentum replacement, and unrestricted exact integration durations. The result does not compare policies with unequal integration costs, different random-time laws at successive steps, state-dependent durations, accept/reject corrections, discretized Hamiltonian dynamics, more than two frequencies, or nonquadratic targets. A predetermined multi-time schedule can null the two oscillator modes in successive steps even when the sharp one-step iid factor is positive; therefore this finding makes no lower-bound claim about such schedules. The computed synchronous-coupling factor bounds a Wasserstein-2 discrepancy under that coupling but is not asserted to be a sharp Wasserstein-2 mixing rate or a total-variation guarantee. Equivalent trigonometric inequalities under different terminology or specialized HMC priority not found in the inspected literature remain possible.

## References
1. J.-K. Wang and A. Wibisono, *Accelerating Hamiltonian Monte Carlo via Chebyshev Integration Time*, arXiv:2207.02189, July 5, 2022. https://arxiv.org/abs/2207.02189 ; full text https://arxiv.org/html/2207.02189v2 .
2. S. Apers, S. Gribling and D. Szilágyi, *Hamiltonian Monte Carlo for efficient Gaussian sampling: long and random steps*, arXiv:2209.12771, September 26, 2022. https://arxiv.org/abs/2209.12771 ; full text https://arxiv.org/html/2209.12771v1 .
3. Q. Jiang, *On the Dissipation of Ideal Hamiltonian Monte Carlo Sampler*, arXiv:2209.07438, September 15, 2022. https://arxiv.org/html/2209.07438v3 .
4. N. Bou-Rabee and J. M. Sanz-Serna, *Randomized Hamiltonian Monte Carlo*, arXiv:1511.09382, November 2015. https://arxiv.org/html/1511.09382v2 .
