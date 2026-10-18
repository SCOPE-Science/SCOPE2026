# Exact Euclidean distance and scale monotonicity of log-cosh transition bodies of parallelotopes

## Finding
For every integer \(n\ge 2\) and every origin-centered parallelotope \(K=T[-1,1]^n\) with \(T\in GL(n,\mathbb R)\) and Euclidean volume \(V=2^n|\det T|\), consider the logarithmic-cosh boundary functional
\[
\Phi_K(y)=\int_{\partial K}(x\cdot\nu(x))\log\cosh\!\left(\frac{y\cdot\nu(x)}{2x\cdot\nu(x)}\right)dS(x),
\qquad \mathcal T_K=\{y\in\mathbb R^n:\Phi_K(y)\le 1\}.
\]
Here \(\nu\) is the outer unit normal defined on the relative interiors of facets, and the integral is the finite sum of facet integrals. Put \(F(s)=\operatorname{arcosh}(e^s)\) for \(s>0\). Then
\[
\boxed{d_{\mathrm{BM}}(\mathcal T_K,B_2^n)=\frac{F(1/V)}{\sqrt n\,F(1/(nV))}.}
\]
For fixed \(n\ge2\), this exact distance decreases strictly as \(V\) increases from zero to infinity, and its range is exactly \((1,\sqrt n)\). The limiting values are \(\sqrt n\) as \(V\downarrow0\) and \(1\) as \(V\to\infty\).

## Assumptions and scope
The body \(K\) is a full-dimensional, origin-centered parallelotope, with arbitrary Euclidean edge geometry and positive volume \(V\); no regularity of its facets beyond flatness is assumed. The functional \(\Phi_K\) is *defined directly by its facet integral*. The smooth-body covariogram convergence theorem in [1] assumes a \(C^3\) boundary and is not claimed here for polyhedral \(K\).

The Banach--Mazur distance between symmetric convex bodies is \(\inf\{\lambda\ge1: E\subset L\subset\lambda E\}\), where \(E\) ranges over origin-centered ellipsoids after identifying one body with a Euclidean ball by an invertible linear map. Since all bodies here are centrally symmetric, allowing translations does not improve this distance.

## Proof
**1. Exact reduction of the facet functional.** Let the \(i\)-th opposite facet pair of \(K=T[-1,1]^n\) have distance \(h_i>0\) from the origin and outer normals \(\pm\nu_i\). Either facet has \((n-1)\)-area \(V/(2h_i)\). On it, \(x\cdot\nu=h_i\), and \(\nu_i/h_i=T^{-\mathsf T}e_i\). The two facets therefore contribute exactly \(V\log\cosh((T^{-1}y)_i/2)\). For \(z=T^{-1}y/2\),
\[
\Phi_K(2Tz)=V\sum_{i=1}^n\log\cosh z_i.
\]
Consequently \(\mathcal T_K=2T\mathcal C_{n,s}\), where \(s=1/V>0\) and
\[
\mathcal C_{n,s}=\left\{z\in\mathbb R^n:\sum_{i=1}^n f(|z_i|)\le s\right\},\qquad f(t)=\log\cosh t.
\]
This is an origin-symmetric compact strictly convex body invariant under signed coordinate permutations.

