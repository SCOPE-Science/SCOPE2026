# A sharp mean–variance frontier for demand-uncertain Braess routing

## Finding

Consider the normalized directed four-vertex Braess road network with origin \(O\), destination \(T\), intermediate vertices \(A,B\), and travel-time functions \(\ell_{OA}(x)=x\), \(\ell_{AT}(x)=1\), \(\ell_{OB}(x)=1\), \(\ell_{BT}(x)=x\). Compare the original network against the network with an additional zero-time directed link \(A\to B\). Let \(D\geq0\) be a random *nonatomic traffic demand*, observed before travelers choose routes. At each realized demand, travelers reach their own deterministic Wardrop equilibrium. Denote by \(C_1(D)\) and \(C_0(D)\) the resulting **total physical travel times** with and without the shortcut, respectively, and let \(\Delta(D)=C_1(D)-C_0(D)\). Positive expected \(\Delta\) means the new road raises expected total travel time.

**Theorem (sharp distribution-free variance threshold).** For every nonnegative demand law with finite second moment, letting \(m=\mathbb E D\), \(v=\operatorname{Var}(D)\), one has

\[
\boxed{\mathbb E\Delta(D)\geq \frac34\left[\left(m-\frac23\right)(2-m)-v\right].}
\]

For every fixed \(\frac23<m<2\), put \(v_*(m)=(m-\frac23)(2-m)\). If \(v<v_*(m)\), **every** nonnegative demand distribution with these moments suffers a strict expected Braess paradox: \(\mathbb E\Delta>0\). If \(v=v_*(m)\), the expected difference is nonnegative for every distribution, and equality holds **only** for the unique law supported on \(\{\frac23,2\}\) with mean \(m\). If \(v>v_*(m)\), there exist two-point demand laws with the **same** prescribed \(m,v\), one with \(\mathbb E\Delta<0\) and another with \(\mathbb E\Delta>0\). Hence the frontier is exact for all positive variances and every mean in the stated interval.

For example, at \(m=\frac32\), the sharp frontier is \(v_*=\frac5{12}\). The laws \(\Pr(D=\frac12)=\frac13,\Pr(D=2)=\frac23\) and \(\Pr(D=1)=\frac23,\Pr(D=\frac52)=\frac13\) both have \(m=\frac32\), \(v=\frac12\), but their expected shortcut costs are respectively \(-\frac1{24}\) and \(+\frac13\).

## Assumptions and scope

The model uses a continuum of infinitesimal travelers, a single origin–destination pair, nonnegative real-valued demand, a one-way costless shortcut, congestion-dependent link costs precisely as displayed, independent deterministic route choice at **each realized demand**, and deterministic Wardrop equilibria after demand becomes known. There is no toll, uncertainty in road capacities, stochastic route-choice noise, travel-time risk aversion, queuing dynamic, or induced change of demand when the road is added. The comparison is of the **expected total flow-weighted physical time**, not the expected per-traveler delay or an ex-ante Wardrop equilibrium at mean demand. The finding is a moment guarantee for this canonical network, not a distribution-free theorem for all networks.

## Proof

**1. Solve both equilibrium problems exactly.** Without the shortcut, both old paths have equal cost at equal flow \(d/2\), giving \(C_0(d)=d(1+d/2)\) for each \(d\geq0\). With the shortcut, write the amounts assigned to the upper, lower and new crossing paths as \(u,w,c\geq0\), with \(u+w+c=d\). Their three route costs are \(1+u+c\), \(1+w+c\), and \(u+w+2c=d+c\). Symmetry and the convex Beckmann potential give \(u=w=(d-c)/2\). Up to an irrelevant constant, its potential is

\[
\Phi_d(c)=\frac{(d+c)^2}{4}+d-c,\qquad 0\leq c\leq d.
\]

It is strictly convex in \(c\), and its unique minimizer is \(c=\min\{d,\max\{0,2-d\}\}\). Thus the shortcut-only regime applies for \(0\leq d\leq1\), all three routes can be used for \(1\leq d\leq2\), and the shortcut carries zero flow for \(d\geq2\). The corresponding total actual travel times are \(C_1(d)=2d^2\), \(C_1(d)=2d\), and \(C_1(d)=C_0(d)\). Subtracting yields

\[
\Delta(d)=\begin{cases}\frac32d^2-d,&0\leq d\leq1,\\ d-\frac12d^2,&1\leq d\leq2,\\0,&d\geq2.\end{cases}
\]

The formulas agree at both junctions. This deterministic curve is background input to the moment theorem, not a claim that the original Braess example is new.

**2. Establish a globally sharp quadratic support inequality.** Write \(q(d)=\frac34(d-\frac23)(2-d)\). Direct algebra produces the *exact* nonnegative gap

\[
\Delta(d)-q(d)=\begin{cases}\left(1-\frac32d\right)^2,&0\leq d\leq1,\\\left(1-\frac12d\right)^2,&1\leq d\leq2,\\\frac34(d-\frac23)(d-2),&d\geq2.\end{cases}
\]

