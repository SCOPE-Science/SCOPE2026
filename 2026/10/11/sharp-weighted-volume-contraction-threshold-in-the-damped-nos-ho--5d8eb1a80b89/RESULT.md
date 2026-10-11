# Sharp weighted-volume contraction threshold in the damped Nosé–Hoover oscillator

## Finding
For \(a>0\) and \(b>0\), consider
\[
\dot x=y-bx,\qquad \dot y=yz-x,\qquad \dot z=a-y^2.
\]
Define
\[
\Psi(x,y,z)=\frac{-x^2+y^2+z^2}{2a}-\frac{z}{ab},
\qquad w(x,y,z)=e^{-\Psi(x,y,z)}.
\]
The weighted divergence of the vector field with respect to the strictly positive smooth volume density \(w\,dx\,dy\,dz\) is exactly
\[
\boxed{\operatorname{div}_{w}F=\frac1b-b-\frac{(y-bx)^2}{ab}.}
\]
Thus \(b=1\) is the **sharp universal weighted-volume nonexpansion boundary** on the entire phase space. For \(b>1\), every material region along an existing flow segment loses weighted volume at least exponentially at rate \(b-1/b\); at \(b=1\) it is nonexpanding. If \(0<b<1\), the weighted divergence is positive at both equilibria, so universal nonexpansion is impossible. The stated exponential rate is attained infinitesimally at either equilibrium and cannot be strengthened uniformly.

Every compactly supported invariant Borel probability measure \(\mu\) satisfies the exact sharp identity
\[
\boxed{\int(z-b)\,d\mu=\frac1b-b-\frac1{ab}\int(y-bx)^2\,d\mu\leq\frac1b-b.}
\]
Equality holds **if and only if** \(\mu\) is an arbitrary probability mixture of the two equilibria \(E_\pm=(\pm\sqrt a/b,\pm\sqrt a,1/b)\). In particular every other compactly supported ergodic invariant probability has strict inequality. For an ergodic such measure, the left-hand side is the sum of its three Lyapunov exponents, counting multiplicity. Accordingly the sign of the maximal possible ergodic Lyapunov sum is negative for \(b>1\), zero for \(b=1\), and positive for \(0<b<1\).

## Assumptions and scope
The parameters are real with \(a>0\), \(b>0\). The equations define a polynomial smooth local flow \(\phi_t\); a statement about arbitrary initial conditions only concerns times for which solutions exist. The weighted volume density is globally positive but need **not** have finite total mass on unbounded space. Compact invariance means invariant under the complete flow on the compact set. Lyapunov-sum statements concern compactly supported ergodic invariant Borel probabilities; no ergodicity or boundedness assertion is made for general trajectories.

## Proof
The usual Euclidean divergence is \(\operatorname{div}F=z-b\). Direct differentiation and cancellation of the cubic terms give
\[
\begin{aligned}
\frac{d}{dt}\Psi
&=\frac{-x(y-bx)+y(yz-x)+z(a-y^2)}a-\frac{a-y^2}{ab}\\
&=z-\frac1b+\frac{(y-bx)^2}{ab}.
\end{aligned}
\]
Since \(\operatorname{div}_{w}F=\operatorname{div}F+F\cdot\nabla\log w=z-b-\dot\Psi\), the boxed pointwise identity follows. For a measurable material region with finite weighted volume, the transport/Jacobian formula and the pointwise inequality imply nonexpansion for \(b=1\) and contraction by \(e^{-(b-1/b)t}\) for \(b>1\), while solutions exist.

More precisely, Liouville's identity and the preceding coboundary yield for every solution segment
\[
\det D\phi_t(p)=\exp\!\left[\left(\frac1b-b\right)t-\frac1{ab}\int_0^t(y(s)-bx(s))^2\,ds
+\Psi(\phi_t(p))-\Psi(p)\right].
\]
If \(K\) is a compact invariant set and \(M_K=\sup_{p\in K}|\Psi(p)|\), then for all \(p\in K\) and \(t\geq0\),
\[
0<\det D\phi_t(p)\leq e^{2M_K}e^{-(b-1/b)t}\quad(b>1).
\]
This is Euclidean phase-volume contraction in the asymptotic exponential sense, rather than pointwise negative Euclidean divergence. The stationary points of the vector field are exactly \(E_+\) and \(E_-\), and there \(y-bx=0\). Their instantaneous Euclidean divergence is \(1/b-b\). Since it is also their constant-time Jacobian growth rate, the exponential rate and the \(b=1\) threshold are sharp.

