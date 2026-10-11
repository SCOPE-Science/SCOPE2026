# Sharp one-sided stationary moment envelope for the Holmes cubic map
## Finding
Consider the Holmes cubic map
\[
T_{a,b}(x,y)
=
\left(
y,\,
ax-x^3-by
\right),
\]
with
\[
b>0,
\qquad
a>b+1.
\]
Define the nonzero fixed-point amplitude
\[
\rho=\sqrt{a-b-1}.
\]
Then
\[
(0,0),
\qquad
(\rho,\rho),
\qquad
(-\rho,-\rho)
\]
are fixed points.

Let \(\mu\) be any compactly supported invariant Borel probability measure. If
\[
m=\mathbb E_\mu[x],
\]
then invariance forces
\[
\boxed{
\mathbb E_\mu[y]=m
}
\]
and the exact cubic moment law
\[
\boxed{
\mathbb E_\mu[x^3]=\rho^2m
}.
\]

Suppose now that
\[
\operatorname{supp}\mu\subset[0,\infty)^2.
\]
Then
\[
\boxed{
0\le m\le\rho
}
\]
and
\[
\boxed{
\operatorname{Var}_\mu(x)
=
\operatorname{Var}_\mu(y)
\le
m(\rho-m)
}.
\]

The envelope is sharp at every admissible mean. For each
\[
m\in[0,\rho],
\]
put
\[
t=\frac{m}{\rho}.
\]
The invariant measure
\[
(1-t)\delta_{(0,0)}+t\delta_{(\rho,\rho)}
\]
has mean \(m\) and satisfies equality.

Moreover, equality is rigid:
\[
\boxed{
\operatorname{Var}_\mu(x)=m(\rho-m)
}
\]
holds if and only if \(\mu\) is a mixture of the two first-quadrant fixed-point atoms
\[
\delta_{(0,0)}
\quad\text{and}\quad
\delta_{(\rho,\rho)}.
\]
Therefore every compact first-quadrant stationary state that is not equilibrium-supported satisfies
\[
\boxed{
0<m<\rho,
\qquad
\operatorname{Var}_\mu(x)<m(\rho-m)
}.
\]

The map is odd:
\[
T_{a,b}(-x,-y)=-T_{a,b}(x,y).
\]
Hence the reflected theorem holds for compact invariant measures supported in the third quadrant. Writing
\[
M=|m|,
\]
one has
\[
0\le M\le\rho,
\qquad
\operatorname{Var}_\mu(x)
\le
M(\rho-M),
\]
with equality exactly for mixtures of
\[
\delta_{(0,0)}
\quad\text{and}\quad
\delta_{(-\rho,-\rho)}.
\]

There is also a finite-amplitude periodic-orbit consequence. Every nonconstant periodic orbit contained in the open first quadrant has at least one iterate satisfying
\[
0<x<\rho
\]
and at least one satisfying
\[
x>\rho.
\]
The reflected absolute-value statement holds in the open third quadrant.

At the published pre-crisis parameter values
\[
a=2.71,
\qquad
b=0.18,
\]
the two symmetric chaotic attractors lie separately in the first and third quadrants. Here
\[
\rho^2
=
2.71-0.18-1
=
\frac{153}{100},
\]
so
\[
\boxed{
\rho=\frac{\sqrt{153}}{10}
}.
\]
Thus every compact stationary state carried by either one-sided chaotic branch obeys the corresponding fixed-point-centered mean-variance envelope, strictly unless it is supported on fixed points.

## Assumptions and scope
The theorem concerns the standard two-dimensional Holmes cubic map in the orientation
\[
(x,y)\longmapsto(y,ax-x^3-by).
\]
Compact support guarantees existence of the moments used below.

The one-sided variance envelope assumes support in a closed coordinate quadrant. This is not an arbitrary restriction: a complete same-object study reports two symmetric coexisting chaotic attractors, one in the first quadrant and one in the third quadrant, immediately before their attractor-merging crisis.

The historical source for the underlying strange-attractor oscillator was published on 23 October 1979. A later complete same-object paper explicitly states that the displayed cubic map was introduced by Holmes and uses it to study attractor-merging crises and intermittency. The structured source date uses the earliest verified day-resolved public source in that lineage.

A bibliographic mathematical record for the Holmes strange-attractor work lists MSC \(37D45\) among its dynamical classifications. The present result is assigned primary MSC \(37D45\).

No ergodicity assumption is required. The theorem applies to fixed-point atoms, periodic-orbit measures, one-sided chaotic invariant measures, and their invariant convex mixtures when the support remains in the specified quadrant.

## Proof
Because the first coordinate of the image is the old second coordinate, invariance implies equality of the two coordinate marginals:
\[
(\pi_x)_\#\mu
=
(\pi_y)_\#\mu.
\]
In particular,
\[
\mathbb E[x]=\mathbb E[y]=m
\]
and
\[
\mathbb E[x^k]=\mathbb E[y^k]
\]
whenever the moment exists.

Applying invariance to the second coordinate gives
\[
m
=
\mathbb E[ax-x^3-by].
\]
Using equal coordinate means,
\[
m
=
(a-b)m-
\mathbb E[x^3],
\]
so
\[
\mathbb E[x^3]
=
(a-b-1)m
=
\rho^2m.
\]
This proves the global cubic moment law.

Now assume
\[
x\ge0,
\qquad
y\ge0
\]
on the support. If \(m=0\), nonnegativity implies
\[
x=y=0
\]
almost surely, so \(\mu=\delta_{(0,0)}\).

