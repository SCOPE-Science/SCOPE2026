# Future-memory projection and strict stationary variance defects in the hyperchaotic Rössler flow
## Finding
Consider the four-dimensional Rössler flow
\[
\dot x=-y-w,\qquad
\dot y=x+a y+z,\qquad
\dot z=d z+c w,\qquad
\dot w=xw+b,
\]
with
\[
d>0,\qquad c\ne0,\qquad b\ne0.
\]
Every compactly supported invariant Borel probability measure \(\mu\) satisfies the two exact stationary regressions
\[
\boxed{\mathbb E_\mu[w\mid z]= -\frac{d}{c}z}
\]
and
\[
\boxed{\mathbb E_\mu[x\mid w]= -\frac{b}{w}}.
\]
The second identity also forces the invariant support a positive distance away from \(w=0\).

The regression residuals are normalized coordinate speeds, so
\[
\boxed{
\operatorname{Var}_\mu(w)-\left(\frac{d}{c}\right)^2\operatorname{Var}_\mu(z)
=\frac1{c^2}\mathbb E_\mu[\dot z^2]
}
\]
and
\[
\boxed{
\operatorname{Var}_\mu(x)-b^2\operatorname{Var}_\mu(1/w)
=\mathbb E_\mu\!\left[\left(\frac{\dot w}{w}\right)^2\right]
}.
\]
Either defect is zero exactly for invariant measures supported on equilibria.

There is also an exact trajectory-level representation that is specific to the positive coefficient \(d\). Every bounded complete trajectory satisfies
\[
\boxed{
z(t)=-c\int_0^\infty e^{-ds}w(t+s)\,ds
}.
\]
Thus the linearly expanding \(z\)-channel is selected by bounded recurrence as an exponentially weighted *future* average of the reinjection coordinate \(w\), while at the same instant its stationary regression satisfies \(\mathbb E[w\mid z]=-(d/c)z\).

For Rössler's hyperchaotic parameters
\[
a=\frac14,\qquad b=3,\qquad c=-\frac12,\qquad d=\frac1{20},
\]
the theorem reads
\[
\mathbb E[w\mid z]=\frac{z}{10},
\]
\[
\operatorname{Var}(w)-\frac1{100}\operatorname{Var}(z)=4\mathbb E[\dot z^2],
\]
and
\[
\operatorname{Var}(x)-9\operatorname{Var}(1/w)
=\mathbb E\!\left[\left(\frac{\dot w}{w}\right)^2\right].
\]
The two equilibria are
\[
E_s=\left(-s\frac{3\sqrt{13}}{2},-s\frac{2}{\sqrt{13}},s\frac{20}{\sqrt{13}},s\frac{2}{\sqrt{13}}\right),
\qquad s\in\{-1,1\}.
\]
Hence each displayed variance inequality is strict for every compact invariant probability measure not supported on \(\{E_{-1},E_1\}\).

## Assumptions and scope
The normalization is exactly the four-dimensional system written in the complete mathematical treatment by Wilczak. It is equivalent to the more common presentation obtained by interchanging the two final coordinates. The theorem is stated in the displayed variables so that every sign and coefficient can be checked directly against that source.

Compact support supplies the bounded test functions needed in the generator argument and makes every support trajectory complete and bounded. The reciprocal \(1/w\) is not assumed integrable in advance; separation of the support from \(w=0\) is proved before the reciprocal variance identity is used.

The earliest verified public-source date for Rössler's four-variable hyperchaos equation is 30 April 1979. A later complete mathematical study of this exact four-dimensional system lists primary MSC \(34C37\) and \(37B10\).

## Proof
Let \(L\) denote the flow generator.

Take an arbitrary continuous function \(\phi\) on the compact \(z\)-range of the support, and choose an antiderivative \(H\) with \(H'(z)=\phi(z)\). Then
\[
LH=\phi(z)(dz+cw).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(z)(dz+cw)]=0
\]
for every such \(\phi\). Therefore
\[
\mathbb E_\mu[w\mid z]=-\frac dc z.
\]
Since
\[
w+\frac dc z=\frac{\dot z}{c},
\]
the law of total variance gives
\[
\operatorname{Var}(w)
=\left(\frac dc\right)^2\operatorname{Var}(z)
+\frac1{c^2}\mathbb E[\dot z^2].
\]

For the nonlinear reinjection coordinate, take an arbitrary continuous \(\psi\) on the compact \(w\)-range and an antiderivative \(K\). Invariance gives
\[
0=\mathbb E_\mu[LK]
=\mathbb E_\mu[\psi(w)(xw+b)].
\]
Hence
\[
b+w\mathbb E_\mu[x\mid w]=0
\]
almost surely. If \(M=\sup_{\operatorname{supp}\mu}|x|\), then \(M>0\) and
\[
|b|=|w\mathbb E[x\mid w]|\le M|w|
\]
almost surely. Consequently
\[
|w|\ge\frac{|b|}M
\]
on the support, so \(1/w\) is bounded there and
\[
\mathbb E_\mu[x\mid w]=-\frac bw.
\]
Because
\[
x+\frac bw=\frac{\dot w}{w},
\]
a second conditional-variance decomposition yields
\[
\operatorname{Var}(x)
=b^2\operatorname{Var}(1/w)
+\mathbb E\!\left[\left(\frac{\dot w}w\right)^2\right].
\]

