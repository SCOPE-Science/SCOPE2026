# Exact Floquet reset and entanglement-breaking horizons for two switched qubit dissipators

## Finding

A single damped qubit driven alternately by two unitary conjugates of the same Lindblad jump admits an **exact finite-switching solution**. At every strictly positive dwell time, one complete two-leg switching cycle is a convex mixture of the identity channel and a replacement channel, with a **faithful**, explicitly computable replacement state. In contrast, the continuously averaged Lindblad generator has a **pure** replacement state. Finite-switching imperfections thus turn an evolution with no finite entanglement-breaking time into one with a sharp finite entanglement-breaking cycle index. Its physical entanglement-breaking horizon diverges logarithmically as the switching becomes arbitrarily fast. Two Floquet observation sections have different exact replacement-state purities, but their entanglement-breaking indices differ by at most one cycle.

For any dwell \(h>0\), let \(v=e^{-h}\), \(u=e^{-h/2}\), \(k=2\sqrt2/3\). At the cycle boundary, the channel is
\[
\Phi_h(\rho)=a\rho+(1-a)\tau_h,\qquad a=e^{-4h},\qquad
\tau_h=\tfrac12(I+\mathbf r_h\cdot\boldsymbol\sigma),
\]
where
\[
\mathbf r_h=\frac{k(1-v^3)}{1-v^4}(1,0,v).
\]
At the symmetrically shifted Floquet section the map is
\[
\Psi_h(\rho)=a\rho+(1-a)\widehat\tau_h,\qquad
\widehat{\mathbf r}_h=\frac{k}{1-u^8}\bigl(u(1-u^6),\ 0,\ (1-u^3)(1+u^5)\bigr).
\]
Both states are strictly mixed for every \(h>0\). More precisely,
\[
1-\|\mathbf r_h\|^2
=\frac{(1-v)^2(v^2+4v+1)}{9(1+v)^2(1+v^2)}>0,
\]
and the two sections have the strict, explicit purity ordering
\[
\|\widehat{\mathbf r}_h\|^2-\|\mathbf r_h\|^2
=\frac{8u^2(1-u)^4(1+u+u^2)^2}{9(1+u^2)^2(1+u^4)^2}>0.
\]
Define \(\delta_h=\sqrt{1-\|\mathbf r_h\|^2}\) and \(\widehat\delta_h=\sqrt{1-\|\widehat{\mathbf r}_h\|^2}\). The smallest number of complete switching cycles after which every system–ancilla state is separable is exactly
\[
N_h=\left\lceil\frac{1}{4h}\log\frac{2+\delta_h}{\delta_h}\right\rceil,
\qquad
\widehat N_h=\left\lceil\frac{1}{4h}\log\frac{2+\widehat\delta_h}{\widehat\delta_h}\right\rceil.
\]
These integers satisfy \(N_h\le\widehat N_h\le N_h+1\) for every \(h>0\). Their physical horizon is asymptotically
\[
2hN_h=\tfrac12\log\frac{4\sqrt3}{h}+O(h),\qquad
2h\widehat N_h=\tfrac12\log\frac{4\sqrt3}{h}+O(h)
\quad (h\downarrow0).
\]
The continuously averaged generator has no finite entanglement-breaking time at all.

## Assumptions and scope

Work on a qubit with Pauli matrices \(\sigma_x,\sigma_y,\sigma_z\), matrix identity \(I\), and Lindblad convention
\[
\mathcal D_L(\rho)=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\}.
\]
Let \(L_1=\sigma_x+i\sigma_y/\sqrt2\), \(U=-i(\sigma_x+\sigma_z)/\sqrt2\), \(L_2=UL_1U^\dagger\), and \(\mathcal D_j=\mathcal D_{L_j}\). The physical control holds \(\mathcal D_1\) for time \(h\), then \(\mathcal D_2\) for time \(h\), and repeats. Channels multiply right-to-left; thus \(\Phi_h=e^{h\mathcal D_2}e^{h\mathcal D_1}\), and the centered section is \(\Psi_h=e^{(h/2)\mathcal D_1}e^{h\mathcal D_2}e^{(h/2)\mathcal D_1}\). These are two observation sections of one periodic control, not claims of independent physical protocols. Their indices refer to repeated complete section-to-section maps. Time is measured in the dimensionless units fixed by the displayed dissipators. Ancillary systems may have arbitrary finite dimension: for qubit channels, entanglement breaking is characterized by separability of the qubit–qubit Choi state.

