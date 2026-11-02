# Four-type stochastic domination for the sibling coupon collector

## Finding
Let \(p=(p_1,p_2,p_3,p_4)\) be any strictly positive probability vector. Draw independent coupon types with replacement, stop at the first time every type has appeared, and let \(U(p)\) count those types that have appeared exactly once at this stopping time. Equivalently, \(U\) is the number of missing entries in the second collector's album in the siblings coupon-collector model. With \(u=(1/4,1/4,1/4,1/4)\),
\[
 \Pr_p\{U(p)\ge k\}\le\Pr_u\{U(u)\ge k\},\qquad k=1,2,3,4.
\]
If \(p\ne u\), then the inequality is strict for \(k=3\); consequently equality of the two distributions holds if and only if \(p=u\). The exact uniform law, in order \(U=1,2,3,4\), is \((97,97,67,27)/288\). The two nontrivial interior upper tails have values \(191/288\) at \(k=2\) and \(47/144\) at \(k=3\), and the final tail is \(3/32\) at \(k=4\).

The new ingredient is the exact four-type middle-tail inequality
\[
 T(p):=\Pr_p\{U(p)\ge3\}\le 47/144,
\]
with equality precisely for the uniform law. The first and final upper-tail inequalities follow from independently established transform extremality and the arithmetic-geometric mean inequality, respectively.

## Assumptions and scope
The vector \(p\) is arbitrary in the open four-dimensional probability simplex (four entries, one sum constraint). Coupons are independent across draws. All stopping times are finite almost surely because every \(p_i>0\). Only the second collector and exactly four coupon types are addressed. Stochastic dominance here refers to ordinary first-order comparison at *all* integer thresholds, not just probability generating functions, moments, or asymptotic tails. Primary classification: MSC2020 60C05.

## Proof
**1. Exact Poissonized coefficient formula.** Give type \(i\) an independent rate-\(p_i\) Poisson process. Their superposition has iid type labels distributed as \(p\), so the coupon multiplicities at the last first arrival agree with the discrete model. The final first-arriving type always contributes one to \(U\). Conditioning on that type and its arrival time gives the identity [Long, Proposition 2.1]
\[
 G_p(z):=\mathbb E_p[z^U]
 =z\sum_{k=1}^{4}\int_0^\infty p_k e^{-p_kt}
 \prod_{i\ne k}\bigl(1-e^{-p_it}+(z-1)p_it e^{-p_it}\bigr)\,dt.
\]
Expand \(G_p(z)/z=\sum_{m=0}^3 C_m(p)(z-1)^m\). In each product choose \(m\) marked factors, expand the remaining unmarked factors by inclusion-exclusion, and integrate \(\int_0^\infty t^m e^{-bt}\,dt=m!/b^{m+1}\). Writing \(A_i=\prod_{j\ne i}p_j\) and \(e_3=\sum_iA_i\), the two coefficients needed here are
\[
 C_2(p)=6\sum_{i=1}^4\frac{A_i}{(1-p_i)^3}-6e_3,
 \qquad C_3(p)=24\prod_{i=1}^4p_i.
\]
Indeed, for \(C_2\), the inclusion-exclusion subsets consist of the four three-element subsets, each contributing \(6A_i/(1-p_i)^3\), and the full four-element subset, contributing \(-6e_3\). For \(C_3\), only the full set contributes, and its integral is \(4!\prod_i p_i\). Since \(U-1\in\{0,1,2,3\}\), \(C_m=\mathbb E\binom{U-1}{m}\), whence
\[
 T(p)=C_2(p)-2C_3(p)
 =6\sum_{i=1}^4\frac{\prod_{j\ne i}p_j}{(1-p_i)^3}
 -6\sum_{i=1}^4\prod_{j\ne i}p_j
 -48\prod_{i=1}^4p_i.\tag{1}
\]
This evaluates to \(47/144\) when all probabilities are \(1/4\).

