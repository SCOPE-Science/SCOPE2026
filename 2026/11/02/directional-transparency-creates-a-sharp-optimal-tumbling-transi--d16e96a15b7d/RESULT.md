# Directional transparency creates a sharp optimal-tumbling transition on a reactive circle

## Finding

Consider a persistent particle on a circle with independent velocity reversals and a single permeable point detector. A nonlethal crossing carries the particle through without a change of velocity; the detector absorbs a clockwise crossing with probability \(p\) and a counterclockwise crossing with probability \(q\), independently on every encounter. For uniform initial position and equiprobable initial directions, the exact dimensionless mean absorption time is

\[\boxed{\frac{vT(\lambda)}{L}=\frac{z}{6}+\frac{12-6(p+q)+3pq}{6s}+\frac{(p-q)^2}{2s(sz+pq)}},\qquad z=\frac{\lambda L}{v},\quad s=p+q-pq.\]

The optimal tumbling rate undergoes a sharp transition:

\[\boxed{\lambda_*=\frac{v}{L}\max\!\left\{0,\frac{\sqrt3\,|p-q|-pq}{s}\right\}}.\]

For \(p\ne q\) the objective is strictly convex and the minimizer is unique. When \(p=q\), the objective is affine with strictly positive slope, so the unique minimizer is also zero. In particular, a strictly positive reversal rate is beneficial exactly when \(\sqrt3\,|p-q|>pq\). This criterion depends only on the two direction-specific absorption probabilities and not on circumference or speed.

For \(p=1\), \(q=1/4\), \(L=v=1\), the exact optimum is \(\lambda_*=(3\sqrt3-1)/4\), at which \(T(\lambda_*)=5/6+\sqrt3/4\); the ballistic mean is \(T(0)=2\).

## Assumptions and scope

Fix \(L,v>0\), \(\lambda\geq0\), \(p,q\in(0,1]\). The position \(X_t\) lies on the ring \(\mathbb R/L\mathbb Z\), and the velocity \(V_t\in\{-v,+v\}\) changes sign at independent Poisson events of rate \(\lambda\). The detector is the single point \(0\). Each crossing with direction \(+v\) has independent absorption probability \(p\); with direction \(-v\) the probability is \(q\). If the particle survives, it crosses the point transparently and continues in the same direction. The initial position is Lebesgue-uniform on \((0,L)\), independent of an equiprobable initial velocity. Time is continuous, and absorption is the stopping time of first successful detection.

This is not a reflecting-wall model. Crucially, an unsuccessful hit transmits without reversing the particle. The two positive reaction probabilities exclude inaccessible one-way detectors at zero tumble rate.

## Proof

**Finiteness and the backward equations.** Put \(\tau=L/v\). Conditional on the present position and direction, a trajectory with no tumbles in the next \(\tau\) traverses the detector at least once (apart from an event of zero initial probability), and its first such traversal succeeds with conditional probability at least \(m=\min(p,q)>0\). For \(\lambda\geq0\), the probability of no tumble for duration \(\tau\) is \(e^{-\lambda\tau}\). Hence the survival probability across each successive block of duration \(\tau\) contracts by at least the fixed positive amount \(m e^{-\lambda\tau}\), by the strong Markov property. Absorption occurs almost surely and has a finite mean. The backward mean functions \(f_\pm(x)\), for \(0<x<L\), obey

\[v f_+'(x)+\lambda(f_-(x)-f_+(x))=-1,\qquad -v f_-'(x)+\lambda(f_+(x)-f_-(x))=-1.\]

At the detector, the renewal boundary conditions are

\[f_+(L)=(1-p)f_+(0),\qquad f_-(0)=(1-q)f_-(L).\]

The first identity corresponds to clockwise arrival at \(L\) and immediate crossing to \(0\); the second corresponds to counterclockwise arrival at \(0\) and immediate crossing to \(L\). Absorption contributes zero additional survival time on a successful crossing. The equations also remain valid at \(\lambda=0\).

**Exact solution.** Set \(y=x/L\), \(z=\lambda L/v\), \(F_\pm(y)=(v/L)f_\pm(Ly)\). Write \(D=F_+-F_-\) and \(S=F_++F_-\). Subtracting and adding the two backward equations yields

\[D'(y)=-2,\qquad S'(y)=2zD(y).\]

Thus there are constants \(A,B\) with

\[D(y)=A-2y,\qquad S(y)=B+2z(Ay-y^2).\]

Let \(s=p+q-pq>0\), \(H=sz+pq>0\). Substituting \(F_\pm=(S\pm D)/2\) into the two detector conditions and solving the resulting \(2\times2\) system gives, with no singular denominator in the allowed range,

\[A=1-\frac{p-q}{H},\qquad B=\frac{s+z(4-p-3q+pq)}{H}.\]

Uniformly averaging both initial velocities and all initial positions, the dimensionless mean equals

\[\frac{vT}{L}=\frac12\int_0^1S(y)\,dy=\frac B2+z\left(\frac A2-\frac13\right).\]

Direct substitution and collecting terms yields

\[\frac{vT}{L}=\frac{s z^2+[12-6(p+q)+4pq]z+3s}{6(sz+pq)}.\]

