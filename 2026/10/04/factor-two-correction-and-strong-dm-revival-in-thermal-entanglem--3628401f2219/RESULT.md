# Factor-two correction and strong-DM revival in thermal entanglement teleportation

## Finding

Consider the thermal two-qubit Heisenberg channel with \(z\)-directed Dzyaloshinskii--Moriya interaction used by Guo-Feng Zhang,
\[
H=
\frac J2
\left[
\sigma_x\otimes\sigma_x+
\sigma_y\otimes\sigma_y+
\sigma_z\otimes\sigma_z+
D(\sigma_x\otimes\sigma_y-\sigma_y\otimes\sigma_x)
\right].
\]
Two independent copies of its Gibbs state are used in the standard two-qubit teleportation protocol.

Set
\[
x=\frac JT,\qquad
s=\sqrt{1+D^2},\qquad
y=xs,
\]
and
\[
Z=
2e^{-x/2}\left(1+e^x\cosh y\right).
\]
For an input pure state with concurrence
\[
0<C_{\mathrm{in}}\le1,
\]
direct evaluation of the teleportation channel gives
\[
\boxed{
C_{\mathrm{out}}
=
\max\!\left\{
\frac{
4\left[
C_{\mathrm{in}}e^x\sinh^2y
-
2s^2\cosh y
\right]
}{
Z^2s^2
},
0
\right\}.
}
\]

The published Eq. (14) has the same expression with prefactor \(2\) instead of \(4\). Therefore, whenever the teleported state is entangled,
\[
\boxed{
C_{\mathrm{out}}^{\mathrm{correct}}
=
2C_{\mathrm{out}}^{\mathrm{printed}}.
}
\]
The factor error does not change the zero-versus-positive threshold because the quantity inside the maximum has the same sign.

There is a second consequence that is not visible from the source's large-\(D\) discussion. For every fixed
\[
J\ne0,\qquad T>0,\qquad C_{\mathrm{in}}>0,
\]
the output concurrence is strictly positive for every sufficiently large finite \(D\), and
\[
\boxed{
C_{\mathrm{out}}(D)
=
\frac{C_{\mathrm{in}}}{1+D^2}
+
O\!\left(
e^{-|J|\sqrt{1+D^2}/T}
\right)
}
\]
as
\[
D\to\infty.
\]
In particular,
\[
\boxed{
\lim_{D\to\infty}D^2C_{\mathrm{out}}(D)
=
C_{\mathrm{in}}.
}
\]

Thus the limiting value
\[
C_{\mathrm{out}}\to0
\]
quoted in the source is correct, but it is approached from the positive side once \(D\) is sufficiently large. Strong DM coupling does not produce permanent finite-\(D\) entanglement death for a nonzero-entanglement input; instead it leaves a universal algebraic tail.

## Assumptions and scope

The result uses exactly the Hamiltonian, thermal channel, Bell-measurement probabilities, and two-copy standard teleportation protocol stated in the 2007 source.

The input is the source family
\[
|\psi\rangle_{\mathrm{in}}
=
\cos\!\left(\frac{\theta}{2}\right)|10\rangle
+
e^{i\phi}
\sin\!\left(\frac{\theta}{2}\right)|01\rangle,
\]
whose concurrence is
\[
C_{\mathrm{in}}=\sin\theta.
\]
The conclusion concerns
\[
C_{\mathrm{in}}>0.
\]
A separable input remains outside the entanglement-teleportation claim.

The high-\(D\) statement fixes nonzero \(J\) and positive \(T\) while sending \(D\) to infinity. It is a statement about the mathematical model; no claim is made that arbitrarily large dimensionless DM coupling is microscopically realizable.

## Proof

Let
\[
\rho_T=Z^{-1}e^{-H/T}.
\]
The source's Gibbs state has equal \(|00\rangle\) and \(|11\rangle\) populations and a single \(|01\rangle\), \(|10\rangle\) coherence. Its four Bell-measurement probabilities define a one-qubit Pauli channel.

Because the two \(\Phi\)-Bell probabilities are equal, the Pauli channel has equal transverse contraction factors. Writing its action on Pauli operators as
\[
\sigma_x\mapsto\lambda_\perp\sigma_x,\qquad
\sigma_y\mapsto\lambda_\perp\sigma_y,\qquad
\sigma_z\mapsto\lambda_z\sigma_z,
\]
direct Bell overlaps give
\[
\lambda_\perp
=
\frac{2e^{x/2}\sinh y}{sZ},
\]
and
\[
\lambda_z
=
\frac{
2\left(
e^{x/2}\cosh y-e^{-x/2}
\right)
}{Z}.
\]

Apply two independent copies of this Pauli channel to the input state. The only output coherence relevant to concurrence is
\[
|(\rho_{\mathrm{out}})_{23}|
=
\frac{C_{\mathrm{in}}}{2}\lambda_\perp^2.
\]
The two corner populations are equal:
\[
(\rho_{\mathrm{out}})_{11}
=
(\rho_{\mathrm{out}})_{44}
=
\frac{1-\lambda_z^2}{4}.
\]
The output is an \(X\)-state, so Wootters concurrence is
\[
C_{\mathrm{out}}
=
2\max\!\left\{
|(\rho_{\mathrm{out}})_{23}|
-
\sqrt{
(\rho_{\mathrm{out}})_{11}
(\rho_{\mathrm{out}})_{44}
},
0
\right\}.
\]
Therefore
\[
C_{\mathrm{out}}
=
\max\!\left\{
C_{\mathrm{in}}\lambda_\perp^2
-
\frac{1-\lambda_z^2}{2},
0
\right\}.
\]

