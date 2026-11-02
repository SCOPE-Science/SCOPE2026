# Gradient alignment doubles the codimension threshold for Haar-subspace quadratic steps

## Finding
For a rank-one-singular positive-semidefinite quadratic model, a uniformly randomized \(k\)-dimensional subspace makes the reduced Hessian invertible almost surely. But the unrestricted reduced minimizer can have an infinite mean-square Euclidean norm. An exact threshold depends on both the codimension and whether the gradient is exactly in the Hessian's range.

Let \(r=d-k\), \(a=k/2\), and \(b=r/2\). If the gradient has any nonzero component in the Hessian kernel, the step-norm tail has exponent \(b\); if the gradient is nonzero and orthogonal to that kernel, the exponent is instead \(2b\). These exponents are exact, with positive explicit constants. Hence the sharp finite-second-moment conditions are \(r>4\) for kernel-contaminated gradients and \(r>2\) for kernel-orthogonal gradients.

This is an exact diagnostic of a potentially fragile modeling choice: in a Gauss--Newton-type local model the exact gradient is in the reduced curvature's range, but even a tiny inconsistent kernel component can destroy the unconditional step variance at codimensions three and four. It does not assert that a safeguarded optimization algorithm diverges.

## Assumptions and scope
Fix integers \(d\ge2\), \(1\le k<d\), a scalar \(c>0\), and a unit vector \(e\in\mathbb R^d\). Put \(H=c(I-ee^{\mathsf T})\), let \(U\in\mathbb R^{d\times k}\) be a Haar-uniform orthonormal frame, and define
\[
 s_\varepsilon(U,g)=U\big(U^{\mathsf T}(H+\varepsilon I)U\big)^{-1}U^{\mathsf T}g,
 \qquad \varepsilon\ge0.
\]
The inverse at \(\varepsilon=0\) exists with probability one because \(k<d\). The sign of this step is immaterial: the unconstrained minimizer of \(s^{\mathsf T}Hs/2-g^{\mathsf T}s\) in \(\operatorname{ran}U\) is \(s_0\). Set \(g_\parallel=e^{\mathsf T}g\), \(g_\perp=g-g_\parallel e\), \(r=d-k\), \(a=k/2\), and \(b=r/2\). Expectations and probabilities are over the Haar subspace, with deterministic \(g\). The beta function is \(B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)\).

Let \(W\) be a fixed coordinate of a uniformly distributed unit vector in \(\mathbb R^{d-1}\); if \(d=2\), then \(|W|=1\) almost surely. Define \(\mu_q=\mathbb E|W|^q\), with \(\mu_q=\Gamma((d-1)/2)\Gamma((q+1)/2)/(\sqrt\pi\Gamma((d-1+q)/2))\) for \(d\ge3\) (the same formula also yields one for \(d=2\)).

The exact tail laws for any fixed nonzero \(g\) are
\[
 \lim_{t\to\infty}t^b\Pr(\|s_0\|>t)=\frac{(|g_\parallel|/c)^b}{bB(a,b)}\quad\text{if }g_\parallel\ne0,
\]
\[
 \lim_{t\to\infty}t^{2b}\Pr(\|s_0\|>t)=\frac{(\|g\|/c)^{2b}\mu_{2b}}{bB(a,b)}\quad\text{if }g_\parallel=0.
\]
Thus the exact moment threshold is \(0<q<b\) in the first case and \(0<q<2b\) in the second. For the zero gradient all moments are zero. At the boundary moments the expectation diverges.

For \(r>4\), every gradient satisfies
\[
 \mathbb E\|s_0\|^2=\frac1{c^2}\left[
 \frac{k(d-2)}{(r-2)(r-4)}g_\parallel^2+
 \frac{k(r-1)}{(d-1)(r-2)}\|g_\perp\|^2\right].
\]
For a kernel-orthogonal gradient the second term alone is valid whenever \(r>2\). In particular, with \(d=5,k=1,c=1\) (so \(r=4\)), a unit kernel-orthogonal gradient has expected squared step \(3/8\), whereas every gradient with nonzero kernel component has infinite expected squared step.

