# Exact kick–momentum covariance and two-cycle rigidity in the Chirikov standard map
## Finding
Consider the standard map on the cylinder
\[
P=p+K\sin\theta,
\qquad
\Theta=\theta+P\pmod{2\pi},
\qquad
K\ne0,
\]
where \(p\in\mathbb R\) is the lifted momentum and \(\theta\in\mathbb R/(2\pi\mathbb Z)\) is the angle. Put
\[
\Delta p=P-p=K\sin\theta.
\]

Let \(\nu\) be any compactly supported invariant Borel probability measure. Then
\[
\boxed{\mathbb E_\nu[\sin\theta]=0}
\]
and the kick has the exact stationary half-anticovariance law
\[
\boxed{
\operatorname{Cov}_\nu(p,\Delta p)
=-\frac12\operatorname{Var}_\nu(\Delta p)
}.
\]
The outgoing momentum has the reflected law
\[
\boxed{
\operatorname{Cov}_\nu(P,\Delta p)
=+\frac12\operatorname{Var}_\nu(\Delta p)
}.
\]
Equivalently, the midpoint momentum is orthogonal to the kick:
\[
\boxed{
\operatorname{Cov}_\nu\!\left(\frac{p+P}{2},\Delta p\right)=0
}.
\]

Since
\[
\operatorname{Var}(\Delta p)
=K^2\mathbb E[\sin^2\theta],
\]
Cauchy–Schwarz yields the exact stationary activity bound
\[
\boxed{
\operatorname{Var}_\nu(p)
\ge
\frac14\operatorname{Var}_\nu(\Delta p)
=
\frac{K^2}{4}\mathbb E_\nu[\sin^2\theta]
}.
\]

The boundary is dynamically rigid. Suppose
\[
\mathbb E_\nu[\sin^2\theta]>0
\]
and equality holds. Write
\[
m=\mathbb E_\nu[p].\]
Then equality in Cauchy–Schwarz forces
\[
\boxed{
p-m=-\frac K2\sin\theta
}
\]
almost surely. One iterate reverses the centered momentum,
\[
P-m=-(p-m),
\]
and invariance forces
\[
\sin\Theta=-\sin\theta.
\]
Consequently
\[
p_2=p,
\qquad
\theta_2=\theta+2m\pmod{2\pi}.
\]
Compatibility of the equality relation along all even iterates forces
\[
\boxed{m\in\pi\mathbb Z},
\]
and hence
\[
\boxed{T^2=\mathrm{id}}
\]
almost surely.

Thus an ergodic equality state with nonzero kick variance is supported on one nontrivial two-cycle. Every ergodic compact invariant state with nonzero kick variance that is not a two-cycle satisfies
\[
\boxed{
\operatorname{Var}(p)
>
\frac14\operatorname{Var}(\Delta p)
}
\]
and
\[
\boxed{
-1<\operatorname{Corr}(p,\Delta p)<0
}.
\]
More precisely,
\[
\operatorname{Corr}(p,\Delta p)
=-\frac12
\sqrt{\frac{\operatorname{Var}(\Delta p)}{\operatorname{Var}(p)}}.
\]

The variance boundary is genuinely attained. At
\[
K=2\pi,
\]
the two points
\[
(\theta,p)=\left(\frac{\pi}{2},-\pi\right),
\qquad
(\theta,p)=\left(\frac{3\pi}{2},\pi\right)
\]
form a two-cycle. Its invariant orbit measure has
\[
\operatorname{Var}(p)=\pi^2,
\qquad
\operatorname{Var}(\Delta p)=4\pi^2,
\]
so equality holds exactly.

The theorem gives an exact stationarity diagnostic for the same map whose chaotic components can exhibit extremely long transient density bias: an empirical stationary sample must satisfy the half-anticovariance identity even when its spatial density has not yet visibly flattened.

## Assumptions and scope
The phase space is the cylinder rather than the torus: the angle is reduced modulo \(2\pi\), while momentum is kept as a real lift. This distinction is essential because the theorem uses the ordinary first and second moments of momentum.

