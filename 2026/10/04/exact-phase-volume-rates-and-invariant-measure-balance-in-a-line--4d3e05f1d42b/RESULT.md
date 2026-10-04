# Exact phase-volume rates and invariant-measure balance in a line-equilibrium quadratic flow

## Finding

Consider the polynomial flow
\[
\dot x=y,\qquad
\dot y=-a x+y z,\qquad
\dot z=x^2-b y^2,
\]
with \(a>0\) and \(b>0\). Its divergence is exactly
\[
\nabla\!\cdot F=z.
\]
The equilibria form the line \(E_s=(0,0,s)\), \(s\in\mathbb R\). Along that stationary trajectory, Liouville's formula gives
\[
\det D\phi_t(E_s)=e^{s t},
\]
and therefore
\[
\lim_{t\to\infty}\frac1t\log\left|\det D\phi_t(E_s)\right|=s.
\]
Hence bounded trajectories realize every real phase-volume rate. In particular, the vector field is not globally Lebesgue-volume preserving.

There is a stronger smooth-volume obstruction. If a positive \(C^1\) density \(\rho\) made \(\rho\,dx\,dy\,dz\) invariant on an open set containing some \(E_s\) with \(s\ne0\), then
\[
0=\nabla\!\cdot(\rho F)(E_s)
 =\rho(E_s)\,\nabla\!\cdot F(E_s)
 =\rho(E_s)s,
\]
which is impossible.

