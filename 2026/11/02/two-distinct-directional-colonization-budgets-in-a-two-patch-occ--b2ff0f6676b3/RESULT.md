# Two distinct directional-colonization budgets in a two-patch occupancy chain

## Finding
Consider two habitat patches with independent background colonization rate \(c>0\) per empty patch, local extinction rates \(0<e<f\), and a fixed total directional cross-colonization capacity \(B>0\). Let \(u\in[0,B]\) be the extra colonization rate into patch 2 when only patch 1 is occupied; the reverse capacity is \(B-u\). In the unique stationary law, let \(E(u)\) be the expected number of occupied patches and \(P(u)\) the probability both patches are occupied.

**Theorem.** Each objective has a unique maximizing allocation, respectively \(u_E\) and \(u_P\). There are explicit, strictly ordered positive budget thresholds \(0<B_E<B_P\) such that
\[
\begin{array}{c|c}
0<B\le B_E&u_E=u_P=B\\
B_E<B\le B_P&B/2<u_E<B=u_P\\
B>B_P&B/2<u_E<u_P<B.
\end{array}
\]
Thus simultaneous occupation concentrates capacity strictly more toward the higher-extinction patch than mean occupation does, once the budget is sufficient for these objectives to disagree. For equal extinction rates \(e=f>0\), both objectives instead have the unique optimizer \(u=B/2\).

For explicit thresholds set
\[
C=2c+e+f,\quad \delta=f-e,\quad g=ef/c,\quad h=e+f+2g,\quad j=e+f+g,\quad
r=\frac{\delta}{\sqrt{h^2-\delta^2}+h}.
\]
Then
\[
B_E=\frac{Cr}{1-r},\quad T=\delta(2C+g)-2jC,\qquad
B_P=\frac{T+\sqrt{T^2+8(j-\delta)\delta C(C+g)}}{4(j-\delta)}.
\]
Both are finite and strictly positive. In particular, \(u_E=(B+(B+C)r)/2\) for \(B>B_E\). For \(B>B_P\), \(u_P=B/2+t_P\), with \(t_P\) the unique root of \(W_P\) in \((0,B/2)\) defined below.

## Assumptions and scope
The stochastic process is a continuous-time Markov chain on \(00,10,01,11\), where each bit denotes habitat occupancy. Its nonzero off-diagonal rates are \(00\to10: c\), \(00\to01:c\), \(10\to00:e\), \(10\to11:c+u\), \(01\to00:f\), \(01\to11:c+B-u\), \(11\to10:f\), and \(11\to01:e\). Rates \(c,e,f,B\) are arbitrary positive real numbers; \(e<f\), and the allocation \(u\) includes endpoints. No other transitions occur. Positive background colonization makes the finite chain irreducible, giving a unique stationary law. The theorem optimizes stationary occupancy, not quasi-stationary survival time in a closed metapopulation.

## Proof
Write \(L=B+C\), \(t=u-B/2\), and \(a=(B+2c)L/2\). Let \(\tau_s\) be the cofactor of the negative generator with state \(s\)'s row and column deleted. The four-state Markov-chain tree identity, or direct substitution into \(\pi Q=0\), gives
\[
\tau_{00}=efL,\quad \tau_{10}=cf(L-2t),\quad \tau_{01}=ce(L+2t),\quad
\tau_{11}=c(a+\delta t-2t^2).
\]
Each cofactor is positive for \(-B/2\le t\le B/2\), and \(\pi_s=\tau_s/\sum\tau_s\). Defining
\[
b=L\left(\frac{B+2c}{2}+e+f+\frac{ef}{c}\right),\qquad
D(t)=b-\delta t-2t^2>0,
\]
one obtains \(\sum\tau_s=cD(t)\) and
\[
E(t)=\frac{L^2-4t^2}{D(t)},\qquad
P(t)=\frac{a+\delta t-2t^2}{D(t)}.
\]
Since \(\delta>0\), reflecting a negative \(t\) to \(-t>0\) strictly improves both objectives: the numerator of \(E\) stays the same and that of \(P\) increases, while the common denominator decreases. All maxima lie in \([0,B/2]\).

