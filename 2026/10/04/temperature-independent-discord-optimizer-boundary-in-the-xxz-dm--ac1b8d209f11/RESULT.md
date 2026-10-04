# Temperature-independent discord optimizer boundary in the XXZ–DM dimer

## Finding

Consider the antiferromagnetic two-qubit XXZ Hamiltonian with a \(z\)-directed Dzyaloshinskii--Moriya interaction,
\[
H=
J(\sigma_x\otimes\sigma_x+\sigma_y\otimes\sigma_y)
+
J_z\sigma_z\otimes\sigma_z
+
D_z(\sigma_x\otimes\sigma_y-\sigma_y\otimes\sigma_x),
\]
with
\[
J>0,\qquad J_z>0,\qquad D_z\in\mathbb R.
\]
Define
\[
R=\sqrt{J^2+D_z^2}.
\]

For every positive temperature \(T\), the Gibbs state is locally unitarily equivalent to a Bell-diagonal state. Its two transverse correlation magnitudes are equal, and comparison with the longitudinal magnitude has the exact form
\[
\boxed{
|c_z|-|c_\perp|
=
\frac{2e^{-J_z/T}}{Z}
\left(
e^{2(J_z-R)/T}-1
\right)
},
\]
where
\[
Z=
2e^{-J_z/T}
+
2e^{J_z/T}\cosh(2R/T).
\]

Therefore the local projective measurement that maximizes the classical correlation in the Bell-diagonal discord formula has a temperature-independent phase boundary:
\[
\boxed{
\begin{array}{ll}
J_z>R:& \text{longitudinal optimizer},\\
J_z<R:& \text{transverse optimizer},\\
J_z=R:& \text{all axes are degenerate}.
\end{array}
}
\]

Equivalently, if
\[
J_z>J,
\]
the optimizer switches at
\[
\boxed{
|D_z|=\sqrt{J_z^2-J^2}
},
\]
for every
\[
T>0.
\]
If
\[
J_z\le J,
\]
there is no nontrivial switch as \(D_z\) is varied: the transverse branch is always optimal, except for the isotropic equality point when \(J_z=J\) and \(D_z=0\).

The same reduction gives the exact leading high-temperature decay of the base-\(2\) quantum discord \(\mathcal D(T)\):
\[
\boxed{
\lim_{T\to\infty}T^2\mathcal D(T)
=
\begin{cases}
\dfrac{R^2}{\ln2},
& J_z\ge R,\\[6pt]
\dfrac{R^2+J_z^2}{2\ln2},
& J_z\le R.
\end{cases}
}
\]
The two formulas coincide when
\[
J_z=R.
\]

Thus the numerical asymptotic decay reported for the thermal discord has a sharp analytic coefficient, and the measurement optimization has a coupling-controlled boundary that does not move with temperature.

## Assumptions and scope

The Hamiltonian and coupling convention are those of the \(D_z\) part of Chen and Yin's two-qubit XXZ model. The claim assumes the antiferromagnetic regime used in that source,
\[
J>0,\qquad J_z>0.
\]
Boltzmann's constant is set to one.

The discord is the standard one-sided projective-measurement quantum discord. Because the thermal state has maximally mixed one-qubit marginals and is locally unitarily equivalent to a Bell-diagonal state, the Bell-diagonal optimization applies exactly.

“Transverse” means a measurement axis in the \(xy\)-plane after the local \(z\)-rotation that removes the DM phase. Returning to the original basis only rotates that transverse axis within the \(xy\)-plane, so the longitudinal-versus-transverse classification is unchanged.

## Proof

Write
\[
J+iD_z=Re^{i\phi},
\qquad
R=\sqrt{J^2+D_z^2}.
\]
A relative local \(z\)-rotation removes the phase \(e^{i\phi}\) from the exchange term. Quantum discord is invariant under local unitaries, so it is enough to study
\[
H'
=
R(\sigma_x\otimes\sigma_x+\sigma_y\otimes\sigma_y)
+
J_z\sigma_z\otimes\sigma_z.
\]

The four Bell eigenstates have Gibbs weights
\[
p_{\Phi^+}=p_{\Phi^-}
=
\frac{e^{-J_z/T}}{Z},
\]
\[
p_{\Psi^+}
=
\frac{e^{(J_z-2R)/T}}{Z},
\qquad
p_{\Psi^-}
=
\frac{e^{(J_z+2R)/T}}{Z},
\]
with
\[
Z=
2e^{-J_z/T}
+
2e^{J_z/T}\cosh(2R/T).
\]

The Bell-diagonal correlation coefficients have
\[
|c_x|=|c_y|
=
|c_\perp|
=
\frac{2e^{J_z/T}\sinh(2R/T)}{Z},
\]
and, because \(J_z>0\),
\[
|c_z|
=
\frac{2\left[e^{J_z/T}\cosh(2R/T)-e^{-J_z/T}\right]}{Z}.
\]
Subtracting gives
\[
|c_z|-|c_\perp|
=
\frac{2}{Z}
\left[
e^{J_z/T-2R/T}-e^{-J_z/T}
\right]
=
\frac{2e^{-J_z/T}}{Z}
\left(
e^{2(J_z-R)/T}-1
\right).
\]
Its sign is therefore exactly the sign of
\[
J_z-R
\]
for every positive temperature.