For the first equality case, suppose \(\dot z=0\) on the invariant support. Along every support trajectory, \(z\) is constant and \(dz+cw=0\), so \(w\) is constant. Then \(\dot w=xw+b=0\); because \(b\ne0\), one has \(w\ne0\), hence \(x\) is constant. The equation \(\dot x=-y-w=0\) makes \(y\) constant as well, and the support trajectory is an equilibrium. The converse is immediate. The same argument begins from \(\dot w=0\) for the second defect: constant nonzero \(w\) fixes \(x=-b/w\), then \(x\) fixes \(y=-w\), and invariance fixes \(z\), so the trajectory is an equilibrium.

Finally, along any bounded complete trajectory,
\[
\frac d{dt}\left(e^{-dt}z(t)\right)=c e^{-dt}w(t).
\]
Integrating from \(t\) to \(T\) and sending \(T\to\infty\), boundedness makes \(e^{-dT}z(T)\to0\). Therefore
\[
z(t)=-c\int_0^\infty e^{-ds}w(t+s)\,ds.
\]
This is a two-sided-orbit identity imposed by bounded recurrence; it is not a causal initial-value formula.

At the classical parameters, solving the four equilibrium equations gives \(w^2=4/13\), then \(y=-w\), \(z=10w\), and \(x=-39w/4\), which yields the two points displayed above.

## Verification
The accompanying checker uses exact rational arithmetic. It verifies the classical coefficients
\[
-\frac dc=\frac1{10},\qquad
\left(\frac dc\right)^2=\frac1{100},\qquad
\frac1{c^2}=4,\qquad b^2=9,
\]
and the exact equilibrium relations
\[
y=-w,\qquad z=10w,\qquad x=-\frac{39}4w,\qquad w^2=\frac4{13}.
\]
It also checks that all four vector-field components vanish under these relations and that the two residual identities clear exactly to the corresponding differential equations. The stored checker output is `VERIFY_OK`.

The conditional-expectation steps, support separation from \(w=0\), equality rigidity, and future-memory representation are analytic consequences of invariance and bounded complete trajectories. They are not inferred from finite simulation.

## Relationship to prior work
Rössler's 1979 article introduced the four-variable oscillator as the first simple hyperchaotic flow, with two expanding directions and one quadratic reinjection term. The issue header gives the public date 30 April 1979.

Wilczak's complete 2009 mathematical article writes the exact normalization used here and, at \(a=1/4\), \(b=3\), \(c=-1/2\), \(d=1/20\), rigorously proves symbolic dynamics together with infinitely many homoclinic and heteroclinic connections. The complete text was searched for `invariant measure`, `average`, `variance`, `moment`, and `covariance`; none of those searches produced the stationary projection or variance identities above.

Wilczak, Serrano, and Barrio later proved coexistence and dynamical connections between hyperchaotic and chaotic invariant sets in the same four-dimensional Rössler model. Those topological and computer-assisted existence results do not implication-wise determine the conditional expectations of \(w\) from \(z\) or \(x\) from \(w\), nor the two exact fluctuation defects.

The closest indexed stationary results located in the scientific database concern the *three-dimensional* Rössler system, including a heightwise flux law and a compact-recurrence variance law. They do not specialize to this four-dimensional flow: the additional linearly expanding coordinate changes both the state space and the equations, and the future-memory identity has no counterpart in those three-dimensional statements.

## Limitations
The theorem concerns compactly supported invariant probability measures and bounded complete trajectories. It does not assert existence, uniqueness, ergodicity, or physicality of an invariant measure.

The future-memory formula is a boundary-value identity selected by boundedness in both time directions; it should not be interpreted as a causal rule for predicting \(z(t)\) from data available at time \(t\).

The result gives exact conditional first moments and variance defects, not a full invariant density or the Lyapunov spectrum.

The complete 1979 article was not inspected through a lawful open full-text route, and the complete 2016 SIAM article was access-limited in the inspected route. The complete 2009 same-object mathematical paper was inspected. A differently phrased stationary identity could remain in unindexed literature; this is the principal residual originality risk.

## References
1. O. E. Rössler, “An equation for hyperchaos,” *Physics Letters A* 71, 155–157 (1979), DOI 10.1016/0375-9601(79)90150-6.
2. D. Wilczak, “Abundance of heteroclinic and homoclinic orbits for the hyperchaotic Rössler system,” *Discrete and Continuous Dynamical Systems B* 11, 1039–1055 (2009), DOI 10.3934/dcdsb.2009.11.1039.
3. D. Wilczak, S. Serrano, and R. Barrio, “Coexistence and Dynamical Connections between Hyperchaos and Chaos in the 4D Rössler System: A Computer-Assisted Proof,” *SIAM Journal on Applied Dynamical Systems* 15, 356–390 (2016), DOI 10.1137/15M1039201.
4. C. Letellier and O. E. Rössler, “Hyperchaos,” *Scholarpedia* 2(8):1936 (2007), DOI 10.4249/scholarpedia.1936.
