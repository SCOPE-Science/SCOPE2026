# Convex incidence creates bistability below the published SIR threshold

## Finding

Consider
\[
\begin{aligned}
S'&=B-\eta S-MIS(1+\gamma I)+\alpha R,\\
I'&=MIS(1+\gamma I)-(\mu+\eta)I,\\
R'&=\mu I-(\alpha+\eta)R,
\end{aligned}
\]
with positive parameters.

The disease-free equilibrium is
\[
E_0=\left(\frac{B}{\eta},0,0\right).
\]
Linearization in the infected direction gives
\[
\lambda_I=\frac{MB}{\eta}-(\mu+\eta),
\]
and therefore the invasion threshold of the printed vector field is
\[
\mathcal R_{\mathrm{inv}}
=
\frac{MB}{\eta(\mu+\eta)}.
\]

The source instead displays
\[
\widehat{\mathcal R}_0
=
\frac{MB}{\mu(B+\mu)}.
\]
That expression is not the threshold obtained from the disease-free linearization.

There is a second, independent issue. Even the correct local condition
\[
\mathcal R_{\mathrm{inv}}<1
\]
does not imply absence of endemic equilibria.

Define
\[
K=\frac{B}{\eta},
\qquad
a=\frac{\mu+\eta}{M},
\qquad
c=1+\frac{\mu}{\alpha+\eta}.
\]
Every endemic equilibrium satisfies
\[
S=\frac{a}{1+\gamma I},
\qquad
R=\frac{\mu}{\alpha+\eta}I,
\]
and its infected coordinate solves
\[
c\gamma I^2+(c-K\gamma)I+(a-K)=0.
\]

When
\[
\mathcal R_{\mathrm{inv}}=\frac{K}{a}<1,
\]
there are two distinct positive endemic equilibria exactly when
\[
\gamma>\gamma_{\mathrm{SN}},
\]
where
\[
\gamma_{\mathrm{SN}}
=
\frac{c\left(\sqrt a+\sqrt{a-K}\right)^2}{K^2}.
\]
At equality there is one double positive endemic equilibrium, and below that value there is none.

For
\[
B=\eta=\mu=M=\alpha=1,
\qquad
\gamma=10,
\]
both the source's displayed threshold and the invasion threshold equal
\[
\frac12.
\]
Nevertheless, the system has
\[
E_-=
\left(\frac34,\frac16,\frac1{12}\right)
\]
and
\[
E_+=
\left(\frac25,\frac25,\frac15\right)
\]
as positive endemic equilibria. The disease-free equilibrium and \(E_+\) are locally asymptotically stable, while \(E_-\) is a saddle. Thus the model has local disease-free/endemic bistability with a below-one threshold.

## Assumptions and scope

All parameters are positive. The claim concerns the ordinary differential equation system printed in the motivating source.

The term “backward bifurcation” is used in the standard epidemiological sense that a stable disease-free state and a stable endemic state coexist while the invasion threshold is below one. The exact witness establishes this coexistence directly; no numerical continuation is required.

The result does not claim novelty for backward bifurcation itself. Earlier nonlinear-incidence epidemic models already exhibit that phenomenon.

## Proof

Adding the three equations gives
\[
(S+I+R)'=B-\eta(S+I+R).
\]
Hence every equilibrium obeys
\[
S+I+R=K,
\qquad
K=\frac{B}{\eta}.
\]

At an endemic equilibrium \(I>0\), the infected equation gives
\[
MS(1+\gamma I)=\mu+\eta,
\]
so
\[
S=\frac{a}{1+\gamma I},
\qquad
a=\frac{\mu+\eta}{M}.
\]
The recovered equation gives
\[
R=\frac{\mu}{\alpha+\eta}I.
\]
With
\[
c=1+\frac{\mu}{\alpha+\eta},
\]
the total-population identity becomes
\[
\frac{a}{1+\gamma I}+cI=K.
\]
Multiplication by \(1+\gamma I\) gives
\[
c\gamma I^2+(c-K\gamma)I+(a-K)=0.
\]

The disease-free infected eigenvalue is
\[
MK-(\mu+\eta),
\]
so
\[
\mathcal R_{\mathrm{inv}}
=
\frac{MK}{\mu+\eta}
=
\frac{K}{a}.
\]

