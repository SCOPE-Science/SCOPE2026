# Strict absorption-time ordering under two-state diffusivity switching

## Finding

Let a particle diffuse in a bounded region while its diffusivity changes between two positive values according to a symmetric continuous-time Markov chain. If the internal chain begins at its stationary distribution and the spatial starting point is uniform, then **increasing the switching rate strictly decreases the first-exit survival probability at every positive time**, for every bounded connected smooth absorbing/reflecting domain. In particular, every nondecreasing integrable functional of the exit time is smaller at higher rates, whenever its expectation exists and the usual strictness condition applies.

Writing \(m=(D_-+D_+)/2\), the survival curves satisfy, for \(0\le\gamma_1<\gamma_2<\infty\) and \(t>0\),
\[
S_{\mathrm{hom},m}(t)<S_{\gamma_2}(t)<S_{\gamma_1}(t)\le S_{\mathrm{frozen}}(t),
\]
where equality on the right occurs exactly when \(\gamma_1=0\). The lower limit is approached as the switching rate tends to infinity, and the upper limit is the equally weighted frozen-diffusivity mixture.

On an interval \((0,L)\) with both endpoints absorbing, there is a stronger conclusion for the **mean** exit time: the mean over stationary initial internal states, even from a fixed interior position \(x\), is strictly decreasing in the switching rate. For \(\gamma>0\) it has the explicit expression
\[
T_\gamma(x)=\frac{x(L-x)}{2m}+\frac{h^2}{2\gamma m^2}\left(1-\frac{\cosh(\alpha(x-L/2))}{\cosh(\alpha L/2)}\right),\quad
h=\frac{D_+-D_-}{2},\quad \alpha=\sqrt{\frac{2\gamma m}{D_-D_+}}.
\]
The two limiting means are \(x(L-x)m/(2D_-D_+)\) in the frozen case and \(x(L-x)/(2m)\) in the infinitely fast switching limit.

## Assumptions and scope

Choose \(0<D_-<D_+\), and let \(Z_t\in\{-1,+1\}\) flip at rate \(\gamma\ge0\), independently of Brownian motion. Initially \(Z_0\) is symmetric Bernoulli. Set \(D_t=m+h Z_t\), where \(m=(D_-+D_+)/2\) and \(h=(D_+-D_-)/2\). Between boundary encounters, the position evolves as \(dX_t=\sqrt{2D_t}\,dW_t\). A nonempty Dirichlet boundary portion absorbs, and the rest (if any) reflects. Assume a bounded connected domain in \(\mathbb R^d\) with regular boundary and boundary decomposition sufficient for the standard self-adjoint positive discrete-spectrum Dirichlet–Neumann Laplacian. The general stochastic ordering assumes \(X_0\) is uniform on the domain and independent of the chain. Its conclusions concern the absorption time \(\tau_\gamma\), not the conditional law at an arbitrary fixed starting point. The interval mean formula concerns a fixed interior spatial start but still averages the internal state.

## Proof

