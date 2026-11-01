# A sharp two-orbit frequency-mismatch floor for conditioned planar flow conjugacies

## Finding
Let \(f:\mathbb R^2\to\mathbb R^2\) be a \(C^1\) vector field possessing two distinct simple periodic trajectories \(\Gamma_1,\Gamma_2\) enclosing the origin. For each \(i\in\{1,2\}\), denote its primitive positive period by \(T_i\), orientation index about the origin by \(\nu_i\in\{-1,1\}\), minimum distance to the origin by \(r_i=\min_{x\in\Gamma_i}|x|>0\), and signed angular frequency by \(\omega_i=2\pi\nu_i/T_i\).

Fix any \(C^1\) diffeomorphism \(F:\mathbb R^2\to\mathbb R^2\) with \(F(0)=0\) and global metric bounds \(m|x-y|\le |F(x)-F(y)|\le M|x-y|\) for some \(0<m\le M\). Write \(J(x_1,x_2)=(-x_2,x_1)\). For any fixed angular reference speed \(\Omega\in\mathbb R\), the pulled-back rotational reference vector field is \(f_{F,\Omega}(x)=DF(x)^{-1}\Omega JF(x)\). Then the uniform model discrepancy on the two target orbits obeys
\[
\boxed{\max_{x\in\Gamma_1\cup\Gamma_2}|f(x)-f_{F,\Omega}(x)|\ \ge\ \frac{m}{M}\frac{r_1r_2}{r_1+r_2}|\omega_1-\omega_2|.}
\]
The numerical coefficient is optimal even within smooth polynomial vector fields and isometrically conditioned transformations. Specifically, \(f(x)=(1+|x|^2)Jx\), the circles of radii \(1\) and \(2\), \(F=\operatorname{id}\) and \(\Omega=4\) yield equality, with both sides exactly \(2\).

## Assumptions and scope
The trajectories are ordinary nonconstant periodic solutions of a \(C^1\) planar autonomous ODE, their geometric traces are simple Jordan curves surrounding \(0\), and their periods are primitive. Neither monotonicity of the physical polar angle nor radial symmetry of \(f\) is required. The transformation is a global \(C^1\) diffeomorphism that fixes \(0\), with explicit finite positive lower and upper metric constants. The residual is evaluated only on the two specified true periodic trajectories; the reference is a single constant-speed planar rotation, not an action-dependent angular flow. If the two signed frequencies coincide, the stated lower bound is zero and is not claimed to be informative.

## Proof
Parametrize each orbit by its true trajectory \(x_i(t)\), \(0\le t\le T_i\), and set \(y_i(t)=F(x_i(t))\). As \(F\) is a homeomorphism of the plane fixing the origin, \(y_i\) is again a Jordan curve enclosing the origin. The sign \(s=\operatorname{sgn}\det DF\in\{-1,1\}\) is constant throughout the connected plane. The winding number of \(y_i\) about \(0\) is therefore \(s\nu_i\). This same sign applies to both orbits.

The defining equation for \(f_{F,\Omega}\) gives
\[
\dot y_i(t)=DF(x_i(t))f(x_i(t))=\Omega Jy_i(t)+DF(x_i(t))[f(x_i(t))-f_{F,\Omega}(x_i(t))].
\]
The continuous angular lift along \(y_i\) has derivative \(\dot\vartheta_i=(Jy_i\cdot\dot y_i)/|y_i|^2\). Consequently,
\[
\dot\vartheta_i-\Omega=\frac{Jy_i\cdot DF(x_i)[f(x_i)-f_{F,\Omega}(x_i)]}{|y_i|^2}.
\]
If \(\varepsilon\) denotes the supremum in the displayed finding, the differential bound \(\|DF\|\le M\), together with \(|y_i(t)|=|F(x_i(t))-F(0)|\ge m|x_i(t)|\ge mr_i\), yields \(|\dot\vartheta_i-\Omega|\le M\varepsilon/(mr_i)\). Integrating over one primitive period and using \(\vartheta_i(T_i)-\vartheta_i(0)=2\pi s\nu_i\) proves
\[
|s\omega_i-\Omega|\le \frac{M\varepsilon}{mr_i},\qquad i=1,2.
\]
The triangle inequality now gives \(|\omega_1-\omega_2|=|s\omega_1-s\omega_2|\le(M\varepsilon/m)(1/r_1+1/r_2)\). Rearrangement gives the claimed bound. No periodic-orbit perturbation, compactness limit, or numerical extrapolation is used.

