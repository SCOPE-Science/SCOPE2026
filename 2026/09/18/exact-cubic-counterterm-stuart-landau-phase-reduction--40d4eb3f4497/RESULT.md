# Exact cubic counterterm cancels the full second-order phase correction in a Stuart–Landau triad

## Result

Consider the three Stuart–Landau oscillators used by Muolo, Nakao, and Bick (2026) in their explicit second-order calculation,
\[
\dot z_i=(a+ib)z_i-|z_i|^2z_i
+\varepsilon e^{i\rho}\sum_{\ell\ne i}w_{i\ell}z_\ell ,
\qquad a>0,
\]
with straight isochrones and no linear self-coupling. Their phase reduction has the form
\[
\dot\theta_i=b+\varepsilon F_i^{(1)}(\theta)
+\varepsilon^2 f_i^{(2)}(\theta)+O(\varepsilon^3),
\]
where \(f_i^{(2)}\) is their Eq. (55), equivalently Eq. (8) in the main text.

There is an explicit globally phase-equivariant cubic physical counterterm that removes the **entire**
\(f_i^{(2)}\), not only its explicit nonpairwise harmonics.

For a fixed \(i\), let \(j,k\) be the other two indices and define
\[
\begin{aligned}
Q_i(z)={}&e^{2i\rho}\Big[
 w_{ij}w_{ji}|z_j|^2z_i+w_{ik}w_{ki}|z_k|^2z_i
 +w_{ij}w_{jk}|z_i|^2z_k+w_{ik}w_{kj}|z_i|^2z_j\\
&\hspace{30mm}-2w_{ij}w_{ik}z_jz_k\bar z_i\Big]\\
&+\big(w_{ij}w_{ji}-w_{ij}^2e^{2i\rho}\big)z_j^2\bar z_i
 +\big(w_{ik}w_{ki}-w_{ik}^2e^{2i\rho}\big)z_k^2\bar z_i\\
&+w_{ij}w_{jk}z_j^2\bar z_k
 +w_{ik}w_{kj}z_k^2\bar z_j .
\end{aligned}
\]

Modify the physical system by
\[
\boxed{
\dot z_i=(a+ib)z_i-|z_i|^2z_i
+\varepsilon e^{i\rho}\sum_{\ell\ne i}w_{i\ell}z_\ell
-\frac{\varepsilon^2}{4a^2}Q_i(z).
}
\]
Then, in the same phase convention as the cited second-order calculation,
\[
\boxed{
\dot\theta_i=b+\varepsilon F_i^{(1)}(\theta)+O(\varepsilon^3)
}
\]
for all three components. Thus the complete order-\(\varepsilon^2\) correction can be physically counteracted by resonant cubic coupling.

## Proof

The uncoupled limit cycle has radius \(R=\sqrt a\). For an additive cubic monomial
\[
C\,z_pz_q\bar z_r
\]
in the \(i\)-th physical equation, its tangent phase contribution on the unperturbed torus is
\[
\frac1R\operatorname{Im}\!\left(
e^{-i\theta_i}C z_pz_q\bar z_r
\right)
=
a\,\operatorname{Im}\!\left(
C e^{i(\theta_p+\theta_q-\theta_r-\theta_i)}
\right).
\]
Because the added counterterm is already of order \(\varepsilon^2\), only this projection on the unperturbed torus contributes at order \(\varepsilon^2\); evaluating it on the order-\(\varepsilon\) deformation produces only order-\(\varepsilon^3\) terms.

Write the source's second-order term as
\[
f_i^{(2)}=\frac{S_i}{4a}.
\]
Expanding Eq. (55) for the two indices \(j,k\ne i\) gives
\[
\begin{aligned}
S_i={}&
w_{ij}w_{ji}\{\sin 2\rho+\sin 2(\theta_j-\theta_i)\}\\
&+w_{ij}w_{jk}\{
\sin(\theta_k-\theta_i+2\rho)
+\sin(2\theta_j-\theta_k-\theta_i)\}\\
&+w_{ik}w_{ki}\{\sin 2\rho+\sin 2(\theta_k-\theta_i)\}\\
&+w_{ik}w_{kj}\{
\sin(\theta_j-\theta_i+2\rho)
+\sin(2\theta_k-\theta_j-\theta_i)\}\\
&-w_{ij}^2\sin(2(\theta_j-\theta_i)+2\rho)
-2w_{ij}w_{ik}\sin(\theta_j+\theta_k-2\theta_i+2\rho)\\
&-w_{ik}^2\sin(2(\theta_k-\theta_i)+2\rho).
\end{aligned}
\]

