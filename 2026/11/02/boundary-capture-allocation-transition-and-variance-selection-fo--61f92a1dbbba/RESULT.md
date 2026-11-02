# Boundary-capture allocation transition and variance selection for a persistent particle

## Finding

Consider a one-dimensional velocity-jump particle in the interval \([-h,h]\), where \(h,v>0\). The velocity is \(+v\) or \(-v\) and reverses at Poisson rate \(\rho\ge0\). The particle starts at the midpoint, with either velocity equally likely. On reaching an endpoint, it is independently absorbed with probability \(q_-\) at the left end or \(q_+\) at the right end; otherwise, its velocity immediately reverses without a holding time. The capture budget is the *sum of per-collision absorption probabilities* \(q_-+q_+=Q\), fixed with \(0<Q\le2\), and \(0\le q_-,q_+\le1\). Let \(T\) be the time of eventual absorption.

Write \(\xi=\rho h/v\) and \(P=q_-q_+\). The exact mean is
\[
\frac{v\mathbb E T}{h}=F_{\xi,Q}(P):=\frac{P(2\xi^2-3\xi+1)+Q(3\xi-2)+4}{Q+(2\xi-1)P}.
\]
For every \(0<Q<2\), the complete optimal-allocation phase diagram is:

* If \(0\le\xi<1/2\), the *only* mean-minimizing allocations, up to exchanging endpoints, are \(\{q_-,q_+\}=\{Q,0\}\) for \(0<Q\le1\), or \(\{1,Q-1\}\) for \(1\le Q<2\). These are maximally unequal.
* If \(\xi>1/2\), the *unique* mean-minimizing allocation is \(q_-=q_+=Q/2\).
* At the exact threshold \(\xi=1/2\), **every** feasible allocation has the same mean,
\[
\mathbb E T=\frac{h}{v}\frac{8-Q}{2Q}.
\]
  Yet the variance singles out the maximally unequal allocations: exactly at this threshold,
\[
\frac{v^2}{h^2}\operatorname{Var}(T)=\frac{96-32Q-11Q^2+32P}{6Q^2}.
\]
  Hence the variance is strictly increasing in \(P\), so its minimum among the mean-optimal allocations is attained only at maximal inequality (up to exchange). The equal split incurs the *exact* variance penalty
\[
\operatorname{Var}_{\mathrm{equal}}(T)-\operatorname{Var}_{\mathrm{unequal}}(T)=\frac{h^2}{v^2}
\begin{cases}
4/3,&0<Q\le1,\\
4(2-Q)^2/(3Q^2),&1\le Q<2.
\end{cases}
\]
When \(Q=2\), both endpoints are necessarily perfectly absorbing, so the feasible allocation is unique at every \(\xi\). The critical reversal rate is \(\rho_c=v/(2h)\), equivalently the mean ballistic run length \(v/\rho_c\) equals the full corridor length \(2h\).

## Assumptions and scope

The process is a piecewise-deterministic Markov process with constant speed, independent exponential velocity reversals, and instantaneous independent Bernoulli capture at each endpoint collision. Absorption at a collision has zero extra time; reflection reverses velocity instantaneously. The initial position is exactly the midpoint and initial velocity is unbiased. The objective is the *unconditional mean eventual absorption time*, not finite-time capture probability, and the budget is \(q_-+q_+\), not a sum of Robin reactivities or chemical free energies. Perfectly reflecting endpoints (capture probability zero) are permitted, but not simultaneously since \(Q>0\).

## Proof

Scale position as \(y=x/h\in[-1,1]\) and time as \(s=vt/h\). Let \(M_n^{\pm}(y)\) be the \(n\)-th moment of the scaled absorption time starting with velocity sign \(\pm\), and set \(M_0^{\pm}=1\). The backward generator gives, for \(n\ge1\),
\[
\pm\frac{dM_n^\pm}{dy}+\xi(M_n^\mp-M_n^\pm)=-nM_{n-1}^\pm.
\]
The collision rules imply
\[
M_n^-(-1)=(1-q_-)M_n^+(-1),\qquad
M_n^+(1)=(1-q_+)M_n^-(1).
\]
With \(S_n=(M_n^++M_n^-)/2\) and \(H_n=(M_n^+-M_n^-)/2\), adding/subtracting the equations yields
\[
H_n'=-nS_{n-1},\qquad S_n'=2\xi H_n-nH_{n-1},\qquad S_0=1,\quad H_0=0.
\]
For \(n=1\), the general polynomial solution is \(H_1(y)=c-y\) and \(S_1(y)=k+2\xi cy-\xi y^2\). Solving the two collision boundary conditions uniquely determines \(k=F_{\xi,Q}(P)\); this is the unbiased initial mean. The denominator is positive because \(Q+(2\xi-1)P\ge Q-P=1-(1-q_-)(1-q_+)>0\) whenever \(2\xi-1<0\), and is evidently positive otherwise.

