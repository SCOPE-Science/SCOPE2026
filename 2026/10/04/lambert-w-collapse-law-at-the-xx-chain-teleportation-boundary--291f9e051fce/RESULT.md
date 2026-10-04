# Lambert-W collapse law at the XX-chain teleportation boundary

## Finding

For Yeo's antiferromagnetic two-qubit Heisenberg \(XX\) thermal channel, put
\[
\eta=\frac{B_m}J\in[0,1),
\qquad
x_\eta=\frac{J}{T_{\mathrm{tel}}(\eta)}.
\]
The source criterion for standard teleportation with fidelity above \(2/3\) is
\[
\sinh\!\left(\frac JT\right)>\cosh\!\left(\frac{B_m}T\right).
\]
Thus \(x_\eta\) is the unique positive root of
\[
\boxed{\sinh x=\cosh(\eta x)}.
\]
It is equivalently determined by
\[
\boxed{
\tanh\!\left(\frac{(1-\eta)x}2\right)=e^{-(1+\eta)x}
}.
\]

Let \(W\) be the principal Lambert function, defined by \(W(z)e^{W(z)}=z\). Then as \(\eta\uparrow1\),
\[
\boxed{
x_\eta\sim
\frac{W\!\left(2(1+\eta)/(1-\eta)\right)}{1+\eta}
},
\]
and therefore
\[
\boxed{
\frac{T_{\mathrm{tel}}(\eta)}J
\sim
\frac{1+\eta}{W\!\left(2(1+\eta)/(1-\eta)\right)}
\sim
\frac2{W\!\left(4/(1-\eta)\right)}
}.
\]

At this same teleportation threshold, the thermal concurrence is exactly
\[
\boxed{
C_r(\eta)=
\frac12-e^{-x_\eta}-\frac12e^{-2x_\eta}
}.
\]
Hence
\[
C_r(\eta)\longrightarrow\frac12
\]
while \(T_{\mathrm{tel}}(\eta)\to0\). More precisely,
\[
\boxed{
\frac12-C_r(\eta)
\sim
\frac12\sqrt{
(1-\eta)W\!\left(4/(1-\eta)\right)
}
}.
\]

So the operational temperature window collapses only at an inverse-logarithmic Lambert-\(W\) scale, while the amount of concurrence remaining at the classical-fidelity boundary rises to one half.

## Assumptions and scope

The Hamiltonian is
\[
H=
\frac J2(\sigma_x\otimes\sigma_x+\sigma_y\otimes\sigma_y)
+
\frac{B_m}2(\sigma_z\otimes I+I\otimes\sigma_z),
\]
with \(J>0\), \(0\le B_m<J\), and Boltzmann's constant set to one.

The threshold concerns the unprocessed thermal state under the standard Bell-measurement/Pauli-correction protocol in the source. Local filtering, distillation, magnetic impurity, and anisotropic extensions are outside the claim.

## Proof

Set \(x=J/T\) and \(\eta=B_m/J\). The source gives
\[
F=
\frac{\cosh(\eta x)+2\cosh x+\sinh x}
{3(\cosh(\eta x)+\cosh x)}.
\]
Thus \(F>2/3\) exactly when
\[
\sinh x>\cosh(\eta x).
\]

At equality,
\[
e^x-e^{-x}=e^{\eta x}+e^{-\eta x}.
\]
Rearrangement and factoring yield
\[
\tanh\!\left(\frac{(1-\eta)x}2\right)=e^{-(1+\eta)x}.
\]
For \(0\le\eta<1\), the left side is strictly increasing from zero to one and the right side is strictly decreasing from one to zero, so the positive root is unique.

Put
\[
\delta=1-\eta,\qquad
u=\frac{\delta x_\eta}2,\qquad
\kappa=\frac{1+\eta}\delta.
\]
Then
\[
\tanh u=e^{-2\kappa u}.
\]
As \(\delta\downarrow0\), one must have \(u\to0\), hence \(\tanh u=u(1+o(1))\). Therefore
\[
(2\kappa u)e^{2\kappa u}=2\kappa(1+o(1)).
\]
Inverting with \(W\) gives
\[
2\kappa u\sim W(2\kappa).
\]
Since \(2\kappa u=(1+\eta)x_\eta\), the stated \(x_\eta\) and \(T_{\mathrm{tel}}\) asymptotics follow.

