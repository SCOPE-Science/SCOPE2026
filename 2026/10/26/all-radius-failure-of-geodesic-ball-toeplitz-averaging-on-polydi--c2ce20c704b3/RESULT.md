# All-radius failure of geodesic-ball Toeplitz averaging on polydiscs

## Finding

**Theorem.** For each integer \(n\ge 2\) and **every** radius \(R>0\), there exists a real-valued \(f_R\in C^\infty(\mathbb D^n)\cap L^\infty(\mathbb D^n)\), with \(|f_R|\le1\), such that its Euclidean-volume average over each genuine Bergman geodesic ball of radius \(R\) tends to zero as the center approaches **any part** of \(\partial\mathbb D^n\), while the Toeplitz operator \(T_{f_R}\) on the unweighted Bergman space \(A^2(\mathbb D^n)\) is noncompact. More precisely, some \(t_R>0\) satisfies
\[
\|T_{f_R}\|_{\mathrm{ess}}\ge(1+t_R^2)\left(\frac{\pi t_R}{\sinh(\pi t_R)}\right)^2>0.
\]
This strengthens the *sufficiently-small-radius* counterexample of Ma–Zhang to every prescribed positive radius. The constructed symbol depends on the chosen radius; no single symbol is claimed to work for all radii simultaneously.

There is also an exact new multiplier asymptotic. Fix \(r>0\) and equip \(\mathbb H^n\), \(\mathbb H=\{x+iy:y>0\}\), with the product metric \(ds_0^2=\sum_{j=1}^n (dx_j^2+dy_j^2)/y_j^2\). Put \(o=(i,\ldots,i)\), \(u(z)=\log y_1-\log y_2\), and
\[
I_r(t)=\int_{d_0(o,z)<r} e^{it u(z)}\,dV_{\mathrm E}(z),\qquad b=r/\sqrt2.
\]
For each fixed \(r>0\), as \(t\to+\infty\),
\[
\boxed{\ I_r(t)=\sqrt2(2\pi)^{n-1/2}b^{n-3/2}\sinh(b)\,t^{-n-1/2}
\cos\!\left(\sqrt2rt-\frac{\pi(2n+1)}4\right)
+O_{n,r}(t^{-n-3/2}).\ }
\]
In particular \(I_r\) is real and has infinitely many distinct positive zeros for **every** \(r>0\).

## Assumptions and scope

The dimension \(n\) is any fixed integer at least two; \(r,R\) are arbitrary fixed strictly positive real numbers. All volumes defining the ball averages and \(I_r\) are ordinary Euclidean volumes, **not** hyperbolic invariant volumes. In the normalization of Ma–Zhang, \(r=\sqrt{2(n+1)}R\). The Bergman space and Toeplitz operator use ordinary Euclidean area on \(\mathbb D^n\). The kernel-average and essential-norm conclusions rely on the localization construction spelled out below, with one chosen positive zero \(t_R\) of the multiplier. Constants in the oscillatory remainder may depend on both \(n\) and the fixed \(r\); no uniform estimate as \(r\to\infty\) is claimed.

## Proof

**1. Phase geometry.** Introduce logarithmic vertical coordinates \(s_j=\log y_j\), so that each hyperbolic plane has metric \(ds_j^2+e^{-2s_j}dx_j^2\). Write \(q(z)=d_0(o,z)^2/2\). Then \(u=s_1-s_2\) has \(|\nabla_g u|^2=2\), hence no interior stationary point. Cauchy–Schwarz along the product distance implies \(|u(z)|\le\sqrt2d_0(o,z)\). On the closed ball the only points of equality are
\[
p_+=(ie^b,ie^{-b},i,\ldots,i),\quad p_-=(ie^{-b},ie^b,i,\ldots,i),
\]
with critical values \(+\sqrt2r\) and \(-\sqrt2r\). There are no other stationary points of \(u\) restricted to the boundary sphere. Indeed, at such a point \(\nabla_gu\) is proportional to \(\nabla_gq\). The latter's component in each coordinate is the end-velocity of the unique geodesic from \(i\), multiplied by its length. Its vanishing horizontal component forces \(x_j=0\) in the first two factors, while the zero gradient of \(u\) in all remaining factors forces those coordinates to equal \(i\). The remaining normal equations are \((1,-1)=c(s_1,s_2)\) with \(s_1^2+s_2^2=r^2\), giving exactly the two stated points.

**2. Nondegenerate boundary extrema and coefficient.** At \(p_+\), \(\nabla_gu=b^{-1}\nabla_gq\). The Hessian on the tangent space of \(\partial B_r\) of the restricted phase is the restriction of \(\operatorname{Hess}_g u-b^{-1}\operatorname{Hess}_gq\). In orthonormal directions consisting of the horizontal direction in factor one, the horizontal direction in factor two, and \(2n-3\) remaining tangential directions, the eigenvalues are exactly
\[
-(1+\coth b),\quad-(\coth b-1),\quad \underbrace{-1/b,\ldots,-1/b}_{2n-3\text{ times}}.
\]
To check these identities, use \(\operatorname{Hess}_g s_j\) equal to \(-1\) in the unit horizontal direction, zero in the unit vertical direction; and the hyperbolic-distance identity \(\operatorname{Hess}(d(i,z)^2/2)=\rho\coth\rho\) horizontally and \(1\) radially, with smooth limiting value \(1\) at \(\rho=0\). Since \(\coth b>1\), the maximum is nondegenerate, with positive determinant of the negative Hessian
\[
H_r=(1+\coth b)(\coth b-1)b^{-(2n-3)}=\frac{b^{-(2n-3)}}{\sinh^2b}.
\]
By the coordinate-exchange symmetry, \(p_-\) is a nondegenerate minimum with the same absolute Hessian determinant. The Euclidean volume density relative to Riemannian volume is \(\prod_j y_j^2\), which equals \(1\) at both critical points.

