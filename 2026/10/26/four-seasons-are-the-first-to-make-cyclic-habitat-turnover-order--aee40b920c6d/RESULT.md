# Four seasons are the first to make cyclic habitat turnover order-sensitive

## Finding
Consider a two-state habitat patch with season-specific colonization rates \(c_i>0\), extinction rates \(e_i>0\), and durations \(T_i>0\). A finite list of seasons repeats in a fixed order. Write \(q_i=c_i/(c_i+e_i)\), \(u_i=\exp[-(c_i+e_i)T_i]\), and let \(E(i_1\cdots i_n)\) be the expected number of actual extinction jumps per period in the unique periodically stationary process. The expected number of colonization jumps is the same.

1. Reversing or cyclically rotating any number of seasons preserves \(E\). Thus every permutation of at most three seasons has the same \(E\), though the periodic occupancy profiles can differ.
2. For four labeled seasons, let \(R=\prod_i(1-u_i)/(1-\prod_i u_i)\). Then
   \[
   E(1234)-E(1324)=-R(q_1-q_4)(q_2-q_3),\qquad
   E(1234)-E(1243)=R(q_1-q_2)(q_3-q_4).
   \]
   These three orders represent all cyclic/reversal classes.
3. If \(q_1<q_2<q_3<q_4\), then \(E(1324)>E(1234)>E(1243)\). Alternating the two lower and two higher occupancies maximizes turnover. **Both** other classes group the two lower and the two higher occupancies, but grouping alone does not characterize the minimum: the minimizing class is \(1243\), with cross-group adjacent pairs \(\{1,3\}\) and \(\{2,4\}\); the intermediate class \(1234\) has pairs \(\{1,4\}\) and \(\{2,3\}\). The two positive successive gaps, from largest to smallest turnover, are \(R(q_4-q_1)(q_3-q_2)\) and \(R(q_2-q_1)(q_4-q_3)\). Hence four blocks are the minimum needed for order sensitivity to be possible, with no equal-duration or equal-rate constraint.

In the transformed clock \(z=\int_0^t(c+e)\,ds\), let \(L\) denote the period and extend \(q(z)=c(z)/(c(z)+e(z))\) periodically. The same expected count satisfies
\[
E=\int_0^L q(z)[1-q(z)]\,dz+\frac12\int_0^\infty e^{-v}\int_0^L[q(z)-q(z-v)]^2\,dz\,dv .
\]
The excess term is strictly positive exactly when the equilibrium occupancies are not all equal.

## Assumptions and scope
All seasons have strictly positive duration and strictly positive constant Markov transition rates. There is no feedback into those rates. The claim concerns the expectation for one periodically stationary patch; it does not require independence among patches elsewhere. It does not concern finite-time transients, higher moments, or differences inferred from sparse observations. The four-block identities apply also at ties, where one or both strict inequalities can become equalities.

## Proof
**Periodic state and reversal.** The occupancy probability satisfies \(dp/dt=c(1-p)-ep\). With \(r_i=1-u_i\), its season map is \(p\mapsto u_i p+r_i q_i\). A complete period has contraction multiplier \(U=\prod_i u_i\in(0,1)\) and a unique periodic stationary occupancy. Integrating the occupancy equation over a period shows equality of the expected colonization and extinction counts.

