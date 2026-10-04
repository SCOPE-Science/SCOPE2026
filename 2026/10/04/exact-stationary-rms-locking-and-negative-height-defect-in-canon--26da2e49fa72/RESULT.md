# Exact stationary RMS locking and negative-height defect in canonical Sprott B
## Finding
For the canonical Sprott B flow
\[
\dot x=yz,\qquad \dot y=x-y,\qquad \dot z=1-xy,
\]
every compactly supported invariant Borel probability measure \(\mu\) satisfies
\[
\int xy\,d\mu=\int y^2\,d\mu=1
\]
and
\[
\int y^2z\,d\mu=-\int (x-y)^2\,d\mu\le 0.
\]
Equality in the second displayed identity holds exactly when \(\mu\) is a convex mixture of the two equilibria \((1,1,0)\) and \((-1,-1,0)\).

Therefore, if \(\mu\) is not such an equilibrium mixture, then
\[
\mu(|y|<1)>0,\qquad \mu(|y|>1)>0,\qquad \mu(z<0)>0.
\]
In particular every nonconstant periodic orbit has root-mean-square \(y\)-amplitude exactly one, crosses both sides of the equilibrium amplitude \(|y|=1\), and enters the half-space \(z<0\).

## Assumptions and scope
The phase space is \(\mathbb R^3\), the vector field is the canonical Case B system introduced by Sprott, and \(\mu\) is invariant under its continuous flow and has compact support. Compact support is used only to justify the polynomial moment identities without additional integrability hypotheses.

The statement concerns invariant probability measures, including periodic-orbit measures and invariant measures supported on compact recurrent sets. It does not assert existence, uniqueness, ergodicity, or physicality of a chaotic invariant measure, and it does not classify all bounded trajectories.

## Proof
Let \(L\) be the Lie derivative along the vector field. For every continuously differentiable function \(F\) used below, invariance and compact support give
\[
\int LF\,d\mu=0.
\]

Taking \(F=z\) gives
\[
Lz=1-xy,
\]
hence
\[
\int xy\,d\mu=1.
\]

Taking \(F=y^2/2\) gives
\[
L(y^2/2)=y(x-y)=xy-y^2,
\]
so the previous identity yields
\[
\int y^2\,d\mu=1.
\]

Taking \(F=xy\) gives
\[
L(xy)=x(x-y)+y(yz)=x^2-xy+y^2z.
\]
After integration,
\[
0=\int x^2\,d\mu-1+\int y^2z\,d\mu.
\]
On the other hand,
\[
\int (x-y)^2\,d\mu
=\int x^2\,d\mu-2\int xy\,d\mu+\int y^2\,d\mu
=\int x^2\,d\mu-1.
\]
Combining the last two equations proves
\[
\int y^2z\,d\mu=-\int (x-y)^2\,d\mu\le 0.
\]

It remains to identify the equality case. Equality forces \(x=y\) on the support of \(\mu\). The support of an invariant probability measure is invariant under the flow. On the closed set \(x=y\), preservation of that relation along an orbit requires
\[
\frac{d}{dt}(x-y)=yz=0.
\]
A compact invariant support cannot contain a point with \(x=y=0\), because then \(z(t)=z(0)+t\) is unbounded. Hence \(z=0\) on the support. Preservation of \(z=0\) then requires
\[
\dot z=1-x^2=0,
\]
so the support is contained in \(\{(1,1,0),(-1,-1,0)\}\). Conversely every convex mixture of the two equilibrium point masses is invariant and attains equality.

Finally, \(\int y^2\,d\mu=1\). If a non-equilibrium invariant measure had \(|y|\le 1\) almost surely or \(|y|\ge 1\) almost surely, equality of the mean square to one would force \(|y|=1\) on its support; invariance then forces the same two-equilibrium support just described. Thus every non-equilibrium invariant measure has positive mass on both \(|y|<1\) and \(|y|>1\). Its strict defect
\[
\int y^2z\,d\mu<0
\]
also forces positive mass in \(z<0\).

## Verification
The proof uses only three exact polynomial coboundaries:
\[
Lz=1-xy,
\]
\[
L(y^2/2)=xy-y^2,
\]
and
\[
L(xy)=x^2-xy+y^2z.
\]
Substitution into the invariant-measure identity \(\int LF\,d\mu=0\) reproduces every displayed moment relation. No numerical integration, truncation, or asymptotic approximation is used.

The equality case was checked against the actual vector field rather than inferred only from vanishing integrals: invariance of the support reduces \(x=y\) first to \(z=0\) on any compact invariant support and then to \(x^2=1\).

## Relationship to prior work
Sprott's 1994 paper introduced the Case B equations and reported their critical points, Lyapunov exponents, and fractal dimension. Mota and Oliveira later embedded the same system in the two-parameter Sprott BC family and studied finite singularities, Hopf bifurcation, dynamics at infinity, and nonexistence of polynomial first integrals, invariant algebraic surfaces, and Darboux first integrals. Their full text identifies the canonical Sprott B equations but does not state invariant-measure averages, mean-square identities, or the defect proved here. Feng and Wei studied delayed feedback and local Hopf bifurcation for a generalized Sprott B system; the accessible abstract is about controlled and delayed dynamics rather than the unforced invariant-measure identities above.

Semantic searches for the exact moment relations, their periodic-orbit form, amplitude-threshold consequence, and negative-height consequence did not locate a published statement implying this result. The closest located published balance laws concern different vector fields, so they do not imply the Sprott B identities.

## Limitations
The originality check cannot exclude every item outside indexed or accessible literature. The 2015 generalized-Sprott-B article was available only through its abstract in the sources inspected, so unobserved details of that paper remain a residual bibliographic risk. The claim is deliberately limited to compactly supported invariant probability measures of the canonical unforced Sprott B flow.

## References
1. J. C. Sprott, “Some simple chaotic flows,” *Physical Review E* 50 (1994), R647–R650. DOI: 10.1103/PhysRevE.50.R647. Published 1994-08-01.
2. M. C. Mota and R. D. S. Oliveira, “Dynamic aspects of Sprott BC chaotic system,” *Discrete and Continuous Dynamical Systems - B* 26 (2021), 1653–1673. DOI: 10.3934/dcdsb.2020177.
3. Y. Feng and Z. Wei, “Delayed feedback control and bifurcation analysis of the generalized Sprott B system with hidden attractors,” *The European Physical Journal Special Topics* 224 (2015), 1619–1636. DOI: 10.1140/epjst/e2015-02484-9.
