# Bessel-to-Laplace profiles and ballistic fronts in a weakly restarted three-state quantum walk

## Finding

For the one-dimensional lackadaisical discrete-time quantum walk with complete geometric resetting, take the localized **flat-band-dark** coin state defined below. At each step the entire state is restarted independently with probability \(q\). Let \(X_t\) denote a position measured from the restart site, and let \(X_q^{\mathrm{st}}\) have the stationary position distribution. Fix any self-loop weight \(\ell>0\), and put
\[
u=\sqrt{\frac{\ell}{\ell+2}},\qquad
\rho_\ell(v)=\frac{\sqrt{1-u^2}}{\pi(1-v^2)\sqrt{u^2-v^2}}\mathbf 1_{\{|v|<u\}}.
\]
Then \(\rho_\ell\) is a normalized, even probability density. As \(q\downarrow0\),
\[
qX_q^{\mathrm{st}}\ \Longrightarrow\ Y_\ell=EV_\ell,
\]
where \(E\) has the unit-rate exponential law, \(V_\ell\) has density \(\rho_\ell\), and they are independent. The limiting characteristic function is the **elementary closed form**
\[
\boxed{\quad
\mathbb E e^{i\xi Y_\ell}
=\frac{1+\xi^2\sqrt{(1-u^2)/(1+u^2\xi^2)}}{1+\xi^2}.
\quad}
\]
Its even probability density, for every \(y\ne0\), is
\[
\boxed{\quad
g_\ell(y)=\int_0^u\frac{\rho_\ell(v)}{v}e^{-|y|/v}\,dv.
\quad}
\]
At the center and far from it, this density has the two distinct sharp laws
\[
\boxed{\quad
g_\ell(y)=\frac1\pi\sqrt{\frac2\ell}\log\frac1{|y|}+O_\ell(1),\qquad y\to0,
\quad}
\]
\[
\boxed{\quad
g_\ell(y)\sim\sqrt{\frac{\ell+2}{4\pi u|y|}}e^{-|y|/u},\qquad |y|\to\infty.
\quad}
\]
There are also two exact **iterated self-loop endpoints**. With the weak-reset limit taken first,
\[
\frac{Y_\ell}{u}\ \Longrightarrow\ \frac1\pi K_0(|y|)\,dy
\quad\text{as }\ell\downarrow0,
\qquad
Y_\ell\ \Longrightarrow\ \frac12e^{-|y|}\,dy
\quad\text{as }\ell\to\infty,
\]
where \(K_0\) is the modified Bessel function and the displayed densities specify the limiting measures.

The result extends to a complete transient spatial-profile crossover. For every fixed \(z>0\), with \(t_q=\lfloor z/q\rfloor\),
\[
qX_{t_q}\ \Longrightarrow\ Y_{\ell,z}=\min(E,z)V_\ell.
\]
For \(0<|y|<uz\), the density is
\[
g_{\ell,z}(y)=\frac{e^{-z}}z\rho_\ell(y/z)
+\int_{|y|/u}^z\frac{e^{-a}}a\rho_\ell(y/a)\,da,
\]
and it vanishes for \(|y|>uz\). The advancing ballistic edge is singular with an **exact prefactor**:
\[
\boxed{\quad
g_{\ell,z}(y)\sim
\frac{e^{-z}}{2\pi\sqrt z}\sqrt{\frac{\ell+2}{u}}
\frac1{\sqrt{uz-|y|}},\qquad |y|\uparrow uz.
\quad}
\]
Consequently the finite-time compact support with its square-root ballistic front becomes the stationary, unbounded, exponentially tailed profile after the rescaled observation time tends to infinity. All weak-reset spatial moments of positive order converge to their counterparts under these limits.

## Assumptions and scope

The walker lives on \(\mathbb Z\) with coin basis \(\{|-1\rangle,|0\rangle,|+1\rangle\}\). For a fixed \(\ell>0\), define
\[
|s_\ell\rangle=\frac{(1,\sqrt\ell,1)^\mathsf T}{\sqrt{\ell+2}},\qquad
C_\ell=2|s_\ell\rangle\langle s_\ell|-I_3,
\]
with one-step unitary \(U_\ell=S(C_\ell\otimes I)\), where \(S\) moves coin components by \(-1,0,+1\) sites. Initially, and after each reset, the walker is placed at the origin with coin
\[
|\chi_\perp\rangle=\frac{(\sqrt\ell,-2,\sqrt\ell)^\mathsf T}{\sqrt{2(\ell+2)}}.
\]
Each resetting event erases the complete prior position-and-coin state. The reset decision is independent at each discrete step. Position refers to a measurement of the ensemble at the stated time, not repeated projective monitoring along one uninterrupted quantum trajectory. The stationary state is the classical mixture over the geometrically distributed age \(A_q\) with \(\Pr(A_q=a)=q(1-q)^a\), \(a=0,1,\ldots\). The limits in the theorem hold for each **fixed** \(\ell>0\) as \(q\to0^+\); the \(\ell\)-endpoint limits are taken afterward.

