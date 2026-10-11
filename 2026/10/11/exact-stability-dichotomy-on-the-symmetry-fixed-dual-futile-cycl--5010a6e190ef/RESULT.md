# Exact stability dichotomy on the symmetry-fixed dual futile-cycle Jacobian
## Finding
Consider the reduced six-dimensional Jacobian of the sequential-and-distributive dual futile cycle in Vassena's notation. Impose the fixed-point equalities of the network automorphism \(\sigma\):
\[
a=c=\alpha,\quad e_1=f_7=\varepsilon,\quad u_2=x_8=\mu,\quad u_3=x_9=\nu,
\]
\[
b_4=b_{10}=\beta,\quad e_4=f_{10}=\gamma,\quad v_5=y_{11}=\rho,\quad v_6=y_{12}=\tau,
\]
with \(\alpha,\beta,\varepsilon,\gamma,\mu,\nu,\rho,\tau>0\). Define
\[
\Delta=\nu(\gamma+\rho+\tau)-\gamma\tau.
\]
Then the reduced Jacobian is Hurwitz stable if and only if \(\Delta>0\), equivalently if and only if its determinant is positive. If \(\Delta=0\), there is exactly one simple zero eigenvalue and the other five eigenvalues have negative real part. If \(\Delta<0\), there is exactly one positive real eigenvalue and the other five eigenvalues have negative real part. Therefore no nonzero purely imaginary eigenvalue occurs anywhere on this positive symmetry-fixed slice.

This proves Conjecture 3.1 of the motivating preprint on this natural eight-parameter subfamily and gives a sharper complete spectral dichotomy there.
## Assumptions and scope
The statement is about the source's reduced Jacobian at a positive steady state, with all sixteen derivative parameters positive and the eight \(\sigma\)-paired derivatives set equal as displayed above. The motivating source states that arbitrary positive derivative data are realizable at a steady state for parameter-rich kinetics, so the slice is not merely formal. The pair equalities do not, by themselves, impose the two mass-action constraints in Proposition 5.1; thus the statement is not just a restatement of the source's no-Hopf theorem for mass action kinetics.

The conclusion is local and spectral. It does not assert existence, uniqueness, or global stability of a steady state, and it does not classify nonlinear zero-eigenvalue bifurcations at \(\Delta=0\).
## Proof
Use symmetry-adapted coordinates
\[
q_\pm=Q_1\pm Q_2,\qquad u_\pm=U\pm X,\qquad v_\pm=V\pm Y.
\]
After the eight pair equalities are substituted into the source's matrix \(G_{\mathrm{red}}\), this change of basis block-diagonalizes it as \(G_+\oplus G_-\), where
\[
G_+=\begin{pmatrix}
0&-\nu&\tau\\
\alpha&-(\alpha+\varepsilon+\mu+\nu)&-\varepsilon\\
-2\beta&-\gamma&-(2\beta+\gamma+\rho+\tau)
\end{pmatrix},
\]
\[
G_-=\begin{pmatrix}
0&-\nu&-\tau\\
\alpha&-(\alpha+\varepsilon+\mu+\nu)&-\varepsilon\\
0&-\gamma&-(\gamma+\rho+\tau)
\end{pmatrix}.
\]
Write
\[
p_\pm(z)=\det(zI-G_\pm)=z^3+c_{1,\pm}z^2+c_{2,\pm}z+c_{3,\pm}.
\]
For the antisymmetric block,
\[
c_{1,-}=\alpha+\varepsilon+\mu+\nu+\gamma+\rho+\tau>0,
\]
\[
\begin{aligned}
c_{2,-}={}&\alpha\gamma+\alpha\nu+\alpha\rho+\alpha\tau+\varepsilon\rho+\varepsilon\tau+\gamma\mu+\gamma\nu\\
&+\mu\rho+\mu\tau+\nu\rho+\nu\tau>0,
\end{aligned}
\]
and
\[
c_{3,-}=\alpha\bigl(\nu(\gamma+\rho+\tau)-\gamma\tau\bigr)=\alpha\Delta.
\]
Exact expansion gives \(c_{1,-}c_{2,-}-c_{3,-}>0\); its expanded polynomial has 56 monomials and every coefficient is positive. Hence the cubic Routh--Hurwitz criterion says that \(G_-\) is Hurwitz exactly when \(\Delta>0\).

