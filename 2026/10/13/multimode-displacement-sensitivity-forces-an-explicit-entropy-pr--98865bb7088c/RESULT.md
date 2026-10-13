# Multimode displacement sensitivity forces an explicit entropy-production cost

## Finding
Consider the uniform \(N\)-mode thermal Lindblad model with bath occupation \(\bar n>0\), decay rate \(\gamma\), a stable Gaussian steady state with covariance \(V\), and mean \(\bar r\). Write
\[
\nu=\bar n+\frac12,
\qquad
F_{\max}=\lambda_{\max}(V^{-1}),
\qquad
F_{\mathrm{eq}}=\frac1\nu,
\qquad
R=\frac{F_{\max}}{F_{\mathrm{eq}}}=\nu\lambda_{\max}(V^{-1}).
\]
Here \(F_{\max}\) is the largest quantum Fisher information over unit-norm multimode displacement directions, while \(F_{\mathrm{eq}}\) is the corresponding value in the undriven bath-equilibrium covariance \(\nu I_{2N}\).

For every integer \(N\ge1\),
\[
1\le R<2N
\]
and
\[
\boxed{
\frac{\dot\Sigma}{\gamma}
\ge
2N\nu\,\operatorname{arcoth}(2\nu)
\frac{(R-1)^2}{R(2N-R)}.
}
\]
In particular, if \(R=\rho N\) with fixed \(0<\rho<2\), then
\[
\liminf_{N\to\infty}\frac{\dot\Sigma}{\gamma N}
\ge
\frac{2\rho\nu\operatorname{arcoth}(2\nu)}{2-\rho}.
\]
Thus an extensive best-direction displacement-sensitivity gain relative to bath equilibrium requires extensive entropy production, and the lower bound diverges as the normalized gain approaches its trace-imposed ceiling \(2N\).

## Assumptions and scope
The dynamics are the uniform multimode extension in arXiv:2610.01112v1: a quadratic Hamiltonian, identical thermal damping on all modes, and a stable Gaussian steady state. The bath occupation is strictly positive so that \(\operatorname{arcoth}(2\nu)\) is finite. The displacement direction is an arbitrary real unit vector in the \(2N\)-dimensional phase space. The reference \(F_{\mathrm{eq}}=1/\nu\) is the undriven bath-equilibrium state, not the state-dependent passive thermal reference used for the single-mode main-text inequality of the source.

## Proof
The source proves for the uniform \(N\)-mode steady state that
\[
\operatorname{tr}(V^{-1})=\frac{2N}{\nu}.
\]
It also gives the multimode entropy-production identity
\[
\frac{\dot\Sigma}{\gamma}
=
\operatorname{arcoth}(2\nu)
\left(
\|\bar r\|^2+\operatorname{tr}V-2N\nu
\right),
\]
obtained by substituting the trace identity into its generalized formula. For a unit displacement direction \(u\), the Gaussian displacement QFI is \(u^{\mathsf T}V^{-1}u\), so its maximum is \(F_{\max}=\lambda_{\max}(V^{-1})\).

Let \(d=2N\) and let
\[
x_i=\nu\lambda_i(V^{-1})>0,
\qquad i=1,\ldots,d.
\]
Then
\[
\sum_{i=1}^{d}x_i=d,
\qquad
\max_i x_i=R.
\]
The average is one, hence \(R\ge1\); positivity of all remaining eigenvalues gives \(R<d=2N\). Relabel so that \(x_1=R\). By convexity of \(x\mapsto1/x\),
\[
\sum_{i=2}^{d}\frac1{x_i}
\ge
\frac{(d-1)^2}{d-R}.
\]
Therefore
\[
\frac{\operatorname{tr}V}{\nu}
=
\sum_{i=1}^{d}\frac1{x_i}
\ge
\frac1R+rac{(d-1)^2}{d-R}.
\]
Using \(\|\bar r\|^2\ge0\) in the entropy-production identity yields
\[
\frac{\dot\Sigma}{\gamma}
\ge
\nu\operatorname{arcoth}(2\nu)
\left(
\frac1R+rac{(2N-1)^2}{2N-R}-2N
\right).
\]
The bracket simplifies exactly to
\[
\frac{2N(R-1)^2}{R(2N-R)},
\]
which proves the claim. Substituting \(R=\rho N\) and dividing by \(N\) gives the stated extensive-scaling limit.

## Verification
The proof is analytic and does not rely on finite enumeration. The accompanying checker independently verifies the algebraic simplification and samples positive inverse-covariance spectra with normalized trace \(2N\), confirming the reciprocal-sum inequality and the resulting entropy-production bound. Those finite checks are corroborative only.

## Relationship to prior work
Yoshimura and Hamazaki derive the single-mode dissipation-sensitivity inequalities and, in the End Matter, the two uniform multimode identities used above. They explicitly identify multimode extensions and system-size scaling of the dissipation-sensitivity trade-off as a future direction. Their paper does not state a multimode displacement-QFI inequality or the rational \(N\)-dependent profile above. The present bound combines their general multimode thermodynamic identities with the arbitrary-mode displacement-QFI formula and a new spectral extremization.

Earlier work by Wang and Wang studies entropy production and QFI in a two-site nonequilibrium fermionic model, not a uniform multimode bosonic Gaussian covariance problem. Ptaszyński and Esposito analyze entropy production in fermionic and bosonic Gaussian systems through system-environment correlations, but do not derive a steady-state displacement-QFI bound of the form above.

## Limitations
For \(N>1\), the equality spectrum of the reciprocal-sum optimization need not be realizable by a physical covariance satisfying all symplectic uncertainty and steady-state Lyapunov constraints. The theorem is therefore a universal lower bound, not a claim of global sharpness over physically attainable multimode steady states. It applies only to the uniform thermal-bath Gaussian setting and to displacement sensitivity benchmarked against the bath-equilibrium covariance. It does not establish the source's state-dependent passive-reference analogue, a non-Gaussian extension, or an entanglement-enabled optimality theorem.

## References
1. K. Yoshimura and R. Hamazaki, “Dissipation–Sensitivity Trade-Off in Dissipative Bosonic Systems,” arXiv:2610.01112v1 (2026).
2. X. Wang and J. Wang, “The effect of nonequilibrium entropy production on the quantum Fisher information and correlations,” arXiv:1912.12734v1 (2019).
3. K. Ptaszyński and M. Esposito, “Quantum and Classical Contributions to Entropy Production in Fermionic and Bosonic Gaussian Systems,” PRX Quantum 4, 020353 (2023).
