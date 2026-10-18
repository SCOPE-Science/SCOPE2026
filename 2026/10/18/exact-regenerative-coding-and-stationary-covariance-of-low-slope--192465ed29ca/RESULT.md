# Exact regenerative coding and stationary covariance of low-slope random interval maps

## Finding

Fix an arbitrary probability distribution \(p_\beta\) on the positive integers and independently select a fresh \(B_t\) with this distribution at each iteration of the interval map
\[
T_\beta(x)=\begin{cases}
2x,&0\le x\le\tfrac12,\\
2^{-\beta}(2x-1),&\tfrac12<x\le1.
\end{cases}
\]
Write \(Y=(1/2,1]\) and \(I_n=(2^{-(n+1)},2^{-n}]\) for integers \(n\ge0\). Equalities involving densities and return maps are understood modulo the countable endpoint set.

**Exact regenerative coding.** Starting with a uniformly distributed point in \(Y\), successive first-return durations to \(Y\) are independent and identically distributed, each with the law
\[
\tau\;\overset{d}{=}\; B+G+1,
\qquad \Pr(G=g)=2^{-(g+1)}\quad(g=0,1,2,\ldots),
\]
where \(B\) has law \(p_\beta\), \(G\) is independent of \(B\), and \(\tau\ge2\). Furthermore the location at each return is uniform on \(Y\), independently of all preceding return-duration labels. In particular, for \(|z|<1\),
\[
R(z):=\mathbb E z^\tau
=\frac{z}{2-z}\sum_{\beta\ge1}p_\beta z^\beta,
\qquad \mathbb E\tau=\mathbb EB+2\quad\text{(possibly infinite)}.
\]

**Exact invariant density and mass.** There is a conservative ergodic, Lebesgue-equivalent, annealed invariant measure \(\nu\), normalized by \(\nu(Y)=1\), with explicitly piecewise constant density
\[
\boxed{\;h(x)=2\,\mathbb E[2^{\min(n,B)}],\quad x\in I_n,\ n\ge0.\;}
\]
It has
\[
\boxed{\;\nu(I_n)=\mathbb E[2^{\min(n,B)-n}],\qquad
\nu((0,1])=\mathbb EB+2.\;}
\]
Consequently a Lebesgue-absolutely-continuous invariant probability measure on \((0,1]\) exists exactly when \(\mathbb EB<\infty\), and is uniquely given by \(\pi=\nu/(\mathbb EB+2)\). In the infinite-mean case \(\nu\) is \(\sigma\)-finite and infinite; atomic invariant measures supported at the fixed point \(0\) are not ruled out by this statement.

**Complete stationary return-observable covariance.** If \(m:=\mathbb EB+2<\infty\), let \(X_t\) have stationary annealed law \(\pi\), put \(J_t=\mathbf1_{\{X_t\in Y\}}\), and let \(c_n=\operatorname{Cov}(J_0,J_n)\). Then
\[
\boxed{\;\sum_{n\ge0}c_nz^n
=\frac{1}{m(1-R(z))}-\frac{1}{m^2(1-z)},\quad |z|<1.\;}
\]
Thus the entire two-time return-observation law is explicit for every choice of \(p_\beta\), including unbounded distributions with finite mean. For the deterministic distribution \(p_1=1\), this specializes to
\[
\boxed{\;c_n=\tfrac29(-\tfrac12)^n\quad(n\ge0),\;}
\]
showing exact alternating return correlations.

## Assumptions and scope

The random parameters are independent over time and independent of the initial coordinate. Their law can have infinite support and infinite mean, but each selected parameter is finite almost surely. All statements concern **annealed** dynamics (the Markov transition kernel or its i.i.d.-environment extension), not a common quenched invariant density for each environment. Points on the partition boundaries form a null set for the absolutely continuous measures considered. The fixed point at zero is outside \((0,1]\) and is not part of the Lebesgue-equivalent invariant component. The stationary covariance formula requires \(\mathbb EB<\infty\); only the induced return law and the \(\sigma\)-finite invariant measure are asserted at infinite mean.

## Proof