The derivatives of \(E(t)\) and \(P(t)\) have common positive denominator \(D(t)^2\) and respective numerators
\[
W_E(t)=\delta L^2-4Lh\,t+4\delta t^2,\qquad
W_P(t)=\delta L(L+g)-4Lj\,t+4\delta t^2.
\]
Both polynomials are positive at zero and strictly decreasing on \([0,L/2]\), since their derivatives there are at most \(-4L(h-\delta)\) and \(-4L(j-\delta)\), respectively. At \(L/2\) they are negative: \(W_E(L/2)=-2(h-\delta)L^2\), and \(W_P(L/2)=-2(j-\delta)L^2+\delta Lg<0\) because \(j-\delta=2e+g\) and \(\delta<L\). Denote the unique roots on \((0,L/2)\) by \(t_E=Lr/2\) and \(t_P\), respectively. Since \(B<L\), the derivative signs on the feasible interval give the optimizers \(u_E=B/2+\min(t_E,B/2)\) and \(u_P=B/2+\min(t_P,B/2)\).

The condition \(t_E<B/2\) is equivalent to \(B>B_E=Cr/(1-r)\). Substituting \(t=B/2\) into \(W_P\) gives
\[
W_P(B/2)=-2(j-\delta)B^2+TB+\delta C(C+g).
\]
Its leading coefficient is negative and its constant term positive, so it has exactly one positive zero, \(B_P\) as stated. The \(P\) optimum is interior precisely when \(B>B_P\).

On \([0,L/2]\) the difference \(W_P(t)-W_E(t)=\delta Lg+4Lgt\) is strictly positive. Therefore \(W_P(t_E)>0\) and \(t_P>t_E\). In particular, at \(B=B_E\) we have \(W_P(B/2)>0\), so \(B_P>B_E\). Applying the feasible bounds to the two roots gives all three regimes and their endpoint inclusions. If \(e=f\), then \(\delta=0\), and both derivative signs are strictly opposite to that of \(t\) away from zero on the full feasible interval. Thus both unique optima are \(u=B/2\).

## Verification
Run `python verify.py` with the Python standard library. The program constructs the generator independently, solves the stationary linear system by exact rational Gaussian elimination, and checks both objective formulas at 405 rational parameter/allocation tuples. For \(c=e=B=1\) and \(f=3\) it checks the derivative signs separating the two optima, brackets the mean-occupancy optimizer by \(0.85<u_E<0.86\), and verifies the radical simplification for the exact optimizer, all by rational arithmetic. These finite checks corroborate the algebra rather than replace the parameter-uniform proof.

In this example \(B_E\approx0.6742346142<1<B_P\approx1.5532340636\). The mean-occupancy optimizer is \(u_E=18-7\sqrt6\approx0.8535718005\), while simultaneous-occupancy probability is maximized at \(u_P=1\).

## Relationship to prior work
Levins' 1969 metapopulation framework introduced occupancy-based colonization–extinction dynamics. Etienne and Heesterbeek (2001) optimize persistence-related conservation interventions in a stochastic model; their accessible abstract describes extinction-time objectives and prioritizing links, but does not establish this externally recolonized stationary two-objective allocation law. Vuilleumier and Possingham (2006) analyze asymmetric colonization in a 100-patch simulation and mean-field setting, rather than this exact two-patch four-state optimization. Wu et al. (2020) analyze asymmetric dispersal for deterministic population densities with logistic source–sink dynamics. The distinct claim concerns the paired mean-count and joint-occupancy thresholds and the strict ordering of the allocations, not the joint-occupancy objective in isolation.

## Limitations
The theorem models recolonization of empty patches; it does not model mortality reduction in occupied patches, migration costs, evolution, time-dependent decisions, demographic abundance, or a permanently extinct state. External immigration \(c>0\) is essential: with \(c=0\) the stationary occupancy vanishes and the question changes to quasi-stationarity. Results apply to two patches only. Historical priority is not established: the full 2001 Etienne–Heesterbeek article was not accessible, and a more general matrix-allocation theorem could subsume the formulas.

## References
1. Levins, R. (1969), *Some Demographic and Genetic Consequences of Environmental Heterogeneity for Biological Control*, Bulletin of the Entomological Society of America 15:237–240. DOI 10.1093/besa/15.3.237.
2. Etienne, R. S., and Heesterbeek, J. A. P. (2001), *Rules of Thumb for Conservation of Metapopulations Based on a Stochastic Winking-Patch Model*, American Naturalist 158:389–407. DOI 10.1086/321986.
3. Vuilleumier, S., and Possingham, H. P. (2006), *Does colonization asymmetry matter in metapopulations?*, Proceedings of the Royal Society B 273:1637–1642. DOI 10.1098/rspb.2006.3469. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC1634917/.
4. Wu, H., Wang, Y., Li, Y., and DeAngelis, D. L. (2020), *Dispersal asymmetry in a two-patch system with source–sink populations*, Theoretical Population Biology. DOI 10.1016/j.tpb.2019.11.004.
