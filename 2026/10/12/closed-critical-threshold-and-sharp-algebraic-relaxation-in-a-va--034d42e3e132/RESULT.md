# Closed critical threshold and sharp algebraic relaxation in a vaccinated SEIR model

## Finding

For zero infected inflow, the reduced model studied by Witbooi, Vyambwera, and Nsuami is
\[
\dot S=A_0-\theta(I)SE-\mu_0S,
\]
\[
\dot E=\theta(I)SE-\mu_1E,
\qquad
\dot I=\alpha E-\mu_2I,
\]
with
\[
\mu_0=\mu+z,
\quad
\mu_1=\mu+\delta_1+\alpha+\omega_1,
\quad
\mu_2=\mu+\delta_2+\omega_2.
\]
The source assumes that \(\theta\) is positive, continuously differentiable, and nonincreasing.

The disease-free equilibrium is
\[
(S_0,0,0),
\qquad
S_0=\frac{A_0}{\mu_0},
\]
and the source defines
\[
\mathcal R_0
=
\frac{\theta(0)A_0}{\mu_0\mu_1}.
\]
Its Theorem 3 proves global asymptotic stability only for
\[
\mathcal R_0<1.
\]

At the omitted boundary
\[
\mathcal R_0=1,
\]
the disease-free equilibrium is still globally asymptotically stable. More sharply, if
\[
E(0)>0,
\]
then the convergence is generically algebraic with an exact full infected-state profile.

Write
\[
\theta_0=\theta(0),
\qquad
\theta_1=\theta'(0)\le0,
\]
\[
d=\frac{\mu_1}{\mu_0},
\qquad
h=\frac{\alpha}{\mu_2},
\]
and
\[
K
=
\frac{\theta_0\mu_1}{\mu_0}
-
S_0\theta_1\frac{\alpha}{\mu_2}.
\]
Because \(\theta_0,\mu_1,\mu_0>0\) and \(\theta_1\le0\),
\[
K>0.
\]

Every critical solution in the source's invariant region with \(E(0)>0\) satisfies
\[
tE(t)\longrightarrow\frac1K,
\]
\[
tI(t)\longrightarrow\frac{h}{K},
\]
and
\[
t\bigl(S_0-S(t)\bigr)\longrightarrow\frac{d}{K}.
\]

Thus the exposed class has a logarithmically divergent cumulative tail,
\[
\int_0^tE(s)\,ds
\sim
\frac{\log t}{K}.
\]
Moreover,
\[
\int_0^t\theta(I(s))S(s)E(s)\,ds
\sim
\frac{\mu_1}{K}\log t,
\]
and
\[
\int_0^t\alpha E(s)\,ds
\sim
\frac{\alpha}{K}\log t.
\]

The coefficient \(K\) separates two mechanisms. The term
\[
\frac{\theta_0\mu_1}{\mu_0}
\]
comes from susceptible depletion around the vaccinated disease-free state, while
\[
-S_0\theta_1\frac{\alpha}{\mu_2}
\]
is the additional critical damping produced by the local behavioral decrease in contact rate.

## Assumptions and scope

Assume
\[
A_1=0,
\]
all demographic and transition rates in the source are positive except that the vaccination rate may be nonnegative, and
\[
\theta(I)>0,\qquad \theta'(I)\le0.
\]
The critical condition is
\[
\theta_0S_0=\mu_1.
\]

The sharp profile requires \(E(0)>0\). If \(E(0)=0\), then \(E(t)\equiv0\); the infected component \(I\) decays exponentially and the \(t^{-1}\) law is not applicable.

The result concerns the deterministic reduced \((S,E,I)\) system used by the source for its threshold analysis. The recovered compartment is a stable linear equation forced by these variables and therefore converges to its corresponding disease-free value.

## Proof

Define
\[
L(S,E)
=
S-S_0
+
S_0\log\frac{S_0}{S}
+
E.
\]
This is nonnegative and vanishes only when
\[
S=S_0,\qquad E=0.
\]

At the critical threshold,
\[
\theta_0S_0=\mu_1.
\]
Using
\[
A_0=\mu_0S_0,
\]
direct differentiation gives
\[
\dot L
=
-\frac{\mu_0(S-S_0)^2}{S}
+
E\bigl(S_0\theta(I)-\mu_1\bigr).
\]
Hence
\[
\dot L
=
-\frac{\mu_0(S-S_0)^2}{S}
-
S_0E\bigl(\theta_0-\theta(I)\bigr)
\le0.
\]

The source provides a bounded positively invariant region. A sublevel set of \(L\) also stays away from \(S=0\), because the logarithmic term diverges there. LaSalle's invariance argument therefore gives
\[
S(t)\to S_0,
\qquad
E(t)\to0.
\]
Indeed, if a trajectory remained in the zero-derivative set with \(S=S_0\) and \(E>0\), then
\[
\dot S=-\theta(I)S_0E<0,
\]
so it would immediately leave that set. Finally,
\[
\dot I=\alpha E-\mu_2I
\]
is a stable linear equation with forcing tending to zero, so
\[
I(t)\to0.
\]

The same Lyapunov function controls \(E\) and the susceptible displacement, while the variation-of-constants formula controls \(I\), giving Lyapunov stability as well as global attraction. Thus the disease-free equilibrium is globally asymptotically stable at
\[
\mathcal R_0=1.
\]

For the sharp rate, set
\[
x=S_0-S.
\]
Because \(E(0)>0\), positivity gives
\[
E(t)>0
\]
for every finite \(t\).