Assume
\[
\mathcal R_{\mathrm{inv}}<1.
\]
Then \(a>K\). The endemic quadratic has two positive roots precisely when its root sum is positive and its discriminant is positive:
\[
K\gamma>c
\]
and
\[
(K\gamma-c)^2>4c\gamma(a-K).
\]
The discriminant vanishes at
\[
\gamma_\pm
=
\frac{c\left(\sqrt a\pm\sqrt{a-K}\right)^2}{K^2}.
\]
The positivity condition \(K\gamma>c\) selects the upper branch, yielding
\[
\gamma>\gamma_+=\gamma_{\mathrm{SN}}.
\]

For the exact witness,
\[
K=1,\qquad a=2,\qquad c=\frac32,
\]
so
\[
\gamma_{\mathrm{SN}}
=
\frac32(1+\sqrt2)^2
=
\frac92+3\sqrt2
<
10.
\]
The endemic equation becomes
\[
30I^2-17I+2=0
=
(6I-1)(5I-2),
\]
so
\[
I=\frac16
\quad\text{or}\quad
I=\frac25.
\]
Substitution yields the two equilibria in the finding.

At \(E_0\), the characteristic polynomial is
\[
(\lambda+1)^2(\lambda+2).
\]
At \(E_-\), it is
\[
\frac{\lambda+1}{36}
\left(
36\lambda^2+43\lambda-42
\right),
\]
whose quadratic factor has one positive root. At \(E_+\), it is
\[
\frac{\lambda+1}{5}
\left(
5\lambda^2+12\lambda+14
\right),
\]
whose quadratic roots have real part \(-6/5\). Therefore \(E_0\) and \(E_+\) are locally asymptotically stable and \(E_-\) is a saddle.

## Verification

The bundled `verify.py` uses exact symbolic arithmetic. It checks the two reproduction-number formulas, the saddle-node value, all three equilibria, and all three characteristic polynomials.

It verifies that
\[
\widehat{\mathcal R}_0
=
\mathcal R_{\mathrm{inv}}
=
\frac12
\]
for the counterexample, so the contradiction does not depend on choosing between the source's displayed threshold and the threshold reconstructed from its vector field.

No finite experiment is used to infer the general equilibrium classification.

## Relationship to prior work

The motivating article prints the three-compartment model, a reproduction number, the statement that no positive equilibrium exists below threshold, and a global-attraction claim for the disease-free state in that regime.

Backward bifurcation under convex or nonlinear incidence is established in earlier epidemic literature. Buonomo and Lacitignola study a convex-incidence SEIR system and report conditions for backward bifurcation. Chinviriyasit, Janreung, and Chinviriyasit study a nonlinear-incidence SEIRS model and explicitly describe coexistence of stable disease-free and endemic states below one.

Those works establish the general phenomenon as prior art, but they do not supply the exact quadratic classification for the motivating SIR model or the rational equilibria above.

## Limitations

The result does not provide a complete global phase portrait or a full basin classification for every parameter choice.

The sharp formula \(\gamma_{\mathrm{SN}}\) classifies positive endemic equilibria in the regime \(\mathcal R_{\mathrm{inv}}<1\). Additional questions such as periodic dynamics are not addressed.

The exact witness proves local bistability but does not compute the complete separatrix between the two attracting states.

## References

1. R. ud Din, K. Shah, M. A. Alqudah, T. Abdeljawad, F. Jarad, “Mathematical study of SIR epidemic model under convex incidence rate,” AIMS Mathematics 5 (2020), 7548–7561. DOI: 10.3934/math.2020483.
2. B. Buonomo, D. Lacitignola, “On the dynamics of an SEIR epidemic model with a convex incidence rate,” Ricerche di Matematica 57 (2008), 261–281. DOI: 10.1007/s11587-008-0039-4.
3. W. Chinviriyasit, S. Janreung, S. Chinviriyasit, “On the Backward Bifurcation of an SEIRS Epidemic Model with Nonlinear Incidence Rate,” WSEAS Transactions on Systems 17 (2018), 221–227.
