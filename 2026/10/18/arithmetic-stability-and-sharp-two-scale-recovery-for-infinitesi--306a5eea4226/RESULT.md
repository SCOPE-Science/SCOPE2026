# Arithmetic stability and sharp two-scale recovery for infinitesimal planar chord tomography

## Finding

Let the unit disk be perturbed by a real radial function \(f\in C^3(\mathbb R/2\pi\mathbb Z)\). For each angle \(0<\alpha<\pi/2\), measure, in every oriented normal direction \(\theta\), the length of the chord cut out by the line at signed distance \(t=\cos\alpha\) from the origin. The first variation of this chord-length function at the disk is the operator
\[
(D_\alpha f)(\theta)=\frac{f(\theta+\alpha)+f(\theta-\alpha)}{\sin\alpha}.
\]

**Finite-offset stability classification.** For a finite nonempty family \(\boldsymbol\alpha=(\alpha_1,\ldots,\alpha_k)\in(0,\pi/2)^k\), the combined first-variation map \(D_{\boldsymbol\alpha}f=(D_{\alpha_1}f,\ldots,D_{\alpha_k}f)\) admits an \(L^2\) lower stability estimate
\[
\sum_{j=1}^k\|D_{\alpha_j}f\|_2^2\ge c_{\boldsymbol\alpha}\|f\|_2^2
\quad\text{for every }f\in L^2(S^1)
\]
with some positive \(c_{\boldsymbol\alpha}\) **if and only if** there is an integer vector \(h=(h_1,\ldots,h_k)\in\mathbb Z^k\) with
\[
\sum_{j=1}^k h_j\alpha_j\in\pi\mathbb Z
\quad\text{and}\quad
\sum_{j=1}^k h_j\text{ odd}.
\]
The optimal lower constant is the infimum, over \(m\in\mathbb Z\), of the explicitly known modal weights
\[
W_m(\boldsymbol\alpha)=\sum_{j=1}^k\frac{4\cos^2(m\alpha_j)}{\sin^2\alpha_j}.
\]
If all \(\alpha_j/\pi=p_j/q_j\) are reduced positive rationals, there is a nonzero common kernel precisely when all denominators \(q_j\) are even and have the same \(2\)-adic valuation. In that event the kernel consists exactly of harmonics with indices
\[
m=(2\ell+1)\operatorname{lcm}(q_1/2,\ldots,q_k/2),\qquad\ell\in\mathbb Z.
\]
For rational families, absence of a common kernel is equivalent to uniform stability. In particular, for a single reduced rational angle \(\alpha/\pi=p/q\) with odd \(q\), the sharp lower squared bound is \(4\sin^2(\pi/(2q))/\sin^2\alpha\). A single irrational angle has no exact kernel but is never bounded below. If at least one \(\alpha_j/\pi\) in a multi-offset family is irrational, there is no exact common kernel, although there may be no uniform lower bound.

**Universal two-scale design.** For every \(0<\alpha<\pi/4\), the two chord offsets \(\cos\alpha\) and \(\cos(2\alpha)\) always yield
\[
\boxed{\left(1+\csc^2\alpha\right)\|f\|_2^2\le
\|D_\alpha f\|_2^2+\|D_{2\alpha}f\|_2^2
\le \left(4\csc^2\alpha+4\csc^2(2\alpha)\right)\|f\|_2^2.}
\]
The upper coefficient is attained by the constant mode, and the lower coefficient is optimal for every irrational \(\alpha/\pi\). Thus two individually ill-conditioned fixed-offset measurements can have a uniformly stable joint linearization.

As an exact rational example, at \(\alpha_1=\pi/6\) and \(\alpha_2=\pi/4\), the sharp constants are \(4\) and \(24\):
\[
4\|f\|_2^2\le\|D_{\pi/6}f\|_2^2+\|D_{\pi/4}f\|_2^2\le24\|f\|_2^2.
\]
Neither measurement alone is injective on first-order perturbations.

