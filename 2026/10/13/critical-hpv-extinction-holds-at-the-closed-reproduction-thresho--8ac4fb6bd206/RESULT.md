# Critical HPV extinction holds at the closed reproduction threshold

## Finding

For the HPV model
\[
\begin{aligned}
\dot S&=\Lambda+\delta R-\lambda(t)S-dS,\\
\dot E&=\lambda(t)S+\alpha_4I_1-(\alpha+\gamma_1+d)E,\\
\dot I_1&=\alpha E+\alpha_3I_2-(\alpha_1+\alpha_4+\gamma_2+d)I_1,\\
\dot I_2&=\alpha_1I_1-(\alpha_3+\alpha_2+d)I_2,\\
\dot A&=\alpha_2I_2-(\delta_1+d)A,\\
\dot R&=\gamma_1E+\gamma_2I_1-(\delta+d)R,
\end{aligned}
\]
with
\[
\lambda(t)=
\frac{\beta_1E+\beta_2I_1+\beta_3I_2}{N},
\qquad
N=S+E+I_1+I_2+A+R,
\]
the disease-free equilibrium
\[
X_0=
\left(\frac{\Lambda}{d},0,0,0,0,0\right)
\]
is globally asymptotically stable on the source's feasible region for the closed condition
\[
\mathcal R_0\le1.
\]

The source states and proves this only for
\[
\mathcal R_0<1.
\]
The missing equality case is nonhyperbolic, but the nonlinear standard-incidence factor supplies strict decay away from the disease-free set.

## Assumptions and scope

All epidemiological rates appearing above are positive, as in the source model. Initial data lie in the source's positively invariant region
\[
\Omega=
\left\{
(S,E,I_1,I_2,A,R)\ge0:
S+E+I_1+I_2+A+R\le\frac{\Lambda}{d}
\right\}.
\]

The reproduction number \(\mathcal R_0\) is the next-generation threshold defined by the source.

The result concerns disease-free global asymptotic stability. It does not assess the source's separate nonexistence-of-limit-cycles argument or its later optimal-control problem.

## Proof

Define
\[
q_E=\alpha+\gamma_1+d,
\qquad
q_1=\alpha_1+\alpha_4+\gamma_2+d,
\qquad
q_2=\alpha_3+\alpha_2+d,
\]
and set
\[
y=(E,I_1,I_2)^{\mathsf T},
\qquad
\Phi=\beta_1E+\beta_2I_1+\beta_3I_2.
\]

At the disease-free susceptible fraction \(S/N=1\), the infectious core has Metzler matrix
\[
A_0=
\begin{pmatrix}
\beta_1-q_E & \beta_2+\alpha_4 & \beta_3\\
\alpha & -q_1 & \alpha_3\\
0 & \alpha_1 & -q_2
\end{pmatrix}.
\]

The source computes \(\mathcal R_0\) by the next-generation construction. The standard next-generation threshold theorem gives
\[
\mathcal R_0<1
\iff
s(A_0)<0,
\qquad
\mathcal R_0=1
\iff
s(A_0)=0.
\]
Because all transition rates linking \(E\), \(I_1\), and \(I_2\) are positive, \(A_0\) is irreducible. Let \(w>0\) be a positive left Perron vector:
\[
w^{\mathsf T}A_0=s(A_0)w^{\mathsf T}.
\]

The nonlinear infectious core is exactly
\[
\dot y
=
A_0y
-
\left(1-\frac SN\right)
\begin{pmatrix}
\Phi\\0\\0
\end{pmatrix}.
\]
Hence for
\[
L=w^{\mathsf T}y
\]
one obtains
\[
\dot L
=
s(A_0)L
-
w_1\left(1-\frac SN\right)\Phi.
\]

If
\[
\mathcal R_0\le1,
\]
then \(s(A_0)\le0\), so \(\dot L\le0\). At the critical value, if \(y\ne0\), positivity of the transmission coefficients gives \(\Phi>0\), while
\[
N-S\ge E+I_1+I_2>0
\]
gives \(S/N<1\). Thus
\[
\dot L<0
\]
whenever the infectious core is nonzero, even when \(s(A_0)=0\).

