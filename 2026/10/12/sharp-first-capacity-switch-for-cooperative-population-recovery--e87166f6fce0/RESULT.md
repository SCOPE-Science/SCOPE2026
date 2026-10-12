# Sharp first capacity switch for cooperative population recovery

## Finding
A finite habitat can be too large for a population that requires a mate to produce offspring: diluting encounters may outweigh additional room for births. The theorem below gives an exact first recovery target where adding a habitat site is beneficial and the unique mortality-to-birth-attempt ratio at which the best habitat capacity changes.

Fix an integer \(K\ge3\). In the precisely defined model below, the recovery probability from two founders is
\[
P_{K,L}(\gamma)=\left[1+\sum_{j=2}^{K-1}\prod_{i=2}^{j}
\frac{\gamma(L-1)^2}{(i-1)(L-i)}\right]^{-1},\qquad L\ge K,\quad\gamma>0.
\]
Every capacity maximizing this probability lies between \(K\) and \(2K-3\), inclusive. For recovery targets \(K=3\) and \(K=4\), the only maximizing capacities are \(L=3\) and \(L=4\), respectively. At the first different target, \(K=5\), the optimizer is \(L=5\) for \(\gamma<\gamma_*\), \(L=6\) for \(\gamma>\gamma_*\), and both at equality, where
\[
\gamma_* =\frac{113+\sqrt{23901}}{253}\approx1.05770546456.
\]
No capacity \(L\ge7\) is optimal for \(K=5\).

## Assumptions and scope
There are \(L\) exchangeable sites, at most one individual per site, and initially exactly two occupied sites. Each living individual dies independently at constant rate \(d>0\). Each individual independently attempts offspring production at rate \(\beta>0\). At each attempt it independently draws (with replacement) two sites uniformly among the other \(L-1\) sites. The first draw must land on another occupied site (a mate), and the second on an unoccupied site (a nursery). Both conditions are required for one birth. There is no relocation, immigration, resource turnover, spatial neighbor restriction, age structure or environmental heterogeneity. Each attempt's two site draws are independent; occupied and unoccupied outcomes for the two draws are automatically disjoint. The stopping criterion is the first arrival at population \(K\) or zero, without imposing a time horizon.

When there are \(i\) individuals, the total birth and death rates are
\[
\lambda_i=\beta\frac{i(i-1)(L-i)}{(L-1)^2},\qquad\mu_i=d i.
\]
Births are absent when only one individual survives; thus hitting \(K\) before extinction from two individuals is equivalent to hitting \(K\) before hitting one individual. Define \(\gamma=d/\beta\); only this rate ratio affects the hitting probability.

## Proof
**Hitting law.** Set \(u_1=0\), \(u_K=1\), and let \(u_i\) be the probability of hitting \(K\) before state one when starting from \(i\), for \(2\le i<K\). The backward equation is
\[
\lambda_i(u_{i+1}-u_i)=\mu_i(u_i-u_{i-1}).
\]
With increments \(w_i=u_i-u_{i-1}\), we obtain
\[
w_{j+1}=w_2\prod_{i=2}^{j}\frac{\mu_i}{\lambda_i}
=w_2\prod_{i=2}^{j}\frac{\gamma(L-1)^2}{(i-1)(L-i)}.
\]
Because \(\sum_{i=2}^{K}w_i=1\) and \(u_2=w_2\), the displayed exact hitting law follows. All denominators are strictly positive under the hypotheses.

**Finite universal capacity bound.** Let \(r_i(L)=\gamma(L-1)^2/((i-1)(L-i))\). For real \(L>i\), differentiating gives
\[
\frac{d}{dL}\log r_i(L)
=\frac{L+1-2i}{(L-1)(L-i)}.
\]
If \(L\ge2K-3\) and \(2\le i\le K-1\), this derivative is nonnegative; after increasing \(L\) beyond this bound it is strictly positive. Therefore every nonconstant summand in the hitting-law denominator increases strictly as capacity increases beyond \(2K-3\). In particular \(P_{K,L}(\gamma)<P_{K,2K-3}(\gamma)\) for any integer \(L>2K-3\). Thus every maximizing capacity lies in the asserted finite interval for all \(\gamma>0\).

**First two recovery targets.** For \(K=3\), the capacity interval contains only \(L=3\). For \(K=4\), it contains \(L=4,5\). The two respective denominators are
\[
D_{4,4}=1+\frac92\gamma+\frac{81}{4}\gamma^2,\qquad
D_{4,5}=1+\frac{16}{3}\gamma+\frac{64}{3}\gamma^2.
\]
The latter exceeds the former at every positive \(\gamma\). Hence the unique optimal capacities are \(3\) and \(4\), respectively.

