# Attracting period-three cycles and Li–Yorke chaos in exact proximal Polyak steps on strongly convex quadratics

## Finding
Consider the deterministic, one-sample ProxSPS algorithm with constant model parameter \(\alpha>0\), exact loss lower bound \(C=0\), and
\[
f(x)=\frac{(x-1)^2}{2},\qquad \varphi(x)=\frac{\lambda x^2}{2},\qquad \lambda>0.
\]
The composite objective \(\psi=f+\varphi\) is \((1+\lambda)\)-strongly convex, with unique minimizer \(x_\star=1/(1+\lambda)\). Its ProxSPS step is the unique solution
\[
F_{\alpha,\lambda}(x)=\arg\min_{y\in\mathbb R}
\left\{\max\left(\frac{(x-1)^2}{2}+(x-1)(y-x),0\right)
+\frac{\lambda y^2}{2}+\frac{(y-x)^2}{2\alpha}\right\}.
\]
For every \(0<\lambda<1/3\) and \(\alpha>4/(1-3\lambda)\), the interval \([0,1]\) is forward invariant. Put
\[
c=\frac{\alpha(2-\lambda)-1}{\alpha(2+\lambda)-1},\qquad
D=\alpha+3+4\alpha\lambda.
\]
The *exact* iteration on this interval is the continuous two-branch affine map
\[
F_{\alpha,\lambda}(x)=
\begin{cases}
(1+x)/2,&0\le x\le c,\\
\bigl(\alpha+(1-\alpha)x\bigr)/(1+\alpha\lambda),&c\le x\le1.
\end{cases}
\]
It possesses the explicit *least-period-three* orbit
\[
x_0=\frac{\alpha+3}{D},\qquad
x_1=\frac{\alpha+3+2\alpha\lambda}{D},\qquad
x_2=\frac{\alpha+3+3\alpha\lambda}{D},
\]
with the strict itinerary
\[
0<x_0<x_1<c<x_2<1,
\qquad F(x_0)=x_1,\quad F(x_1)=x_2,\quad F(x_2)=x_0.
\]
Its three-step multiplier is
\[
\mu_3=\frac{1-\alpha}{4(1+\alpha\lambda)}.
\]
Consequently, the three-cycle is locally attracting precisely when
\[
\alpha(1-4\lambda)<5
\]
within the stated period-three parameter domain; at equality its linearized multiplier has magnitude one and no attraction claim is made. The continuous invariant interval map also has points of every positive integer period and an uncountable Li–Yorke scrambled set, by the classical period-three theorem. This does **not** assert that typical iterates are chaotic: a locally attracting three-cycle and a Li–Yorke scrambled set can coexist.

For the rational witness \(\alpha=5\), \(\lambda=1/20\), the kink is \(c=35/37\), the attracting orbit is
\[
\frac89\ \longmapsto\ \frac{17}{18}\ \longmapsto\ \frac{35}{36}\ \longmapsto\ \frac89,
\]
and its three-step multiplier is exactly \(-4/5\). Thus even with a tight loss lower bound and a strictly convex quadratic objective, an excessively large constant ProxSPS model parameter can support stable nonconvergent optimization trajectories and interval chaos.

## Assumptions and scope
There is exactly one deterministic loss sample; no stochastic oracle error, nonconvexity, inaccurate lower bound, momentum, or numerical approximation is involved. The full optimization domain is \(\mathbb R\), while the claims about periodic points and Li–Yorke chaos concern its forward-invariant subinterval \([0,1]\). The regularizer is the genuine proximal quadratic \(\lambda x^2/2\), not a gradient added to the truncated loss model. Every subproblem is strongly convex and has a unique minimizer.

The assertion is an existence and parameter-family result for **large fixed** \(\alpha\), outside the small-stepsize regimes used in the source's convergence theorems. It is not a counterexample to those theorems. The term 'chaos' means precisely the classical Li–Yorke interval-map conclusion from the rigorously exhibited primitive period-three point; it is not a claim of positive measure of irregular orbits, ergodicity, or an attractor with positive Lyapunov exponent.

