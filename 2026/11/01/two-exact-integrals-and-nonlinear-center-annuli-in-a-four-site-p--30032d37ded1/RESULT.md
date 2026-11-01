# Two exact integrals and nonlinear center annuli in a four-site phase-lag ring

## Finding

The smallest four-vertex cycle has an exact integrability phenomenon at every **strictly positive but sub-quadrature phase lag**. For the stated nearest-neighbor Sakaguchi flow on four phases, there is an invariant lifted phase-difference cell on which two explicit, generically independent conserved quantities exist. The cell has a branching set of equilibria and an interval of nonlinear, neutrally periodic relative-phase motions, not just a linearly oscillatory approximation.

More precisely, for every fixed \(0<\alpha<\pi/2\), introduce coordinates \((v,z,\phi)\in(0,\pi)^3\) as in the next section. Then
\[
H=\log\frac{\sin v\sin z}{\sin\phi},\qquad
J=\log\frac{\sin v}{\sin z}+\phi\tan\alpha
\]
are conserved; their gradients are independent wherever the reduced vector field is nonzero. Every central equilibrium \((\pi/2,\pi/2,\phi_0)\) with
\[
\frac{\pi}{2}-\alpha<\phi_0<\frac{\pi}{2}+\alpha
\]
has a local annulus of nonconstant periodic **relative-phase** trajectories on its fixed-\(J\) leaf. Their periods approach
\[
\boxed{T_0(\alpha,\phi_0)=\frac{\pi}{\sqrt{\sin^2\alpha-\cos^2\phi_0}}}
\]
as they approach the equilibrium. Outside the closed interval, the central equilibrium has a real normal saddle pair; at its endpoints the normal linearization is double-zero.

## Assumptions and scope

Take four real phase lifts \(\theta_0,\theta_1,\theta_2,\theta_3\) evolving on a cyclic graph with indices modulo four and physical time normalization
\[
\dot\theta_j=\sin(\theta_{j-1}-\theta_j+\alpha)+\sin(\theta_{j+1}-\theta_j+\alpha),\quad 0<\alpha<\pi/2.
\]
Eliminate common phase using the invertible real-linear change
\[
\theta_0=u+v,\quad\theta_2=u-v,\quad\theta_1=w+z,\quad\theta_3=w-z,\quad\phi=w-u.
\]
Work with a chosen lift satisfying \(0<v,z,\phi<\pi\). The statements refer to this open, invariant three-dimensional cell of **lifts**, and do not claim a single-valued globally smooth first integral over the entire phase torus. Local phase-difference periodicity means periodicity in \((v,z,\phi)\) modulo common rotation: the four absolute phases can retain an accumulated common drift.

## Proof

**1. Exact reduction and invariant domain.** Since the two neighbors of each even site are precisely the two odd sites, elementary sine addition and subtraction yield
\[
\begin{aligned}
\dot v&=-2\sin v\cos z\cos(\phi+\alpha),\\
\dot z&=-2\sin z\cos v\cos(\alpha-\phi),\\
\dot\phi&=-4\cos\alpha\sin\phi\cos v\cos z.
\end{aligned}
\]
Each component has the corresponding factor \(\sin v\), \(\sin z\), or \(\sin\phi\), and the remaining factors are bounded and smooth. The scalar differential inequality for the logarithm of distance to either face therefore prevents a solution starting strictly inside \((0,\pi)^3\) from crossing a face in finite time. Since the original angular vector field is smooth and bounded, the cell is invariant for all finite positive and negative times.