It vanishes for nonnegative \(d\) **only** at \(d=\frac23\) and \(d=2\). Taking expectations, justified by the finite second moment, gives \(\mathbb E q(D)=\frac34[(m-\frac23)(2-m)-v]\) and the stated inequality. At the threshold \(v=v_*\), equality requires \(D\) almost surely in \(\{\frac23,2\}\), and the mean forces unique weights \(\Pr(D=\frac23)=\frac34(2-m)\) and \(\Pr(D=2)=\frac34(m-\frac23)\). These weights are positive and sum to one for \(\frac23<m<2\), giving variance \(v_*\).

**3. Prove exact sharpness above the frontier, at every variance.** Fix \(\frac23<m<2\) and \(v>v_*\). For any \(0<r<m\), define \(h=m+v/(m-r)\) and assign weights \((h-m)/(h-r)\) at \(r\) and \((m-r)/(h-r)\) at \(h\). This law has mean \(m\) and variance exactly \(v=(m-r)(h-m)\). Select a sufficiently small positive \(\varepsilon\) and make two choices \(r_-=\frac23-\varepsilon>0\) and \(r_+=\frac23+\varepsilon<m\). Because \(v>(m-\frac23)(2-m)\), both corresponding \(h\) values exceed \(2\) when \(\varepsilon\) is small enough. In the first law \(\Delta(r_-)<0\) and \(\Delta(h)=0\), so its expected difference is negative. In the second \(\Delta(r_+)>0\) and \(\Delta(h)=0\), so its expected difference is positive. Both have the prescribed two moments. No higher-moment assumptions are required.

The exact \(m=\frac32,v=\frac12\) examples in the finding follow by substituting the two stated two-point laws into \(\Delta\). The proof covers all admissible continuum demand laws, including discrete mixtures; no finite enumeration is used as a substitute for an infinite-dimensional proof.

## Verification

Run `python3 checker.py` in the same directory as this file. The standalone standard-library checker performs 14,500 exact-rational assertions: deterministic Wardrop complementarity and piecewise travel-time expressions, identities for the global quadratic support gap, random finite-support laws satisfying the bound, general-mean two-point equality and strict opposite-sign witnesses, and the exact numerical example. The algebraic steps in the proof, rather than these finite checks, establish the theorem for all laws.

## Relationship to prior work

The deterministic Braess phenomenon and the general distinction between user and system equilibria are classical; Steinberg and Zangwill (1983) analyze fixed-demand paradox occurrence much more generally. Random travel demand and stochastic network equilibria are well established; Nakayama and Watling (2014) develop models with stochastic flow distributions, using equilibrium interpretations that differ from **post-realization deterministic Wardrop routing**. Zhao, Fu and Wang (2014) consider a Braess network under logit stochastic user equilibrium and elastic demand, also a different route-choice model. The 2009 ICUS network-design study compares simulations under varying demands and congestion probabilities, but the accessible relevant text does not exhibit the present exact first-two-moment frontier. The new assertion is the distribution-free exact variance threshold, its uniquely sharp equality law, and opposite-sign laws with identical first two moments; it is not novelty of Braess' example, stochastic congestion modeling or the fixed-demand cost curve.

## Limitations

This is an idealized demand-revealed equilibrium comparison. If drivers do not re-equilibrate for each demand realization, if congestion latency functions or tolls differ, or if travelers optimize risk-adjusted or ex-ante expected costs, the threshold can change. The threshold is sufficient to certify **positive expected harm below it**; above it, sign is not identified by the first two moments, not guaranteed negative. The 2014 elastic-demand stochastic-equilibrium paper was not available for full-text comparison; no claim of independently certified historical priority is made. The proof and finite checks are not empirical traffic validation.

## References

- R. Steinberg and W. I. Zangwill, *The Prevalence of Braess' Paradox*, Transportation Science 17 (1983), 301–318. DOI: https://doi.org/10.1287/trsc.17.3.301 (published online August 1, 1983).
- S. Nakayama and D. Watling, *Consistent formulation of network equilibrium with stochastic flows*, Transportation Research Part B 66 (2014), 50–69. DOI: https://doi.org/10.1016/j.trb.2014.03.007 ; lawful open author manuscript https://eprints.whiterose.ac.uk/id/eprint/84524/.
- C. Zhao, B. Fu and T. Wang, *Braess paradox and robustness of traffic networks under stochastic user equilibrium*, Transportation Research Part E 61 (2014), 135–141. DOI: https://doi.org/10.1016/j.tre.2013.11.008. (Abstract accessible; full text not inspected.)
- *The Application of Stochastic Assignment Technique to Network Design Problems*, ICUS Report 37, 2nd Joint Student Seminar on Civil Infrastructures (July 6, 2009), pp. 239–263, https://icus.iis.u-tokyo.ac.jp/wp/wp-content/uploads/2021/04/37_2nd-joint-student-seminar-2009_2009-01v2.pdf (relevant excerpts inspected; some pages unavailable as page images).