The feasible region is compact and positively invariant. LaSalle's invariance principle therefore gives
\[
E(t),I_1(t),I_2(t)\to0.
\]
The remaining infected downstream compartment satisfies
\[
\dot A=\alpha_2I_2-(\delta_1+d)A,
\]
and the recovered compartment satisfies
\[
\dot R=\gamma_1E+\gamma_2I_1-(\delta+d)R.
\]
Both are stable linear filters of inputs tending to zero, so
\[
A(t),R(t)\to0.
\]
Finally,
\[
\dot S=\Lambda+\delta R-\lambda(t)S-dS
\]
is asymptotically the stable scalar equation
\[
\dot S=\Lambda-dS,
\]
hence
\[
S(t)\to\frac{\Lambda}{d}.
\]

For completeness, the critical Perron vector can be written explicitly. At
\[
\mathcal R_0=1,
\]
the determinant condition \(\det A_0=0\) is equivalent to
\[
(q_E-\beta_1)(q_1q_2-\alpha_1\alpha_3)
=
\alpha\left[q_2(\beta_2+\alpha_4)+\alpha_1\beta_3\right].
\]
Since
\[
q_1q_2>\alpha_1\alpha_3,
\]
this forces
\[
q_E>\beta_1.
\]
Then
\[
w=
\left(
\alpha q_2,\;
q_2(q_E-\beta_1),\;
\alpha\beta_3+\alpha_3(q_E-\beta_1)
\right)
\]
has strictly positive components and satisfies
\[
w^{\mathsf T}A_0=0.
\]

It remains to record Lyapunov stability at the critical equilibrium. Let
\[
m=\min_i w_i>0.
\]
Since \(L(t)\le L(0)\),
\[
E+I_1+I_2
\le
\frac{L(0)}{m}.
\]
The equations for \(A\) and \(R\) give uniform small-input bounds. On \(\Omega\), define
\[
z=\frac{\Lambda}{d}-S\ge0.
\]
Then
\[
\dot z
=
-dz-\delta R+\lambda S
\le
-dz+\Phi.
\]
Since \(\Phi\) is bounded by a fixed multiple of \(L(0)\), \(z(t)\) remains uniformly small whenever the initial displacement is small. This proves Lyapunov stability and completes global asymptotic stability.

## Verification

The bundled `verify.py` symbolically reconstructs \(A_0\), the critical determinant identity, and the explicit positive left-null vector.

It verifies
\[
w^{\mathsf T}A_0
=
\left(0,\det A_0,0\right)
\]
for the displayed \(w\). Thus at the critical threshold \(\det A_0=0\), the claimed left-null identity is exact.

The checker also verifies that
\[
\det A_0=0
\]
is algebraically equivalent to the displayed positive identity for \(q_E-\beta_1\).

No numerical trajectory or finite parameter experiment is used in the proof.

## Relationship to prior work

The motivating article formulates the six-compartment HPV model, computes its next-generation reproduction number, and proves global asymptotic stability of the disease-free equilibrium under the strict condition
\[
\mathcal R_0<1.
\]
It separately derives a forward bifurcation at the unit threshold. The equality case is not included in its global-stability theorem.

Earlier HPV threshold literature establishes global disease-free stability in more elaborate age- and sex-structured vaccination models under model-specific additional conditions. Those results concern different systems and do not imply the critical equality case for this six-compartment treatment model.

Searches by the motivating DOI, exact title, critical-threshold terminology, equality-case global stability, and equivalent Perron/Lyapunov formulations did not locate a published statement of this source-specific closed-threshold theorem.

## Limitations

The proof relies on the source model's standard incidence and positivity of the infectious transition rates.

It establishes the disease-free threshold
\[
\mathcal R_0\le1
\]
but does not characterize global dynamics for
\[
\mathcal R_0>1.
\]

The result does not validate or repair the article's separate multidimensional Dulac–Bendixson argument or its optimal-control derivation.

## References

1. K. Zhang, Y. Ji, Q. Pan, Y. Wei, Y. Ye, H. Liu, “Sensitivity analysis and optimal treatment control for a mathematical model of Human Papillomavirus infection,” AIMS Mathematics 5 (2020), 2646–2670. DOI: 10.3934/math.2020172.
2. T. Malik, A. Gumel, E. H. Elbasha, “Qualitative analysis of an age- and sex-structured vaccination model for human papillomavirus,” Discrete and Continuous Dynamical Systems - B 18 (2013), 2151–2174. DOI: 10.3934/dcdsb.2013.18.2151.
