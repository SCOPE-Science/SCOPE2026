# Exact mean-width balancing and a Gaussian critical window for two-level order polytopes

## Finding
For integers \(p,q\ge 1\), put \(d=p+q\), and consider the standard Euclidean order polytope of the ordinal sum of two antichains:
\[
\mathcal O_{p,q}=\{(x,y)\in\mathbb R^p\times\mathbb R^q:0\le x_i\le y_j\le1\ \text{for every }i,j\}.
\]
Here the mean width is \(w(K)=\mathbb E_{U\in S^{d-1}}[h_K(U)+h_K(-U)]\), with \(U\) Haar-uniform and \(h_K\) the support function. Let \(Y=\max\{Z,0\}\) for \(Z\sim N(0,1)\), let all \(Y_i,Y'_j\) be independent copies, and define
\[
D_{p,q}=\sum_{i=1}^p Y_i-\sum_{j=1}^qY'_j,\quad
\mu=\frac1{\sqrt{2\pi}},\quad v=\frac12-\frac1{2\pi},\quad
c_d=\sqrt2\,\frac{\Gamma((d+1)/2)}{\Gamma(d/2)}.
\]
Then the **exact** mean width for every \(p,q\ge1\) is
\[
\boxed{w(\mathcal O_{p,q})=\frac{d\mu+\mathbb E|D_{p,q}|}{c_d}.}\tag{1}
\]
The expectation is evaluable by the convergent one-dimensional integral (7) below, without simulation or vertex enumeration.

For each fixed \(d\ge2\), the width is invariant under \(p\leftrightarrow q\) and **strictly increases with** \(|p-q|\), along the parity-compatible admissible values. It is minimized only by \(p=\lfloor d/2\rfloor\), \(q=\lceil d/2\rceil\) and their swap, and is maximized only at \(\{p,q\}=\{1,d-1\}\); for \(d=2,3\) the available configurations make these descriptions coincide.

There is a sharp square-root imbalance window. If \(d\to\infty\) and \((p-q)/\sqrt d\to\tau\in\mathbb R\), then
\[
\boxed{w(\mathcal O_{p,q})=\mu\sqrt d+F(\tau)+o(1),}\tag{2}
\]
where, writing \(\varphi,\Phi\) for the standard normal density and cumulative distribution function,
\[
F(\tau)=2\sqrt v\,\varphi\!\left(\frac{\mu\tau}{\sqrt v}\right)
+\mu\tau\left[2\Phi\!\left(\frac{\mu\tau}{\sqrt v}\right)-1\right].\tag{3}
\]
This profile is even, strictly convex and uniquely minimized at \(\tau=0\), with
\[
F(0)=\frac{\sqrt{\pi-1}}\pi.
\]
For macroscopic imbalance, if \(p/d\to s\in[0,1]\), then
\[
\boxed{\frac{w(\mathcal O_{p,q})}{\sqrt d}\longrightarrow\frac{1+|2s-1|}{\sqrt{2\pi}}.}\tag{4}
\]

## Assumptions and scope
The result concerns *the inherited standard Euclidean metric* on \(\mathbb R^{p+q}\), with no affine rescaling and no volume normalization. Both levels are nonempty and fully comparable across the levels: each lower element precedes every upper element, with no comparisons inside a level. Width is the **spherical average of the full directional width**, not the Gaussian expectation without radial normalization. The finite equality statements range over all integers \(p,q\ge1\); the limits allow any admissible sequences specified above. The theorem does not assert corresponding formulas for arbitrary height-two posets with missing cross-relations, or for other non-Euclidean metrics.

## Proof
**(i) Support identity.** Write \(t=\max_i x_i\). Every point of \(\mathcal O_{p,q}\) satisfies \(0\le t\le\min_j y_j\). For \(0<t<1\), it decomposes as
\[
(x,y)=(1-t)\left(0,\frac{y-t\mathbf1_q}{1-t}\right)+t\left(\frac xt,\mathbf1_q\right).
\]
Both points in parentheses lie in the respective cube faces \(\{0\}^p\times[0,1]^q\) and \([0,1]^p\times\{1\}^q\). The endpoint cases \(t=0,1\) lie in those faces directly. Consequently the order polytope is their convex hull. For a vector \(g=(a,b)\), maximizing a linear functional over the two faces gives
\[
h_{\mathcal O_{p,q}}(a,b)
=\max\left\{\sum_{j=1}^q(b_j)_+,\ \sum_{j=1}^q b_j+\sum_{i=1}^p(a_i)_+\right\}
=\sum_{j=1}^q(b_j)_++\left(\sum_i(a_i)_+-\sum_j(-b_j)_+\right)_+.
\tag{5}
\]
Here \(r_+=\max\{r,0\}\).

**(ii) Exact width.** For independent standard Gaussian coordinates, \((a_i)_+\) and \((-b_j)_+\) are independent copies of \(Y\), with \(\mathbb EY=\mu\), \(\operatorname{Var}(Y)=v\). The identity \(r_+=(r+|r|)/2\) applied to (5) yields
\[
\mathbb E h_{\mathcal O_{p,q}}(G)=\frac{d\mu+\mathbb E|D_{p,q}|}{2}.\tag{6}
\]
The standard normal vector factors as \(G=RU\), with \(R=\|G\|_2\) independent of uniform \(U\), and \(\mathbb ER=c_d\). Homogeneity of support and symmetry of \(G\) give \(w=2\mathbb E h(G)/c_d\), proving (1). In particular the only normalization in (1) is the actual Gaussian radial expectation.

For a direct finite-dimensional evaluation, set \(\phi(t)=\mathbb E e^{itY}=\frac12+\frac1{\sqrt{2\pi}}\int_0^\infty e^{-x^2/2+itx}\,dx\). The classical Fourier identity for absolute first moments yields
\[
\boxed{\mathbb E|D_{p,q}|=\frac2\pi\int_0^\infty
\frac{1-\operatorname{Re}[\phi(t)^p\overline{\phi(t)}^{\,q}]}{t^2}\,dt.}\tag{7}
\]
The integrand extends continuously at zero because \(D_{p,q}\) has finite second moment, and decays as \(O(t^{-2})\) at infinity since characteristic functions have modulus at most one. Formula (7) is a convergent exact one-dimensional representation.

**(iii) Strict balancing at every finite dimension.** Exchange the levels to see \(D_{q,p}\stackrel d=-D_{p,q}\), hence width symmetry. For \(p\ge q\ge2\), couple the imbalance-increasing pair \((p+1,q-1)\) with \((p,q)\) by writing their difference variables as \(S+Y\) and \(S-Y\), where \(S\) has \(p\) positive summands and \(q-1\) negative summands, and \(Y\) is independent. Split \(S=S_0+T\), where \(S_0\) is a difference of two independent sums of \(q-1\) copies of \(Y\), so \(S_0\stackrel d=-S_0\), and \(T\) is an independent sum of \(p-q+1\ge1\) copies of \(Y\). Define \(\psi(s)=\mathbb E_Y[|s+Y|-|s-Y|]\). This function is odd and strictly increasing, since \(\psi(s)=2\mathbb E\min\{s,Y\}\) for \(s\ge0\), and \(Y\) has positive probability in every interval \((0,a)\). Because \(T\ge0\) and \(\Pr(T>0)>0\),
\[
\mathbb E|S+Y|-\mathbb E|S-Y|=\mathbb E\psi(S_0+T)>\mathbb E\psi(S_0)=0.
\]
The factor \(c_d\) and the term \(d\mu\) are unchanged, proving the strictly increasing sequence from balance toward both extremes. The comparison between the two middle configurations when \(d\) is odd is equality by level-swap symmetry.

**(iv) Critical window.** The centered sum \(D_{p,q}-\mu(p-q)\) has variance \(dv\), and is a sum of independent centered variables with bounded third absolute moments. The triangular-array Lyapunov central limit theorem therefore gives
\[
\frac{D_{p,q}}{\sqrt d}\Rightarrow N(\mu\tau,v)
\quad\text{whenever }(p-q)/\sqrt d\to\tau.
\]
Its second moments remain bounded, so the absolute values are uniformly integrable. Consequently \(\mathbb E|D_{p,q}|/\sqrt d\to\mathbb E|\mu\tau+\sqrt v Z|=F(\tau)\), with (3) the elementary folded-normal formula. As \(c_d=\sqrt d(1+O(d^{-1}))\), (2) follows. Differentiation yields \(F''(\tau)=2\mu^2\varphi(\mu\tau/\sqrt v)/\sqrt v>0\), proving strict convexity and the minimum statement. If \(p/d\to s\), then \(D_{p,q}/d\to\mu(2s-1)\) in \(L^2\), since its variance divided by \(d^2\) is \(v/d\). Combining this with (1) proves (4).

## Verification
The standalone reproducibility script \(\texttt{checks/mean_width_check.py}\) tests the exact vertex-support identity against direct enumeration for 1,920 Gaussian inputs across sixteen layer-size pairs, evaluates (7) against the perimeter-over-pi mean width of the planar right isosceles order triangle, and tests finite balancing and symmetry through dimension twelve using deterministic quadrature. The critical profile is evaluated at five specified imbalance values. Run from the package root using \(\texttt{python checks/mean_width_check.py}\) with Python, NumPy, and SciPy installed. The file is included in full with no external data dependency. These are finite corroboration checks, not proofs of the all-dimension claims: the latter follow from steps (i)–(iv).

## Relationship to prior work
Stanley's *Two Poset Polytopes* (1986) establishes the classical order-polytope definition, its filter vertices and its Ehrhart/volume relationship; the support identity (5) also follows from that vertex description. Chan, Pak and Panova's *Effective poset inequalities* (first posted May 5, 2022) treats linear extensions, order polynomials and related geometric/Ehrhart inequalities. Chan and Pak's later work concerns Alexandrov–Fenchel equality complexity and slices of order polytopes. These sources supply motivation and background, but none of the inspected relevant results yields the exact spherical mean width (1), the strict fixed-d balancing law, or the Gaussian critical-window profile (2)–(4). General inequalities on mean width of convex bodies provide no explicit profile for these two-level polytopes without further calculations. A published computation of the John ellipsoid of balanced two-layer order polytopes concerns a different canonical invariant and only equal-size levels; its ellipsoid data alone do not determine the sphere-average support functional.

## Limitations
No claim is made for arbitrary bipartite comparability patterns or nonstandard Euclidean metrics. The novelty comparison is evidence-based rather than a proof that no equivalent result exists in all publications; older literature under alternate terminology could cover part of the statement. Numerical quadrature is only a reproducibility check. The work has not undergone independent mathematical review or external proof certification.

## References
- Richard P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23. Full text: https://math.mit.edu/~rstan/pubs/pubfiles/66.pdf
- Swee Hong Chan, Igor Pak, Greta Panova, *Effective poset inequalities*, arXiv:2205.02798, initial public version May 5, 2022; SIAM Journal on Discrete Mathematics 37 (2023), 1842–1880. https://arxiv.org/abs/2205.02798
- Swee Hong Chan and Igor Pak, *Equality cases of the Alexandrov–Fenchel inequality are not in the polynomial hierarchy*, arXiv:2309.05764, first public version September 2023. https://arxiv.org/abs/2309.05764
- Károly J. Böröczky, Ferenc Fodor, Daniel Hug, *Strengthened inequalities for the mean width and the ℓ-norm*, Journal of the London Mathematical Society 104 (2021), 233–268. https://doi.org/10.1112/jlms.12429
