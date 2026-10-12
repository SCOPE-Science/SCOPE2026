# Sharp metric error and modal boundary for Pareto-reset Ising relaxation

## Finding
Let a one-dimensional periodic Ising spin system undergo Glauber dynamics at a finite nonnegative inverse-temperature–coupling product, with repeated instantaneous resets to a fixed configuration of positive spatial mean magnetization \(m_0\). Independent reset intervals follow the Pareto density \(\alpha\tau_0^\alpha w^{-\alpha-1}\mathbf 1_{\{w\ge\tau_0\}}\), where \(\alpha>1\) and \(\tau_0>0\). Write \(\gamma=\tanh(2\beta J)\), \(\lambda=1-\gamma>0\), and \(b=\lambda\tau_0\). Here magnetization means the **conditional spin-noise expectation of the spatial mean, given the time since the most recent reset**, not the single-realization finite-volume spin average.

The stationary law of this conditional mean \(M\) is absolutely continuous on \(0<m<m_0\), with density
\[
f_M(m)=\frac{\alpha-1}{\alpha\lambda\tau_0 m}
\begin{cases}
1,&m_0e^{-b}<m<m_0,\\
\bigl(b/\log(m_0/m)\bigr)^\alpha,&0<m\le m_0e^{-b}.
\end{cases}
\]
There are no point masses. When \(b<\alpha\), its density has a strict finite local maximum at \(m_*=m_0e^{-b}\) and a strict interior minimum at \(m_0e^{-\alpha}\), in addition to its integrable divergence near zero. When \(b\ge\alpha\), the density is strictly decreasing as a function of \(m\), with no finite interior local maximum. Thus \(b=\alpha\) is the sharp modal boundary.

Define \(\widetilde M=m_0\exp(-\lambda\max\{A,\tau_0\})\), where \(A\) denotes the equilibrium time elapsed since the last reset. This explicit coarse-graining collapses the entire \(A<\tau_0\) sector to the cutoff point \(m_*\), as in the cutoff-atom approximation used for the stationary law in the motivating work. With total variation normalized as \(d_{\mathrm{TV}}=\sup_B|\mu(B)-\nu(B)|\), and one-dimensional \(W_1\) for absolute-distance cost,
\[
\boxed{\;d_{\mathrm{TV}}(\mathcal L(M),\mathcal L(\widetilde M))=\frac{\alpha-1}{\alpha},\;}
\]
\[
\boxed{\;W_1(\mathcal L(M),\mathcal L(\widetilde M))=\frac{m_0(\alpha-1)}{\alpha}\left(\frac{1-e^{-b}}{b}-e^{-b}\right).\;}
\]
Consequently, for fixed \(\alpha>1\), as \(b\downarrow0\) the first distance remains fixed while the second is \(\frac{m_0(\alpha-1)}{2\alpha}b+O(b^2)\). This is a sharp strong-versus-weak approximation distinction.

## Assumptions and scope
Fix \(N\ge3\) Ising spins on a ring, an initial deterministic configuration \(s^0\in\{-1,1\}^N\) with \(m_0=N^{-1}\sum_j s_j^0>0\), and parameters \(\beta,J\ge0\) with \(\beta J<\infty\). For spin \(j\), the Glauber flip rate is
\[
w_j(s)=\frac12\left(1-\frac{\gamma}{2}s_j(s_{j-1}+s_{j+1})\right),\qquad\gamma=\tanh(2\beta J),
\]
with periodic indices. At time zero a reset occurs; subsequent resets to \(s^0\) occur after independent Pareto waiting times \(W\) with \(\Pr(W>t)=1\) for \(0\le t<\tau_0\) and \(\Pr(W>t)=(\tau_0/t)^\alpha\) for \(t\ge\tau_0\). Waiting times and spin-flip randomness are independent. The **last-reset age** is \(A_t\), and \(M_t=N^{-1}\sum_j\mathbb E[s_j(t)\mid A_t,\text{reset state }s^0]\). The result concerns convergence \(M_t\Rightarrow M\) as \(t\to\infty\). Statements about modes refer to this density, not the full finite-\(N\) spin-sample distribution. \(\alpha\le1\), non-Pareto resets, and two-dimensional relaxation are not included.

## Proof
**Step 1 (exact conditional relaxation).** The generator applied to the local spin satisfies \(\mathcal Ls_j=-s_j+\frac\gamma2(s_{j-1}+s_{j+1})\). Summing around the ring gives
\[
\mathcal L\Bigl(\sum_j s_j\Bigr)=-(1-\gamma)\sum_j s_j=-\lambda\sum_j s_j.
\]
Therefore, at any elapsed time \(a\ge0\), the conditional expected spatial mean is exactly \(m_0e^{-\lambda a}\), even in finite volume and without any independent-spin approximation. Hence \(M_t=m_0e^{-\lambda A_t}\).

**Step 2 (stationary age and density).** Because the reset intervals are continuous and have finite mean \(\mathbb EW=\alpha\tau_0/(\alpha-1)\), the nonlattice renewal-age theorem gives \(A_t\Rightarrow A\), where
\[
g(a)=\frac{\Pr(W>a)}{\mathbb EW}=\frac{\alpha-1}{\alpha\tau_0}\begin{cases}1,&0\le a<\tau_0,\\(\tau_0/a)^\alpha,&a\ge\tau_0.\end{cases}
\]
The two age sectors integrate respectively to \((\alpha-1)/\alpha\) and \(1/\alpha\). The continuous monotone change of variable \(m=m_0e^{-\lambda a}\), \(a=\log(m_0/m)/\lambda\), has Jacobian \(|da/dm|=1/(\lambda m)\). Applying it to \(g\) gives the stated complete density and excludes all atoms (including at both endpoints).

