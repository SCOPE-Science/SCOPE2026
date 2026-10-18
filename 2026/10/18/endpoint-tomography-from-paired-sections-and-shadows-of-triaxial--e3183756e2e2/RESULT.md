# Endpoint tomography from paired sections and shadows of triaxial ellipsoids

## Finding
Let \(E\subset\mathbb R^3\) be a centered ellipsoid with three distinct squared semiaxes \(0<a<b<c\), and let \(U\) be uniformly distributed on the unit sphere. For the **same** normal \(U\), let \(S(U)\) be the area of the central planar section \(E\cap U^\perp\), and let \(P(U)\) be the area of the orthogonal planar projection of \(E\) onto \(U^\perp\). Define the dimensionless observable
\[
Z(U)=\left(\frac{P(U)}{S(U)}\right)^2,
\quad K=\operatorname{ess\,sup}Z,
\quad \gamma=\lim_{\varepsilon\downarrow0}\frac{\Pr\{Z\ge K-\varepsilon\}}{\varepsilon}.
\]
The limit exists, is finite and strictly positive, and has the **exact** value
\[
K=\frac{(a+c)^2}{4ac},\qquad
\gamma=\sqrt{\frac{2a^2bc^2}{(b-a)(c-a)^2(a+c)(c-b)}}.
\]
These **two scalar distributional statistics** recover the unordered shape of \(E\) up to scaling and polar duality. Explicitly, put
\[
k=2K-1+2\sqrt{K(K-1)},\quad
B=\frac{(k-1)^2}{k},\quad
H=k+1-\frac{2k}{(k+1)B\gamma^2}.
\]
The possible normalized squared semiaxis triples are **exactly** \((1,t,k)\), where
\[
t=\frac{H\pm\sqrt{H^2-4k}}2.
\]
The two roots are reciprocal about \(\sqrt{k}\), namely \(t\) and \(k/t\); they coincide if and only if \(b^2=ac\). The ambiguity is unavoidable: polar duality (followed by a similarity and coordinate permutation) leaves the complete law of \(Z\) unchanged, not just \(K\) and \(\gamma\).

For example, squared semiaxes \((1,2,3)\) give \(K=4/3\) and \(\gamma=3/2\); the only alternatives with these observations are the shapes \((1,2,3)\) and \((1,3/2,3)\), up to common scaling, rotation and reflections.

## Assumptions and scope
The ellipsoid is \(E=\{x\in\mathbb R^3:x^{\mathsf T}Q^{-1}x\le1\}\), where \(Q\) is real symmetric positive definite and its ordered eigenvalues are \(0<a<b<c\). All areas are ordinary two-dimensional Euclidean areas. The central plane and projection plane are identical and perpendicular to the same Euclidean-Haar normal \(U\); normals are neither weighted by section area nor selected after affine normalization. Shape means the eigenvalue triple of \(Q\) up to overall positive scaling and permutation. Polarity takes \(Q\) to \(Q^{-1}\), so in normalized ordered eigenvalues it takes \((1,t,k)\) to \((1,k/t,k)\). No claim is made for equal-axis ellipsoids or general convex bodies.

## Proof
**1. Exact paired-observation identity.** Diagonalize \(Q=\operatorname{diag}(a,b,c)\). A linear change of variables from the Euclidean unit ball gives
\[
S(u)=\frac{\pi\sqrt{abc}}{\sqrt{a u_1^2+b u_2^2+c u_3^2}},\qquad
P(u)=\pi\sqrt{abc}\sqrt{\frac{u_1^2}a+\frac{u_2^2}b+\frac{u_3^2}c}.
\]
For the projection formula, use the determinant of the restricted quadratic form on \(u^\perp\), or the codimension-one cofactor identity. Thus, writing \(w_i=u_i^2\),
\[
Z(u)=\left(\sum_i\lambda_iw_i\right)
\left(\sum_i\lambda_i^{-1}w_i\right)
=1+A w_1w_2+B w_1w_3+C w_2w_3,
\]
where
\[
A=\frac{(b-a)^2}{ab},\quad
B=\frac{(c-a)^2}{ac},\quad
C=\frac{(c-b)^2}{bc}.
\]
The pairwise expansion uses \(\sum_iw_i=1\); the coefficients are nonnegative.

**2. All maximizers and their nondegenerate quadratic deficit.** Since every eigenvalue \(\lambda\in[a,c]\) satisfies \(\lambda+ac/\lambda\le a+c\), the arithmetic-geometric mean inequality gives
\[
4ac\,Z(u)\le\left(\sum_i(\lambda_i+ac/\lambda_i)w_i\right)^2\le(a+c)^2.
\]
Because \(a<b<c\), equality holds exactly at the four sphere directions with \(u_2=0\) and \(|u_1|=|u_3|=1/\sqrt2\). Thus \(K=(a+c)^2/(4ac)=1+B/4\). Near any such direction choose the smooth spherical coordinates
\[
u_2=y,\quad (u_1,u_3)=\sqrt{1-y^2}(\cos\theta,\sin\theta),
\]
and write \(s=\theta-\theta_*\) for the corresponding maximizing angle \(\theta_*\). Direct expansion of the exact pairwise formula yields
\[
K-Z(u)=B s^2+D y^2+O\big((|s|+|y|)^3\big),
\quad D=\frac{B-A-C}{2}
=\frac{(b-a)(a+c)(c-b)}{2abc}>0.
\]
This is a positive-definite quadratic form, so no additional near-maximizing directions occur outside disjoint neighborhoods of these four points.

