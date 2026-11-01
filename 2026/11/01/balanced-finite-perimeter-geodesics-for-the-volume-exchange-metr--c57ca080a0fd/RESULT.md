# Balanced finite-perimeter geodesics for the volume-exchange metric

## Finding
The equal-volume subspace of finite-perimeter partitions is a geodesic space for the one-to-one volume-exchange metric. For any two such partitions \(P,Q\) into \(m\) cells, an explicit path \(R_t\), \(0\le t\le1\), preserves every cell volume and satisfies
\[
d_V^1(R_s,R_t)=|s-t|d_V^1(P,Q),\qquad
I(R_t)\le I(P)+I(Q)+m(m-1)\operatorname{diam}(\Omega)^{d-1}.
\]

## Assumptions and scope
Let \(d\ge2\), \(m\ge2\) be integers and let \(\Omega\subset\mathbb R^d\) be a nonempty bounded, connected Lipschitz domain. Put \(M=\mathcal L^d(\Omega)>0\) and \(D=\operatorname{diam}(\Omega)\). A partition is a collection of exactly \(m\) measurable cells covering \(\Omega\) modulo null sets, pairwise disjoint modulo null sets, each of measure \(M/m\) and finite relative perimeter. Labels are immaterial. Define its interface area by \(I(P)=\frac12\sum_{i=1}^{m}\operatorname{Per}(P_i;\Omega)\). The distance \(d_V^1\) is the one-to-one volume-exchange metric of [1]. By [1, Theorem 5], this equals the minimum, over partial matchings, of half the sum of symmetric-difference volumes. No individual-cell connectivity, smoothness, or convexity is assumed.

## Proof
**Optimal alignment.** If a partial matching leaves a cell \(P_i\) and a cell \(Q_j\) unmatched, pairing them replaces the cost \(\mu(P_i)+\mu(Q_j)\) by \(\mu(P_i\triangle Q_j)=\mu(P_i)+\mu(Q_j)-2\mu(P_i\cap Q_j)\), which cannot be larger. With equally many cells all pairs may therefore be completed to a full matching; a minimizing permutation exists. Relabel \(Q\) by that permutation. Write \(p,q\) for the corresponding labels and \(B_{ij}=P_i\cap Q_j\). The metric identity becomes
\[
L:=d_V^1(P,Q)=\mu\{p\ne q\}=\sum_{i\ne j}\mu(B_{ij}).
\]
Every \(B_{ij}\) has finite perimeter as an intersection of finite-perimeter sets.

**Volume-balanced switches.** For each \(i\ne j\), the function \(F_{ij}(c)=\mu(B_{ij}\cap\{x_1<c\})\) is continuous, nondecreasing, and runs from zero to \(\mu(B_{ij})\) by Fubini's theorem. For \(0<t<1\) select a nondecreasing threshold \(c_{ij}(t)\) with \(F_{ij}(c_{ij}(t))=t\mu(B_{ij})\), and put \(E_{ij}(t)=B_{ij}\cap\{x_1<c_{ij}(t)\}\). At the endpoints take \(E_{ij}(0)=\varnothing\) and \(E_{ij}(1)=B_{ij}\), with null blocks empty throughout. Thus \(\mu(E_{ij}(t))=t\mu(B_{ij})\), the switches are nested as \(t\) increases, and all switched sets have finite perimeter.

Define \(r_t=q\) on the union of the off-diagonal switched blocks \(E_{ij}(t)\), and \(r_t=p\) elsewhere. Its level-set partition is \(R_t\). Since both terminal partitions have the same volume for each aligned index,
\[
\sum_{j\ne k}\mu(B_{kj})=\mu(P_k)-\mu(B_{kk})=\mu(Q_k)-\mu(B_{kk})=\sum_{i\ne k}\mu(B_{ik}).
\]
Hence
\[
\mu((R_t)_k)=\mu(P_k)-t\sum_{j\ne k}\mu(B_{kj})+t\sum_{i\ne k}\mu(B_{ik})=M/m.
\]
Each intermediate cell therefore remains positive and balanced.

**Exact geodesic identity.** For \(0\le s\le t\le1\), nested switches show that the set of points where the natural labels \(r_s,r_t\) differ has measure \((t-s)L\). Matching these labels gives \(d_V^1(R_s,R_t)\le(t-s)L\). Likewise, \(d_V^1(P,R_s)\le sL\) and \(d_V^1(R_t,Q)\le(1-t)L\). The triangle inequality gives
\[
L\le d_V^1(P,R_s)+d_V^1(R_s,R_t)+d_V^1(R_t,Q)\le sL+d_V^1(R_s,R_t)+(1-t)L.
\]
Thus \(d_V^1(R_s,R_t)=(t-s)L\), proving constant speed. If \(L=0\), the constant path works.

**Finite perimeter and area control.** For each fixed \(t\), the intermediate label agrees locally with either \(p\) or \(q\) away from the original interfaces and the at most \(m(m-1)\) cut hyperplanes \(\{x_1=c_{ij}(t)\}\). By locality of BV derivatives, its jump set is contained, up to an \(\mathcal H^{d-1}\)-null set, in that union. Every cross section of \(\Omega\) by a coordinate hyperplane has \((d-1)\)-measure at most \(D^{d-1}\): its projection in each of the remaining coordinate directions is contained in an interval of length at most \(D\). Taking the half-sum of cell perimeters counts each partition interface once. Consequently
\[
I(R_t)\le I(P)+I(Q)+m(m-1)D^{d-1}<\infty,
\]
including both endpoints. This proves that the entire shortest path lies in the prescribed finite-perimeter equal-volume partition space.

## Verification
The standalone `checker.py` implements a finite-grid counterpart with exact integer masses and rational metric distances. Running `python checker.py` passed **302 exact assertions** for balanced partitions into two, three, and four cells; each test checks endpoint balance, all intermediate cell masses, and every quarter-time pair of distances. These finite tests do not establish the continuum theorem. Its proof rests on matching cost, exact quantiles, flow balance, the metric triangle inequality, and finite-perimeter locality.

## Relationship to prior work
The matching formula and equality with the continuous volume-exchange metric are due to Alvarado et al. [1]. Leonardi and Tamanini [2, Section 3.1] introduced a closely equivalent unlabeled symmetric-difference metric on partitions and developed its metric and finite-perimeter properties. The present conclusion is different: a constrained *equal-volume, finite-perimeter* subspace admits shortest paths preserving each cell volume and satisfying a uniform interface-area bound. The prior metric identities alone do not state those pathwise geometric properties. Volume-constrained isoperimetric partition research [3] addresses different minimization questions.

## Limitations
No claim is made about uniqueness, connected or smooth cells, perimeter minimizing geodesics, optimality of the displayed uniform bound, or infinitely many cells. Hidden precedent in earlier partition metric literature is a historical-priority risk. No finite numerical experiment substitutes for the continuum argument.

## References
1. E. Alvarado, J. Jung, J. Mason, S. Pothagoni, and B. Schweinhart, *The Volume Exchange Metric*, arXiv:2610.26897v1, publicly submitted 16 October 2026, https://arxiv.org/html/2610.26897v1.
2. G. P. Leonardi and I. Tamanini, *Metric spaces of partitions, and Caccioppoli partitions*, Adv. Math. Sci. Appl. **12** (2002), 725–753, https://cvgmt.sns.it/paper/189/.
3. M. Novaga, E. Paolini, and V. M. Tortorelli, *Locally isoperimetric partitions*, Trans. Amer. Math. Soc. **378** (2025), 2517–2548, arXiv:2312.13709.