## Proof
**Exact ProxSPS map.** Schaipp, Gower, and Ulbrich's truncated-model ProxSPS update (their equation (11) and the squared-norm specialization in Lemma 1) for the present data reads
\[
F(x)=\frac{x-\tau(x)(x-1)}{1+\alpha\lambda},
\qquad
\tau(x)=\min\left\{\alpha,
\left[\frac{(1+\alpha\lambda)f(x)-\alpha\lambda(x-1)x}{(x-1)^2}\right]_+\right\}
\]
whenever \(x\ne1\); at \(x=1\) the loss gradient vanishes and \(F(1)=1/(1+\alpha\lambda)\). This formula also follows from elementary first-order optimality conditions for the displayed strongly convex model, so the calculation depends on the *actual* proximal subproblem rather than a heuristic stepsize convention.

For \(0\le x<1\), direct cancellation gives
\[
\frac{(1+\alpha\lambda)f(x)-\alpha\lambda(x-1)x}{(x-1)^2}
=\frac{1+\alpha\lambda}{2}+\frac{\alpha\lambda x}{1-x}>0.
\]
This uncapped proposal is strictly increasing. Under \(\alpha(1-3\lambda)>4\), one has \(0<c<1\) and the proposal first equals \(\alpha\) at the unique point \(x=c\). On \([0,c]\) the uncapped value yields \(F(x)=(1+x)/2\), whereas on \([c,1]\) the cap gives \(F(x)=[\alpha+(1-\alpha)x]/(1+\alpha\lambda)\). The two expressions agree at \(c\), by its defining equation. As \(\alpha>4>1\), the right branch is decreasing and its endpoint value is strictly positive, while the left branch is increasing and its values lie in \([1/2,1)\). Thus \(F([0,1])\subset(0,1)\) and the restriction is a continuous interval self-map.

**Exact three-cycle and itinerary.** Define \(D,x_0,x_1,x_2\) as above. Every denominator is positive and
\[
x_1-x_0=\frac{2\alpha\lambda}{D}>0,
\qquad
x_2-x_1=\frac{\alpha\lambda}{D}>0,
\qquad
1-x_2=\frac{\alpha\lambda}{D}>0.
\]
Algebraic reduction gives the two decisive strict branch comparisons
\[
c-x_1=\frac{2\alpha\lambda\,[\alpha(1-3\lambda)-4]}
{[\alpha(2+\lambda)-1]D}>0,
\qquad
x_2-c=\frac{7\alpha\lambda(1+\alpha\lambda)}
{[\alpha(2+\lambda)-1]D}>0.
\]
Hence \(x_0,x_1\) use the first branch and \(x_2\) the second. Direct substitution, with *no limiting argument*, yields
\[
\frac{1+x_0}{2}=x_1,
\qquad \frac{1+x_1}{2}=x_2,
\qquad \frac{\alpha+(1-\alpha)x_2}{1+\alpha\lambda}=x_0.
\]
As the three points are distinct, their least period is three. The three points lie strictly away from the kink, so the multiplier is the product of the constant branch slopes, namely \(\mu_3=(1/2)^2(1-\alpha)/(1+\alpha\lambda)\).

**Attraction criterion.** The threefold return map is affine on some neighborhood of \(x_0\) with slope \(\mu_3\), because the orbit's branch inequalities are strict. Hence \(|\mu_3|<1\) is equivalent to local asymptotic attraction; \(|\mu_3|>1\) yields local repulsion. Since \(\alpha>4\), the multiplier is negative, and the inequality \(|\mu_3|<1\) reduces to \(\alpha(1-4\lambda)<5\). At equality the return map is locally an orientation-reversing isometry, so no asymptotic attraction follows. For \(\alpha=5\) and \(\lambda=1/20\), exact substitution gives the displayed rational orbit, strict kink inequalities and multiplier \(-4/5\).

