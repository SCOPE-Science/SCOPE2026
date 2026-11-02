# Four seasons are the first schedule-sensitive horizon for latent–infectious invasion

## Finding

In a discrete susceptible–exposed–infectious–susceptible (SEIS) model, keep the exposed-stage progression rate and infectious-stage recovery rate fixed, and prescribe a periodic multiset of transmission probabilities. With one, two, or three seasons in a period, **every permutation of the same transmission levels has exactly the same disease-free invasion multiplier**. With four seasons, all schedules with four distinct levels fall into exactly three multiplier classes, ordered by the products of opposite-season transmission levels. This yields a parameter-independent sharp ordering and an explicit example in which alternating and grouped transmission schedules have opposite invasion verdicts despite identical seasonal averages and multisets.

Precisely, put \(a=1-\gamma\), \(c=\gamma\), \(d=1-\mu\), and
\[
 M(b)=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
 P(b_1,\dots,b_k)=M(b_k)\cdots M(b_1).
\]
For \(1\le k\le3\), \(\rho(P)\) is invariant under every permutation. For \(k=4\), let \(S=\sum_{i=1}^4 b_i\) and \(Q=b_1b_3+b_2b_4\). Then
\[
 \operatorname{tr}P=a^4+d^4+c(a^2+ad+d^2)S+c^2Q,\qquad
 \det P=\prod_{i=1}^{4}(ad-cb_i).
\]
If \(0<b_{(1)}<b_{(2)}<b_{(3)}<b_{(4)}\le1\), the three possible opposite-season pairings give **strictly ordered invasion multipliers**, from least to greatest:
\[
 \begin{split}
 &b_{(1)}b_{(4)}+b_{(2)}b_{(3)},\\
 &b_{(1)}b_{(3)}+b_{(2)}b_{(4)},\\
 &b_{(1)}b_{(2)}+b_{(3)}b_{(4)}.
 \end{split}
\]
Each level occurs for eight of the 24 labelled season permutations. For two low and two high seasons with \(0<L<H\le1\), alternation \((L,H,L,H)\) strictly exceeds clustering \((L,L,H,H)\) in disease-free invasion multiplier: their monodromy traces differ by exactly \(c^2(H-L)^2\).

## Assumptions and scope

The nonlinear SEIS difference equations on the population simplex are
\[
 \begin{aligned}
 S_{t+1}&=S_t-\beta_t S_t I_t+\mu I_t,\\
 E_{t+1}&=(1-\gamma)E_t+\beta_t S_t I_t,\\
 I_{t+1}&=\gamma E_t+(1-\mu)I_t,
 \end{aligned}
\]
with \(S_t+E_t+I_t=1\), \(0<\gamma,\mu<1\), and \(0<\beta_t\le1\). The schedule is a prescribed periodic sequence of length \(k\). These hypotheses preserve the simplex and give the disease-free state \((S,E,I)=(1,0,0)\). Its infected linearization on \((E,I)\) is exactly \(M(\beta_t)\). Thus \(\rho(P)>1\) signifies local linear invasion and \(\rho(P)<1\) signifies local linear extinction under periodic repetition; no claim is made about exact nonlinear prevalence trajectories or endemic cycles.

For four unequal levels the result is a complete classification over **all** orderings, not just an alternating-versus-clustered comparison. If levels coincide, the formula and the weak ordering remain true, but classes can merge.

## Proof

**1. Invariant determinant.** Multiplicativity gives
\[
 \det P(b_1,\dots,b_k)=\prod_{i=1}^k(ad-cb_i),
\]
which depends only on the seasonal multiset.

**2. Trace identities.** Direct multiplication, without approximation, gives for \(k=1,2,3\), respectively,
\[
 \begin{aligned}
 \operatorname{tr}P_1 &=a+d,\\
 \operatorname{tr}P_2 &=a^2+d^2+c(b_1+b_2),\\
 \operatorname{tr}P_3 &=a^3+d^3+c(a+d)(b_1+b_2+b_3).
 \end{aligned}
\]
Every expression is symmetric in the season levels. A further multiplication gives the four-season trace identity in the Finding. An alternative derivation expands \(M(b)=M(0)+bE_{12}\): the degree-two trace terms arise exactly from pairs of insertion positions separated by one season, because \(E_{12}^2=0\), \(E_{12}M(0)E_{12}=cE_{12}\), and \(\operatorname{tr}(E_{12}M(0)E_{12}M(0))=c^2\); degree-three and degree-four terms vanish because at least two insertion factors would be adjacent. The remaining terms are \(a^4+d^4+c(a^2+ad+d^2)S\).

**3. Why trace orders invasion.** Each \(M(b)\) is strictly positive. Hence every product \(P\) is a strictly positive \(2\times2\) matrix and its Perron root is the larger simple real eigenvalue
\[
 r(T,D)=\frac{T+\sqrt{T^2-4D}}{2},
\]
where \(T=\operatorname{tr}P\) and \(D=\det P\). Along any common-determinant comparison,
\[
 \frac{\partial r}{\partial T}=\frac{r}{\sqrt{T^2-4D}}>0.
\]
Consequently the trace identities yield equality of multipliers for \(k\le3\), and the ordering for \(k=4\) is precisely the ordering of \(Q\).