For the symmetric block, all three coefficients \(c_{1,+},c_{2,+},c_{3,+}\) are polynomials with strictly positive coefficients, and the exact expansion of \(c_{1,+}c_{2,+}-c_{3,+}\) has 86 monomials, all with positive coefficients. Therefore \(G_+\) is Hurwitz for every positive choice of the eight parameters.

At \(\Delta=0\),
\[
p_-(z)=z\bigl(z^2+c_{1,-}z+c_{2,-}\bigr),
\]
so zero is simple and the quadratic factor is Hurwitz. At \(\Delta<0\), the coefficient signs of \(p_-\) are \((+,+,+,-)\), so Descartes' rule gives exactly one positive real root. If that root is \(r>0\), the remaining two roots have positive product and sum \(-c_{1,-}-r<0\); they are therefore either both negative real numbers or a complex-conjugate pair with negative real part.

Finally,
\[
\det G_{\mathrm{red}}=c_{3,+}c_{3,-},
\]
and \(c_{3,+}>0\), so \(\operatorname{sign}\det G_{\mathrm{red}}=\operatorname{sign}\Delta\). This proves all three cases and the equivalence with the determinant sign.
## Verification
The exact block diagonalization, characteristic polynomials, determinant factorization, and coefficientwise positivity of both cubic Hurwitz margins are replayed symbolically by `artifacts/verify_symmetry_slice.py`. Running that file produced `artifacts/verify_output.txt` ending in `VERIFY_OK`. The computation uses exact symbolic algebra only; no floating-point sampling is part of the proof.

The source matrix was independently reconstructed from equation (2.7) and the displayed reduced Jacobian before the symmetry substitutions were made.
## Relationship to prior work
Vassena's 2026 preprint identifies the same \(\mathbb Z_2\) graph automorphism and explicitly lists the eight derivative pairs exchanged by it, but does not assume equality of those pairs in the general parameter-rich problem. The paper exhibits a Hopf-capable, strongly asymmetric positive derivative choice and leaves Conjecture 3.1 open: positive determinant should imply Hurwitz stability. Its closest general advance is a conditional Hurwitz criterion involving an additional polynomial inequality, while the mass-action section proves absence of Hopf only after imposing two kinetic constraints.

The symmetry-fixed classification above uses a different mechanism: the source's six-dimensional Jacobian splits exactly into symmetric and antisymmetric cubic blocks. It therefore proves the determinant conjecture and excludes Hopf on a natural parameter-rich slice that is not forced to satisfy the mass-action constraints.

Conradi, Feliu, and Mincheva previously ruled out Hopf bifurcations in several simplified mass-action double-phosphorylation models using convex steady-state parameters and Hurwitz matrices. That result is mass-action-specific and does not imply the present classification of the source's general derivative-level symmetry slice.
## Limitations
The theorem does not prove Conjecture 3.1 for all sixteen independent positive derivative parameters. It does not claim that every nonlinear kinetic family respecting the graph automorphism has the same global dynamics, nor does it identify the nonlinear bifurcation at the zero-eigenvalue boundary. Bibliographic searches cannot rule out an equivalent observation in unindexed literature.
## References
1. N. Vassena, *Sequential and distributive dual futile cycle: Hopf bifurcation can occur under parameter-rich kinetics but cannot occur under mass action kinetics*, arXiv:2608.27081v1, first public 2026-08-27; revised version inspected as arXiv:2608.27081v2.
2. C. Conradi, E. Feliu, M. Mincheva, *On the existence of Hopf bifurcations in the sequential and distributive double phosphorylation cycle*, Mathematical Biosciences and Engineering 17 (2020), 494--513, DOI 10.3934/mbe.2020027.