In the transformed clock \(p'=q-p\) and \(E=\int_0^L(1-q)p\,dz\), by integrating the intensity of extinction jumps. Using \(p=q-p'\) and \(\int_0^L p'\,dz=0\) gives the equilibrium baseline plus \(\int_0^L q(q-p)\,dz\). The unique periodic solution is \(p(z)=\int_0^\infty e^{-v}q(z-v)\,dv\). Periodic translation invariance gives \(\int q(z)^2\,dz=\int q(z-v)^2\,dz\) on a period, so expansion of the squared difference in the Finding gives exactly the excess. Its integral is strictly positive for nonconstant \(q\): on \(v\in[0,L]\), the weight is bounded below by \(e^{-L}\), and the unweighted double integral there is \(2L\int_0^L(q-\overline q)^2\,dz\). The inner integral is invariant under reflection of \(q\), because reflection reverses the lag and the change of lag sign is just a periodic translation. Reversing season order reflects \(q\) up to translation. Rotation also just translates the periodic forcing. These operations exhaust the permutations for at most three labels.

**Four-block differences.** Let \(p_j\) be the stationary occupancy just before label \(j\). Integrating on each season gives equilibrium baseline \(B=\sum_i e_i q_i T_i\) plus \(\sum_j(1-q_j)r_j(p_j-q_j)\). Since \(\sum_j r_j(q_j-p_j)=0\), the excess is \(\sum_j q_j r_j(q_j-p_j)\). Unroll the stationary recurrence once around the cycle: the coefficient of \(q_i\) in \((1-U)p_j\) for distinct labels \(i,j\) is \(r_i\) times the product of the \(u\)'s strictly between \(i\) and \(j\) in forward cyclic order. The self-coefficient is \(r_j\prod_{i\ne j}u_i\), independent of order. Thus the cross term for the unordered pair \(i,j\) in \((1-U)(E-B)\) is \(-r_i r_j q_i q_j\) times the sum of the products on the two open arcs between \(i,j\). For four labels with remaining pair \(a,b\), the arc sum is \(1+u_a u_b\) if \(i,j\) are adjacent and \(u_a+u_b\) otherwise. Their difference is \(r_a r_b\).

Between \(1234\) and \(1324\), the first order has exclusive adjacent pairs \(12,34\) and the second \(13,24\); the difference in \(E\) is \(-R(q_1q_2+q_3q_4-q_1q_3-q_2q_4)\). Between \(1234\) and \(1243\), the exclusive adjacent pairs are \(23,14\) and \(24,13\), respectively; the difference is \(-R(q_2q_3+q_1q_4-q_2q_4-q_1q_3)\). Factoring gives both identities. There are three dihedral classes, since the 24 orders of distinct labels fall into classes of eight. As \(R>0\), strict ordering of the occupancies gives the ranking and gaps in the Finding.

## Verification and example
The accompanying standard-library `verify.py` uses exact rational arithmetic to check the recurrence and flux excess on 1080 rational parameter sets and on all 24 orders of a worked example. The optional SymPy `symbolic_check.py` expands the recurrence to check both identities in independent \(q_i,u_i\); these checks supplement the proof. For \(c_i+e_i=1\), \(T_i=\log 2\), and \(q_i=i/5\), the common baseline is \((4/5)\log 2\) and the three excesses for \(1243,1234,1324\) are \(3/25,46/375,49/375\), respectively. The maximum exceeds the minimum by \(4/375\) expected jumps per patch per period.

## Relationship to prior work and limitations
Ecological occupancy and species-turnover literature motivates colonization–extinction models, often from seasonal observation with imperfect detection. The analysis here uses actual continuous-time jump counts under reordering of prescribed seasons. Periodic stochastic-pump work on signed currents studies a different statistic: net signed flow in a two-state periodic cycle is zero and does not determine the unsigned activity. The reversal symmetry is an autocorrelation identity; the finite classification concerns the first order-sensitive length and all three four-label classes. The theory is not a field-data result or a priority claim, and it does not address nonlinear rescue, higher-state or non-Markov models, or optimal arrangements of arbitrarily many seasons.

## References
- Brown and Kodric-Brown (1977), *Turnover Rates in Insular Biogeography: Effect of Immigration on Extinction*, DOI: 10.2307/1935620.
- MacKenzie et al. (2003), *Estimating site occupancy, colonization, and local extinction when a species is detected imperfectly*, DOI: 10.1890/02-3090.
- Hines, Nichols and Collazo (2014), *Multiseason occupancy models for correlated replicate surveys*, DOI: 10.1890/13-0907.1.
- Yackulic et al. (2015), *To predict the niche, model colonization and extinction*, DOI: 10.1890/14-1361.1.
- Rahav, Horowitz and Jarzynski (2008), *Directed flow in non-adiabatic stochastic pumps*, arXiv:0808.0015, DOI: 10.1103/PhysRevLett.101.140602.
