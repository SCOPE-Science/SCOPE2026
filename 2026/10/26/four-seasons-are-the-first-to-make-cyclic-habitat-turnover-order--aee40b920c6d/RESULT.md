# Four seasons are the first to make cyclic habitat turnover order-sensitive

## Finding
Consider one habitat patch whose occupancy alternates between present (state 1) and absent (state 0). In season \(i\), colonization \(0\to1\) has rate \(c_i>0\), extinction \(1\to0\) has rate \(e_i>0\), and the season lasts \(T_i>0\). Let \(q_i=c_i/(c_i+e_i)\) be its isolated equilibrium occupancy and \(u_i=\exp[-(c_i+e_i)T_i]\in(0,1)\). A given ordering of seasons is repeated indefinitely. Write \(E(i_1\cdots i_n)\) for the expected number of extinction events in one complete period of the **unique periodically stationary process**. Expected colonizations equal expected extinctions over a stationary period.

**Theorem (sharp onset of order-dependent turnover).** For any positive rates and durations:

1. The expected turnover is unchanged if the cyclic order is reversed. Consequently **every permutation of at most three seasons has exactly the same expected turnover**, even when its periodically stationary occupancy profile differs.
2. Four seasons can have different turnover. Let \(R=\prod_{i=1}^4(1-u_i)/(1-\prod_{i=1}^4u_i)>0\). For labeled seasons \(1,2,3,4\),
   \[
   E(1234)-E(1324)=-R(q_1-q_4)(q_2-q_3),
   \]
   \[
   E(1234)-E(1243)=R(q_1-q_2)(q_3-q_4).
   \]
   Every four-season permutation belongs to exactly one of the three cyclic/reversal equivalence classes represented by \(1234\), \(1324\), and \(1243\).
3. In particular, if \(q_1<q_2<q_3<q_4\), then
   \[
   E(1324)>E(1234)>E(1243).
   \]
   Thus **alternating** the two lower and two higher equilibrium-occupancy seasons maximizes turnover, whereas **grouping** the lower pair and the higher pair minimizes it. The two successive, strictly positive gaps are exactly
   \[
   E(1324)-E(1234)=R(q_4-q_1)(q_3-q_2),
   \]
   \[
   E(1234)-E(1243)=R(q_2-q_1)(q_4-q_3).
   \]
   This ranking holds for arbitrary positive season durations and total transition rates, not just equal-length seasons.

An additional exact energy identity states that, upon changing time to \(z=\int_0^t(c+e)\,ds\), of total transformed period length \(L\), and periodically extending \(q(z)=c(z)/(c(z)+e(z))\),
\[
E=\int_0^Lq(z)[1-q(z)]\,dz
+\frac12\int_0^\infty e^{-v}\int_0^L[q(z)-q(z-v)]^2\,dz\,dv.
\]
The second term is strictly positive whenever two occupied-duration seasons have different equilibrium occupancies. It measures the excess turnover caused by seasonal changes above the integrated within-season equilibrium flux.

## Assumptions and scope
A season is a positive-duration time interval with constant, strictly positive transition rates between the two site-occupancy states. The same finite list of blocks repeats forever, in the selected cyclic order. Individual patches are statistically independent only if interpreting the result per patch across a population; **independence is not required for the one-patch expectation**. The quantity optimized is the expected actual count of \(1\to0\) jumps in the unique periodically stationary continuous-time Markov process, not the number of differences between sparse annual census observations, nor a finite-time transient from an arbitrary prescribed initial occupancy. There are no direct interactions between patches or feedback of regional occupancy on the rates.

Strict inequalities in the four-season ranking require four strictly ordered \(q_i\). At ties the displayed identities still hold, but rankings need not be strict. Rates/durations and occupancies are finite, with \(0<q_i,u_i<1\). The complete scalar process is determined by its occupancy probability \(p(t)\), satisfying \(\dot p=c(1-p)-ep\).

## Proof
**1. Unique periodic state and turnover integral.** Write \(k_i=c_i+e_i\), \(r_i=1-u_i\). On season \(i\), the occupancy probability obeys \(\dot p=k_i(q_i-p)\), so the exact season map is \(F_i(x)=u_i x+r_iq_i\). A complete-period map has contraction multiplier \(U=\prod_i u_i\in(0,1)\), hence a unique fixed point in \((0,1)\). Iterating any initial occupancy converges to this periodically stationary state. Over a stationary cycle, integrating \(\dot p=c(1-p)-ep\) gives equal mean colonizations and extinctions.

