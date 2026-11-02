# Sharp fermionic covariance-admissibility frontier for coherence-selective bath resetting

## Finding
Consider a finite number-conserving fermionic system, with at least one system mode and at least one bath mode. Its one-particle density matrix is a Hermitian block matrix
\[
\Gamma=\begin{pmatrix}A&C\\C^\dagger&B\end{pmatrix},\qquad 0\preceq\Gamma\preceq I.
\]
Let the prescribed bath target \(B_0\) satisfy \(0\preceq B_0\preceq I\). For a retention factor \(0\le\eta\le1\), consider the *hard-bath, partial-coherence reset rule*
\[
\mathcal R_\eta(\Gamma)=\begin{pmatrix}A&\eta C\\\eta C^\dagger&B_0\end{pmatrix}.
\]
The rule maps **every** admissible fermionic one-particle density matrix to another admissible one if and only if
\[
\boxed{\eta^2\le q(B_0):=\min\{\lambda_{\min}(B_0),\ 1-\lambda_{\max}(B_0)\}.}
\tag{1}
\]
Both obstructions in (1) are sharp already for a single system mode and a single occupied bath eigenmode. This theorem is about one-particle covariance admissibility, **not** the existence of a completely positive trace-preserving implementation; covariance admissibility alone does not establish such an implementation.

For a finite thermal bath, \(B_0=(I+e^{\beta(H_B-\mu I)})^{-1}\), with inverse temperature \(\beta>0\) and extreme bath energies \(E_-\le E_+\), (1) becomes
\[
\boxed{\eta_{\mathrm{safe}}^2(\mu)=\frac{1}{1+\exp\{\beta\max(E_+-\mu,\mu-E_-)\}}.}
\tag{2}
\]
It is uniquely maximized at the band midpoint \(\mu=(E_-+E_+)/2\), where
\[
\boxed{\eta_{\mathrm{safe,peak}}=\big(1+e^{\beta(E_+-E_-)/2}\big)^{-1/2}.}
\tag{3}
\]
Thus a bounded band admits a nonzero universal covariance-safe retention at finite temperature, while a bath with an unbounded energy spectrum in at least one direction has no strictly positive uniform retention bound at any fixed finite \(\beta\) and finite \(\mu\).

There is also an exact **reachable-state distinction**. For a resonant single system mode and single bath mode of hopping strength \(g>0\), let the reference bath occupation be \(0\le n\le1\), and start the continuous-reset evolving-correlation equations from uncorrelated system occupation \(0\le p\le1\). The exact trajectory is
\[
\Gamma(t)=\begin{pmatrix}
 n+(p-n)\cos(\sqrt2 gt)&i(p-n)\sin(\sqrt2 gt)/\sqrt2\\
 -i(p-n)\sin(\sqrt2 gt)/\sqrt2&n
\end{pmatrix}.
\tag{4}
\]
It satisfies \(0\preceq\Gamma(t)\preceq I\) **for every** \(t\ge0\) if and only if
\[
\boxed{|p-n|\le\min\{n,1-n\}.}
\tag{5}
\]
In particular, even though the endpoint \(\eta=1\) fails the all-input guarantee of (1), particular trajectories may remain admissible. Conversely, outside the interval (5), a trajectory beginning at a perfectly valid uncorrelated covariance becomes inadmissible in finite time. These are different, precisely specified quantifiers.

## Assumptions and scope
The system and bath mode spaces are finite-dimensional for (1)--(3). Matrices \(A,B,B_0\) are Hermitian, and \(C\) has the appropriate rectangular shape. The physicality condition is exactly that the gauge-invariant fermionic one-particle correlation matrix is a positive contraction. Input states may be correlated, pure or mixed and are quantified over **all** such matrices. The resetting rule retains the entire system block and replaces the bath block with \(B_0\), independently of its prior value. Neither the bath's Hamiltonian nor system--bath interaction affects (1). The thermal formulas assume ordinary Fermi--Dirac occupations of the bath eigenmodes. The continuous-resonant trajectory (4)--(5) assumes vanishing initial intermode coherence, a single mode on each side, zero detuning and a frozen bath occupation in the evolving-correlation limit.

