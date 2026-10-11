# Limit-cycle-only phase data do not identify the full phase response curve
## Finding
For fixed \(\lambda>0\) and \(\omega>0\), consider the one-parameter family of smooth polynomial planar systems
\[
\dot x=\lambda(1-r^2)x-[\omega+c(1-r^2)]y,
\qquad
\dot y=[\omega+c(1-r^2)]x+\lambda(1-r^2)y,
\qquad r^2=x^2+y^2,
\]
where \(c\in\mathbb R\). Every member of the family has the same hyperbolically attracting unit circle, the same parametrized motion on that circle, and the same vector-field values there. In polar coordinates,
\[
\dot r=\lambda r(1-r^2),\qquad
\dot\theta=\omega+c(1-r^2),
\]
so on \(r=1\) one has \(\dot r=0\) and \(\dot\theta=\omega\), independently of \(c\).

Nevertheless the exact asymptotic phase on the basin \(r>0\) is
\[
\Phi_c(r,\theta)=\theta-\frac{c}{\lambda}\log r\pmod{2\pi},
\]
and therefore the phase response curve on the unit circle is
\[
Z_c(\theta)=(-\sin\theta,\cos\theta)-\frac{c}{\lambda}(\cos\theta,\sin\theta).
\]
The tangential component is fixed, while the radial component is \(-c/\lambda\) and can take any real value. Consequently, data restricted to the limit cycle—even exact continuous state data with exact velocities and exact phase labels—do not identify the full phase response curve or the transverse extension of asymptotic phase.

This also gives a direct identifiability obstruction for learning a vector field from a single periodic orbit. All systems above fit the same orbit and its velocity with zero error, yet their transverse dynamics and phase response curves differ. Hence zero training error on one limit-cycle trajectory cannot, by ODE uniqueness alone, imply convergence of a learned vector field to the true vector field in any neighborhood of that trajectory.

## Assumptions and scope
The claim concerns scientific identifiability from data whose support is exactly one stable limit cycle. The observed information may include the complete parametrized orbit, arbitrarily dense timestamps, exact velocities on the orbit, and the constant-speed phase labels. The impossibility remains because all of those observables are identical throughout the family above.

The conclusion is about the full vector phase response curve, equivalently the gradient of asymptotic phase on the cycle. The tangential normalization is identifiable: every member satisfies
\[
Z_c(\theta)\cdot F(\chi(\theta))=\omega.
\]
What is not identified is the transverse component. The theorem does not say that a neural network cannot select a useful phase response curve in practice; it says that such a selection is not uniquely determined by limit-cycle-only data without additional assumptions or information.

## Proof
Write the vector field in polar form. Direct substitution gives
\[
\dot r=\lambda r(1-r^2),\qquad
\dot\theta=\omega+c(1-r^2).
\]
At \(r=1\), the radial derivative of \(\lambda r(1-r^2)\) is \(-2\lambda<0\), so the unit circle is hyperbolically attracting. Its trajectory is
\[
\chi(t)=(\cos(\theta_0+\omega t),\sin(\theta_0+\omega t)),
\]
which is independent of \(c\). The Cartesian vector field restricted to the unit circle is likewise independent of \(c\).

For \(r>0\), define
\[
\Phi_c(r,\theta)=\theta-\frac{c}{\lambda}\log r.
\]
Along every trajectory in the basin except the repelling origin,
\[
\frac{d}{dt}\Phi_c
=\omega+c(1-r^2)-\frac{c}{\lambda}\frac{\dot r}{r}
=\omega+c(1-r^2)-c(1-r^2)
=\omega.
\]
Thus \(\Phi_c\) is an asymptotic phase function. On \(r=1\), all members restrict to the same phase \(\Phi_c(1,\theta)=\theta\).

Using \(\nabla\theta=(-\sin\theta,\cos\theta)/r\) and \(\nabla\log r=(\cos\theta,\sin\theta)/r\), evaluation at \(r=1\) gives
\[
Z_c(\theta)=\nabla\Phi_c|_{r=1}
=(-\sin\theta,\cos\theta)-\frac{c}{\lambda}(\cos\theta,\sin\theta).
\]
Therefore distinct values of \(c\) give identical on-cycle states and velocities but different phase response curves. Since a zero-loss learner fed only those on-cycle observations cannot distinguish the members of this family, the true transverse phase gradient and neighboring vector field are not identifiable from those observations alone.

## Verification
The proof is analytic and requires no finite experiment. Three checks are decisive. First, the polynomial Cartesian equations reduce exactly to the stated polar equations. Second, differentiating \(\Phi_c\) along the flow gives the constant \(\omega\) identically. Third, the phase-response formula follows by an elementary gradient calculation and visibly changes with \(c\) only in the radial direction.

The construction also stress-tests the strongest natural version of the data claim: knowing the entire orbit continuously and knowing \(F\) exactly at every point of that orbit still leaves \(c\) completely unconstrained. Increasing the sampling density cannot remove this ambiguity.

## Relationship to prior work
Zhang et al. formulate a phase-learning loss using the pointwise constraint \(\nabla\phi\cdot F=\omega\) on limit-cycle samples and emphasize that their main first step does not require off-cycle samples. They explicitly note that the main training procedure does not constrain transversal gradients, yet use the learned gradient as a phase response curve. Their supplementary Neural-ODE extension further states that a candidate vector field is expected to converge to the underlying dynamics when the trajectory-fitting loss goes to zero. The family above shows that these on-cycle conditions do not provide identifiability: infinitely many smooth vector fields have exactly the same zero-loss on-cycle data but different transverse phase gradients.

The same paper also recognizes that limit-cycle samples are insufficient for direct numerical recovery of transverse Jacobian variations and proposes an adjoint-regularized extension. The present result sharpens that observation into an exact impossibility statement for the full phase response curve under limit-cycle-only information.

Yawata, Fukami, Taira, and Nakao's earlier phase-autoencoder method uses off-cycle training trajectories. In their Stuart–Landau tests, the initial states are randomly displaced from the cycle, and they report that setting the displacement parameter to zero makes accurate phase and phase-sensitivity estimation difficult. Their Stuart–Landau example also uses the familiar logarithmic phase geometry. That work is consistent with, rather than equivalent to, the exact non-identifiability theorem here.

## Limitations
The theorem does not assert that the focal machine-learning method necessarily returns an incorrect phase response curve on its tested examples. Architectural bias, regularization, favorable model classes, or implicit information from training can select a curve that happens to be accurate. The theorem only excludes universal identification from data supported solely on the periodic orbit.

Additional information can remove the ambiguity. Examples include off-cycle trajectories, the Jacobian of the vector field along the cycle together with the adjoint equation, controlled transverse perturbations with measured phase shifts, or a justified parametric model class that fixes the transverse dynamics.

## References
1. Jingdong Zhang, Luan Yang, Murilo S. Baptista, Zefeng Zhang, Qunxi Zhu, Wei Lin, and Celso Grebogi, “Ptolemy’s Equant Equates to a Universal Dynamical Clock via Machine Learning,” arXiv:2607.15472v1, first submitted 2026-07-16.
2. Koichiro Yawata, Kai Fukami, Kunihiko Taira, and Hiroya Nakao, “Phase autoencoder for limit-cycle oscillators,” *Chaos* 34, 063111 (2024), doi:10.1063/5.0205718; arXiv:2403.06992v1.
