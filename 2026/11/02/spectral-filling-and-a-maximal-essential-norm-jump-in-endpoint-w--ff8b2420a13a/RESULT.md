# Spectral filling and a maximal essential-norm jump in endpoint-weighted Cesàro operators

## Finding

On the complex Hilbert space \(L^2(0,1)\), consider the integral operators
\[
(H_\gamma f)(x)=\frac1x\int_0^x(1-t)^{-\gamma}f(t)\,dt,\qquad 0<x<1,
\]
initially for compactly supported smooth functions, with real parameter \(\gamma\). Let \(D=\{\lambda\in\mathbb C:|\lambda-1|<1\}\), let \(\sigma_{\mathrm F}\) denote the Fredholm essential spectrum, and let \(\operatorname{ind}\) denote Fredholm index.

**Complete threshold and spectral classification.** The defining integral has a bounded extension if and only if \(\gamma\le1\). All such extensions have norm and essential norm exactly \(2\). For every \(\gamma<1\),
\[
\sigma(H_\gamma)=\overline D,\qquad \sigma_{\mathrm p}(H_\gamma)=D,\qquad
\sigma_{\mathrm F}(H_\gamma)=\partial D.
\]
Each eigenvalue in \(D\) has a one-dimensional eigenspace and is surjective as an operator \(H_\gamma-\lambda I\). For \(\lambda\notin\partial D\),
\[
\operatorname{ind}(H_\gamma-\lambda I)=
\begin{cases}1,&\lambda\in D,\\0,&\lambda\notin\overline D.\end{cases}
\]
At the critical exponent \(\gamma=1\), the operator is normal and has \(\sigma(H_1)=\sigma_{\mathrm F}(H_1)=\partial D\), no eigenvalues, and Fredholm index zero on both complementary components.

