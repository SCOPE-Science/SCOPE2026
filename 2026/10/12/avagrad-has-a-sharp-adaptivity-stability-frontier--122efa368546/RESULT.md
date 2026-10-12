# AvaGrad has a sharp adaptivity-stability frontier
## Finding

AvaGrad normalizes its delayed coordinatewise adaptive rates by their root-mean-square before applying the gradient. This exactly removes a common scalar rescaling of the adaptive-rate vector, but it does not remove coordinate anisotropy.

That distinction has a sharp one-step stability law.

Consider
\[
F(x)=\frac12\lambda\lVert x\rVert_2^2,
\qquad
\lambda>0,
\]
in dimension
\[
d\ge1.
\]
Take one source-form AvaGrad step with
\[
\beta_{1,t}=0,
\]
so the first moment equals the current gradient. Let the delayed second-moment state satisfy
\[
0\le v_i\le G^2
\]
for every coordinate, and let
\[
\varepsilon>0.
\]

The source coordinate rates are
\[
\eta_i=\frac1{\sqrt{v_i}+\varepsilon},
\]
and AvaGrad normalizes them by their root-mean-square:
\[
p_i
=
\frac{\eta_i}{\lVert\eta/\sqrt d\rVert_2}
=
\frac{\sqrt d\,\eta_i}{\lVert\eta\rVert_2}.
\]
Hence
\[
\frac1{G+\varepsilon}\le\eta_i\le\frac1{\varepsilon}.
\]

Define
\[
\rho=\frac{\varepsilon}{G+\varepsilon}.
\]
Then every effective coordinate rate obeys
\[
\boxed{
p_{\min}
=
\frac{\sqrt d\,\rho}{\sqrt{\rho^2+d-1}}
\le p_i\le
\frac{\sqrt d}{\sqrt{1+(d-1)\rho^2}}
=
p_{\max}.
}
\]
Both bounds are sharp.

Writing
\[
a=\alpha\lambda,
\]
the AvaGrad step is diagonal:
\[
x_i^+=(1-a p_i)x_i.
\]
Therefore
\[
\frac{F(x^+)}{F(x)}
=
\frac{\sum_i(1-a p_i)^2x_i^2}{\sum_i x_i^2}.
\]

The exact robust worst-case factor over every nonzero \(x\) and every admissible delayed state is
\[
\boxed{
\sup_{x\ne0,\;v\in[0,G^2]^d}
\frac{F(x^+)}{F(x)}
=
\max\left\{
(1-a p_{\min})^2,
(1-a p_{\max})^2
\right\}.
}
\]

Consequently, for
\[
a>0,
\]
AvaGrad is objective-nonincreasing for every admissible state and every nonzero vector exactly when
\[
\boxed{
a\le
\frac{2}{p_{\max}}
=
\frac{2}{\sqrt d}
\sqrt{1+(d-1)\rho^2}.
}
\]
It is uniformly contractive exactly when
\[
\boxed{
0<a<
\frac{2}{\sqrt d}
\sqrt{1+(d-1)\rho^2}.
}
\]

At equality, an extremal state with one coordinate at
\[
v_i=0
\]
and every other coordinate at
\[
v_j=G^2
\]
has
\[
p_i=p_{\max}.
\]
Choosing \(x\) supported on that coordinate gives
\[
1-a p_i=-1,
\]
so the objective is preserved by an exact sign reflection. Above the threshold, the same state and direction increase the objective.

The frontier interpolates cleanly between two regimes. If adaptability is weak and the coordinate rates are nearly equal,
\[
\rho\to1,
\]
then
\[
p_{\max}\to1
\]
and the robust ceiling approaches the scalar gradient-descent value
\[
a\le2.
\]
If the adaptive rates can be arbitrarily heterogeneous,
\[
\rho\downarrow0,
\]
then
\[
p_{\max}\to\sqrt d
\]
and the robust ceiling approaches
\[
a\le\frac2{\sqrt d}.
\]

## Assumptions and scope

The theorem concerns one source-form AvaGrad step with no first-moment memory at that step:
\[
\beta_{1,t}=0.
\]
This isolates the preconditioner-normalization mechanism.

The second-moment vector is delayed exactly as in the defining algorithm and is treated as an arbitrary state satisfying the source bounded-gradient consequence
\[
0\le v_i\le G^2.
\]
The theorem is therefore a robust statewise guarantee, not a claim that every extremal state occurs along every deterministic quadratic trajectory.

The denominator convention is the defining paper's
\[
\eta_i=\frac1{\sqrt{v_i}+\varepsilon}.
\]

The objective is isotropic. Curvature anisotropy would introduce an additional interaction with the diagonal adaptive rates.

## Proof