**3. Sharp upper-tail coefficient.** In the coordinates above, spherical area measure is exactly \(d\theta\,dy\), so Haar probability measure is \(d\theta\,dy/(4\pi)\). At each maximizer, rescale \((s,y)=\sqrt{\varepsilon}(v,z)\). The event \(Z\ge K-\varepsilon\) converges after this rescaling to the ellipse \(Bv^2+Dz^2\le1\), whose area is \(\pi/\sqrt{BD}\). A uniform local quadratic lower bound justifies dominated convergence. Summing the four disjoint neighborhoods gives
\[
\Pr\{Z\ge K-\varepsilon\}
=\frac{\varepsilon}{\sqrt{BD}}+o(\varepsilon),
\qquad \gamma=\frac1{\sqrt{BD}}
=\sqrt{\frac2{B(B-A-C)}}.
\]
Substitution of the definitions of \(B,D\) gives the displayed formula in \(a,b,c\).

**4. Exact inverse and polarity obstruction.** Normalize \(a=1\), \(b=t\), \(c=k\), with \(1<t<k\). The support endpoint equation \(4K=k+2+k^{-1}\) gives the unique \(k>1\) shown above. Moreover
\[
B-A-C=\frac{(t-1)(k+1)(k-t)}{kt}
=\frac{k+1}{k}\left(k+1-t-\frac{k}{t}\right).
\]
The measured tail slope determines \(B-A-C=2/(B\gamma^2)\), hence \(t+k/t=H\). Therefore \(t\) is exactly one of the two positive roots of \(t^2-Ht+k=0\), both lying in \((1,k)\). These roots are \(t\) and \(k/t\); they coincide precisely when \(t=\sqrt{k}\), equivalently \(b^2=ac\).

Finally, for any positive definite \(Q\) and every direction \(u\),
\[
(u^{\mathsf T}Q u)(u^{\mathsf T}Q^{-1}u)
=(u^{\mathsf T}Q^{-1}u)(u^{\mathsf T}Q u).
\]
Thus replacing \(Q\) by a scalar multiple of \(Q^{-1}\) leaves \(Z(u)\) unchanged pointwise, and reordering axes merely rotates the Haar direction. No statistic derived solely from \(Z\) can distinguish the two polar shapes. Conversely the reconstruction proves that these are the only ambiguities among strictly triaxial ellipsoids.

## Verification
The standalone file `checker.py` requires Python 3, NumPy and SciPy. Execute `python checker.py`. It performs exact rational tests of the pairwise identity, factorization of \(B-A-C\), and the quadratic reconstruction; checks the polarity invariance and global spectral bound; and independently integrates the true spherical upper-tail probability using a conditional arcsine law. Tested squared-axis triples \((1,2,3)\), \((2,3,7)\), \((1,4,25)\) yield numerical tail-to-asymptotic ratios approaching one as the deficit decreases. Numerical integration is a diagnostic check only; the proof above establishes the limit for all strictly triaxial ellipsoids.

## Relationship to prior work
Fish, Ryabogin, Sun and Yaskin (2026) study determination from parallel section functions. Kim, Yaskin and Zvavitch (2015 preprint; 2017 journal) introduce and investigate **separate marginal** section and projection distributions and volume comparison questions. Their inspected statements do not analyze the **same-direction quotient** or recover a triaxial shape from its two upper-tail statistics. Hillier (1999 preprint, 2001 journal) develops densities of a single random spherical quadratic form, rather than the product of a quadratic form and its inverse. The established Kantorovich inequality supplies the maximum \(K\), but supplies neither the upper-tail slope \(\gamma\) nor the reconstruction from \((K,\gamma)\). A separate published result reconstructs ellipsoid axes from the first three reciprocal-square section moments; it uses different measurements and does not imply recovery from this quotient's endpoint data. These are mathematical distinctions, not claims of exhaustive historical priority.

## Limitations
This is an exact population-law theorem, not a finite-sample estimator or a uniform statistical error bound. It requires three **distinct** axis lengths; the tail geometry degenerates as two eigenvalues coalesce, so limits are not uniform there. The complete law cannot distinguish polar-dual ellipsoids, and the theorem does not claim determination of orientation. A general joint quadratic-form density or an older unlocated treatment of the Kantorovich quotient might offer an alternative derivation; the priority comparison is limited to the explicitly identified literature. No claim is made for nonellipsoidal convex bodies or higher-dimensional shapes.

## References
1. A. Fish, D. Ryabogin, W. R. Sun and V. Yaskin, *On determination of convex bodies by their section functions*, arXiv:2610.10229, first public 7 October 2026. https://arxiv.org/abs/2610.10229
2. J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289, first posted December 2015; *Journal of the London Mathematical Society* 95 (2017), 52–72. https://arxiv.org/abs/1512.07289
3. G. Hillier, *The density of a quadratic form in a vector uniformly distributed on the n-sphere*, discussion paper 9902 (1999); *Econometric Theory* 17 (2001), 1–28. https://doi.org/10.1017/S026646660117101X
4. *Sharp finite-moment reconstruction of ellipsoid axes from unoriented central sections*, published-finding corpus published mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-finite-moment-reconstruction-of-ellipsoid-axes-from-unorie--dce61c5feeed
5. *Exact random-radius law for one-spike ellipsoids in every codimension*, published-finding corpus published mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-random-radius-law-for-one-spike-ellipsoids-in-every-codime--e99f37d3b7ae
