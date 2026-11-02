# A prevalence threshold and posterior reversal for two stopped ecological survey modalities

## Finding
Consider one site, of fixed but unknown occupancy state \(H\in\{0,1\}\), with prior \(\pi=\Pr(H=1)\in(0,1)\). Two prescribed sensing blocks \(A,B\) of fixed lengths can be administered in either order. An alarm stops the entire survey immediately, including the block in which it occurs. Every pair of consecutive blocks terminates at the end of the second block if no alarm occurs. Within each block, alarms follow state-conditional Poisson processes as defined below.

Put \(u_{hi}=\exp(-\lambda_{hi}t_i)\) and
\[
D_h=(1-u_{hA})(1-u_{hB})\left(\frac{c_A}{\lambda_{hA}}-\frac{c_B}{\lambda_{hB}}\right),\qquad h\in\{0,1\}.
\]
If \(L_{AB}\) and \(L_{BA}\) denote the total *random survey labour expenditure* in the two orders, then
\[
\boxed{\mathbb E L_{AB}-\mathbb E L_{BA}=(1-\pi)D_0+\pi D_1.}
\]
Thus if \(D_0D_1<0\), the optimal order reverses exactly once at the unique prevalence
\[
\boxed{\pi_* = \frac{D_0}{D_0-D_1}\in(0,1).}
\]
In particular, if \(D_0>0>D_1\), the strict minimizer is \(BA\) for \(\pi<\pi_*\), the two orders tie exactly at \(\pi_*\), and \(AB\) is the strict minimizer for \(\pi>\pi_*\). When \(D_0\) and \(D_1\) have the same strict sign, the same strict ordering prevails for all prevalences. When either is zero, the displayed affine formula supplies all boundary and equality cases; if both are zero, the orders always tie.

The order reversal can occur even if **each sensing block is individually informative**, meaning \(\lambda_{1i}>\lambda_{0i}\). For \(c_A=c_B=1\), \(t_A=t_B=\log 2\), and
\[
(\lambda_{0A},\lambda_{1A})=(1,4),\qquad (\lambda_{0B},\lambda_{1B})=(2,3),
\]
we have \(D_0=3/16\), \(D_1=-35/512\), and \(\pi_*=96/131\). At prior \(\pi=9/10\), \(AB\) has smaller expected labour by \(219/5120\) than \(BA\). An obligatory preceding informative block \(C\) with rates \((\lambda_{0C},\lambda_{1C})=(1,3)\), cost rate \(1\), and length \(\log 2\), changes the occupancy posterior **after no alarm** to \(9/13<96/131\). Conditional on this no-alarm history, the strict preferred order of the remaining two blocks is now \(BA\), despite both candidate blocks still being individually informative. The exact unconditional difference between \(CAB\) and \(CBA\) is \(69/40960>0\).

## Assumptions and scope
Fix \(t_A,t_B>0\), constant expenditure rates \(c_A,c_B>0\), and conditional alarm intensities \(\lambda_{hi}>0\) for each \(h=0,1\), \(i=A,B\). The unknown occupancy state is sampled once and does not change during the protocol. Conditional on it, each alarm process has an exponential first-alarm waiting time, and survival probabilities over disjoint blocks multiply. The block durations, intensities and expenditure rates are known, no alarm is verified or disambiguated before stopping, and the policy **always** runs both prescribed blocks in a chosen order unless an earlier alarm terminates it. There are no setup, switching or schedule-dependent costs. An optional terminal charge for alarm/no-alarm may depend on \(H\) but not on which block produced an alarm or its arrival time; such charges are invariant under the two orders. The optimization compares the two possible orders only; it does not optimize the prescribed lengths or select a fully adaptive multiblock strategy.

## Proof
For a block \(i\), conditional on state \(H=h\) and on reaching the block without an earlier alarm, the survey spends \(c_i\min\{T_{hi},t_i\}\), with \(T_{hi}\sim\mathrm{Exp}(\lambda_{hi})\). By integrating its survival function,
\[
\mathbb E[c_i\min\{T_{hi},t_i\}\mid H=h]=c_i\int_0^{t_i}e^{-\lambda_{hi}s}\,ds
=\frac{c_i(1-u_{hi})}{\lambda_{hi}}.
\]
The probability of reaching block \(B\) after block \(A\) is \(u_{hA}\). Hence, conditional on \(H=h\),
\[
\mathbb E[L_{AB}\mid h]=\frac{c_A(1-u_{hA})}{\lambda_{hA}}+u_{hA}\frac{c_B(1-u_{hB})}{\lambda_{hB}},
\]
\[
\mathbb E[L_{BA}\mid h]=\frac{c_B(1-u_{hB})}{\lambda_{hB}}+u_{hB}\frac{c_A(1-u_{hA})}{\lambda_{hA}}.
\]
Subtract and factor \((1-u_{hA})(1-u_{hB})\) to obtain exactly \(D_h\). Conditioning on \(H\) gives the affine interchange identity, its sign classification, and (when signs oppose) the unique strict-crossing threshold \(\pi_*\).