## Proof

**1. Affine Bloch equations.** A direct Pauli calculation, also recorded in the motivating source, gives
\[
\dot{\mathbf r}=Q_j\mathbf r+\mathbf b_j,\quad
Q_1=\operatorname{diag}(-1,-2,-3),\quad \mathbf b_1=2\sqrt2\,(0,0,1),
\]
\[
Q_2=\operatorname{diag}(-3,-2,-1),\quad \mathbf b_2=2\sqrt2\,(1,0,0).
\]
For a single leg of length \(t\), the homogeneous multiplier is \(e^{tQ_j}\). The first leg translates the third coordinate by \(k(1-e^{-3t})\), and the second leg translates the first coordinate by the same quantity. Because \(Q_1+Q_2=-4I_3\), both complete sections have homogeneous multiplier \(e^{-4h}I_3\). Composing the translation terms yields exactly the two fixed Bloch vectors displayed under Finding. An affine map \(\mathbf r\mapsto a\mathbf r+(1-a)\mathbf s\) on qubits equals \(\rho\mapsto a\rho+(1-a)\tau_{\mathbf s}\) by linearity of the Bloch parametrization. These facts establish both reset formulas for all \(h>0\).

**2. Faithfulness and section-dependent purity.** Substituting the first fixed vector and factoring gives the formula for \(1-\|\mathbf r_h\|^2\). Subtracting its squared norm from that of the centered section, with common denominator, gives the stated strict positive identity. To show the centered state is still interior to the Bloch ball, exact factorization gives
\[
1-\|\widehat{\mathbf r}_h\|^2
=\frac{(1-u)^2 P(u)}{9(1+u^2)^2(1+u^4)^2},
\]
where
\[
P(u)=u^{10}+2u^9-3u^8+8u^7+6u^6+20u^5+6u^4+8u^3-3u^2+2u+1.
\]
For \(0<u<1\), regrouping \(P(u)=(1-u)(1+3u)+8u^3+6u^4+20u^5+6u^6+u^7(8-3u)+2u^9+u^{10}\) proves \(P(u)>0\). Thus both replacement states have full rank for every strictly positive dwell.

**3. Exact entanglement-breaking criterion.** Consider any qubit reset mixture \(\mathcal R_{a,\tau}(\rho)=a\rho+(1-a)\tau\), with \(0\le a\le1\), \(\tau=(I+\mathbf s\cdot\boldsymbol\sigma)/2\), and \(\delta=\sqrt{1-\|\mathbf s\|^2}\). Its normalized Choi matrix is \(a|\Phi^+\rangle\langle\Phi^+|+(1-a)(I/2)\otimes\tau\). Diagonalize \(\tau\), with eigenvalues \(\lambda_\pm=(1\pm\|\mathbf s\|)/2\). After partial transpose, the only potentially negative two-by-two block has diagonal entries \((1-a)\lambda_+/2\), \((1-a)\lambda_-/2\), and off-diagonal entries \(a/2\). Its determinant is nonnegative precisely if
\[
a^2\le(1-a)^2\lambda_+\lambda_-=(1-a)^2\delta^2/4,
\quad\text{equivalently}\quad a\le\frac{\delta}{2+\delta}.
\]
Positivity of partial transpose is equivalent to separability in two-by-two dimensions; a qubit channel is entanglement breaking exactly when its Choi state is separable. The channel's \(m\)-fold power is \(\rho\mapsto a^m\rho+(1-a^m)\tau\) for every nonnegative integer \(m\). Taking \(a=e^{-4h}\), with each \(\delta>0\), proves both ceiling formulas including their equality endpoints.