**2. Sharp Euclidean radii and contact directions.** The function \(h(a)=f(\sqrt a)\) is strictly concave on \([0,\infty)\). Indeed, for \(t>0\), \(h'(t^2)=\tanh t/(2t)\), which strictly decreases because \(\tanh t-t\operatorname{sech}^2 t>0\), obtained by differentiating from its zero value at the origin. Therefore, for \(r>0\) and \(z\) with \(\sum z_i^2=r^2\), strict concavity (Jensen above, repeated subadditivity below) gives
\[
f(r)\le\sum_i f(|z_i|)\le n f(r/\sqrt n).
\]
The lower equality holds exactly for a single nonzero coordinate, while upper equality holds exactly when all \(|z_i|=r/\sqrt n\). Since \(f(F(t))=t\), the largest ball centered at zero contained in \(\mathcal C_{n,s}\) has radius
\[
r_{\mathrm{in}}=\sqrt n\,F(s/n),
\]
and touches exactly the \(2^n\) sign diagonals. Its smallest circumscribed origin-centered ball has radius
\[
r_{\mathrm{out}}=F(s),
\]
and touches exactly the \(2n\) coordinate axes.

**3. Ellipsoids cannot improve the radii quotient.** Let \(E_Q=\{z:z^{\mathsf T}Qz\le1\}\) be any centered ellipsoid with \(E_Q\subset\mathcal C_{n,s}\subset\lambda E_Q\), where \(Q\) is positive definite. Write \(p(z)\) for the Minkowski gauge of \(\mathcal C_{n,s}\). The inclusions are precisely
\[
p(z)^2\le z^{\mathsf T}Qz\le\lambda^2p(z)^2\quad\text{for every }z.
\]
Average both inequalities over the finite signed-permutation group. Since \(p\) is invariant and the average of \(g^{\mathsf T}Qg\) equals \((\operatorname{tr}Q/n)I\), the round ellipsoid \(E_{(\operatorname{tr}Q/n)I}\) satisfies both inclusions with the same \(\lambda\). Thus an optimal comparison ellipsoid can be chosen round. Its minimum possible factor is \(r_{\mathrm{out}}/r_{\mathrm{in}}\), proving the boxed exact Banach--Mazur formula.

**4. Strict monotonicity in volume.** Set \(R_n(s)=F(s)/(\sqrt n F(s/n))\). It suffices to show that \(R_n\) is strictly increasing in \(s>0\). Define \(\eta(s)=sF'(s)/F(s)\) and write \(t=F(s)\), so \(s=f(t)\) and \(\eta(s)=f(t)/(tf'(t))\). Let
\[
H(t)=\frac{tf'(t)}{f(t)},\qquad\kappa(t)=\frac{tf''(t)}{f'(t)}=\frac{2t}{\sinh(2t)}.
\]
The function \(\kappa\) is strictly decreasing for positive \(t\), as \(\sinh(2t)/(2t)\) is strictly increasing. Using \(f(0)=0\) and integrating the derivative of \(tf'(t)\) gives
\[
H(t)=\frac{\int_0^t f'(v)(1+\kappa(v))\,dv}{\int_0^t f'(v)\,dv}>1+\kappa(t).
\]
Consequently
\[
\frac{H'(t)}{H(t)}=\frac{1+\kappa(t)-H(t)}{t}<0.
\]
Hence \(\eta(s)=1/H(F(s))\) is strictly increasing, and
\[
\frac{d}{ds}\log R_n(s)=\frac{\eta(s)-\eta(s/n)}s>0
\qquad(s>0,n\ge2).
\]
Since \(s=1/V\), the distance strictly decreases in \(V\). Finally, \(F(s)\sim\sqrt{2s}\) as \(s\downarrow0\), while \(F(s)=s+\log2+o(1)\) as \(s\to\infty\). These imply the asserted endpoint limits and strict open range.

## Verification
The accompanying standalone standard-library script `verify_transition.py` tests the exact facet and extremal-radius formulas, evaluates explicit boundaries for dimensions \(2\) through \(8\), checks randomly sampled intermediate sphere directions, and confirms the predicted monotonic behavior on a fixed numerical grid. The script is a finite numerical regression only; the inequalities for all dimensions, all positive volumes, and all directions are proved above by analytic arguments.

## Relationship to prior work
Haddad, Jiménez, and Resende [1] introduce the critical log-cosh transition functional as part of the smoothed covariogram's three-regime limit for \(C^3\) convex bodies. Their paper develops this functional and its interpolation between projection-body geometries, without deriving an exact Euclidean Banach--Mazur profile for parallelotopes. The present work evaluates the facet formula (well-defined outside their regularity hypothesis), optimizes over *all* ellipsoids, and establishes strict volume dependence.

Grundbacher and Kobos [2] study exact Banach--Mazur distances for different \(\ell_p\)-sum and cone families. Those bodies are not the nonlinear log-cosh sublevel sets here. Averaging over coordinate symmetries is a classical tool and is not claimed to be novel; the exact interpolation law and its strict parameter monotonicity are the specific results.

## Limitations
No claim is made for arbitrary convex bodies, for nonsymmetric translated boxes, or for smooth-covariogram level-set convergence on nonsmooth polytopes. The result is an exact affine-distance profile for the facet-integral extension of the transition functional, not a reconstruction theorem. The possibility of equivalent calculations in unindexed older Orlicz-norm literature remains. No independent scientific audit has been performed.

## References
[1] Julián Haddad, C. Hugo Jiménez, Matheus Resende, *A Smooth Covariogram and the Transition Between Projection Bodies*, arXiv:2610.11700v1 (public October 8, 2026), especially the critical-transition boundary formula and Theorem 5, https://arxiv.org/html/2610.11700v1 .

[2] Florian Grundbacher and Tomasz Kobos, *Exact Banach--Mazur distances of certain \(\ell_p\)-sums and cones*, arXiv:2603.18268 (2026), https://arxiv.org/abs/2603.18268 .