Since the state converges to the disease-free equilibrium,
\[
\frac{\dot E}{E}
=
\theta(I)S-\mu_1
\longrightarrow0.
\]

Define
\[
q_I=\frac{I}{E}.
\]
Then
\[
\dot q_I
=
\alpha
-
\left(
\mu_2+\frac{\dot E}{E}
\right)q_I,
\]
so
\[
q_I\longrightarrow
h=\frac{\alpha}{\mu_2}.
\]

Likewise,
\[
\dot x=-\mu_0x+\theta(I)(S_0-x)E.
\]
For
\[
q_S=\frac{x}{E},
\]
one gets
\[
\dot q_S
=
\theta(I)(S_0-x)
-
\left(
\mu_0+\frac{\dot E}{E}
\right)q_S.
\]
Therefore
\[
q_S\longrightarrow
d=\frac{\mu_1}{\mu_0}.
\]

Now
\[
\frac{\dot E}{E^2}
=
\frac{\theta(I)(S_0-x)-\theta_0S_0}{E}.
\]
Split this as
\[
\frac{\dot E}{E^2}
=
S_0
\frac{\theta(I)-\theta_0}{I}
\frac{I}{E}
-
\theta(I)\frac{x}{E}.
\]
Using differentiability of \(\theta\) at zero and the two ratio limits,
\[
\frac{\dot E}{E^2}
\longrightarrow
S_0\theta_1\frac{\alpha}{\mu_2}
-
\theta_0\frac{\mu_1}{\mu_0}
=
-K.
\]
Thus
\[
\left(\frac1E\right)'
\longrightarrow K.
\]
Dividing by \(t\) gives
\[
tE(t)\longrightarrow\frac1K.
\]
Multiplication by the ratio limits yields the stated limits for \(I\) and \(S_0-S\).

Finally,
\[
E(t)\sim\frac1{Kt},
\]
so
\[
\int_0^tE(s)\,ds
\sim
\frac{\log t}{K}.
\]
The exposed balance
\[
\dot E=\theta(I)SE-\mu_1E
\]
then gives
\[
\int_0^t\theta(I)SE\,ds
=
E(t)-E(0)+\mu_1\int_0^tE(s)\,ds,
\]
which proves the local-infection cumulative law. Multiplying the exposed integral by \(\alpha\) gives the exposed-to-symptomatic law.

## Verification

A standalone checker evaluates an admissible critical example with
\[
\mu_0=2,\qquad
\mu_1=4,\qquad
\mu_2=3,\qquad
\alpha=1,
\qquad
S_0=4,
\]
and
\[
\theta(I)=\frac1{1+I/2}.
\]
Then
\[
\theta_0=1,\qquad
\theta_1=-\frac12,
\qquad
K=\frac83.
\]
The predicted limits are
\[
tE\to\frac38,\qquad
tI\to\frac18,\qquad
t(S_0-S)\to\frac34.
\]

The checker integrates the exact ODE and verifies convergence toward these constants. This numerical replay is corroborative only; the theorem is proved analytically above.

## Relationship to prior work

The motivating article states and proves disease-free global asymptotic stability for the strict condition
\[
\mathcal R_0<1.
\]
Its proof introduces a positive coefficient multiplying \(I\), which requires a strictly negative threshold margin and therefore does not cover equality.

Earlier nonlinear-contact epidemic literature already shows that equality-case disease-free global stability can hold in related SEI or SEIS models. In particular, Zhang, Li, and Xu explicitly prove global asymptotic stability for
\[
\mathcal R_0\le1
\]
in a different SEIS system with general saturation incidence. Therefore the mere closure of the threshold is not claimed as original.

The source-specific contribution here is the exact critical relaxation law for the vaccinated generalized-contact SEIR model:
\[
t(E,I,S_0-S)
\]
has an explicit nonzero vector limit, and the coefficient records both vaccination-sensitive susceptible restoration and the local derivative of behavioral contact reduction.

Two prior analyses of the same 2023 source are scientifically disjoint. One concerns endemic-equilibrium comparative statics under positive infected immigration, while another concerns the first Pontryagin costate in the controlled model. Neither statement covers or implies zero-importation critical dynamics.

Targeted searches using the source DOI and title, equality-threshold terminology, algebraic-decay terminology, critical-relaxation aliases, and generalized-contact SEIR language did not locate this exact asymptotic profile.

## Limitations

The theorem is tied to the source's differentiable nonincreasing contact function and its zero-importation case.

The coefficient uses only the first derivative \(\theta'(0)\). Higher-order asymptotics are not claimed.

The result concerns deterministic critical dynamics and does not address demographic or environmental stochasticity.

An equivalent asymptotic statement could exist under different notation in literature not surfaced by the targeted searches.

## References

1. P. J. Witbooi, S. M. Vyambwera, M. U. Nsuami, “Control and elimination in an SEIR model for the disease dynamics of COVID-19 with vaccination,” AIMS Mathematics 8 (2023), 8144–8161. DOI: 10.3934/math.2023411.
2. H. Zhang, Y. Li, W. Xu, “Global Stability of an SEIS Epidemic Model with General Saturation Incidence,” Abstract and Applied Analysis 2013, 710643. DOI: 10.1155/2013/710643.
3. G. Li, Z. Jin, “Global stability of an SEI epidemic model with general contact rate,” Chaos, Solitons & Fractals 23 (2005), 997–1004. DOI: 10.1016/j.chaos.2004.06.012.
