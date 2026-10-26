# Three radial destinations suffice for three extrema of commuting-distance variance

## Finding
Consider the finite-system, origin-conditioned radiation model for destinations ordered by strictly increasing travel distance. In a three-destination instance with positive opportunity masses \((1,100,100)\), equally spaced distance indices \((1,2,3)\), and a variable origin population \(m>0\), the conditional trip-distance variance has **exactly three** positive critical points: two strict local maxima separated by a strict local minimum, despite the whole distance distribution shifting strictly outward in first-order stochastic order as \(m\) increases.

Specifically, with \(J\) the realized destination distance, the variance is
\[
V(m)=\operatorname{Var}(J)=\frac{500m(m+201)(21m^2+162m+4141)}{40401(m+1)^2(m+101)^2},
\]
and its derivative factors as
\[
V'(m)=-\frac{500(m^2-3858m+4141)(99m^2-202m-20301)}{40401(m+1)^3(m+101)^3}.
\]
Thus its three positive stationary populations are approximately \(1.073652859114\), \(15.376434751063\), and \(3856.92634714089\), with successive types maximum, minimum, maximum. Among radiation destination systems with distinct distances and positive destination opportunity masses, three destinations are **minimal** for this phenomenon: any two-destination system has at most one positive stationary point of its distance variance.

## Assumptions and scope
Let \(r\ge2\) destination regions have strictly ordered travel distances \(d_1<\cdots<d_r\) and positive opportunity masses \(n_i>0\). Their intervening opportunities are \(s_i=\sum_{j<i}n_j\), with \(S=\sum_{j=1}^r n_j\). In the finite-normalized radiation law, conditioned on a trip being allocated among these destinations, the probability of destination \(i\) is
\[
p_i(m)=\frac{m(m+S)n_i}{S(m+s_i)(m+s_i+n_i)},\qquad m>0.
\]
The example takes \(r=3\), \((n_1,n_2,n_3)=(1,100,100)\), \((d_1,d_2,d_3)=(1,2,3)\), and \(S=201\). Distances may be interpreted as equally spaced radial destination bins; no physical unit, unobserved urban geography, or empirical fit is asserted. All results are algebraic consequences of this deterministic probability family.

## Proof
**Normalization and outward stochastic order.** The identity
\[
\frac{n_i}{(m+s_i)(m+s_i+n_i)}=\frac1{m+s_i}-\frac1{m+s_i+n_i}
\]
telescopes to \(\sum_{i=1}^rp_i=1\). For every cutoff \(j\in\{2,\ldots,r\}\),
\[
\Pr_m\{J\ge d_j\}=\sum_{i=j}^rp_i(m)=\frac{m(S-s_j)}{S(m+s_j)}.
\]
Its derivative is \((S-s_j)s_j/[S(m+s_j)^2]>0\), because \(0<s_j<S\). This proves strict first-order stochastic increase of destination distance with origin population.

**Exact three-destination classification.** Substituting the chosen masses yields
\[
p_1=\frac{m+201}{201(m+1)},\quad p_2=\frac{100m(m+201)}{201(m+1)(m+101)},\quad p_3=\frac{100m}{201(m+101)}.
\]
The mean and second moment are \(\mu=p_1+2p_2+3p_3\) and \(M_2=p_1+4p_2+9p_3\). Expanding \(M_2-\mu^2\), collecting rational terms, and differentiating yields exactly the factorizations in the Finding. Denominators are positive for all \(m>0\). The quadratic \(A(m)=m^2-3858m+4141\) has two positive roots: one in \((1,2)\) because \(A(1)>0>A(2)\), and one in \((20,3858)\) because \(A(20)<0<A(3858)\). Since \(A\) is monic quadratic these are its only roots. The quadratic \(B(m)=99m^2-202m-20301\) has exactly one positive root (its constant coefficient is negative), in \((2,20)\) because \(B(2)<0<B(20)\). Consequently the derivative's sign on the four positive intervals is successively \(+,-,+,-\). Every stationary point is simple, so the three extrema are strict and their types are as claimed.

**Sharp number of destinations.** If \(r=2\), write \(p(m)=p_2(m)=m n_2/[S(m+n_1)]\). Since \(p'(m)=n_1n_2/[S(m+n_1)^2]>0\), for any \(d_1<d_2\) one has
\[
\operatorname{Var}_m(J)=(d_2-d_1)^2p(m)(1-p(m)),\quad
\frac{d}{dm}\operatorname{Var}_m(J)=(d_2-d_1)^2p'(m)(1-2p(m)).
\]
The strictly increasing function \(p(m)\) crosses \(1/2\) at most once; hence this variance has at most one positive stationary point. If \(r=1\), variance is identically zero and has no strict local extrema. The three-destination construction is therefore minimal for three strict positive local extrema.

## Verification
Run the embedded `check.py` after installing the standalone dependency in `requirements.txt` (SymPy). It reproduces the normalization, moments, exact rational derivative factorization, root intervals and signs, and the two-destination structural identities from the formulas in this document. Exact symbolic identities, rather than a finite sampling grid, certify the rational calculation; the derivative sign and root-count argument supplies the all-positive-parameter proof for this instance. The decimal roots are supplementary approximations, not certificates.

## Relationship to prior work
Simini and collaborators introduced the radiation mobility law (arXiv:1111.0586v1, publicly posted 2011-11-02). Masucci and collaborators described the finite-size normalization of radiation flows (arXiv:1206.5735v1, publicly posted 2012-06-25). Those laws and the existence of nontrivial destination probabilities are **prior work**; only the three-extrema variance phenomenon, its exact instance and minimal destination count are proposed here. In Simini and colleagues' supplemental calculations, variance concerns counts on given commuter flows rather than the variance of distances across destination categories. Other published work on fixed finite-distribution variance bounds does not itself classify the origin-population trajectory under these specific rational probabilities. Nonetheless, an undiscovered general variance-curve or mixture theorem could subsume this special construction; historical priority requires wider expert verification.

## Limitations
This is a precise counterexample and a sharp minimal-destination obstruction, **not** a classification of all three-destination mass and distance configurations. It studies conditional allocations to a finite set, not absolute commuting volumes, individual-level causal behavior, geography-dependent destination choice, or measurement noise. Increasing travel distance in stochastic order does not mean its variance increases monotonically. No empirical occurrence or universality of the specific opportunity ratio is claimed. Independent validation has not been performed.

## References
1. F. Simini, M. C. González, A. Maritan, A.-L. Barabási, *A universal model for mobility and migration patterns*, arXiv:1111.0586v1 (2011-11-02), https://arxiv.org/abs/1111.0586.
2. A. P. Masucci, J. Serras, A. Johansson, M. Batty, *Gravity vs Radiation Models: On the Importance of Scale and Heterogeneity in Commuting Flows*, arXiv:1206.5735v1 (2012-06-25), https://arxiv.org/abs/1206.5735.