At \(E_s\), the Jacobian has characteristic polynomial
\[
\lambda\bigl(\lambda^2-s\lambda+a\bigr).
\]
For \(a>0\), the two transverse eigenvalues therefore have negative real part when \(s<0\), positive real part when \(s>0\), and equal \(\pm i\sqrt a\) when \(s=0\). The negative half-line is transversely attracting pointwise and the positive half-line transversely repelling pointwise. No individual \(E_s\) is asymptotically stable in the full phase space, because every neighborhood of it contains a distinct stationary point \(E_{s'}\).

Every compactly supported invariant probability measure \(\mu\) additionally obeys
\[
\int x^2\,d\mu=b\int y^2\,d\mu,
\qquad
\int y^2z\,d\mu=0.
\]
For \(b>0\), the two quadratic moments vanish exactly for invariant measures supported on the equilibrium line.

## Assumptions and scope

The result concerns the exact autonomous polynomial ODE above with \(a>0\) and \(b>0\). Liouville's formula is applied on every time interval on which the local flow exists; the equilibrium trajectories exist for all time. The invariant-measure identities require only a compactly supported invariant probability measure, so the polynomial observables used below are integrable.

The introducing 2022 article uses \(a=1\), \(b=0.68\) for its main numerical chaotic trajectory. It defines conservative dynamics in terms of constant phase-space volume and then infers system-wide zero dissipation from a numerically computed Lyapunov spectrum whose sum is approximately zero. The theorem here distinguishes that trajectory-level observation from the exact global vector-field geometry.

## Proof

For
\[
F(x,y,z)=\bigl(y,-a x+y z,x^2-b y^2\bigr),
\]
direct differentiation gives
\[
\nabla\!\cdot F
=\partial_x y+\partial_y(-a x+y z)+\partial_z(x^2-b y^2)
=z.
\]
For a \(C^1\) flow map \(\phi_t\), Liouville's formula yields
\[
\det D\phi_t(p)
=\exp\left(\int_0^t z(\phi_\tau(p))\,d\tau\right).
\]
Since \(F(E_s)=0\), one has \(\phi_t(E_s)=E_s\), and substitution gives \(\det D\phi_t(E_s)=e^{st}\). Taking \(t^{-1}\log\) proves the continuum of exact phase-volume rates.

If \(\rho>0\) is \(C^1\) and \(\nabla\!\cdot(\rho F)=0\), then at an equilibrium
\[
\nabla\!\cdot(\rho F)
=\nabla\rho\cdot F+\rho\,\nabla\!\cdot F
=\rho(E_s)s.
\]
This cannot vanish when \(s\ne0\).

The Jacobian at \(E_s\) is
\[
J_s=
\begin{pmatrix}
0&1&0\\
-a&s&0\\
0&0&0
\end{pmatrix},
\]
so
\[
\det(\lambda I-J_s)
=\lambda(\lambda^2-s\lambda+a).
\]
The transverse roots have sum \(s\) and product \(a>0\). If they are real, both have the sign of \(s\); if they are complex, both have real part \(s/2\). At \(s=0\) they are \(\pm i\sqrt a\). The lack of asymptotic stability of an individual equilibrium follows because a distinct nearby equilibrium is a constant trajectory and therefore never converges to \(E_s\).

Finally, invariance of a compactly supported probability measure implies that the mean Lie derivative of every polynomial observable is zero. Applying this to \(z\) gives
\[
0=\int \dot z\,d\mu
 =\int(x^2-b y^2)\,d\mu,
\]
hence the quadratic-moment identity. Applying it to \(a x^2+y^2\) gives
\[
0=\int \frac d{dt}(a x^2+y^2)\,d\mu
 =2\int y^2z\,d\mu.
\]
If the quadratic moments vanish, then \(x=y=0\) almost everywhere because \(b>0\), so the measure is supported on the equilibrium line; the converse is immediate.

## Verification

The accompanying symbolic checker reconstructs the divergence, equilibrium line, Jacobian characteristic polynomial, and both Lie-derivative identities exactly. It also verifies that the equilibrium-line tangent-map determinant has exponent equal to \(s\).

These checks are algebraic. They do not reproduce the source article's long-time numerical Lyapunov calculation or establish the existence or nonexistence of its reported chaotic sea.

## Relationship to prior work

Veeman, Natiq, Ali, Rajagopal, and Hussain introduced this five-term quadratic oscillator in 2022 and reported a numerical Lyapunov spectrum approximately \((0.0055,0,-0.0055)\) for one initial condition. The article concludes from the zero numerical sum and Kaplan--Yorke dimension three that the oscillator is conservative and has no dissipation. It also identifies the equilibrium line and the sign change in its transverse linear spectrum.

Jafari, Sprott, and Dehghan's 2019 taxonomy is the closest conceptual precursor. It explicitly distinguishes uniformly zero divergence from state-dependent divergence and includes a category in which average dissipation depends on initial conditions. Their examples show that zero average divergence on one orbit need not imply the same behavior for all initial conditions. They do not analyze the present vector field, its equilibrium-line continuum of exact rates, the smooth invariant-density obstruction, or the invariant-measure identities above.

Targeted title, DOI, equation, divergence, invariant-density, equilibrium-rate, and correction searches did not reveal an inspected publication containing this source-specific theorem. The result therefore sharpens the 2022 paper's classification without asserting that its displayed non-equilibrium chaotic trajectory has nonzero average divergence.

## Limitations

The theorem does not determine \(\lim_{T\to\infty}T^{-1}\int_0^T z(t)\,dt\) for the particular chaotic initial condition used in the 2022 paper. It therefore neither proves nor disproves that this one numerical trajectory has zero average divergence. It also does not establish or refute chaos, multistability, the plotted bifurcations, or any Hamiltonian or mechanical energy interpretation.

The originality assessment is literature-search based and may miss an unindexed correction or equivalent derivation. The smooth-volume obstruction assumes a positive \(C^1\) density; singular invariant measures are not excluded.

## References

1. D. Veeman, H. Natiq, A. M. Ali Ali, K. Rajagopal, and I. Hussain, “A Simple Conservative Chaotic Oscillator with Line of Equilibria: Bifurcation Plot, Basin Analysis, and Multistability,” *Complexity* 2022, Article 9345036 (2022). DOI: 10.1155/2022/9345036.
2. S. Jafari, J. C. Sprott, and S. Dehghan, “Categories of Conservative Flows,” *International Journal of Bifurcation and Chaos* 29(2), 1950021 (2019). DOI: 10.1142/S0218127419500214.