For each state, the final no-alarm probability is \(u_{hA}u_{hB}\) in either order. Therefore a charge depending only on state and the final alarm/no-alarm indicator has identical statewise expectation for both orders, so adding it does not change the interchange law.

For an obligatory prefix of alarm-driven blocks, let \(S_h\) be its conditional probability of producing no alarm. The prefix's own expected labour is unchanged by the order chosen for the following \(A,B\); the state-specific contribution of swapping those two is multiplied by \(S_h\). Therefore the full-schedule labour difference is
\[
(1-\pi)S_0D_0+\pi S_1D_1=(\pi S_1+(1-\pi)S_0)[(1-\pi')D_0+\pi'D_1],
\]
where Bayes' rule gives \(\pi'=\pi S_1/(\pi S_1+(1-\pi)S_0)\). The positive prefactor proves the exact posterior-threshold rule on reaching the pair. No claim is made that the obligatory prefix was itself optimally selected.

For the displayed rational witness, the prescribed lengths \(\log2\) give \(u_{0A}=1/2\), \(u_{1A}=1/16\), \(u_{0B}=1/4\), and \(u_{1B}=1/8\). Direct substitution yields \(D_0=3/16\), \(D_1=-35/512\), and \(\pi_*=96/131\). At \(\pi=9/10\), the difference is \(-219/5120\). For the fixed prefix \(C\), no-alarm probabilities are \(S_0=1/2\), \(S_1=1/8\); thus \(\pi'=9/13\), and the full-order difference is \((1/10)(1/2)(3/16)+(9/10)(1/8)(-35/512)=69/40960>0\). These are exact rational identities. The strict inequalities follow by integer cross multiplication.

## Verification
Run \(\texttt{python3 checker_ordering.py}\) in the folder containing the accompanying standalone checker. It independently computes the exact rational examples and checks the direct expected-labour integral against the interchange formula for \(2{,}500\) randomized informative Poisson-model instances with possible obligatory prefixes, along with \(200\) order-invariant reachability checks. A successful run reports \(2{,}700\) randomized checks and the exact example. These finite tests are supplemental: the proof above is analytic for every real parameter satisfying the assumptions.

## Relationship to prior work
Guillera-Arroita, Hauser and McCarthy (2014) formulate ecological surveillance ending at first detection and derive expected inspection time and budget decisions, but their detection process does not include false alarms when the species is absent or an order choice between two false-alarm-prone modalities. Miller and colleagues (2011) address occupancy models with false-positive detections, but study inference rather than within-block stopped-labour order selection. Smart and colleagues (2016) compare imperfect-detection methods under survey cost constraints, optimizing allocations rather than the stated first-alarm ordering. Duffuaa and Pollock (1999) provide broad dependent binary-inspection sequencing with classification errors and fixed per-inspection costs; their full-information dynamic programming method is a close conceptual predecessor. The present formula explicitly integrates *state-dependent time expended inside a stopped Poisson block* and yields an exact two-state prevalence crossing and a conditional no-alarm order reversal. Whether a larger stochastic scheduling result already entails this specialization remains an historical-priority risk.

## Limitations
This is a mathematical surveillance model, not a claim about empirical alarm-rate calibration or species occurrence at a particular site. Fixed alarm rates, latent occupancy stability, perfect immediate stoppage, negligible setup/switching cost, and order-independent terminal consequences are essential. The theorem does not optimize durations, allow verification of alarms, or account for the impact of false-positive management actions whose costs depend on which method issued the alarm. It does not assert novelty beyond the literature comparisons described here; an independent historical-priority evaluation has not been performed.

## References
1. Guillera-Arroita, G., Hauser, C. E. and McCarthy, M. A. (2014). *Optimal surveillance strategy for invasive species management when surveys stop after detection*. Ecology and Evolution. DOI: 10.1002/ece3.1056. First publicly posted 11 April 2014. https://onlinelibrary.wiley.com/doi/full/10.1002/ece3.1056
2. Miller, D. A. W. et al. (2011). *Improving occupancy estimation when two types of observational error occur: non-detection and species misidentification*. Ecology. DOI: 10.1890/10-1396.1. https://doi.org/10.1890/10-1396.1
3. Smart, A. S. et al. (2016). *Assessing the cost-efficiency of environmental DNA sampling*. Methods in Ecology and Evolution. DOI: 10.1111/2041-210X.12598. https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.12598
4. Duffuaa, S. O. and Pollock, S. M. (1999). *Optimal Sequencing of Inspection of Dependent Characteristics*. Journal of Optimization Theory and Applications 103:557–565. DOI: 10.1023/A:1021731907266. https://www.researchgate.net/publication/30845953_Optimal_Sequencing_of_Inspection_of_Dependent_Characteristics
