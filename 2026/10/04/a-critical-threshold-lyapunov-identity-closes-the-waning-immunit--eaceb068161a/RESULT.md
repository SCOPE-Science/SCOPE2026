# A critical-threshold Lyapunov identity closes the waning-immunity SARS-CoV-2 disease-free theorem

## Finding

Consider the seven-class SARS-CoV-2 model
\[
\begin{aligned}
\dot S&=\Lambda-\mu S-\beta S(E+A+\epsilon V)+\eta R,\\
\dot E&=\beta S(E+A+\epsilon V)-(p+q+\mu)E,\\
\dot A&=pE-(\gamma_A+\mu)A,\\
\dot V&=qE-(\kappa+\gamma_V+\mu+\delta)V,\\
\dot H&=\kappa V+\sigma C-(\alpha+\gamma_H+\mu+\delta)H,\\
\dot C&=\alpha H-(\sigma+\mu+\delta)C,\\
\dot R&=\gamma_AA+\gamma_VV+\gamma_HH-(\mu+\eta)R.
\end{aligned}
\]
Set
\[
S_*=\frac{\Lambda}{\mu},\qquad
\zeta_1=p+q+\mu,\qquad
\zeta_2=\gamma_A+\mu,\qquad
\zeta_3=\kappa+\gamma_V+\mu+\delta.
\]
The source works on the feasible region
\[
\Omega=\left\{(S,E,A,V,H,C,R)\ge0:\ S+E+A+V+H+C+R\le S_*\right\}.
\]
Its reproduction number is
\[
\mathcal R_0=
\frac{\beta S_*}{\zeta_1}
\left(1+\frac p{\zeta_2}+\frac{q\epsilon}{\zeta_3}\right).
\]

The source's Theorem 4 proves global asymptotic stability of the disease-free equilibrium only for \(\mathcal R_0<1\), while its conclusion states the closed condition \(\mathcal R_0\le1\). The equality case is not supplied by the printed proof. It can be closed exactly, and the same argument also reproves the strict case.

Define
\[
h=E+A+\epsilon V
\]
and
\[
\mathcal L
=
E+\frac{\beta S_*}{\zeta_2}A
+\frac{\beta\epsilon S_*}{\zeta_3}V.
\]
Then every solution in \(\Omega\) satisfies the exact identity
\[
\boxed{
\dot{\mathcal L}
=\beta(S-S_*)h
+\zeta_1(\mathcal R_0-1)E.}
\]
Therefore
\[
\mathcal R_0\le1
\quad\Longrightarrow\quad
\dot{\mathcal L}\le0.
\]
Moreover, within \(\Omega\), equality can occur only when
\[
E=A=V=0.
\]
LaSalle's invariance principle then gives
\[
E(t),A(t),V(t)\to0.
\]
The remaining hospital, ICU, and recovery equations form a stable linear cascade driven by these vanishing inputs, so
\[
H(t),C(t),R(t)\to0.
\]
Finally, the susceptible equation gives
\[
S(t)\to S_*.
\]
Thus the disease-free equilibrium
\[
\mathcal E_0=(S_*,0,0,0,0,0,0)
\]
is globally attracting for the full closed threshold \(\mathcal R_0\le1\).

It is also Lyapunov stable at the nonhyperbolic endpoint. Let
\[
d=S_*-S.
\]
Since the total population is at most \(S_*\), one has \(d\ge0\) and the sum of all nonsusceptible compartments is at most \(d\). Furthermore,
\[
\dot d
=-\mu d+\beta Sh-\eta R
\le-\mu d+\beta S_*h.
\]
Because all coefficients in \(\mathcal L\) are positive, there is a parameter-dependent constant \(M>0\) such that
\[
h\le M\mathcal L.
\]
As \(\mathcal L(t)\le\mathcal L(0)\),
\[
d(t)
\le d(0)e^{-\mu t}
+\frac{\beta S_*M}{\mu}\mathcal L(0)(1-e^{-\mu t}).
\]
Small initial displacement from \(\mathcal E_0\) therefore remains uniformly small. Combining stability with global attraction proves:
\[
\boxed{\mathcal E_0\text{ is globally asymptotically stable for every }\mathcal R_0\le1.}
\]
In particular, the equality claim in the source conclusion is correct, despite not being covered by its stated Theorems 3 and 4.

## Assumptions and scope

All parameters appearing as rates are positive, and the infectivity modifier satisfies \(0<\epsilon<1\), as in the source. The result is restricted to the source's feasible region \(\Omega\); this is the biologically relevant positively invariant set used in its dynamical analysis.

The theorem concerns the disease-free equilibrium and the threshold \(\mathcal R_0\le1\). It does not address the global stability of the endemic equilibrium when \(\mathcal R_0>1\), which the source itself leaves as a conjectural direction.

The endpoint \(\mathcal R_0=1\) is nonhyperbolic, so the result is not obtained by extending a strict linear stability inequality by continuity. The proof instead uses a nonlinear Lyapunov identity and invariance.

## Proof

Write
\[
S_*=\frac{\Lambda}{\mu},
\qquad
h=E+A+\epsilon V.
\]
The three compartments that directly enter the force of infection satisfy
\[
\dot E=\beta Sh-\zeta_1E,
\qquad
\dot A=pE-\zeta_2A,
\qquad
\dot V=qE-\zeta_3V.
\]
Differentiating \(\mathcal L\) gives
\[
\begin{aligned}
\dot{\mathcal L}
&=\beta Sh-\zeta_1E
+\frac{\beta S_*}{\zeta_2}(pE-\zeta_2A)
+\frac{\beta\epsilon S_*}{\zeta_3}(qE-\zeta_3V)\\
&=\beta Sh-\beta S_*(A+\epsilon V)
+\left[-\zeta_1+\frac{\beta S_*p}{\zeta_2}
+\frac{\beta\epsilon S_*q}{\zeta_3}\right]E.
\end{aligned}
\]
From the definition of \(\mathcal R_0\),
\[
\beta S_*
\left(1+\frac p{\zeta_2}+\frac{q\epsilon}{\zeta_3}\right)
=\zeta_1\mathcal R_0.
\]
Hence
\[
\dot{\mathcal L}
=\beta(S-S_*)h+\zeta_1(\mathcal R_0-1)E.
\]

