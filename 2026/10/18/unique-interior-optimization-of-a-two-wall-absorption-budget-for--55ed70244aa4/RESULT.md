# Unique interior optimization of a two-wall absorption budget for persistent search

## Finding
Consider the one-dimensional two-velocity run-and-tumble search specified below. For every strictly positive total surface-absorption budget, and for **every starting position and every initial orientation distribution**, the expected absorption time has a **unique minimizer assigning strictly positive absorption rate to both sticky walls**. The optimum is explicit, has a sharp spatial-orientational balance criterion, and its linear response at the symmetric point is independent of the wall-detachment rate.

Use the nondimensional parameters
\[
p=\alpha L/v,\qquad h=\gamma L/v,\qquad B=KL/v,\qquad y=x_0/L,\qquad m=2\theta-1.
\]
Here \(p,h,B>0\), \(0<y<1\), and \(-1\le m\le1\). Let \(u=\kappa_\mathrm L L/v\), so that \(\kappa_\mathrm R L/v=B-u\). Put
\[
\delta=2p(y-1/2)+m,\qquad
\eta=\frac{B(p+1)}{B(p+1)+4h}\in(0,1).
\]
The **unique** minimizer \(0<u_*<B\) is
\[
\boxed{\displaystyle
u_* =\frac B2\left(1-\frac{\delta}{(p+1)\left[1+\sqrt{1-\eta\delta^2/(p+1)^2}\right]}\right).}
\]
The square root is strictly positive because \(|\delta|\le p+1\) and \(0<\eta<1\). In particular
\[
u_*>B/2\iff 2p(y-1/2)+m<0,\quad
u_*=B/2\iff 2p(y-1/2)+m=0.
\]
At \((y,m)=(1/2,0)\), the exact response coefficients are
\[
\boxed{\frac{\partial u_*}{\partial y}=-\frac{Bp}{2(p+1)},\qquad
\frac{\partial u_*}{\partial m}=-\frac{B}{4(p+1)}.}
\]
Both are independent of \(h\), although \(u_*\) itself generally depends on \(h\). Moreover \(u_*\) decreases strictly with either \(y\) or \(m\), with the other variable held fixed. Thus a particle located closer to the left wall can nevertheless receive a larger *right*-wall absorption allocation if sufficiently likely to start moving right.

## Assumptions and scope
A particle moves at velocity \(+v\) or \(-v\) on \((0,L)\), with \(L,v>0\), and reverses its velocity at independent exponential times with rate \(\alpha>0\). On encountering either endpoint it attaches to that wall. While attached to wall \(i\in\{\mathrm L,\mathrm R\}\), it either is absorbed at rate \(\kappa_i\ge0\), or detaches into the interior at rate \(\gamma>0\); these exponential clocks are independent of the bulk trajectory and of one another. The fixed sum is \(\kappa_\mathrm L+\kappa_\mathrm R=K>0\). Initially \(X_0=x_0\in(0,L)\), and independently the velocity is \(+v\) with probability \(\theta\in[0,1]\). The objective is the expected time to **eventual absorption at either wall**, unconditioned on which wall absorbs. There is no stochastic resetting, translational diffusion, bulk killing, or interaction between particles.

