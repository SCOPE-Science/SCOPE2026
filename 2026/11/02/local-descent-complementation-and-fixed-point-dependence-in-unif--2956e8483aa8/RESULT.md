# Local descent complementation and fixed-point dependence in uniform random involutions

## Finding

Let \(\Pi\) be uniformly distributed over all involutions of \([n]=\{1,\ldots,n\}\), where \(n\ge3\). Put
\[
I_i=\mathbf1\{\Pi(i)=i\},\qquad D_j=\mathbf1\{\Pi(j)>\Pi(j+1)\},
\]
for \(1\le i\le n\) and \(1\le j<n\). **Each local descent \(D_j\) is independent of the entire joint vector of fixed-point indicators outside its two adjacent sites:**
\[
\boxed{D_j\ \perp\!\!\!\perp\ (I_i:i\notin\{j,j+1\}).}
\tag{1}
\]
This is joint independence, not merely vanishing pairwise covariances. In particular, for any remotely specified fixed/nonfixed-site pattern having positive probability, the conditional descent probability equals \(1/2\).

Write \(T_m\) for the number of involutions on \(m\) labeled points, with \(T_0=T_1=1\) and \(T_m=T_{m-1}+(m-1)T_{m-2}\). The full cross-covariance matrix is supported on the two diagonals adjacent to the descent positions:
\[
\boxed{
\operatorname{Cov}(I_i,D_j)=\begin{cases}
\displaystyle\frac{(j-1)T_{n-3}-T_{n-1}/2}{T_n},&i=j,\\[5pt]
\displaystyle\frac{(n-j-1)T_{n-3}-T_{n-1}/2}{T_n},&i=j+1,\\[5pt]
0,&i\notin\{j,j+1\}.
\end{cases}}
\tag{2}
\]
For \(F=\sum_{i=1}^n I_i\), the number of fixed points, and \(D=\sum_{j=1}^{n-1}D_j\), the number of descents, it follows for each \(j\) that
\[
\boxed{\operatorname{Cov}(F,D_j)=-\frac{T_{n-2}}{T_n}<0,}\qquad
\boxed{\operatorname{Cov}(F,D)=-\frac{(n-1)T_{n-2}}{T_n}=-1+\frac{T_{n-1}}{T_n}.}
\tag{3}
\]
The dependence is not only a boundary effect. Its fixed-site decomposition is
\[
\boxed{
\operatorname{Cov}(I_i,D)=\begin{cases}
-\dfrac{T_{n-1}}{2T_n},&i\in\{1,n\},\\[5pt]
\dfrac{T_{n-3}-T_{n-2}}{T_n},&2\le i\le n-1.
\end{cases}}
\tag{4}
\]
Thus for \(n\ge4\), **every** fixed-site indicator is strictly negatively correlated with total descents, including all interior sites. In addition, \(\operatorname{Cov}(F,D)\to-1\) as \(n\to\infty\).

## Assumptions and scope

An involution is a permutation satisfying \(\Pi^2=\mathrm{id}\), equivalently a disjoint union of fixed points and transpositions. The probability measure is uniform over all such involutions, not uniform over the full symmetric group and not conditioned on the number of transpositions. Fixed-site indicators concern specified labels, whereas the global statistic \(F\) counts all fixed sites. All identities hold without parity restrictions, for every integer \(n\ge3\). Zero covariance is not automatically independence, but (1) explicitly asserts independence of the full remotely indexed vector.

## Proof