The source concurrence in the relevant antiferromagnetic range is
\[
C=
\frac{\sinh x-1}{\cosh(\eta x)+\cosh x}.
\]
At the teleportation boundary \(\cosh(\eta x_\eta)=\sinh x_\eta\), so
\[
C_r(\eta)
=
\frac{\sinh x_\eta-1}{e^{x_\eta}}
=
\frac12-e^{-x_\eta}-\frac12e^{-2x_\eta}.
\]

Finally put \(v=(1+\eta)x_\eta\). The threshold equation and the previous asymptotic imply
\[
v\sim W(4/\delta),
\qquad
e^{-v}\sim\frac{\delta v}4.
\]
Because \(x_\eta=v/(1+\eta)\) and \(1+\eta\to2\),
\[
e^{-x_\eta}
\sim
\frac12\sqrt{\delta W(4/\delta)}.
\]
The term \(e^{-2x_\eta}\) is lower order, proving the concurrence-gap formula.

## Verification

`verify_xx_teleportation_boundary.py` solves the threshold equation by monotone bisection and independently evaluates the source fidelity and concurrence.

It reproduces all nine published table rows for \(\eta=0.1,0.2,\ldots,0.9\), checks the transformed threshold identity, and checks the exact threshold-concurrence formula. It also verifies convergence of the two endpoint ratios at \(\eta=0.99,0.999,0.9999,0.99999\).

The finite replay supplements the analytic uniqueness and asymptotic proof.

## Relationship to prior work

Yeo derives the thermal concurrence and maximal standard-teleportation fidelity for the two-qubit \(XX\) dimer. The paper proves that quantum advantage is equivalent to
\[
\sinh(J/T)>\cosh(B_m/T)
\]
and tabulates critical teleportation temperatures and threshold concurrences for \(B_m/J=0.1,\ldots,0.9\). It notes that increasing \(B_m\) enlarges the range of entangled thermal states that are not useful for this protocol.

The source does not state the monotone hyperbolic-tangent form, the Lambert-\(W\) endpoint law, or the limiting threshold concurrence \(1/2\).

Li and Xu later study a magnetic-impurity \(XX\) chain and report in their abstract that impurity plus field can raise critical temperatures without bound. Their model is different, and only the abstract was available for comparison, so no whole-document noncoverage claim is made here.

Qin, Tao, and Tian later treat an \(XXZ\) generalization. Their full article gives anisotropic fully entangled fractions and a two-copy entanglement-teleportation analysis but does not state the endpoint law above.

## Limitations

The result is specific to the standard protocol without local preprocessing and to the one-sided limit \(B_m/J\uparrow1\) with \(J>0\).

The Lambert-\(W\) formulas are leading asymptotics, not exact finite-\(\eta\) closed forms.

The full text of the magnetic-impurity extension was not available in the inspected source path, leaving a residual originality risk for a related specialized limit.

## References

1. Y. Yeo, “Teleportation via thermally entangled state of a two-qubit Heisenberg XX chain,” arXiv:quant-ph/0205014, first submitted 3 May 2002; related publication DOI: 10.1103/PhysRevA.66.062312.
2. S.-B. Li and J.-B. Xu, “Magnetic field effects on the optimal fidelity of standard teleportation via the two qubits Heisenberg XX chain in thermal equilibrium,” arXiv:quant-ph/0312125, first submitted 15 December 2003.
3. M. Qin, Y.-J. Tao, and D.-P. Tian, “Teleportation via thermally entangled states of a two-qubit Heisenberg XXZ chain,” *Chinese Physics C* 32 (2008), 710–713, DOI: 10.1088/1674-1137/32/9/007.