At fixed \(Q\), only the product \(P\) changes. Direct differentiation gives the *strict global sign identity*
\[
\frac{\partial F_{\xi,Q}}{\partial P}=
\frac{(1-2\xi)(4-Q+2Q\xi)}{[Q+(2\xi-1)P]^2}.
\]
Since \(4-Q+2Q\xi>0\), the derivative has the sign of \(1-2\xi\). The feasible product interval is
\[
\max\{0,Q-1\}\le P\le Q^2/4.
\]
Its lower endpoint is attained only by the maximally unequal allocations and its upper endpoint only by equal capture probabilities. This proves all mean-optimal cases, including the exact full degeneracy at \(\xi=1/2\).

For the second moment, set \(\xi=1/2\) in the same backward recurrence. In this case the first-moment solution has \(c=(q_- -q_+)/Q\) and \(k=(8-Q)/(2Q)\), so \(H_1(y)=c-y\) and \(S_1(y)=k+cy-y^2/2\). Integrating \(H_2'=-2S_1\) and \(S_2'=H_2-2H_1\) gives cubic and quartic polynomials with two integration constants. The same boundary equations fix their midpoint value exactly:
\[
S_2(0)=\frac{384-112Q-19Q^2+64P}{12Q^2}.
\]
Thus \(\operatorname{Var}(vT/h)=S_2(0)-k^2=(96-32Q-11Q^2+32P)/(6Q^2)\). This is affine and strictly increasing in \(P\). Subtracting its values at \(P=Q^2/4\) and \(P=\max\{0,Q-1\}\) gives the asserted sharp variance penalties. All formulas extend continuously to the allowable zero-capture boundary and to \(\rho=0\); at least one positive capture probability guarantees eventual absorption with finite moments in a finite corridor.

## Verification

Run `python check.py` with Python 3 and SymPy installed (the checker otherwise uses Python standard libraries). It verifies the first- and second-moment differential and collision equations symbolically, the fixed-budget derivative identity, exact critical-variance formula, the symmetric-boundary second-moment identity, and agreement of the mean with the published telegraph-expression after translating its absorption parametrization. It also performs 84,000 seeded event-driven trajectories over six parameter configurations, and 1,008 allocation comparisons. Numerical tests are finite diagnostics, not a substitute for the all-parameter proof above.

## Relationship to prior work

Angelani (2016, arXiv:1601.04845, originally posted January 19, 2016) gives the Laplace transform and general mean absorption time for a run-and-tumble particle between partially reflecting boundaries; in that convention the particle changes velocity sign at rate \(\alpha/2\) and the boundary parameter is \(\epsilon=q/(2-q)\). Equations (36), (55), and (67) supply independent comparisons for the present moments. The known transform is strictly broader as a distributional description and makes the moments calculable. The distinct question solved here is the *complete constrained boundary-allocation optimum at fixed sum of per-collision capture probabilities*, including the critical flat-mean set and its exact variance-based selection. The source does not state or analyze that optimization. An equivalent constrained-optimization result elsewhere cannot be ruled out.

Bressloff (2023, arXiv:2302.01158) studies encounter-based absorption, including sticky walls and distinct end reactivities. Sticky wall residence dynamics differs from instantaneous reversal at unsuccessful encounters, and the inspected relevant discussion does not establish this fixed-sum per-collision allocation phase diagram. Earlier partly reflecting telegraph boundary work by Masoliver, Porrà and Weiss (1993) is an additional historical-priority risk. An accessible author-uploaded text was inspected for its one-sided partially absorbing boundary model; no full-text mathematical equivalence assessment is claimed for portions that were not reliably rendered.

## Limitations

The budget \(Q\) is a modeling choice: replacing the sum of per-collision probabilities by a different chemical cost can change the optimizer. Initial displacement, directional bias, non-Poisson tumbles, sticky-wall residence, boundary memory, or spatially varying propulsion are outside the claim. The phase diagram concerns the expectation, and the second-moment statement only concerns its exactly degenerate threshold. Historical priority remains uncertain despite targeted comparisons, and independent validation has not been performed.

## References

1. L. Angelani, *Run-and-tumble particles, telegrapher's equation and absorption problems with partially reflecting boundaries*, arXiv:1601.04845 (first submitted 2016-01-19), https://arxiv.org/abs/1601.04845.
2. P. C. Bressloff, *Encounter-based model of a run-and-tumble particle II: absorption at sticky boundaries*, arXiv:2302.01158 (2023), https://arxiv.org/abs/2302.01158.
3. J. Masoliver, J. M. Porrà, and G. H. Weiss, *Solution to the telegrapher's equation in the presence of reflecting and partly reflecting boundaries*, Physical Review E 48, 939–944 (1993), https://doi.org/10.1103/PhysRevE.48.939. Historical comparison: accessible author-uploaded text of its single partly reflecting boundary treatment examined, with rendering limitations.