On \(\Omega\), \(S\le S_*\). Thus \(\dot{\mathcal L}\le0\) whenever \(\mathcal R_0\le1\). If \(h>0\), then some nonsusceptible compartment is positive, so the population constraint gives \(S<S_*\). Therefore the first term is strictly negative. Consequently
\[
\dot{\mathcal L}=0
\quad\Longleftrightarrow\quad
h=0
\quad\Longleftrightarrow\quad
E=A=V=0.
\]
The feasible region is compact and positively invariant, so LaSalle's invariance principle implies that every trajectory approaches the invariant face \(E=A=V=0\); equivalently,
\[
E(t),A(t),V(t)\to0.
\]

The \((H,C)\)-subsystem has homogeneous matrix
\[
B=
\begin{pmatrix}
-(\alpha+\gamma_H+\mu+\delta)&\sigma\\
\alpha&-(\sigma+\mu+\delta)
\end{pmatrix}.
\]
Its trace is negative and
\[
\det B
=(\alpha+\gamma_H+\mu+\delta)(\sigma+\mu+\delta)-\alpha\sigma>0,
\]
so \(B\) is Hurwitz. Since its input \((\kappa V,0)^T\) tends to zero, variation of constants gives \(H,C\to0\). The scalar equation
\[
\dot R=\gamma_AA+\gamma_VV+\gamma_HH-(\mu+\eta)R
\]
then yields \(R\to0\). Finally,
\[
\dot S+\mu(S-S_*)=-\beta Sh+\eta R,
\]
and the right-hand side tends to zero, hence \(S\to S_*\).

It remains to verify stability at the critical endpoint. On \(\Omega\), set \(d=S_*-S\). Then every nonsusceptible component is bounded above by \(d\), and
\[
\dot d\le-\mu d+\beta S_*h.
\]
Because \(\mathcal L\) has strictly positive weights on \(E,A,V\), one may take
\[
M=
\max\left\{
1,
\frac{\zeta_2}{\beta S_*},
\frac{\zeta_3}{\beta S_*}
\right\}
\]
so that \(h\le M\mathcal L\). Therefore
\[
d(t)
\le d(0)e^{-\mu t}
+\frac{\beta S_*M}{\mu}\mathcal L(0)(1-e^{-\mu t}).
\]
Both \(d(0)\) and \(\mathcal L(0)\) tend to zero with the initial distance from \(\mathcal E_0\). This proves Lyapunov stability and completes the global asymptotic stability proof.

## Verification

The bundled script `verify.py` symbolically reconstructs the reproduction-number identity and differentiates the proposed functional from the source equations. It verifies exactly that
\[
\dot{\mathcal L}
-\beta(S-S_*)h
-\zeta_1(\mathcal R_0-1)E=0.
\]
It also checks the positivity decomposition of the hospital/ICU determinant and the source's feasibility implication \(S\le S_*\).

The computation is an algebraic replay only. Global convergence and Lyapunov stability are proved analytically above; no finite simulation is used as an infinite-time argument.

## Relationship to prior work

Egbelowo, Munyakazi, and Hoang (2022), DOI 10.3934/math.2022871, are the primary source. Their Theorem 3 proves local asymptotic stability only for \(\mathcal R_0<1\), and Theorem 4 proves global asymptotic stability only for \(\mathcal R_0<1\). Their conclusion nevertheless states that the disease-free equilibrium is globally asymptotically stable for \(\mathcal R_0\le1\). The functional above supplies the missing critical-threshold proof and independently recovers the strict-subthreshold conclusion.

Ottaviano, Sensi, and Sottile's multi-group SAIRS work, first posted as arXiv:2202.02993 and later published as DOI 10.1002/mma.9303, proves global disease-free stability at \(\mathcal R_0=1\) for an unvaccinated SAIRS model. That model has susceptible, asymptomatic, symptomatic, and recovered classes arranged by communities; it has no exposed, severe, hospital, or ICU cascade and no disease-induced population deficit. Its equality theorem therefore does not imply the seven-class result here. It shows that critical-threshold closure is mathematically meaningful in related epidemic systems, while the present weighted functional is specific to the source model.

## Limitations

The theorem is restricted to initial data in \(\Omega\), exactly the feasible region used by the source. It does not claim a rate of decay at \(\mathcal R_0=1\); the critical convergence can be slower than the exponential decay available strictly below threshold.

The argument does not settle global stability of the endemic equilibrium when \(\mathcal R_0>1\). It also does not validate the empirical parameter fit or forecasting aspects of the source.

## References

1. O. F. Egbelowo, J. B. Munyakazi, M. T. Hoang, “Mathematical study of transmission dynamics of SARS-CoV-2 with waning immunity,” AIMS Mathematics 7 (2022), 15917–15938. DOI: 10.3934/math.2022871.
2. S. Ottaviano, M. Sensi, S. Sottile, “Global stability of multi-group SAIRS epidemic models,” Mathematical Methods in the Applied Sciences 46 (2023), 12340–12360. arXiv:2202.02993; DOI: 10.1002/mma.9303.