**2. A finite, exact positivity certificate for the middle tail.** By permutation symmetry take unnormalized ordered positive weights
\[
(a_1,a_2,a_3,a_4)=(r,r+v,r+v+w,r+v+w+z),
 \qquad r>0,\ v,w,z\ge0,
\]
and write \(S=\sum_i a_i\), \(B_i=S-a_i\), \(A_i=\prod_{j\ne i}a_j\), \(E_3=\sum_iA_i\), \(E_4=\prod_i a_i\), and \(Q=\prod_i B_i^3\). Every denominator is positive. From (1), with \(p_i=a_i/S\), a direct common-denominator calculation gives
\[
\begin{aligned}
P(r,v,w,z):={}&144S^4Q\bigl(47/144-T(p)\bigr)\\
={}&47S^4Q-864S^4\sum_i A_i\prod_{j\ne i}B_j^3\\
&+864S E_3Q+6912E_4Q.\tag{2}
\end{aligned}
\]
Equation (2) is an identity in integers after substituting the ordered weights. Expanding into monomials \(r^\alpha v^\beta w^\gamma z^\delta\) gives a homogeneous degree-16 polynomial with **exactly 955 nonzero monomials, every coefficient a positive integer**, and smallest nonzero coefficient \(47\). The complete list of exponents and integer coefficients is `certificate.tsv`. The standalone standard-library program `verify_certificate.py` independently regenerates the rational identity's denominator-cleared polynomial from (2), enumerates *all* nonzero coefficients using exact integer operations, checks that each is positive, and compares every one against the table. In particular, the coefficients of \(r^{14}v^2\), \(r^{14}w^2\), and \(r^{14}z^2\) are respectively \(1598574528\), \(2131432704\), and \(1598574528\). Thus \(P>0\) whenever at least one of \(v,w,z\) is nonzero; at \(v=w=z=0\), \(P=0\). By positive denominator in (2), \(T(p)\le47/144\) with equality exactly at uniform. This is a complete finite symbolic positivity proof, not inference from finite samples or numerical optimization.

**3. The other three thresholds.** The event \(U\ge1\) has probability one, because the final coupon is observed exactly once. Long's Theorem 2.2 proves \(G_p(z)\ge G_u(z)\) for every \(0<z<1\). Dividing by \(z>0\), then taking \(z\downarrow0\), gives \(\Pr_p(U=1)\ge\Pr_u(U=1)=97/288\); therefore \(\Pr_p(U\ge2)\le191/288\). Finally \(\Pr_p(U=4)=4!\prod_i p_i\le 4!/4^4=3/32\) by the arithmetic-geometric mean inequality. This establishes all ordinary upper-tail inequalities. The strict \(k=3\) inequality also proves the asserted uniqueness.

## Verification
Run `python3 verify_certificate.py` alongside `certificate.tsv` using only the Python standard library. The recorded reproducible result is `CERTIFICATE_OK; positive_terms=955; min_coeff=47; uniform_middle_tail=47/144; assertions=1942`. The program checks 955 integer degrees, 955 strict coefficient signs, the three strictness witnesses, all 955 tabulated coefficients, eight independent exact-rational checks of the formula (1) against the last-arrival integral expanded without using (1), and the four uniform point probabilities. The finite certificate is exhaustive for polynomial (2), while the analytic last-arrival identity and the probability-generating-function comparison are justified in the proof above and the cited source. The test vectors do not purport to exhaust the continuum of probability distributions.

## Relationship to prior work
Doumas and Spektor (2026) proved strict uniform extremality for the *expected* sibling deficit. Long (2026, Proposition 2.1, Theorem 2.2, and Theorem 5.3) proved an exact Poissonized generating-function formula, radial left- and right-PGF comparisons, and binomial-moment extremality for arbitrary numbers of types. Long explicitly states in Remark 5.6 that these results **do not imply ordinary stochastic order** and leaves that strengthening open. The \(k=2\) and \(k=4\) cases above are already implied by Long's transform comparison and the elementary product bound; the proof's substantive new mathematical step is the first interior tail at four types, \(k=3\). Earlier work by Doumas and Papanicolaou and the companion Long paper concerned sibling deficits and expectation/asymptotic extremality, not this exact four-type ordinary stochastic order. This is not a claim that the full all-type, all-sibling stochastic-order question is resolved.

## Limitations
This result proves global domination against the uniform law for **four types and the second collector only**. It does not claim radial monotonicity between arbitrary points on a line segment, comparison of two different nonuniform vectors, increasing-convex order, or analogous results for five or more types or higher siblings. Historical priority outside the inspected literature is not conclusively established, and independent mathematical review has not been performed. The large positive-coefficient certificate is machine-reproducible using exact arithmetic but is not a short hand-derived factorization.

## References
1. A. V. Doumas and S. Spektor, *Equal probabilities maximize the expected deficit in the siblings of the coupon collector*, arXiv:2606.21591, first public June 19, 2026. https://arxiv.org/abs/2606.21591
2. C. D. Long, *Radial Transform Extremality for the Siblings of the Coupon Collector*, arXiv:2606.31391, first public June 30, 2026; especially Proposition 2.1, Theorem 2.2, Proposition 3.1, Theorem 5.3, Remark 5.6. https://arxiv.org/abs/2606.31391
3. C. D. Long, *Extremality and Limit Laws for the Siblings of the Coupon Collector*, arXiv:2606.29635, first public June 28, 2026. https://arxiv.org/abs/2606.29635
4. A. V. Doumas and V. G. Papanicolaou, *The Siblings of the Coupon Collector*, Theory of Probability and Its Applications 62 (2018), 444–470; arXiv:1412.4346. https://arxiv.org/abs/1412.4346
