# Exact schedule risk and optimal contact order on two-hub epidemic trees

## Finding

Consider the double-star tree \(D_{a,b}\) formed from two adjacent hubs, with \(a\ge1\) leaves incident to the left hub and \(b\ge1\) leaves incident to the right hub. There are \(n=a+b+2\) vertices. Give every edge exactly one contact time, all times distinct. Initially one uniformly random vertex is infectious, all other vertices are susceptible, no infection recovers, and each contact across an infectious--susceptible edge transmits independently with probability \(q\in(0,1]\). Write \(Z\) for the number ever infected after the last contact and \(R(\pi)=\mathbb E[Z\mid\pi]\) for its conditional mean given a fixed edge-contact order \(\pi\).

Let \(x\) of the \(a\) left leaf contacts and \(y\) of the \(b\) right leaf contacts occur *before* the hub--hub contact. Put
\[
M_{a,b}(x,y)=x(b-y)+(a-x)y,
\qquad
C_{a,b}(q)=1+\frac{2(a+b+1)}{n}q+
\frac{\binom a2+\binom b2+a+b}{n}q^2.
\]
**The exact schedule response and its full optimality law are**
\[
\boxed{R(\pi)=C_{a,b}(q)+\frac{q^3}{n}M_{a,b}(x,y).}
\]
Consequently \(C_{a,b}(q)\le R(\pi)\le C_{a,b}(q)+abq^3/n\). Equality on the lower side occurs **if and only if** the hub--hub contact is first or last. Equality on the upper side occurs **if and only if** all left leaf contacts precede the hub--hub contact and all right contacts follow it, or vice versa (orders internal to either leaf class are unrestricted). The maximum-minus-minimum outbreak expectation is exactly \(abq^3/n\).

If all \((a+b+1)!\) edge orders are equiprobable, then, for \(0\le x\le a\), \(0\le y\le b\),
\[
\boxed{\mathbb P(X=x,Y=y)=
\frac{\binom ax\binom by(x+y)!(a+b-x-y)!}{(a+b+1)!}.}
\]
Together with the formula for \(M_{a,b}\), this is the **entire discrete probability law** of the calendar-dependent mean outbreak \(R(\pi)\); different pairs \((x,y)\) can give the same value and their probabilities must then be added. Its first two moments are
\[
\boxed{\mathbb E_{\pi}R(\pi)=C_{a,b}(q)+\frac{abq^3}{3n},}
\]
\[
\boxed{\operatorname{Var}_{\pi}(R(\pi))=
\frac{q^6}{n^2}\left[\frac{ab(a+b+2)}{18}+
\frac{ab(a-1)(b-1)}{45}\right].}
\]
This variance is over the **random contact order of the conditional expectation**, not the total variance of the realized random outbreak.

The numbers of minimum and maximum contact orders are \(2(a+b)!\) and \(2a!b!\), respectively. When the two leaf counts are of the same order, the absolute difference between extreme mean outbreaks grows linearly with the network size (at fixed \(q>0\)).

## Assumptions and scope

All vertices are labeled, the tree is undirected, the initial seed is uniform over its \(n\) vertices and infected before any contact, the \(a+b+1\) contact times are distinct, infection is permanent for the observation period, contacts occur once per edge, and conditional on being an infectious--susceptible encounter transmission succeeds with a common independent Bernoulli probability \(q\). The randomized-calendar law samples every permutation of the labeled edges equally. No timing optimization of the actual random realized epidemic is asserted: the optimized quantity is the conditional expectation \(R(\pi)\). The nondegenerate domain is \(a,b\ge1\), \(0<q\le1\), so the strict characterization of the calendar extrema is meaningful; at \(q=0\) all calendars tie.

## Proof

**Unique-path transmission identity.** For an arbitrary fixed edge order on a tree, a distinct target \(v\) can become infected from an initial seed \(u\) if and only if the edge contact times along the unique simple path from \(u\) to \(v\) are strictly increasing, and all the transmissions on that path succeed. Necessity follows because an edge never reappears, and a vertex must first become infected before transmitting further. Sufficiency follows by processing path contacts chronologically; the path has no cycles or competing alternative routes. Hence the conditional probability of infecting \(v\) from \(u\) is either \(q^{d(u,v)}\) or zero, according to the time-order condition. Linearity over a uniform seed gives
\[
R(\pi)=1+\frac1n\sum_{u\ne v}
q^{d(u,v)}\mathbf1\{\text{edge times along }u\to v\text{ strictly increase}\}.
\]
Only distances \(1\), \(2\) and \(3\) occur in \(D_{a,b}\). Each of its \(a+b+1\) edges contributes two directed one-edge paths, regardless of order. Each unordered two-edge path contributes *exactly one* increasing direction (the edge times are distinct). The number of such unordered paths is \(\binom a2+\binom b2+a+b\): pairs of leaves attached to the same hub and leaves adjacent to the opposite hub. This establishes the constant contribution \(C_{a,b}(q)\).

Every three-edge path connects one left leaf to one right leaf, with the hub--hub contact as its middle edge. One of its directions is strictly increasing precisely when the hub contact time lies strictly between the two leaf contact times. With \(x\) left and \(y\) right contacts before that central time, the number of opposite-side pairs is \(x(b-y)+(a-x)y\). Each contributes exactly one directed three-edge infection path, proving the displayed exact schedule formula.

