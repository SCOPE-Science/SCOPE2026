# Sharp half-moment collapse and weak-confinement singularity in harmonic stochastic return

## Finding
For the two-phase diffusion model specified below, the first-completion time \(T_{r,0}\) with freely diffusive return has the exact regularly varying tail
\[
\mathbb P(T_{r,0}>t)\sim \frac{K}{\sqrt{\pi t}},\qquad K=\frac{rI}{p}=1-\frac{k\phi_r}{(k+r)p}\in(0,1).
\]
Thus, for every \(\alpha>0\), \(\mathbb E T_{r,0}^{\alpha}<\infty\) exactly when \(\alpha<1/2\), and in particular its mean is infinite. Yet the same search without resets (\(r=0\)) has finite mean first-passage time. When the return OU stiffness \(\kappa>0\) decreases to zero, the finite mean has the sharp singularity
\[
\lim_{\kappa\downarrow0}\sqrt\kappa\,\mathbb E T_{r,\kappa}=\sqrt{\pi/2}\,K.
\]
The *same explicit amplitude* governs the long-time free-return tail and the small-stiffness mean. This is a singular phase boundary: every positive return stiffness gives finite mean, while zero stiffness makes the mean infinite for any positive reset rate.

## Assumptions and scope
Fix \(k>0\) and \(r>0\). Search starts at \(X_0=0\) on \(( -\infty,1)\) and obeys \(dX_t=-kX_t\,dt+\sqrt2\,dB_t\). The absorbing target is at \(1\). Independently, a clock of rate \(r\) switches the system to a return phase unless the target is reached first. Return from the switch position \(x<1\) obeys \(dY_t=-\kappa Y_t\,dt+\sqrt2\,dW_t\), \(\kappa\ge0\), until reaching \(0\) or \(1\); for \(x<0\) only \(0\) can be reached first by continuity. Target detection is enabled in both phases. On reaching \(0\) the process restarts with fresh independent clocks and driving noises. Define \(T_{r,\kappa}\) as total time until first detection of \(1\), including all return times. No instantaneous teleportation is used.

Let \(\tau=\inf\{t\ge0:X_t=1\}\) be the first-passage time of the *uninterrupted* search, let \(\phi_q=\mathbb E_0(e^{-q\tau})\), and let \(g_q\) be the density of its killed resolvent measure
\[
\int_Eg_q(x)\,dx=\mathbb E_0\int_0^\tau e^{-qt}{\bf1}_{\{X_t\in E\}}\,dt,
\qquad E\subset(-\infty,1),\quad q>0.
\]
The finite positive constants are \(I=\int_{-\infty}^{0}(-x)g_r(x)\,dx\), \(J=\int_0^1xg_r(x)\,dx\), and \(p=\phi_r+rJ\). In particular \(p\) is one-cycle success probability at \(\kappa=0\), and \(K=rI/p\). The normalization is diffusion coefficient \(D=1\), target \(L=1\); rescaling changes the constants.

## Proof
**One-cycle renewal.** For \(q>0\), \(1-\phi_q=q\int g_q\), by integration of the killed survival function. The independent exponential switch has joint time-position density \(r e^{-rt}\mathbb P_0(X_t\in dx,\tau>t)dt\). Consequently the Laplace transform \(F_0(s)=\mathbb E e^{-sT_{r,0}}\) is a quotient \(F_0(s)=[A(s)+B(s)]/[1-C(s)]\), with
\[
A(s)=\phi_{r+s},\quad B(s)=r\int_0^1g_{r+s}(x)b_s(x)dx,\quad C(s)=r\int_{-\infty}^1g_{r+s}(x)a_s(x)dx.
\]
Here \(a_s(x)\) and \(b_s(x)\) are the discounted exit-to-origin and exit-to-target probabilities of return Brownian motion, respectively. For \(x<0\), \(a_s(x)=e^{x\sqrt s}\) and \(b_s(x)=0\); for \(0<x<1\),
\[
 a_s(x)=\frac{\sinh((1-x)\sqrt s)}{\sinh\sqrt s},\qquad b_s(x)=\frac{\sinh(x\sqrt s)}{\sinh\sqrt s}.
\]
Therefore \(a_0(x)+b_0(x)=1\) for all \(x<1\), and \(1-C(0)=\phi_r+rJ=p>0\). The sum of numerator and renewal term satisfies the *exact* identity
\[
1-A(s)-B(s)-C(s)
=s\int_{-\infty}^1g_{r+s}(x)dx
+r\int_{-\infty}^1g_{r+s}(x)[1-a_s(x)-b_s(x)]dx.
\]
On \(x<0\), the last integrand is \(1-e^{x\sqrt s}=(-x)\sqrt s+O(sx^2)\); on \(0<x<1\), it is \(O(s)\) uniformly. For fixed \(k,r>0\), discounted killed-OU occupation has finite moments \(\int (1+|x|^2)g_qdx\), locally uniformly for \(q\ge r\), and \(g_{r+s}\to g_r\) in these weighted integrals as \(s\downarrow0\). It follows that \(1-F_0(s)=\frac{rI}{p}\sqrt{s}+o(\sqrt{s})\). The monotone Tauberian theorem applied to \((1-F_0(s))/s=\int_0^\infty e^{-st}\mathbb P(T_{r,0}>t)dt\) yields the asserted exact tail and hence the sharp moment criterion.

