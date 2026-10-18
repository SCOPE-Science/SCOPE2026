# Sharp constant in Steiner-centered planar Minkowski inversion

## Finding
Let \(\mathbb S^1=\{(\cos\theta,\sin\theta):\theta\in\mathbb R/(2\pi\mathbb Z)\}\), equipped with geodesic distance \(d_g\). A Borel probability measure \(\mu\) is *balanced* if \(\int_{\mathbb S^1}u\,d\mu(u)=0\), and *nondegenerate* if its support is not contained in a pair of antipodal points. Let \(K_\mu\) be the unique Steiner-centered planar convex body with surface-area measure \(S_{K_\mu}=2\pi\mu\), hence perimeter \(2\pi\). For geodesic Wasserstein distance \(W_1\), define
\[
C_*:=\sup_{\substack{\mu,\nu\text{ balanced, nondegenerate}\\\mu\ne\nu}}
\frac{d_H(K_\mu,K_\nu)}{W_1(\mu,\nu)}.
\]
Then \(\boxed{C_*=\pi}\). The supremum remains \(\pi\) even if both measures are required to have everywhere positive smooth densities with respect to angular arclength, and hence both reconstructed bodies are smooth and strictly convex. The upper bound \(C_*\le\pi\) is Proposition 6.1 of An [1]; the finding here is sharpness of the *coefficient*, using explicit balanced, nondegenerate measures. It is distinct from the already established sharpness of the Lipschitz *exponent*.

## Assumptions and scope
We use the geodesic transportation cost \(d_g(e^{i\theta},e^{i\phi})=\min_{k\in\mathbb Z}|\theta-\phi+2\pi k|\). Hausdorff distance is Euclidean, with bodies normalized by Steiner centering and perimeter \(2\pi\). Surface-area measure and its inverse are understood in the standard planar Aleksandrov--Minkowski sense; balanced nondegenerate measures correspond to convex bodies with interior. No assertion concerns different choices of center, other Wasserstein costs, dimensions above two, or attainment of the supremum.

## Proof
**1. Established universal upper bound and its normalization.** A support function \(h_\mu\) satisfies \(h_\mu''+h_\mu=2\pi\mu\) distributionally. Steiner centering fixes its first Fourier harmonics to zero. An [1, Section 6.1, equations (7)--(11)] gives the even periodic Green kernel
\[
G(t)=-\frac{\cos t}{4\pi}+\left(\frac12-\frac{|t|}{2\pi}\right)\sin|t|,\qquad -\pi\le t\le\pi,
\]
with \(\operatorname{Lip}_{d_g}G=1/2\). The balance condition annihilates its cosine correction, so
\[
h_\mu(\theta)-h_\nu(\theta)=2\pi\int_{\mathbb S^1}G(\theta-\phi)\,d(\mu-\nu)(\phi).
\]
Kantorovich--Rubinstein duality and the support-function characterization of Hausdorff distance yield
\[
d_H(K_\mu,K_\nu)\le2\pi\operatorname{Lip}_{d_g}(G)W_1(\mu,\nu)=\pi W_1(\mu,\nu).
\]
This step reproduces the cited result rather than claiming it as new.

**2. Balanced explicit triangle--rectangle measures.** Choose \(0<\varepsilon<\pi/2\) and put \(c=\cos\varepsilon\), \(s=1/(1+c)\). Angles of Dirac masses are interpreted modulo \(2\pi\). Set
\[
U_\varepsilon=\tfrac12(\delta_\varepsilon+\delta_{-\varepsilon}),\qquad
V_\varepsilon=c\delta_0+\tfrac{1-c}{2}(\delta_{\pi/2}+\delta_{-\pi/2}),
\]
\[
\mu_\varepsilon=sU_\varepsilon+(1-s)\delta_\pi,\qquad
\nu_\varepsilon=sV_\varepsilon+(1-s)\delta_\pi.
\]
Both measures have mass one, and their vector first moments equal \(s(c,0)-(1-s)(1,0)=0\), since \(1-s=sc\). The first has three noncollinear support directions; the second has four, and neither support lies in any antipodal pair. Thus their reconstructed bodies are genuine polygons (respectively a triangle and a rectangle with possibly unequal side lengths).