**3. Boundary stationary phase.** Because \(du\ne0\) throughout the closed ball, repeated integration by parts using the vector field \(\nabla_gu/|\nabla_gu|_g^2\) reduces \(I_r(t)\) to oscillatory boundary integrals, with arbitrarily high-order interior remainders. The boundary is smooth: a product of hyperbolic planes is a Hadamard manifold. Ordinary nondegenerate stationary phase on the \((2n-1)\)-dimensional boundary then leaves precisely the two contributions computed above. At \(p_+\), the boundary normal factor is \(+1/\sqrt2\), at \(p_-\) it is \(-1/\sqrt2\). Together with the factor \((it)^{-1}\) from the divergence theorem, the two conjugate leading terms yield
\[
\frac{\sqrt2(2\pi)^{n-1/2}}{\sqrt{H_r}}\,t^{-n-1/2}
\cos\!\left(\sqrt2rt-\frac{\pi(2n+1)}4\right).
\]
The standard smooth stationary-phase expansion supplies a remainder of order \(O_{n,r}(t^{-n-3/2})\). Substitution of \(H_r\) proves the displayed exact coefficient. The amplitude is strictly positive, so along two interlacing sequences where the cosine is \(+1\) or \(-1\), the multiplier takes opposite signs for sufficiently large \(t\). By continuity it has infinitely many positive zeros.

**4. Transfer to a noncompact Toeplitz symbol.** Choose a positive zero \(t_R\) of \(I_{\sqrt{2(n+1)}R}\). The dilation/translation isometry \(z_j\mapsto\alpha_j+\beta_jz_j\) of \(\mathbb H^n\) multiplies \(e^{it_Ru}\) by \((\beta_1/\beta_2)^{it_R}\), and multiplies Euclidean volume by a positive constant. Hence the real function \(G=\operatorname{Re}e^{it_Ru}\) has integral zero over **every** radius-\(r\) product-hyperbolic geodesic ball. Ma–Zhang, Theorem 17, proof after equation (33), supplies the needed localization and Cayley-transform construction for **any fixed radius once such a positive multiplier zero exists**: disjoint, increasingly remote slowly varying cutoffs make the genuine Euclidean disk-ball averages of the resulting \(f_R\) tend to zero along the entire boundary. The same calculation of the normalized-kernel limit gives
\[
\widetilde{f_R}(a_j)\longrightarrow(1+t_R^2)\left(\frac{\pi t_R}{\sinh(\pi t_R)}\right)^2>0.
\]
Since normalized Bergman kernels along \(a_j\to\partial\mathbb D^n\) converge weakly to zero, a compact operator has vanishing corresponding diagonal matrix coefficients. This proves the essential-norm bound and noncompactness.

## Verification

The critical geometric identities are reconstructed in Steps 1 and 2, including the sign and the strict inequality \(\coth b>1\) at every finite positive \(b\). Step 3 computes the explicit leading coefficient and oscillatory phase using the standard boundary stationary-phase theorem; Step 4 invokes the fully specified localization argument in the cited open-access source. The accompanying standalone test checks algebraic identities and the positive-definite boundary Hessian for sample positive radii; finite testing is *not* used to prove the all-radius assertion. Reproduction requires Python with SymPy for `check_stationary.py`; the analytical proof is self-contained apart from the standard stationary-phase result and the explicitly cited localization construction.

## Relationship to prior work

Ma and Zhang, *Compact Toeplitz Operators and the Geometry of Fixed-Radius Averages*, arXiv:2610.22893v1, Theorem B(ii) / Theorem 17, prove the same counterexample for \(0<R<R_n\) using a small-radius Euclidean-ball/Bessel limit to produce one positive zero of \(I_r\). Their equations (33)–(35) and proof of the essential-norm bound are used **with attribution**. The present new step is the global-in-radius stationary-phase law showing that this zero exists for *every* \(r>0\); this removes the restriction \(R<R_n\). Cao, He, and Zhang, arXiv:2609.24614, prove a positive fixed-radius characterization on the single disk, a dimension-one setting where the two-coordinate cancellation mechanism is unavailable. Standard stationary-phase results are attributed to Hörmander.

## Limitations

The theorem does not provide a single symbol valid simultaneously at multiple prescribed radii; it does not assert uniform lower bounds on essential norms over an unbounded radius range, identify the first positive multiplier zero, or extend the failure to positive symbols. It is specifically about genuine geodesic balls on polydiscs in dimension at least two with Euclidean averaging measure. Historical priority relative to older fixed-radius mean-value or spectral multiplier theory warrants independent literature verification. No independent audit has yet been performed.

## References

1. P. Ma and Z. Zhang, *Compact Toeplitz Operators and the Geometry of Fixed-Radius Averages*, arXiv:2610.22893v1 (first public version October 16, 2026), especially Section 4, Theorem 17, equations (32)–(35). https://arxiv.org/html/2610.22893v1
2. G. Cao, L. He, and S. Zhang, *Compactness of Toeplitz Operators on the Bergman Space*, arXiv:2609.24614 (September 2026). https://arxiv.org/abs/2609.24614
3. L. Hörmander, *The Analysis of Linear Partial Differential Operators I*, stationary-phase theorem for nondegenerate critical points (standard reference; no numerical theorem label asserted).