Compact support guarantees those moments. No ergodicity assumption is needed for the exact covariance identities or inequality. Ergodicity is used only for the final statement that a nondegenerate equality measure is the uniform invariant measure on one two-cycle.

The standard map originated earlier than the structured date used here. The checked historical record traces it to Chirikov's earlier work, but the earliest checked day-resolved public source was the Physics Reports review dated 1 May 1979. No day was invented for older year-only material.

A modern mathematical paper on the standard family lists primary MSC \(37D25\), so the result is classified there.

## Proof
Invariance gives equality in distribution of \((\Theta,P)\) and \((\theta,p)\).

Because
\[
P-p=K\sin\theta,
\]
stationarity of the first momentum moment gives
\[
0=\mathbb E[P-p]=K\mathbb E[\sin\theta].
\]
Since \(K\ne0\),
\[
\mathbb E[\sin\theta]=0.
\]
Thus the kick has zero mean.

Stationarity of the second momentum moment gives
\[
0
=
\mathbb E[P^2-p^2]
=
2\mathbb E[p\Delta p]
+
\mathbb E[(\Delta p)^2].
\]
The kick has zero mean, so
\[
\mathbb E[p\Delta p]
=
\operatorname{Cov}(p,\Delta p),
\]
and therefore
\[
\operatorname{Cov}(p,\Delta p)
=-\frac12\operatorname{Var}(\Delta p).
\]
Since \(P=p+\Delta p\),
\[
\operatorname{Cov}(P,\Delta p)
=
\operatorname{Cov}(p,\Delta p)+\operatorname{Var}(\Delta p)
=
\frac12\operatorname{Var}(\Delta p).
\]
Averaging these two equations yields midpoint orthogonality.

Cauchy–Schwarz gives
\[
\frac14\operatorname{Var}(\Delta p)^2
=
\operatorname{Cov}(p,\Delta p)^2
\le
\operatorname{Var}(p)\operatorname{Var}(\Delta p).
\]
If the kick variance is positive, division proves
\[
\operatorname{Var}(p)
\ge
\frac14\operatorname{Var}(\Delta p).
\]
If the kick variance is zero, the same inequality is immediate. Since
\[
\Delta p=K\sin\theta
\]
and \(\mathbb E[\sin\theta]=0\),
\[
\operatorname{Var}(\Delta p)=K^2\mathbb E[\sin^2\theta].
\]

Now assume positive kick variance and equality. Equality in Cauchy–Schwarz implies an affine almost-sure relation. Its coefficient is fixed by the covariance:
\[
p-m
=
\frac{\operatorname{Cov}(p,\Delta p)}{\operatorname{Var}(\Delta p)}\Delta p
=
-\frac12\Delta p
=
-\frac K2\sin\theta.
\]
Therefore
\[
P-m
=
p-m+\Delta p
=
\frac12\Delta p
=-(p-m).
\]
The same equality relation holds at the image point on a full invariant set:
\[
P-m=-\frac K2\sin\Theta.
\]
Comparison gives
\[
\sin\Theta=-\sin\theta.
\]
Hence the second momentum iterate is
\[
p_2
=P+K\sin\Theta
=P-K\sin\theta
=p.
\]
For the angle,
\[
\theta_2
=
\Theta+p_2
=
\theta+P+p
=
\theta+2m
\pmod{2\pi}.
\]
The equality relation at the second iterate therefore gives
\[
\sin(\theta+2m)=\sin\theta
\]
almost surely.