**1. An exact local descent-complementing involution.** Fix \(j\) and abbreviate \(a=j\), \(b=j+1\), and \(\tau=(a\ b)\). Define a map \(\Phi_j\) on all involutions as follows. If \(a,b\) are both fixed points, replace the two singleton cycles by the transposition \((a\ b)\). If \((a\ b)\) is a two-cycle, replace it by the two singleton cycles. In every other case, conjugate by \(\tau\):
\[
\Phi_j(\pi)=\tau\pi\tau.
\]
This map is an involution. In the first two cases it exchanges an ascent at \(j\) with a descent at \(j\). In the conjugation case, write \(x=\pi(a)\) and \(y=\pi(b)\). The new adjacent values are \(\tau(y)\) and \(\tau(x)\). If neither \(x\) nor \(y\) equals \(a\) or \(b\), they are simply exchanged and the comparison reverses. If one of \(a,b\) is fixed but the other is paired to an outside label \(c\), the two relevant comparisons are either \(a>c\) versus \(c>b\), or \(c>b\) versus \(a>c\). Since \(a,b\) are consecutive integers and \(c\) is outside the pair, these comparisons have opposite truth values. Finally, when both adjacent images lie in \(\{a,b\}\), the involution is exactly one of the two exceptional cases already handled. Thus in all cases:
\[
D_j(\Phi_j(\pi))=1-D_j(\pi).
\tag{5}
\]
For every remote label \(i\notin\{a,b\}\), the same map preserves \(I_i\). Indeed, changing the local singleton/two-cycle configuration leaves remote cycles intact; in the conjugation case, \(\tau\) fixes \(i\), and \(\tau\pi(i)=i\) if and only if \(\pi(i)=i\). Consequently \(\Phi_j\) pairs descents and ascents *within every fiber of the full remote fixed-point pattern*. It follows that
\[
\Pr(D_j=1\mid (I_i)_{i\notin\{j,j+1\}}=v)=\tfrac12
\]
for every pattern \(v\) with positive probability. This proves (1), and also \(\mathbb E D_j=1/2\).

**2. One-point conditioning.** The telephone-number recurrence comes from considering whether a specified point is fixed or paired. Fixing a prescribed site leaves \(T_{n-1}\) possible involutions, hence
\[
\Pr(I_i=1)=\frac{T_{n-1}}{T_n}.
\tag{6}
\]
Conditional on \(I_j=1\), the remaining \(n-1\) labels form a uniform involution. For each prescribed \(k<j\), the event \(\Pi(j+1)=k\) pairs \(j+1\) with \(k\), leaving \(T_{n-3}\) involutions on the other labels. There are exactly \(j-1\) such choices of \(k\), so
\[
\Pr(I_j=1,D_j=1)=\frac{(j-1)T_{n-3}}{T_n}.
\tag{7}
\]
Similarly, conditional on \(I_{j+1}=1\), a descent requires \(\Pi(j)>j+1\), giving \(n-j-1\) possible partners and
\[
\Pr(I_{j+1}=1,D_j=1)=\frac{(n-j-1)T_{n-3}}{T_n}.
\tag{8}
\]
Subtracting \(\Pr(I_i=1)\mathbb ED_j=T_{n-1}/(2T_n)\) in the local cases and using (1) for remote sites proves (2).

**3. Covariance summation and strict signs.** For fixed \(j\), add the two nonzero entries in (2). Their numerator is
\[
(n-2)T_{n-3}-T_{n-1}=-T_{n-2}
\]
by the telephone recurrence. This gives the first identity in (3), and summing over \(j\) gives the second. Alternatively, the last equality in (3) follows from \(T_n=T_{n-1}+(n-1)T_{n-2}\). For a fixed interior site \(i\), only the columns \(j=i-1\) and \(j=i\) contribute. Their sum is
\[
\frac{(n-1)T_{n-3}-T_{n-1}}{T_n}
=\frac{T_{n-3}-T_{n-2}}{T_n}.
\]
At each endpoint there is only one nonzero adjacent column, with covariance \(-T_{n-1}/(2T_n)\), proving (4). Since \(T_{n-2}>T_{n-3}\) for \(n\ge4\), all interior covariances are then strictly negative. For \(n=3\) the lone interior covariance is zero, a genuine boundary case.

**4. Limiting covariance.** Put \(r_n=T_n/T_{n-1}\) for \(n\ge1\). Then \(r_1=1\) and \(r_n=1+(n-1)/r_{n-1}\). Induction gives \(\sqrt n\le r_n\le1+\sqrt n\): the upper bound follows from the lower bound at \(n-1\), and the lower bound from the upper bound at \(n-1\). Therefore \(T_{n-1}/T_n=1/r_n\le n^{-1/2}\). Equation (3) yields \(\operatorname{Cov}(F,D)=-1+O(n^{-1/2})\), and in particular the claimed limit.

## Verification