For a purely kernel-parallel gradient \(g=g_\parallel e\ne0\), ridge regularization has exact regimes as \(\varepsilon\downarrow0\):
\[
\mathbb E\|s_\varepsilon\|^q\to (|g_\parallel|/c)^q\frac{B(a+q/2,b-q)}{B(a,b)}\quad (0<q<b),
\]
\[
\mathbb E\|s_\varepsilon\|^b\sim\frac{|g_\parallel|^b}{c^b B(a,b)}\log\frac c\varepsilon,
\qquad
\mathbb E\|s_\varepsilon\|^q\sim\frac{|g_\parallel|^q B(b,q-b)}{c^b B(a,b)}\varepsilon^{b-q}\quad(q>b).
\]

## Proof
Let \(P=UU^{\mathsf T}\), \(v=U^{\mathsf T}g\), \(a_U=U^{\mathsf T}e\), and \(T=\|a_U\|^2=\|Pe\|^2\). Rotational invariance yields \(T\sim\operatorname{Beta}(a,b)\) by the ratio of independent chi-square sums of degrees \(k\) and \(d-k\). In particular \(0<T<1\) almost surely.

The reduced Hessian is \(c(I_k-a_Ua_U^{\mathsf T})\). Sherman--Morrison gives
\[
 s_0=c^{-1}U\left[v+\frac{a_U(a_U^{\mathsf T}v)}{1-T}\right],\qquad
 c^2\|s_0\|^2=\|v\|^2+\frac{(2-T)(a_U^{\mathsf T}v)^2}{(1-T)^2}.
\]
For \(g=g_\parallel e\), this simplifies exactly to \(\|s_0\|=|g_\parallel|\sqrt T/[c(1-T)]\). The beta density of \(Y=1-T\) satisfies \(f_Y(y)=y^{b-1}(1-y)^{a-1}/B(a,b)\); hence \(\Pr(Y<y)\sim y^b/[bB(a,b)]\). This proves the aligned tail and the aligned beta-moment formula. If \(g=g_\parallel e+g_\perp\) with \(g_\parallel\ne0\), the singular part along \(e\) is of size \(Y^{-1}\), while the orthogonal part is at most order \(Y^{-1/2}\), uniformly in the other random directions. Its relative contribution vanishes as \(Y\downarrow0\), proving the same leading tail.

If \(g\perp e\), then \(a_U^{\mathsf T}v=e^{\mathsf T}Pg\). By \(P^2=P\), the transverse vector \(Pe-Te\) has squared length \(T(1-T)\). Conditional on \(T\), its normalized direction in \(e^\perp\) is uniform and independent of \(T\); therefore \(e^{\mathsf T}Pg=\|g\|\sqrt{T(1-T)}W\). Substitution gives the exact pathwise identity
\[
 c^2\|s_0\|^2=g^{\mathsf T}Pg+\frac{\|g\|^2T(2-T)W^2}{1-T}.
\]
The first term is bounded by \(\|g\|^2\). The second is equivalent near \(Y=0\) to \(\|g\|^2W^2/Y\); beta lower tails, independence, and dominated integration over bounded \(|W|\) yield the perpendicular constant and moment threshold. All constants are strictly positive for \(g\ne0\).

For the exact second moment, the beta identities give \(\mathbb E[T/(1-T)^2]=k(d-2)/[(r-2)(r-4)]\) when \(r>4\). Separately, the perpendicular case uses \(\mathbb E[g^{\mathsf T}Pg]=(k/d)\|g\|^2\), \(\mathbb EW^2=1/(d-1)\), and \(\mathbb E[T(2-T)/(1-T)]=(d-2)/(r-2)-r/d\) when \(r>2\). The formula follows by algebra; mixed cross terms vanish by reflection \(g_\perp\mapsto-g_\perp\) under the Haar law. Nonintegrability at the stated endpoints follows from the positive tail constants, not from numerical truncation.

For the ridge regimes, the aligned step satisfies \(\|s_\varepsilon\|=|g_\parallel|\sqrt T/[\varepsilon+c(1-T)]\). Integrate its \(q\)-th power against the beta density. Dominated convergence applies when \(q<b\). At \(q=b\), integrate \(y^{b-1}/(\varepsilon+cy)^b\) over \(\varepsilon/c\ll y\ll1\) to obtain the logarithm. For \(q>b\), set \(y=(\varepsilon/c)u\) and integrate \(u^{b-1}/(1+u)^q\) over \((0,\infty)\), giving \(B(b,q-b)\).

