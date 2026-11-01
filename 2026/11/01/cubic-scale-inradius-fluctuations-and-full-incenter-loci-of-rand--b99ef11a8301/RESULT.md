# Cubic-scale inradius fluctuations and full incenter loci of random central cube sections

## Finding
Let \(n\ge2\), let \(Q_n=[-1,1]^n\), and let \(H_u=u^\perp\) for a Euclidean unit vector \(u\in S^{n-1}\). Write \(\rho_n(u)\) for the radius of a **largest inscribed Euclidean ball in the intrinsic section** \(Q_n\cap H_u\), with its center permitted to vary inside \(H_u\). Then, for **every** \(u\),
\[
\boxed{\rho_n(u)=\left(1-\min_{1\le i\le n}u_i^2\right)^{-1/2}.}
\]
Every center of a maximum inscribed ball is given by the exact system
\[
\boxed{\mathcal I_n(u)=\left\{z\in u^\perp:\ |z_i|\le1-\rho_n(u)\sqrt{1-u_i^2}\ \text{for each }i\right\}.}
\]
If every coordinate of \(u\) is nonzero and the smallest absolute coordinate is unique, this incenter set has **affine dimension exactly \(n-2\)**. In particular, a generic central section of a cube of dimension at least three has infinitely many centers of maximum inscribed balls, despite having a uniquely determined optimal radius.

Now let \(U_n\) be Haar-uniform on \(S^{n-1}\), and put \(R_n=\rho_n(U_n)\). Its full support is \([1,b_n]\), where \(b_n=\sqrt{n/(n-1)}\). Its **exact finite-dimensional survival law** is, for \(1\le r\le b_n\), with \(a=1-r^{-2}\) and \(s=1-na\),
\[
\boxed{\mathbb P(R_n\ge r)=\frac{\Gamma(n/2)}{\pi^{n/2}}s^{n-1}
\int_{\substack{y_i\ge0\\\sum_{i=1}^n y_i=1}}
\prod_{i=1}^n(a+s y_i)^{-1/2}\,dy_1\cdots dy_{n-1}.}
\]
The simplex integral uses \(y_n=1-\sum_{i<n}y_i\). The law is atomless. In dimension two it reduces to the elementary expression
\[
\mathbb P(R_2\le r)=1-\frac2\pi\arcsin(2/r^2-1),\qquad 1\le r\le\sqrt2.
\]

There are explicit **sharp endpoint signatures**. As \(\varepsilon\downarrow0\),
\[
\boxed{\mathbb P(R_n\le1+\varepsilon)
=\frac{2\sqrt2\,n\Gamma(n/2)}{\sqrt\pi\,\Gamma((n-1)/2)}\sqrt\varepsilon+O_n(\varepsilon).}
\]
At the other endpoint, as \(r\uparrow b_n\),
\[
\boxed{\mathbb P(R_n\ge r)\sim
\frac{\Gamma(n/2)n^{n/2}}{\pi^{n/2}(n-1)!}
\left(\frac{2n}{b_n^3}\right)^{n-1}(b_n-r)^{n-1}.}
\]
Finally, the inradius excess has a **cubic rather than linear or quadratic dimensional scale**:
\[
\boxed{n^3(R_n-1)\Longrightarrow \frac\pi4 E^2,\qquad E\sim\operatorname{Exp}(1),}
\]
so the limiting distribution has CDF \(1-\exp(-2\sqrt{t/\pi})\) for \(t\ge0\). More strongly, for every fixed real \(p>0\),
\[
\boxed{\lim_{n\to\infty}\mathbb E\big[n^3(R_n-1)\big]^p
=\left(\frac\pi4\right)^p\Gamma(2p+1).}
\]
In particular, \(\mathbb E(R_n-1)\sim\pi/(2n^3)\).

## Assumptions and scope
All balls, diameters, and distances are Euclidean **within the intrinsic hyperplane metric**. The central section is by a codimension-one linear hyperplane, not an arbitrary affine translate. The Haar direction is unoriented; replacing \(u\) by \(-u\) changes nothing. The cube has side length two. A statement about the largest **inscribed** ball is distinct from the smallest enclosing-ball radius (sometimes called the random radius) of the same section. The infinite-dimensional assertion takes \(n\to\infty\) with hyperplane codimension fixed at one. At nongeneric normals the displayed formula for \(\mathcal I_n(u)\) remains exact, although its affine dimension may be smaller.

