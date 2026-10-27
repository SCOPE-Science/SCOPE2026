# An unavoidable exterior square-root singularity of critical-cusp invariant densities

## Finding
For every real \(1<\vartheta<2\), put \(K=(1-\vartheta/2)/\sqrt2\) and consider the symmetric full-branch map
\[
f_{\vartheta}(1/2\pm t)=1-\vartheta t-2K\sqrt t,\qquad 0\le t\le1/2.
\]
Let \(h_{\vartheta}\) denote its unique Lebesgue-normalized absolutely continuous invariant probability density. Define
\[
x_*=1+K^2/\vartheta,\qquad v=K^2/\vartheta^2.
\]
Then \(h_{\vartheta}\) is the restriction of a holomorphic function on an open complex neighborhood of \([0,1]\), strictly positive on \((0,1)\), and its analytic germ at \(1\) has a unique real-axis continuation \(\widetilde h\) along \(1<x<x_*\) satisfying
\[
\boxed{\lim_{x\uparrow x_*}\sqrt{x_*-x}\,\widetilde h(x)
=-\frac{K}{\vartheta^{3/2}}\left[h_{\vartheta}(1/2-v)+h_{\vartheta}(1/2+v)\right]<0.}
\]
Thus \(x_*\) is a genuine exterior inverse-square-root singularity, located at the exact distance
\[
\boxed{x_*-1=\frac{(2-\vartheta)^2}{8\vartheta}}
\]
from the physical interval. No \(h_{\vartheta}\) in this parameter range agrees almost everywhere with a rational function. The Taylor series of its germ at \(x=1\) has radius at most \((2-\vartheta)^2/(8\vartheta)\). This is an upper bound, not an assertion that no closer nonreal singularities exist.

## Assumptions and scope
All assertions hold for every \(\vartheta\in(1,2)\), not for the endpoint \(\vartheta=2\). Holomorphy refers to the spatial variable, not analyticity with respect to a perturbation parameter. The map is nonsmooth at its apex \(1/2\), but its two inverse branches are holomorphic near the whole closed target interval. The density is normalized by \(\int_0^1 h_{\vartheta}(x)\,dx=1\). Existence, uniqueness, \(W^{2,1}\) regularity, peripheral spectral simplicity and convergence of its transfer iterates are established in the cited 2026 critical-cusp paper. Those facts are inputs, not newly proved here.