As a further robustness fact, if \(H\succeq0\) has one-dimensional kernel \(\operatorname{span}(e)\) and \(m(I-ee^{\mathsf T})\preceq H\preceq M(I-ee^{\mathsf T})\) for \(0<m\le M\), then for the purely kernel-aligned gradient \(e\), the exact subspace step satisfies
\[
\frac{\sqrt T}{M(1-T)}\le\|U(U^{\mathsf T}HU)^{-1}U^{\mathsf T}e\|\le\frac{\sqrt T}{m(1-T)}.
\]
The lower inequality follows from Loewner inversion and Cauchy--Schwarz, while the upper follows from the reduced smallest eigenvalue being at least \(m(1-T)\). Thus the aligned \(q<b\) moment threshold persists for every fixed positive-definite spectrum on \(e^\perp\), even though its exact tail coefficient can change.

## Verification
The accompanying standalone `verify.py` reconstructs the reduced inverse by direct finite-dimensional Gaussian elimination and compares it against the Sherman--Morrison formula on reproducible Haar frames. It also checks the beta-moment simplifications using exact rational identities, both the aligned and perpendicular special cases, and anisotropic pathwise bounds. Numerical probes are finite diagnostic checks, not proofs of the tail limits. The mathematical proof above uses the beta law and explicit integration.

## Relationship to prior work
Cartis and Roberts (2021 preprint; journal version 2022/2023) investigate random-subspace optimization and derivative-free Gauss--Newton models with trust-region safeguards. Cartis, Fowkes and Shao (2022) explicitly analyze random-subspace methods under trust regions or quadratic regularization. Their theorems therefore do not give the unsafeguarded finite-dimensional step-norm tail and gradient-alignment classification here. Pilanci and Wainwright's Newton Sketch concerns condition-controlled sketched Newton steps for strongly convex or self-concordant models. LeJeune et al.'s *Asymptotics of the Sketched Pseudoinverse* concerns high-dimensional spectral equivalents and requires care at singular, unregularized inversion thresholds; it does not supply the exact fixed-dimensional Haar-geometry phase law here in the inspected treatment.

The beta projection identity, Sherman--Morrison inversion and chi-square ratio law are standard tools; no originality is claimed for them. What is assessed here is their precise combination into a kernel-alignment/codimension moment and tail classification, including the explicit discontinuity under arbitrarily small inconsistent gradient components.

## Limitations
The main exact constants require an isotropic Hessian on the orthogonal complement of its one-dimensional kernel and Haar-uniform subspaces. The anisotropic extension establishes only a moment threshold, not an exact coefficient. A gradient component along the kernel makes the unrestricted full-space quadratic unbounded below, even though the random reduced problem has a unique minimizer almost surely. This is therefore a statement about **unconstrained local model steps**, not about globally well-posed optimization or an actual safeguarded algorithm. The results do not establish finite-precision error, convergence rates of iterative methods, multistep dynamics, or a general nonlinear theorem. Independent review and a complete publication-priority assessment remain outstanding.

## References
1. C. Cartis and L. Roberts, *Scalable Subspace Methods for Derivative-Free Nonlinear Least-Squares Optimization*, public preprint 23 February 2021, https://optimization-online.org/2021/02/8264/ ; arXiv:2102.12016, https://arxiv.org/abs/2102.12016 .
2. C. Cartis, J. Fowkes and Z. Shao, *Randomised Subspace Methods for Non-convex Optimization, with Applications to Nonlinear Least-squares*, arXiv:2211.09873 (2022), https://arxiv.org/abs/2211.09873 .
3. E. LeJeune, P. Patil, H. Javadi, R. G. Baraniuk and R. J. Tibshirani, *Asymptotics of the Sketched Pseudoinverse*, SIAM Journal on Mathematics of Data Science, https://doi.org/10.1137/22M1530264 .
4. M. Pilanci and M. J. Wainwright, *Newton Sketch: A Near Linear-Time Optimization Algorithm with Linear-Quadratic Convergence*, SIAM Journal on Optimization, https://doi.org/10.1137/15M1021106 .