**3. A transport plan and a support-function lower bound.** For \(U_\varepsilon\to V_\varepsilon\), send \(c/2\) of the mass from each of \(\pm\varepsilon\) to zero, and send \((1-c)/2\) from \(+\varepsilon\) to \(+\pi/2\) and from \(-\varepsilon\) to \(-\pi/2\). Match the common mass at \(\pi\) to itself. All distances used are shortest-arc distances, giving the explicit admissible upper estimate
\[
W_1(\mu_\varepsilon,\nu_\varepsilon)\le sT_\varepsilon,\qquad
T_\varepsilon=c\varepsilon+(1-c)(\pi/2-\varepsilon).
\]
Notice that an *upper* estimate on transportation cost suffices for a *lower* estimate on the quotient. By the displayed Green convolution and its evenness,
\[
(h_{\mu_\varepsilon}-h_{\nu_\varepsilon})(0)
=2\pi s\{G(\varepsilon)-cG(0)-(1-c)G(\pi/2)\}.
\]
Substitution of \(G(0)=-1/(4\pi)\) and \(G(\pi/2)=1/4\) gives the exact positive-near-zero expression
\[
(h_{\mu_\varepsilon}-h_{\nu_\varepsilon})(0)=2\pi s E_\varepsilon,\quad
E_\varepsilon=\left(\frac12-\frac{\varepsilon}{2\pi}\right)\sin\varepsilon-\frac{1-\cos\varepsilon}{4}.
\]
Since \(\sin\varepsilon/\varepsilon\to1\) and \((1-\cos\varepsilon)/\varepsilon\to0\), one has \(E_\varepsilon/\varepsilon\to1/2\). Similarly \(T_\varepsilon/\varepsilon\to1\), and \(E_\varepsilon>0\) for sufficiently small \(\varepsilon\). Consequently
\[
\frac{d_H(K_{\mu_\varepsilon},K_{\nu_\varepsilon})}{W_1(\mu_\varepsilon,\nu_\varepsilon)}
\ge\frac{2\pi E_\varepsilon}{T_\varepsilon}\longrightarrow\pi.
\]
Combining with Step 1 proves \(C_*=\pi\). The limiting measures become degenerate, but *every member of the approximating family* is admissible. No equality at a positive \(\varepsilon\) is asserted.

**4. Smooth strict-convexity restriction.** Fix \(\varepsilon>0\) and convolve both measures on the circle with the normalized strictly positive periodic heat kernel \(H_t\), \(t>0\). Rotational convolution preserves probability and sends the first complex Fourier coefficient to \(e^{-t}\) times itself, so balance persists exactly. The resulting measures \(\mu_{\varepsilon,t},\nu_{\varepsilon,t}\) have strictly positive smooth densities; the Minkowski equation \(h''+h=2\pi\,d\mu/d\theta\) then gives smooth strictly convex boundaries. On the compact circle, weak convergence as \(t\downarrow0\) implies \(W_1(\mu_{\varepsilon,t},\nu_{\varepsilon,t})\to W_1(\mu_\varepsilon,\nu_\varepsilon)>0\). The Green convolution converges uniformly in \(\theta\), hence so does the Hausdorff distance of the reconstructed bodies. Their quotients therefore converge to the polygonal quotient. Taking \(t\downarrow0\) first, then \(\varepsilon\downarrow0\), gives the same optimal coefficient among smooth strictly convex bodies.

## Verification
The standalone program `check.py` checks the exact mass and balance bookkeeping algebraically by numerical evaluation, the explicit coupling's nonnegative marginals and cost, the Green-kernel support difference, and convergence of the certified quotient lower bound toward \(\pi\). It needs only Python 3's standard library and can be run with `python3 check.py` after extracting the embedded files. The proof of the universal sharp constant is analytic, not an inference from finite numerical samples or the program. The decisive limits are \(E_\varepsilon/\varepsilon\to1/2\) and \(T_\varepsilon/\varepsilon\to1\); the positive heat regularization proves the smooth restriction.

## Relationship to prior work
An [1, Proposition 6.1] proves the inequality with coefficient \(\pi\). Its discussion immediately after Proposition 6.3 explicitly leaves the *optimal coefficient* undetermined; Proposition 6.3 proves only that a Lipschitz exponent larger than one is impossible. Thus the upper estimate alone does not settle this new best-constant determination. The quantitative Minkowski stability results of Böröczky--Machado--Ramos [2] concern a dual-convex discrepancy and an optimized translation under dispersion assumptions, rather than the exact geodesic \(W_1\)-to-Steiner-centered-Hausdorff constant. Abdallah--Mérigot [3] study reconstruction from random normal measurements and different stability estimates. Marckert--Renault [4] treat the probabilistic Gauss--Minkowski correspondence and transport-like comparisons, but the inspected statements do not specify this sharp coefficient. The novelty claim is restricted to the displayed exact sharpness and explicit family.

## Limitations
The extremizing sequence degenerates as \(\varepsilon\downarrow0\); the proof does not provide a pair attaining equality, characterize all extremizing sequences, or establish a best coefficient when uniform positive curvature bounds, a fixed diameter lower bound, or a distance from degenerate measures is imposed. Only the geodesic \(W_1\), perimeter-\(2\pi\), Steiner-centered planar normalization is covered. An overlooked equivalent result in other formulations of the Minkowski inverse problem remains possible.

## References
[1] C. An, *Gauss--Chebyshev Quadrature, S1-Designs, and the Planar Minkowski Inverse Problem: A One-Dimensional Model for Design-Induced Convex Geometry*, arXiv:2610.11814v1 (first posted 8 October 2026), Sections 4 and 6, especially Proposition 6.1 and the paragraph after Proposition 6.3. https://arxiv.org/abs/2610.11814

[2] K. Böröczky, J. M. Machado, and J. P. G. Ramos, *Quantitative Stability for Minkowski's Problem*, arXiv:2603.17726v3. https://arxiv.org/abs/2603.17726

[3] H. Abdallah and Q. Mérigot, *On reconstruction from random normal measurements*, arXiv:1402.5010v1. https://arxiv.org/abs/1402.5010

[4] J.-F. Marckert and D. Renault, *Compact convex sets of the plane and probability theory*, ESAIM: Probability and Statistics (2014), doi:10.1051/ps/2014008. https://doi.org/10.1051/ps/2014008