Dividing this rational function into its affine and reciprocal components gives exactly the displayed finding formula. Notice that \(H>0\) independently certifies uniqueness of the backward solution, including the ballistic boundary.

**Optimization and endpoint.** Differentiating the formula with respect to \(z\geq0\) gives

\[\frac{d}{dz}\left(\frac{vT}{L}\right)=\frac16-\frac{(p-q)^2}{2(sz+pq)^2},\qquad \frac{d^2}{dz^2}\left(\frac{vT}{L}\right)=\frac{s(p-q)^2}{(sz+pq)^3}.\]

When \(p=q\), the derivative is \(1/6>0\) everywhere. Otherwise the second derivative is strictly positive and the first derivative tends to \(1/6>0\) as \(z\to\infty\). It has one positive zero if and only if its value at the origin is negative, equivalently \(\sqrt3|p-q|>pq\), and the zero solves \(sz+pq=\sqrt3|p-q|\). Equality in the threshold leaves the unique minimum at \(z=0\). Since the objective grows as \(z/6\) at infinity, these critical points are global. The explicit parameter example follows by exact substitution.

## Verification

A standalone Python checker is included as `check.py`. It independently constructs a finite-volume continuous-time Markov chain with \(2N\) velocity-labelled cells. Cell transitions occur at rate \(vN/L\), reversals at rate \(\lambda\), and only transitions across the wrap point are killed with the appropriate direction-specific probability. The checker solves the finite killed-generator Poisson equation, checks convergence toward the analytical continuum answer at \(N=80,200,500\), and tests the closed-form optimum at several interior and boundary parameter choices. Execution succeeded on the embedded checker with NumPy and SciPy installed; the exact all-parameter statement is proved above, not inferred from these finite computations. A separate symbolic rearrangement of the solved boundary equations verified the claimed rational and reciprocal expressions identically.

## Relationship to prior work

Masoliver, Porrà and Weiss study the telegrapher's equation with an absorbing/reflecting **boundary** and derive radiation boundary conditions. Angelani develops mean absorption times for one-dimensional run-and-tumble motion with two partially **reflecting endpoints**, including asymmetric boundary strengths; these do not enforce the periodic *transmission-preserving* detector conditions above. Tejedor, Voituriez and Bénichou establish optimal persistence in a different discrete persistent-search problem with perfect capture. De Gregorio and Iafrate establish analytic properties of the unabsorbed telegraph process **on a circle**, which provides a close ambient process but not a point-reactive mean-time optimization. Mercado-Vásquez and Boyer study independently stochastic-gated targets between reflecting walls. Marris and Giuggioli develop a considerably broader **discrete** correlated-walk renewal framework, including partial and directional first passage on periodic lattices; it is the closest structural coverage risk but does not state the continuous-time circle transparency formula or the sharp optimally positive turning-rate criterion. Jeon, Go and Kim study partially absorbing targets and optimal **speed** in reflecting confinement. Neither a failed keyword search nor a partition of problems proves priority; the precise novelty assessed here is the complete continuous reactive-circle threshold and its closed-form minimizer, not the underlying telegraph process or linear backward-equation method.

## Limitations

The derivation relies on a single point trap with direction-dependent, independent Bernoulli absorption at each crossing, transparent survival, equal-magnitude velocities, constant independent Poisson reversal rate, and a uniform/equiprobable initial law. An extended target, sticky or reflective encounters, resetting, non-Poisson tumbling or spatially varying kinetics is outside the claim. The exact quantitative limit as one reaction probability tends to zero does not justify substituting zero in the ballistic model: positive reaction probabilities are required. Historical priority remains provisional because broader first-passage formulations may yield an equivalent result through a nontrivial specialization; independent scientific validation has not been performed.

## References

1. J. Masoliver, J. M. Porrà and G. H. Weiss, *Solution to the telegrapher's equation in the presence of reflecting and partly reflecting boundaries*, Physical Review E **48**, 939 (1993), https://doi.org/10.1103/PhysRevE.48.939 . Open full text: https://diposit.ub.edu/bitstreams/b5933acc-0d93-4c6f-a9c7-b3de28f4a538/download .
2. V. Tejedor, R. Voituriez and O. Bénichou, *Optimizing persistent random searches*, https://arxiv.org/abs/1111.1881 (2011).
3. L. Angelani, *Run-and-tumble particles, telegrapher's equation and absorption problems with partially reflecting boundaries*, https://arxiv.org/abs/1601.04845 (2016 preprint).
4. A. De Gregorio and F. Iafrate, *Telegraph random evolutions on a circle*, https://arxiv.org/abs/2011.03025 (2020).
5. G. Mercado-Vásquez and D. Boyer, *First hitting times between a run-and-tumble particle and a stochastically-gated target*, https://arxiv.org/abs/2102.11787 (2021).
6. E. Jeon, B. G. Go and Y. W. Kim, *Searching for a partially absorbing target by a run-and-tumble particle in a confined space*, https://arxiv.org/abs/2310.04016 (2023).
7. D. Marris and L. Giuggioli, *Persistent and anti-Persistent Motion in Bounded and Unbounded Space: Resolution of the First-Passage Problem*, https://arxiv.org/abs/2404.13360 (2024).