Assume \(m>0\). Cauchy-Schwarz applied to
\[
x^2=x^{1/2}x^{3/2}
\]
gives
\[
\mathbb E[x^2]^2
\le
\mathbb E[x]\mathbb E[x^3]
=
\rho^2m^2.
\]
Hence
\[
\mathbb E[x^2]
\le
\rho m.
\]
Therefore
\[
\operatorname{Var}(x)
=
\mathbb E[x^2]-m^2
\le
m(\rho-m).
\]
Since variance is nonnegative and \(m>0\), this also yields
\[
m\le\rho.
\]
Equality of coordinate marginals gives
\[
\operatorname{Var}(y)=\operatorname{Var}(x).
\]

For equality in the variance envelope, equality must hold in Cauchy-Schwarz. Thus
\[
x^{3/2}=c\,x^{1/2}
\]
almost surely for some constant \(c\), so every positive value of \(x\) is the same. The equality
\[
\mathbb E[x^2]=\rho\mathbb E[x]
\]
forces that positive value to be \(\rho\). Therefore
\[
x\in\{0,\rho\}
\]
almost surely. Equal coordinate marginals imply
\[
y\in\{0,\rho\}
\]
almost surely as well.

The support of an invariant probability measure under a continuous map is forward invariant. Among the four points in
\[
\{0,\rho\}^2,
\]
two cannot belong to such a support:
\[
T(0,\rho)
=
(\rho,-b\rho)
\]
leaves the first quadrant because \(b>0\), while
\[
T(\rho,0)
=
\left(0,(b+1)\rho\right)
\]
is outside \(\{0,\rho\}^2\). The remaining points
\[
(0,0)
\quad\text{and}\quad
(\rho,\rho)
\]
are fixed. Hence equality occurs exactly for their convex mixtures.

Odd symmetry gives the third-quadrant statement by reflection.

Finally, let a nonconstant periodic orbit lie in the open first quadrant. Its invariant orbit measure satisfies
\[
\mathbb E[x^3]=\rho^2\mathbb E[x],
\]
so over one period
\[
\sum x_n(x_n^2-\rho^2)=0.
\]
All \(x_n\) are positive. If every \(x_n\le\rho\), each summand is nonpositive and at least one is strictly negative unless every \(x_n=\rho\), which would give the fixed point. Likewise, if every \(x_n\ge\rho\), the sum is strictly positive unless the orbit is fixed. Thus a nonconstant positive periodic orbit has iterates on both sides of \(\rho\). Reflection proves the third-quadrant version.

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the invariant-mean algebra
\[
\mathbb E[x^3]=(a-b-1)m,
\]
the fixed-point identity
\[
\rho^2=a-b-1,
\]
and the sharp equality formulas for mixtures of the origin and a nonzero fixed point in a rational test family.

For the published pre-crisis parameters
\[
a=\frac{271}{100},
\qquad
b=\frac{18}{100},
\]
it verifies exactly that
\[
\rho^2=\frac{153}{100}.
\]

The Cauchy-Schwarz inequality, equality classification, support-invariance step, and periodic-orbit sign argument are analytic parts of the proof; they are not inferred from finite numerical orbit samples.

The stored checker output is `VERIFY_OK`.

## Relationship to prior work
Holmes' foundational strange-attractor article studies a periodically forced double-well Duffing oscillator and its Poincaré dynamics.

A complete 1994 same-object paper states that the cubic map
\[
(x,y)\mapsto(y,ax-x^3-by)
\]
was introduced by Holmes and studies its crises and intermittency. It reports, at
\[
a=2.71,
\qquad
b=0.18,
\]
a first-quadrant chaotic attractor together with its third-quadrant symmetric partner, followed near
\[
a\approx2.7154
\]
by an attractor-merging crisis. Full-document searches found no invariant-measure, covariance, average, or stationary-moment theorem matching the present statement.

A later stochastic-stability paper studies the Holmes map under noise and compares attractor robustness. Its accessible statement concerns escape and noise sensitivity rather than exact deterministic invariant-measure moments; restricted full text is retained as a residual comparison risk.

The accepted claim is not the existence of a strange attractor, symmetry of the two branches, or the crisis location. It is the exact invariant-measure cubic moment law and the sharp, fully classified mean-variance envelope that becomes available precisely on the one-sided branches documented in the published dynamics.

## Limitations
The sharp variance envelope requires support in one closed diagonal quadrant. It is not asserted for invariant measures spanning both signs after the attractor-merging crisis.

The theorem constrains first, second, and third moments but does not determine the invariant distribution or prove existence of the one-sided chaotic attractors.

The 1979 article is the historical source for the oscillator and associated strange Poincaré dynamics; the complete equation-level comparison for the cubic map is the 1994 paper that explicitly attributes the map to Holmes.

The later 2004 stochastic-stability paper was compared through its accessible scientific statement rather than complete full text.

Because the invariant-mean calculation is short, an equivalent moment identity could remain in unindexed map literature, although the checked same-object full text and semantic searches did not reveal the sharp one-sided variance envelope or its equality classification.

## References
1. P. Holmes, “A nonlinear oscillator with a strange attractor,” *Philosophical Transactions of the Royal Society of London. Series A* 292, 419–448 (1979), DOI 10.1098/rsta.1979.0068.
2. J. Güémez, M. A. Matías, I. Pastor, and M. A. F. Sanjuán, “Crises and intermittency in a map with one-dimensional reinjection,” *Physica D* 79, 164–173 (1994), PII 0167-2789(94)90082-5.
3. S. Kraut and U. Feudel, “Stability properties of nonhyperbolic chaotic attractors with respect to noise,” *Physical Review Letters* 93, 250603 (2004), DOI 10.1103/PhysRevLett.93.250603.