**1. Return branches and the iid excursion law.** Write \(u=2x-1\in(0,1]\) for \(x\in Y\). For each integer \(g\ge0\), define
\[
K_g=\left(\frac{1+2^{-(g+1)}}2,\frac{1+2^{-g}}2\right]\subset Y.
\]
These intervals partition \(Y\) modulo endpoints, and \(|K_g|/|Y|=2^{-(g+1)}\). For \(x\in K_g\), the first right-branch iterate is \(2^{-\beta}u\in I_{\beta+g}\). Exactly \(\beta+g\) subsequent applications of the common left branch \(x\mapsto2x\) take the orbit back to \(Y\). Therefore its first-return duration is \(\beta+g+1\), and its return location is
\[
\mathcal R_g(x)=2^g(2x-1)\in Y.
\]
This affine map takes \(K_g\) bijectively onto \(Y\) with derivative \(2^{g+1}\), **independently of** \(\beta\). If the entering coordinate is uniform on \(Y\), then \(G=g\) has probability \(2^{-(g+1)}\) and, conditional on \(G=g\) and any \(\beta\), the return coordinate is uniform on \(Y\). Since the environment choice at every visit to \(Y\) is independent of the past, the pair of labels \((B,G)\) at each successive visit has the same product law and is independent of all past visit labels. Induction establishes the iid durations and the conditional-uniform return claim. Summing \(\mathbb E z^{B+G+1}\) gives the stated probability-generating function; \(\mathbb EG=1\) gives the mean \(\mathbb E B+2\).

**2. Invariant measure by an exact transfer calculation.** Set
\[
h_n=2\sum_{\beta\ge1}p_\beta 2^{\min(n,\beta)}
\quad\text{for each integer }n\ge0.
\]
This is finite and positive for every fixed \(n\), and \(h_0=2\), so its associated measure has \(\nu(Y)=h_0|I_0|=1\). The annealed transfer operator sends density \(h\) on \(I_{n+1}\) to density \(h_{n+1}/2\) on \(I_n\) under the common left branch. The right branch with index \(\beta\) covers \(I_n\) precisely when \(\beta\le n\), and its inverse Jacobian is \(2^{\beta-1}\). Its contribution from \(Y\) is consequently \(h_0\sum_{\beta\le n}p_\beta 2^{\beta-1}=\sum_{\beta\le n}p_\beta2^\beta\). The elementary identity
\[
2\cdot2^{\min(n,\beta)}-2^{\min(n+1,\beta)}
=2^\beta\mathbf1_{\{\beta\le n\}}
\]
proves \(h_n=h_{n+1}/2+\sum_{\beta\le n}p_\beta2^\beta\). Hence the density is invariant on every shell.

Integrating gives \(\nu(I_n)=2^{-(n+1)}h_n\). For each fixed positive integer \(\beta\), Tonelli's theorem gives
\[
\sum_{n\ge0}2^{\min(n,\beta)-n}
=\sum_{n<\beta}1+\sum_{n\ge\beta}2^{\beta-n}
=\beta+2.
\]
Averaging proves \(\nu((0,1])=\mathbb EB+2\), without requiring the mean to be finite.

The induced return coordinate map \(\mathcal R\) has full branches \(K_g\) with zero distortion and relative branch sizes \(2^{-(g+1)}\); under uniform measure the branch itinerary is an independent sequence and generates the Borel \(\sigma\)-algebra modulo null sets because inverse-branch lengths shrink exponentially. It is therefore ergodic and conservative. The standard first-return tower whose levels have lengths \(\tau\) lifts this induced invariant probability to the displayed \(\sigma\)-finite conservative ergodic measure \(\nu\). An invariant probability absolutely continuous with respect to Lebesgue would induce an absolutely continuous invariant probability on \(Y\); the full-branch return map has the unique such measure, namely normalized Lebesgue on \(Y\). The return tower then forces its total mass to be \(\mathbb E\tau\). Hence finiteness and uniqueness follow exactly as asserted.

