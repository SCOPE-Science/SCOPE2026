# Four mortality classes are necessary for two hazard-rank reversals under strict survival ordering

## Finding
Consider two mortality cohorts with the **same** finite list of strictly ordered, positive individual mortality rates \(0<\lambda_1<\cdots<\lambda_m\), but potentially different strictly positive baseline class proportions \(a_i\) and \(b_i\), each summing to one. Each individual remains in its initial class and has an exponential lifetime at its class rate. Let \(S_A,S_B\) be the cohort survival functions and \(h_A=-S_A'/S_A\), \(h_B=-S_B'/S_B\) their population hazards.

**Sharp class-count theorem.** For every choice of common rates and positive class proportions, when \(m\leq3\), the sign of \(h_A(t)-h_B(t)\) can change at most once over \(t>0\). Four shared classes already permit **two and exactly two** strict hazard-rank reversals, even while one cohort has strictly lower survival probability at **every** positive age.

A positive rational witness uses rates \((1,2,3,4)\) and class proportion vectors
\[
(a_1,a_2,a_3,a_4)=\frac1{11}(4,2,1,4),\qquad
(b_1,b_2,b_3,b_4)=\frac18(3,1,3,1).
\]
For these populations, \(S_A(t)<S_B(t)\) for all \(t>0\), whereas \(h_A(t)-h_B(t)\) is positive, then negative, then positive as age increases. The two distinct crossover times are the negatives of the logarithms of the roots in \((0,1)\) of
\[
P(q)=11q^4+4q^3+19q^2-18q+2,
\]
approximately \(0.5423453\) and \(2.0444276\), respectively.

## Assumptions and scope
Each cohort consists of a mixture of \(m\geq1\) fixed, unobserved mortality types. Conditional on class \(i\), an individual lifetime is exponential with rate \(\lambda_i\). The **same** strictly increasing rate list is used for both cohorts, but the initial class weights are arbitrary positive numbers summing to one within each cohort. There is no migration between classes, no exposure-related change of individual rates and no censoring in the mathematical definition. Time is continuous and nonnegative; crossover counts concern distinct zeros at positive ages where the difference changes sign.

The unconditional survival and hazard functions are
\[
S_A(t)=\sum_{i=1}^m a_i e^{-\lambda_i t},\quad
S_B(t)=\sum_{i=1}^m b_i e^{-\lambda_i t},\quad
h_A(t)=\frac{\sum_i\lambda_i a_i e^{-\lambda_i t}}{S_A(t)},\quad
h_B(t)=\frac{\sum_i\lambda_i b_i e^{-\lambda_i t}}{S_B(t)}.
\]
The statement does not assert an upper bound of two crossings for arbitrary numbers of classes. It does not assert that four classes are necessary without the shared-rate condition.

## Proof
**Step 1: An exact crossing numerator.** Positivity of both survival functions gives
\[
\operatorname{sgn}(h_A-h_B)=\operatorname{sgn} N(t),\qquad
N(t)=\sum_{1\le i<j\le m}(\lambda_j-\lambda_i)(a_jb_i-a_ib_j)e^{-(\lambda_i+\lambda_j)t}.
\]
Indeed, this is exactly the numerator obtained by putting the two cohort hazards over the positive denominator \(S_A(t)S_B(t)\). No approximation or asymptotic argument is involved.

**Step 2: At most one reversal with three classes.** When \(m\le2\), the numerator has at most one nonzero exponential term and cannot change sign. When \(m=3\), put \(r_i=a_i/b_i>0\). The three coefficients of \(N(t)\), ordered by their strictly increasing exponent sums \(\lambda_1+\lambda_2<\lambda_1+\lambda_3<\lambda_2+\lambda_3\), have respective signs
\[
\operatorname{sgn}(r_2-r_1),\quad
\operatorname{sgn}(r_3-r_1),\quad
\operatorname{sgn}(r_3-r_2).
\]
After deleting any zero coefficients, this sign sequence cannot be \((+,-,+)\) or \((-,+,-)\), since either pattern contradicts transitivity of the real-number ordering of the three ratios. Hence it has at most one change of sign.

For completeness, an exponential sum \(\sum_j c_j e^{-\alpha_jt}\) with strictly ascending exponents and coefficients changing sign at most once has at most one real zero: if the positive coefficients precede the negative coefficients, multiply by \(e^{\alpha_k t}\), where \(k\) is the last positive position. Every resulting positive term is nondecreasing and every negative term is increasing (toward zero), so the transformed sum is strictly increasing except in the trivial no-crossing cases. Reversing all coefficient signs handles the opposite order. Consequently, \(N(t)\) and the hazard difference can have no more than one strict reversal on \(t>0\). This proves the universal lower bound \(m\ge4\).