For a Bell-diagonal two-qubit state, the projective measurement maximizing the classical correlation is aligned with a correlation coefficient of largest absolute value. Hence the optimizer is longitudinal for
\[
J_z>R
\]
and transverse for
\[
J_z<R.
\]
At
\[
J_z=R,
\]
the locally rotated Hamiltonian is isotropic and every measurement axis is degenerate. Solving
\[
J_z=R
\]
for \(D_z\) gives the stated DM threshold.

For the high-temperature law, let
\[
\beta=\frac1T.
\]
The correlations satisfy
\[
c_x=c_y=-\beta R+O(\beta^2),
\qquad
c_z=-\beta J_z+O(\beta^2).
\]
For a Bell-diagonal state with small correlation vector \(c\),
\[
2-S(\rho)
=
\frac{c_x^2+c_y^2+c_z^2}{2\ln2}
+
O(\lVert c\rVert^3),
\]
while its maximal classical correlation is
\[
1-h_2\!\left(\frac{1+c_{\max}}{2}\right)
=
\frac{c_{\max}^2}{2\ln2}
+
O(c_{\max}^4),
\]
where
\[
c_{\max}=\max\{|c_x|,|c_y|,|c_z|\}.
\]
Subtracting gives
\[
\mathcal D(T)
=
\frac{c_x^2+c_y^2+c_z^2-c_{\max}^2}{2\ln2}
+
O(T^{-3}).
\]
Using the exact optimizer ordering yields the two displayed coefficients.

## Verification

`verify_discord_boundary.py` rebuilds the \(4\times4\) Hamiltonian directly from Pauli matrices, forms the Gibbs state by diagonalization, and computes its \(3\times3\) correlation matrix.

For a deterministic parameter grid, it checks that the singular values of the direct correlation matrix agree with the analytic values
\[
|c_\perp|,\quad |c_\perp|,\quad |c_z|.
\]
It verifies that the largest singular direction is longitudinal or transverse exactly according to the sign of
\[
J_z-\sqrt{J^2+D_z^2}.
\]

The script also evaluates the Bell-diagonal discord exactly and checks convergence of
\[
T^2\mathcal D(T)
\]
to the claimed piecewise coefficient at increasing temperatures.

The numerical replay is supplementary. The temperature-independent boundary and asymptotic coefficient are proved analytically above.

## Relationship to prior work

Chen and Yin study this exact XXZ+\(D_z\) thermal state, give the Hamiltonian, calculate its quantum discord, and emphasize numerically that the discord decreases toward zero only asymptotically with temperature. Their plots separately vary \(D_z\) and \(J_z\), and their discussion focuses on the contrasting trends of discord and concurrence. The inspected source does not identify the local-unitary Bell-diagonal reduction as a temperature-independent measurement-optimizer phase diagram, nor does it state the piecewise \(T^{-2}\) decay coefficient.

Luo gives the analytic quantum-discord formula for Bell-diagonal two-qubit states in terms of the largest correlation magnitude. That general theorem is the optimization input used here. The new specialization is the exact comparison
\[
|c_z|-|c_\perp|
\]
for the Chen--Yin Gibbs family and the resulting coupling boundary.

Kundu and Subrahmanyam later show that preferred discord measurement bases can change across anisotropy-driven critical behavior in Heisenberg antiferromagnets. Their work concerns pair correlations in many-spin ground states and does not state the finite-temperature two-site DM boundary
\[
J_z=\sqrt{J^2+D_z^2}
\]
or the high-temperature coefficient obtained here.

A later study of quantum coherence writes the same two-site XYZ+\(D_z\) Gibbs matrix explicitly and confirms that the \(D_z\) interaction enters the transverse energy scale through
\[
\sqrt{J^2+D_z^2}
\]
in the XXZ specialization. It does not analyze discord optimization.

Targeted searches for the exact boundary, the corresponding DM threshold, and a \(T^{-2}\) discord coefficient did not locate an equivalent statement.

## Limitations

The result is for the \(D_z\) Hamiltonian without external magnetic fields and in the antiferromagnetic regime
\[
J>0,\qquad J_z>0.
\]
The \(D_x\) model considered separately by the source is not covered.

The optimizer boundary concerns projective-measurement quantum discord. Other discord-like quantities can have different optimizers.

The high-temperature formula gives the leading coefficient, not a complete asymptotic expansion. The remainder is
\[
O(T^{-3})
\]
in general.

A residual literature risk remains because Bell-diagonal discord is classical material and the exact specialization may have appeared in unindexed notes or under a gauge-rotated XXZ parameterization.

## References

1. Y.-X. Chen and Z. Yin, “Thermal Quantum Discord in Anisotropic Heisenberg XXZ Model with Dzyaloshinskii--Moriya Interaction,” arXiv:1002.0176, first public 1 February 2010; *Communications in Theoretical Physics* 54 (2010), 60–64, DOI: 10.1088/0253-6102/54/1/12.
2. S. Luo, “Quantum discord for two-qubit systems,” *Physical Review A* 77 (2008), 042303, DOI: 10.1103/PhysRevA.77.042303.
3. A. Kundu and V. Subrahmanyam, “Distribution of quantum discord in Heisenberg Antiferromagnets,” arXiv:1307.1325, first public 4 July 2013.
4. S. Radhakrishnan, S. Shukla, and T. Byrnes, “Quantum coherence of the Heisenberg spin models with Dzyaloshinsky--Moriya interactions,” *Scientific Reports* 7 (2017), 13865, DOI: 10.1038/s41598-017-13871-6.