For sharpness, take \(f(x)=(1+|x|^2)Jx\). Its circle of radius \(r\) rotates with angular frequency \(1+r^2\). Therefore the radii \(1\) and \(2\) have respective signed frequencies \(2\) and \(5\). When \(F\) is the identity and \(\Omega=4\), the discrepancy is \(|2-4|\cdot1=2\) on the first circle and \(|5-4|\cdot2=2\) on the second. The formula gives \((1\cdot2/(1+2))|2-5|=2\). Thus the coefficient cannot increase uniformly in this class. The example also shows that minimizing over the reference angular speed does not remove the positive discrepancy.

## Verification
The accompanying self-contained standard-library program `verify.py` checks the exact rational constants for the sharp example; independently evaluates the two-radius minimax objective on rational frequency candidates; and checks a diagonally anisotropic linear transformation's directly calculated orbitwise supremum against the theorem's weaker conditioned bound. These finite checks support the explicit example only: the universal statement follows from the winding-number integration and metric estimates in the proof. The full proof is executable by hand from the formulas above without auxiliary data.

## Relationship to prior work
He (2026), Proposition 6 and Remarks 7–8, establishes exact preservation of periods and frequency–amplitude relations by time-preserving smooth conjugacies and explains the necessity of learnable reference invariants. That exact qualitative obstruction does not, by itself, give the positive condition-number-dependent residual floor above. The present statement quantifies the unavoidable error of a fixed-frequency reference on two observed cycles and proves sharpness in an explicit polynomial family. Bizzi, Nissenbaum and Pereira (2024 preprint; 2025 proceedings) establish architecture and flow structure for neural conjugate flows, but the inspected text does not give this two-orbit uniform vector-field residual bound. Classical winding-number invariance supplies the main topological step and is not asserted as new.

## Limitations
This is a theorem about a uniform generator/vector-field discrepancy on *two exact periodic orbits* with a specified global bi-Lipschitz condition number. It is not a lower bound for pointwise interpolation loss on a finite training sample, for integral loss under an arbitrary sampling distribution, for general action-dependent angular references, or for transformations whose lower metric constant degenerates. The universal coefficient is proved optimal at \(m=M=1\); optimality for each prescribed ratio \(m/M<1\) is not claimed. The theorem does not establish novelty over every historical result in rotation-number stability or approximate conjugacy; an independently performed literature audit remains open.

## References
1. Andrew Qing He, *Neural Vector Field Transformations: Learning the Flow of Autonomous Systems by Conjugation to Explicitly Integrable Reference Flows*, arXiv:2610.29039v1 (first public October 21, 2026), especially Section 2, Proposition 6, and Section 3. https://arxiv.org/abs/2610.29039
2. Arthur Bizzi, Lucas Nissenbaum and João M. Pereira, *Neural Conjugate Flows: Physics-Informed Architectures with Flow Structure*, arXiv:2411.08326v1 (November 13, 2024), later *Proceedings of the AAAI Conference on Artificial Intelligence* 39(15) (2025), 15576–15586. https://arxiv.org/abs/2411.08326 ; https://doi.org/10.1609/aaai.v39i15.33710
3. Christoph Kawan and Torben Stender, *Lipschitz conjugacy of linear flows*, *Journal of the London Mathematical Society* 80 (2009), 699–715, doi:10.1112/jlms/jdp034 (background on exact Lipschitz conjugacy of linear flows; not a claimed source for the new estimate).