**All periods and Li–Yorke chaos.** The forward-invariant set \([0,1]\) is a compact real interval; its restriction of \(F\) is continuous. The exact orbit just established has *primitive* period three. The theorem of Li and Yorke, *Period Three Implies Chaos* (1975), therefore gives periodic points of every positive integer least period and an uncountable scrambled set in this same interval. This deduction uses a published theorem, not a finite numerical search; it applies to the interval restriction and consequently to the original real-line ProxSPS iteration.

## Verification
The accompanying standalone `verify.py` uses Python's exact `fractions.Fraction` arithmetic. It directly minimizes the original piecewise-quadratic strongly convex ProxSPS model by evaluating the two unconstrained quadratic vertices and the model kink; this is distinct from replaying the claimed closed form. Across 64 admissible rational parameter pairs it performed 10,112 exact proximal minimizations and matched the piecewise map, checked interval invariance, primitive period-three itineraries, multiplier criteria, and the rational witness. Symbolic factorization independently confirmed the branch-order identities and three point-to-point equalities. These calculations guard against algebra or transcription errors; the all-real-parameter theorem is established in the proof above, and the Li–Yorke conclusion is supplied by the cited classical theorem.

## Relationship to prior work
Schaipp, Gower, and Ulbrich (2023), arXiv:2301.04935, introduce precisely the truncated affine loss plus unchanged proximal regularizer and give the closed-form quadratic-regularizer update. Their principal convergence analyses use regulated stepsizes and do not assert convergence for arbitrary large constant \(\alpha\); the inspected Section 4 and appendices do not exhibit this period-three orbit or invoke Li–Yorke dynamics. Their method provides the essential starting point but not the periodic-orbit statement.

Loizou, Vaswani, Laradji, and Lacoste-Julien (2020/2021) and Orvieto, Lacoste-Julien, and Loizou (2022) study classical stochastic Polyak rules; those updates do not include the present *proximal* quadratic regularizer while truncating only the loss. Published exact finite-cycle observations for a loose-lower-bound SPS rule and for linearized trust-region methods concern distinct update maps, chiefly two-cycles; their statements do not imply the explicit ProxSPS three-cycle or all-period corollary. The period-three-to-chaos implication itself is **classical and not claimed as new**. The new mathematical component is the exact parameterized primitive period-three witness in the genuine ProxSPS map, including an open region of attraction.

## Limitations
The construction specializes to one loss term, a scalar quadratic, and a large constant model parameter. It does not estimate any prevalence of chaos among initial states or guarantee chaotic behavior under random sampling, time-varying parameters, smaller steps, or higher dimensions. The period-three point is explicit for the stated open parameter domain but no complete bifurcation diagram is claimed. A previously unindexed ProxSPS-specific period-three calculation or an equivalent conjugate interval-map result remains an originality risk; no exhaustive mathematical-literature uniqueness claim is made. The return-map attraction criterion is restricted to this one cycle and its local basin, not all trajectories.

## References
1. F. Schaipp, R. M. Gower, M. Ulbrich, *A Stochastic Proximal Polyak Step Size*, arXiv:2301.04935, version 1 first made public 2023-01-12; https://arxiv.org/abs/2301.04935 and https://arxiv.org/html/2301.04935v2. Definition (11), Lemma 1, Algorithm 3, Sections 4.1 and 4.3.
2. T.-Y. Li and J. A. Yorke, *Period Three Implies Chaos*, American Mathematical Monthly 82 (1975), 985–992, DOI:10.2307/2318254. Lawful original full text: https://sites.calvin.edu/tmk5/courses/mw81/I09/LiYorke.pdf.
3. N. Loizou, S. Vaswani, I. Hadj Laradji, S. Lacoste-Julien, *Stochastic Polyak Step-size for SGD: An Adaptive Learning Rate for Fast Convergence*, arXiv:2002.10542 (2020), AISTATS 2021. Distinct nonproximal method.
4. A. Orvieto, S. Lacoste-Julien, N. Loizou, *Dynamics of SGD with Stochastic Polyak Stepsizes: Truly Adaptive Variants and Convergence to Exact Solution*, arXiv:2205.04583 (2022). Distinct nonproximal dynamics.
