# Sharp critical relaxation in a population-dependent SIHR epidemic model

## Finding

The deterministic SIHR system of Jiao and Huang can be written as
\[
N'=A-\mu N-\mu_1I-\mu_2H,
\]
\[
I'=\beta(N)(N-I-H-R)I-(\gamma+\delta+\mu+\mu_1)I,
\]
\[
H'=\delta I-(m+\mu+\mu_2)H,
\qquad
R'=\gamma I+mH-\mu R.
\]

Let
\[
N_\star=\frac{A}{\mu},
\qquad
c=\gamma+\delta+\mu+\mu_1,
\qquad
f(N)=\beta(N)N.
\]
The source assumes
\[
\beta(N)>0,\qquad \beta'(N)\le0,\qquad f'(N)\ge0
\]
and works in an invariant region with
\[
N\le N_\star.
\]
Its reproduction number is
\[
\mathcal R_0=\frac{N_\star\beta(N_\star)}{c}.
\]

The source proves disease-free global asymptotic stability for
\[
\mathcal R_0<1.
\]
At the omitted critical value
\[
\mathcal R_0=1,
\]
the same equilibrium is still globally asymptotically stable, but it is nonhyperbolic and the infection tail is algebraic.

Define
\[
\beta_\star=\beta(N_\star),\qquad
a_H=m+\mu+\mu_2,\qquad
h=\frac{\delta}{a_H},
\]
\[
r=\frac{\gamma+mh}{\mu},\qquad
d=\frac{\mu_1+\mu_2h}{\mu},
\]
and
\[
K=\beta_\star(1+h+r)+d\,f'(N_\star).
\]
Then \(K>0\). For every critical solution in the source's invariant region with \(I(0)>0\),
\[
tI(t)\longrightarrow\frac1K,
\qquad
tH(t)\longrightarrow\frac{h}{K},
\]
\[
tR(t)\longrightarrow\frac{r}{K},
\qquad
t\bigl(N_\star-N(t)\bigr)\longrightarrow\frac{d}{K}.
\]

Thus
\[
\int_0^t I(s)\,ds\sim\frac{\log t}{K}.
\]
Because \(\beta(N)S\to c\),
\[
\int_0^t\beta(N(s))S(s)I(s)\,ds
\sim
\frac{c}{K}\log t.
\]
The cumulative confirmation flow similarly obeys
\[
\int_0^t\delta I(s)\,ds
\sim
\frac{\delta}{K}\log t.
\]

The critical threshold is therefore globally disease-free, but it has a mathematically distinct critical-slowing regime.

## Assumptions and scope

The result concerns the exact deterministic system and invariant region of the source. The contact function obeys the source hypotheses
\[
\beta:\mathbb R_+\to\mathbb R_+,
\qquad
\beta'(N)\le0,
\qquad
\frac{d}{dN}\bigl(\beta(N)N\bigr)\ge0.
\]
The demographic rate satisfies \(\mu>0\), and the source transition rates are nonnegative with
\[
a_H=m+\mu+\mu_2>0.
\]

The sharp \(t^{-1}\) law is stated for \(I(0)>0\). If \(I(0)=0\), the infection remains identically zero and the remaining stable linear subsystem converges exponentially.

No empirical parameter refit is made. The theorem concerns the critical deterministic dynamics of the printed model.

## Proof

At \(\mathcal R_0=1\),
\[
f(N_\star)=\beta(N_\star)N_\star=c.
\]
Since \(S=N-I-H-R\),
\[
I'
=
\bigl(
f(N)-f(N_\star)-\beta(N)(I+H+R)
\bigr)I.
\]
The invariant-region bound \(N\le N_\star\) and monotonicity of \(f\) give
\[
f(N)-f(N_\star)\le0.
\]
Since \(\beta\) is nonincreasing,
\[
\beta(N)\ge\beta(N_\star)=\beta_\star.
\]
Hence
\[
I'\le-\beta_\star I^2.
\]
For \(I(0)>0\),
\[
I(t)\le
\frac{I(0)}{1+\beta_\star I(0)t},
\]
so \(I(t)\to0\).

The equation
\[
H'=\delta I-a_HH
\]
is a stable linear filter of \(I\), hence \(H(t)\to0\). Then
\[
R'=\gamma I+mH-\mu R
\]
gives \(R(t)\to0\). With
\[
z=N_\star-N,
\]
the population equation is
\[
z'=-\mu z+\mu_1I+\mu_2H,
\]
so \(z(t)\to0\). This proves global attraction. Lyapunov stability follows from the same comparison system: \(I\) is nonincreasing and \(H\), \(R\), and \(z\) are stable linear equations with small forcing when the initial displacement is small.