**2. Two first integrals and independence.** Differentiating the first function along this vector field gives
\[
\begin{aligned}
\dot H&= -2\cos v\cos z\bigl[\cos(\phi+\alpha)+\cos(\alpha-\phi)\bigr]
+4\cos\alpha\cos\phi\cos v\cos z=0.
\end{aligned}
\]
Similarly,
\[
\dot J=-2\cos v\cos z\bigl[\cos(\phi+\alpha)-\cos(\alpha-\phi)\bigr]
-4\sin\alpha\sin\phi\cos v\cos z=0.
\]
Here we used the elementary sum and difference formulas for cosine and \(\tan\alpha\cos\alpha=\sin\alpha\). Direct componentwise differentiation also gives the precise identity
\[
\boxed{F=2\cos\alpha\sin\phi\sin v\sin z\ (\nabla H\times\nabla J),}
\]
where the gradient uses coordinate order \((v,z,\phi)\). The multiplier is strictly positive in the open cell; therefore \(\nabla H\) and \(\nabla J\) are independent at every non-equilibrium point. Such points form a dense open subset, proving genuine local complete integrability. Equivalently, the flow preserves the explicit smooth measure with density proportional to \((\sin v\sin z)^{-2}\) relative to \(dv\,dz\,d\phi\); this auxiliary identity can be checked by its divergence and is not needed for periodicity.

**3. Exhaustive equilibrium geometry.** Because \(\sin\phi>0\) and \(\cos\alpha>0\), an equilibrium must have \(\cos v\cos z=0\). If both cosines vanish then all three derivatives vanish, giving \(v=z=\pi/2\) with \(\phi\) arbitrary in \((0,\pi)\). If just \(\cos v=0\), the first equation vanishes only when \(\cos(\phi+\alpha)=0\), hence \(\phi=\pi/2-\alpha\) within the cell; \(z\) is arbitrary. If just \(\cos z=0\), the second equation vanishes only when \(\cos(\alpha-\phi)=0\), hence \(\phi=\pi/2+\alpha\) with arbitrary \(v\). Thus all equilibria are exactly
\[
\begin{aligned}
\mathcal E_0&=\{v=z=\pi/2,\ 0<\phi<\pi\},\\
\mathcal E_-&=\{v=\pi/2,\ \phi=\pi/2-\alpha,\ 0<z<\pi\},\\
\mathcal E_+&=\{z=\pi/2,\ \phi=\pi/2+\alpha,\ 0<v<\pi\}.
\end{aligned}
\]
These line segments meet pairwise only at the respective two points on \(\mathcal E_0\).

**4. Exact normal-type transition.** The Jacobian at \((\pi/2,\pi/2,\phi_0)\) is
\[
DF=\begin{pmatrix}0&2\cos(\phi_0+\alpha)&0\\2\cos(\alpha-\phi_0)&0&0\\0&0&0\end{pmatrix}.
\]
Thus the normal pair obeys
\[
\lambda_\pm^2=4\cos(\phi_0+\alpha)\cos(\alpha-\phi_0)
=4(\cos^2\phi_0-\sin^2\alpha).
\]
This is a real saddle pair when the last expression is positive, an imaginary pair when negative, and a zero pair when it vanishes. The remaining eigenvalue is always zero, tangent to the equilibrium line. We make no nonlinear classification at the two degenerate junctions.

**5. Genuine nonlinear periodic annuli.** Fix \(\phi_0\) strictly in the elliptic interval, and set \(J_0=\phi_0\tan\alpha\). Because \(\partial J/\partial\phi=\tan\alpha>0\), the implicit function theorem makes \(J=J_0\) a smooth two-dimensional graph through the equilibrium, indeed with the explicit local expression
\[
\phi=\phi_0+\frac{\log\sin z-\log\sin v}{\tan\alpha}.
\]
Writing \(x=v-\pi/2\) and \(y=z-\pi/2\), elementary Taylor expansion of this expression gives
\[
\phi=\phi_0+\frac{x^2-y^2}{2\tan\alpha}+O((x^2+y^2)^2).
\]
On this graph the other first integral has the expansion
\[
H-H_0=-\frac12\left[\left(1+\cot\phi_0\cot\alpha\right)x^2
+\left(1-\cot\phi_0\cot\alpha\right)y^2\right]
+O((x^2+y^2)^2),
\]
where \(H_0=-\log\sin\phi_0\). Both quadratic coefficients are strictly positive exactly when \(|\cos\phi_0|<\sin\alpha\). Hence the restriction of \(H\) to \(J=J_0\) has a strict nondegenerate local maximum at the equilibrium. The Morse lemma makes all sufficiently small levels \(H=H_0-\epsilon\), \(\epsilon>0\), smooth embedded closed curves encircling it. No such level contains an equilibrium: the central equilibrium is isolated on the fixed-\(J\) surface in a sufficiently small neighborhood, and the other equilibrium segments are a positive distance away. The smooth autonomous nonzero vector field on each invariant compact circle is therefore periodic, giving the claimed genuine nonlinear family.