**4. Sharp four-season pairing classes.** Write the four distinct increasing levels as \(u<v<w<z\). The three possible opposite pairings are
\[
 Q_{\min}=uz+vw,\quad Q_{\mathrm{mid}}=uw+vz,\quad Q_{\max}=uv+wz.
\]
Their gaps are
\[
 Q_{\mathrm{mid}}-Q_{\min}=(v-u)(z-w)>0,
\qquad Q_{\max}-Q_{\mathrm{mid}}=(z-u)(w-v)>0.
\]
Every partition of the four levels into two opposite pairs is realized by eight labelled cyclic arrangements, proving the count and strict three-level statement. For \(L,L,H,H\), the alternating arrangement has opposite-pair sum \(L^2+H^2\), while the clustered arrangement has \(2LH\); the gap is \((H-L)^2\). Since \(k\le3\) admits no schedule sensitivity and \(k=4\) has a strict example, four is the sharp horizon.

**5. Exact reversal of the invasion threshold.** Let
\[
 \gamma=\mu=\frac12,\qquad L=\frac1{20},\qquad H=1.
\]
For the alternating \((L,H,L,H)\) and clustered \((L,L,H,H)\) schedules, respectively, matrix multiplication yields
\[
 T_{\mathrm{alt}}=\frac{1861}{1600},\qquad
 T_{\mathrm{clust}}=\frac{15}{16},\qquad
 D_{\mathrm{alt}}=D_{\mathrm{clust}}=\frac{81}{25600}.
\]
Their characteristic polynomials evaluated at one satisfy
\[
 1-T_{\mathrm{alt}}+D=-\frac{4095}{25600}<0,
\qquad 1-T_{\mathrm{clust}}+D=\frac{1681}{25600}>0.
\]
The alternating product has one positive eigenvalue above one. The clustered product has two positive eigenvalues summing to \(15/16<1\), so both are below one. Therefore one schedule invades and the other decays linearly, even with the same mean and the same two low and two high transmission periods. This example is strictly within the stated biological range of parameters.

## Verification

The supplied `CHECK.py` is standalone Python 3 code requiring only the standard library. Run `python3 CHECK.py`. It verifies the displayed trace and determinant formulas using exact rational arithmetic across 9,963 permutation/product comparisons, including all 24 permutations for each of 405 generic four-level parameter sets, checks the three strict classes and the sub-four invariance, and reproduces both characteristic-polynomial signs in the exact example. The universal results follow from the proof above, not from the finite check.

## Relationship to prior work

Bacaër (2009) develops general periodic matrix-population growth and reproduction-number theory, including the monodromy-growth relationship, but does not state this four-season opposite-pairing classification in the inspected full text. Cushing and Ackleh (2011) develop a reproductive number for general periodic population projection matrices, with illustrative period-two models. Cao and Zhou (published online 2012) give periodic discrete SIR/SEIS epidemic thresholds; the accessible abstract concerns reproduction numbers and disease persistence rather than a verified four-level order classification. Tanaka and Aihara (first reported 2012) study consequences of seasonal variation patterns using switched-system calculations; their accessible abstract does not establish or exclude this exact four-season linear-invasion theorem. The inaccessible portions of the last two articles and broader matrix-product rearrangement literature remain genuine historical-priority risks.

The present distinction is an **exact complete order theorem for one fixed four-season multiset**, valid for arbitrary distinct transmission levels, together with a sharp minimum number of seasons and an exact invasion-reversal example. It is not asserted as an original general Floquet or next-generation-matrix framework.

## Limitations

The conclusion is local to the disease-free linearization of the stated discrete SEIS system. It does not order outbreak peaks, final epidemic sizes, stationary prevalence, or nonlinear endemic orbits. The sign of the growth gap is universal, but its magnitude depends on progression and transmission contrast. The four-class count assumes distinct labelled seasonal values; coincident values can merge classes. Full historical priority cannot be guaranteed, especially against inaccessible related full texts and broader rearrangement identities for matrix pencils. Independent scientific review has not been performed.

## References

1. N. Bacaër, *Periodic matrix population models: growth rate, basic reproduction number, and entropy*, Bulletin of Mathematical Biology 71 (2009), 1781–1792, DOI: 10.1007/s11538-009-9426-6. Author-hosted full text: https://ummisco.pages.ird.fr/france/bacaer/2009BMB2.html ; public online record dated 2009-05-02.
2. J. M. Cushing and A. S. Ackleh, *A net reproductive number for periodic matrix models*, Journal of Biological Dynamics 6 (2012), 166–188, first published online 2011-02-18, DOI: 10.1080/17513758.2010.544410.
3. H. Cao and Y. Zhou, *The basic reproduction number of discrete SIR and SEIS models with periodic parameters*, Discrete and Continuous Dynamical Systems B 18 (2013), 37–56, published online September 2012, DOI: 10.3934/dcdsb.2013.18.37.
4. G. Tanaka and K. Aihara, *Effects of seasonal variation patterns on recurrent outbreaks in epidemic models*, Journal of Theoretical Biology 317 (2013), 87–95, first publicly listed 2012-10-04, DOI: 10.1016/j.jtbi.2012.09.038.
