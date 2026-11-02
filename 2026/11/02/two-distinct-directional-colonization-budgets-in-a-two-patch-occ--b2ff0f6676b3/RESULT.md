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
Both are finite and strictly positive. In particular, \(u_E=(B+(B+C)r)/2\) for \(B>B_E\), while the optimum \(u_P\) is the unique interior root specified in the proof when \(B>B_P\).

## Assumptions and scope
The stochastic process is a continuous-time Markov chain on \(00,10,01,11\), where each bit denotes habitat occupancy. Its nonzero off-diagonal rates are \(00\to10: c\), \(00\to01:c\), \(10\to00:e\), \(10\to11:c+u\), \(01\to00:f\), \(01\to11:c+B-u\), \(11\to10:f\), and \(11\to01:e\). Rates \(c,e,f,B\) are arbitrary positive real numbers; \(e<f\), and the allocation \(u\) includes endpoints. No other transitions occur. Positive background colonization makes the finite chain irreducible, giving a unique stationary law. The theorem optimizes stationary occupancy, NOT quasi-stationary survival time in a closed metapopulation.

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
one obtains \(\sum\tau_s=cD(t)\) and, exactly,
\[
E(t)=\frac{L^2-4t^2}{D(t)},\qquad
P(t)=\frac{a+\delta t-2t^2}{D(t)}.
\]
Since \(\delta>0\), reflection about \(t=0\) strictly improves both objectives when \(t\) is changed from negative to positive (the numerators of \(E\) match, that of \(P\) increases, and both denominators decrease). All maxima lie in \([0,B/2]\).

On this interval, the signs of \(E'(t)\) and \(P'(t)\) are, respectively, the signs of
\[
W_E(t)=\delta L^2-4Lh\,t+4\delta t^2,\qquad
W_P(t)=\delta L(L+g)-4Lj\,t+4\delta t^2.
\]
The first expression is strictly decreasing on \(0\le t\le B/2\) because \(h>\delta\) and \(L>B\), starts positive, and vanishes uniquely at \(t_E=Lr/2\). The second starts positive and is strictly decreasing throughout \([0,B/2]\): its derivative is \(-4Lj+8\delta t\le -4Lj+4\delta B<0\), because \(j>\delta\) and \(L>B\). Hence each objective is strictly increasing until its first possible derivative zero, then strictly decreasing. The maximizer is its unconstrained positive root if that root is less than \(B/2\), and otherwise the endpoint \(t=B/2\).

The condition \(t_E<B/2\) is equivalent to \(B>B_E=Cr/(1-r)\). Substituting \(t=B/2\) into \(W_P\) gives
\[
W_P(B/2)=-2(j-\delta)B^2+TB+\delta C(C+g).
\]
Its leading coefficient is negative and constant term positive, so it has exactly one positive zero, \(B_P\) as stated; \(P\) is interior-optimized precisely when \(B>B_P\).

To order the two optima, observe
\[
\frac{P(t)}{E(t)}=\frac{a+\delta t-2t^2}{L^2-4t^2}.
\]
At the free optimum \(t=t_E>0\), where \(\delta(L^2+4t_E^2)=4Lh\,t_E\), the numerator of the derivative of this ratio is
\[
\delta(L^2+4t_E^2)-4L(e+f)t_E
=8Lg\,t_E>0.
\]
Because \(E'(t_E)=0\), this implies \(P'(t_E)>0\); the unique free optimizer of \(P\) therefore lies strictly to the right of \(t_E\). In particular \(B_P>B_E\) (at \(B=B_E\), \(P\) is still increasing at the upper endpoint). Clipping both free optima to the permitted interval gives all three claimed regimes, with all boundary inclusions. If \(e=f\), symmetry gives \(\delta=0\), and the derivative signs are strictly opposite to \(t\); both unique optima are \(t=0\).

## Verification
The accompanying standard-library program `verify.py` constructs the generator independently, solves the stationary linear system with exact rational Gaussian elimination, and checks the cofactor-derived formulas on 405 rational parameter/allocation tuples. It also tests strict separation of the objectives in an exact-parameter example. These tests support, but do not replace, the algebraic proof above. Run with `python verify.py`.

For \(c=e=B=1\) and \(f=3\), the thresholds satisfy \(B_E\approx0.6742346142<1<B_P\approx1.553234064\). The mean-occupancy optimizer is \(u_E=18-7\sqrt6\approx0.853571801\), while simultaneous-occupancy probability is maximized at \(u_P=1\). This gives distinct conservation objectives even with only two patches.

## Relationship to prior work
Levins' 1969 metapopulation framework introduced occupancy-based colonization–extinction dynamics. Etienne and Heesterbeek (2001) optimize persistence-related conservation interventions in a stochastic model; their accessible abstract describes extinction-time objectives and prioritizing links, but does not establish this externally recolonized stationary two-objective allocation law. Vuilleumier and Possingham (2006) analyze asymmetric colonization in a 100-patch simulation and mean-field setting, rather than this exact two-patch four-state optimization. Wu et al. (2020) analyze asymmetric dispersal for deterministic population densities with logistic source–sink dynamics. Neither mathematical objects nor objectives are interchangeable. The exact paired threshold and strict optimizer ordering above are not claimed to supersede these results.

## Limitations
The theorem models recolonization of empty patches; it does not model mortality reduction in occupied patches, migration costs, evolution, time-dependent decisions, demographic abundance, or a permanently extinct state. External immigration \(c>0\) is essential: with \(c=0\) the stationary occupancy vanishes and the question changes to quasi-stationarity. Results apply to two patches only. Historical priority is not independently established: the full 2001 Etienne–Heesterbeek article was not accessible, and a more general unpublished or published matrix-allocation theorem could subsume the formulas.

## References
1. Levins, R. (1969), *Some Demographic and Genetic Consequences of Environmental Heterogeneity for Biological Control*, Bulletin of the Entomological Society of America 15:237–240. DOI 10.1093/besa/15.3.237.
2. Etienne, R. S., and Heesterbeek, J. A. P. (2001), *Rules of Thumb for Conservation of Metapopulations Based on a Stochastic Winking-Patch Model*, American Naturalist 158:389–407. DOI 10.1086/321986.
3. Vuilleumier, S., and Possingham, H. P. (2006), *Does colonization asymmetry matter in metapopulations?*, Proceedings of the Royal Society B 273:1637–1642. DOI 10.1098/rspb.2006.3469. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC1634917/.
4. Wu, H., Wang, Y., Li, Y., and DeAngelis, D. L. (2020), *Dispersal asymmetry in a two-patch system with source–sink populations*, Theoretical Population Biology. DOI 10.1016/j.tpb.2019.11.004.