The standalone standard-library program `verify.py` enumerates every involution on \([n]\) for \(2\le n\le10\), compares all mixed covariance entries to (2), tests (3), and checks exactly that every nonempty remote fixed-status fiber contains equally many local ascents and descents. It also checks the local map \(\Phi_j\) object by object: involutivity, descent complementation and preservation of every remote fixed-site bit. It passed **345,599 exact assertions**, including the terminal size with 9,496 involutions. For \(n=2\), the checker tests the natural two-site boundary formulas separately, without relying on \(T_{n-3}\). The infinite-size proof is the pairing and counting argument above; finite enumeration is not used to establish any universal assertion.

Run with `python verify.py` in an ordinary Python 3 environment; no external package or data file is required.

## Relationship to prior work

The full-text paper of Guo and Zeng (2005) establishes the univariate Eulerian descent distribution for involutions, including recurrence and unimodality results, but does not retain the positions of fixed points. Chow (2008) and the earlier Désarménien–Foata theory give richer aggregate involution enumerators, still with the number of fixed points rather than their labeled locations. Reutenauer's original descent-set/cycle-type theorem (1989; subsequently Gessel–Reutenauer, 1993) can count involutions by specified descent set and overall cycle type; because cycle type loses which labels are fixed, those statements do not directly imply the conditional independence of a descent from all **remote fixed-site statuses** or matrix (2).

Earlier fixed-transposition-class inversion-gap formulas give the adjacent descent probability conditional on the **number of transpositions**, namely \(2k(n-k)/(n(n-1))\) at class \(k\). Mixing those formulas with the known class weights can recover the aggregate covariance in (3); that aggregate identity is **not** asserted as independently novel. However the class count does not identify which sites are fixed, and those formulas do not imply the fiberwise independence (1), or the site-resolved covariance matrix (2).

A separately published uniform-*permutation* local covariance decomposition identifies remote fixed-site cancellation and attributes its global covariance \(-1/n\) entirely to endpoints. Conditioning to involutions changes the probability law: here interior fixed sites are strictly negatively correlated with total descents and the aggregate covariance tends to \(-1\), so that result does not cover (1)–(4). The two models must not be conflated. The specific local-complementing map \(\Phi_j\) and its fiberwise conditional-independence conclusion are the contribution claimed here; no novelty is asserted for telephone numbers or the aggregate enumerators.

## Limitations

The theorem concerns uniform involutions and ordinary adjacent descents only. It says nothing about higher-order independence of different descent indicators, conditional behavior after fixing the number of transpositions, or nonuniform permutation laws. The strict sign statement excludes the interior site at \(n=3\), where covariance vanishes. The remote conditional-independence statement includes only *fixed-site statuses*, not arbitrary remote permutation information. Earlier highly refined enumerations may conceal an equivalent fixed-*location* specialization; such historical priority is a remaining risk, and no independent mathematical audit has been performed.

## References

1. V. J. W. Guo and J. Zeng, “The Eulerian Distribution on Involutions is Indeed Unimodal,” arXiv:math/0504195, initially posted 2005-04-10; *J. Combin. Theory Ser. A* 113 (2006), 1061–1071. https://arxiv.org/abs/math/0504195
2. C. Chow, “On the Eulerian Enumeration of Involutions,” *Electron. J. Combin.* 15 (2008), R71, https://doi.org/10.37236/795.
3. C. Reutenauer, “Number of Permutations with Given Descent Set and Cycle Structure,” *Séminaire Lotharingien de Combinatoire* B21h (1989), original full text: https://www.mat.univie.ac.at/~slc/s/sc21reutenauer.pdf; subsequent joint paper I. M. Gessel and C. Reutenauer, *J. Combin. Theory Ser. A* 64 (1993), 189–215, https://doi.org/10.1016/0097-3165(93)90095-p.
4. J. Désarménien and D. Foata, “Fonctions symétriques et séries hypergéométriques basiques multivariées,” *Bull. Soc. Math. France* 113 (1985), 3–22, https://doi.org/10.24033/bsmf.2018.
5. P. J. Forrester, T. Nagao and E. M. Rains, “Correlation functions for random involutions,” *Int. Math. Res. Notices* (2006), https://doi.org/10.1155/IMRN/2006/89796, archival preprint arXiv:math/0503074.