## Proof
**1. Exact inverse branches.** Write \(c=1/2\) and \(s(z)=\sqrt{K^2+\vartheta(1-z)}\), taking the positive branch for real \(z\in[0,1]\). Put \(u(z)=(s(z)-K)/\vartheta\) and \(g_{\pm}(z)=c\pm u(z)^2\). For real \(z\in[0,1]\), one has \(0\le u\le1/\sqrt2\),
\[
\vartheta u^2+2Ku=1-z,\qquad
\left|g_\pm'(z)\right|=\frac{u(z)}{K+\vartheta u(z)}=:w(z).
\]
Consequently the Perron--Frobenius operator is
\[
(\mathcal L\phi)(z)=w(z)\big[\phi(g_-(z))+\phi(g_+(z))\big],\qquad z\in[0,1]. \tag{1}
\]
Here \(g_-\) increases, \(g_+\) decreases, and the analytic transfer weights are respectively \(g_-'=w\) and \(-g_+'=w\). The real derivative bound is \(\sup_{[0,1]}|g_\pm'|=1/(1+\vartheta/2)<1\).

**2. Analyticity of the invariant density.** Since the radical branch point \(x_*=1+K^2/\vartheta\) lies strictly to the right of \(1\), the functions \(g_\pm\) and \(w\) are holomorphic near \(I=[0,1]\). By the strict derivative bound and compactness, there are \(\delta>0\) and \(q<1\) such that both inverse branches are holomorphic on the complex tube \(U_\delta=\{z:\operatorname{dist}(z,I)<\delta\}\), their derivatives have modulus at most \(q\) there, and \(g_\pm(U_\delta)\subset U_{q\delta}\). The last inclusion follows by projecting onto the convex interval \(I\) and integrating derivatives along segments. Since \(\overline{U_{q\delta}}\subset U_\delta\), (1) defines a compact weighted-composition operator \(\mathcal L_H\) on \(H^\infty(U_\delta)\) (Montel compactness of restriction to the two relatively compact images).

Restriction from \(H^\infty(U_\delta)\) to \(W^{2,1}(I)\) is continuous by Cauchy estimates; it intertwines \(\mathcal L_H\) with the Sobolev transfer operator \(\mathcal L_W\). The primary source proves \(\mathcal L_W^n1\to h_{\vartheta}\ne0\) in \(W^{2,1}\), with spectral radius one and no peripheral spectrum other than its algebraically simple eigenvalue \(1\). If the compact operator \(\mathcal L_H\) had spectral radius greater than one, its nonzero peripheral eigenvalue would produce an impossible \(W^{2,1}\) eigenvalue. If its spectral radius were less than one, \(\mathcal L_H^n1\to0\) and hence \(\mathcal L_W^n1\to0\), another contradiction. Thus its spectral radius is one and compactness supplies a unit-modulus eigenvector; intertwining and peripheral simplicity force eigenvalue \(1\), with restriction proportional to \(h_{\vartheta}\). This proves holomorphic extension of the normalized density.

**3. Strict positivity.** The continuous \(W^{2,1}\) density is nonnegative and has integral one, so on some nonempty interior interval \(J\) it is bounded below by a positive number. The inverse branches contract uniformly and produce a full-branch cylinder \(J_\omega\subset J\) of sufficiently large rank. For every \(x\in(0,1)\), the pointwise identity \(h_{\vartheta}(x)=\mathcal L^n h_{\vartheta}(x)\) contains the strictly positive contribution from \(J_\omega\), since its inverse Jacobian is positive at such \(x\). Therefore \(h_{\vartheta}(x)>0\) for every interior point.

**4. Forced exterior branch point.** Formula (1), with the holomorphic density from step 2, gives analytic continuation near \(1\) and along the real interval \(1<x<x_*\). Indeed \(s(x)>0\), \(u(x)<0\), and \(0<u(x)^2<v<1/2\) there, so the required function values \(h_{\vartheta}(c\pm u(x)^2)\) always lie at interior points where the holomorphic germ is defined. As \(x\uparrow x_*\), \(s(x)=\sqrt\vartheta\sqrt{x_*-x}\), \(u(x)\to-K/\vartheta\), and \(w(x)=u(x)/s(x)\). Substituting into (1) gives the claimed finite, nonzero negative limit. Step 3 makes the parenthesized coefficient strictly positive. An analytic or meromorphic function at \(x_*\) has an integer-order Laurent expansion, incompatible with this half-order divergence. In particular a rational function cannot equal the invariant density on \(I\) by analytic identity continuation, and a Taylor disk about \(1\) of radius larger than \(x_*-1\) is impossible. Finally, \(K^2/\vartheta=(2-\vartheta)^2/(8\vartheta)\), as asserted.

## Verification
An accompanying standard-library checker reconstructs the defining inverse-branch identities, the exact real inverse derivative bound, and the singular coefficient by high-precision evaluations for rational parameters \(\vartheta=5/4,3/2,7/4\). The checker tests algebraic consequences; it does not purport to certify the infinite-dimensional compact-operator or positivity arguments, which are given above. At \(\vartheta=3/2\) the exterior singularity is exactly \(x_*=49/48\), and the two interior sample locations in its coefficient are \(35/72\) and \(37/72\).

## Relationship to prior work
Oltiboev--Vafoyev, arXiv:2610.23180v1 (16 October 2026), Section 3, provides the precise map, inverse branches and transfer formula; Section 4 proves unique \(W^{2,1}\) invariant density and spectral gap; Section 5 studies a distinct derivative-trace issue at an interior cusp image; Section 6 proves analyticity in a **probability-law parameter**, not holomorphy in space or a forced exterior singularity. The earlier Oltiboev paper arXiv:2505.17462v1 treats Sobolev linear response for cusp maps. Oltiboev--Rakhimov--Ruziboev arXiv:2608.26969v1 treats random cusp maps with exponent strictly below \(-1/2\), hence not the present endpoint; only its accessible abstract was inspected in this comparison. Standard compact holomorphic transfer-operator theory supplies a technique, but does not alone identify this explicit nonremovable exterior branch point or rule out rational densities for this family. No claim is made that real analyticity itself is new as a general principle.

## Limitations
The singularity is proved along the positive real direction from \(1\) to \(x_*\); there may be closer nonreal singularities, and no assertion of an exact Taylor radius is made. The leading coefficient is expressed through two positive, uniquely determined interior density values, not evaluated in elementary closed form. The result does not establish analyticity of the density as \(\vartheta\to2\), where the forcing coefficient vanishes and the singularity disappears. Historical-priority comparisons cannot exclude an equivalent fact hidden in older transfer-operator calculations under different terminology.

## References
- D. Oltiboev and F. Vafoyev, *Critical cusp cancellation and analytic response for a Bernoulli random interval map*, arXiv:2610.23180v1 (16 October 2026), Sections 3--6, https://arxiv.org/pdf/2610.23180.
- D. Oltiboev, *Linear response for systems with a cusp*, arXiv:2505.17462v1 (23 May 2025), https://arxiv.org/pdf/2505.17462.
- D. Oltiboev, K. Rakhimov and M. Ruziboev, *Linear response for random systems with a cusp*, arXiv:2608.26969v1 (27 August 2026), https://arxiv.org/abs/2608.26969 (abstract compared; full text not accessible in this investigation).
- D. Ruelle, standard complex-analytic transfer-operator framework for expanding maps (methodological background; the exact singularity is proved directly above).