## Proof

**1. Ballistic velocity density.** In momentum \(k\in[-\pi,\pi)\), the lackadaisical walk has one flat band and two dispersive eigenphases, whose group speed has magnitude
\[
|v(k)|=\sqrt{\frac{\ell(1+\cos k)}{\ell+4+\ell\cos k}}
=\frac{\sqrt\ell\,|\cos(k/2)|}{\sqrt{2+\ell\cos^2(k/2)}}.
\]
The specified coin is orthogonal to the flat-band eigenvector at every \(k\). The established ballistic spectral law then gives convergence of the restart-free displacement divided by its age to a velocity \(V_\ell\); its total dispersive spectral weight is one. Reflection interchanging the left and right coin states leaves both the coin and the initial state invariant, so this velocity distribution is even. A uniform \(k\) has \(T=|\cos(k/2)|\) with density \(2/(\pi\sqrt{1-T^2})\) on \((0,1)\). Pushing this forward through \(|v|=\sqrt\ell\,T/\sqrt{2+\ell T^2}\), and splitting evenly between the two signs, gives exactly \(\rho_\ell\). Its normalization follows from the change of variables \(v=u\sin\theta\):
\[
2\int_0^u\rho_\ell(v)\,dv
=\frac{2\sqrt{1-u^2}}\pi\int_0^{\pi/2}\frac{d\theta}{1-u^2\sin^2\theta}=1.
\]
In particular \(V_\ell\) has no atom at zero. The underlying ballistic law itself is not claimed as new.

**2. Renewal-time mixing and all moments.** For stationary geometric reset, the measured position has the law of the restart-free position after an independent age \(A_q\). Since \(qA_q\Rightarrow E\), \(A_q\to\infty\) in probability, and the conditional restart-free velocity converges to \(V_\ell\), the pair \((qA_q,X_{A_q}/A_q)\) converges jointly to independent \((E,V_\ell)\); the zero-age term has vanishing probability. The product map yields \(qX_q^{\mathrm{st}}\Rightarrow EV_\ell\). At \(t_q=\lfloor z/q\rfloor\), the last-reset age equals \(t_q\) if there has been no reset, otherwise its probability at age \(a<t_q\) is \(q(1-q)^a\). Thus its rescaling converges to \(\min(E,z)\), giving the transient assertion. In every case the nearest-neighbor support bound \(|X_a|\le a\), combined with uniform exponential-tail bounds on \(qA_q\), makes positive-order powers uniformly integrable. Hence, for every \(p>0\),
\[
\lim_{q\downarrow0}\mathbb E|qX_q^{\mathrm{st}}|^p
=\Gamma(p+1)\int_{-u}^{u}|v|^p\rho_\ell(v)\,dv,
\]
\[
\lim_{q\downarrow0}\mathbb E|qX_{t_q}|^p
=\left(\int_0^z e^{-a}a^p\,da+e^{-z}z^p\right)
\int_{-u}^{u}|v|^p\rho_\ell(v)\,dv.
\]
This also recovers the published mean-square-displacement crossover without claiming it anew.

**3. Explicit stationary transform and density.** Conditioning on \(V_\ell=v\), the independent exponential age has characteristic function \((1-i\xi v)^{-1}\). By evenness,
\[
\mathbb E e^{i\xi Y_\ell}
=2\int_0^u\frac{\rho_\ell(v)}{1+\xi^2v^2}\,dv.
\]
Writing \(a=u^2\), substituting \(v=u\sin\theta\), and decomposing
\[
\frac1{(1-a\sin^2\theta)(1+a\xi^2\sin^2\theta)}
=\frac1{1+\xi^2}\frac1{1-a\sin^2\theta}
+\frac{\xi^2}{1+\xi^2}\frac1{1+a\xi^2\sin^2\theta},
\]
we use \(\int_0^{\pi/2}(1+b\sin^2\theta)^{-1}d\theta=\pi/(2\sqrt{1+b})\) for \(b>-1\) to obtain the boxed elementary characteristic function. The conditional exponential density for each signed nonzero velocity gives the displayed expression for \(g_\ell\).

