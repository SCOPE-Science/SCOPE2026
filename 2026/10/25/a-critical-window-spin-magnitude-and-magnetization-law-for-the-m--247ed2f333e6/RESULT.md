# A critical-window spin-magnitude and magnetization law for the mean-field quantum Heisenberg ferromagnet

## Finding

Let \(n\ge2\) spin-half particles have total-spin components \(S_n^\alpha=\frac12\sum_{i=1}^n\sigma_i^\alpha\) and Hamiltonian \(H_n=-n^{-1}\sum_{\alpha=x,y,z}(S_n^\alpha)^2\). Let \(\rho_{n,\beta}=e^{-\beta H_n}/Z_n(\beta)\). For any fixed \(t\in\mathbb R\), put \(\beta_n=2+t/\sqrt n\), and let \(J_n\in\{0,1,\dots,n/2\}\) (even \(n\)) or \(J_n\in\{1/2,3/2,\dots,n/2\}\) (odd \(n\)) be the measured total-spin quantum number. Define
\[
I_t=\int_0^\infty y^2\exp\!\left(t y^2-\frac43 y^4\right)dy.
\]
Then, without an assumption on the parity of \(n\), the following limiting laws hold.

**Spin-magnitude distribution and partition function.** \(J_n/n^{3/4}\) converges in distribution, and in every fixed polynomial moment, to a variable \(Y_t\ge0\) with density
\[
f_t(y)=\frac{y^2 e^{t y^2-4y^4/3}}{I_t}\,\mathbf1_{\{y\ge0\}}.
\]
Furthermore,
\[
\lim_{n\to\infty}\frac{Z_n(\beta_n)}{2^n n^{3/4}}
=8\sqrt{\frac2\pi}\,I_t,
\qquad
\lim_{n\to\infty}\frac{Z_n(2+t/\sqrt n)}{Z_n(2)}=\frac{I_t}{I_0}.
\]

