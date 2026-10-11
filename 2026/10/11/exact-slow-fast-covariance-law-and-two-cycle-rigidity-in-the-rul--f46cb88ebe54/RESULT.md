# Exact slow–fast covariance law and two-cycle rigidity in the Rulkov neuron map
## Finding
Consider the classical individual Rulkov map
\[
x_{n+1}=f(x_n,y_n),
\qquad
y_{n+1}
=
y_n-\mu(x_n+1-\sigma),
\qquad
\mu>0,
\]
where \(f\) is the standard piecewise fast map and \(y\) is the slow variable.

Let \(\nu\) be any compactly supported invariant Borel probability measure. Put
\[
m=\sigma-1.
\]
Then the stationary fast-variable mean is pinned exactly:
\[
\boxed{
\mathbb E_\nu[x]=m
}.
\]

More strongly, the slow–fast covariance is fixed by the fast variance:
\[
\boxed{
\operatorname{Cov}_\nu(x,y)
=
\frac{\mu}{2}\operatorname{Var}_\nu(x)
}.
\]

Therefore the covariance matrix of \((x,y)\) satisfies the sharp positive-semidefinite constraint
\[
\boxed{
\operatorname{Var}_\nu(y)
\ge
\frac{\mu^2}{4}\operatorname{Var}_\nu(x)
}.
\]
Equivalently,
\[
\boxed{
4\det\Sigma_\nu
=
4\operatorname{Var}_\nu(x)\operatorname{Var}_\nu(y)
-
\mu^2\operatorname{Var}_\nu(x)^2
\ge0
}.
\]

The equality case is dynamically rigid. If
\[
\operatorname{Var}_\nu(x)>0
\]
and
\[
\operatorname{Var}_\nu(y)
=
\frac{\mu^2}{4}\operatorname{Var}_\nu(x),
\]
then equality in Cauchy–Schwarz forces
\[
y-\mathbb E_\nu[y]
=
\frac{\mu}{2}(x-m)
\]
almost surely. The slow update then gives
\[
y_{n+1}-\mathbb E_\nu[y]
=
-\frac{\mu}{2}(x_n-m).
\]
Because the same affine relation holds at the image point,
\[
\frac{\mu}{2}(x_{n+1}-m)
=
-\frac{\mu}{2}(x_n-m),
\]
hence
\[
\boxed{
x_{n+1}-m=-(x_n-m)
}
\]
almost surely. Applying this twice gives
\[
x_{n+2}=x_n
\]
and likewise
\[
y_{n+2}=y_n
\]
almost surely.

Thus equality with nonzero fast variance can occur only on dynamics of period dividing two. In particular, every ergodic invariant state with nonzero fast variance that is not a two-cycle obeys
\[
\boxed{
\operatorname{Var}_\nu(y)
>
\frac{\mu^2}{4}\operatorname{Var}_\nu(x)
}
\]
and
\[
\boxed{
0<
\operatorname{Corr}_\nu(x,y)
<
1
}.
\]
The correlation is explicitly
\[
\operatorname{Corr}_\nu(x,y)
=
\frac{\mu}{2}
\sqrt{
\frac{\operatorname{Var}_\nu(x)}
{\operatorname{Var}_\nu(y)}
}.
\]

The same balance can be written directly in terms of the slow increment
\[
\Delta y_n=y_{n+1}-y_n=-\mu(x_n-m).
\]
Stationarity gives
\[
\boxed{
\operatorname{Var}_\nu(\Delta y)
=
\mu^2\operatorname{Var}_\nu(x)
}
\]
and
\[
\boxed{
\operatorname{Cov}_\nu(y,\Delta y)
=
-\frac12\operatorname{Var}_\nu(\Delta y)
}.
\]

For the chaotic spiking-bursting example displayed in the classical chaos paper,
\[
(\alpha,\mu,\sigma)
=
(5.6,0.001,0.322),
\]
one has
\[
m=-0.678.
\]
Hence every compact invariant state at these parameters satisfies
\[
\boxed{
\mathbb E[x]=-0.678
}
\]
and
\[
\boxed{
\operatorname{Cov}(x,y)
=
0.0005\,\operatorname{Var}(x)
}.
\]