**Weakly confined return.** For a return starting at \(-a<0\), the OU mean hitting time of \(0\) is obtained from \(m''-\kappa x m'=-1\), with the derivative selected by the natural boundary at \(-\infty\):
\[
m_\kappa(-a)=\sqrt{\frac\pi{2\kappa}}\int_0^a
 e^{\kappa u^2/2}\operatorname{erfc}(\sqrt{\kappa/2}\,u)du.
\]
The scaled complementary error function lies in \((0,1]\) for nonnegative argument. Hence \(\sqrt\kappa m_\kappa(-a)\to\sqrt{\pi/2}\,a\), bounded by \(\sqrt{\pi/2}\,a\), permitting dominated convergence against \(g_r\). For \(0<x<1\), the mean time to hit either endpoint is bounded uniformly for small \(\kappa\); the success splitting probability is
\[
b_\kappa(x)=\frac{\int_0^x e^{\kappa y^2/2}dy}{\int_0^1 e^{\kappa y^2/2}dy}\longrightarrow x.
\]
With \(m_\kappa(x)\) the appropriate mean return exit time (from \(0\) or \(1\) when positive, from \(0\) when negative), the cycle renewal mean is exactly
\[
\mathbb ET_{r,\kappa}=
\frac{(1-\phi_r)/r+r\int_{-\infty}^1g_r(x)m_\kappa(x)dx}
{\phi_r+r\int_0^1g_r(x)b_\kappa(x)dx}.
\]
For every \(\kappa>0\) the terms are finite. Multiply by \(\sqrt\kappa\) and pass to the limit using the preceding bounds: the numerator tends to \(\sqrt{\pi/2}\,rI\), while the denominator tends to \(p\).

**Amplitude identity.** Discounted Dynkin's formula for the test function \(f(x)=x\), applied to the killed search, gives \(\phi_r=(r+k)(I-J)\). Therefore \(rI=rJ+r\phi_r/(r+k)=p-k\phi_r/(r+k)\), proving \(K=1-k\phi_r/((r+k)p)\). Here \(\phi_r>0\), \(I>0\), and \(p>0\), so \(0<K<1\). With no resets, the search-only OU mean is \(\int_0^1e^{ku^2/2}\int_{-\infty}^ue^{-kv^2/2}dv\,du<\infty\), proving the stated noncommutativity at \(r=0\).

## Verification
An independent spatial finite-difference solution of the search resolvent and one-dimensional quadrature of return moments checks the discounted Dynkin identity, the renewal amplitude, and convergence of \(\sqrt\kappa\,\mathbb ET_{r,\kappa}\) to \(\sqrt{\pi/2}K\). Run `python verify.py` with NumPy and SciPy. The finite-grid calculations are numerical checks only; the infinite-time and zero-stiffness limits follow from the preceding analytical argument.

## Relationship to prior work
Dubey and Pal (2026) derive the stochastic-return model with harmonic search/return forces and the exact first-passage **mean** at positive return stiffness, including target detection during return. Biswas, Kundu and Pal (2023/2024) give general stochastic-return renewal methods, including a harmonic-return appendix for freely diffusing search. Biswas, Dubey, Kundu and Pal (2024) study drift-diffusive search with a linear returning potential and mean completion times. Singh (2024) studies time/work costs for diffusive search under confining return and explicitly assumes the target cannot be detected on the return leg. Those formulations and ordinary Brownian first-passage tails are prior knowledge. The additional result here is the sharp **total-completion** heavy-tail amplitude for the harmonic-search model, its half-moment transition, the matching weak-harmonic-stiffness mean coefficient, and the amplitude identity.

## Limitations
The theorem requires one spatial dimension, an independent exponential switch, independent Gaussian forcing in each phase, a positive search stiffness and target at positive separation. The first-passage tail statement is for exactly zero return stiffness at fixed \(r>0\); it is not a uniform joint \(t,\kappa,r\) expansion. General renewal formulas in earlier literature may imply parts of the result with further analysis; no claim is made that renewal itself, OU exit-time formulas, or Brownian \(t^{-1/2}\) first-passage decay are novel. All originality comparisons are best-knowledge and not independent certification.

## References
- A. Dubey and A. Pal, *Towards synergy between theory and experiments: First-passage processes under resetting with stochastic return protocols*, arXiv:2610.18814v1 (2026), https://arxiv.org/html/2610.18814v1.
- A. Biswas, A. Kundu and A. Pal, *Search with stochastic home-returns can expedite classical first passage under resetting*, arXiv:2307.16294v3 (2024), https://arxiv.org/html/2307.16294v3.
- A. Biswas, A. Dubey, A. Kundu and A. Pal, *Drift-diffusive resetting search process with stochastic returns: speed-up beyond optimal instantaneous return*, arXiv:2406.08975v1 (2024), https://arxiv.org/html/2406.08975v1.
- P. Singh, *Cost-time trade-off in diffusion with stochastic return: optimal resetting potential and Pareto front*, arXiv:2407.02071v1 (2024), https://arxiv.org/html/2407.02071v1.
