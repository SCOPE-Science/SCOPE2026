# Sharp two-cycle bifurcation for gradient-clipped heavy-ball on a scalar quadratic
## Finding

Let
\[
f(x)=\frac{\lambda}{2}x^2,\qquad \lambda>0,
\]
and clip the scalar gradient before applying raw heavy-ball momentum:
\[
g(x)=\operatorname{clip}_C(\lambda x)
=\operatorname{sign}(x)\min(\lambda|x|,C),
\]
\[
v_t=\beta v_{t-1}+g(x_t),\qquad
x_{t+1}=x_t-\alpha v_t,
\]
where \(\alpha>0\), \(C>0\), \(\beta\in[0,1)\), and \(\operatorname{sign}(0)=0\). Define
\[
q=\alpha\lambda,\qquad r=\frac{C}{\lambda},\qquad q_\star=2(1+\beta).
\]

The origin is locally asymptotically stable exactly when
\[
0<q<q_\star.
\]
The nonzero period-two orbits have the following complete classification.

For \(q<q_\star\), there are no nonzero period-two orbits.

At the sharp boundary \(q=q_\star\), every amplitude
\[
0<a\le r
\]
gives a symmetric period-two orbit with positions \(a,-a\), and these are all nonzero period-two orbits.

For \(q>q_\star\), put
\[
c=\frac{\alpha C}{2(1+\beta)}
=\frac{q r}{2(1+\beta)}.
\]
Then every nonzero period-two orbit, up to phase, is
\[
x_{2k}=d+c,\qquad x_{2k+1}=d-c,
\]
with
\[
|d|\le c-r.
\]
Both points are in the clipped region. Thus the supercritical cycles form a one-parameter band of fixed half-gap \(c\) and variable center \(d\).

Each interior supercritical cycle, meaning \(|d|<c-r\), is locally normally attracting but not asymptotically stable as an individual cycle. Transverse momentum errors contract by the exact one-step factor \(\beta\), while the center coordinate is neutral. Gradient clipping therefore does not enlarge the local asymptotic-stability interval of heavy-ball on this quadratic. Instead, when the linear origin loses stability, clipping converts the instability into a continuum of persistent alternating cycles.

## Assumptions and scope

The theorem is deterministic and one-dimensional. The clipping operator is applied to the current gradient before it enters the raw heavy-ball recursion. This ordering matters: clipping a momentum accumulator, normalizing the momentum vector, or using normalized exponential-moving-average momentum defines a different dynamical system.

The theorem classifies period-two orbits and local stability of the origin, plus local normal attraction of interior supercritical cycle manifolds. It does not claim that every initial condition converges to one of these cycles, nor does it classify longer periodic or chaotic behavior.

The clipping threshold \(C\) is fixed, the stepsize \(\alpha\) is fixed, and \(\beta<1\). The scalar quadratic has positive curvature \(\lambda\).

## Proof

Inside the unclipped region \(|x|<r\), the state \(z_t=(x_t,v_{t-1})^\top\) evolves linearly as
\[
z_{t+1}=A z_t,
\qquad
A=\begin{bmatrix}
1-q&-\alpha\beta\\
\lambda&\beta
\end{bmatrix}.
\]
Its characteristic polynomial is
\[
p(\zeta)=\zeta^2-(1+\beta-q)\zeta+\beta.
\]
The real second-order Jury inequalities are
\[
1-\beta>0,\qquad q>0,\qquad 2(1+\beta)-q>0.
\]
Since \(\beta\in[0,1)\), the origin is locally asymptotically stable exactly for
\[
0<q<2(1+\beta).
\]
At \(q=q_\star\), the characteristic polynomial factors as
\[
p(\zeta)=(\zeta+1)(\zeta+\beta),
\]
so asymptotic stability is lost through the eigenvalue \(-1\).

Now suppose \(a,b\) are the two distinct positions of a period-two orbit, with the phase chosen so that \(x_t=a\) and \(x_{t+1}=b\). Let
\[
D=a-b.
\]
Periodicity of the position update gives
\[
v_t=\frac{D}{\alpha},\qquad v_{t-1}=-\frac{D}{\alpha}.
\]
The momentum recursion at the two phases therefore gives
\[
g(a)=\frac{(1+\beta)D}{\alpha},\qquad
g(b)=-\frac{(1+\beta)D}{\alpha}.
\]
Hence \(g(a)>0\), \(g(b)<0\), so \(a>0>b\). Write
\[
G=\frac{(1+\beta)D}{\alpha}>0.
\]
There are only two possibilities because the clipping map is linear before saturation and constant after saturation.

If \(G<C\), then both points are unclipped and
\[
a=\frac{G}{\lambda},\qquad b=-\frac{G}{\lambda},\qquad D=\frac{2G}{\lambda}.
\]
Combining this with \(G=(1+\beta)D/\alpha\) forces
\[
q=\alpha\lambda=2(1+\beta)=q_\star.
\]
Conversely, at this equality every \(0<a<r\) satisfies the two-cycle equations, and \(a=r\) is obtained at the saturation boundary. This proves the boundary family \(\{a,-a\}\), \(0<a\le r\).