## Assumptions and scope
The result concerns the original two-dimensional Rulkov neuron map
\[
x_{n+1}=f(x_n,y_n),
\qquad
y_{n+1}=y_n-\mu(x_n+1-\sigma),
\]
with the piecewise fast map introduced in the source and \(\mu>0\).

Compact support guarantees the second moments used here. No smoothness or invertibility of the piecewise fast map is required, and no ergodicity assumption is needed for the mean and covariance identities.

The source preprint was publicly posted on 5 January 2002. A later mathematical study of Rulkov-neuron dynamics lists MSC \(37D45\) first; this classification is used here.

The strict inequality is asserted for ergodic states with nonzero fast variance that are not supported on a two-cycle. Fixed points have zero fast variance and are outside that strict statement.

## Proof
Write
\[
m=\sigma-1.
\]
The slow equation is
\[
y_{n+1}-y_n=-\mu(x_n-m).
\]

Since \(\nu\) is invariant,
\[
\mathbb E[y_{n+1}-y_n]=0.
\]
Therefore
\[
-\mu(\mathbb E[x]-m)=0,
\]
and because \(\mu>0\),
\[
\mathbb E[x]=m.
\]

Apply stationarity to the second moment of the slow variable:
\[
0
=
\mathbb E[y_{n+1}^2-y_n^2].
\]
Using
\[
y_{n+1}=y_n-\mu(x_n-m),
\]
we obtain
\[
0
=
-2\mu\mathbb E[y(x-m)]
+
\mu^2\mathbb E[(x-m)^2].
\]
Because
\[
\mathbb E[x-m]=0,
\]
the first expectation is
\[
\operatorname{Cov}(x,y),
\]
while the second is
\[
\operatorname{Var}(x).
\]
Thus
\[
\operatorname{Cov}(x,y)
=
\frac{\mu}{2}\operatorname{Var}(x).
\]

Positive semidefiniteness of the covariance matrix gives
\[
\operatorname{Cov}(x,y)^2
\le
\operatorname{Var}(x)\operatorname{Var}(y).
\]
If
\[
\operatorname{Var}(x)>0,
\]
substitution yields
\[
\operatorname{Var}(y)
\ge
\frac{\mu^2}{4}\operatorname{Var}(x).
\]
When
\[
\operatorname{Var}(x)=0,
\]
the same inequality is immediate.

Suppose now that
\[
\operatorname{Var}(x)>0
\]
and equality holds. Equality in Cauchy–Schwarz implies an affine almost-sure relation. Its coefficient is fixed by the covariance:
\[
y-\mathbb E[y]
=
\frac{\operatorname{Cov}(x,y)}
{\operatorname{Var}(x)}
(x-m)
=
\frac{\mu}{2}(x-m).
\]

At the image point, the slow equation gives
\[
y_{n+1}-\mathbb E[y]
=
\frac{\mu}{2}(x_n-m)-\mu(x_n-m)
=
-\frac{\mu}{2}(x_n-m).
\]
Invariance means the affine equality also holds for
\[
(x_{n+1},y_{n+1})
\]
almost surely:
\[
y_{n+1}-\mathbb E[y]
=
\frac{\mu}{2}(x_{n+1}-m).
\]
Comparing the last two equations gives
\[
x_{n+1}-m
=
-(x_n-m).
\]
Applying the relation one more time gives
\[
x_{n+2}=x_n.
\]
The affine relation then also gives
\[
y_{n+2}=y_n.
\]
Thus the invariant dynamics is supported almost surely on points of period dividing two.

For an ergodic invariant state with nonzero fast variance, the equality case is therefore a two-cycle. Every other such ergodic state has strict covariance determinant and hence
\[
0<
\operatorname{Corr}(x,y)
<
1.
\]