**Exact perturbation and discontinuity.** For every \(\gamma<1\), the perturbation \(H_\gamma-H_0\) is Hilbert–Schmidt, with exact formula
\[
\|H_\gamma-H_0\|_{\mathcal S_2}^2
=2\psi(2-\gamma)-\psi(2-2\gamma)-\psi(2),
\]
where \(\psi=\Gamma'/\Gamma\). As \(\gamma\uparrow1\), this squared norm is \(\frac{1}{2(1-\gamma)}+O(1)\). Nonetheless \(H_\gamma\to H_1\) in the strong operator topology, while for **every** \(\gamma<1\),
\[
\boxed{\|H_1-H_\gamma\|=\|H_1-H_\gamma\|_{\mathrm{ess}}=2.}
\]
Thus the Fredholm essential spectrum stays fixed at \(\partial D\) while the ordinary spectrum and the interior Fredholm index change abruptly at the critical boundary singularity. This combination of sharp jump distance, strong convergence, and interior-index transition is the principal result.

## Assumptions and scope

The base space is unweighted complex \(L^2(0,1)\) with Lebesgue measure; the exponent \(\gamma\) is real and no analytic continuation in \(\gamma\) is asserted. Operator norms are induced by the \(L^2\)-norm. Fredholm essential spectrum is precisely the set where \(H_\gamma-\lambda I\) fails to be Fredholm (not the Weyl or Browder spectrum). The essential norm is distance to compact operators. The source family is defined on \(C_c^\infty(0,1)\) before extension. For \(\gamma>1\), 'unbounded' means that no bounded operator on all of \(L^2(0,1)\) can agree with this integral on that dense core.

## Proof

**1. Exact critical model.** Set \(x(u)=e^u/(1+e^u)\) and define the unitary
\[
(U_1f)(u)=\sqrt{x(u)(1-x(u))}\,f(x(u)):\ L^2(0,1)\to L^2(\mathbb R).
\]
Since \(x'(u)=x(u)(1-x(u))\), substitution gives
\[
(U_1H_1U_1^{-1}g)(u)=\int_0^\infty e^{-v/2}g(u-v)\,dv.
\]
Its Fourier multiplier is \(m(\xi)=(\tfrac12+i\xi)^{-1}\), whose essential range closes to \(\partial D\). This directly proves normality, norm and essential norm \(2\), spectral circle, absence of eigenvalues, and index zero away from that circle. All points of the circle are essential, because \(m\) has no isolated finite-multiplicity spectral value.

**2. Classical Hardy model.** For \(\gamma=0\), let \((U_0f)(s)=e^{-s/2}f(e^{-s})\), a unitary onto \(L^2(0,\infty)\). Direct substitution yields
\[
(U_0H_0U_0^{-1}g)(s)=\int_0^\infty e^{-v/2}g(s+v)\,dv.
\]
The adjoint of this operator is one-sided convolution with \(e^{-v/2}\). Under the unitary Laplace transform onto \(H^2(\operatorname{Re}z>0)\), the adjoint becomes multiplication by \(m(z)=(z+\tfrac12)^{-1}\). The Cayley coordinate \(\zeta=(z-\tfrac12)/(z+\tfrac12)\) gives \(m=1-\zeta\). Conformal Hardy-space equivalence therefore makes \(H_0\) unitarily equivalent to \(I-S^*\), where \(S\) is the unilateral shift on \(H^2(\mathbb D)\). The standard shift Fredholm calculation implies
\[
\sigma(H_0)=\overline D,\quad \sigma_{\mathrm F}(H_0)=\partial D,
\quad \operatorname{ind}(H_0-\lambda I)=1\ (\lambda\in D),
\]
and index zero and invertibility outside \(\overline D\). In particular \(\|H_0\|=\|H_0\|_{\mathrm{ess}}=2\).

**3. Subcritical Hilbert–Schmidt perturbation.** The integral kernel of \(H_\gamma-H_0\) is
\[
K_\gamma(x,t)=x^{-1}\mathbf1_{0<t<x<1}\bigl((1-t)^{-\gamma}-1\bigr).
\]
Consequently, Fubini gives
\[
\|K_\gamma\|_{L^2((0,1)^2)}^2
=\int_0^1\bigl((1-t)^{-\gamma}-1\bigr)^2\left(\frac1t-1\right)dt.
\]
The integrand is \(O(t)\) near \(t=0\); at \(t=1\) it is integrable precisely when \(\gamma<1\). With \(s=1-t\), the digamma identity \(\int_0^1(s^{a-1}-s^{b-1})(1-s)^{-1}ds=\psi(b)-\psi(a)\), for \(a,b>0\), yields the stated closed form. The Laurent expansion of \(\psi(2-2\gamma)\) at zero gives the quoted blowup. Compact-perturbation invariance transfers the full Fredholm essential spectrum and Fredholm indices of \(H_0\) to every \(H_\gamma\) with \(\gamma<1\).

**4. Point spectrum and absence of exterior eigenvalues.** For \(\lambda\ne0\), differentiation of \(H_\gamma f=\lambda f\) implies, for some scalar \(c\),
\[
f_{\lambda,\gamma}(x)
=c\,x^{1/\lambda-1}
\exp\left(\frac1\lambda\int_0^x\frac{(1-t)^{-\gamma}-1}{t}\,dt\right).
\]
The second factor is bounded above and below in modulus on \((0,1)\) for fixed \(\gamma<1\) and \(\lambda\ne0\): its exponent has finite limits at both ends. Hence \(f_{\lambda,\gamma}\in L^2(0,1)\) exactly when \(\operatorname{Re}(1/\lambda)>1/2\), equivalently \(\lambda\in D\). In this range \(\lambda xf_{\lambda,\gamma}(x)\to0\) as \(x\downarrow0\), so integration of the differentiated equation recovers the original eigenvalue equation. A first-order ODE gives geometric multiplicity one; at \(\lambda=0\), the integral operator is injective, since its weight is everywhere positive. For \(\lambda\notin\overline D\), the compactly perturbed operator is Fredholm of index zero with trivial kernel and is therefore invertible. For \(\lambda\in D\), its Fredholm index and one-dimensional kernel imply zero cokernel: these interior eigenvalues are surjective. This proves the complete subcritical spectrum.

**5. Exact norm for the entire bounded range.** For \(\gamma\le1\), \(0<(1-t)^{-\gamma}\le(1-t)^{-1}\), whence \(|H_\gamma f|\le H_1|f|\) and \(\|H_\gamma\|\le2\). Conversely, for any \(h\in C_c(0,1)\), embed \(h\) near zero by \(f_\delta(x)=\delta^{-1/2}h(x/\delta)\mathbf1_{x<\delta}\). On \((0,\delta)\), the rescaled image of \(H_\gamma f_\delta\) converges in \(L^2\) to \(H_0h\), as \(\delta\downarrow0\). Taking the supremum over this dense class gives \(\|H_\gamma\|\ge\|H_0\|=2\). For \(\gamma<1\), the Hilbert–Schmidt perturbation also forces \(\|H_\gamma\|_{\mathrm{ess}}=\|H_0\|_{\mathrm{ess}}=2\), and for \(\gamma=1\) this follows from Step 1.

**6. A maximal norm and essential-norm jump despite strong convergence.** For \(\gamma<1\), the kernel \((1-t)^{-1}-(1-t)^{-\gamma}\) is nonnegative, so \(\|H_1-H_\gamma\|\le2\). Let \(h\in C_c(0,1)\) and set
\[
f_\delta(t)=\delta^{-1/2}h\bigl((1-t)/\delta\bigr)\mathbf1_{1-\delta<t<1}.
\]
Then \(\|f_\delta\|_2=\|h\|_2\) and \(f_\delta\rightharpoonup0\) weakly. On the rescaled output boundary layer \(x=1-\delta s\), \(0<s<1\),
\[
\sqrt\delta\,[(H_1-H_\gamma)f_\delta](1-\delta s)
=\frac1{1-\delta s}\int_s^1
\left(u^{-1}-\delta^{1-\gamma}u^{-\gamma}\right)h(u)\,du
\longrightarrow\int_s^1\frac{h(u)}u\,du
\]
in \(L^2(0,1)\). The limit is \(H_0^*h\) and \(\|H_0^*\|=2\). Thus the weakly-null sequence gives distance at least \(2\) from every compact operator, while domination gives upper bound \(2\). Finally, as \(\gamma\uparrow1\), the kernels converge pointwise; for functions supported a fixed positive distance from \(1\), dominated convergence gives \(H_\gamma f\to H_1f\) in \(L^2\). Uniform norm bound \(2\) and density yield strong convergence on all \(L^2(0,1)\).

**7. Supercritical unboundedness.** Fix nonnegative nonzero \(h\in C_c((1/4,3/4))\) and use the same boundary-concentrated \(f_\delta\). On \(x=1-\delta s\) its output has rescaled form
\[
\sqrt\delta\,(H_\gamma f_\delta)(1-\delta s)
=\frac{\delta^{1-\gamma}}{1-\delta s}\int_s^1u^{-\gamma}h(u)\,du.
\]
The fixed nonzero integral has positive \(L^2(0,1)\)-norm. For \(\gamma>1\) the output-to-input norm ratio diverges as \(\delta\downarrow0\), excluding any bounded extension.

## Verification

The identities in Steps 1–7 constitute the infinite-dimensional proof. The accompanying `verify.py` uses high-precision quadrature to test the digamma Hilbert–Schmidt identity, the explicit eigenfunction integral equation, the one-sided exponential convolution multiplier, and the predicted sign and scale of the Hilbert–Schmidt divergence. A successful finite computation is only a supplementary check, not proof of the spectra, Fredholm indices, essential norms, or strong-limit statement. Execute with `python verify.py` after installing `mpmath`.

## Relationship to prior work

Belli, Gül, Ross, and Siskakis (arXiv:2604.19691; arXiv:2606.08600) established the norm, normality, and spectral circle of \(H_1\), and extended the latter operator to \(L^p\). Those facts are credited; the variable kernel exponent here is a different deformation from their varying ambient \(L^p\) exponent. Brown–Halmos–Shields studied the classical Hardy averaging model \(H_0\). Abadías, Mahillo, and Miana (arXiv:2604.20408) analyze fractional Cesàro–Hardy kernels \(x^{-\alpha}(x-t)^{\alpha-1}\), not the endpoint-power kernel \(x^{-1}(1-t)^{-\gamma}\) treated here. Existing general compact-perturbation and unilateral-shift Fredholm theorems are used explicitly and are not claimed as new. The additional all-parameter phase diagram and exact strong-but-essentially-maximal critical discontinuity are the asserted new combination.

## Limitations

Only real endpoint-power exponents and unweighted complex \(L^2(0,1)\) are treated. No spectral classification on other \(L^p\) spaces or for arbitrary endpoint weights is asserted. The Hilbert–Schmidt formula controls the difference from \(H_0\); it is not an exact formula for all singular values of \(H_\gamma-H_0\). The strong limit is one-sided \(\gamma\uparrow1\), not operator-norm convergence. Publication priority against every unindexed weighted Hardy-operator theorem is not certified; the nearest inspected results use different operator kernels or different ambient spaces. Independent external validation has not been performed.

## References

1. A. Belli, U. Gül, W. T. Ross, A. G. Siskakis, *The Cesàro operator on \(L^2(0,1)\)*, arXiv:2604.19691v2 (first posted April 21, 2026), https://arxiv.org/html/2604.19691v2.
2. A. Belli, U. Gül, W. T. Ross, A. G. Siskakis, *Crescents and the Real Variable Cesàro Operator*, arXiv:2606.08600v1 (first posted June 7, 2026); *Integral Equations and Operator Theory* **98** (2026), article 42, https://doi.org/10.1007/s00020-026-02865-7.
3. L. Abadías, A. Mahillo, P. J. Miana, *Cesàro–Hardy operators on \(L^p[0,1]\): fine spectrum, weighted Koopman semigroups and invariant subspaces*, arXiv:2604.20408 (first posted April 22, 2026), https://arxiv.org/html/2604.20408.
4. A. Brown, P. R. Halmos, A. L. Shields, *Cesàro operators*, *Acta Scientiarum Mathematicarum (Szeged)* **26** (1965), 125–137.