**Step 3: Strict survival ordering in an exact four-class witness.** Set \(q=e^{-t}\) so \(0<q<1\) for \(t>0\), and write
\[
A(q)=4+2q+q^2+4q^3,\qquad B(q)=3+q+3q^2+q^3.
\]
Then \(S_A(t)=qA(q)/11\), \(S_B(t)=qB(q)/8\). Direct integer arithmetic yields
\[
88q^{-1}(S_A-S_B)=8A(q)-11B(q)
=(q-1)(21q^2-4q+1).
\]
The quadratic has discriminant \(-68<0\), positive leading coefficient and thus is strictly positive for real \(q\); since \(q-1<0\), the survival difference is strictly negative at every positive age.

**Step 4: Exactly two hazard reversals.** Differentiating the survival polynomials gives
\[
h_A(t)-h_B(t)=\frac{q\{A'(q)B(q)-A(q)B'(q)\}}{A(q)B(q)}
=\frac{qP(q)}{A(q)B(q)},
\]
where
\[
P(q)=11q^4+4q^3+19q^2-18q+2.
\]
The denominator is strictly positive for \(0<q<1\). Exactly two coefficient sign changes occur in \(P\) (in descending or ascending degree), so Descartes' rule bounds the number of positive roots, with multiplicity, by two. Yet \(P(0)=2>0\), \(P(1/5)=-494/625<0\), and \(P(1)=18>0\), giving one root in \((0,1/5)\) and another in \((1/5,1)\). These are two distinct simple roots, the only positive roots. Because \(q=e^{-t}\) decreases strictly from one toward zero, the hazard difference is positive, negative and positive on the consecutive age intervals determined by these roots. This proves existence and completes the sharpness claim.

## Verification
The standalone `CHECK.py` uses only Python's standard-library exact rational arithmetic. It verifies the four-class survival and hazard polynomial expansions, the exact factorization for survival dominance, and the rational sign brackets certifying two distinct positive roots. Run `python CHECK.py` from the extracted package directory. The general three-class statement and the global root-count arguments rest on the analytic proof above, not on a finite sample of parameter vectors or numerical root finding.

## Relationship to prior work
Mixture hazards and survivor selection are classical. Proschan's 1963 explanation of decreasing failure rates motivates the distinction between individual and aggregate hazards. The fully accessible discussion of Vaupel and Missov (published publicly on 17 September 2014), particularly Sections 3A, 3D, 4A–4F and 5E, supplies the general mixture-hazard and fixed-frailty framework; its gamma-frailty comparison includes a single marginal-hazard crossover in a different parameterization, but its examined sections do not state the sharp three-versus-four discrete shared-support rule or this strict-survival-order witness. Boland, Proschan and Tong (1989) study variation-diminishing properties of mixture **densities**; these are important possible broader mathematical predecessors, but the accessible abstract does not specify the present hazard-ratio comparison. The precise full-text implication is unresolved, not certified absent. Gupta and Kirmani (2006) compare stochastic orderings of frailty models; accessible descriptive text does not settle this class-count result. The four-class construction is a concrete crossing certificate independent of any bibliographic novelty assertion.

## Limitations
The theorem concerns exact deterministic population survival curves under fixed classes and a shared finite rate list. It is not a statement about empirical hazard estimates, confidence intervals, causal treatment effects, or observed age-specific rates under changing exposures. Two age crossings in finite data may be due to noise or misspecification. The number of latent classes is a model dimension, not directly identifiable from a pair of noisy hazard curves alone. Broader total-positivity and hazard-order literature could contain an equivalent general theorem; independent historical-priority assessment is not performed.

## References
- Vaupel, J. W. and Missov, T. I. (2014), *Unobserved population heterogeneity: A review of formal relationships*, Demographic Research 31, 659–686. Publicly published 17 September 2014. DOI: https://doi.org/10.4054/DemRes.2014.31.22 . Full public text: https://www.researchgate.net/publication/263844831_Unobserved_population_heterogeneity_A_review_of_formal_relationships .
- Boland, P. J., Proschan, F. and Tong, Y. L. (1989), *Crossing Properties of Mixture Distributions*, Probability in the Engineering and Informational Sciences 3(3), 355–366. DOI: https://doi.org/10.1017/S0269964800001224 . The accessible journal record documents the July 1989 issue; no exact 1989 public-release day was assumed.
- Gupta, R. C. and Kirmani, S. N. U. A. (2006), *Stochastic comparisons in frailty models*, Journal of Statistical Planning and Inference 136(10), 3647–3658. DOI: https://doi.org/10.1016/j.jspi.2005.02.020 .
- Proschan, F. (1963), *Theoretical Explanation of Observed Decreasing Failure Rate*, Technometrics 5(3), 375–383. DOI: https://doi.org/10.1080/00401706.1963.10490105 .
