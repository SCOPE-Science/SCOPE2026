# Coherence-resolved capture times and optimal uniform dephasing on quantum stars

## Finding

For a symmetric quantum star with an irreversible hub trap and independent, identically strong leaf dephasing, the entire dependence of the **mean** first absorption time on an arbitrary initial coherent or mixed leaf state is captured by its population in the dark subspace. Define the bright vector \(|B\rangle=n^{-1/2}\sum_{j=1}^{n}|j\rangle\), and set \(w=1-\langle B|\rho_0|B\rangle\). For every positive leaf dephasing rate, the exact mean is

\[
T_{\rho_0}=\frac{n+1}{\kappa}+\frac{\kappa+\gamma+\delta}{4J^2}+\frac{nw}{\gamma}.
\]

For \(w>0\), there are unique and independently determined optimal noise and trap rates,

\[
\gamma_*=2J\sqrt{nw},\qquad \kappa_*=2J\sqrt{n+1},\qquad
T_{\min}=\frac{\sqrt{n+1}+\sqrt{nw}}{J}+\frac{\delta}{4J^2}.
\]

For a localized leaf, \(w=(n-1)/n\), hence \(\gamma_*=2J\sqrt{n-1}\). For an initial dark pure state, \(w=1\); for an initial bright pure state, \(w=0\). Intriguingly, even for the pure bright input, the zero-noise limit of the mean differs from its value with *exactly* zero noise.

## Assumptions and scope

Let \(n\ge2\) be an integer. The single-excitation Hilbert space has orthonormal basis \(|0\rangle\) for the hub and \(|1\rangle,\dots,|n\rangle\) for the leaves. Set \(J>0\), \(\kappa>0\), \(\gamma>0\), \(\delta\ge0\), and

\[
H=J\sum_{j=1}^{n}(|0\rangle\langle j|+|j\rangle\langle0|),\quad P_j=|j\rangle\langle j|.
\]

With the dephasing rates normalized so that leaf-to-leaf off-diagonal density entries decay at rate \(\gamma\), the unnormalized surviving density matrix satisfies

\[
\dot\rho=-i[H,\rho]-\frac\kappa2\{P_0,\rho\}
+\gamma\sum_{j=1}^{n}\bigl(P_j\rho P_j-\tfrac12\{P_j,\rho\}\bigr)
+\delta\bigl(P_0\rho P_0-\tfrac12\{P_0,\rho\}\bigr).
\]

The initial matrix \(\rho_0\) is any positive semidefinite, trace-one operator supported on the leaf span, including arbitrary phases and coherences. The capture probability by time \(t\) is \(1-\operatorname{tr}\rho(t)\), and the unconditional mean capture time is \(T_{\rho_0}=\int_0^\infty\operatorname{tr}\rho(t)dt\). No competing recombination channel is present.

## Proof

Write \(\mathcal L\) for the displayed trace-decreasing generator and \(\mathcal L^\dagger\) for its Hilbert--Schmidt adjoint. Define \(h=(n+1)/\kappa\) and \(\eta=(\kappa+\gamma+\delta)/(4J^2)\). Construct a Hermitian matrix \(X\) by its complete entries

\[
X_{00}=h,\quad X_{0j}=\frac{i}{2J},\quad X_{j0}=-\frac{i}{2J},\quad
X_{ij}=(h+\eta+n/\gamma)\mathbf1_{\{i=j\}}-1/\gamma
\quad(1\le i,j\le n).
\]

**Adjoint equation.** Direct substitution gives \(\mathcal L^\dagger X=-I\) entrywise. At the hub, the Hamiltonian commutator contributes \(n\) and the trap contributes \(-\kappa h=-(n+1)\), leaving \(-1\). At each leaf diagonal, the commutator contributes \(-1\). At distinct leaf pairs, it contributes \(-1\), precisely canceled by the leaf-dephasing contribution \(-\gamma X_{ij}=+1\). The hub-to-leaf commutator is \(iJ\eta\), canceled by the sum of the hub-loss, leaf-dephasing and hub-dephasing terms \(-i(\kappa+\gamma+\delta)/(4J)\). Hermitian-conjugate entries follow automatically.

**Positivity and absorption.** Each of the \(n-1\) leaf dark directions is an eigenvector of \(X\) with eigenvalue \(h+\eta+n/\gamma>0\). On the span of the hub and \(|B\rangle\), the remaining principal block is

\[
\begin{pmatrix}
h&i\sqrt n/(2J)\\
-i\sqrt n/(2J)&h+\eta
\end{pmatrix}.
\]

Its determinant is \(h(h+\eta)-n/(4J^2)>0\), since \(h\eta\ge(n+1)/(4J^2)\). Therefore \(X\) is strictly positive. Taking the trace against the evolution gives

\[
\frac{d}{dt}\operatorname{tr}(X\rho(t))
=\operatorname{tr}((\mathcal L^\dagger X)\rho(t))
=-\operatorname{tr}\rho(t).
\]

