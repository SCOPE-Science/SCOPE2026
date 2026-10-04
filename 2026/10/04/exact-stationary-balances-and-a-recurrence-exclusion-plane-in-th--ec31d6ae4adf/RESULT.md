# Exact stationary balances and a recurrence-exclusion plane in the complex Chen system
## Finding
Consider the complex Chen system
\[
\dot X=a(Y-X),\qquad
\dot Y=(c-a)X-XZ+cY,\qquad
\dot Z=\frac12(\overline X Y+X\overline Y)-bZ,
\]
with \(X,Y\in\mathbb C\), \(Z\in\mathbb R\), \(a>0\), \(b>0\), and \(c=c_1+i c_2\). For every compactly supported invariant Borel probability measure \(\mu\), let
\[
S=\int |X|^2\,d\mu,\qquad
E=\int |\dot X|^2\,d\mu,\qquad
M=\int Z|X|^2\,d\mu.
\]
Then
\[
\int |X|^2\,d\mu=b\int Z\,d\mu
\]
and the exact stationary identity
\[
(c_1-a)\left[M-(2c_1-a)S-\frac{E}{a}\right]=2c_2^2S
\]
holds. Hence, when \(c_1\ne a\) and \(S>0\),
\[
\frac{M}{S}=2c_1-a+\frac{2c_2^2}{c_1-a}+\frac1a\frac{E}{S}.
\]
On the detuned resonance plane \(c_1=a\), \(c_2\ne0\), the only compactly supported invariant probability measure is the point mass at the origin. In particular, there is no nonconstant periodic orbit and no nontrivial compact recurrent statistical state on that plane.

## Assumptions and scope
The statement concerns the autonomous five-real-dimensional flow determined by two complex variables \(X,Y\) and one real variable \(Z\). The coefficients \(a,b\) are real and strictly positive, while \(c\) may be complex. Compact support is assumed only so that the polynomial observables used below are integrable and the generator has zero mean under an invariant measure. No ergodicity assumption is required for the balance laws.

For \(c_1\ne a\), define
\[
\Theta=2c_1-a+\frac{2c_2^2}{c_1-a}.
\]
The weighted-height law reads \(M/S=\Theta+E/(aS)\) whenever \(S>0\). If \(c_2\ne0\), equality \(M/S=\Theta\) is impossible for a nonzero compact invariant measure because equality forces \(\dot X=0\) on its support, which would require the nonreal value \(Z=2c-a\) at any support point with \(X\ne0\). If \(c_2=0\), equality is attained exactly by invariant measures supported on equilibria; when \(2c_1-a>0\), these include the equilibrium circle \(|X|^2=b(2c_1-a)\), \(Y=X\), \(Z=2c_1-a\).

## Proof
Write
\[
s=|X|^2,\qquad R=\operatorname{Re}(\overline X Y),\qquad I=\operatorname{Im}(\overline X Y).
\]
Let \(L\) denote differentiation along the vector field. Direct expansion gives
\[
Ls=2a(R-s).
\]
A second direct expansion gives
\[
LI=(c_1-a)I+c_2(s+R).
\]
Now set
\[
G=aR-\frac{a+c_1}{2}s.
\]
Using the two complex equations for \(X\) and \(Y\), and \(|\dot X|^2=a^2|Y-X|^2\), one obtains the pointwise identity
\[
LG=|\dot X|^2-a c_2 I+a(2c_1-a-Z)s.
\]
If \(\mu\) is compactly supported and invariant, then \(\int Lf\,d\mu=0\) for each of these polynomial observables. Integrating \(Ls\) gives
\[
\int R\,d\mu=S.
\]
Integrating \(LI\) therefore gives
\[
(c_1-a)\int I\,d\mu+2c_2S=0.
\]
Integrating \(LG\) gives
\[
M=(2c_1-a)S+\frac{E}{a}-c_2\int I\,d\mu.
\]
Eliminating \(\int I\,d\mu\) yields
\[
(c_1-a)\left[M-(2c_1-a)S-\frac{E}{a}\right]=2c_2^2S.
\]

