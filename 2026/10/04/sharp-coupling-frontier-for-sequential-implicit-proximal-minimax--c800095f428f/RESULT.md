# Sharp coupling frontier for sequential implicit proximal minimax on a bilinear saddle
## Finding

Consider the strongly convex--strongly concave scalar saddle problem
\[
\min_x\max_y
\Phi(x,y),
\qquad
\Phi(x,y)
=
\frac a2x^2+cxy-\frac a2y^2,
\qquad
a>0,\quad c>0.
\]
It is a deterministic unconstrained specialization of the sequential implicit proximal update introduced in the recent stochastic minimax framework: take one component, no nonsmooth terms, no linear constraint, and
\[
g(x)=\frac a2x^2,
\qquad
f(x,y)=cxy,
\qquad
h(y)=\frac a2y^2.
\]

With a common constant step
\[
\alpha>0,
\]
define
\[
t=\alpha a,
\qquad
\kappa=\frac ca.
\]
The source update becomes
\[
(1+t)y_{k+1}
=
y_k+\kappa t x_k,
\]
followed by
\[
(1+t)x_{k+1}
=
x_k-\kappa t y_{k+1}.
\]

The unique saddle \((0,0)\) is globally asymptotically stable for every initial pair exactly in the following region:
\[
t>0
\quad\text{arbitrary if}\quad
0<\kappa\le1,
\]
and
\[
0<t<\frac{2}{\kappa-1}
\quad\text{if}\quad
\kappa>1.
\]
At the finite boundary
\[
t=\frac{2}{\kappa-1},
\]
one characteristic multiplier is exactly
\[
-1,
\]
so the strict inequality is necessary.

For every
\[
\kappa>0,
\]
the stable iteration has a unique rate-optimal step
\[
t_\star
=
\frac{2}{\sqrt{1+\kappa^2}-1}
=
\frac{2(1+\sqrt{1+\kappa^2})}{\kappa^2},
\]
with optimal asymptotic factor
\[
q_\star
=
\frac{\sqrt{1+\kappa^2}-1}
{\sqrt{1+\kappa^2}+1}.
\]
At this point the two characteristic roots coalesce at
\[
-\frac{1}{1+t_\star}.
\]

Before \(t_\star\), the roots are a complex conjugate pair and the exact factor is
\[
q(t,\kappa)=\frac{1}{1+t}.
\]
After \(t_\star\), the roots are negative real and the dominant modulus increases strictly. Hence the fastest stable step is the discriminant-collision point, not the stability ceiling.

For comparison, the unsplit proximal-point resolvent of the same saddle operator has factor
\[
q_{\mathrm{full}}(t,\kappa)
=
\frac{1}
{\sqrt{(1+t)^2+\kappa^2t^2}},
\]
which decreases strictly for every \(t>0\) and is unconditionally stable. Thus sequential block implicitness does not inherit the full resolvent's unconditional stability: once
\[
c>a,
\]
a finite flip boundary appears.

## Assumptions and scope

The result concerns the exact deterministic two-variable specialization of the source's implicit update system. There is one smooth component, no stochastic sampling, no nonsmooth regularizer, no multiplier, no inexact inner solve, and the same positive step is used in both blocks.

The coupling \(cxy\) is affine in each block and therefore convex in \(x\) and concave in \(y\). The diagonal terms make the objective \(a\)-strongly convex in \(x\) and \(a\)-strongly concave in \(y\), satisfying the source structural assumptions.

The statement is about the source's sequential update: the \(y\)-block is solved implicitly using \(x_k\), and the \(x\)-block is then solved implicitly using \(y_{k+1}\). It is not a statement about the simultaneous full resolvent, extragradient, optimistic gradient, Chambolle--Pock, or a stochastic/inexact implementation.

## Proof

