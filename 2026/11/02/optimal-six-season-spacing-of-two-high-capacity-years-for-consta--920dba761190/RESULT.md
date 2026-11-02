# Optimal six-season spacing of two high-capacity years for constant-yield Beverton–Holt harvesting

## Finding
Fix \(\mu>1\), \(0<L<H\), and a repeated six-season sequence containing two capacities \(H\) and four capacities \(L\). For the Beverton–Holt fishery with constant catch \(h\), the maximal sustainable catch depends only on the cyclic separation \(d\in\{1,2,3\}\) of the two high-capacity seasons, and satisfies the strict universal ordering
\[
0<h_1<h_2<h_3.
\]
Thus evenly separating the favorable seasons maximizes the sustainable constant catch, and placing them next to one another minimizes it. The result holds for all allowed parameter values, not merely for one simulation.

## Assumptions and scope
Population is modeled in discrete seasons by
\[
x_{j+1}=F_{K_j,h}(x_j):=\frac{\mu K_jx_j}{K_j+(\mu-1)x_j}-h,\qquad x_j>0,
\]
where \(\mu>1\), \(0<L<H\), \(h\ge0\), and \(K_{j+6}=K_j\) has the multiset \(\{H,H,L,L,L,L\}\). Strictly positive six-periodic states include fixed points of smaller minimal period. Define \(h_d\) as the largest quota for which a strictly positive six-periodic state exists when the two occurrences of \(H\) are separated by \(d\) cyclic time steps, with \(d=1,2,3\) up to rotation and reflection. The objective is a fixed quota in every season, not an optimized proportion or season-dependent quota.

## Proof
Put \(B_K(h)=\begin{pmatrix}K&\mu-1\\-hK&\mu K-h(\mu-1)\end{pmatrix}\). Its projective action on \((1,x)\) is precisely \(F_{K,h}(x)\), and \(\det B_K=\mu K^2\). Let \(M_d(h)\) be the product of the six matrices in chronological order (later matrices multiplying on the left), and \(T_d(h)=\operatorname{tr}M_d(h)\). The determinant is independent of order:
\[
\det M_d=\mu^6H^4L^8,\qquad 2\sqrt{\det M_d}=2\mu^3H^2L^4=:Q.
\]
At zero catch, the usual Beverton–Holt periodic composition has an attracting positive fixed point; its derivative is strictly less than one. For sufficiently small positive catches, the attracting periodic state persists by continuity, and an additional unstable positive periodic state emerges near zero. If a positive periodic state survives at a quota, one also survives at every smaller quota: the period map is increasing in population and decreasing in catch, and a suitably large positive population is an upper solution. Because all positive iterates are bounded above by \(\mu H/(\mu-1)\), feasible positive fixed points cannot escape to infinity. Nor can a feasible fixed point approach the zero boundary at a strictly positive quota, since each positive output requires its positive input to exceed \(h/\mu\). Consequently, disappearance of the two fixed points at the maximum feasible quota occurs by tangency. The projective matrix then has a repeated positive eigenvalue; equivalently, \(T_d(h_d)=Q\), and \(h_d\) is the first positive zero of \(T_d(h)-Q\).

We next obtain a common upper bound on all three thresholds. Set
\[
h_0:=\frac{L(\mu+1-\sqrt\mu)}{\mu-1}.
\]
For the low-capacity map \(F_{L,h}\), which is strictly increasing on nonnegative input, its supremum after one step at \(h=h_0\) equals \(L/(\sqrt\mu+1)\). Direct substitution gives
\[
F_{L,h_0}\!\left(\frac{L}{\sqrt\mu+1}\right)=-\frac{L}{\mu-1}<0.
\]
Therefore no orbit can stay positive across two successive low-capacity seasons at or above \(h_0\). Any circular sequence with four low and two high years necessarily has two adjacent low years. It follows that
\[
0<h_d<h_0\quad(d=1,2,3).
\]
The strict upper bound also follows by continuity of the two-step negative margin.

