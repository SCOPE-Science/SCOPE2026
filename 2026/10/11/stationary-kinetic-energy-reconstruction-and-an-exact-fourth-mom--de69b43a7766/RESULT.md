# Stationary kinetic-energy reconstruction and an exact fourth-moment law for the van der Pol oscillator
## Finding
Consider the van der Pol oscillator
\[
\dot x=v,\qquad
\dot v=\mu(1-x^2)v-x,
\qquad
\mu>0.
\]

For every compactly supported invariant Borel probability measure \(\pi\),
\[
\boxed{\mathbb E_\pi[v\mid x]=0}.
\]
More strongly, every continuously differentiable test function \(\phi\) on the compact stationary \(x\)-range satisfies the exact virial identity
\[
\boxed{
\mathbb E_\pi[\phi'(x)v^2]
=
\mathbb E_\pi[x\phi(x)]
}.
\]

Let
\[
\rho=x_\#\pi
\]
be the stationary position marginal and define the kinetic-energy projection
\[
\eta(B)=\int_{\{x\in B\}}v^2\,d\pi.
\]
Then \(\eta\) is absolutely continuous with respect to Lebesgue measure and is reconstructed from \(\rho\) alone:
\[
\boxed{
\eta(dx)=q(x)\,dx,
\qquad
q(x)=\int_{[x,\infty)}s\,\rho(ds)
}.
\]
Thus the distribution of stationary kinetic energy across position is fixed by the position marginal, independently of the damping parameter \(\mu\).

Taking
\[
\phi(x)=\frac{x^{k+1}}{k+1}
\]
gives the moment hierarchy
\[
\boxed{
\mathbb E_\pi[x^k v^2]
=
\frac{1}{k+1}\mathbb E_\pi[x^{k+2}]
}
\qquad
(k=0,1,2,\ldots).
\]

The stationary mechanical-energy balance is
\[
\mathbb E_\pi[(1-x^2)v^2]=0.
\]
Combining it with the cases \(k=0\) and \(k=2\) yields
\[
\boxed{
\mathbb E_\pi[x^4]
=
3\mathbb E_\pi[x^2]
}.
\]
Therefore every compact stationary state not supported at the equilibrium obeys
\[
\boxed{
0<\mathbb E_\pi[x^2]<3
}.
\]

Finally, every such non-equilibrium stationary state assigns positive kinetic-energy mass to both signs of the nonlinear damping:
\[
\int_{\{|x|<1\}}v^2\,d\pi>0,
\qquad
\int_{\{|x|>1\}}v^2\,d\pi>0.
\]

## Assumptions and scope
The measure \(\pi\) is invariant under the autonomous flow and has compact support in \(\mathbb R^2\). Compact support supplies all integrability and permits arbitrary one-variable antiderivative test functions on the stationary position range.

The parameter satisfies
\[
\mu>0.
\]
The standard van der Pol equation in second-order form is
\[
\ddot x-\mu(1-x^2)\dot x+x=0.
\]
An authoritative open description accepted on 8 January 2007 gives this normalization and the stable limit cycle. A later full mathematical treatment uses exactly the first-order system above, states that its global invariant set consists of the attracting limit cycle and the origin, and studies rigorous bounds on long-time averages.

The original triode model dates to 1920, but the checked historical record resolves that source only to year and month-level issue information. The `first_public_date` records the earliest day-resolved public source used for this finding and does not invent a day for the 1920 article.

## Proof
Let \(L\) be the generator.

For a continuous function \(h\) on the compact stationary \(x\)-range, choose a continuously differentiable antiderivative \(H\) with
\[
H'(x)=h(x).
\]
Then
\[
LH=h(x)v.
\]
Invariance gives
\[
\mathbb E_\pi[h(x)v]=0
\]
for every \(h\), hence
\[
\mathbb E_\pi[v\mid x]=0.
\]

Taking the stationary mean of the \(v\)-equation gives
\[
0
=
\mu\mathbb E_\pi[(1-x^2)v]-\mathbb E_\pi[x].
\]
The first term vanishes by the conditional law, so
\[
\mathbb E_\pi[x]=0.
\]

Now let \(\phi\) be continuously differentiable. Applying the generator to
\[
\phi(x)v
\]
gives
\[
L(\phi(x)v)
=
\phi'(x)v^2
+
\mu\phi(x)(1-x^2)v
-
x\phi(x).
\]
The middle term has zero stationary mean because its coefficient is a function of \(x\). Invariance therefore gives
\[
\mathbb E_\pi[\phi'(x)v^2]
=
\mathbb E_\pi[x\phi(x)].
\]

Define finite measures
\[
\rho=x_\#\pi,
\qquad
\eta(B)=\int_{\{x\in B\}}v^2\,d\pi.
\]
The preceding identity is
\[
\int \phi'(x)\,\eta(dx)
=
\int x\phi(x)\,\rho(dx).
\]
Thus, in the distributional sense,
\[
\eta'=-x\rho.
\]

Set
\[
q(x)=\int_{[x,\infty)}s\,\rho(ds).
\]
Because \(\rho\) is compactly supported and
\[
\int s\,\rho(ds)=0,
\]
the function \(q\) has compact support and its distributional derivative is
\[
q'=-x\rho.
\]
Therefore the finite signed measure
\[
\eta-q(x)\,dx
\]
has zero distributional derivative. It must be a constant multiple of Lebesgue measure; finiteness forces that constant to vanish. Hence
\[
\eta(dx)=q(x)\,dx.
\]

Choosing
\[
\phi(x)=\frac{x^{k+1}}{k+1}
\]
proves
\[
\mathbb E_\pi[x^k v^2]
=
\frac{1}{k+1}\mathbb E_\pi[x^{k+2}].
\]

For
\[
E=\frac{x^2+v^2}{2},
\]
direct differentiation gives
\[
LE=\mu(1-x^2)v^2.
\]
Stationarity and \(\mu>0\) imply
\[
\mathbb E_\pi[v^2]
=
\mathbb E_\pi[x^2v^2].
\]
The moment hierarchy gives
\[
\mathbb E_\pi[v^2]=\mathbb E_\pi[x^2]
\]
and
\[
\mathbb E_\pi[x^2v^2]=\frac13\mathbb E_\pi[x^4].
\]
Therefore
\[
\mathbb E_\pi[x^4]=3\mathbb E_\pi[x^2].
\]

Write
\[
s=\mathbb E_\pi[x^2].
\]
Cauchy–Schwarz gives
\[
\mathbb E_\pi[x^4]\ge s^2,
\]
so
\[
s^2\le3s.
\]
If \(s=0\), the \(k=0\) identity gives
\[
\mathbb E_\pi[v^2]=0,
\]
and \(\pi\) is the origin atom. If \(s=3\), equality in Cauchy–Schwarz would force \(x^2=3\) almost surely. Invariance would then force \(x\) constant along support trajectories and hence \(v=0\), but the \(v\)-equation would give \(\dot v=-x\ne0\). Thus no invariant probability measure realizes \(s=3\). Every non-equilibrium stationary state has
\[
0<s<3.
\]

Finally,
\[
\int (1-x^2)v^2\,d\pi=0.
\]
For a non-equilibrium measure the kinetic-energy measure \(\eta\) is nonzero and absolutely continuous, so it assigns zero mass to the two points \(x=\pm1\). The displayed zero balance therefore requires positive \(\eta\)-mass on both
\[
|x|<1
\]
and
\[
|x|>1.
\]

## Verification
The accompanying checker verifies, by exact sparse-polynomial arithmetic, the generator decompositions used for the moment hierarchy and energy balance.

For several symbolic monomial tests it verifies
\[
L\!\left(\frac{x^{k+1}v}{k+1}\right)
=
x^k v^2
+
\frac{\mu x^{k+1}(1-x^2)v}{k+1}
-
\frac{x^{k+2}}{k+1}.
\]
After the conditional-mean term is removed, stationarity gives the claimed hierarchy.

The checker also verifies
\[
L\!\left(\frac{x^2+v^2}{2}\right)
=
\mu(1-x^2)v^2
\]
and the exact algebraic implication
\[
\mathbb E[v^2]=\mathbb E[x^2],
\qquad
\mathbb E[x^2v^2]=\frac13\mathbb E[x^4],
\qquad
\mathbb E[v^2]=\mathbb E[x^2v^2]
\]
\[
\Longrightarrow
\mathbb E[x^4]=3\mathbb E[x^2].
\]

The stored checker output is `VERIFY_OK`.

The distributional reconstruction
\[
\eta(dx)=q(x)\,dx
\]
and strict equality cases are analytic arguments in the proof and are not inferred from finite numerical trajectories.

## Relationship to prior work
The van der Pol oscillator is a foundational nonlinear self-oscillator. The original triode article appeared in 1920, and a peer-reviewed open reference gives the modern normalization, its nonlinear damping interpretation, and the stable limit cycle.

Fantuzzi, Goluskin, Huang, and Chernyshenko study the same deterministic first-order system and explicitly develop rigorous bounds on infinite-time averages. Their complete open article writes
\[
\dot x=v,
\qquad
\dot v=\mu(1-x^2)v-x
\]
and studies bounds on the limit-cycle average of
\[
x^2+v^2.
\]
The inspected complete text contains no matches for `moment`, `variance`, `conditional`, or `virial`; its occurrence of “fourth” concerns a numerical Runge–Kutta method rather than a fourth-moment identity. The paper's time-average framework is therefore relevant broader coverage but does not state the kinetic-energy reconstruction or
\[
\mathbb E[x^4]=3\mathbb E[x^2].
\]

Published semantic searches were also run for invariant measures, stationary moment hierarchies, conditional velocity laws, fourth moments, virial identities, and exact time-average relations for the van der Pol oscillator. No checked result implied the accepted theorem. The closest indexed stationary-law results concern different flows.

The finding does not claim a new limit cycle, new existence theorem, or new numerical estimate of its amplitude. Its content is the exact all-invariant-measures weak identity, the resulting reconstruction of the kinetic-energy projection from the position marginal, and the parameter-independent fourth-moment law.

## Limitations
The theorem concerns compactly supported invariant probability measures of the deterministic autonomous oscillator.

The reconstruction determines the position projection of \(v^2d\pi\), not the full joint invariant measure.

The strict bound
\[
\mathbb E[x^2]<3
\]
is a universal stationary consequence, not a sharp formula for the limit-cycle amplitude or period as a function of \(\mu\).

The foundational 1920 article was not available with a fully resolved public day in the checked record and is not used for a whole-document novelty assertion.

The weak-generator identity is elementary once recognized, so an equivalent statement could remain in unindexed historical oscillator literature.

## References
1. B. van der Pol, “A theory of the amplitude of free and forced triode vibrations,” Radio Review 1, 701–710 and 754–762 (1920).
2. T. Kanamaru, “Van der Pol oscillator,” Scholarpedia 2(1):2202 (2007), DOI 10.4249/scholarpedia.2202.
3. G. Fantuzzi, D. Goluskin, D. Huang, and S. I. Chernyshenko, “Bounds for deterministic and stochastic dynamical systems using sum-of-squares optimization,” arXiv:1512.05599 (first submitted 17 December 2015); SIAM Journal on Applied Dynamical Systems 15, 1962–1988 (2016), DOI 10.1137/15M1053347.
