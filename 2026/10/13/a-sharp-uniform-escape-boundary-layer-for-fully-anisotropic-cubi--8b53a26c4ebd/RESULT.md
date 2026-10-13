# A sharp uniform escape boundary layer for fully anisotropic cubic walks

## Finding
Let a nearest-neighbour random walk on \(\mathbb Z^3\) move in either direction of coordinate \(j\) with probability \(h_j/2\), where each \(h_j>0\) and \(\sum_jh_j=1\). Write \(q(h)\) for the probability that the walk, started at the origin, never returns to the origin at a positive time. Define, for \(0<c<1\),
\[
K(c)=\frac1{(2\pi)^2}\int_{[-\pi,\pi]^2}
\frac{du\,dv}{\sqrt{2c(1-\cos u)+2(1-c)(1-\cos v)}}.
\]
**Uniform boundary-layer theorem.** For every \(0<\varepsilon<1\) and \(0<c<1\), with \(h=(1-\varepsilon,\varepsilon c,\varepsilon(1-c))\),
\[
\boxed{\quad \sqrt{1-\varepsilon}\ \le\
\frac{q(h)K(c)}{\sqrt\varepsilon}\ \le\ 1.\quad}
\]
Both inequalities are strict in the interior. At every fixed \(\varepsilon\), the lower factor is optimal uniformly over \(c\), since the normalized middle expression tends to \(\sqrt{1-\varepsilon}\) as \(c\downarrow0\). Further,
\[
K(c)=\frac{\log(1/c)}{2\pi}+O(1)\qquad(c\downarrow0),
\]
so for **every** simultaneous regime \(\varepsilon\downarrow0\), \(c\downarrow0\), without a condition relating their rates,
\[
\boxed{\quad q(1-\varepsilon,\varepsilon c,\varepsilon(1-c))
\sim\frac{2\pi\sqrt\varepsilon}{\log(1/c)}.\quad}
\]
For fixed \(0<c<1\), instead \(q/\sqrt\varepsilon\to1/K(c)\). The function \(K\) is symmetric and strictly convex, and uniquely minimized at \(c=1/2\). These statements together characterize the strongly hierarchical and fixed-ratio escape boundary layers.

For comparison, at a two-dimensional face, fix \(a,b>0\), \(a+b=1\). Then
\[
q((1-\varepsilon)a,(1-\varepsilon)b,\varepsilon)
=\frac{2\pi\sqrt{ab}}{\log(1/\varepsilon)}
\left(1+O_{a,b}(1/\log(1/\varepsilon))\right).
\]
The face coefficient is maximized when \(a=b=1/2\). At fixed \(\varepsilon\) and \(c\downarrow0\), the uniform theorem also gives \(q\sim 2\pi\sqrt{\varepsilon(1-\varepsilon)}/\log(1/c)\).

## Assumptions and scope
Every claim concerns the symmetric, translation-invariant, discrete-time walk with the stated independent step directions. The escape probability \(q\) is the *nonreturn probability after time zero*, not the probability of avoiding a different target. The two coordinates in \(K\) have strictly positive shares \(c\) and \(1-c\); endpoints follow by limits only. Constants in the face error may depend on the fixed positive \(a,b\). All limits hold along arbitrary real parameter sequences satisfying the displayed conditions.

## Proof
**1. Exact return Green integral.** For \(h\) in the open simplex, Fourier inversion for the walk and monotone convergence over geometric damping yield
\[
G(h)=\sum_{n\ge0}\Pr_h(S_n=0)
=\frac1{(2\pi)^3}\int_{[-\pi,\pi]^3}
\frac{d\theta}{1-\sum_{j=1}^3h_j\cos\theta_j}.
\]
The denominator is quadratic near its only torus zero, hence its reciprocal is locally integrable in three dimensions. The renewal identity at the origin yields \(q(h)=G(h)^{-1}\). These formulas use the standard normalization \(h_j/2\) for each of the two signed directions.

**2. Integrate out the dominant direction.** The elementary identity \(\int_{-\pi}^{\pi}(A-B\cos u)^{-1}du/(2\pi)=(A^2-B^2)^{-1/2}\), valid for \(A>|B|\), gives, with \(\delta=c(1-\cos u)+(1-c)(1-\cos v)\),
\[
G(1-\varepsilon,\varepsilon c,\varepsilon(1-c))
=\varepsilon^{-1/2}\int_{\mathbb T^2}
\frac{d\mu(u,v)}{\sqrt{\delta[2(1-\varepsilon)+\varepsilon\delta]}}
=\frac{K(c)}{\sqrt\varepsilon}\,
\mathbb E_{\nu_c}\left[(1-\varepsilon+\varepsilon\delta/2)^{-1/2}\right].
\]
Here \(\mu\) is normalized Haar measure and \(\nu_c\) has density \((2\delta)^{-1/2}/K(c)\) relative to \(\mu\). Since \(0<\delta<2\) almost everywhere, \(1-\varepsilon<1-\varepsilon+\varepsilon\delta/2<1\). Taking reciprocals proves the strict two-sided bound.

