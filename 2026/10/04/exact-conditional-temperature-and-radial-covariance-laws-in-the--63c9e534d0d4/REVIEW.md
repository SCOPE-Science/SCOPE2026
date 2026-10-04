# Same-model review

## Correctness
PASS. For compactly supported invariant \(\mu\), the generator identity applied to arbitrary antiderivatives of continuous functions of \(z\) gives
\[
\mathbb E_\mu[y^2-a\mid z]=0.
\]
For \(a\ne0\), the exact identity \(LQ=-2az\), tested against arbitrary functions of \(Q\), gives
\[
\mathbb E_\mu[z\mid Q]=0.
\]
The polynomial identity
\[
L(zQ)=(y^2-a)Q-2az^2
\]
then gives
\[
\operatorname{Cov}_\mu(y^2,Q)
=
2a\,\mathbb E_\mu[z^2]
=
\frac{1}{2a}\mathbb E_\mu[(LQ)^2].
\]
For \(a>0\), strictness follows because a compact invariant support contained in \(z=0\) would force \(y^2=a\) along its complete trajectories and hence nonzero constant \(y\), making \(x\) unbounded. For \(a<0\), \(\mathbb E[y^2]=a\) is impossible; for \(a=0\), \(y=0\) almost surely and \(L(xy)=y^2-x^2-xyz\) forces \(x=0\). The packaged checker replays all critical algebraic identities exactly.

Scientific risk: the strictness argument uses the standard invariance of the support of an invariant measure for a continuous flow.

## Originality
PASS. The inspected full same-object papers establish the \(a=0\) invariant-sphere geometry, absence of invariant algebraic surfaces and polynomial first integrals for nonzero \(a\), and periodic/KAM/hidden-attractor phenomena. They do not state the final conditional laws or radial covariance defect. Targeted semantic searches used both Sprott A and Nosé–Hoover aliases and found only analogous balance laws for different vector fields or a different trigonometric Nosé–Hoover model.

Scientific risk: the 1986 oscillator source and 2004 analytical Sprott-flow source were not available for complete line-by-line inspection. The simple global thermostat average \(\mathbb E[y^2]=a\) is therefore not treated as the originality-bearing statement by itself.

## Value
PASS. The theorem directly addresses the geometry emphasized by the prior literature: at \(a=0\), radius is an exact first integral, while for \(a\ne0\) the invariant spheres disappear. The identity
\[
\operatorname{Cov}_\mu(y^2,Q)
=
\frac{1}{2a}\mathbb E_\mu[(LQ)^2]
\]
quantifies that loss for every compact recurrent statistical state, not only one numerically observed attractor. The conditional laws and complete nonpositive-parameter classification give additional global recurrence constraints, while the forced sign and amplitude excursions apply to every compact recurrent component and every periodic orbit.

Same-model review: passed. Independent audit: not yet performed.