Because \(X>0\), the integral of survival probability is bounded by \(\operatorname{tr}(X\rho_0)\). Survival probability is nonincreasing because \(\frac d{dt}\operatorname{tr}\rho(t)=-\kappa\rho_{00}(t)\le0\), and a nonnegative nonincreasing integrable function tends to zero. Consequently \(\rho(t)\) tends to zero in trace norm, and the finite-dimensional trace \(\operatorname{tr}(X\rho(t))\) tends to zero as well. Integrating the adjoint identity yields \(T_{\rho_0}=\operatorname{tr}(X\rho_0)\).

**State dependence.** The trace-one leaf input has \(\operatorname{tr}(\rho_0\mathbf1_{\mathrm{leaf}})=1\) and \(\sum_{i,j}\langle i|\rho_0|j\rangle=n\langle B|\rho_0|B\rangle\), giving exactly the claimed expression \(h+\eta+n w/\gamma\). It is independent of all other details of the input state.

**Optimization.** For \(w>0\), the only varying terms are \((n+1)/\kappa+\kappa/(4J^2)\) and \(\gamma/(4J^2)+nw/\gamma\). Each is strictly convex near its unique positive minimum and the derivative equations give \(\kappa_*=2J\sqrt{n+1}\), \(\gamma_*=2J\sqrt{nw}\), with strict global minima by arithmetic--geometric mean inequality. For \(w=0\) the expression is strictly increasing in positive \(\gamma\), so no positive-noise optimum exists.

**Exact zero-dephasing boundary.** At \(\gamma=0\), the Hamiltonian leaves the dark leaf subspace invariant. If \(w>0\), the surviving dark weight is permanently uncaptured. If \(w=0\), positivity of \(\rho_0\) forces the unique initial state \(|B\rangle\langle B|\); on the hub--bright two-dimensional invariant system, the hopping is \(\sqrt n J\). The same two-level adjoint calculation yields

\[
T_{\gamma=0,\,w=0}=\frac2\kappa+\frac{\kappa+\delta}{4nJ^2},
\]

which generally differs from \(\lim_{\gamma\downarrow0}T_{\gamma,w=0}=(n+1)/\kappa+(\kappa+\delta)/(4J^2)\). The discontinuity reflects arbitrarily rare creation of slowly released dark occupation.

## Verification

Run `python check_star.py` with Python, NumPy and SciPy. The script constructs the full density-matrix Liouvillian without use of the symmetry reduction, solves \(180\) independent full-generator mean-first-passage problems across \(n=2,\ldots,7\), and checks arbitrary coherent, incoherent and mixed states. It independently checks \(\mathcal L^\dagger X=-I\), positivity of \(X\), and rate optimization. The observed maximum relative error is \(5.330\times10^{-15}\), and the maximum adjoint residual is \(1.421\times10^{-14}\). Numerical experiments support, but do not replace, the analytical proof for all \(n\).

## Relationship to prior work

Rebentrost and collaborators (2008) and Plenio and Huelga (2008) established the importance of noise-assisted quantum excitation transport. Kassal and Aspuru-Guzik (2012) studied ordered-network trapping efficiency with competing losses. Novo and collaborators (2014) used quantum-walk symmetry reductions without these local Lindblad noise rates. Pepe and collaborators (2023) analyzed an extended-star trapping architecture with dephasing and optimized site-energy defects and capture quantiles; their analyzed observable and initial state differ from the mean-time, coherence-resolved identity established here. A related source-only dephasing calculation applies a Lindblad bath at a different set of sites and does not directly imply the uniform-all-leaf, arbitrary-input formula. Standard finite-dimensional resolvent theory can in principle produce a numerical answer, but no inspected source states this simplification or the joint optimum for the exact model. Priority remains provisional.

## Limitations

The theorem assumes uniform positive star-edge coupling, site-local Markovian dephasing at every leaf, a single irreversible hub trap, and no competing decay or energy disorder. The strictly positive dephasing formula cannot be substituted at zero dephasing because the Liouvillian acquires a dark invariant subspace. Only the first absorption-time moment is classified, not higher moments or the full capture-time distribution. The mathematical formula is self-reviewed but has not received independent scientific validation; its historical priority cannot be certified from a bounded literature search.

## References

- Rebentrost et al., *Environment-Assisted Quantum Transport* (first public 2008-07-07), https://arxiv.org/abs/0807.0929.
- Plenio and Huelga, *Dephasing assisted transport: Quantum networks and biomolecules* (first public 2008-07-30), https://arxiv.org/abs/0807.4902.
- Kassal and Aspuru-Guzik, *Environment-assisted quantum transport in ordered systems* (first public 2012-01-25), https://arxiv.org/abs/1201.5202.
- Novo et al., *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs* (first public 2014-12-22), https://arxiv.org/abs/1412.7209.
- Pepe et al., *Optimized excitonic transport mediated by local energy defects: survival of optimization laws in the presence of dephasing* (first public 2023-08-30), https://arxiv.org/abs/2308.15857.
