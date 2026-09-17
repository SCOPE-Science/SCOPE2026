# Crossing-only switch geometry in a threshold-controlled dengue model

## Result

Consider the piecewise-smooth dengue model of Aldila, Páez Chávez, Gökçe, Götz and Gürbüz (arXiv:2607.18140), in the five dynamically active variables
\[
z=(S,A,I,U,V)^T,
\]
with hospital-capacity threshold \(I=C\) and fogging threshold \(I=kC\), \(0<k\le 1\). The recovery, mosquito-infection and fogging laws are
\[
f(I)=\begin{cases}
\gamma_1 I,&I<C,\\
\gamma_1C+\gamma_2(I-C),&I\ge C,
\end{cases}
\]
\[
g(U,A,I)=\begin{cases}
\beta_{m1}UA,&I<C,\\
\beta_{m1}UA+\beta_{m2}U(I-C),&I\ge C,
\end{cases}
\]
and
\[
h(I)=\begin{cases}0,&I<kC,\\ \eta,&I\ge kC.\end{cases}
\]
The symptomatic component is
\[
\dot I=(1-p)\beta_hSV+\alpha A-f(I)-(\mu_h+\delta)I.
\]

### Theorem 1 — no ordinary Filippov sliding on either threshold

For every \(0<k\le1\), neither switching hypersurface carries an open attracting or escaping Filippov sliding region.

For \(0<k<1\), on the fogging surface
\[
\Sigma_k=\{I=kC\}
\]
the two one-sided vector fields satisfy
\[
F_{\rm on}-F_{\rm off}
=(0,0,0,-\eta U,-\eta V)^T.
\]
With normal \(n=e_I=(0,0,1,0,0)^T\),
\[
n^TF_{\rm on}=n^TF_{\rm off}
=(1-p)\beta_hSV+\alpha A-(\gamma_1+\mu_h+\delta)kC.
\]
Thus the normal components can never have opposite signs. Wherever this common quantity is nonzero, \(\Sigma_k\) is crossed transversally; where it vanishes, one has a common tangency rather than an ordinary codimension-one sliding region.

On the capacity surface
\[
\Sigma_C=\{I=C\},
\]
for \(0<k<1\) fogging is already active on both sides. Moreover,
\[
\gamma_1C=\gamma_1C+\gamma_2(C-C),\qquad
\beta_{m1}UA=\beta_{m1}UA+\beta_{m2}U(C-C),
\]
so the full vector field is continuous across \(\Sigma_C\):
\[
F_C^+=F_C^-.
\]
The Jacobian generally jumps, but there is no Filippov vector-field discontinuity and hence no ordinary sliding region. If \(k=1\), the two thresholds coincide; the only vector-field jump is again the fogging jump above, which is tangent to the common switching surface, so the same no-sliding conclusion holds.

### Theorem 2 — fogging crossings have unipotent saltation

At any transversal crossing of \(\Sigma_k\), let \(F^-\) and \(F^+\) denote the vector fields immediately before and after the event and put
\[
\phi=n^TF^-\ne0.
\]
There is no state reset, so the standard saltation matrix is
\[
\mathcal S
=I_5+\frac{(F^+-F^-)n^T}{\phi}.
\]
Because the vector-field jump is tangent to the switching surface,
\[
n^T(F^+-F^-)=0.
\]
Consequently
\[
(\mathcal S-I_5)^2=0,
\qquad
\det \mathcal S=1,
\]
and every eigenvalue of \(\mathcal S\) equals one. Thus a fogging activation or deactivation is an exact rank-one unipotent shear (unless the jump itself vanishes). For an off-to-on crossing,
\[
\mathcal S_{\rm on}
=I_5-
\frac{\eta(0,0,0,U,V)^T e_I^T}{\phi},
\]
with the sign reversed for an on-to-off crossing.

For \(0<k<1\), a transversal crossing of \(\Sigma_C\) has
\[
\mathcal S_C=I_5,
\]
because the vector field itself is continuous there. When \(k=1\), the coincident threshold again has the unipotent fogging saltation above.

### Corollary — threshold events do not change the Floquet determinant

For a periodic orbit whose threshold encounters are all transversal, every event saltation matrix has determinant one. Hence the determinant of the monodromy matrix receives no multiplicative contribution from threshold events. If \(J(t)\) is the smooth-regime Jacobian along the orbit between events, then
\[
\det M=\exp\!\left(\int_0^T \operatorname{tr}J(t)\,dt\right),
\]
where the integral is taken piecewise over the smooth flight segments. Threshold events can still shear perturbations and alter individual Floquet multipliers; the statement concerns their product.

### Corollary — the fogging event is mosquito-radial