## Proof
**Step 1: uniform sufficiency for positivity.** Write the original admissible matrix as \(\Gamma=\left(\begin{smallmatrix}A&C\\C^\dagger&B\end{smallmatrix}\right)\). Since \(\Gamma\succeq0\) and \(B\preceq I\), one has
\[
\begin{pmatrix}A&C\\C^\dagger&I\end{pmatrix}
=\Gamma+\begin{pmatrix}0&0\\0&I-B\end{pmatrix}\succeq0.
\]
Congruence by \(\operatorname{diag}(I,\eta I)\) gives \(\left(\begin{smallmatrix}A&\eta C\\\eta C^\dagger&\eta^2 I\end{smallmatrix}\right)\succeq0\). If \(B_0\succeq\eta^2I\), then adding \(\operatorname{diag}(0,B_0-\eta^2I)\) proves \(\mathcal R_\eta(\Gamma)\succeq0\).

**Step 2: uniform sufficiency for the Pauli upper bound.** From \(I-\Gamma\succeq0\) and \(B\succeq0\), the matrix \(\left(\begin{smallmatrix}I-A&-C\\-C^\dagger&I\end{smallmatrix}\right)\) is positive. The same congruence and addition show \(I-\mathcal R_\eta(\Gamma)\succeq0\) whenever \(I-B_0\succeq\eta^2 I\). The two conditions are precisely (1).

**Step 3: sharpness of both independent bounds.** Let \(e\) be a normalized bath eigenvector with eigenvalue \(b\) of \(B_0\), and let \(s\) be any orthonormal system vector. Choose the admissible rank-one projector \(\Gamma_p=|\psi_p\rangle\langle\psi_p|\) with \(\psi_p=\sqrt p\,s+\sqrt{1-p}\,e\), where \(0<p<1\). On the span of \(s,e\), the determinant of the reset covariance is
\[
\det\big(\mathcal R_\eta(\Gamma_p)|_{\mathrm{span}\{s,e\}}\big)=p\,[b-\eta^2(1-p)].
\tag{6}
\]
If \(\eta^2>b\), any \(0<p<1-b/\eta^2\) makes (6) negative. Taking the eigenvector for \(\lambda_{\min}(B_0)\) establishes the first necessity. Similarly, the determinant of the complementary block is
\[
\det\big((I-\mathcal R_\eta(\Gamma_p))|_{\mathrm{span}\{s,e\}}\big)
=(1-p)[1-b-\eta^2p].
\tag{7}
\]
If \(\eta^2>1-b\), choosing \((1-b)/\eta^2<p<1\) makes (7) negative. Taking the eigenvector for \(\lambda_{\max}(B_0)\) establishes the second necessity. Equalities in (1) are allowed by Steps 1--2; the theorem is inclusive at the boundary.

**Step 4: thermal optimum.** The Fermi occupation \(f(E)=(1+e^{\beta(E-\mu)})^{-1}\) decreases strictly with \(E\). Hence \(\lambda_{\min}(B_0)=f(E_+)\) and \(1-\lambda_{\max}(B_0)=1-f(E_-)\), yielding (2). Minimizing \(\max(E_+-\mu,\mu-E_-)\) over real \(\mu\) uniquely balances its two affine terms at \(\mu=(E_-+E_+)/2\). This gives (3), including the equal-band-edge case. An unbounded upper or lower spectrum makes the corresponding limiting bath eigenoccupations approach zero or one; the infimum of the universal bound is then zero, as a limiting extension of the finite-dimensional criterion (no finite unbounded-spectrum matrix is asserted).

**Step 5: continuous resonant reachable region.** The evolving-correlation equations reduce to \(\dot P=-2g\operatorname{Im}c\), \(\dot c=ig(P-n)\), \(c(0)=0\) and \(P(0)=p\). Solving the harmonic equation \(\ddot P=-2g^2(P-n)\) yields (4). Put \(d=p-n\) and \(\theta=\sqrt2gt\); then \(\Gamma(t)=nI+dK(\theta)\), where
\[
K(\theta)=\begin{pmatrix}\cos\theta&i\sin\theta/\sqrt2\\-i\sin\theta/\sqrt2&0\end{pmatrix}.
\]
The eigenvalues of \(K\) are \(\big(\cos\theta\pm\sqrt{2-\cos^2\theta}\big)/2\), both in \([-1,1]\). Indeed \(\sqrt{2-c^2}\le2-|c|\) for \(|c|\le1\), equivalent to \(0\le2(1-|c|)^2\) after squaring. At \(\theta=0\) and \(\theta=\pi\) the extreme eigenvalues \(+1\) and \(-1\) are attained. Therefore all trajectories have eigenvalues in \([0,1]\) exactly when \(n-|d|\ge0\) and \(n+|d|\le1\), which is (5).

