# A mass–frequency entropy gradient for symmetric competition with global mutation

## Finding

**Theorem (strict gradient structure and complete point convergence).** Let \(d\ge2\), let \(A=(A_{ij})_{1\le i,j\le d}\) be a real symmetric matrix with **strictly positive entries**, and let \(\mu>0\). For every nonzero initial condition in the closed nonnegative orthant, the solution of
\[
\dot x_i=x_i\Bigl(1-\sum_{j=1}^d A_{ij}x_j\Bigr)+\mu\sum_{j\ne i}(x_j-x_i),\qquad 1\le i\le d,
\]
is global, is strictly positive at each positive time, and converges to a single strictly positive equilibrium as \(t\to\infty\). No nonconstant periodic solution or other non-equilibrium recurrent state exists in the nonnegative orthant; every invariant probability measure is supported on equilibria (including the origin).

More quantitatively, put \(S=\sum_i x_i>0\) and \(p_i=x_i/S\). The explicit real-analytic potential
\[
\Phi(S,p)=\log S-S\,p^{\mathsf T}Ap+2\mu\sum_{i=1}^d\log p_i
\]
on the positive mass–frequency simplex satisfies the **exact strict dissipation identity**
\[
\boxed{\ \frac{d}{dt}\Phi(S(t),p(t))
 =\left(\frac{\dot S}{S}\right)^2
   +2\sum_{i=1}^d\frac{\dot p_i^{\,2}}{p_i}\ \ge0.\ }
\]
Equality at any time holds exactly at an equilibrium. In particular, every nonstationary orbit dissipates a positive amount and
\[
\int_0^\infty\left[(\dot S/S)^2+2\sum_i\dot p_i^{\,2}/p_i\right]dt
=\Phi(S_\infty,p_\infty)-\Phi(S_0,p_0)<\infty
\]
for strictly positive initial states, with the obvious positive-time starting point if the initial state is on the boundary.

## Assumptions and scope

The population dimension \(d\) is any fixed integer at least two; \(A=A^{\mathsf T}\) has \(A_{ij}>0\), but **need not be positive definite**. All species have intrinsic per-capita growth one; mutation occurs between every distinct pair at the common fixed rate \(\mu>0\). The theorem does not assume a small mutation rate, hyperbolicity or uniqueness of equilibria. In dimension three, \(A\) with diagonal entries one and off-diagonal entries \(a>0\) is precisely the equal-interaction slice \(\alpha=\beta=a\) of the globally mutated May–Leonard model of Jaramillo–Mrad–Stepien. The zero initial state remains at the origin and is excluded from the positive-limit assertion.

## Proof

**1. Exact mass–frequency equations.** For \(S>0\), write \(q=p^{\mathsf T}Ap\). Summing the equations cancels mutation and gives
\[
\dot S=S-S^2q.
\]
Subtracting \(p_i\dot S\) from \(\dot x_i\) and dividing by \(S\) gives
\[
\dot p_i=-Sp_i\bigl((Ap)_i-q\bigr)+\mu(1-dp_i),\qquad\sum_i p_i=1.
\]
These identities are algebraic, not limiting approximations.

**2. Gradient identity.** Taking derivatives of \(\Phi\) before restricting to the affine simplex yields
\[
\partial_S\Phi=S^{-1}-q,\qquad
V_i:=\partial_{p_i}\Phi=-2S(Ap)_i+2\mu/p_i.
\]
Symmetry of \(A\) is used exactly in the second identity. Let \(\overline V=\sum_i p_iV_i\). The two evolution equations become
\[
\dot S=S^2\partial_S\Phi,\qquad
\dot p_i=\tfrac12p_i(V_i-\overline V).
\]
The second expression is the Shahshahani gradient on the simplex with mobility one-half. By the chain rule, using \(\sum_i\dot p_i=0\),
\[
\dot\Phi=S^2(\partial_S\Phi)^2+\tfrac12\sum_i p_i(V_i-\overline V)^2
=(\dot S/S)^2+2\sum_i\dot p_i^{\,2}/p_i.
\]
Because \(S>0\) and every \(p_i>0\), the equality case is exactly \(\dot S=0=\dot p_i\) for all \(i\), equivalently \(\dot x=0\).

**3. Compactness, positivity and global existence.** Put \(m=\min_{i,j}A_{ij}>0\). On the simplex \(q\ge m\), hence \(\Phi(S,p)\le\log S-mS\). The right-hand side tends to \(-\infty\) as \(S\downarrow0\) or \(S\to\infty\). On a compact positive range of \(S\), the entropy term \(2\mu\sum\log p_i\) tends to \(-\infty\) if any \(p_i\downarrow0\), whereas \(-Sq\) is bounded. Therefore each nonempty superlevel \(\{\Phi\ge c\}\) is compact in the interior mass–frequency domain. A strictly positive solution is trapped in its initial superlevel and is consequently global and bounded away from every boundary. At a nonzero boundary point of the original orthant, any vanishing coordinate has derivative \(\mu S>0\). Thus a solution started nonnegative and nonzero enters the strictly positive orthant for every \(t>0\); its subsequent trajectory is controlled by the same superlevel argument. Uniqueness prevents reaching the origin at a finite time.