If \(G=C\), both points are saturated. Then
\[
D=\frac{\alpha C}{1+\beta}=2c.
\]
Saturation requires \(a\ge r\) and \(b\le-r\), so \(D\ge2r\). This is equivalent to
\[
q\ge2(1+\beta).
\]
At equality, \(D=2r\), forcing the single endpoint pair \(a=r\), \(b=-r\), already contained in the boundary family. Above the boundary, write
\[
a=d+c,\qquad b=d-c.
\]
The saturation conditions become
\[
d+c\ge r,\qquad d-c\le-r,
\]
which are exactly
\[
|d|\le c-r.
\]
This also proves that no nonzero period-two orbit exists below the boundary, because the unsaturated case forces equality and the saturated case requires the boundary or above.

For local normal attraction, fix a supercritical interior cycle \(|d|<c-r\). In a sufficiently small neighborhood, the two iterates remain strictly clipped with alternating signs. Let the reference velocity be
\[
v_t^\star=(-1)^t\frac{C}{1+\beta}
\]
with the phase chosen consistently, and define \(e_t=v_t-v_t^\star\). Because the clipped forcing is locally constant on each phase,
\[
e_t=\beta e_{t-1}.
\]
Writing the position as
\[
x_t=d_t+(-1)^t c,
\]
the position update yields
\[
d_{t+1}=d_t-\alpha e_t.
\]
Therefore
\[
e_t=\beta^t e_0
\]
and, for \(0\le\beta<1\),
\[
d_t\longrightarrow d_\infty
=d_0-\frac{\alpha e_0}{1-\beta}.
\]
For sufficiently small initial perturbations, \(d_\infty\) remains in the open center band \((-c+r,c-r)\), making the assumed clipped alternating itinerary self-consistent. The transverse error contracts exactly by \(\beta\), whereas changing \(d\) moves along the cycle manifold and is neutral. For \(\beta=0\), transverse momentum error is removed in one step.

## Verification

The accompanying `verify.py` reconstructs the update from its definitions and checks four independent algebraic consequences: the Jury boundary of the unclipped linearization; exact boundary cycles at several amplitudes; exact supercritical cycles at interior and endpoint centers; and convergence of perturbed interior supercritical trajectories to the center predicted by the closed-form transverse recurrence.

The executable checks are finite transcription guards. Completeness of the two-cycle classification follows from the two exhaustive possibilities \(G<C\) and \(G=C\) in the proof, not from numerical enumeration.

## Relationship to prior work

Zhang, He, Sra, and Jadbabaie analyze gradient clipping and normalized gradient methods under a relaxed smoothness condition, with theory centered on clipped gradient descent rather than the fixed-step heavy-ball clipping dynamics above. Koloskova, Hendrikx, and Stich give tight deterministic and stochastic convergence guarantees for clipped gradient methods and characterize the effect of arbitrary clipping thresholds, again without this period-two heavy-ball phase diagram.

Mai and Johansson study stochastic gradient clipping and also a momentum extension for weakly convex problems. Their momentum construction and convergence analysis target stochastic weakly convex optimization and do not state the fixed-parameter scalar quadratic bifurcation above. Cutkosky and Mehta study normalized SGD with momentum, where normalization is applied to a momentum-based direction rather than clipping the current scalar gradient before a raw heavy-ball recursion. Orvieto studies the classical unclipped heavy-ball method on convex quadratics and provides nearby quadratic momentum theory without gradient saturation.

Targeted searches combining gradient clipping, heavy-ball or momentum, scalar quadratics, period-two or limit-cycle language, saturation, and the boundary \(\alpha\lambda=2(1+\beta)\) did not reveal the complete classification stated here. The main residual originality risk is that an equivalent switched-system or saturated-control calculation may exist under terminology not used in optimization papers.

## Limitations

The result is specific to a scalar positive quadratic and fixed clipping, stepsize, and momentum parameters. It does not provide a global basin of attraction for the cycle manifold, classify periods greater than two, or establish behavior in multiple dimensions.

Individual supercritical cycles are not asymptotically stable because the cycle manifold has a neutral center direction. Normal attraction is asserted only for interior cycles whose two points remain strictly inside the saturated regions under small perturbations. Endpoint cycles at \(|d|=c-r\) lie on the clipping kink and are excluded from that local smooth-manifold statement.

Changing the order of clipping and momentum, using normalized EMA momentum, clipping the momentum accumulator, or normalizing the momentum vector changes the recurrence and is outside the claim.

## References

1. Jingzhao Zhang, Tianxing He, Suvrit Sra, and Ali Jadbabaie, “Why gradient clipping accelerates training: A theoretical justification for adaptivity,” arXiv:1905.11881v1, 2019.
2. Ashok Cutkosky and Harsh Mehta, “Momentum Improves Normalized SGD,” arXiv:2002.03305v1, 2020.
3. Vien V. Mai and Mikael Johansson, “Stability and Convergence of Stochastic Gradient Clipping: Beyond Lipschitz Continuity and Smoothness,” arXiv:2102.06489v1, 2021.
4. Antonio Orvieto, “An Accelerated Lyapunov Function for Polyak's Heavy-Ball on Convex Quadratics,” arXiv:2301.05799v1, 2023.
5. Anastasia Koloskova, Hadrien Hendrikx, and Sebastian U. Stich, “Revisiting Gradient Clipping: Stochastic bias and tight convergence guarantees,” arXiv:2305.01588v1, 2023.
