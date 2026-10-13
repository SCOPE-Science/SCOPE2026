# Two endpoint scales for the locally optimal exponential Stein test of Poisson zero inflation

## Finding
Fix a Poisson null mean \(\lambda>0\), an exponential weight \(u\in(0,1)\), and let \(t=1-u\). For iid count observations define
\[
A_{n,u}=\frac1n\sum_{i=1}^n X_i u^{X_i}-\bar X\frac1n\sum_{i=1}^n u^{X_i+1}.
\]
The nuisance-fitted, null-standardized statistic is \(Z_{n,u}=\sqrt n A_{n,u}/s_u(\bar X)\), where
\[
s_u(\mu)^2=\mu u^2e^{2\mu(u-1)}\big[(1+\mu(1-u)^2)e^{\mu(1-u)^2}-1\big].
\]
When the null holds, \(Z_{n,u}\Rightarrow N(0,1)\). Against the mean-preserving contiguous zero-inflated Poisson model of structural-zero probability \(\omega_n=h/\sqrt n\), with Poisson-component mean \(\lambda/(1-\omega_n)\) and fixed \(h\ge0\),
\[
Z_{n,u}\Rightarrow N\left(-h\sqrt{F_\lambda(t)},1\right),\qquad
F_\lambda(t)=\frac{\lambda(e^{\lambda t}-1)^2}{(1+\lambda t^2)e^{\lambda t^2}-1}.
\]
For each \(\lambda>0\), all maximizers \(t_\lambda\) of the continuous extension of \(F_\lambda\) to \([0,1]\) are interior. Every choice of maximizers has the two sharp limits
\[
t_\lambda\longrightarrow\frac23\quad(\lambda\downarrow0),\qquad
\lambda(1-t_\lambda)\longrightarrow1\quad(\lambda\to\infty).
\]
Equivalently, the locally power-optimal weight parameter tends to \(1/3\) at vanishing mean and is asymptotic to \(1/\lambda\) at large mean. The optimal noncentrality-squared coefficient additionally satisfies
\[
\max_{0\le t\le1}F_\lambda(t)=\frac{\lambda^2}{2}\left(1+\frac\lambda3+O(\lambda^2)\right)\ (\lambda\downarrow0),\quad
\max_{0\le t\le1}F_\lambda(t)\sim e^\lambda\ (\lambda\to\infty).
\]

## Assumptions and scope
All limits in sample size hold with \(\lambda>0\), \(u\in(0,1)\), and \(h\ge0\) fixed. The small- and large-\(\lambda\) limits subsequently concern the optimal parameter of this already-derived local experiment; they are **iterated limits**, not a uniform triangular-array theorem in which \(\lambda\) and sample size both vary. For finite \(n\) define \(Z_{n,u}=0\) when its estimated denominator vanishes; under each fixed positive-mean null or contiguous alternative this event has probability tending to zero. Optimization is *within the one-parameter family* of single exponential Stein weights and does not assert globally most powerful testing among all possible statistics. The endpoint \(t=0\) is a continuous envelope limit, not a legitimate nondegenerate weight.

For a fixed two-sided asymptotic size \(\alpha\in(0,1)\) and \(h>0\), local power is \(\Pr(|N(-h\sqrt{F_\lambda(t)},1)|>z_{1-\alpha/2})\), strictly increasing in \(F_\lambda(t)\). Thus maximizing \(F_\lambda\) is precisely optimizing this test's local power. No uniqueness of the finite-mean optimizer is asserted.