As the circles shrink, the vector field converges after linear scaling to its normal oscillator with frequency \(\omega_0=2\sqrt{\sin^2\alpha-\cos^2\phi_0}\). Standard smooth center-period continuity, or linearizing the flow in the local Morse coordinates and integrating over one turn, gives \(T\to2\pi/\omega_0\), the displayed limit. This proves all quantified claims for every \(0<\alpha<\pi/2\) and every admissible \(\phi_0\).

## Verification

The accompanying standalone `verify.py` checks, with SymPy, both first-integral derivatives, the exact cross-product multiplier, and the central Jacobian. It also reconstructs the reduced dynamics independently from the original four-phase equations for 280 reproducibly seeded interior configurations, checks conservation derivatives, and verifies the normal-type inequality. Execute with `python verify.py` using SymPy and NumPy. All assertions passed on the supplied artifact. These finite checks corroborate the exact identities; the existence of a periodic annulus follows from the analytical level-set and Morse-lemma argument, not from numerical integrations.

## Relationship to prior work

Yan, Ozawa, Kori, and Sato (2026) study winding-state stability, basin metamorphosis, and high-dimensional ring dynamics for precisely the same nearest-neighbor phase-lag equation. Their full text and end matter analyze mostly larger networks (notably sizes five and eighty) and do not derive these four-site logarithmic integrals or the nonlinear fixed-leaf center annuli. The Nambu representation and the exact three-branch equilibrium diagram are additional consequences of the four-site bipartite geometry.

Thibeault, Claveau, Allard, and Desrosiers (2025) already identify nontrivial constants of motion in Kuramoto networks, including an opposite-pair sine ratio in zero-lag bipartite examples. We credit that discovery. Their stated sufficient conditions involving oppositely directed phase lags or special incoming-edge symmetries do not establish the present equal positive directed phase-lag equation: the same \(\alpha>0\) is used in both directions here. The present two-integral formula and the strictly positive-lag nonlinear center foliation are not implied by that zero-lag ratio alone.

Ashwin, Bick, and Burylko (2016) treat general coupling on permutation-symmetric all-to-all networks; Ashwin and Burylko (2015) examine minimal weak-chimera motifs with a different coupling architecture. Those are not the equal-weight four-cycle dynamics of this theorem. Absence of an equivalent theorem from inspected sources is evidence for provisional originality, not proof of historical uniqueness.

## Limitations

The integrals are local to the stated invariant lifted cell and become singular at its boundary; no globally defined pair of first integrals on the full torus is asserted. The phase-difference periodic orbits can have common-phase drift. The two junction equilibria with zero normal eigenvalues are not classified beyond their linearization. This is special to the four-site bipartite ring and does not imply integrability for larger rings, arbitrary natural frequencies, or the endpoint \(\alpha=\pi/2\). Historical priority against all specialized phase-network literature remains subject to further independent review.

## References

1. J. Yan, A. Ozawa, H. Kori, and Y. Sato, *Basin Metamorphosis in Coupled Phase Oscillators*, arXiv:2603.02135, first submitted 2026-03-02, version 2 dated 2026-07-09. https://arxiv.org/html/2603.02135v2
2. V. Thibeault, B. Claveau, A. Allard, and P. Desrosiers, *Kuramoto meets Koopman: Constants of motion, symmetries, and network motifs*, arXiv:2504.06248 (2025). https://arxiv.org/abs/2504.06248
3. P. Ashwin, C. Bick, and O. Burylko, *Identical Phase Oscillator Networks: Bifurcations, Symmetry and Reversibility for Generalized Coupling*, Frontiers in Applied Mathematics and Statistics 2:7 (2016). https://doi.org/10.3389/fams.2016.00007
4. P. Ashwin and O. Burylko, *Weak chimeras in minimal networks of coupled phase oscillators*, Chaos 25, 013106 (2015); arXiv:1407.8070. https://arxiv.org/abs/1407.8070