**4. Exact one-cycle section bound.** Higher centered-section purity implies \(\widehat\delta_h<\delta_h\), so \(\widehat N_h\ge N_h\). Put \(A=e^{h\mathcal D_1}\), \(B=e^{h\mathcal D_2}\), \(C=e^{(h/2)\mathcal D_1}\). Using \(C^2=A\), an exact rearrangement gives \(\Psi_h^{m+1}=C\Phi_h^m BC\) for every integer \(m\ge0\). If \(\Phi_h^m\) is entanglement breaking, so is any physical-channel pre- and post-processing of it. Consequently \(\widehat N_h\le N_h+1\), establishing the bound without approximating either section.

**5. Rapid-switching law and singular averaged limit.** Taylor expansion of the exact formulas gives
\[
1-\|\mathbf r_h\|^2=\frac{h^2}{12}+O(h^4),\qquad
1-\|\widehat{\mathbf r}_h\|^2=\frac{h^2}{12}+O(h^4),
\]
so \(\delta_h=\widehat\delta_h=h/(2\sqrt3)+O(h^3)\). Substitution into the ceiling formulas, and the bound of one cycle on ceiling discretization, yields \(2hN_h=\tfrac12\log(4\sqrt3/h)+O(h)\) and the analogous centered-section estimate. The averaged Lindbladian \(\overline{\mathcal D}=(\mathcal D_1+\mathcal D_2)/2\) has Bloch equation \(\dot{\mathbf r}=-2(\mathbf r-\mathbf n)\), with pure \(\mathbf n=(1,0,1)/\sqrt2\). Its channel is \(e^{-2t}\rho+(1-e^{-2t})\tau_{\mathbf n}\), whose replacement-state parameter is \(\delta=0\). By Step 3, it is never entanglement breaking at finite time, despite its exact contraction rate equaling that of the switched cycle per physical unit of time. This completes the proof.

## Verification

A standalone Python checker `verify.py` uses NumPy and SciPy matrix exponentials of the two \(4\times4\) Lindblad superoperators, independently reconstructs both section maps and their Choi matrices, tests the closed-form fixed vectors, checks PPT at the predicted integer boundaries, and samples short-dwell asymptotics. Run `python verify.py` after installing `requirements.txt`. The current package replay passes 196 checks. These finite checks corroborate the analytic identities but are not a proof for arbitrary dwell time or all integer powers.

## Relationship to prior work

Wang (arXiv:2610.00046; first posted September 3, 2026), section 2.2, introduced precisely this two-ray dissipative qubit system and proved pure-state stabilization under the continuously averaged generator. The current result retains that physical model but resolves exact **finite** switching, two Floquet sections, and their operational entanglement-breaking horizons. Trinh (arXiv:2606.31243) has already established a generalized Bell-mixture separability threshold; the general two-by-two PPT criterion in Step 3 is an elementary known ingredient, not claimed as new. Hanson, Rouzé and França (arXiv:1902.08173) study eventual entanglement breaking in Markovian dynamics generally. This result differs in its exact switched-ray formulas, purity ordering, phase bound and logarithmic singular switching limit. No literature-wide claim of priority is asserted.

## Limitations

The theorem is for an ideal qubit with exactly the two specified jump operators, equal positive dwell times, and a fixed periodic alternation. The midpoint section is a change of sampling phase rather than independent control. The physical horizon is for repeated full-cycle channels, not arbitrary intermediate times. The asymptotic statement is in the rapid-switching limit, not an estimate uniform over modified generators. Perturbations of the jumps, non-Markovian memory, and coherent system Hamiltonians are not analyzed. Priority against all conceivable quantum-control or Floquet results has not been independently certified.

## References

1. Y. Wang, *Lie-Wedge Stratification and Pure-State Stabilizability in Single-Channel Qubit Control*, arXiv:2610.00046 (first public version September 3, 2026), https://arxiv.org/abs/2610.00046.
2. X. D. Trinh, *Absorption capacity of separable noise: Bell-mixing thresholds on entanglement and teleportation*, arXiv:2606.31243 (2026), https://arxiv.org/abs/2606.31243.
3. E. Hanson, C. Rouzé and D. Stilck França, *Eventually Entanglement Breaking Markovian Dynamics: Structure and Characteristic Times*, arXiv:1902.08173 (2019), https://arxiv.org/abs/1902.08173.
