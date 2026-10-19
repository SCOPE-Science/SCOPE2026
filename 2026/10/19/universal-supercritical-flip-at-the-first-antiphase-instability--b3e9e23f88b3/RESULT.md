# Universal supercritical flip at the first antiphase instability on weighted trees

## Finding
For **every finite tree** with at least one edge and **arbitrary positive edge weights**, the first loss of linear stability of phase opposition in its discrete repulsive-sine Huygens map is a **strictly supercritical period-doubling bifurcation**. A unique nearby prime-period-two attracting orbit emerges immediately above the sharp step-size boundary. Its leading spatial profile, displacement coefficient, and leading critical multiplier are explicit in the weighted top-Laplacian eigenvector.

More precisely, let the tree have \(N+1\ge2\) vertices and \(N\) edges, with positive weights \(a_e\). Choose the bipartite orientation so that at each vertex all incident incidence signs agree. Write \(B\) for the incidence matrix, \(A=\operatorname{diag}(a_e)\), \(K=B^{\mathsf T}B\), \(M=KA\), and \(\Lambda=\lambda_{\max}(A^{1/2}KA^{1/2})\). Let \(v\in(0,\infty)^N\) be the unique Perron eigenvector normalized by \(v^{\mathsf T}Av=1\), and define
\[
\kappa=\frac13\sum_{e=1}^{N}a_ev_e^4>0,\qquad \delta=h\Lambda-2.
\]
For some \(\varepsilon>0\) depending on the tree and weights, whenever \(0<\delta<\varepsilon\), the map admits a unique small prime-period-two orbit near antiphase. In edge deviations \(x=z-\pi\mathbf1\), its points are \(\pm x_\delta\), with
\[
 x_\delta=\sqrt{\frac{\delta}{\kappa}}\,v+O(\delta^{3/2}).
\]
This orbit is locally exponentially attracting. Its one-step Jacobian has one critical multiplier \(-1+2\delta+O(\delta^2)\), while its other multipliers converge to \(1-2\lambda_j/\Lambda\) for the remaining positive eigenvalues \(\lambda_j<\Lambda\). The corresponding two-step multiplier in the critical mode is \(1-4\delta+O(\delta^2)\). Below the boundary \(0<h<2/\Lambda\), antiphase is a hyperbolic sink; above it antiphase is unstable. No claim is made at the equality boundary or away from the stated local bifurcation neighborhood.

## Assumptions and scope
The tree is undirected, finite, connected and has no cycles. All \(a_e\) are strictly positive, with no genericity assumptions and no bound on vertex degrees. The phase-edge map is
\[
 G_h(z)=z+hKA\sin z\pmod{2\pi},\qquad z\in\mathbb T^N,
\]
where sine acts coordinatewise. The phase-opposition state is \(z_*=\pi\mathbf1\). The center coordinates \(x=z-z_*\) are taken in a local real chart; the model then becomes \(F_h(x)=x-hM\sin x\). The step is \(h>0\). The real positive parameter \(\delta=h\Lambda-2\) measures distance above the first sharp loss-of-stability threshold.

## Proof
**1. A simple positive top mode for every weighted tree.** Every tree is bipartite. Orient every edge from one color class to the other, so \(K_{ee}=2\) and \(K_{ef}=1\) when different edges meet, with all other entries zero. The line graph of a connected tree is connected. Therefore \(K\), and hence the entrywise nonnegative matrix \(M=KA\), is irreducible. Perron--Frobenius gives a simple largest positive eigenvalue \(\Lambda\), with strictly positive eigenvector \(v\). Since \(M\) is similar to symmetric positive definite \(A^{1/2}KA^{1/2}\), all remaining eigenvalues are real and satisfy \(0<\lambda_j<\Lambda\). The normalized left eigenvector is \(w=Av\), so \(w^{\mathsf T}v=1\), \(w^{\mathsf T}M=\Lambda w^{\mathsf T}\).

**2. Exact oddness and cubic coefficient.** The local map is odd and analytic. Expanding the sine gives
\[
 F_h(x)=(I-hM)x+\frac h6M(x^{\circ3})+O(\lVert x\rVert^5).
\]
At \(h_0=2/\Lambda\), its linearization has the simple multiplier \(-1\) in direction \(v\), while all transverse multipliers \(1-2\lambda_j/\Lambda\) lie strictly between \(-1\) and \(1\). The critical multiplier crosses \(-1\) transversely, because its derivative with respect to \(\delta\) is \(-1\). The center-manifold scalar normal form in coordinate \(u=w^{\mathsf T}x\), using oddness and the absence of quadratic terms, is
\[
 u\longmapsto-(1+\delta)u+\kappa u^3+O(\delta u^3+u^5),\qquad
 \kappa=\frac{h_0}6w^{\mathsf T}M(v^{\circ3})
 =\frac13\sum_e a_ev_e^4>0.
\]
The last equality uses \(w^{\mathsf T}M=\Lambda w^{\mathsf T}\) and \(h_0\Lambda=2\). Stable-manifold slaving does not alter the cubic coefficient: its transverse component starts at cubic order, and projection by the left eigenvector annihilates the transverse linear term.