For the first mean law, use
\[
V=s-2aZ.
\]
The vector field gives the exact identity
\[
LV=-2as+2abZ.
\]
Integration against \(\mu\) yields \(S=b\int Z\,d\mu\).

Finally suppose \(c_1=a\) and \(c_2\ne0\). The stationary identity from \(LI\) becomes \(2c_2S=0\), hence \(S=0\). Since \(s\ge0\), the support of \(\mu\) lies in \(X=0\). Invariance of the support and \(\dot X=aY\) then force \(Y=0\) on the support. On \(X=Y=0\), the remaining equation is \(\dot Z=-bZ\); the only invariant probability measure for this scalar contraction is \(\delta_0\). Thus the origin point mass is the unique compactly supported invariant probability measure on the detuned resonance plane.

## Verification
The bundled `verify.py` expands the five-real-dimensional vector field symbolically and verifies, as polynomial identities, the displayed formulas for \(Ls\), \(LI\), \(LG\), and \(LV\). It then checks the algebraic elimination producing the stationary identity. Running the packaged checker returns `VERIFY_OK`.

As a consistency check against the later bifurcation paper, its explicit rotating periodic orbit has \(c_1=28\), angular frequency
\[
\omega=\frac{2ac_2}{a-28},
\]
and constant height \(Z=M_0\). Since \(|\dot X|^2=\omega^2|X|^2\) on that orbit, the new identity reduces to
\[
M_0=56-a-\frac{2c_2^2}{a-28}+\frac{\omega^2}{a}
=56-a+\frac{2(a+28)c_2^2}{(a-28)^2},
\]
which is exactly the height formula implicit in the published amplitude expression.

## Relationship to prior work
Zhang and Chen introduced the 2021 boundedness analysis for this complex Chen system and, in their Lemma 3.3, used \(V=|X|^2-2aZ\) to obtain a one-sided transient estimate from the identity \(LV=-2a|X|^2+2abZ\). Their paper develops ultimate bounds and does not state the stationary \(I\)-balance, the derivative-energy weighted-height identity, or the recurrence exclusion at \(\operatorname{Re}c=a\) with \(\operatorname{Im}c\ne0\).

Mahmoud, Bountis, and Mahmoud introduced and numerically studied the positive-real-parameter complex Chen system, including its equilibrium circle and a chaotic attractor. Wang and Zhang later studied Hopf bifurcation, explicit rotating periodic solutions, ultimate bounds, and a related family with infinitely many Hopf bifurcations. The weighted-height identity above applies to the same vector field, recovers the constant height of their explicit rotating periodic orbit as a consequence of a measure-wide balance, and adds the sharp detuned resonance obstruction. The inspected full texts do not state this invariant-measure law or the resonance exclusion.

## Limitations
The result is a constraint on compact invariant probability measures, not a classification of all forward trajectories. On \(c_1=a\), \(c_2\ne0\), the theorem excludes nontrivial compact recurrent statistical states but does not claim that every nonzero trajectory is global, bounded, or convergent. For \(c_1\ne a\), the weighted-height formula is exact, but by itself it does not prove existence of a nontrivial invariant measure or a chaotic attractor. The result also does not provide an independent numerical validation of any published chaotic simulation.

## References
1. X. Zhang and G. Chen, “Boundedness of the complex Chen system,” *Discrete and Continuous Dynamical Systems - B* 27 (2022), 5673–5700, DOI 10.3934/dcdsb.2021291. Early access: 2021-12-17.
2. G. M. Mahmoud, T. Bountis, and E. E. Mahmoud, “Active control and global synchronization of the complex Chen and Lü systems,” *International Journal of Bifurcation and Chaos* 17 (2007), 4295–4308, DOI 10.1142/S0218127407019962.
3. L. Wang and X. Zhang, “Bifurcation and Dynamics of the complex Chen systems,” *Discrete and Continuous Dynamical Systems - B* 29 (2024), 1243–1282, DOI 10.3934/dcdsb.2023132. Early access: 2023-07-31.