**Step 3 (sharp modal boundary).** On the age parameterization, \(f_M(m_0e^{-\lambda a})=g(a)e^{\lambda a}/(\lambda m_0)\). The logarithmic derivative with respect to \(a\) is \(\lambda\) below \(\tau_0\) and \(\lambda-\alpha/a\) above \(\tau_0\). If \(\lambda\tau_0<\alpha\), the sign changes from positive to negative at the cutoff and back to positive at \(a=\alpha/\lambda\), yielding exactly the finite cusp maximum and later interior minimum. If \(\lambda\tau_0\ge\alpha\), this logarithmic derivative is nonnegative everywhere and strictly positive except possibly at one point. Since \(m\) strictly decreases as \(a\) increases, the density is strictly decreasing in \(m\) on the entire open support. Finally \(f_M(m)\to\infty\) as \(m\downarrow0\) because \(m^{-1}\log(m_0/m)^{-\alpha}\to\infty\).

**Step 4 (the exact metric gap).** Write \(B=\{A<\tau_0\}\), \(p=\Pr(B)=(\alpha-1)/\alpha\), and \(m_*=m_0e^{-b}\). The two laws coincide on the event \(B^c\). On \(B\), the true \(M\) has a continuous distribution supported on \((m_*,m_0)\), while \(\widetilde M=m_*\) is a point mass of weight \(p\). Taking the singleton \(\{m_*\}\) shows total variation at least \(p\); the common coupling bounds it above by \(p\), proving equality. The same coupling gives \(M\ge\widetilde M\) almost surely. Consequently it is optimal for the one-dimensional \(W_1\) cost: its mean difference equals the \(W_1\) upper bound, and the test function \(m\mapsto m\) (1-Lipschitz) gives the reverse lower bound. Thus
\[
W_1=\mathbb E(M-\widetilde M)
=\frac{\alpha-1}{\alpha\tau_0}m_0\int_0^{\tau_0}\bigl(e^{-\lambda a}-e^{-b}\bigr)da,
\]
which evaluates to the stated closed form. Taylor expansion of exponentials proves the final small-\(b\) asymptotic.

## Verification
The standalone standard-library program `verify.py` evaluates normalization of both renewal-age sectors, numerically integrates the independently expressed log-magnetization density, tests the exact transport integral, checks derivative-sign classification on both sides of the critical line, and independently samples the two-component age distribution. Run `python3 verify.py`; the executed program returned `VERIFY_OK 210 analytic normalizations, piecewise densities, transport, modal signs, and independently sampled stationary laws`. These are finite, numerical checks; Steps 1–4 prove the full quantified claims.

## Relationship to prior work
V K and Nagar, *Ising Model with Power Law Resetting*, arXiv:2602.15495, Phys. Rev. Research 8, 023197 (2026), establish the Pareto-reset Ising model, the exact one-dimensional conditional mean relaxation, and a stationary formula (their equations (5)–(10)). In their equation (6), the age range below the minimum inter-reset interval is aggregated to the cutoff trajectory; their equation (10) consequently contains a point mass at the cutoff. The present theorem **does not claim novelty for the reset model, relaxation equation, long-age tail, or renewal-age framework**. It evaluates the unaggregated small-age sector and the *quantitative information lost by exactly that cutoff-atom approximation*, together with the resulting modal boundary. These statements do not say that the older coarse-grained law is a fully resolved description of the unaggregated stochastic process.

Eule and Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, New J. Phys. 18 (2016) 033006, give the general non-Poisson resetting framework; the stationary backward-age rather than raw waiting-time distribution is essential. *Lévy Diffusion Under Power-Law Stochastic Resetting*, Entropy 28 (2026) 104, explicitly gives the piecewise Pareto stationary-age density (equation (31)) in a different application. Both are fully credited; the age identity alone and the resulting change-of-variable density are known ingredients, not a claim to a new renewal theorem. The new object of comparison is the 2026 cutoff-atom approximation for the reset Ising observable, and its sharp metric and modal consequences.

## Limitations
The result applies to the conditional expectation of average magnetization, not to a single-trajectory spin realization (whose magnetization is discrete at finite \(N\)). It does not evaluate finite-observation-time errors, finite-\(N\) spin-noise variances, or robustness of finite-histogram modal estimates. The two distance statements compare the true stationary conditional-mean law to one **explicitly defined** approximation; they do not imply that every discretization has this error. The continuous shoulder and the cutoff atom may be close in weak metrics as \(b\downarrow0\), even though they remain mutually singular on the affected sector. Priority over all unindexed sources is not certified. The general age-to-observable transformation follows known renewal results, so originality is confined to the precise comparison and classification.

## References
1. Anagha V K and Apoorva Nagar, *Ising Model with Power Law Resetting*, arXiv:2602.15495 (first public 17 February 2026); Phys. Rev. Research 8, 023197 (2026), DOI 10.1103/d3hg-bgmh, https://arxiv.org/pdf/2602.15495.
2. Stephan Eule and Jakob J Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, New Journal of Physics 18, 033006 (2016), DOI 10.1088/1367-2630/18/3/033006, https://edoc.mdc-berlin.de/id/eprint/19462/1/19462oa.pdf.
3. *Lévy Diffusion Under Power-Law Stochastic Resetting*, Entropy 28, 104 (2026), DOI 10.3390/e28010104, https://pmc.ncbi.nlm.nih.gov/articles/PMC12839795/.
4. Matteo Magoni, Satya N Majumdar, and Gregory Schehr, *Ising model with stochastic resetting*, arXiv:2002.04867 (2020), https://arxiv.org/abs/2002.04867 (Poissonian resetting, not the Pareto-cutoff comparison).