At \(I=kC\), the saltation update changes mosquito perturbations by the same relative amount:
\[
\Delta(\delta U)=-\frac{\eta U}{\phi}\,\delta I,
\qquad
\Delta(\delta V)=-\frac{\eta V}{\phi}\,\delta I
\]
for activation. Therefore, when \(U,V>0\),
\[
\Delta\!\left(\frac{\delta U}{U}-\frac{\delta V}{V}\right)=0.
\]
Equivalently, writing total mosquitoes \(N=U+V\) and infected fraction \(q=V/N\), the event shear acts only in the \(N\)-direction: the first-order perturbation \(\delta q\) has no instantaneous saltation jump whenever \(N>0\). This reflects the model assumption that fogging adds the same mortality rate to susceptible and infected mosquitoes.

## Proof

For \(0<k<1\), both sides of \(I=kC\) lie below hospital capacity, so \(f\) and \(g\) have the same formulas on the two sides. Switching fogging from \(0\) to \(\eta\) changes only the \(U\)- and \(V\)-equations, by \(-\eta U\) and \(-\eta V\), respectively. Hence the displayed jump vector has zero \(I\)-component. The two normal velocities are therefore identical. Standard Filippov sliding or escaping on a codimension-one switching surface requires the two one-sided normal velocities to have opposite signs; this cannot occur here. At \(I=C\), continuity follows directly from the matching values of the two pieces of \(f\) and \(g\). The case \(k=1\) combines these two observations.

The saltation formula for an autonomous threshold with identity reset gives the displayed \(\mathcal S\). Write
\[
N_s=\mathcal S-I_5=\frac{\Delta F\,n^T}{\phi}.
\]
Then
\[
N_s^2=\frac{\Delta F\,(n^T\Delta F)\,n^T}{\phi^2}=0.
\]
The matrix determinant lemma gives
\[
\det\mathcal S=1+\frac{n^T\Delta F}{\phi}=1.
\]
Nilpotence of \(N_s\) implies that all eigenvalues of \(I_5+N_s\) are one. The Floquet determinant statement follows from multiplicativity of determinants, Liouville's formula on each smooth flight segment, and \(\det\mathcal S_j=1\) at each event. The mosquito-fraction statement follows by substituting the two event updates into the differential of \(q=V/(U+V)\).

## Context and significance

The motivating paper explicitly leaves a Filippov sliding-mode analysis of \(I=kC\) and \(I=C\) as future work. The calculation above shows that the ordinary sliding regions sought in that analysis are structurally absent for the model as written. This is not true for threshold dengue models in general: You, Meyer-Baese, Xu and Zhang (2024) analyze a different threshold-controlled dengue system whose switching law does produce a genuine sliding mode. The distinction is geometric. In the present model, the discontinuous fogging action changes mosquito mortality while the switching normal is the human symptomatic coordinate, so the jump is tangent to the switching hypersurface.

The saltation result gives a compact exact rule for variational calculations of the periodic outbreaks reported in the motivating paper. Although the event matrices are not generally the identity at fogging switches, they are determinant-one shears and preserve the mosquito infection-fraction perturbation instantaneously.

## Limitations

The theorem concerns ordinary first-order Filippov sliding/escaping regions. At points where the common normal velocity vanishes, the system has a degenerate tangency; higher-order grazing or tangency phenomena are not classified here. The saltation formula applies only to transversal crossings, where the normal velocity is nonzero. The result does not determine existence or stability of periodic orbits by itself, and it does not classify the Hopf bifurcation reported in the source paper. It analyzes the model exactly as formulated in arXiv:2607.18140v1; later model revisions could change the switch geometry.

## References

1. D. Aldila, J. Páez Chávez, A. Gökçe, T. Götz, B. Gürbüz, *A Mathematical Model of Dengue Transmission Incorporating Hospital Capacity and Threshold-Based Fogging Interventions*, arXiv:2607.18140v1 (2026). https://arxiv.org/abs/2607.18140
2. M. di Bernardo, C. J. Budd, A. R. Champneys, P. Kowalczyk, *Piecewise-smooth Dynamical Systems: Theory and Applications*, Springer (2008). https://doi.org/10.1007/978-1-84628-708-4
3. N. J. Kong, J. J. Payne, J. Zhu, A. M. Johnson, *Saltation Matrices: The Essential Tool for Linearizing Hybrid Dynamical Systems*, Proceedings of the IEEE 112 (2024), 585–608. https://doi.org/10.1109/JPROC.2024.3440211
4. W. You, A. Meyer-Baese, X. Xu, Q. Zhang, *The dynamics and near-optimal controls of a dengue model with threshold policy*, Mathematical Methods in the Applied Sciences 47 (2024), 13313–13335. https://doi.org/10.1002/mma.10192