## Assumptions and scope

Let \(u_\theta=(\cos\theta,\sin\theta)\). For sufficiently small real \(\varepsilon\), define
\[
K_\varepsilon=\{r(\cos\phi,\sin\phi):0\le r\le1+\varepsilon f(\phi)\},
\qquad f\in C^3(S^1;\mathbb R).
\]
Here \(\varepsilon\) is small enough that the radial function is positive and the curve is strictly convex; this follows from positivity at \(\varepsilon=0\) of the radial curvature numerator \(r^2+2(r')^2-r r''\). Define the chord length
\[
A_{K_\varepsilon}(\theta,t)=\mathcal H^1\bigl(K_\varepsilon\cap\{x:\langle x,u_\theta\rangle=t\}\bigr),\quad 0<t<1.
\]
For each fixed \(t\), the chord is nonempty for all directions and small \(\varepsilon\). The geometric derivative acts on smooth real perturbations; the displayed \(L^2\) inequalities refer to its unique bounded extension from smooth functions to all \(L^2(S^1)\). Fourier coefficients use \(\widehat f(m)=(2\pi)^{-1}\int_0^{2\pi}f(\theta)e^{-im\theta}\,d\theta\); the norm is the unnormalized arclength \(L^2\) norm. Statements concern first variations at the *unit disk*, not finite-amplitude nonlinear inversion.

## Proof

**1. First variation at a transverse chord.** Rotate a given normal to \(u_0=(1,0)\), set \(t=\cos\alpha\), and write the two endpoint polar angles as \(\phi_+(\varepsilon)\) and \(\phi_-(\varepsilon)\). They satisfy
\[
(1+\varepsilon f(\phi_\pm(\varepsilon)))\cos\phi_\pm(\varepsilon)=\cos\alpha,
\qquad \phi_\pm(0)=\pm\alpha.
\]
The implicit function theorem applies because \(\sin\alpha\ne0\), with derivatives
\[
\phi_+'(0)=f(\alpha)\cot\alpha,\qquad
\phi_-'(0)=-f(-\alpha)\cot\alpha.
\]
The signed tangential endpoint coordinates are \(y_\pm=(1+\varepsilon f(\phi_\pm))\sin\phi_\pm\), so \(y_+'(0)=f(\alpha)/\sin\alpha\) and \(y_-'(0)=-f(-\alpha)/\sin\alpha\). Differentiating \(y_+-y_-\) and rotating back gives the asserted expression for \(D_\alpha f\), uniformly in \(\theta\). Positivity of curvature guarantees these are the only two intersections.

**2. Spectral weights and exact reconstruction.** Translation by \(\pm\alpha\) has Fourier multiplier \(e^{\pm im\alpha}\). Consequently,
\[
\widehat{D_\alpha f}(m)=\lambda_m(\alpha)\widehat f(m),
\qquad\lambda_m(\alpha)=\frac{2\cos(m\alpha)}{\sin\alpha}.
\]
Parseval gives \(\sum_j\|D_{\alpha_j}f\|_2^2=2\pi\sum_m W_m|\widehat f(m)|^2\). Thus the greatest admissible squared lower frame bound is \(\inf_m W_m\); a positive bound yields the Fourier left inverse, for data \(g_j=D_{\alpha_j}f\),
\[
\widehat f(m)=\frac{\sum_j\lambda_m(\alpha_j)\widehat g_j(m)}{W_m(\boldsymbol\alpha)}.
\]
Its operator norm is at most \((\inf_mW_m)^{-1/2}\) as a map from the product data space to \(L^2\). If the infimum vanishes, trigonometric single-mode perturbations rule out every uniform positive lower bound.

**3. Arithmetic criterion for all finite families.** Work in the compact torus \(\mathbb T^k=(\mathbb R/\mathbb Z)^k\), and let \(H\) be the closure of the integer orbit of \(a=(\alpha_1/\pi,\ldots,\alpha_k/\pi)\). Since \(W_m\) is continuous as a function of \(ma\) modulo integers and its terms are nonnegative, \(\inf_mW_m=0\) exactly when \(b=(1/2,\ldots,1/2)\in H\). The character criterion for a closed cyclic subgroup of a torus (the usual Kronecker approximation theorem) says that \(b\in H\) exactly when every \(h\in\mathbb Z^k\) satisfying \(h\cdot a\in\mathbb Z\) also satisfies \(h\cdot b\in\mathbb Z\). Here \(h\cdot b=\tfrac12\sum_j h_j\). Negating this equivalence yields precisely the odd-sum integer-relation condition.

For completeness, the character criterion follows by averaging trigonometric polynomials over the Haar measure of \(H\): if \(b\notin H\), a continuous function separates the disjoint cosets \(H\) and \(b+H\); uniform trigonometric approximation and Haar averaging leave only the characters annihilating \(H\), so one such character must distinguish \(b\) from zero. Conversely, every annihilating character equals one throughout \(H\). This proves the criterion without assuming more than standard Fourier approximation and Haar measure on a compact torus.

**4. Exact rational kernels.** Suppose \(\alpha_j/\pi=p_j/q_j\) in lowest terms. A Fourier mode \(m\) vanishes for offset \(j\) exactly when \(2mp_j/q_j\) is odd. If \(q_j\) is odd this cannot hold. If \(q_j\) is even, \(p_j\) is odd and the zero modes are \(m=(q_j/2)(2\ell+1)\). Their simultaneous intersection is nonempty exactly when all \(q_j/2\) have the same \(2\)-adic valuation, equivalently all \(q_j\) do. In that case it is precisely the set of odd multiples of their least common multiple. Because the weights are periodic in \(m\) with period \(\operatorname{lcm}(q_j)\), having no exact zero implies a strictly positive minimum and conversely. With an irrational offset no integer mode can vanish for that offset, hence there is no common kernel. For a single rational angle with odd \(q\), the residues \(mp\bmod q\) traverse all classes, and the closest classes to half a period are at distance \(1/2\) from \(q/2\). This yields the stated sharp minimum \(4\sin^2(\pi/(2q))/\sin^2\alpha\). For a single irrational angle, irrational rotation is dense modulo \(\pi\), which makes its weight arbitrarily small without ever being zero.

**5. Sharp two-scale certificate.** Set \(s=\sin\alpha\), \(c=\cos\alpha\), and \(z=\cos^2(m\alpha)\). Since \(\cos^2(2m\alpha)=(2z-1)^2\) and \(\sin^2(2\alpha)=4s^2c^2\), direct expansion gives the exact identity
\[
W_m(\alpha,2\alpha)=
\frac{4z}{s^2}+\frac{(2z-1)^2}{s^2c^2}
=1+\frac{1}{s^2}+\frac{(2z-s^2)^2}{s^2c^2}.
\]
This proves the lower bound for every mode. The expression is convex in \(z\in[0,1]\), so its maximum occurs at an endpoint; the value at \(z=1\) exceeds that at \(z=0\), giving the stated upper coefficient, attained at \(m=0\). If \(\alpha/\pi\) is irrational, the set of angles \(m\alpha\bmod\pi\) is dense in \([0,\pi)\); hence \(z\) approaches \(s^2/2\) and the lower coefficient cannot be improved. The pair is uniformly stable for every \(\alpha\) also directly from the integer relation \(2\alpha-(2\alpha)=0\) with coefficient sum \(2-1=1\) odd.

**6. Sharp rational example.** At \((\alpha_1,\alpha_2)=(\pi/6,\pi/4)\), the weight is
\[
W_m=16\cos^2(m\pi/6)+8\cos^2(m\pi/4).
\]
It has period \(12\), with exact values for \(m=0,\ldots,11\):
\[
(24,16,4,4,12,16,16,16,12,4,4,16).
\]
Thus \(\min W_m=4\), \(\max W_m=24\), and each endpoint is attained by smooth single Fourier modes. The individual zero-mode sets are odd multiples of \(3\) and odd multiples of \(2\), so neither one-offset map is injective, but their kernels are disjoint.

## Verification

The standalone `check.py` reproduces the exact period-\(12\) spectral table with rational arithmetic, checks rational-kernel intersections for a finite grid, checks the two-scale algebraic certificate on rational samples, and compares the derived first variation with centered finite differences of actual radial-chord intersections for several smooth perturbations and offsets. The geometric and spectral conclusions above follow from the proof, not from a finite parameter sweep. Run `python3 check.py` using the Python standard library only. The expected message is `FINITE_CHORD_TOMOGRAPHY_CHECKS_OK`.

## Relationship to prior work

Fish, Ryabogin, Sun, and Yaskin (arXiv:2610.10229v1, first posted 7 October 2026) show in their Theorem 6.2 that an accumulating infinite family of section offsets determines arbitrary convex bodies. The present result concerns a different question: the exact finite-offset **first-order** stability threshold, its arithmetic classification, and an explicit sharp two-scale frame at the disk; it asserts no global nonlinear determination. The same source discusses the older Barker--Larman question of one offset.

Haddad and Ryabogin (arXiv:2605.00299v1) investigate rigidity of **four-dimensional** bodies of revolution from constant non-central three-dimensional sections, with arithmetic restrictions of a different kind. They recall Santaló's known uniqueness result when one compared planar body is a disk. That uniqueness result does not supply or contradict a bounded inverse for the derivative at the disk; a nonlinear injectivity theorem alone need not control the smallest linearized singular values.

Matthews (Canadian Mathematical Bulletin, published online 30 September 2026) proves nonlinear unique reconstruction for **polygons** from supporting-line chords of analytic hedgehogs, rather than first variations of smooth convex disks. Standard Fourier diagonalization and the Kronecker character criterion are used openly as prior mathematical tools. Their combination with chord geometry and the sharp two-scale bounds is the contribution assessed here. No uniqueness claim is based solely on failed literature searches.

## Limitations

The inequalities control only the linearized response at the unit disk and do not imply a local or global nonlinear Lipschitz inverse for finite perturbations. For irrational single offsets the derivative is injective but lacks an \(L^2\) lower bound; this does not constitute a counterexample to nonlinear uniqueness. For rational \(\alpha/\pi\), the universal two-scale lower coefficient need not be sharp; the optimal value is the minimum of finitely many explicitly computable spectral weights. The full text of the original 2001 Barker--Larman paper and of some older chord-function results was not available for definitive statement-by-statement comparison. Equivalent unindexed or textbook transform results remain possible, so originality retains residual literature risk.

## References

1. A. Fish, D. Ryabogin, W. R. Sun, V. Yaskin, *On determination of convex bodies by their section functions*, arXiv:2610.10229v1 (7 October 2026), especially Sections 1, 2, and 6. https://arxiv.org/html/2610.10229v1
2. J. Haddad, D. Ryabogin, *On convex bodies with constant non-central sections*, arXiv:2605.00299v1 (1 May 2026), especially Sections 1 and 2. https://arxiv.org/html/2605.00299v1
3. B. Matthews, *Hedgehog reconstruction of polygons: Non-central sections and slabs*, Canadian Mathematical Bulletin, published online 30 September 2026. https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/hedgehog-reconstruction-of-polygons-noncentral-sections-and-slabs/93C726B7D2528F586260A36266EB814B
4. J. A. Barker, D. G. Larman, *Determination of convex bodies by certain sets of sectional volumes*, Discrete Mathematics 241 (2001), 79–96, DOI:10.1016/S0012-365X(01)00111-X (metadata and secondary descriptions inspected; full original unavailable).
5. R. J. Gardner, *Geometric Tomography*, second edition, Cambridge University Press (2006), background reference (not inspected in full).