The source update specializes to
\[
y_{k+1}
=
y_k+\alpha(c x_k-a y_{k+1}),
\]
and
\[
x_{k+1}
=
x_k-\alpha(a x_{k+1}+c y_{k+1}).
\]
After dividing by \(a\) through
\[
t=\alpha a,
\qquad
\kappa=\frac ca,
\]
this gives the two displayed implicit equations.

For
\[
z_k=
\begin{pmatrix}
x_k\\
y_k
\end{pmatrix},
\]
we have
\[
z_{k+1}=M(t,\kappa)z_k,
\]
where
\[
M(t,\kappa)
=
\frac{1}{(1+t)^2}
\begin{pmatrix}
1+t-\kappa^2t^2&-\kappa t\\
\kappa t(1+t)&1+t
\end{pmatrix}.
\]
Its trace and determinant are
\[
T
=
\frac{2+2t-\kappa^2t^2}{(1+t)^2},
\qquad
D
=
\frac{1}{(1+t)^2}.
\]
Thus the characteristic polynomial is
\[
p(r)=r^2-Tr+D.
\]

For a real monic quadratic, the Jury conditions are
\[
1-T+D>0,
\qquad
1+T+D>0,
\qquad
1-D>0.
\]
Here
\[
1-T+D
=
\frac{(1+\kappa^2)t^2}{(1+t)^2}>0,
\]
\[
1-D
=
\frac{t(2+t)}{(1+t)^2}>0,
\]
and
\[
1+T+D
=
\frac{4+4t+(1-\kappa^2)t^2}{(1+t)^2}.
\]
When
\[
0<\kappa\le1,
\]
the last quantity is positive for every \(t>0\). When
\[
\kappa>1,
\]
its positive zero is
\[
t_s
=
\frac{2}{\kappa-1},
\]
so Schur stability holds exactly for \(0<t<t_s\).

At \(t=t_s\),
\[
p(-1)=1+T+D=0.
\]
The second multiplier is then \(-D\), which has modulus below one. Therefore the boundary itself is nonconvergent for generic initial data and the finite ceiling is sharp.

The discriminant is
\[
\Delta
=
T^2-4D
=
\frac{\kappa^2t^2
\left[\kappa^2t^2-4(1+t)\right]}
{(1+t)^4}.
\]
It vanishes at the unique positive point
\[
t_\star
=
\frac{2}{\sqrt{1+\kappa^2}-1}.
\]
If \(\kappa>1\), then
\[
\sqrt{1+\kappa^2}>\kappa
\]
implies
\[
t_\star<t_s,
\]
so the collision lies strictly inside the stable region.

For \(0<t<t_\star\), the roots are complex conjugates. Their common modulus is
\[
\sqrt D
=
\frac{1}{1+t},
\]
which decreases strictly.

At \(t=t_\star\), the relation
\[
\kappa^2t_\star^2=4(1+t_\star)
\]
gives
\[
T=-\frac{2}{1+t_\star},
\]
so both roots equal
\[
-\frac{1}{1+t_\star}.
\]
Therefore
\[
q_\star
=
\frac{1}{1+t_\star}
=
\frac{\sqrt{1+\kappa^2}-1}
{\sqrt{1+\kappa^2}+1}.
\]