**4. Sharp center, tails, and moving edge.** Smoothness and evenness give \(\rho_\ell(v)=\rho_\ell(0)+O_\ell(v^2)\) near zero, where \(\rho_\ell(0)=\pi^{-1}\sqrt{2/\ell}\). Splitting the density integral at a fixed small positive velocity shows its singular contribution to be \(\rho_\ell(0)\int e^{-|y|/v}dv/v=\rho_\ell(0)\log(1/|y|)+O_\ell(1)\). Near the maximal speed, writing \(v=u-h\),
\[
\rho_\ell(u-h)\sim \frac1{2\pi}\sqrt{\frac{\ell+2}{u}}\,h^{-1/2}.
\]
Laplace's endpoint method in the density integral, with \(1/v=1/u+h/u^2+O(h^2)\), yields the boxed exponential tail and square-root prefactor. The law of \(\min(E,z)\) has an atom of mass \(e^{-z}\) at \(z\), together with density \(e^{-a}\) on \((0,z)\). This yields the transient-density formula. As \(|y|\uparrow uz\), the atom-at-\(z\) term diverges as the displayed inverse square root, while the continuous-age contribution is only \(O_{\ell,z}(\sqrt{uz-|y|})\), proving the sharp front law.

**5. Two self-loop endpoints.** As \(\ell\downarrow0\), the rescaled velocity \(V_\ell/u\) converges to the arcsine law on \((-1,1)\). The product with an independent exponential variable has density
\[
\frac1\pi\int_0^1\frac{e^{-|y|/v}}{v\sqrt{1-v^2}}\,dv
=\frac1\pi\int_0^\infty e^{-|y|\cosh t}\,dt
=\frac1\pi K_0(|y|).
\]
As \(\ell\to\infty\), the dispersive velocity tends to an equal mixture of \(+1\) and \(-1\); multiplying by the exponential age gives the symmetric Laplace density \(e^{-|y|}/2\). These statements use sequential limits, not an unrestricted simultaneous scaling.

## Verification

The accompanying standalone Python program checks normalization, independent quadrature of the characteristic function, asymptotic constants, the two self-loop endpoint transforms, and finite-reset data generated directly by repeated application of the three-component coin-and-shift operator. The numerical walk is a finite-age truncation with an explicit geometric remainder bound. These checks corroborate, but do not replace, the preceding analytic proof. Run with Python 3, NumPy and SciPy using `python verify_walk.py`.

## Relationship to prior work

Das, *Restart and first detection in a lackadaisical quantum walk with flat-band localization* (arXiv:2609.08973v1), supplies the coin, the flat-band-dark preparation, the geometric stationary-age representation, the restart-free ballistic spectral law and a weak-reset mean-square-displacement crossover. These facts are inputs, not new claims. What is calculated here is the explicit **entire rescaled position law** in closed characteristic-function form, its logarithmic central singularity, sharp exponential spatial tail and transient front, and the Bessel-to-Laplace self-loop classification. The formulas in that paper make this direction natural and may imply portions of the present result when combined with additional analysis; they do not state these combined explicit profiles and singular constants.

Wald and Böttcher, *From classical to quantum walks with stochastic resetting on networks* (Phys. Rev. E 103, 012122, 2021), analyze resetting in classical–quantum network walks; Wald, Yao, Platini, Hooley and Carollo, *Stochastic resetting in discrete-time quantum dynamics* (Quantum 9, 1742, 2025), study finite-dimensional gate dynamics and their reset stationary states. Chełminiak, Wójcik and Wójcik, *Discrete-time walk on one-dimensional lattice under stochastic resetting* (Phys. Rev. E 111, 044143, 2025), primarily study monitored absorption. None of these sources was used to claim a new renewal principle or ballistic spectral law. The scientific distinction is the spatial weak-reset density and its two explicitly calculated geometric singularities for a self-loop-deformed three-state walk.

## Limitations

This is a one-dimensional, translation-invariant, perfectly reinitialized three-state quantum walk. The theorem specializes to the specified flat-band-dark coin state and does not classify every initial coin. Its elementary formula is for the **scaling limit** of ensemble position distributions; it is not an exact finite-reset-position law or a pathwise theorem under projective monitoring. The Bessel and Laplace endpoints take the weak-reset limit first. The source's general renewal and spectral formulas are strong antecedents, so a specialist priority review should inspect whether a broader unrecognized theorem implicitly supplies these explicit constants. 

## References

1. D. Das, *Restart and first detection in a lackadaisical quantum walk with flat-band localization*, arXiv:2609.08973v1 (September 8, 2026), https://arxiv.org/abs/2609.08973 ; full HTML https://arxiv.org/html/2609.08973.
2. S. Wald and L. Böttcher, *From classical to quantum walks with stochastic resetting on networks*, Phys. Rev. E **103**, 012122 (2021), https://doi.org/10.1103/PhysRevE.103.012122.
3. S. Wald, L. H. Yao, T. Platini, C. Hooley and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, Quantum **9**, 1742 (2025), https://doi.org/10.22331/q-2025-05-13-1742.
4. P. Chełminiak, J. Wójcik and A. Wójcik, *Discrete-time walk on one-dimensional lattice under stochastic resetting: Advantage of quantum over classical scenario*, Phys. Rev. E **111**, 044143 (2025), https://doi.org/10.1103/PhysRevE.111.044143.