## Proof
**1. Influence and null variance.** For \(X\sim\operatorname{Poi}(\lambda)\), set \(a=e^{\lambda(u-1)}\). The Poisson factorial-moment generating identities yield \(\mathbb E[u^X]=a\), \(\mathbb E[Xu^X]=\lambda u a\), and \(\mathbb E[X^2u^X]=(\lambda u+\lambda^2u^2)a\). Differentiating the three-mean map defining \(A_{n,u}\) gives the centered influence
\[
\psi_u(X)=Xu^X-\lambda u^{X+1}-ua(X-\lambda).
\]
Writing \(H=Xu^X-\lambda u^{X+1}\), the same identities give \(\mathbb E[H]=0\), \(\operatorname{Cov}(H,X)=\lambda ua\), and
\[
\mathbb E[H^2]=\lambda u^2[1+\lambda(1-u)^2]e^{\lambda(u^2-1)}.
\]
Consequently,
\[
\operatorname{Var}(\psi_u)=\mathbb E[H^2]-\lambda u^2a^2=s_u(\lambda)^2>0.
\]
The multivariate iid central limit theorem, differentiability of the empirical-mean map, and Slutsky's lemma give the displayed null Gaussian limit.

**2. Contiguous alternative and local power.** Under a mean-preserving ZIP law with \(\omega\in[0,1)\), its probability generating function is
\[
\phi_\omega(z)=\omega+(1-\omega)\exp\left(\frac\lambda{1-\omega}(z-1)\right).
\]
Direct differentiation gives the exact population Stein residual
\[
\mathbb E_\omega[Xu^X]-\lambda\mathbb E_\omega[u^{X+1}]
=\lambda u\omega\left[e^{\lambda(u-1)/(1-\omega)}-1\right].
\]
For \(\omega_n=h/\sqrt n\), the centered sample means obey a triangular-array central limit theorem, since the distributions converge to Poisson with uniformly bounded moments in a neighborhood of \(\omega=0\). Their mean residual times \(\sqrt n\) tends to \(h\lambda u(a-1)\). Dividing by \(s_u(\lambda)\), and using \(a=e^{-\lambda t}\), produces
\[
\frac{\lambda u(a-1)}{s_u(\lambda)}=-\sqrt{F_\lambda(t)}.
\]
The two-sided normal-test power is strictly increasing with the magnitude of its Gaussian noncentrality (for positive \(h\)), giving the claimed optimization criterion.

**3. Finite-intensity interior maximizers.** Extend continuously at \(t=0\) by \(F_\lambda(0)=\lambda^2/2\). The extension is positive and continuous on \([0,1]\). For \(0<t<1\), the derivative of \(F_\lambda\) has the same sign as
\[
G_\lambda(t)=1+\lambda t^2-e^{-\lambda t^2}-t(2+\lambda t^2)(1-e^{-\lambda t}).
\]
Indeed, its numerator after differentiation equals \(2\lambda^2(e^{\lambda t}-1)e^{\lambda t+\lambda t^2}G_\lambda(t)\), with a positive denominator. At \(t\downarrow0\), \(G_\lambda(t)=\lambda^2t^3+O_\lambda(t^4)>0\); and \(G_\lambda(1)=(1+\lambda)e^{-\lambda}-1<0\). Hence neither endpoint can maximize, and every global maximizer is interior.

**4. Small-mean optimum.** Uniform Taylor expansion over \(0\le t\le1\), obtained by factoring the common \(\lambda t^2\) from numerator and denominator before expanding, gives
\[
F_\lambda(t)=\frac{\lambda^2}{2}\left[1+\lambda\left(t-\frac34t^2\right)+O(\lambda^2)\right].
\]
The continuous polynomial \(t-3t^2/4\) has a unique maximizer \(2/3\) on \([0,1]\), with maximum \(1/3\). Uniform convergence of the renormalized objectives proves all maximizers tend to \(2/3\) and yields the first maximal-value expansion.