For invariant compactly supported \(\mu\), integrate the identity for \(\dot\Psi\) against \(\mu\). Smoothness and compact support allow differentiation under the invariant integral, giving \(\int\dot\Psi\,d\mu=0\). This proves the boxed stationary identity. If equality holds, nonnegativity gives \(\dot x=y-bx=0\) for \(\mu\)-almost every point. Invariance at all rational times and continuity imply for almost every initial point that \(\dot x(t)=0\) at **all real times** on its complete orbit. Hence \(x(t)=X\) is constant, \(y(t)=bX\) is constant, and \(0=\dot y=X(bz-1)\). If \(X=0\), then \(x=y=0\) and \(\dot z=a>0\), so this complete orbit is unbounded and cannot belong to compact support. Thus \(X\ne0\), so \(z=1/b\); finally \(\dot z=a-b^2X^2=0\) forces \(X=\pm\sqrt a/b\). Therefore the invariant measure is supported on \(\{E_+,E_-\}\). Conversely all mixtures of their Dirac masses attain equality.

For an ergodic compactly supported measure, the multiplicative ergodic theorem and Liouville's formula imply that the sum of three Lyapunov exponents is \(\int\operatorname{div}F\,d\mu\). The stationary identity then supplies its sharp upper bound. A Dirac mass at an equilibrium attains the bound for every \(a,b>0\), including a positive value whenever \(0<b<1\); hence the sign-change boundary cannot be improved.

## Verification
The standalone `proof_check.py` reconstitutes the vector field, checks the differential coboundary and weighted-divergence identities as exact rational symbolic expressions, solves the equilibrium equations under \(a,b>0\), checks the equilibrium divergence, and checks the characteristic polynomial. This verifies algebraic premises; the invariant-measure equality case and uniform bounds are justified analytically above, not inferred from finite experiments or script output.

## Relationship to prior work
Sprott's 2014 article introduces this exact two-parameter damped oscillator in its Eq. (6) and reports attractor-merging behavior near \(b=1.06\) at \(a=1\). Munmuangsaen and coauthors' 2015 study, Eq. (2), examines the same system by numerical Lyapunov spectra, bifurcation regions, and adjustable attractor dimension, including the state-dependent Euclidean divergence \(z-b\). Those published computations do not state the globally exact weighted-divergence conjugacy, the sharp \(b=1\) universal contraction boundary, or equality classification for all compact stationary states. A 2022 related quadratic-oscillator study analyzes different damping placements, not this cohomological identity. The distinction is substantive: the displayed Euclidean divergence \(z-b\) itself changes sign over state space, while the explicitly weighted divergence has a parameter-controlled definite sign for every state when \(b\geq1\).

## Limitations
No global boundedness, compact-attractor existence, invariant probability uniqueness, or trajectory-wise positivity of Lyapunov exponents is claimed. The smooth weighted density generally has infinite mass on the full noncompact phase space. A pointwise Euclidean divergence bound is **not** claimed: Euclidean contraction follows along compact invariant sets only after bounding the coboundary. The sharpness witnesses are equilibrium measures, not asserted chaotic attractors. Literature comparisons support but cannot prove absolute novelty, and no independent audit has been performed.

## References
1. J. C. Sprott, “Simplest Chaotic Flows with Involutional Symmetries,” *International Journal of Bifurcation and Chaos* **24** (2014), 1450009, doi:10.1142/S0218127414500096, https://sprott.physics.wisc.edu/pubs/paper407.pdf (especially Eq. (6)).
2. B. Munmuangsaen, J. C. Sprott, W. J.-C. Thio, A. Buscarino, and L. Fortuna, “A Simple Chaotic Flow with a Continuously Adjustable Attractor Dimension,” *International Journal of Bifurcation and Chaos* **25** (2015), doi:10.1142/S0218127415300360, https://www.iris.unict.it/retrieve/dfe4d22a-bc83-bb0a-e053-d805fe0a78d9/ws-ijbc.pdf (especially Section 2).
3. M. Mehrabbeik, S. Jafari, and J. C. Sprott, “A simple three-dimensional quadratic flow with an attracting torus,” *Physics Letters A* **451** (2022), 128427, https://sprott.physics.wisc.edu/pubs/paper525.pdf (different damping term).