**Measured magnetization distribution.** Let \(M_n\) be the outcome of measuring \(S_n^z\) in \(\rho_{n,\beta_n}\). Then \(M_n/n^{3/4}\) converges to \(Y_t U\), where \(U\) is independent of \(Y_t\) and is uniform on \([-1,1]\). Its density is
\[
g_t(z)=\frac1{2I_t}\int_{|z|}^\infty y\exp\!\left(t y^2-\frac43y^4\right)dy\quad(z\in\mathbb R).
\]
Exactly at criticality this reduces to the non-Gaussian complementary-error-function profile
\[
g_0(z)=\frac{\sqrt\pi(4/3)^{1/4}}{2\Gamma(3/4)}\,
\operatorname{erfc}\!\left(\sqrt{4/3}\,z^2\right).
\]
Finally, the exact susceptibility scaling function is
\[
\lim_{n\to\infty}n^{-3/2}\operatorname{Var}_{\rho_{n,\beta_n}}(S_n^z)
=\frac{I_t'}{3I_t},
\]
with \(I_0'/3I_0=\frac{\sqrt3}{6}\Gamma(5/4)/\Gamma(3/4)\). It interpolates as \(I_t'/3I_t\sim 1/(2|t|)\) for \(t\to-\infty\), and \(I_t'/3I_t\sim t/8\) for \(t\to+\infty\) (limits taken after the thermodynamic limit).

## Assumptions and scope

There is no magnetic field, anisotropy, inhomogeneous interaction, or assumption on the parity of \(n\). The normalization \(H_n=-\mathbf S_n^2/n\) is essential: its critical inverse temperature is \(2\). The parameter \(t\) is held fixed as \(n\to\infty\). The results concern equilibrium Gibbs measurements; they do not assert a gap estimate for a Gibbs-sampling Lindbladian in the moving-temperature window. Convergence of moments refers to each individually fixed nonnegative integer power. \(\Gamma\) and \(\operatorname{erfc}\) have their standard Euler-gamma and complementary-error-function meanings.

## Proof

**1. Exact finite-dimensional spin-sector mass.** The \(\mathrm{SU}(2)\) representation decomposes as \(\bigoplus_{s\in\mathcal S_n}V_s\otimes\mathbb C^{m_{n,s}}\), with \(\dim V_s=2s+1\) and
\[
m_{n,s}=\binom n{n/2-s}-\binom n{n/2-s-1}
=\frac{2s+1}{n/2+s+1}\binom n{n/2-s}.
\]
The convention is that binomial coefficients with a negative lower index are zero. All lower arguments \(n/2-s\) are integers. The energy on this sector is \(-s(s+1)/n\). Hence the exact (unnormalized) sector mass is
\[
W_{n,t}(s)=\frac{(2s+1)^2}{n/2+s+1}
\binom n{n/2-s}
\exp\!\left(\frac{(2+t/\sqrt n)s(s+1)}n\right).
\]
The partition function is \(Z_n(\beta_n)=\sum_{s\in\mathcal S_n}W_{n,t}(s)\). There is no extra degeneracy factor outside this formula.

**2. Uniform critical-window local asymptotics.** Write \(y=s/n^{3/4}\). Standard Stirling expansion of the binomial in the regime \(s=O(n^{3/4})\) yields, uniformly for \(y\) in any fixed compact interval of \([0,\infty)\),
\[
\log\binom n{n/2-s}
=n\log2-\frac12\log n+\frac12\log(2/\pi)
-\frac{2s^2}{n}-\frac{4s^4}{3n^3}+o(1),
\]
where this form also holds at \(s=0\) and at half-integer spin with the stipulated lattice convention. Moreover,
\[
\frac{(2s+1)^2}{(n/2+s+1)n^{1/2}}\longrightarrow8y^2,
\]
and \(\beta_n s(s+1)/n=2s^2/n+t s^2/n^{3/2}+o(1)\) uniformly on these compacts. Thus
\[
\sup_{s/n^{3/4}\le R}\left|
\frac{W_{n,t}(s)}{2^n}-8\sqrt{\frac2\pi}\,y^2
 e^{t y^2-4y^4/3}\right|\to0
\quad\text{for every finite }R.
\]
This identity includes \(y\to0\), since the exact prefactor is bounded by a constant times \((y+n^{-3/4})^2\) on bounded intervals.

**3. Tail domination (not merely a pointwise Laplace argument).** Put \(p=1/2-s/n\). The binary relative entropy satisfies
\[
D(p\|1/2)=2(s/n)^2+\frac43(s/n)^4+
\sum_{j\ge3}c_j(s/n)^{2j},\qquad c_j>0.
\]
For \(0\le s\le n/4\), the uniform binomial upper bound and the exact rational prefactor imply, for \(t\) in any fixed compact interval, and \(y=s/n^{3/4}\),
\[
\frac{W_{n,t}(s)}{2^n}
\le C(1+y^2)\exp\!\left(Ty^2-\frac43y^4\right),
\quad |t|\le T.
\]
The factor \(e^{O(s/n)}\) is uniformly bounded. For \(n/4<s\le n/2\), the same entropy inequality provides exponential decay in \(n\) after canceling the \(2s^2/n\) energy term; any remaining polynomial prefactor is immaterial. These estimates also hold after multiplying the summand by any fixed power \(y^k\). Because the mesh spacing in \(y\) is \(n^{-3/4}\), dominated Riemann sums yield
\[
\frac{\sum_sW_{n,t}(s)\varphi(s/n^{3/4})}{2^n n^{3/4}}
\longrightarrow8\sqrt{2/\pi}\int_0^\infty y^2 e^{t y^2-4y^4/3}\varphi(y)dy
\]
for every bounded continuous \(\varphi\) and for every polynomial \(\varphi(y)=y^k\). This proves the partition asymptotic, spin weak limit and moment convergence. Dividing by the \(t=0\) case yields the claimed partition ratio.

**4. Conditional magnetic quantum numbers.** In each spin-\(s\) sector the Gibbs operator is scalar. Consequently \(M_n\mid J_n=s\) is *exactly uniform* on \(\{-s,-s+1,\dots,s\}\). The conditional law of \(M_n/n^{3/4}\) therefore converges for \(s/n^{3/4}\to y\) to uniform on \([-y,y]\), including the degenerate law at \(y=0\). Joint convergence with Step 3 gives \(M_n/n^{3/4}\Rightarrow Y_tU\). Integrating the conditional density \(1/(2y)\) against \(f_t\) gives \(g_t\). At \(t=0\), substitution \(v=\sqrt{4/3}\,y^2\) gives the stated \(\operatorname{erfc}\) density, using \(I_0=\frac14(4/3)^{-3/4}\Gamma(3/4)\).

**5. Variance and crossover tails.** Rotation invariance gives \(\operatorname{Tr}(\rho_{n,\beta_n}S_n^z)=0\) and the exact sector identity
\[
\operatorname{Var}(S_n^z)=\frac13\mathbb E[J_n(J_n+1)].
\]
Step 3 with second moments yields the susceptibility. The exact formula \(I_t'=\int_0^\infty y^4e^{ty^2-4y^4/3}dy\) follows by dominated differentiation. The substitution \(y=v/\sqrt{|t|}\) yields \(I_t'/I_t\sim 3/(2|t|)\) as \(t\to-\infty\). For \(t\to+\infty\), set \(u=y^2\) and complete the square \(tu-4u^2/3=3t^2/16-(4/3)(u-3t/8)^2\); Laplace concentration gives \(I_t'/I_t\sim3t/8\). The critical gamma value follows by evaluating the same two integrals.

## Verification

The included `verify.py` reconstructs the finite-spin weights directly from log-gamma factorials; checks the full spin-space dimension identity for \(n=2,\dots,18\); evaluates the finite \(n=2000\) partition coefficient, spin second moment and magnetization variance for \(t=-1,0,1\); and checks the gamma-function integral identities. The printed finite values respectively approach the analytic limits. The code does not prove the thermodynamic limits: their proof is the uniform local expansion and global tail domination in Steps 2–3. Run with Python 3, SciPy and its transitive NumPy dependency: `python verify.py`.

## Relationship to prior work

Raikovich, Mák, Czabán and Gilyén [1], Sections 2.1 and 6.2, establish the spin-sector multiplicities, the critical spin scale, and \(\Theta(n^{3/2})\) variance for their study of the spectral gap of Gibbs-sampler generators. Basso, Bergamaschi, Lin, Ragone and Stubbs [2], especially Appendix D, supply a detailed quartic Laplace/tail analysis for fixed temperatures, and identify the critical quartic degeneracy; their dynamical study does not give the joint critical-window spin-magnitude/magnetization distribution stated here. The fourth-order saddle-point mechanism is therefore prior knowledge. The contribution claimed here is the explicit *moving-temperature* one-parameter equilibrium weak limit, the normalized partition crossover, the magnetic measurement density (including its critical \(\operatorname{erfc}\) form), and the associated susceptibility scaling function. This is an equilibrium result, not a strengthened Lindbladian spectral-gap theorem. Classical finite-size scaling laws for Curie–Weiss and related mean-field models provide useful general context; no claim is made to the novelty of quartic scaling itself.

## Limitations

The finite-spin calculations support, but cannot replace, the uniform large-\(n\) proof. All limits hold at fixed \(t\); they do not imply a uniform approximation when \(t=t_n\to\pm\infty\). The endpoint expansions describe the *already limiting* susceptibility function. The result is restricted to the isotropic all-to-all spin-half model with the stated Hamiltonian normalization. In particular, it does not settle dynamical mixing/spectral gaps in the moving-temperature window, and does not claim that quartic finite-size scaling was previously unknown. Other treatments of general \(O(3)\) mean-field universality could contain equivalent laws; that is a residual priority risk.

## References

[1] L. Raikovich, J. Mák, C. Czabán, and A. Gilyén, "The complete phase diagram of detailed-balanced Gibbs samplers for the mean-field Heisenberg model," arXiv:2610.06818v1 (first publicly submitted 2026-10-05), especially Sections 2.1 and 6.2. https://arxiv.org/abs/2610.06818

[2] J. Basso, T. Bergamaschi, L. Lin, M. Ragone, and K. D. Stubbs, "Spectral Gap of the Davies Generator for the Mean-Field Heisenberg Model," arXiv:2607.21798v1 (first publicly submitted 2026-07-23), especially Section 3 and Appendix D. https://arxiv.org/abs/2607.21798