It remains to show that the spectral radius increases after the collision. For \(t>t_\star\), both roots are negative. Let \(q\) be the larger modulus and set
\[
y=(1+t)q.
\]
Then
\[
y+\frac1y
=
H(t),
\qquad
H(t)
=
\frac{\kappa^2t^2}{1+t}-2>2,
\]
with \(y>1\). Hence
\[
\frac{y'}{y}
=
\frac{H'}{\sqrt{H^2-4}}.
\]
Put
\[
J=\frac{\kappa^2t^2}{1+t}.
\]
A direct calculation gives
\[
\bigl[(1+t)H'\bigr]^2-(H^2-4)
=
4J(1+\kappa^2)>0.
\]
Since all quantities are positive,
\[
\frac{y'}y>\frac1{1+t}.
\]
Therefore
\[
\frac{d}{dt}\log q
=
\frac{y'}y-\frac1{1+t}>0.
\]
This proves that \(t_\star\) is the unique global minimizer of the asymptotic factor over the stable region.

Finally, the simultaneous saddle operator is
\[
F(x,y)
=
\begin{pmatrix}
ax+cy\\
ay-cx
\end{pmatrix}.
\]
Its full proximal-point resolvent
\[
(I+\alpha F)^{-1}
\]
has eigenvalues
\[
\frac{1}{1+t\pm i\kappa t},
\]
and therefore factor
\[
q_{\mathrm{full}}
=
\frac1{\sqrt{(1+t)^2+\kappa^2t^2}}.
\]
This is below one for every \(t>0\) and decreases strictly to zero, proving the stated separation between full and sequential implicitness.

## Verification

The standalone script `artifacts/verify_sequential_implicit_bilinear.py` reconstructs the matrix directly from the two sequential implicit block solves. It checks the trace, determinant, Jury expressions, finite flip boundary, discriminant collision, rate-optimal formula, and representative monotonicity on each side of the collision.

The script also evaluates the full resolvent factor for comparison. These finite checks are supporting verification only; the necessary-and-sufficient stability result and all-parameter rate optimum follow from the algebraic proof above.

## Relationship to prior work

Zhu, Wang, and Dai introduce the sequential implicit proximal update used here for strongly convex--strongly concave minimax problems, including nonsmooth regularizers, stochastic variance reduction, and linearly coupled constraints. Their paper proves global linear convergence under sufficient constant-step and inexactness conditions. Its inspected full text defines the staggered \(y\)-then-\(x\) implicit system but does not state a necessary-and-sufficient scalar coupling frontier or a closed-form rate-optimal step.

Ouyang studies an alternating proximity mapping method for strongly convex--strongly concave saddle problems with bilinear coupling and proves several sufficient conditions for linear convergence. The inspected problem statement and theorem summary are broader but sufficient-condition based; no exact two-dimensional Schur frontier, discriminant-collision optimizer, or comparison with the simultaneous resolvent was found.

Classical proximal-point theory treats the full resolvent of a maximal monotone operator. On the present strongly monotone linear saddle operator, that resolvent is unconditionally stable for every positive step, exactly as the direct calculation above shows. The accepted finding concerns the loss of that property caused by the source's sequential block implicitness, rather than a limitation of proximal-point theory itself.

Targeted published-research searches covered sequential and staggered implicit proximal updates, Gauss--Seidel saddle splitting, bilinear strong convexity/concavity, the exact flip threshold, the square-root rate formula, and equivalent eigenvalue language. No statement implying the combined sharp stability and rate phase diagram was found.

## Limitations

The result is exact for a symmetric scalar saddle with equal diagonal curvature and a common step. Unequal primal and dual curvatures, unequal steps, vector-valued coupling spectra, constraints, stochastic sampling, and inexact inner solves can produce different phase diagrams.

The finding does not claim that the source algorithm is unstable under its published sufficient parameter rules. It identifies the exact boundary of a natural constant-step deterministic specialization and shows why the word “implicit” alone does not imply full-resolvent stability.

Alternating saddle-point literature is extensive. Although the closest alternating-proximity work and classical full-resolvent theory were compared, an older exact scalar calculation under different splitting terminology remains the principal historical originality risk.

## References

1. K. Zhu, J. Wang, Y.-H. Dai, *A Stochastic Implicit Proximal Point Algorithm for Solving Linearly Constrained Stochastic Minimax Problems*, arXiv:2605.23488v1, 2026.
2. H. Ouyang, *Alternating Proximity Mapping Method for Strongly Convex-Strongly Concave Saddle-Point Problems*, arXiv:2310.20156v1, 2023.
3. R. T. Rockafellar, *Monotone Operators and the Proximal Point Algorithm*, SIAM Journal on Control and Optimization 14(5), 877--898, 1976. DOI: 10.1137/0314056.