Set
\[
\ell=\frac1{G+\varepsilon},
\qquad
u=\frac1{\varepsilon},
\qquad
\rho=\frac{\ell}{u}.
\]
For a fixed coordinate \(i\),
\[
p_i
=
\frac{\sqrt d\,\eta_i}
{\sqrt{\eta_i^2+\sum_{j\ne i}\eta_j^2}}.
\]
This expression is increasing in \(\eta_i\) and decreasing in every other \(\eta_j\).

Therefore its maximum over
\[
\ell\le\eta_j\le u
\]
occurs at
\[
\eta_i=u,
\qquad
\eta_j=\ell\quad(j\ne i),
\]
giving
\[
p_{\max}
=
\frac{\sqrt d\,u}
{\sqrt{u^2+(d-1)\ell^2}}
=
\frac{\sqrt d}{\sqrt{1+(d-1)\rho^2}}.
\]

Likewise its minimum occurs at
\[
\eta_i=\ell,
\qquad
\eta_j=u\quad(j\ne i),
\]
giving
\[
p_{\min}
=
\frac{\sqrt d\,\ell}
{\sqrt{\ell^2+(d-1)u^2}}
=
\frac{\sqrt d\,\rho}{\sqrt{\rho^2+d-1}}.
\]

For the isotropic quadratic,
\[
\nabla F(x)=\lambda x.
\]
With
\[
\beta_{1,t}=0,
\]
the AvaGrad update is
\[
x_i^+
=
x_i-\alpha p_i\lambda x_i
=
(1-a p_i)x_i.
\]
Thus the objective ratio is a convex combination of the coordinate factors
\[
(1-a p_i)^2.
\]
For fixed \(p\), its supremum over nonzero \(x\) is the largest coordinate factor.

The scalar function
\[
(1-a p)^2
\]
is convex in \(p\). Therefore its maximum on
\[
[p_{\min},p_{\max}]
\]
occurs at an endpoint. Since both endpoint rate values are attained by admissible states, the robust objective factor is exactly
\[
\max\left\{
(1-a p_{\min})^2,
(1-a p_{\max})^2
\right\}.
\]

For
\[
a>0
\]
and
\[
p_i>0,
\]
all coordinate factors are at most one exactly when
\[
a p_i\le2
\]
for every coordinate and every admissible state. The sharp condition is therefore
\[
a p_{\max}\le2.
\]
Strict inequality gives strict contraction because
\[
p_{\min}>0.
\]

## Verification

The accompanying `verify.py` samples bounded delayed second-moment states, reconstructs the source AvaGrad normalization, and compares direct objective ratios with the closed endpoint envelope.

It verifies the sharp \(p_{\min}\) and \(p_{\max}\) states, the exact boundary reflection, the strict-contraction side, the unstable side, and the limiting SGD and dimension-dependent regimes.

The finite computations are transcription guards. The rate bounds and if-and-only-if stability frontier are proved analytically above.

## Relationship to prior work

Savarese, McAllester, Babu, and Maire introduce AvaGrad by delaying the adaptive-rate computation and normalizing the coordinatewise rate vector by its Euclidean root-mean-square. Their motivation is to make the global learning rate and the adaptability parameter more separable. Their analysis emphasizes invariance to common scaling of the adaptive-rate vector and gives a stochastic nonconvex convergence guarantee.

The defining paper also explicitly studies the interaction between the global learning rate and the adaptability parameter in experiments. Larger denominator regularization reduces adaptivity, while smaller values permit more heterogeneous coordinate rates.

The inspected defining full text does not state the exact isotropic-quadratic robust stability frontier above, the sharp coordinate-rate dynamic range after root-mean-square normalization, or the limiting transition from
\[
2
\]
to
\[
2/\sqrt d.
\]

The result does not contradict the paper's scale-normalization observation. Multiplying every \(\eta_i\) by the same positive constant leaves every \(p_i\) unchanged exactly. The theorem instead isolates the remaining dependence on the *shape* of the adaptive-rate vector: root-mean-square normalization removes common scale but not coordinate concentration.

Focused published-record searches for AvaGrad quadratic stability, normalized-rate coordinate concentration, adaptability-dependent stability, and exact learning-rate frontiers did not identify an implication-equivalent result.

## Limitations

The theorem is one-step and deterministic conditional on the delayed state.

It uses
\[
\beta_{1,t}=0
\]
and does not classify momentum-state dynamics.

It assumes an isotropic quadratic and a coordinatewise second-moment state bounded by the source gradient bound.

The sharp extremal state is a robust admissible-state construction; it need not arise on every deterministic training trajectory.

## References

1. Pedro Savarese, David McAllester, Sudarshan Babu, and Michael Maire, “Domain-independent Dominance of Adaptive Methods,” arXiv:1912.01823v1, first submitted 2019-12-04; later published at CVPR 2021.