**4. Convergence to one point.** The potential is real analytic in \((S,p)\) on its open domain. Its gradient mobility is a smooth strictly positive-definite Riemannian metric on each compact interior subset: the mass coefficient is \(S^2\), and the frequency coefficient is one-half of the Shahshahani metric on the \((d-1)\)-dimensional tangent space. Consequently this is an **analytic gradient ascent** with a compact positive orbit. The finite-dimensional Łojasiewicz gradient convergence theorem implies that every such orbit has finite tail arc length and converges to one critical point. For completeness, the mechanism is the local inequality \(|\Phi(z)-\Phi(z_*)|^{1-\vartheta}\le C\|\nabla\Phi(z)\|\), with \(0<\vartheta\le1/2\), near an accumulation point \(z_*\). Uniform positive definiteness of the mobility in a compact neighborhood converts it, together with the dissipation identity, into a finite-length bound before the orbit can exit that neighborhood; hence the orbit stays nearby and converges to \(z_*\). The limit is an equilibrium by Step 2.

**5. Recurrence and stationary laws.** Strict monotonicity of \(\Phi\) away from equilibria excludes nonconstant interior recurrent orbits. Every invariant probability is concentrated on recurrent points by Poincaré recurrence; no nonzero boundary point is recurrent because positive time carries it into the interior. Hence each invariant probability is supported on the equilibrium set, with the origin allowed. This conclusion concerns invariant probabilities, not time-dependent transient distributions.

## Verification

The independently executable `CHECKER.py` performs exact rational tests of the original population field against both mass–frequency equations and against the dissipation identity for symmetric positive matrices with different off-diagonal interactions; it also checks the exact three-species equilibrium ratio identity and the distinction from the uniform-competition specialization. The computations were carried out from the embedded source, using actual packaged bytes. These finite exact checks test algebraic identities but do **not** replace the real-analytic gradient convergence proof, which applies to all stated dimensions, parameters, and positive trajectories. All logarithms are natural.

## Relationship to prior work

Jaramillo, Mrad and Stepien [1], Sections III–V and Appendix A, define the globally mutated three-species May–Leonard model, analyze local stability, find explicit symmetric-slice equilibrium formulas and show numerical nonoscillation on \(\alpha=\beta\). Their equilibrium formulas are **not claimed as new here**. The present claim is a strict global entropy-gradient identity and point convergence **for arbitrary positive symmetric competition matrices and all mutation rates**, covering in particular a multistable diagonal slice not covered by the source's local or numerical results.

Coville and Fabre [2], Theorems 1.1–1.4, prove global convergence for mutation models with a species-independent competition term, and in a small uniformly bounded perturbative regime; their general-interaction existence theorem is weaker. The present result allows arbitrarily strong species-specific **symmetric** competition and can have multiple positive equilibria. For example, the three-species equal-off-diagonal case with \(a=13/10\), \(\mu=3/100\) has a symmetric equilibrium and six additional nonsymmetric positive equilibria, so the cited unique-equilibrium statements cannot imply the present global point convergence. The exact location of equilibrium-fold curves in this specialized case is related to [1, Eq. (33)], not claimed as an independent new fold discovery.

The identification of symmetric-game replicator dynamics with the Shahshahani gradient, and classical Łojasiewicz convergence theory, are established mathematical tools [3,4]. The contribution is the **coupled mass–frequency potential** and its strict global dissipation identity for the nonconservative mutated competition ODE; the literature check is not a claim of exhaustive publication priority.

## Limitations

Strict positivity of every interaction-matrix entry provides properness of the potential, while matrix symmetry and common parent-independent mutation rate are essential for the displayed gradient formula. This theorem does **not** address cyclically asymmetric May–Leonard coefficients \(\alpha\ne\beta\), where limit cycles are known, or arbitrary mutation graphs. Global convergence does not select a unique equilibrium in multistable regimes, specify basin boundaries, give a uniform convergence rate, or prove the existence of a smooth attracting carrying manifold. The analytic convergence step invokes the classical finite-dimensional Łojasiewicz theorem, not an external independent verification. Literature comparisons are bounded and do not establish worldwide publication priority.

## References

1. G. Jaramillo, L. Mrad, T. L. Stepien, “Dynamics of a linearly-perturbed May–Leonard competition model,” arXiv:2210.04342v1 (first public 2022-10-09), v2 (2023-05-12), *Chaos* 33, 053135 (2023), doi:10.1063/5.0138150. Primary MSC2020 37G15. Full accessible preprint: https://arxiv.org/html/2210.04342v2.
2. J. Coville and F. Fabre, “Convergence to the Equilibrium in a Lotka–Volterra ODE Competition System with Mutations,” arXiv:1301.6237v2 (2013), especially Theorems 1.1–1.4. https://arxiv.org/pdf/1301.6237.
3. S. Shahshahani, “A new mathematical framework for the study of linkage and selection,” *Memoirs of the AMS* 17, no. 211 (1979). Used for the standard simplex gradient metric.
4. S. Łojasiewicz, “Une propriété topologique des sous-ensembles analytiques réels,” in *Les Équations aux Dérivées Partielles*, CNRS (1963). Standard analytic-gradient convergence principle.