Suppose, toward a contradiction, that
\[
\sin m\ne0.
\]
Then
\[
\sin(\theta+2m)-\sin\theta
=
2\cos(\theta+m)\sin m

enforces
\[
\cos(\theta+m)=0
\]
almost surely. Applying the same argument after two more iterates also gives
\[
\cos(\theta+3m)=0
\]
almost surely. Thus \(2m\) is an integer multiple of \(\pi\). If it is an even multiple, then \(m\in\pi\mathbb Z\), contradicting \(\sin m\ne0\). If it is an odd multiple, then \(m\in\pi/2+\pi\mathbb Z\), and \(\cos(\theta+m)=0\) forces \(\sin\theta=0\), contradicting positive kick variance. Therefore
\[
m\in\pi\mathbb Z.
\]
It follows that
\[
\theta_2=\theta\pmod{2\pi},
\qquad
p_2=p,
\]
so \(T^2\) is the identity almost surely.

An ergodic invariant probability for a transformation whose square is the identity is concentrated on one orbit of size at most two. Positive kick variance excludes a fixed point, leaving a nontrivial two-cycle.

## Verification
The accompanying checker uses only the Python standard library and exact rational arithmetic. It verifies the second-moment stationarity algebra, the incoming/outgoing half-covariances, midpoint orthogonality, the covariance-determinant inequality, and the equality reflection algebra.

The checker also verifies the explicit equality two-cycle at \(K=2\pi\) using exact coefficients in units of \(\pi\).

The stored checker output is `VERIFY_OK`.

The step from covariance equality to \(m\in\pi\mathbb Z\) and period-two support is an analytic trigonometric argument in the proof. No finite orbit enumeration or numerical simulation is used.

## Relationship to prior work
Chirikov's classical review is a foundational source for the standard map and its role in Hamiltonian chaos. The accepted theorem does not concern the overlap criterion or the existence of stochastic layers.

Meiss's complete 1994 paper is a particularly close statistical comparison. It studies measures generated by chaotic standard-map trajectories, Birkhoff averages, long-lived density spikes, stickiness near elliptic islands, and eventual numerical ergodicity. The complete searchable PDF contains no occurrence of `covariance`; its occurrence of `variance` concerns the histogram of spatial occupation density, not momentum–kick covariance. Its conclusion emphasizes that transient density bias can persist even after extremely long integrations.

Pustyl'nikov's 2000 paper explicitly studies statistical properties of trajectories for a class including the standard map and formulates a probabilistic analogue of a standard-map conjecture. Its accessible abstract does not state a stationary kick–momentum covariance law.

De Simoi's mathematical study concerns abundance of elliptic islands for the standard family at large parameter and provides the dynamical-systems classification used here. Those elliptic-island results do not imply the all-invariant-measures second-moment identity or its period-two equality classification.

The half-anticovariance identity by itself reflects stationarity of an additive momentum increment. The standard-map-specific content retained in the final claim is the exact kick representation \(\Delta p=K\sin\theta\) and the fact that saturation forces the full two-dimensional dynamics, not merely the momentum marginal, to have period dividing two with mean momentum in \(\pi\mathbb Z\).

## Limitations
The result is stated for compactly supported invariant measures on the cylinder. Diffusive accelerator-mode trajectories with unbounded momentum are outside its scope.

The theorem does not establish existence, uniqueness, or absolute continuity of chaotic invariant measures.

The inequality is informative as a strict diagnostic only when the kick variance is nonzero. Zero-kick invariant states require separate orbit classification.

The structured source date is the earliest checked day-resolved public source; historical accounts trace the map to earlier work for which the checked evidence did not provide a day-level public date.

The basic half-anticovariance identity is a general stationary-increment fact. The originality and value claim is therefore restricted to its standard-map realization together with the full equality rigidity \(m\in\pi\mathbb Z\) and \(T^2=\mathrm{id}\), not to the generic covariance algebra alone.

Because the proof is short, an equivalent standard-map-specific equality-rigidity observation could remain in unindexed literature.

## References
1. B. V. Chirikov, “A universal instability of many-dimensional oscillator systems,” *Physics Reports* 52, 263–379 (1979), DOI 10.1016/0370-1573(79)90023-1.
2. J. D. Meiss, “Transient measures in the standard map,” *Physica D* 74, 254–267 (1994), DOI 10.1016/0167-2789(94)90197-X.
3. L. D. Pustyl'nikov, “The Standard Map and a Probabilistic Conjecture,” *Mathematische Nachrichten* 219, 181–187 (2000), DOI 10.1002/1522-2616(200011)219:1<181::AID-MANA181>3.0.CO;2-1.
4. J. De Simoi, “On cyclicity-one elliptic islands of the standard map,” *Journal of Modern Dynamics* 7, 153–208 (2013), DOI 10.3934/jmd.2013.7.153; preprint arXiv:1107.3518.
