# A sharp five-category Poisson-binomial threshold for three-draw richness

## Finding
Let \(X_1,X_2,X_3\) be independent draws from one categorical law supported on at most \(m\) labels, and let \(K=|\{X_1,X_2,X_3\}|\) be the number of distinct labels seen. If \(m\le5\), there exist independent (possibly degenerate) Bernoulli random variables \(B_1,B_2\) such that
\[
K\ \stackrel{d}{=}\ 1+B_1+B_2.
\]
This maximum alphabet size is sharp for a universal statement: when \(m=6\), the law with weights \(5/6,1/30,1/30,1/30,1/30,1/30\) has no such representation. The same failure is possible for every alphabet size at least six, by appending zero masses (or by sufficiently small positive perturbations when full support is required).

## Assumptions and scope
The three observations are identically distributed **and independent**; category probabilities are arbitrary nonnegative real numbers summing to one. Labels of zero mass may be removed. This result concerns three draws only, not arbitrary sample sizes; independent Bernoulli summands in the distributional representation need not coincide with individual occupied-label indicators. A shifted Poisson-binomial law here means the distribution of one plus two independent Bernoulli variables with probabilities in \([0,1]\).

## Proof
Write \(p_1,\ldots,p_m\) for the category probabilities and \(u=\sum_i p_i^2\), \(v=\sum_i p_i^3\). The probabilities of observing respectively one, two, or three distinct labels are exactly
\[
a=v,\qquad b=3(u-v),\qquad c=1-3u+2v.
\]
Indeed, \(a\) counts three equal outcomes, \(b\) counts the three choices for the singleton in a two-equal outcome, and the rest have three distinct labels. Thus \(a,b,c\ge0\), \(a+b+c=1\), and the probability-generating polynomial of \(K-1\) is \(F(z)=a+bz+cz^2\). Such a polynomial is a product of two Bernoulli probability-generating factors if and only if its discriminant \(\Delta=b^2-4ac\) is nonnegative: because its coefficients are nonnegative, all real zeros must be nonpositive; normalization \(F(1)=1\) then gives the required Bernoulli factors. The linear and constant cases are covered by degenerate factors.

Substitution gives
\[
\Delta=9u^2-6uv+v^2-4v=(3u-v)^2-4v.
\]
For fixed \(u\), this expression is strictly decreasing in \(v\), because \(\partial\Delta/\partial v=2v-6u-4<0\) whenever \(0\le v\le u\le1\). Hence it suffices to maximize \(v\) at each allowed value of \(u\).

For \(m\le5\), pad the probability list with zeros to obtain five coordinates. Put \(y_i=p_i-1/5\), so that \(\sum_i y_i=0\) and \(R^2=\sum_i y_i^2=u-1/5\), with \(0\le R^2\le4/5\). The following sharp centered-cubic inequality holds for all five real coordinates summing to zero:
\[
\sum_{i=1}^5 y_i^3\le\frac{3}{\sqrt{20}}R^3. \tag{1}
\]
For \(R=0\) this is immediate. For fixed \(R>0\), the sphere in the zero-sum hyperplane is compact and smooth. At a maximum of the cubic, Lagrange multipliers give \(3y_i^2=\lambda+2\mu y_i\) for each coordinate, so there are at most two distinct coordinate values. Suppose \(k\) coordinates take the larger value and \(5-k\) the smaller value. The zero-sum and norm constraints force
\[
\sum_i y_i^3=\frac{5-2k}{\sqrt{5k(5-k)}}R^3,
\qquad k\in\{1,2,3,4\}.
\]
The largest of these four values occurs for \(k=1\), yielding (1). This proves the critical extremal inequality without assuming nonnegativity of the centered coordinates.