## Proof
Rescale position by \(L\) and time by \(L/v\). Let \(f_+(x),f_-(x)\) be conditional expected dimensionless absorption times for a particle at \(x\in(0,1)\) in the two velocity states. First-step conditioning gives the backward equations
\[
f_+'+p(f_--f_+)=-1,\qquad -f_-'+p(f_+-f_-)=-1,
\]
with sticky-boundary equations
\[
u f_-(0)+h\big(f_-(0)-f_+(0)\big)=1,\qquad
(B-u)f_+(1)+h\big(f_+(1)-f_-(1)\big)=1.
\]
Indeed a wall visit contributes an exponential holding time of mean \(1/(u+h)\) or \(1/(B-u+h)\), followed by absorption or inward detachment. Solving yields
\[
Q(u)=Bh+(p+1)u(B-u)>0,
\]
\[
C(u)=\frac{u[2+2h+(p+1)(B-u)]-B}{Q(u)},
\]
\[
S(u)=\frac{B[h(p+1)+p+1/2]+2h(h+1)
+[B(p+1)/2-p(h+1)]u-(p+1)u^2/2}{Q(u)},
\]
and, for every \(0\le x\le1\),
\[
f_\pm(x)=S(u)+p(C(u)x-x^2)\pm\frac{C(u)-2x}{2}.
\]
The exact dimensionless mean for the given starting ensemble is therefore
\[
F(u;y,m)=\theta f_+(y)+(1-\theta)f_-(y)
=S(u)+p(C(u)y-y^2)+\frac m2(C(u)-2y).
\]
Introduce \(w=py+m/2\) and \(\Theta(u)=-S'(u)/C'(u)\). Direct differentiation, with a denominator that stays strictly positive, gives
\[
C'(u)=\frac{(h+1)[(p+1)(B^2-2Bu+2u^2)+2Bh]}{Q(u)^2}>0.
\]
Writing \(t=2u/B-1\in[-1,1]\), the quotient simplifies exactly to
\[
\Theta(u)=\frac p2-\frac{(p+1)t}{1+\eta t^2},\qquad
\eta=\frac{B(p+1)}{B(p+1)+4h}\in(0,1).
\]
In particular,
\[
\frac{\partial F}{\partial u}=C'(u)[w-\Theta(u)]
=\frac{C'(u)}2\left[\delta+\frac{2(p+1)t}{1+\eta t^2}\right].
\]
The map \(t\mapsto t/(1+\eta t^2)\) is strictly increasing on \([-1,1]\), since its derivative is \((1-\eta t^2)/(1+\eta t^2)^2>0\). The derivative bracket is negative at \(u=0\) and positive at \(u=B\): the admissibility bound \(|\delta|\le p+1\) is **strictly smaller** than \(2(p+1)/(1+\eta)\), because \(\eta<1\). Consequently \(F\) first decreases then increases, and exactly one global minimizer lies in \((0,B)\), even when \(m=\pm1\).

At the unique zero of \(F_u\), put \(s=-\delta/[2(p+1)]\). The scalar equation \(s=t/(1+\eta t^2)\) has the unique solution in \((-1,1)\)
\[
t_* = \frac{2s}{1+\sqrt{1-4\eta s^2}}
=-\frac{\delta}{(p+1)[1+\sqrt{1-\eta\delta^2/(p+1)^2}]}.
\]
Substitution in \(u=B(1+t)/2\) proves the displayed optimizer. Its sign relative to \(B/2\) is exactly opposite the sign of \(\delta\), and differentiating the explicit formula at \(\delta=0\) gives \(\partial u_*/\partial\delta=-B/[4(p+1)]\). Since \(\partial\delta/\partial y=2p\) and \(\partial\delta/\partial m=1\), the two response coefficients follow. Global strict decrease in \(y,m\) follows from the strict increase of \(t/(1+\eta t^2)\).

## Verification
The standalone Python 3/SymPy program `verify.py` checks both backward equations, both wall equations, equality with the published unbiased generic-boundary MFPT expression, the exact derivatives, the monotonic-threshold identity, the endpoint inequalities, and an exact radical example. On execution the program reported `PASS 994 including all-direction boundary witnesses` after 994 symbolic/rational assertions. All essential universal claims above are established by inequalities in this proof rather than by enumerated tests.

For a concrete check, when \(p=h=B=1\), \(y=1/4\), and \(m=0\), the dimensionless objective reduces to
\[
F(u)=\frac{22u^2-6u-115}{16(2u^2-2u-1)},
\]
whose unique minimizer is \(u_*=(13-\sqrt{141})/2\simeq0.5628\). A rightward initial-velocity bias can reverse the optimal left-wall preference: at the same parameters with \(m=1\), \(\delta=1/2\) and therefore \(u_*<B/2\).

## Relationship to prior work
Bressloff (arXiv:2302.01158, first posted 2 February 2023) develops partially absorbing sticky boundaries for a run-and-tumble particle and derives MFPT and splitting-probability formulas, including independent wall contact-time statistics. Angelani (2023, DOI:10.1088/1751-8121/ad009e) derives a broad exact MFPT for different sticky/absorbing wall parameters; its equation (A1) specializes algebraically to our \(m=0\) expression. We do **not** claim that general MFPT representation as new. The present statement determines, for a fixed **joint** absorption-rate budget, the unique global optimum over **all** allocations and **all** initial direction distributions, and supplies an explicit closed-form allocation, never-concentrate-all theorem, sharp spatial-orientation reversal condition, and wall-detachment-independent local response. These conclusions require an optimization and global sign argument absent from the compared source results. Angelani (2024), *Optimal escapes in active matter*, optimizes **bulk tumbling rate** and studies different boundary configurations rather than allocating a fixed sum of two simultaneous absorption rates.

## Limitations
The theorem assumes positive wall detachment and positive bulk tumbling. The strict interior result may fail in singular limits where either tends to zero; it is not asserted uniformly through such limits. It does not treat spatially varying speed, non-exponential wall waiting, correlated resampling, or optimization of absorption probability by a specified deadline. The source MFPT already contains the algebraic information from which the optimization can be derived; future priority checks could find an unrecognized explicit optimization result. No independent mathematical audit has yet been performed.

## References
1. P. C. Bressloff, *Encounter-based model of a run-and-tumble particle II: absorption at sticky boundaries*, arXiv:2302.01158v1 (2 February 2023), https://arxiv.org/abs/2302.01158 .
2. L. Angelani, *One-dimensional run-and-tumble motions with generic boundary conditions*, Journal of Physics A (2023), DOI:10.1088/1751-8121/ad009e, https://doi.org/10.1088/1751-8121/ad009e .
3. L. Angelani, *Optimal escapes in active matter*, European Physical Journal E 47, 9 (2024), https://doi.org/10.1140/epje/s10189-023-00402-7 .