**First switch.** For \(K=5\) the general bound leaves only \(L=5,6,7\). Their denominators are
\[
\begin{aligned}
D_{5,5}&=1+\frac{16}{3}\gamma+\frac{64}{3}\gamma^2+\frac{1024}{9}\gamma^3,\\
D_{5,6}&=1+\frac{25}{4}\gamma+\frac{625}{24}\gamma^2+\frac{15625}{144}\gamma^3,\\
D_{5,7}&=1+\frac{36}{5}\gamma+\frac{162}{5}\gamma^2+\frac{648}{5}\gamma^3.
\end{aligned}
\]
Each nonconstant coefficient of \(D_{5,7}\) strictly exceeds the corresponding coefficient of \(D_{5,5}\), so capacity seven is worse than capacity five for every positive \(\gamma\). The general capacity bound eliminates capacities above seven; moreover the derivative calculation shows all capacities at least seven get worse as capacity increases. Finally, exact subtraction yields
\[
D_{5,6}-D_{5,5}=\frac{\gamma}{48}(44+226\gamma-253\gamma^2).
\]
The quadratic factor is positive for \(0<\gamma<\gamma_*\), zero at \(\gamma_*\), and negative above it. Since hitting probability is the reciprocal of the strictly positive denominator, these signs give the complete and unique optimality classifications claimed. This completes the proof.

## Verification
The accompanying standalone `verify_model.py` uses only Python's exact `fractions.Fraction` arithmetic. It checks the six coefficient formulas, the threshold polynomial on an exact rational isolating interval, and the finite range reduction over many values. As an independent algebraic cross-check it solves the original Markov backward equations using exact rational Gauss–Jordan elimination and compares with the closed hitting formula. It also checks coefficient domination for capacities through 999 and enumerated recovery targets through 17. The checker reports:

`VERIFY_OK exact_coefficients=1 threshold_interval=1 direct_backward_equations=1 algebraic_general_cutoff_test=1 checks= 3917`

These finite checks corroborate but do not constitute proof of the all-parameter, all-capacity assertions; the displayed derivative, backward recurrence and exact factorization prove those assertions.

## Relationship to prior work
Windus and Jensen (2006 preprint; 2007 journal) study a distinct spatial lattice population with mate interactions and show that reducing the habitat may improve survival for low-density populations. Their simulation-based conservation phenomenon motivates, but does not establish, this well-mixed finite-target hitting-probability capacity classification. Doering, Sargsyan and Sander (2004 preprint) provide exact birth–death methods primarily for mean extinction times; the first-passage recurrence used here is standard rather than claimed as new. Cuddington and collaborators (2015) study mate-location structure and Allee thresholds, providing ecological context rather than the present capacity optimizer. The assessed contribution is the exact all-capacity bound and first nontrivial optimum switch within the model specified here, not the general facts that Allee effects occur or that birth–death hitting recurrences exist.

## Limitations
The independent uniform sampling of a mate and a vacant site is a modeling assumption; its optimal-capacity theorem does not extend automatically to nearest-neighbor lattices, sex-structured reproduction, finite time windows, stochastic habitats, or empirical population viability. The threshold applies to the probability of *ever first reaching a prescribed finite target*, not survival forever, which would have probability zero in this finite closed population with possible individual deaths. The theorem determines the first recovery target exhibiting a capacity switch; it does not classify the detailed capacity phase diagrams for every larger recovery target. General birth–death theory could imply portions of the recurrence and structural cutoff, and the literature search cannot exclude every unindexed equivalent optimization.

## References
1. C. R. Doering, K. V. Sargsyan, L. M. Sander, *Extinction times for birth-death processes: exact results, continuum asymptotics, and the failure of the Fokker–Planck approximation*, arXiv:q-bio/0401016v1 (first posted 2004-01-10), https://arxiv.org/abs/q-bio/0401016.
2. A. Windus, H. J. Jensen, *Allee Effects and Extinction in a Lattice Model*, arXiv:q-bio/0612005v1 (first posted 2006-12-05), https://arxiv.org/abs/q-bio/0612005; *Theoretical Population Biology* 72 (2007), 459–467, https://doi.org/10.1016/j.tpb.2007.07.006.
3. K. Cuddington, Z. T. Hull, W. J. S. Currie, M. A. Koops, *Landmarking and strong Allee thresholds*, *Theoretical Ecology* 8 (2015), 333–347 (online 2015-03-11), https://doi.org/10.1007/s12080-015-0254-z.