**Extremal calendars.** Both terms of \(M_{a,b}(x,y)\) are nonnegative. For \(a,b\ge1\), the equation \(M_{a,b}=0\) is equivalent to \((x,y)=(0,0)\) or \((a,b)\). Also
\[
ab-M_{a,b}(x,y)=xy+(a-x)(b-y)\ge0.
\]
Equality here is equivalent to \((x,y)=(a,0)\) or \((0,b)\). Since \(q^3/n>0\), these are exactly the stated minimizing and maximizing schedules. Counting unrestricted internal edge permutations gives \(2(a+b)!\) minimum schedules and \(2a!b!\) maximum schedules.

**Full random-calendar law.** Fix \((x,y)\). Select the \(x\) early left and \(y\) early right edges in \(\binom ax\binom by\) ways; order the \(x+y\) early edges in \((x+y)!\) ways and the remaining \(a+b-x-y\) late edges in \((a+b-x-y)!\) ways. Place the hub contact between those groups. Dividing by the total \((a+b+1)!\) permutations gives the stated exact joint distribution; applying \(M_{a,b}\) gives the distribution of \(R(\pi)\).

**Mean and variance.** Generate the random edge order with independent continuous uniform arrival marks. For each one of the \(ab\) left-right leaf pairs \((i,j)\), define \(I_{ij}=1\) when the hub-contact mark lies strictly between the two leaf-contact marks. Then \(M=\sum_{i,j}I_{ij}\). All six orders of the three marks have equal probability, and exactly two have the hub mark in the middle, so \(\mathbb E I_{ij}=1/3\), \(\operatorname{Var}(I_{ij})=2/9\). If two indicators share exactly one leaf, their joint probability is \(1/6\): conditioning on the hub mark \(t\), the shared leaf lies on either side, and both opposite leaves must lie on the other side, giving \(\int_0^1t(1-t)\,dt=1/6\). Their covariance is \(1/18\). If two pairs share no leaf, conditional independence given the hub mark gives joint probability
\[
\int_0^1[2t(1-t)]^2\,dt=\frac{2}{15},
\]
so their covariance is \(1/45\). There are \(ab\) individual indicators, \(a\binom b2+b\binom a2\) unordered pairs sharing one leaf, and \(2\binom a2\binom b2\) unordered pairs with no leaf in common. Thus
\[
\begin{aligned}
\operatorname{Var}(M)
&=\frac{2ab}{9}+
2\left[a\binom b2+b\binom a2\right]\frac1{18}
+2\left[2\binom a2\binom b2\right]\frac1{45}\\
&=\frac{ab(a+b+2)}{18}+\frac{ab(a-1)(b-1)}{45}.
\end{aligned}
\]
Substituting the linear relation between \(R(\pi)\) and \(M\) proves both moment identities. All steps hold for every stated integer \(a,b\) and every real \(0<q\le1\); finite testing is not used as an infinite proof.

## Verification

Run `python verify.py` with Python 3 and the standard library. The standalone checker verifies the calendar formula and sharp extrema, enumerates all \((a+b+1)!\) edge permutations for every \(a,b\in\{1,2,3,4\}\) with \(a+b\le6\), checks the full exact distribution and rational first two moments, and independently simulates infection event-by-event over all Bernoulli contact-outcome masks for smaller cases at \(q=1/2\) and \(q=2/3\). It additionally checks seeded larger cases. The supplied run produced `VERIFY_OK checks=75521`. These exhaustive *finite* checks test the mathematical derivation but do not replace the universal proof above.

## Relationship to prior work

Holme and Masuda's 2014 public preprint (later 2015 journal publication) motivates the distinction between temporal contact order and final epidemic extent, but studies empirical networks rather than the full two-parameter double-star schedule distribution. De Silva, Molla, Pfender, Retter and Tait (2015 preprint; 2016 journal publication) study the **length of the longest increasing edge-ordered path** in hypercubes and random graphs, not the mean-weighted count and all-calendar law on two-hub trees. Deligkas and Potapov (2022) study reachability optimization by delaying and merging labels, rather than the exact probability distribution over all edge permutations. A prior exact theorem for a single one-contact path is subsumed only in the four-vertex special case \(a=b=1\); neither that path theorem nor the cited source results give the full double-star formula for all \(a,b\), the schedule-count law, or the random-schedule variance. No claim of exhaustive historical priority or independent certification is made.

## Limitations

The theorem is an exact mathematical result for a discrete one-shot, no-recovery transmission mechanism with homogeneous independent transmission probability, a single uniform seed, and a diameter-three tree. It does not cover repeated edge contacts, recoveries, arbitrary trees, multi-seed outbreaks, clustered or correlated transmissions, or the variance of realized outbreak size. The random-calendar variance quantifies sensitivity to schedules, not stochastic uncertainty conditional on a schedule. Earlier equivalent counting identities in the edge-ordering or epidemiology literature may exist beyond the inspected sources; independent validation has not been performed.

## References

1. P. Holme and N. Masuda, *The basic reproduction number as a predictor for epidemic outbreaks in temporal networks*, arXiv:1407.6598, first submitted July 24, 2014; *PLOS ONE* 10 (2015), e0120567. https://arxiv.org/abs/1407.6598 ; https://doi.org/10.1371/journal.pone.0120567
2. J. De Silva, T. Molla, F. Pfender, T. Retter and M. Tait, *Increasing paths in edge-ordered graphs: the hypercube and random graph*, arXiv:1502.03146, first submitted February 10, 2015; *Electronic Journal of Combinatorics* 23 (2016), P2.15. https://arxiv.org/pdf/1502.03146 ; https://doi.org/10.37236/5036
3. A. Deligkas and I. Potapov, *Optimizing reachability sets in temporal graphs by delaying*, *Information and Computation* 285 (2022), 104890. https://doi.org/10.1016/j.ic.2022.104890