Now evaluate \(Q_i\) on \(z_\ell=Re^{i\theta_\ell}\). Term by term,
\[
\frac1R\operatorname{Im}\!\left(e^{-i\theta_i}Q_i\right)=aS_i.
\]
Consequently the counterterm contributes
\[
-\frac{1}{4a^2}\,aS_i=-\frac{S_i}{4a}=-f_i^{(2)}
\]
to the second-order phase equation. This cancels Eq. (55) identically.

## A missing cubic pairwise harmonic

The same calculation exposes a small but consequential gap in the source's enumeration of resonant cubic pairwise couplings. Its general resonant monomial
\[
G_i^{\rm cub}=e^{i\xi}w_{ipqr}z_pz_q\bar z_r
\]
also allows
\[
p=q=j,\qquad r=i,
\]
namely
\[
G_i\propto z_j^2\bar z_i.
\]
Its first-order phase harmonic is
\[
\boxed{
\sin\!\big(2(\theta_j-\theta_i)+\xi\big),
}
\]
which is a genuine pairwise second harmonic. This case is not among the two nonlinear pairwise cases listed in Eqs. (59)--(60) of the source. It is precisely the cubic control direction needed to cancel the second-harmonic pieces in Eqs. (50a), (50c), (53a), and (53c).

## Consequence for coupling design

The partial cancellation reported in the source is therefore not a structural obstruction of resonant cubic coupling. It follows from the narrower design ansatz that uses only the two explicitly nonpairwise cubic families with a common strength. If one allows the full globally phase-equivariant cubic basis—including nonlinear pairwise and phase-independent terms—then the first-order Kuramoto--Sakaguchi phase model can be recovered through second order:
\[
\dot\theta=b\mathbf 1+\varepsilon F^{(1)}(\theta)+O(\varepsilon^3).
\]

Even within the source's nonpairwise-only ansatz, its three explicit nonpairwise harmonics can all be canceled with one common scale \(\eta=\varepsilon^2/(4a)\) by choosing their physical weights to match the quadratic network products:
\[
w_{ijjk}^{\rm phys}=w_{ij}w_{jk},\qquad
w_{ikkj}^{\rm phys}=w_{ik}w_{kj},\qquad
w_{ijki}^{\rm phys}=2w_{ij}w_{ik},
\]
with the phase choices used in the source. What cannot be removed by that restricted ansatz are the remaining pairwise and phase-independent second-order terms.

## Verification

`artifacts/verify_counterterm.py` directly evaluates the source's Eq. (55) and the tangent projection of the cubic counterterm on a deterministic grid for all three oscillator components. It reports
```
max_abs_residual=4.441e-16
checks=375
```
in double precision.

## Scope and limitations

The theorem is an order-by-order phase-reduction statement, not an exact equality of the full physical flows at finite \(\varepsilon\). It applies to the explicit straight-isochrone, \(c=-1\), \(d=0\), three-oscillator setting for which the source gives Eq. (55). It does not compute the order-\(\varepsilon^3\) remainder or prove that a particular laboratory implementation can realize every complex cubic coefficient.

General synchronization engineering and the fact that nonlinear feedback can synthesize prescribed phase harmonics are established ideas and are not claimed as new. The source-specific contributions here are the complete cubic counterterm for its explicit second-order correction, the identification of the omitted \(z_j^2\bar z_i\) pairwise second-harmonic case, and the conclusion that second-order cancellation is complete in the enlarged resonant-cubic design space.

## Sources

- R. Muolo, H. Nakao, and C. Bick, *Physical and emergent nonpairwise interactions in oscillator networks: from higher-order phase reduction to coupling design*, arXiv:2609.20632v1 (2026). https://arxiv.org/abs/2609.20632
- H. Kori, C. G. Rusin, I. Z. Kiss, and J. L. Hudson, *Synchronization engineering: theoretical framework and application to dynamical clustering*, Chaos 18, 026111 (2008). https://doi.org/10.1063/1.2927531
- E. T. K. Mau, O. E. Omel'chenko, and M. Rosenblum, *Phase reduction explains chimera shape: When multibody interaction matters*, Phys. Rev. E 110, L022201 (2024). https://doi.org/10.1103/PhysRevE.110.L022201