## Proof
**1. Ball containment and exact deterministic radius.** Let \(P_u=I-uu^{\mathsf T}\) be orthogonal projection onto \(H_u\). For every \(z\in H_u\), \(t\ge0\), the closed intrinsic ball \(z+t(B_2^n\cap H_u)\) lies in \(Q_n\) exactly when, for all \(i\),
\[
\sup_{\substack{h\in H_u\\\|h\|_2\le1}}|z_i+t h_i|
=|z_i|+t\|P_u e_i\|_2
=|z_i|+t\sqrt{1-u_i^2}\le1.
\]
The equality is attained in the projected coordinate direction (when nonzero). Since \(Q_n\cap H_u\) is centrally symmetric, if a radius-\(t\) ball centered at \(z\) fits, so does its reflection centered at \(-z\), and averaging their points shows the radius-\(t\) ball centered at zero also fits. Thus the optimal radius is the minimum over \(i\) of \(1/\sqrt{1-u_i^2}\), which is \(\big(1-\min_i u_i^2\big)^{-1/2}\). The same containment test at that radius proves the full incenter formula. This can alternatively be read from polarity: the polar inside \(H_u\) of \(Q_n\cap H_u\) is the orthogonal projection of the cross-polytope \(\operatorname{conv}\{\pm e_i\}\), whose maximum vertex norm is \(\max_i\sqrt{1-u_i^2}\).

**2. The dimension of the complete incenter set.** Suppose \(u_i\ne0\) for all \(i\), and that \(i_*\) uniquely minimizes \(|u_i|\). At \(t=\rho_n(u)\), the \(i_*\)-th center constraint is \(|z_{i_*}|\le0\), whereas each of the other \(n-1\) coordinate bounds is strictly positive. Thus the affine hull of \(\mathcal I_n(u)\) is
\[
\{z\in\mathbb R^n:z_{i_*}=0,\ \langle u,z\rangle=0\}.
\]
Because at least one other coordinate of \(u\) is nonzero, these are independent equations; their solution space has dimension \(n-2\). The zero center strictly satisfies every other coordinate constraint, so it lies in the relative interior of an \((n-2)\)-dimensional incenter polytope. Haar random normals satisfy these genericity assumptions with probability one.

**3. Exact distribution and support.** Let \(G_1,\dots,G_n\) be independent standard Gaussian variables. The normalized vector \(G/\|G\|_2\) has Haar law; the vector of squared coordinates \(X_i=G_i^2/\sum_jG_j^2\) has the Dirichlet distribution with \(n\) parameters equal to \(1/2\). Its density on \(x_i>0\), \(\sum x_i=1\), is
\[
\frac{\Gamma(n/2)}{\pi^{n/2}}\prod_{i=1}^n x_i^{-1/2}.
\]
The event \(R_n\ge r\) is exactly \(X_i\ge a=1-r^{-2}\) for every coordinate. With the change \(x_i=a+(1-na)y_i\), the Jacobian in the first \(n-1\) coordinates is \(s^{n-1}\); this proves the displayed integral. The simplex density is strictly positive in its relative interior, hence the law is atomless and has the claimed full support. For \(n=2\), write \(U_2=(\cos\theta,\sin\theta)\), with \(\theta\) uniform; then \(\min U_{2,i}^2=(1-|\cos 2\theta|)/2\). As \(|\cos 2\theta|\) has the arcsine law, the stated elementary CDF follows.

**4. Both endpoint constants.** Let \(m=\min_i|U_{n,i}|\). The density of a single absolute coordinate at zero is
\[
\frac{2\Gamma(n/2)}{\sqrt\pi\Gamma((n-1)/2)}.
\]
For small \(t\), the probability \(m\le t\) is \(n\) times the probability \(|U_{n,1}|\le t\), up to \(O_n(t^2)\): for \(n\ge3\) this follows by bounding the joint two-coordinate density near \((0,0)\); for \(n=2\) two coordinate bands are disjoint when \(t<1/\sqrt2\). Since \(m=\sqrt{1-R_n^{-2}}\), at \(R_n=1+\varepsilon\) the corresponding cutoff is \(t=\sqrt{2\varepsilon}+O(\varepsilon^{3/2})\). This proves the lower-endpoint expansion.

For the upper endpoint set \(s=1-na\downarrow0\) in the exact integral. Uniformly over the fixed simplex, \((a+s y_i)^{-1/2}\to\sqrt n\); its integral tends to \(n^{n/2}/(n-1)!\). Since \(s=1-n+n/r^2\sim(2n/b_n^3)(b_n-r)\), multiplication gives the displayed sharp \((n-1)\)-power asymptotic.

**5. Cubic-scale limit and all moments.** Write \(h_n=\min_i|G_i|\), \(S_n=\sum_iG_i^2\), and \(c=\sqrt{2/\pi}\). For each \(x\ge0\), because \(\mathbb P(|G_1|\le t)=ct+O(t^3)\),
\[
\mathbb P(nh_n>x)=(1-\mathbb P(|G_1|\le x/n))^n\longrightarrow e^{-cx}.
\]
Also \(S_n/n\to1\) in probability. Consequently \(n^{3/2}m=nh_n/\sqrt{S_n/n}\) converges to \(E/c\), where \(E\) is unit-rate exponential. The elementary expansion \((1-z^2)^{-1/2}-1=z^2/2+O(z^4)\) now proves the distributional limit \((\pi/4)E^2\).