**3. Exact sharpness of the lower factor and the logarithmic cusp.** Put \(d=1-c\) and \(A(u)=1-\cos u\). For \(d\ge1/2\) and \(z\downarrow0\), a comparison of \(2d(1-\cos v)\) with \(d v^2\) near \(v=0\), bounding the complement uniformly, proves
\[
\frac1{2\pi}\int_{-\pi}^{\pi}
\frac{dv}{\sqrt{z+2d(1-\cos v)}}
=\frac{\log(1/z)}{2\pi\sqrt d}+O(1),
\]
where the error is uniform for \(0<z\le4c\) and \(c\) sufficiently small. Indeed \(2d(1-\cos v)=dv^2+O(v^4)\), the integrand difference has uniformly bounded integral, and \(\int_{-r}^r(dv^2+z)^{-1/2}dv=\log(1/z)/\sqrt d+O(1)\). Substitute \(z=2cA(u)\) and average over \(u\); the function \(\log A(u)\) is integrable at \(u=0\). Thus \(K(c)=\log(1/c)/(2\pi\sqrt{1-c})+O(1)=\log(1/c)/(2\pi)+O(1)\).

Under \(\nu_c\), the event \(\delta\ge\rho\) has probability at most \(1/(K(c)\sqrt{2\rho})\), tending to zero for every fixed \(\rho>0\). Hence \(\delta\to0\) in \(\nu_c\)-probability. At fixed \(\varepsilon\), bounded convergence in the last expectation in step 2 gives the lower-factor equality in the limit. If \(\varepsilon\downarrow0\) simultaneously with \(c\downarrow0\), the uniform two-sided estimate squeezes \(qK/\sqrt\varepsilon\to1\), giving the joint scaling without any relative-rate restriction.

**4. Convexity of the shape constant.** The quantity \(K(c)\) is an average of \([2(cA(u)+(1-c)A(v))]^{-1/2}\). This is a strictly convex function of \(c\) whenever \(A(u)\ne A(v)\), a set of positive area. Finiteness of \(K\) for interior \(c\) follows from the integrable \(r^{-1}\) singularity near the origin. Symmetry in \(u,v\) gives \(K(c)=K(1-c)\), proving the unique minimizer.

**5. Planar face.** For \(h=((1-\varepsilon)a,(1-\varepsilon)b,\varepsilon)\), set \(D=a(1-\cos u)+b(1-\cos v)\). Integrating the third coordinate gives
\[
G(h)=\frac1{1-\varepsilon}\int_{\mathbb T^2}
\frac{d\mu}{\sqrt{D[D+2\varepsilon/(1-\varepsilon)]}}.
\]
Near zero, \(D=(au^2+bv^2)/2+O((u^2+v^2)^2)\). Replacing \(D\) by this quadratic form changes the integral by \(O_{a,b}(1)\): the derivative of the integrand in its first argument is \(O(D^{-2})\), while the quadratic replacement error is \(O((u^2+v^2)^2)\). Outside a fixed small disk the integral is bounded uniformly. Elliptical polar coordinates \(x=\sqrt{a/2}\,u\), \(y=\sqrt{b/2}\,v\) then yield
\[
G(h)=\frac{\log(1/\varepsilon)}{2\pi\sqrt{ab}}+O_{a,b}(1).
\]
Inverting gives the asserted face asymptotic. The arithmetic-geometric mean inequality gives the unique maximum of its coefficient.

## Verification
The accompanying `verify.py` reconstructs rational exact return coefficients by both multinomial counting and direct transition propagation for three nondegenerate weight triples, and checks the renewal decomposition of return probabilities. Its optional SciPy numerical section evaluates both the three-coordinate Green integral and the two-coordinate \(K\) integral using Bessel-function Laplace transforms, tests the uniform inequalities on twenty parameter pairs, and checks symmetry, strict minimum, and a reference \(K(1/2)\) value. The final package checker completed 77 assertions. Numerical checks are not substituted for the proof of universal claims.

## Relationship to prior work
Hsiau–Tsai–Yao (2026) prove stochastic ordering of first-return times under majorization for this walk family. Their order comparison alone does not determine escape-probability scaling rates or the uniform sharp multiplicative bound. Delves–Joyce (2001) provide exact anisotropic cubic-lattice Green functions and are explicitly credited for that foundational coverage: neither an exact Green function nor the renewal inversion is claimed new. A 2010 survey by Guttmann identifies the earlier exact result for a one-parameter anisotropic form with two equal coordinate weights. The claim here concerns a fully unequal transverse split, a uniform singular approximation valid at every ratio, the sharp uniform lower factor, and its arbitrary-rate two-scale consequence. Some older exact Green representations may allow these results to be derived after additional analysis; see limitations.

## Limitations
The theorem concerns only translation-invariant walks on \(\mathbb Z^3\) with symmetric signed steps. It does not give exact first-return-time distributions, mean return times, or quantitative finite-time mixing. The 2026 motivating paper's full text and some older exact-Green-function papers could not be materially inspected; the relationship assessment therefore carries genuine residual priority risk. The stand-alone results here have an analytical proof but no independent scientific audit. Extreme-axis endpoints have zero escape probability and are treated only through limits.

## References
1. S.-R. Hsiau, T.-Y. Tsai and Y.-C. Yao, “Stochastic dominance of first return times for nearest-neighbor random walks on \(\mathbb Z^d\),” arXiv:2609.36728, initially submitted 29 September 2026. https://arxiv.org/abs/2609.36728
2. R. T. Delves and G. S. Joyce, “Exact evaluation of the Green function for the anisotropic simple cubic lattice,” *J. Phys. A* **34** (2001), L59–L65. https://doi.org/10.1088/0305-4470/34/8/101
3. R. T. Delves and G. S. Joyce, “On the Green Function for the Anisotropic Simple Cubic Lattice,” *Ann. Phys.* **291** (2001), 71–133. https://doi.org/10.1006/aphy.2001.6148
4. A. J. Guttmann, “Lattice Green functions in all dimensions,” *J. Phys. A* **43** (2010), 305205. https://arxiv.org/abs/1004.1435