Expanding the third powers now yields
\[
v=\frac1{25}+\frac35R^2+\sum_i y_i^3
\le\frac1{25}+\frac35R^2+\frac3{\sqrt{20}}R^3.
\]
The upper bound is attained by a one-heavy/four-equal probability vector
\[
q(t)=(1-4t,t,t,t,t),\qquad 0\le t\le\frac15,
\]
whose squared-mass sum is \(u(q(t))=1-8t+20t^2\). As \(t\) runs from \(0\) to \(1/5\), this function runs continuously and strictly down from \(1\) to \(1/5\), so **for every feasible value of \(u\)** the corresponding \(q(t)\) has the same \(u\) and maximizes \(v\). Since \(\Delta\) decreases in \(v\), \(\Delta(p)\ge\Delta(q(t))\).

Direct polynomial expansion gives the exact factorization
\[
\Delta(q(t))=48t^3\bigl(75t^3+30t^2-27t+4\bigr).
\]
Set \(H(t)=75t^3+30t^2-27t+4\). On \([0,1/5]\), its derivative \(225t^2+60t-27\) is increasing and at most \(-6\), so \(H\) is decreasing there and
\[
H(t)\ge H(1/5)=\frac25>0.
\]
Consequently \(\Delta(p)\ge0\) for every probability law with no more than five categories, giving the claimed shifted Bernoulli-sum representation.

For six categories choose \(p=(5/6,1/30,1/30,1/30,1/30,1/30)\). Direct exact sums yield
\[
u=\frac7{10},\quad v=\frac{521}{900},\quad
(a,b,c)=\left(\frac{521}{900},\frac{109}{300},\frac{13}{225}\right).
\]
Its discriminant is
\[
\Delta=\left(\frac{109}{300}\right)^2
-4\left(\frac{521}{900}\right)\left(\frac{13}{225}\right)
=-\frac{1439}{810000}<0.
\]
Therefore \(F\) has nonreal conjugate zeros and cannot be a product of Bernoulli generating factors. For an exactly \(m\)-category positive law with \(m>6\), perturb by giving the extra labels arbitrarily small positive masses and proportionally reducing the original six masses. The strict negative discriminant persists by continuity. This proves sharpness.

## Verification
The accompanying standalone standard-library checker `CHECKER.py` reconstructs the stated polynomial factorization by exact rational coefficient arithmetic, verifies the six-category discriminant, and checks 2,997 rational probability vectors and 230 independent three-draw enumerations. These finite checks are diagnostics **only**: the proof of the universal five-category claim is the Lagrange-multiplier extremal inequality and the analytic positivity factorization above. No infinite statement is inferred from enumeration.

## Relationship to prior work
O'Neill's *Three Distributions in the Extended Occupancy Problem* (arXiv:2209.02220, first publicly available 2022-09-06) develops occupancy, hitting-time and spillage laws for uniform bin allocation (possibly with fall-through). In contrast, the present statement concerns arbitrary **unequal** categorical probabilities and an exact real-zero/independent-Bernoulli threshold for three draws. Tang and Tang's *The Poisson Binomial Distribution—Old & New* (arXiv:1908.10024, Theorem 4.1) gives the classical equivalence between Poisson-binomial distributions and real-rooted probability-generating polynomials. That equivalence is used here, but it does not itself establish the five-category discriminant inequality or the six-category obstruction. The cited primary texts were compared for those precise implications; no equivalent sharp occupancy-support threshold was identified in the material examined.

## Limitations
The theorem addresses exactly three iid draws; no claim is made about four or more draws, dependent draws, or nonidentical allocation laws. The six-category counterexample excludes exact Poisson-binomial **equality in distribution**, not approximation or other forms of negative dependence. Source coverage is not exhaustive: unindexed earlier work or an equivalent application of classical coefficient inequalities may predate the result. The finite checker supplements but does not replace the real-parameter proof. No independent external audit has been performed.

## References
1. B. O'Neill, *Three Distributions in the Extended Occupancy Problem*, arXiv:2209.02220 (first public version 2022-09-06); *Methodology and Computing in Applied Probability* **25**, article 84 (2023), DOI:10.1007/s11009-023-10053-y.
2. W. Tang and F. Tang, *The Poisson Binomial Distribution—Old & New*, arXiv:1908.10024 (2019), especially Section 4, Theorem 4.1.