For the sharp profile, \(I(t)>0\) for finite \(t\), and convergence of the state implies
\[
\frac{I'}I\to0.
\]
Set
\[
q_H=\frac HI.
\]
Then
\[
q_H'
=
\delta-
\left(
a_H+\frac{I'}I
\right)q_H,
\]
so
\[
q_H\to h=\frac{\delta}{a_H}.
\]

For
\[
q_R=\frac RI,
\]
\[
q_R'
=
\gamma+mq_H-
\left(
\mu+\frac{I'}I
\right)q_R,
\]
hence
\[
q_R\to r=\frac{\gamma+mh}{\mu}.
\]

For
\[
q_z=\frac zI,
\]
\[
q_z'
=
\mu_1+\mu_2q_H-
\left(
\mu+\frac{I'}I
\right)q_z,
\]
so
\[
q_z\to d=\frac{\mu_1+\mu_2h}{\mu}.
\]

Divide the exact infected equation by \(I^2\):
\[
\frac{I'}{I^2}
=
\frac{f(N)-f(N_\star)}{I}
-
\beta(N)
\left(
1+\frac HI+\frac RI
\right).
\]
Differentiability of \(f\) at \(N_\star\) and \(z/I\to d\) give
\[
\frac{f(N)-f(N_\star)}{I}
\to
-d\,f'(N_\star).
\]
Together with the ratio limits,
\[
\frac{I'}{I^2}\to-K.
\]
Therefore
\[
\left(\frac1I\right)'\to K
\]
and
\[
tI(t)\to\frac1K.
\]
The remaining state limits follow by multiplication with \(h\), \(r\), and \(d\). The logarithmic integral laws follow from \(I(t)\sim1/(Kt)\) and \(\beta(N)S\to c\).

## Verification

The proof is analytic and does not infer infinite-time behavior from a finite computation.

The bundled checker verifies symbolically that the critical Jacobian has one simple zero eigenvalue and all remaining eigenvalues have negative real part. It also verifies the ratio-equation identities and the algebraic expression for \(K\).

A numerical critical replay with an admissible contact function is included only as a consistency check. It confirms convergence of
\[
tI,\quad tH,\quad tR,\quad t(N_\star-N)
\]
toward the analytic constants. The general theorem is established by the exact inequalities and limits above.

## Relationship to prior work

Jiao and Huang derive the model, its invariant region, and \(\mathcal R_0\), and prove global disease-free stability only for \(\mathcal R_0<1\). Their Appendix proof takes \(V=I\) and closes with a strict negative estimate. It does not discuss the equality case or a critical relaxation law.

Hou, Lan, Yuan, and Zhang later reproduce the deterministic SIHR transition graph as the basis of a stochastic model. Their introduction again summarizes deterministic disease-free stability for \(\mathcal R_0<1\) and endemicity for \(\mathcal R_0>1\), then turns to stochastic threshold dynamics.

Zhang and Ma's earlier SEIR work with saturating contact rate already states global disease-free stability for \(\mathcal R_0\le1\) in a different model. Accordingly, equality-case global stability by itself is not claimed as new. The result here is the exact source-specific SIHR critical profile and its coefficient
\[
K=\beta_\star(1+h+r)+d\,f'(N_\star),
\]
which records hospitalization, recovery, disease-induced population deficit, and the slope of the population-dependent contact law.


## Limitations

The exact \(t^{-1}\) profile requires positive initial infection. The theorem uses the source's contact-function differentiability and invariant-region assumptions.

The result is deterministic and does not analyze the stochastic equality case of the 2022 follow-up.

Only indexed abstract-level material was available in the bounded comparison for the 2003 Zhang–Ma SEIR paper. That abstract establishes equality-case global stability but does not expose a source-specific SIHR relaxation coefficient. Additional rate information in inaccessible material remains a residual literature risk.

## References

1. S. Jiao, M. Huang, “An SIHR epidemic model of the COVID-19 with general population-size dependent contact rate,” AIMS Mathematics 5 (2020), 6714–6725. DOI: 10.3934/math.2020431.
2. T. Hou, G. Lan, S. Yuan, T. Zhang, “Threshold dynamics of a stochastic SIHR epidemic model of COVID-19 with general population-size dependent contact rate,” Mathematical Biosciences and Engineering 19 (2022), 4217–4236. DOI: 10.3934/mbe.2022195.
3. J. Zhang, Z. Ma, “Global dynamics of an SEIR epidemic model with saturating contact rate,” Mathematical Biosciences 185 (2003), 15–32. DOI: 10.1016/S0025-5564(03)00087-7.