**1. A strictly ordered integrated-diffusivity mode.** For any \(\lambda>0\), the Feynman–Kac transform of the integrated diffusivity is
\[
\Phi_\gamma(t,\lambda)=\mathbb E\exp\left(-\lambda\int_0^t D_s\,ds\right)=e^{-\lambda mt}f_\gamma(t,a),\qquad a=\lambda h>0.
\]
Symmetry of the stationary two-state chain gives the scalar initial-value problem
\[
f_\gamma''+2\gamma f_\gamma'-a^2f_\gamma=0,\quad f_\gamma(0)=1,\quad f_\gamma'(0)=0.
\]
Its solution is
\[
f_\gamma(t,a)=e^{-\gamma t}\left(\cosh(t\sqrt{\gamma^2+a^2})+\frac{\gamma}{\sqrt{\gamma^2+a^2}}\sinh(t\sqrt{\gamma^2+a^2})\right).
\]
The integrated first-order equation \(f_\gamma'(t)=a^2\int_0^t e^{-2\gamma(t-s)}f_\gamma(s)\,ds\) shows \(f_\gamma'(t)>0\) for \(t>0\). Let \(g(t)=\partial_\gamma f_\gamma(t,a)\). Parameter differentiation yields
\[
g''+2\gamma g'-a^2g=-2f_\gamma',\qquad g(0)=g'(0)=0.
\]
The causal Green kernel for the operator on the left is
\[
K(u)=\frac{e^{(-\gamma+\sqrt{\gamma^2+a^2})u}-e^{(-\gamma-\sqrt{\gamma^2+a^2})u}}{2\sqrt{\gamma^2+a^2}}>0\quad (u>0).
\]
Hence \(g(t)=-2\int_0^tK(t-s)f_\gamma'(s)\,ds<0\) for all \(t>0\). Also \(f_0(t,a)=\cosh(at)\), and \(\lim_{\gamma\to\infty}f_\gamma(t,a)=1\). Therefore each mode transform \(\Phi_\gamma(t,\lambda)\) strictly decreases to the homogeneous-diffusion mode, and is bounded above by its frozen-mixture mode.

**2. Positive spatial weights turn the mode comparison into stochastic order.** Let \((\lambda_j,\varphi_j)\) be an orthonormal Dirichlet–Neumann eigenbasis with \(\lambda_j>0\). Subordination by the independent random clock \(\int_0^tD_sds\), followed by integration over independent uniform starting and ending positions, gives the exact heat-content expansion
\[
S_\gamma(t)=\mathbb P(\tau_\gamma>t)=\frac1{|\Omega|}\sum_{j\ge1}\left|\int_\Omega\varphi_j(x)\,dx\right|^2\Phi_\gamma(t,\lambda_j).
\]
Every coefficient is nonnegative, the coefficients sum to one by Parseval, and the ground-state coefficient is strictly positive (the connected domain's first eigenfunction may be taken positive). The mode inequality from Step 1 therefore gives a **strict** survival inequality for each \(t>0\). Taking the frozen and rapid-switching limits termwise is justified by bounded convergence with these summable nonnegative weights. These survival inequalities constitute strict first-order stochastic dominance. Integrating over time yields the strict ordering of the finite mean exit times, since \(D_t\ge D_->0\) and the bounded domain has a positive Dirichlet spectral gap.

**3. Exact pointwise interval means.** Let \(T_\pm(x)\) be the mean exit time conditional on the two initial internal states. The backward equations and boundary conditions are
\[
D_\pm T_\pm''+\gamma(T_\mp-T_\pm)=-1,\qquad T_\pm(0)=T_\pm(L)=0.
\]
Set \(u=(T_++T_-)/2\), \(v=(T_+-T_-)/2\). Then
\[
m u''+hv''=-1,\qquad h u''+mv''-2\gamma v=0.
\]
Putting \(u=x(L-x)/(2m)+W\) and eliminating \(v\) gives
\[
-W''+\alpha^2W=\frac{h^2}{mD_-D_+},\qquad W(0)=W(L)=0,
\quad \alpha^2=\frac{2\gamma m}{D_-D_+}.
\]
The unique Dirichlet solution is the displayed hyperbolic-cosine formula. If \(\gamma_2>\gamma_1>0\), the positive Dirichlet-resolvent maximum principle applied to these two equations, with their common positive forcing, yields \(W_{\gamma_2}(x)<W_{\gamma_1}(x)\) on every \(0<x<L\). The limits follow from the small-argument expansion of \(\cosh\) and the exponential decay of the interior-to-boundary ratio as \(\gamma\to\infty\). For \(\gamma=0\), the average of the two ordinary Brownian exit means gives the claimed frozen limit directly.

## Verification

A standalone independent script `switching_exit_checks.py` numerically reconstructs the two-state tilted generator, solves the coupled backward boundary-value problem by finite differences, and compares finite samples of the strict mode ordering. Running `python switching_exit_checks.py` produced: **144** matrix-exponential comparisons (maximum absolute error \(2.69\times10^{-15}\)), **six** independent finite-difference comparisons (maximum error \(1.45\times10^{-6}\)), and **24** strict ordered mode families at five switching rates each. Only the analytic arguments prove the all-domain and all-time statements; numerical experiments are not substitutes for these proofs. The program requires Python with NumPy and SciPy.

## Relationship to prior work

Chubynsky and Slater (2014) introduced the fluctuating-diffusivity approach motivating the stochastic medium. Jain and Sebastian (2016) studied survival in bounded rearranging environments; their publicly available abstract establishes substantial prior work on this observable but does not settle the claimed strict switching-rate order, and their complete text could not be examined here. Grebenkov (2018), especially Sections 1 and 3 and equations (1), (3), and (48)–(49), already provides the arbitrary-domain spectral subordination and a two-state matrix/closed-form transform. **Neither formula nor the model is claimed as new.** The present result differentiates the two-state transform to obtain a strict *all-time* ordering, passes it through nonnegative uniform-start heat-content weights, and establishes a separate fixed-position interval mean comparison. Searches of nearby published work did not establish these particular consequences, but historical priority remains subject to further full-text and independent verification.

## Limitations

The strong stochastic ordering requires a stationary **symmetric** two-state internal chain and a **uniform spatial start**. It must not be extrapolated to an arbitrary nonuniform initial position or to asymmetric switching rates without further proof. The fixed-position statement is solely about the state-averaged **mean** in a fully absorbing one-dimensional interval, not about the complete distribution for that start. Equality/strictness assumes two distinct positive diffusivities, a nonempty absorbing boundary and positive elapsed time; limits at zero/infinite rates are not attained by interior finite rates. Historical novelty is provisional: complete text of Jain and Sebastian (2016) was inaccessible, and no independent audit has been performed.

## References

- M. V. Chubynsky and G. W. Slater, “Diffusing diffusivity: A model for anomalous and anomalous yet Brownian diffusion” (2014), arXiv:1404.3573, https://arxiv.org/abs/1404.3573 (first publicly available 2014-04-14).
- R. Jain and K. L. Sebastian, “Diffusing Diffusivity: Survival in a Crowded Rearranging and Bounded Domain,” *J. Phys. Chem. B* 120 (2016) 9215–9222, DOI:10.1021/acs.jpcb.6b06094 (abstract examined; full text inaccessible).
- D. S. Grebenkov, “A unifying approach to first-passage time distributions in diffusing diffusivity and switching diffusion models” (2018), arXiv:1812.07249, https://arxiv.org/abs/1812.07249 (full article text, especially Sections 1 and 3, examined).