**3. Antipodal two-cycle branch.** The equation \(F_h(x)=-x\) is odd. By the analytic Lyapunov--Schmidt reduction using the simple kernel of \(2I-h_0M\), its reduced nonzero equation reads
\[
 0=-\delta u+\kappa u^3+O(\delta u^3+u^5).
\]
Division by \(u\ne0\), followed by the implicit-function theorem in \(u^2\), gives precisely the two solutions \(u=\pm\sqrt{\delta/\kappa}+O(\delta^{3/2})\) for small \(\delta>0\), and no nonzero local solutions when \(\delta<0\). Their transverse components are \(O(u^3)\), establishing the stated edge profile. They are exchanged by the odd map and have least period two. The standard one-dimensional flip normal form (or the corresponding squared-map reduction) excludes other nearby prime-period-two orbits.

**4. Attraction and sharpness.** Since \(DF_h(-x)=DF_h(x)\), the two-step derivative at either member is \(DF_h(x_\delta)^2\). Perturbing the simple critical eigenvalue,
\[
 \mu_{\mathrm{crit}}=-1-\delta+\frac{h\Lambda}{2}\,u^2\sum_e a_ev_e^4+O(\delta^2)
 =-1+2\delta+O(\delta^2).
\]
Its square is \(1-4\delta+O(\delta^2)\), strictly inside the unit circle for small positive \(\delta\). All other eigenvalues remain inside by continuity and the strict spectral gap. This proves local exponential attraction. For \(h<2/\Lambda\), the fixed-point multipliers \(1-h\lambda_j\) lie in \((-1,1)\), while for \(h>2/\Lambda\) the top multiplier \(1-h\Lambda<-1\); hence the stability boundary is sharp.

## Verification
The standalone file `verify_flip.py` computes the Perron mode of the weighted tree, solves the exact antipodal-cycle equation \(2x-hM\sin x=0\), checks the predicted square-root scaling and calculates all one-step Jacobian eigenvalues. Eight diagnostic instances across four trees (one edge, a weighted path, a weighted star and a weighted branched tree) pass at two distinct small positive values of \(\delta\). These finite calculations corroborate only the algebra and local scaling. The proof is the analytical Perron-mode, Lyapunov--Schmidt and eigenvalue argument above.

## Relationship to prior work
Buescu, D'Aniello and Oliveira, arXiv:2610.10993v1, establish the precise antiphase **fixed-point** stability edge and loss of strict Lyapunov descent at \(h=2/\Lambda\) (Corollary 5.3), as well as almost-everywhere attraction at smaller steps and Morse--Smale properties on special trees. Their Section 5, proof of Corollary 5.3 and conclusions do not study an attracting period-two successor on the other side of this edge. The generic period-doubling theorem is classical and supplies the conceptual reduction, but does not determine the required cubic nondegeneracy and its **strictly positive sign for every weighted tree**. That sign and the explicit Perron-weighted amplitude and multipliers are the contribution asserted here. The tree-wide assertion does not follow merely from a fixed point acquiring multiplier less than \(-1\): a flip can also be subcritical. The classical work on gradient-descent avoidance of strict saddles below the descent step size does not imply post-threshold period-two attraction.

## Limitations
Only local dynamics close to antiphase, for parameters in a small one-sided neighborhood of \(2/\Lambda\), is classified. The neighborhood size depends on the finite weighted tree. Global basins and other distant cycles are not classified. The fixed-point flip on a tree should not be confused with Morse--Smale dynamics of a noninvertible map. No independent mathematical audit or publication-priority certification has occurred.

## References
1. J. Buescu, E. D'Aniello and H. M. Oliveira, *Morse--Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, first posted 2026-10-07, especially Sections 3 and 5 and Corollary 5.3. https://arxiv.org/html/2610.10993v1
2. *Period doubling*, Scholarpedia, generic flip normal form and sign criterion. https://www.scholarpedia.org/article/Period_doubling
3. H. Schaeffer and S. G. McCalla, *Extending the Step-Size Restriction for Gradient Descent to Avoid Strict Saddle Points*, SIAM Journal on Mathematics of Data Science 2 (2020), 1181--1197, arXiv:1908.01753. The theorem concerns precritical strict-saddle avoidance, not the postcritical flip.