Finally,
\[
\Delta y=-\mu(x-m),
\]
so
\[
\operatorname{Var}(\Delta y)
=
\mu^2\operatorname{Var}(x).
\]
Moreover,
\[
\operatorname{Cov}(y,\Delta y)
=
-\mu\operatorname{Cov}(x,y)
=
-\frac{\mu^2}{2}\operatorname{Var}(x)
=
-\frac12\operatorname{Var}(\Delta y).
\]

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the second-moment stationarity algebra leading to
\[
\operatorname{Cov}(x,y)
=
\frac{\mu}{2}\operatorname{Var}(x),
\]
the determinant form of the variance inequality, the slow-increment identities, and the exact source-parameter specialization
\[
\sigma-1=-0.678,
\qquad
\frac{\mu}{2}=0.0005.
\]

It also verifies algebraically that the equality-line relation and the slow update force the reflection law
\[
x_{n+1}-m=-(x_n-m).
\]

The stored checker output is `VERIFY_OK`.

The passage from equality in Cauchy–Schwarz to period-two rigidity is an analytic argument; no finite orbit enumeration or numerical trajectory is used.

## Relationship to prior work
Rulkov's original full-text preprint introduces the two-dimensional slow–fast map, explicitly identifies
\[
x_s=-1+\sigma
\]
as the level at which the slow variable is instantaneously unchanged, and analyzes silence, tonic spiking, periodic bursting, and chaotic spiking-bursting regimes. The source does not formulate a stationary covariance or variance law.

Shilnikov and Rulkov give a detailed same-map study of the origin of chaos. Their complete article writes the same slow update, studies the fixed point, subcritical Andronov–Hopf bifurcation, canards, homoclinic geometry, and chaotic spiking-bursting mechanisms. Full-text searches found no `covariance`, `variance`, or `invariant measure` formulation.

A later open study maps the distribution of spiking and bursting over extensive parameter regions using Lyapunov exponents and periodicity diagrams. Its full text likewise contains no covariance or variance formulation.

The accepted result is implication-wise different from the familiar nullcline statement that the slow drift vanishes pointwise when
\[
x=\sigma-1.
\]
The new statement says that every compact stationary state, including chaotic bursting states, has exactly that fast-variable mean and that its full slow–fast covariance is forced by its fast variance. The determinant equality further detects period-two dynamics.

## Limitations
The theorem constrains only first and second stationary moments; it does not determine the full invariant distribution or prove existence of a chaotic invariant measure.

The covariance relation follows from the slow feedback equation and therefore applies to any invariant state of the classical individual map, but it does not by itself distinguish different higher-period or chaotic attractors with identical second moments.

Equality in the variance bound is fully rigid for ergodic states with nonzero fast variance: such an equality state is a two-cycle. For nonergodic mixtures, the almost-sure reflection relation is the precise equality condition.

The later MSC source concerns Rulkov-neuron dynamics in a coupled setting and is used only to verify dynamical-systems classification, not as evidence for the scientific claim.

The author-hosted 2003 PDF was text-readable in the checked route, while page-image rendering was unavailable; the same equations and principal scope were independently available from the publisher abstract and the original full-text preprint.

Because the proof is short, an equivalent covariance identity could remain in unindexed literature.

## References
1. N. F. Rulkov, “Modeling of Spiking-Bursting Neural Behavior Using Two-Dimensional Map,” arXiv:nlin/0201006 (posted 5 January 2002); Physical Review E 65, 041922 (2002), DOI 10.1103/PhysRevE.65.041922.
2. A. L. Shilnikov and N. F. Rulkov, “Origin of Chaos in a Two-Dimensional Map Modeling Spiking-Bursting Neural Activity,” International Journal of Bifurcation and Chaos 13, 3325–3340 (2003), DOI 10.1142/S0218127403008521.
3. G. M. Ramírez-Ávila, S. Depickère, I. M. Jánosi, et al., “Distribution of spiking and bursting in Rulkov’s neuron model,” European Physical Journal Special Topics 231, 319–328 (2022), DOI 10.1140/epjs/s11734-021-00413-5.
4. I. Bashkirtseva, A. N. Pisarchik, and L. Ryashko, “Coexisting Attractors and Multistate Noise-Induced Intermittency in a Cycle Ring of Rulkov Neurons,” Mathematics 11, 597 (2023), DOI 10.3390/math11030597.