To compare the three traces, set \(t=\operatorname{tr}B_L=L(\mu+1)-h(\mu-1)\). Expand each six-fold product by writing \(B_H=B_L+(H-L)A\), where \(A=\begin{pmatrix}1&0\\-h&\mu\end{pmatrix}\). Terms with zero or one occurrence of \(A\) are independent of the separation \(d\). The two-\(A\) term is \((H-L)^2\operatorname{tr}(A B_L^{d-1}A B_L^{5-d})\). Applying the Cayley–Hamilton identity \(B_L^2=tB_L-\mu L^2 I\), or expanding these \(2\times2\) products directly, gives the exact polynomial identities
\[
T_2-T_1=h^2\mu(H-L)^2(\mu-1)^2\bigl[t^2-\mu L^2\bigr],
\]
\[
T_3-T_2=h^2\mu^2L^2(H-L)^2(\mu-1)^2.
\]
For \(0<h<h_0\), the definition of \(h_0\) gives \(t>\sqrt\mu L\). Hence both trace differences are strictly positive. Since \(T_d(0)=(1+\mu^6)H^2L^4>Q\) and every first positive root lies in \((0,h_0)\), these strictly ordered continuous functions must have strictly ordered first roots: \(h_1<h_2<h_3\). Indeed, if a larger trace had a first zero no later than a smaller trace, the smaller trace would already be negative there and would have had an earlier zero, a contradiction. This establishes the theorem for every allowed \(\mu,L,H\).

## Verification
The companion `verify6harvest.py` independently builds all three chronological matrix products in symbolic arithmetic; checks their determinants, zero-catch traces and two factorizations; verifies the two-low-season extinction calculation; and provides exact rational brackets for the first roots for \((\mu,L,H)=(4,1,4)\). In increasing separation order, these are
\[
\begin{aligned}
h_1&\in(0.413372280,0.413372282),\\
h_2&\in(0.424771624,0.424771627),\\
h_3&\in(0.429903690,0.429903692).
\end{aligned}
\]
The exact symbolic identities and the preceding proof—not the finite checks—establish the all-parameter theorem. Run `python verify6harvest.py` with SymPy installed.

## Relationship to prior work
AlSharawi and Ben Haj Rhouma (2010) established the projective-matrix and trace criterion, the dihedral symmetry, and permutation orderings through period five. Their concluding Question 1 asks for higher-period classifications. The present result treats the first unclassified period, six, in the natural two-favorable-season family, and establishes strict ordering uniformly across all positive capacities and growth factors. The 2009 constant-environment study treats different harvesting comparisons. Bohner and Streipert (2016) optimize harvest *effort* (a proportional mechanism) in a periodic Beverton–Holt system, not the permutation dependence of a uniform subtraction quota. Al-Ghassani and AlSharawi (2020) fix and permute harvesting *quotas* and compare the population geometric mean, not the ordering of capacity years under a fixed quota. Distinct maps and objectives prevent a direct implication. No historical priority beyond the inspected material is claimed.

## Limitations
Only six seasons with exactly two identical high capacities and four identical low capacities are classified. The result concerns deterministic positive periodic persistence for sufficiently large initial stocks, not small-population extinction probabilities, a global optimum over nonconstant harvest policies, or an arbitrary number of capacity levels. Some closely related post-2016 full text could not be inspected; broader unrecognized permutation theorems remain a historical-priority risk. The semistable boundary cycle is considered sustainable in the mathematical existence sense and is not robust to adverse demographic noise.

## References
1. Z. AlSharawi and M. Ben Haj Rhouma, *The Discrete Beverton–Holt Model with Periodic Harvesting in a Periodically Fluctuating Environment*, Advances in Difference Equations (2010), article 215875, doi:10.1155/2010/215875 (first available public date: 2010-03-08).
2. Z. AlSharawi and M. B. H. Rhouma, *The Beverton–Holt model with periodic and conditional harvesting*, Journal of Biological Dynamics 3 (2009), 463–478, doi:10.1080/17513750802601041.
3. M. Bohner and S. Streipert, *Optimal harvesting policy for the Beverton–Holt model*, Mathematical Biosciences and Engineering 13 (2016), 673–695, doi:10.3934/mbe.2016014.
4. A. S. Al-Ghassani and Z. AlSharawi, *The effect of maps permutation on the global attractor of a periodic Beverton–Holt model*, Applied Mathematics and Computation 370 (2020), 124905, doi:10.1016/j.amc.2019.124905.