**5. Large-mean optimum.** At \(t=1\), \(F_\lambda(1)\sim e^\lambda\). For \(0<t\le1/3\), using \((1+v)e^v-1\ge2v\) and \(e^x-1\le xe^x\), one gets \(F_\lambda(t)\le\lambda^2e^{2\lambda/3}/2=o(e^\lambda)\); this bound extends to \(t=0\). On the interval \(1/3\le t\le1-\delta\), with any fixed \(\delta>0\), the denominator is at least \(e^{\lambda t^2}/2\) for all large \(\lambda\), so
\[
F_\lambda(t)\le2\lambda e^{\lambda(2t-t^2)}\le2\lambda e^{\lambda(1-\delta^2)}=o(e^\lambda).
\]
Therefore any maximizer \(t_\lambda\to1\). At each such interior maximizer \(G_\lambda(t_\lambda)=0\), or equivalently
\[
\lambda t_\lambda^2(1-t_\lambda)=2t_\lambda-1+e^{-\lambda t_\lambda^2}-t_\lambda(2+\lambda t_\lambda^2)e^{-\lambda t_\lambda}.
\]
The exponential terms tend to zero and \(t_\lambda\to1\), hence \(\lambda(1-t_\lambda)\to1\). Substituting into the exact \(F_\lambda\) formula gives \(F_\lambda(t_\lambda)/e^\lambda\to1\) because the exponent \(\lambda(2t-t^2)=\lambda-\lambda(1-t)^2\) differs from \(\lambda\) by \(o(1)\), and \(\lambda/(1+\lambda t^2)\to1\). This completes the proof.

## Verification
Run `python verify.py` in the extracted directory with Python, SymPy, and SciPy installed. The verifier checks exact symbolic variance, derivative and mean-ZIP-residual identities; the uniform small-mean expansion coefficients; and finite sums of Poisson probabilities plus independently optimized numerical examples. At the time of this package's construction it printed `PASS` with 96 separately counted checks. The analytic proof, not the finite calculations, covers all allowed real intensities and weights.

## Relationship to prior work
Weiß, Puig, and Aleksandrov (2023; publicly online September 27, 2022), Sections 2–3 and Tables 2–3, introduce the same exponential Stein weight, derive a general asymptotic power method, and numerically optimize weights against fixed zero-inflation alternatives. Their reported finite-mean values and general asymptotic machinery are **prior art**. The present result isolates a *contiguous mean-preserving ZIP experiment* and proves a closed pointwise local-power envelope with two explicit small-/large-intensity optimization limits, including the \(1/\lambda\) large-intensity weight scale. It does not claim to discover the Stein statistic, the numerical optimization strategy, or the general delta-method theory. Aleksandrov and colleagues (2022) already advocate exponential weighting for ZIP detection. Baringhaus and Henze (1992) used an integrated empirical-pgf derivative discrepancy; the later Weiß–Nik (2025) paper gives discrete-grid pgf tests and covariance calculations. Neither materially inspected statement supplies the two endpoint scales proved here.

## Limitations
The result does not establish a unique finite-\(\lambda\) maximizer, finite-sample uniform power optimality, optimality among arbitrary Poisson tests, or simultaneous \(n,\lambda\to\infty\) behavior. An equivalent earlier specialization of general Poisson local-power theory could remain in literature not fully accessible, notably earlier integrated-pgf test papers. The result is a self-review, without independent audit.

## References
1. C. H. Weiß, P. Puig, and B. Aleksandrov, *Optimal Stein-type goodness-of-fit tests for count data*, Biometrical Journal 65 (2023), article 2200073; first online 2022-09-27, DOI: 10.1002/bimj.202200073. Full text: https://onlinelibrary.wiley.com/doi/full/10.1002/bimj.202200073 .
2. B. Aleksandrov et al., *Goodness-of-fit tests for Poisson count time series based on the Stein–Chen identity*, Statistica Neerlandica (2022), DOI: 10.1111/stan.12252. https://onlinelibrary.wiley.com/doi/abs/10.1111/stan.12252 .
3. L. Baringhaus and N. Henze, *A goodness of fit test for the Poisson distribution based on the empirical generating function*, Statistics & Probability Letters 13 (1992), 269–274, DOI: 10.1016/0167-7152(92)90033-2.
4. C. H. Weiß and S. Nik, *Computationally efficient pgf-based goodness-of-fit tests for Poisson counts and beyond*, Journal of Statistical Computation and Simulation (first online 2025-12-21), DOI: 10.1080/00949655.2025.2604785.
