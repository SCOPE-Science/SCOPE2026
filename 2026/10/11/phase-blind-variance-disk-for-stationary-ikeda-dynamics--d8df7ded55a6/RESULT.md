# Phase-blind variance disk for stationary Ikeda dynamics
## Finding
Consider the classical Ikeda map
\[
F(g)=a+R g\exp\!\left(i\left(\phi-\frac{p}{1+|g|^2}\right)\right),
\qquad a>0,\quad 0<R<1.
\]
For every compactly supported invariant Borel probability measure \(\mu\), define
\[
m=\int_{\mathbb C} g\,d\mu(g),\qquad
q=\int_{\mathbb C}|g|^2\,d\mu(g),\qquad
V=q-|m|^2.
\]
Then
\[
(1-R^2)q=2a\operatorname{Re}m-a^2,
\]
and therefore
\[
\boxed{\;V=\frac{a^2R^2}{(1-R^2)^2}-\left|m-\frac{a}{1-R^2}\right|^2\;}.
\]
Thus every stationary barycenter lies in the closed disk
\[
\left|m-\frac{a}{1-R^2}\right|\le \frac{aR}{1-R^2}.
\]
The boundary is attained exactly by invariant point masses, hence exactly by fixed-point trajectories. Every non-Dirac invariant measure lies strictly inside the disk.

In real coordinates \(g=x+iy\), the same identity is
\[
\operatorname{Var}(x)+\operatorname{Var}(y)
=
\frac{a^2R^2}{(1-R^2)^2}
-\left(\bar x-\frac{a}{1-R^2}\right)^2-\bar y^2.
\]
The nonlinear detuning parameters \(\phi\) and \(p\) disappear completely.

## Assumptions and scope
The claim concerns the classical Ikeda map on \(\mathbb C\), with real input amplitude \(a>0\), scaled mirror reflectivity \(0<R<1\), and arbitrary real detuning parameters \(\phi,p\). The probability measure is assumed invariant under \(F\) and compactly supported, which guarantees the required first and second moments. No ergodicity assumption is needed.

The quantity \(q\) is the stationary mean field intensity, \(|m|^2\) is the coherent power of the stationary mean complex amplitude, and \(V=q-|m|^2\) is the mean-square fluctuation about that amplitude. The finding therefore gives an exact coherent/fluctuating power budget from the barycenter alone.

## Proof
Write
\[
u(g)=\exp\!\left(i\left(\phi-\frac{p}{1+|g|^2}\right)\right),
\qquad |u(g)|=1,
\]
and put
\[
c=\int g\,u(g)\,d\mu(g).
\]
Invariance applied to the coordinate function gives
\[
m=\int F(g)\,d\mu(g)=a+Rc,
\]
so
\[
Rc=m-a.
\]

Next, invariance applied to \(|g|^2\) gives
\[
\begin{aligned}
q
&=\int |F(g)|^2\,d\mu(g)\\
&=a^2+R^2q+2aR\operatorname{Re}c\\
&=a^2+R^2q+2a\operatorname{Re}(m-a).
\end{aligned}
\]
Rearranging yields
\[
(1-R^2)q=2a\operatorname{Re}m-a^2.
\]
Subtracting \(|m|^2\) and completing the square gives
\[
\begin{aligned}
V
&=\frac{2a\operatorname{Re}m-a^2}{1-R^2}-|m|^2\\
&=\frac{a^2R^2}{(1-R^2)^2}
-\left|m-\frac{a}{1-R^2}\right|^2.
\end{aligned}
\]
Since
\[
V=\int |g-m|^2\,d\mu(g)\ge0,
\]
the disk constraint follows.

Finally, \(V=0\) holds exactly when \(g=m\) almost surely, so \(\mu=\delta_m\). Such a Dirac measure is invariant exactly when \(F(m)=m\). This proves the boundary characterization and strictness for every non-Dirac invariant measure.

## Verification
The derivation uses only invariance, the constant input term, and the unit modulus of the nonlinear phase factor. A standalone symbolic checker in `verify_identity.py` verifies that the completed-square expression is algebraically identical to the second-moment balance. Its packaged output is `IDENTITY_OK`.

The boundary statement was checked directly from the nonnegative variance representation \(V=\int |g-m|^2\,d\mu\): zero variance forces a point mass, and invariance of a point mass is equivalent to the fixed-point equation.

## Relationship to prior work
Ikeda introduced the optical ring-cavity dynamics in 1979. A later full-text study by Osinga and Rankin writes the map in the same complex form, identifies \(a\) as input amplitude and \(R\) as scaled mirror reflectivity, and studies fixed points, periodic windows, chaotic attractors, and boundary crises. That paper's primary classifications are 37G25 and 37M20. Its full text does not state a stationary variance, invariant-measure, average, or moment identity.

A 2019 study of the Ikeda map analyzes intermittent extreme events using empirical probability-density and interevent statistics, while a 2022 study computes entropy- and Lyapunov-based chaos diagnostics for the same standard map. These are statistically adjacent but do not provide the exact stationary coherent/fluctuating power budget above.

The identity is also not a numerical fit: the nonlinear phase cancels exactly in the second-moment balance. The result is therefore complementary to bifurcation, rare-event, entropy, and dimension analyses of the Ikeda attractor.

## Limitations
The claim is an exact constraint on invariant statistics; it does not determine which interior barycenters are dynamically realizable, classify invariant measures, prove existence or uniqueness of a physical measure, or locate bifurcations. It assumes a compactly supported invariant probability measure. The 1979 source was verified bibliographically but its full text was not available in the inspected sources; no claim is made about whether it contains fixed-point algebra that specializes to the zero-variance boundary case.

## References
1. K. Ikeda, “Multiple-valued stationary state and its instability of the transmitted light by a ring cavity system,” *Optics Communications* 30(2), 257–261 (1979), DOI 10.1016/0030-4018(79)90090-7. Earliest verified public date: 1979-08-01.
2. H. M. Osinga and J. Rankin, “Two-parameter locus of boundary crisis: Mind the gaps!,” *AIMS Conference Publications* 2011, 1148–1157, DOI 10.3934/proc.2011.2011.1148. Preprint dated July 2010.
3. A. Ray, S. Rakshit, D. Ghosh, and S. K. Dana, “Intermittent large deviation of chaotic trajectory in Ikeda map: Signature of extreme events,” *Chaos* 29, 043131 (2019), DOI 10.1063/1.5092741; arXiv:1903.10156.
4. “Analysis of Chaotic Dynamics by the Extended Entropic Chaos Degree,” *Entropy* 24, 827 (2022), DOI 10.3390/e24060827.