**3. Stationary return covariance.** Assume \(m=\mathbb E\tau<\infty\). The stationary probability of observing \(Y\) is \(\pi(Y)=1/m\). Conditioned on \(J_0=1\), the successive future return gaps are iid with the preceding law. Define \(u_0=1\) and \(u_n=\Pr(J_n=1\mid J_0=1)\). The renewal equation \(u_n=\sum_{j=1}^n\Pr(\tau=j)u_{n-j}\) gives \(\sum_{n\ge0}u_nz^n=1/(1-R(z))\) on \(|z|<1\). Thus \(\mathbb E[J_0J_n]=u_n/m\) and \(c_n=u_n/m-1/m^2\), proving the generating function. When \(p_1=1\), \(R(z)=z^2/(2-z)\) and
\[
\frac1{1-R(z)}
=\frac{2-z}{(1-z)(2+z)}
=\frac{1}{3(1-z)}+\frac{4}{3(2+z)}.
\]
Its coefficient at \(z^n\) is \(1/3+(2/3)(-1/2)^n\), and the stated covariance follows.

## Verification

A standalone standard-library Python file, `verification.py`, performs exact-rational checks for four distinct finitely supported parameter laws. It checks each displayed shell transfer recurrence, exact total mass including the infinite dyadic tail, 20 return-distribution coefficients per law, the first 20 renewal coefficients per law, geometric branch lengths and affine-Jacobian identities, and all first 30 deterministic-parameter covariance coefficients. It produced `PASS: 512 exact-rational checks`. These are finite algebraic diagnostics, **not** proofs for arbitrary unbounded parameter laws; the proof above supplies the unrestricted arguments. To reproduce: run `python verification.py` with Python 3 and no extra dependencies.

## Relationship to prior work

Inoue and Toyokawa, *Invariant measures for random piecewise convex maps* (arXiv:2303.10873, first posted 2023-03-20), define precisely this family in Example 4.1 and prove the existence of a Lebesgue-equivalent conservative ergodic \(\sigma\)-finite invariant measure. Their Proposition 4.1 gives **two-sided order comparisons** for the masses of dyadic shells, with the same combination of truncated weighted probabilities occurring here. Such comparisons already yield useful finiteness conclusions; existence and the broad finiteness mechanism are **not** claimed as discoveries here. The contribution is the exact normalized shell-density identity, the iid excursion coding with arbitrary parameter law, and the resulting full stationary covariance generating function, none of which is stated in the inspected Example 4.1 or its proofs.

Inoue, *First return maps of random maps and invariant measures* (2019/2020), gives a general inducing framework, which is acknowledged rather than claimed as new. Kalle and Maggioni, *Invariant densities for random systems of the interval* (arXiv:1805.11430), provide exact density methods under expansion-on-average assumptions; their condition \(\sum_\beta p_\beta/|T_\beta'(x)|<1\) fails on \(Y\) here because it becomes \(\sum_\beta p_\beta2^{\beta-1}\ge1\). Neither general inducing theory nor general renewal theory is asserted to be original. The exact full-branch reduction for the specific model is the new substantive statement.

## Limitations

The assertion is annealed, not a quenched theorem. Return durations are iid only when the initial coordinate at a return is Lebesgue-uniform on \(Y\), equivalently under the induced invariant distribution; no such iid assertion is made for an arbitrary deterministic initial point. The invariant measure may be infinite, in which case stationary probability covariances on the full interval are not defined. No spectral-gap bound, central limit theorem, mixing-rate theorem, or conclusion about all other invariant (possibly singular) probabilities is proved. The general framework and comparable shell-mass asymptotics predate this calculation; a historically earlier unindexed explicit return-law calculation remains possible.

## References

1. T. Inoue and H. Toyokawa, *Invariant measures for random piecewise convex maps*, arXiv:2303.10873, first released 2023-03-20, particularly Section 4.1 and Proposition 4.1. https://arxiv.org/abs/2303.10873
2. T. Inoue, *First return maps of random maps and invariant measures*, *Nonlinearity* **33** (2020), 249–275; first published 2019-11-22. DOI:10.1088/1361-6544/ab4c83.
3. C. Kalle and M. Maggioni, *Invariant densities for random systems of the interval*, arXiv:1805.11430, first released 2018-05-29; see Section 2, assumption (A2). https://arxiv.org/abs/1805.11430