For moment convergence, put \(Z_n=n^{3/2}m\). Since \(m\le1/\sqrt n\), always \(Z_n\le n\). For \(0\le x\le n\), on \(\{S_n\ge n/2\}\), the event \(Z_n>x\) forces \(h_n>x/(\sqrt2 n)\). A Gaussian Chernoff bound gives \(\mathbb P(S_n<n/2)\le e^{-n/16}\). The half-normal survival function satisfies \(\mathbb P(|G_1|>t)\le e^{-0.45t}\) for all \(t\ge0\) (for \(t\le1\) integrate its density; for \(t\ge1\) use its Gaussian tail bound). Therefore
\[
\mathbb P(Z_n>x)\le e^{-n/16}+e^{-0.45x/\sqrt2}\le2e^{-x/16},\quad 0\le x\le n,
\]
and the probability is zero for \(x>n\). All positive moments of \(Z_n\) are uniformly bounded. Moreover, \(n^3(R_n-1)\le Z_n^2\), using \(m^2\le1/2\) and the exact identity
\[
(1-m^2)^{-1/2}-1=\frac{m^2}{\sqrt{1-m^2}(1+\sqrt{1-m^2})}.
\]
Uniform integrability at arbitrarily higher powers follows. Passing to the distributional limit proves convergence of every fixed positive moment, with \(\mathbb E E^{2p}=\Gamma(2p+1)\). All claims follow.

## Verification
Run `python3 artifacts/verify_cube_section_inradius.py` from the extracted package root. This standalone standard-library program obtains polygons by literal intersection with all twelve edges of the three-cube, orders their vertices in the section plane, computes perpendicular distances from the origin to each polygon edge, and compares their minimum with the independently stated radius formula for 400 random normals. It also checks six exact two-dimensional CDF values against independent Simpson integration of the Dirichlet density, checks random finite-dimensional support, and compares 5,000 high-dimensional samples with the predicted cubic scaling and squared-exponential limit. The recorded execution returned `CUBE_SECTION_INRADIUS_CHECKS_OK`. The finite diagnostics are not substitutes for the all-dimensional proof, the endpoint asymptotics, or moment uniform integrability.

## Relationship to prior work
Guédon, Litvak, Tatarko and Vritsiou, *On random diameters of convex bodies* (arXiv:2609.24131v1, 21 September 2026) study random **outer** radii and diameters, obtaining high-probability bounds and applications to \(p\)-ellipsoids. Their accessible full text distinguishes their outer radius explicitly from inradius and does not state a distribution for cube-section inscribed balls, nor its center locus. Brandenburg and Meroni, *Combinatorics of slices of cubes* (arXiv:2510.09265v1, 10 October 2025), classify face-lattice types of cube hyperplane sections in bounded dimensions; their accessible HTML studies vertex counts, section volumes and combinatorics rather than the intrinsic largest inscribed ball. Ambrus, *Critical central sections of the cube* (arXiv:2107.14778), concerns critical points of the section **volume**, not inradius. Böröczky and Henk, *Random Projections of Regular Polytopes* (1997 preprint, published 2000), prove expected face-count asymptotics for projections of regular cross-polytopes, not distribution laws of their circumscribed Euclidean radii. Related indexed geometric results on incenter loci of Boolean signed-chain polytopes and on directional vertex-count fluctuations of random cube sections concern respectively a different ambient polytope and a different section observable; their full statements have been compared. None of these works directly implies the coupled sharp finite law, incenter dimension, and cubic-scale squared-exponential limit for cube-section inradii. This comparison cannot rule out an unindexed earlier exact calculation.

## Limitations
This theorem concerns intrinsic Euclidean inballs in **central codimension-one** cube sections, not circumradii, noncentral sections, arbitrary codimension or arbitrary convex bodies. The result is an exact analytic classification and asymptotic law; it does not claim new general inequalities for all convex bodies. The Dirichlet integral is a genuine \((n-1)\)-dimensional integral, not an elementary closed form in arbitrary dimension. The expression for every center remains true without genericity, but the \((n-2)\)-dimensional assertion needs the stated genericity. Publication priority beyond accessible indexed records remains unverified. The computational tests are finite and no independent mathematical audit is asserted.

## References
1. O. Guédon, A. E. Litvak, K. Tatarko, B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131v1 (first public 21 September 2026), https://arxiv.org/abs/2609.24131.
2. M.-C. Brandenburg and C. Meroni, *Combinatorics of slices of cubes*, arXiv:2510.09265v1 (first public 10 October 2025), https://arxiv.org/html/2510.09265v1.
3. G. Ambrus, *Critical central sections of the cube*, arXiv:2107.14778 (2021), https://arxiv.org/abs/2107.14778.
4. *Cube-section incenter loci of Boolean signed-chain polytopes*, published mathematical finding, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-cube-section-incenter-loci-of-boolean-signed-chain-polytopes--9b96bfb466e7 .
5. *Direction-resolved half-normal fluctuations of random central cube sections*, published mathematical finding, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-direction-resolved-half-normal-fluctuations-of-random-central-cu--5ebe8c4adfad .
5. K. Böröczky Jr. and M. Henk, *Random Projections of Regular Polytopes*, preprint SC 97-21 (May 1997), published *Arch. Math.* 2000. Author-hosted full text: https://page.math.tu-berlin.de/~henk/preprints/boeroeczky%20henk%26random%20projections%20of%20regular%20polytopes.pdf .
