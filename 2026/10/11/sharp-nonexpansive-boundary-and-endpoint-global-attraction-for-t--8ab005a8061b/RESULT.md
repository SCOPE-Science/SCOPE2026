# Sharp nonexpansive boundary and endpoint global attraction for the saturating Ikeda map

## Finding
For the saturating Ikeda map
\[
 F(z)=A+u z\exp\!\left(i\left(\phi-\frac{\eta}{1+|z|^2}\right)\right),
 \qquad z\in\mathbb C,
\]
with complex forcing \(A\), real detuning \(\phi\), nonzero real phase-saturation parameter \(\eta\), and attenuation \(u\ge0\), define
\[
 u_*(\eta)=\sqrt{1+\frac{\eta^2}{16}}-\frac{|\eta|}{4}.
\]
The map is globally Euclidean nonexpansive **exactly** for \(0\le u\le u_*(\eta)\), and globally Lipschitz with a constant strictly less than one **exactly** for \(0\le u<u_*(\eta)\). At the endpoint \(u=u_*(\eta)\) every two distinct points still become strictly closer after one iteration, though no *uniform* one-step contraction constant below one exists. In the entire closed parameter range, there is exactly one fixed point and every initial orbit converges to it. This result is uniform in \(A\) and \(\phi\). For \(\eta=6\) the precise endpoint is \((\sqrt{13}-3)/2\).

## Assumptions and scope
All statements concern the full Euclidean plane identified with \(\mathbb C\); no restriction to a selected attracting basin or an initially bounded region is imposed. The real parameters satisfy \(\eta\ne0\) and \(u\ge0\). Complex input \(A\) and real phase offset \(\phi\) are arbitrary. The case \(\eta=0\), where the endpoint \(u_*=1\) need not have an attracting fixed point, is expressly excluded. Global stability is proved for a sufficient closed region; no instability claim is made above its boundary.

## Proof
Write \(r=|z|\) and \(\theta(r)=\phi-\eta/(1+r^2)\). Away from the origin, use radial/tangential orthonormal frames in source and target. Up to an orthogonal rotation, the real derivative is the shear matrix
\[
 DF_z=u R_{\theta(r)}\begin{pmatrix}1&0\\k(r)&1\end{pmatrix},
 \qquad k(r)=r\theta'(r)=\frac{2\eta r^2}{(1+r^2)^2}.
\]
The singular values of the displayed shear are
\[
 s_\pm(k)=\sqrt{1+k^2/4}\pm |k|/2.
\]
These formulas extend continuously to the origin. Since
\[
 0\le\frac{r^2}{(1+r^2)^2}\le\frac14,
\]
with equality only at \(r=1\), the *exact*, globally attained Euclidean Lipschitz constant is
\[
 L(F)=u\left(\sqrt{1+\eta^2/16}+\frac{|\eta|}4\right).
\]
The equality between the supremum derivative norm and the global Lipschitz constant follows from the fundamental theorem of calculus along straight line segments (upper bound) and differentiation along the maximizing singular vector (lower bound). Thus \(L(F)\le1\) precisely for \(u\le u_*(\eta)\), and \(L(F)<1\) precisely below it; above it the derivative expands some tangent vector at \(|z|=1\), excluding Euclidean nonexpansiveness.

At the endpoint the norm \(\|DF_z\|=1\) holds exactly when \(|z|=1\); at all other points it is strictly below one. For any distinct \(z,w\), their connecting line segment intersects the unit circle at no more than two points. Integrating the derivative along that segment therefore gives
\[
 |F(z)-F(w)|<|z-w|,
\]
a strict *pairwise* decrease even though \(L(F)=1\).

Because \(\eta\ne0\), \(u_*(\eta)<1\). Every orbit is bounded: \(|F(z)|\le |A|+u|z|\), hence \(|F^n(z)|\le u^n|z|+|A|/(1-u)\). A closed disk centered at zero of radius strictly exceeding \(|A|/(1-u)\) is forward invariant, and Brouwer's theorem provides at least one fixed point. Pairwise strict contractivity at the endpoint, and strict uniform contraction in the interior, gives uniqueness. For arbitrary initial \(z\), the distances \(|F^n(z)-z_*|\) decrease to a limit \(\ell\ge0\); the orbit is precompact. If \(\ell>0\), take a convergent subsequence of states to \(w\ne z_*\); continuity and strict distance decrease imply \(|F(w)-z_*|<|w-z_*|=\ell\), contradicting convergence of the distance sequence to \(\ell\). Therefore \(\ell=0\), proving global attraction even at the nonuniform endpoint.

## Verification
The standalone Python/SymPy checker `check_ikeda.py` reconstructs the shear trace/determinant, the exact location of the radial maximum, the reciprocal threshold identity, and the exact \(\eta=6\) value. The global nonexpansiveness and endpoint convergence rely on the complete analytic argument above, not numerical experiments. All calculations hold uniformly over the full unbounded plane.

## Relationship to prior work
The Ikeda optical cavity map originated in Ikeda's 1979 work and its 1980 development with Daido and Akimoto. The later exact saturating-phase planar form is standard in dynamical illustrations of the model. This finding isolates the exact Euclidean nonexpansiveness frontier and the qualitative endpoint attraction, rather than locating particular bifurcations or computing stationary distributions. Hansson–Wabnitz (2015) analyze cavity multistability and linearized stationary stability for a non-saturating Kerr roundtrip phase, so those calculations do not imply the global boundary here. The Ikeda case treated by Fortunato–Kurizki–Schleich (1998) concerns active stabilization by measurement/interference; its available abstract does not establish the present unconditional global frontier. These comparisons do not establish absolute novelty against all historical material.

## Limitations
The boundary is *sharp for Euclidean nonexpansiveness*, not known to be the boundary of uniqueness or global attraction. A derivative singular norm of one at the endpoint does not preclude an orbit-dependent exponential rate, but no uniform single-step Euclidean contraction factor below one exists there. The linear/unsaturated phase model is not addressed. Some older relevant full papers could not be inspected in full, so unnoticed equivalent statements remain a literature risk. No independent audit was performed.

## References
1. K. Ikeda, "Multiple-valued stationary state and its instability of the transmitted light by a ring cavity system," *Optics Communications* 30 (1979), 257–261. DOI: 10.1016/0030-4018(79)90090-7.
2. K. Ikeda, H. Daido and O. Akimoto, "Optical Turbulence: Chaotic Behavior of Transmitted Light from a Ring Cavity," *Physical Review Letters* 45 (1980), 709–712. DOI: 10.1103/PhysRevLett.45.709.
3. M. Fortunato, G. Kurizki and W. P. Schleich, "Stabilization of Deterministically Chaotic Systems by Interference and Quantum Measurements: The Ikeda Map Case," *Physical Review Letters* 80 (1998), 5730. arXiv:quant-ph/9808048.
4. T. Hansson and S. Wabnitz, "Frequency comb generation beyond the Lugiato-Lefever equation: multi-stability and super cavity solitons," arXiv:1503.03274 (2015), sections II–V (full lawful open HTML).
