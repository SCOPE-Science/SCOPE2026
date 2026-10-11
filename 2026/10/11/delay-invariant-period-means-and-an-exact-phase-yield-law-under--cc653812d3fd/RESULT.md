# Delay-invariant period means and an exact phase–yield law under additive predation

## Finding
Consider the delayed predator–prey model
\[
\dot u(t)=u(t)\left[r\left(1-\frac{u(t-\tau)}{K}\right)-\frac{a}{1+m u(t)}-\alpha v(t)\right],
\qquad
\dot v(t)=v(t)(\beta u(t)-d),
\]
with positive parameters and \(\tau\ge 0\). Let the positive coexistence equilibrium be \(E_*=(u_*,v_*)\), where
\[
u_* = \frac{d}{\beta},\qquad
v_* = \frac1\alpha\left[r\left(1-\frac{u_*}{K}\right)-\frac{a}{1+m u_*}\right]>0.
\]
For every strictly positive nonconstant \(T\)-periodic solution, define
\[
\bar f=\frac1T\int_0^T f(t)\,dt,\qquad u_\tau(t)=u(t-\tau),
\]
and
\[
Q=\overline{\frac{(u-u_*)^2}{1+m u}}.
\]
Then
\[
\bar u=u_*,\qquad
v_*-\bar v=\frac{a m^2}{\alpha(1+m u_*)^2}Q>0,
\]
and
\[
\alpha\operatorname{Cov}_T(u,v)+\frac rK\operatorname{Cov}_T(u,u_\tau)
=\frac{a m}{1+m u_*}Q
=\frac{\alpha(1+m u_*)}{m}(v_*-\bar v)>0.
\]
Thus delay may redistribute correlation between the current predator–prey pair and the lagged prey pair, while their weighted sum is exactly fixed by the predator mean deficit.

For the numerical delayed example in the source,
\[
(r,K,a,m,\alpha,\beta,d)=(1.2,45,1.25,1.5,0.2,0.04,0.2),
\]
so
\[
u_*=5,\qquad v_*=\frac{469}{102}=4.598039215686\ldots,
\]
and every strictly positive nonconstant periodic orbit satisfies
\[
\frac15\operatorname{Cov}_T(u,v)+\frac{2}{75}\operatorname{Cov}_T(u,u_\tau)
=\frac{17}{15}\left(\frac{469}{102}-\bar v\right)>0.
\]

## Assumptions and scope
All seven biological parameters are strictly positive, \(\tau\ge0\), and the coexistence equilibrium exists with \(v_*>0\). The solution is assumed strictly positive and exactly \(T\)-periodic. Covariance means
\[
\operatorname{Cov}_T(f,g)=\overline{fg}-\bar f\,\bar g.
\]
No small-amplitude, near-Hopf, or small-delay assumption is made. The theorem applies to every positive nonconstant periodic solution of the printed delayed model, wherever such a solution exists.

## Proof
Because \(v(t)>0\),
\[
\frac d{dt}\log v(t)=\beta u(t)-d.
\]
Integrating over one period gives \(\bar u=d/\beta=u_*\). Likewise,
\[
\frac d{dt}\log u(t)=r\left(1-\frac{u(t-\tau)}K\right)-\frac a{1+m u(t)}-\alpha v(t).
\]
A periodic average is invariant under time translation, so \(\overline{u(t-\tau)}=\bar u=u_*\). Hence
\[
\alpha\bar v=r\left(1-\frac{u_*}K\right)-a\overline{\frac1{1+m u}}.
\]
Subtracting this relation from the equilibrium identity yields
\[
v_* - \bar v=\frac a\alpha\left(\overline{\frac1{1+m u}}-\frac1{1+m u_*}\right).
\]
For every positive \(x\),
\[
\frac1{1+m x}=\frac1{1+m u_*}-\frac{m(x-u_*)}{(1+m u_*)^2}
+\frac{m^2(x-u_*)^2}{(1+m u_*)^2(1+m x)}.
\]
Averaging eliminates the linear term because \(\bar u=u_*\), giving the mean-defect formula. If \(Q=0\), then \(u\equiv u_*\); the predator equation gives \(v\) constant, and the prey equation then forces \(v\equiv v_*\). Thus a nonconstant positive cycle has \(Q>0\).

Next average the undivided prey equation:
\[
0=r\bar u-\frac rK\overline{u u_\tau}-a\overline{\frac u{1+m u}}-\alpha\overline{uv}.
\]
Subtract \(u_*\) times the averaged logarithmic prey equation. Since \(\bar u=u_*\),
\[
0=-\frac rK\operatorname{Cov}_T(u,u_\tau)-a\overline{\frac{u-u_*}{1+m u}}-\alpha\operatorname{Cov}_T(u,v).
\]
The exact identity
\[
\frac{x-u_*}{1+m x}=\frac{x-u_*}{1+m u_*}-\frac{m(x-u_*)^2}{(1+m u_*)(1+m x)}
\]
gives
\[
\overline{\frac{u-u_*}{1+m u}}=-\frac m{1+m u_*}Q.
\]
Substitution proves the covariance balance, and elimination of \(Q\) by the mean-defect formula gives its final form.

## Verification
The bundled checker verifies the two rational identities with exact rational arithmetic and verifies the source specialization
\[
u_*=5,\quad v_*=\frac{469}{102},\quad \frac rK=\frac{2}{75},\quad
\frac{a m}{1+m u_*}=\frac{15}{68},\quad
\frac{\alpha(1+m u_*)}{m}=\frac{17}{15}.
\]
The theorem is analytic; no finite simulation is used as proof of the universal statement.

## Relationship to prior work
Bai and Zhang introduce the nondelayed additive-predation model and derive a period-integral relation for that planar system. They then study the density-feedback delayed model by characteristic roots, Hopf bifurcation, normal forms, and numerical examples. Their delayed numerical example exhibits repeated stability switches and Hopf-generated periodic coexistence. The source does not state the delay-invariant period means or the exact lagged covariance phase–yield law above.

A later additive-predation study replaces logistic prey growth by a Smith growth function, and a 2025 extension adds predator intraspecific competition. Those changes alter the balance equations and do not imply this exact delayed logistic identity. Database searches using mean, covariance, lagged autocovariance, periodic-orbit, additive-predation, and density-feedback formulations did not locate an equivalent statement. Search failure is not treated as proof of novelty.

## Limitations
This is a necessary identity for strictly positive periodic solutions. It does not prove existence, uniqueness, orbital stability, Hopf direction, or basin structure, and it does not apply to boundary periodic solutions with \(v\equiv0\). It also does not characterize general nonperiodic recurrent dynamics. Originality assessment remains search-limited outside the directly related additive-predation literature.

## References
1. D. Bai and X. Zhang, “Dynamics of a Predator–Prey Model with the Additive Predation in Prey,” Mathematics 10 (2022), 655. DOI: 10.3390/math10040655.
2. D. Bai, J. Zheng and Y. Kang, “Global dynamics of a predator-prey model with a Smith growth function and the additive predation in prey,” Discrete and Continuous Dynamical Systems - B 29 (2024), 1923–1960. DOI: 10.3934/dcdsb.2023161.
3. D. Bai et al., “Impact of Intraspecific Competition of Predator on Coexistence of a Predator-Prey Model with Additive Predation on Prey,” SIAM Journal on Applied Dynamical Systems 24 (2025), 1191–1230. DOI: 10.1137/24M1685997.