## Verification
A standalone standard-library Python checker is included at `verifier/verify.py`. Run `python3 verifier/verify.py` from the extracted package directory. It independently tests the two-by-two positivity and Pauli bounds using exact rational arithmetic, constructs strict rank-one witnesses beyond both thresholds, samples the reachable trajectory, and checks the thermal midpoint result. Numerical sampling is only supplementary: arbitrary dimensions, all real parameters, and the infinite collection of admissible inputs are covered by the analytical proof above. The exact time and transcendental Fermi exponentials are not certified by finite sampling.

## Relationship to prior work
Kumar, Lazarides and Ala-Nissila (2026), *Thermodynamics of Coherence-Selective Quantum Reset Protocols*, introduce exactly the hard-bath partial-coherence update in their equations (14a)--(14d), with the full range \(0\le\eta\le1\), and study coherent fixed points, heat and chemical-potential dependence. This paper supplies the map definition, not the all-input spectral admissibility classification (1)--(3). Their earlier *Coherence-Controlled Quantum Zeno Dynamics from Exact Reset Maps* derives the continuous evolving-correlation equations used to obtain (4)--(5). The later *Memory--Transport Competition in Physical Two-Bath Quantum Reset Dynamics* explicitly observes that arbitrary hard resetting with retained coherence need not define a physical fermionic state and replaces it by physical thermal attenuators. **That qualitative nonphysicality observation is prior work and is not claimed here.** The contribution assessed here is the exact inclusive universal retention frontier, the thermal midpoint optimization, and the complete resonant reachable-state window. The last, especially close October 2026 paper was accessible through its abstract but not as full text for this comparison; this leaves a genuine priority risk concerning uninspected technical sections. General covariance positivity and matrix congruence are standard, also not claimed as new.

## Limitations
The all-input bound is a fermionic *covariance-admissibility* statement, neither an implementable completely positive map nor proof of physical realizability of all retained correlations. No claim is made that every numerical fixed point or trajectory studied in prior publications is unphysical above the bound. When \(\eta\) exceeds the universal bound, specific input subfamilies can remain admissible, as the exact resonant example demonstrates. The continuous resonant example does not extend without proof to detuned or multi-mode dynamics, finite reset intervals, or nonzero initial coherences. The spectral result assumes a hard reset of the entire bath block; physical thermal attenuators that modify bath occupation and coherence jointly are different operations. The incomplete full-text comparison with the October 2026 closely related manuscript limits any publication-priority conclusion.

## References
1. J. Kumar, A. Lazarides, T. Ala-Nissila, *Thermodynamics of Coherence-Selective Quantum Reset Protocols*, arXiv:2604.17152v1 (first public posting 2026-04-18), https://arxiv.org/abs/2604.17152. Full-text sections II C, VI, VII and surrounding derivations inspected at https://www.researchgate.net/publication/404022312_Thermodynamics_of_Coherence-Selective_Quantum_Reset_Protocols.
2. J. Kumar, A. Lazarides, T. Ala-Nissila, *Coherence-Controlled Quantum Zeno Dynamics from Exact Reset Maps*, arXiv:2603.27619v1 (first public posting 2026-03-29), https://arxiv.org/abs/2603.27619. Full-text section IV, equations (63)--(76), inspected at https://www.researchgate.net/publication/403308667_Coherence-Controlled_Quantum_Zeno_Dynamics_from_Exact_Reset_Maps.
3. J. Kumar, A. Lazarides, T. Ala-Nissila, *Memory--Transport Competition in Physical Two-Bath Quantum Reset Dynamics*, arXiv:2610.30457v1 (first public posting 2026-10-21), https://arxiv.org/abs/2610.30457. Accessible abstract inspected; full text unavailable in this review.