**2. Exact nonnegative excess and reversal.** Set \(z=\int_0^t k(s)\,ds\), so that \(dp/dz=q-p\) on a period of length \(L=\sum_i k_iT_i\). The expected extinction count becomes \(E=\int_0^L(1-q)p\,dz\). Since \(p=q-p'\) and \(\int_0^Lp'\,dz=0\), integration by parts at this level (no differentiation of the discontinuous input is necessary) yields
\[
E=\int_0^Lq(1-q)\,dz+\int_0^Lq(q-p)\,dz.
\]
The unique periodic solution of \(p'+p=q\) is the absolutely convergent causal convolution \(p(z)=\int_0^\infty e^{-v}q(z-v)\,dv\). Therefore, by Tonelli's theorem and periodic translation invariance,
\[
\int_0^Lq(q-p)\,dz
=\frac12\int_0^\infty e^{-v}\int_0^L[q(z)-q(z-v)]^2\,dz\,dv.
\]
The integrand is nonnegative; because \(e^{-v}>0\), its integral vanishes if and only if the periodic piecewise-constant \(q\) is almost everywhere constant. Reversing the season order transforms \(q(z)\) into a translate of \(q(-z)\); under \(z\mapsto-z\), periodic translation invariance gives the same inner squared-difference integral. The equilibrium-flux integral is also invariant. This proves reversal invariance for any number of seasons. Cyclic rotation only shifts the periodic input and its stationary response in time, so it preserves \(E\). The dihedral group of a triangle already contains all six permutations, proving complete three-season order invariance.

**3. Exact four-season exchange identities.** For the ordered list \((i_1,i_2,i_3,i_4)\), denote the occupancy immediately before season \(i_j\) by \(p_j\). The recurrence \(p_{j+1}=u_{i_j}p_j+r_{i_j}q_{i_j}\) and periodicity give the explicit initial value
\[
p_1=\frac{\sum_{j=1}^{4}r_{i_j}q_{i_j}\prod_{h=j+1}^{4}u_{i_h}}{1-U}.
\]
The number of extinctions on season \(i_j\), found by directly integrating the exponential occupancy, is
\[
 e_{i_j}\int_0^{T_{i_j}}p(t)\,dt
=e_{i_j}q_{i_j}T_{i_j}+(1-q_{i_j})r_{i_j}(p_j-q_{i_j}).
\]
Using \(p_{j+1}-p_j=r_{i_j}(q_{i_j}-p_j)\) and \(\sum_j(p_{j+1}-p_j)=0\), this gives the exact algebraic formula
\[
E(i_1i_2i_3i_4)=B+\sum_{j=1}^4q_{i_j}r_{i_j}(q_{i_j}-p_j),
\quad B=\sum_{i=1}^4e_iq_iT_i.
\]
All cyclic arrangements share the same \(B\) and \(U\). Substituting the displayed \(p_1\) into the recurrence and this sum, and collecting factors, gives **two exact polynomial identities**:
\[
(1-U)[E(1234)-E(1324)]
=-r_1r_2r_3r_4(q_1-q_4)(q_2-q_3),
\]
\[
(1-U)[E(1234)-E(1243)]
=r_1r_2r_3r_4(q_1-q_2)(q_3-q_4).
\]
These are algebraic identities in the eight independent variables \(q_i,u_i\); no limiting argument or empirical fitting enters. They can be reproduced exactly from the recurrence with the accompanying symbolic identity checker, which expands both differences as rational functions in eight independent variables and reduces their numerators to zero. The standard-library rational verifier additionally tests sampled parameter choices; neither script is used in place of the displayed derivation. Dividing by \(1-U>0\) proves the stated differences.

Every permutation of four distinct labels lies in precisely one of three dihedral classes (eight elements each). By the first part, its turnover equals that of that class's representative. When \(q_1<q_2<q_3<q_4\), each pair of factors in the two identities is strictly positive before the indicated signs are applied, yielding the unique maximizing, intermediate and minimizing classes. The positive gaps show that **four is the minimum number of distinct seasonal blocks** for order-sensitive expected turnover in this model.

## Verification
The accompanying \(\texttt{verify.py}\) uses only Python's standard library and computes all season maps and flux excesses with exact rational arithmetic. Running \(\texttt{python verify.py}\) produced: \(1080\) exact rational parameter-set checks for nonnegative excess, arbitrary-length reversal invariance (one through nine seasons), three-season permutation equality, and the two four-season exchange identities, followed by checks of all \(24\) four-block permutations of the worked example. The optional symbolic checker also completed exact cancellation of both polynomial identity numerators. The finite checks supplement but do not replace the analytical proof.

**Worked example.** Take \(k_i=c_i+e_i=1\), \(T_i=\log 2\), and \((q_1,q_2,q_3,q_4)=(1/5,2/5,3/5,4/5)\). Then \(u_i=1/2\), \(R=1/15\) and the common equilibrium-flux contribution is \(B=(4/5)\log2\). The three order classes have exact expected extinction counts
\[
E(1243)=\frac45\log2+\frac3{25},\qquad
E(1234)=\frac45\log2+\frac{46}{375},\qquad
E(1324)=\frac45\log2+\frac{49}{375}.
\]
Hence the maximizing arrangement exceeds the minimum by exactly \(4/375\) expected extinctions per patch per cycle. The absolute number of events can be nonintegral because it is an expectation.

## Relationship to prior work
Brown and Kodric-Brown's 1977 island-biogeography work makes colonization, extinction and species turnover central ecological quantities. MacKenzie et al. (2003) and Hines et al. (2014) formulate dynamic site-occupancy models in terms of seasonal colonization and extinction probabilities, including imperfect detection. Yackulic et al. (2015) analyze the consequences of environment-dependent local colonization and extinction for occupancy trajectories. The present result addresses a different quantity and assumption regime: actual **continuous-time jump counts** on the unique periodically stationary site, under reordering of the same prescribed seasonal blocks. No detection model is involved.

Rahav, Horowitz and Jarzynski (2008) study periodically driven Markov processes and net signed probability currents. Their no-pumping result constrains **net** flows, whereas this theorem compares the sum of one-way transition events, whose net signed current is always zero on a two-state periodic cycle. The time-reversal part also has a classical linear-response interpretation: it follows from symmetry of a squared-difference autocorrelation. The substantive claim is the **sharp three-to-four-season distinction and complete four-season ranking with explicit positive gaps**; originality is not claimed for the underlying Markov or convolution equations.

## Limitations
The result assumes fixed positive Markov rates within each season, independent of the occupancy probability elsewhere in the habitat network; it does not cover nonlinear rescue effects, demographic interactions, hidden states, non-Markov residence times, or imperfect observation. It describes long-run periodic expected jump counts, not finite-horizon turnover from a given initial state, higher moments, or observed census turnover. General rearrangement or linear-filter energy results could imply the four-block formula without using the same ecological terminology. Searches and primary-text comparisons found no explicit preceding four-season classification; absence of a match is not proof of publication priority. The finite verification script alone cannot certify any assertion for a continuum of parameters.

## References
- Brown, J. H. and Kodric-Brown, A. (1977), *Turnover Rates in Insular Biogeography: Effect of Immigration on Extinction*, Ecology 58, 445–449. DOI: 10.2307/1935620. First published 1977-03-01.
- MacKenzie, D. I., Nichols, J. D., Hines, J. E., Knutson, M. G. and Franklin, A. B. (2003), *Estimating site occupancy, colonization, and local extinction when a species is detected imperfectly*, Ecology 84, 2200–2207. DOI: 10.1890/02-3090.
- Hines, J. E., Nichols, J. D. and Collazo, J. A. (2014), *Multiseason occupancy models for correlated replicate surveys*, Methods in Ecology and Evolution 5, 583–591. DOI: 10.1111/2041-210X.12186.
- Yackulic, C. B., Nichols, J. D., Reid, J. and Der, R. (2015), *To predict the niche, model colonization and extinction*, Ecology 96, 16–23. DOI: 10.1890/14-1361.1.
- Rahav, S., Horowitz, J. and Jarzynski, C. (2008), *Directed flow in non-adiabatic stochastic pumps*, Physical Review Letters 101, 140602. arXiv:0808.0015; DOI: 10.1103/PhysRevLett.101.140602.