Substitution of the two contraction factors and elementary simplification give
\[
C_{\mathrm{out}}
=
\max\!\left\{
\frac{
e^x
\left[
C_{\mathrm{in}}e^x\sinh^2y
-
2s^2\cosh y
\right]
}{
s^2(1+e^x\cosh y)^2
},
0
\right\}.
\]
Using
\[
Z^2
=
4e^{-x}(1+e^x\cosh y)^2
\]
gives the displayed prefactor-\(4\) formula.

The source's printed Eq. (14) has prefactor \(2\) in the \(Z\)-form, so its positive value is exactly one half of the directly reconstructed concurrence.

For the strong-DM limit, write the positive raw expression as
\[
\frac{
C_{\mathrm{in}}e^{2x}\sinh^2y
}{
s^2(1+e^x\cosh y)^2
}
-
\frac{
2e^x\cosh y
}{
(1+e^x\cosh y)^2
}.
\]
Since
\[
|y|=\frac{|J|}{T}s\to\infty,
\]
the first term equals
\[
\frac{C_{\mathrm{in}}}{s^2}
\left[
1+O(e^{-|y|})
\right],
\]
while the second term is
\[
O(e^{-|y|}).
\]
Hence
\[
C_{\mathrm{out}}
=
\frac{C_{\mathrm{in}}}{s^2}
+
O(e^{-|y|}).
\]
Because
\[
s^2=1+D^2,
\]
the stated asymptotic follows.

The same estimate proves eventual positivity: the positive term is algebraic in \(D\), whereas the subtraction is exponentially small in \(D\).

## Verification

`verify_dm_teleportation.py` reconstructs the \(4\times4\) Gibbs state directly from Pauli matrices, computes its Bell probabilities, applies the resulting Pauli teleportation channel independently to both input qubits, and evaluates Wootters concurrence from the resulting density matrix.

Across deterministic antiferromagnetic and ferromagnetic parameter grids, the direct matrix concurrence agrees with the corrected formula. Whenever the output is positive, the direct value is exactly twice the value of the source's printed Eq. (14).

The checker also verifies explicit strong-\(D\) revival examples and convergence of
\[
D^2C_{\mathrm{out}}
\]
to
\[
C_{\mathrm{in}}.
\]

The numerical replay is supplementary. The factor correction and asymptotic tail are proved analytically above.

## Relationship to prior work

Zhang derives the thermal channel and the standard two-copy teleportation output. The paper's Eq. (14) prints an output concurrence with prefactor \(2\), and its discussion says that increasing DM interaction ultimately makes the output entanglement zero while correctly noting that the limiting concurrence tends to zero.

Direct reconstruction of the protocol shows that the Wootters concurrence has prefactor \(4\). The zero set of the printed formula is unaffected, but every positive concurrence value is smaller by a factor of two.

A later XXZ study by Chen, Shan, Huang, Liu, and Li also studies output concurrence and fidelity under different DM orientations. It confirms that strong DM coupling can have nontrivial teleportation effects, but the inspected material does not identify the factor-two correction to the 2007 expression or the universal
\[
D^{-2}
\]
tail.

Later thermal-teleportation work continues to use Heisenberg channels with DM interactions. Targeted searches for the exact 2007 DOI together with “correction,” “factor two,” the printed output-concurrence formula, and the strong-\(D\) asymptotic did not locate a published correction.

## Limitations

The factor-two statement is specific to the standard two-copy Pauli teleportation protocol and the concurrence normalization used by Wootters and by the source for the input state.

The positivity threshold is unchanged by the factor correction. Results in the source that depend only on whether the printed expression is positive can therefore remain valid even when the positive concurrence magnitude is wrong.

The high-\(D\) tail concerns fixed nonzero \(J\), fixed positive \(T\), and nonzero input concurrence. The limits \(J\to0\), \(T\to\infty\), or \(C_{\mathrm{in}}\to0\) are not interchangeable with the strong-\(D\) limit.

A residual literature risk remains because later teleportation papers often reuse closely related formulas, and an unindexed erratum or independent correction may exist.

## References

1. G.-F. Zhang, “Thermal entanglement and teleportation in a two-qubit Heisenberg chain with Dzyaloshinski-Moriya anisotropic antisymmetric interaction,” arXiv:quant-ph/0703019, first public 2 March 2007; *Physical Review A* 75 (2007), 034304, DOI: 10.1103/PhysRevA.75.034304.
2. T. Chen, C.-J. Shan, Y.-X. Huang, T.-K. Liu, and J.-X. Li, “The effect of different Dzyaloshinskii--Moriya interactions on teleportation via a two-qubit Heisenberg chain,” *Modern Physics Letters B* 24 (2010), 461–473, DOI: 10.1142/S0217984910022536.
3. G. Bowen and S. Bose, “Teleportation as a depolarizing quantum channel, relative entropy, and classical capacity,” *Physical Review Letters* 87 (2001), 267901, DOI: 10.1103/PhysRevLett.87.267901.
