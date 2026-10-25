# Exact basin separation and nonoscillatory convergence for probability-admissible higher-order SIS maps

## Finding
For every integer \(m\ge1\), let
\[
 F(x)=(1-\delta)x+(1-x)P(x),\qquad P(x)=\sum_{j=1}^{m}b_jx^j.
\]
Under the separate, probability-admissible conditions \(0<\delta\le1\), \(b_j\ge0\), \(\sum_j b_j\le1\), every orbit \(x_{t+1}=F(x_t)\) with \(x_0\in[0,1]\) converges to a fixed point. More precisely, **every fixed point divides the interval into forward-invariant sides**. In every open gap between consecutive fixed points the orbit is monotone in time and converges to the endpoint selected by the sign of \(F(x)-x\). This excludes every nonconstant periodic orbit and every nonconvergent orbit without requiring that \(F\) itself be monotone.

Nonzero fixed points are exactly the roots in \((0,1)\) of
\[
 (1-x)G(x)=\delta,\qquad G(x)=\sum_{j=1}^{m}b_jx^{j-1}.
\]
There are at most \(m\) such roots, counting distinct positive equilibria. The endpoints \(0\) and \(1\) are treated explicitly: \(0\) is always fixed and \(F(1)=1-\delta<1\).

For the admissible three-body instance
\[
 \delta=\frac15,\quad b_1=\frac1{20},\quad b_2=\frac{19}{20},
 \qquad r_{\pm}=\frac{9\pm2\sqrt6}{19},
\]
there are exactly three equilibria \(0,r_-,r_+\), and the **exact complete basins** are \([0,r_-)\to0\), \(\{r_-\}\to r_-\), and \((r_-,1]\to r_+\). Here \(F'(1)=-1/5\), demonstrating that the result extends beyond monotone one-step maps.

## Assumptions and scope
The variable \(x_t\) is a homogeneous deterministic mean-field infected fraction, not a sample path of a finite-state stochastic epidemic. The synchronous discrete recurrence is the spatially uniform restriction of a higher-order SIS Euler update. The effective coefficients \(\delta\) and \(b_j\) include the sampling step, and need not sum together to at most one: only \(0<\delta\le1\) and \(\sum_j b_j\le1\) separately are assumed. The infection incidence has no spontaneous constant term and is nonnegative and polynomial in prevalence. Every statement quantifies over all admissible coefficients, all integers \(m\ge1\), and all \(x_0\in[0,1]\).

## Proof
**Invariant interval.** Since \(0\le P(x)\le\sum_jb_j\le1\) and \(0\le1-\delta\le1\) for \(0\le x\le1\),
\[
 0\le F(x)=x(1-\delta)+(1-x)P(x)\le x+(1-x)=1.
\]
Also \(F(x)-x=x[(1-x)G(x)-\delta]\). Therefore the positive fixed points are the roots of \((1-x)G(x)=\delta\). This polynomial is not identically zero: its value at \(x=1\) is \(-\delta\). Consequently there are finitely many roots; its degree is at most \(m\). Neither \(x=1\) nor any negative coordinate is a permitted nonzero equilibrium.

**Equilibrium barrier lemma.** Let \(r\in(0,1)\) be any fixed point. The equilibrium equation gives \(\delta=(1-r)G(r)\), \(P(r)=rG(r)\), and hence
\[
 1-\delta-P(r)=1-G(r)\ge0.
\]
The last inequality uses \(G(r)=\sum_j b_jr^{j-1}\le\sum_jb_j\le1\). The polynomial \(P\) is nondecreasing on \([0,1]\). For \(x\ge r\),
\[
 \begin{aligned}
 F(x)-r
 &=(1-\delta)(x-r)+(1-x)P(x)-(1-r)P(r)\\
 &\ge(x-r)(1-\delta-P(r))=(x-r)[1-G(r)]\ge0.
 \end{aligned}
\]
For \(x\le r\), replacing \(P(x)\) by the larger \(P(r)\) reverses the bound:
\[
 F(x)-r\le(x-r)[1-G(r)]\le0.
\]
Thus neither side of any positive equilibrium can be crossed in one step. The disease-free equilibrium also bounds every trajectory from below because \(F\ge0\).

**Global convergence and complete basin rule.** List the distinct fixed points as \(0=r_0<r_1<\cdots<r_k<1\). Each closed interval \([r_j,r_{j+1}]\) is invariant under \(F\), as is \([r_k,1]\); if \(k=0\), the entire interval is the rightmost interval. On each corresponding open gap, \(F(x)-x\) has constant nonzero sign by continuity and absence of additional roots. Consequently an orbit in the gap is either nondecreasing and bounded above by the right endpoint, or nonincreasing and bounded below by the left endpoint. Its limit exists, and continuity makes that limit a fixed point, necessarily the corresponding endpoint. On \((r_k,1]\), the sign is negative, since \(F(1)-1=-\delta<0\). An initial fixed point stays fixed. These arguments cover all initial conditions including \(x_0=0,1\), and prove exact basin assignment by evaluating the drift sign once in each gap. They also exclude nontrivial periodic or nonconvergent trajectories.

**Nonmonotone, bistable example.** With the parameters in the finding, direct factorization gives
\[
 F(x)-x=-\frac{x}{20}(19x^2-18x+3),
\]
with positive roots \(r_\pm=(9\pm2\sqrt6)/19\). This drift is negative below \(r_-\), positive between the roots and negative above \(r_+\). The general barrier-and-convergence theorem gives the asserted exact basins. Differentiation yields \(F'(1)=-1/5\), so the map is not increasing; moreover \(F'(0)=17/20\), and the nonzero multipliers are \(F'(r_-)= (83+9\sqrt6)/95>1\) and \(F'(r_+)=(83-9\sqrt6)/95\in(0,1)\).

**Why the probability constraint matters.** Outside the theorem's admissible infection range, take \(\delta=1\), \(P(x)=(16/5)x\). Although \(F(x)=(16/5)x(1-x)\) still maps \([0,1]\) into itself, it has the distinct exact period-two points
\[
 u=\frac{21-\sqrt{21}}{32},\qquad v=\frac{21+\sqrt{21}}{32},
 \qquad F(u)=v,\quad F(v)=u,
\]
whose two-step multiplier is \(F'(u)F'(v)=4/25\). The coefficient \(b_1=16/5>1\) violates the separate infection-probability condition. This is a boundary comparison, not a prediction of epidemic oscillations within the admissible model.

## Verification
The included standalone `verify.py` carries out exact symbolic checks of the bistable factorization, both irrational fixed-point identities, multipliers, and the inadmissible comparison two-cycle; it also checks interval preservation over a deterministic rational grid of admissible parameter tuples. Run `python verify.py` with Python 3 and SymPy installed. The arbitrary-order convergence theorem is established by the barrier proof above, not by the finite computations.

## Relationship to prior work
Liang, Cui and Liu [1] derive synchronous higher-order SIS updates for hypergraphs, distinguish a separate physical interval-preserving constraint (Assumption 3a) from a stronger small-step constraint (Assumption 3b), and provide sufficient local/global stability and basin results in Propositions 1–3 and 8–10 and Theorems 1–6. The present claim concerns the homogeneous invariant subspace and supplies an unconditional complete basin partition for *all* effective coefficient choices under the weaker separate constraints, even when the scalar map is nonmonotone. No such general homogeneous barrier-and-global-convergence statement was located in the portions of [1] examined. It is not a claim about their full heterogeneous network model.

Schreiber, Huang, Jiang and Wang [2] analyze a discrete SIS map with exponential single-contact infection probability and a unique endemic equilibrium; their Theorem 2.1 does not imply a complete multistable basin classification for arbitrary nonnegative higher-order polynomial incidence. Azizan Ruhi, Ahn and Hassibi [3] establish global pairwise-network SIS results with a unique endemic state, rather than arbitrary-order coexistence under the separate physical coefficient bounds. These distinctions concern equations and implications, not merely titles.

## Limitations
Only deterministic homogeneous one-dimensional dynamics are treated. No claim is made that a spatially heterogeneous hypergraph network, a finite stochastic SIS epidemic, or a model with exogenous spontaneous infection has the same basin structure. The coefficient bounds are sufficient and physical; the logistic comparison shows that interval invariance alone is insufficient, but does not assert necessity of each individual bound. The theorem proves convergence without universal rates, and does not identify the precise location of all roots for arbitrary coefficient vectors. Publication-priority uncertainty remains, and no independent scientific review has been performed.

## References
[1] L. Liang, S. Cui, F. Liu, *Discrete-time SIS Social Contagion Processes on Hypergraphs*, arXiv:2408.08602v1 (first public version 2024-08-16), esp. model (5)/(17), Assumption 3, Propositions 1–3, 8–10 and Theorems 1–6. https://arxiv.org/pdf/2408.08602

[2] S. J. Schreiber, S. Huang, J. Jiang, H. Wang, *Extinction and quasi-stationarity for discrete-time, endemic SIS and SIR models*, arXiv:2005.08312v1 (2020), Theorem 2.1. https://arxiv.org/pdf/2005.08312

[3] N. Azizan Ruhi, H. J. Ahn, B. Hassibi, *Analysis of Exact and Approximated Epidemic Models over Complex Networks*, arXiv:1609.09565v1 (2016), Sections 1–2. https://arxiv.org/pdf/1609.09565
