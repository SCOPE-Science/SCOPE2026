# Independent non-identically distributed observations need not have independent record indicators

## Result

Let \(X_1,X_2,X_3\) be independent, continuously distributed real random variables with cdfs \(F_1,F_2,F_3\). Define the upper-record indicators
\[
I_2=\mathbf 1\{X_2>X_1\},\qquad
I_3=\mathbf 1\{X_3>\max(X_1,X_2)\}.
\]
Then
\[
\Pr(I_2=1)=\int F_1(x)\,dF_2(x),
\]
\[
\Pr(I_3=1)=\int F_1(x)F_2(x)\,dF_3(x),
\]
and
\[
\Pr(I_2=I_3=1)=\int F_1(x)\{1-F_3(x)\}\,dF_2(x).
\]
Consequently, independence of the observations does **not** imply independence of \(I_2\) and \(I_3\). The latter requires the additional identity
\[
\int F_1(1-F_3)\,dF_2
=\left(\int F_1\,dF_2\right)
 \left(\int F_1F_2\,dF_3\right),
\]
which does not hold for general non-identical marginals.

This directly contradicts the universal non-iid independence claim in G. S. Lo and E. H. Babou, *Independence of the indicator functions of record values for Multivariate independent data*, arXiv:2602.20416 (2026), whose abstract and main argument state independence for independent observations without requiring identical distributions, already for \(d=1\).

## An exact one-parameter counterexample family

Take
\[
X_1,X_3\sim \operatorname{Unif}(0,1),\qquad
X_2\sim \operatorname{Unif}(0,a),\qquad a>0,
\]
independently. Put \(p_2=\Pr(I_2=1)\), \(p_3=\Pr(I_3=1)\), and \(c=\Pr(I_2=I_3=1)\).

For \(0<a\le1\), direct integration gives
\[
p_2=\frac a2,\qquad
p_3=\frac12-\frac{a^2}{6},\qquad
c=\frac a2-\frac{a^2}{3},
\]
so
\[
\boxed{\operatorname{Cov}(I_2,I_3)
=\frac{a(a-1)(a-3)}{12}.}
\]
For \(a\ge1\),
\[
p_2=1-\frac1{2a},\qquad
p_3=\frac1{3a},\qquad
c=\frac1{6a},
\]
and therefore
\[
\boxed{\operatorname{Cov}(I_2,I_3)
=\frac{1-a}{6a^2}.}
\]
Thus the dependence can have either sign. In particular,
\[
a=\frac12:\quad
(p_2,p_3,c)=\left(\frac14,\frac{11}{24},\frac16\right),\qquad
\operatorname{Cov}(I_2,I_3)=\frac5{96}>0,
\]
whereas
\[
a=2:\quad
(p_2,p_3,c)=\left(\frac34,\frac16,\frac1{12}\right),\qquad
\operatorname{Cov}(I_2,I_3)=-\frac1{24}<0.
\]
At \(a=1\) the iid uniform case is recovered and the covariance is zero.

## Product extension to every dimension

For any \(d\ge1\), let each observation be a vector with mutually independent coordinates, with each coordinate following the scalar law above for the corresponding observation. Let \(J_j\) denote the complete record indicator: all coordinates of the \(j\)-th vector strictly exceed the corresponding coordinatewise maxima of the preceding observations.

Coordinate independence gives
\[
\Pr(J_2=1)=p_2^d,\qquad
\Pr(J_3=1)=p_3^d,\qquad
\Pr(J_2=J_3=1)=c^d.
\]
Hence
\[
\operatorname{Cov}(J_2,J_3)=c^d-(p_2p_3)^d.
\]
Because \(c\) and \(p_2p_3\) are nonnegative, this covariance has the same sign as \(c-p_2p_3\). Therefore the same absolutely continuous product family refutes the claimed universal independence in every dimension under the simultaneous-coordinate record definition.

## Why the special \(F^\alpha\) theory is different

The classical non-identical setting in which record indicators are independent is Nevzorov's \(F^\alpha\)-scheme,
\[
F_i(x)=F(x)^{\alpha_i},\qquad \alpha_i>0,
\]
not an arbitrary collection of independent marginals. For three observations,
\[
\Pr(I_2=1)=\frac{\alpha_2}{\alpha_1+\alpha_2},\qquad
\Pr(I_3=1)=\frac{\alpha_3}{\alpha_1+\alpha_2+\alpha_3},
\]
and
\[
\Pr(I_2=I_3=1)
=\frac{\alpha_2\alpha_3}
{(\alpha_1+\alpha_2)(\alpha_1+\alpha_2+\alpha_3)},
\]
so the two indicators are indeed independent. Nevzorov's result, and later expositions, establish independence in this structured family; related converse results characterize the power-family structure under record-indicator independence conditions.

Barlevy and Nagaraja (2005) explicitly summarize Nevzorov's theorem: independent variables with cdfs \(F_i=F^{\alpha(i)}\) have independent record indicators, and they also state a converse characterization under non-disjoint-support conditions. He and Borovkov (2020) likewise identify indicator independence as a key property of the \(F^\alpha\)-scheme and obtain only asymptotic pairwise independence under a substantially broader threshold scheme. These results are incompatible with a universal theorem for arbitrary independent non-identical marginals.

## Location of the error in the 2026 argument

In the proof leading to equation (2.3) of Lo and Babou (2026), probabilities of events from disjoint observation blocks are factored after introducing random record-endpoint variables. Conditional on fixed endpoints, the corresponding block events can be independent, but their conditional probabilities remain functions of the endpoint values; adjacent factors also share endpoint variables. Integrating the product over those shared endpoints cannot in general be replaced by a product of unconditional expectations. The uniform-scale family above gives an exact finite-dimensional witness to the resulting failed factorization.

## Scope and originality

The classical fact that special non-identically distributed sequences can have independent record indicators is not new, and neither is the \(F^\alpha\) theory or its characterizations. The contribution recorded here is narrowly a correction of the 2026 universal claim: an exact continuous one-parameter counterexample family with both signs of dependence, its product extension to every dimension, and an identification of the factorization failure in the proposed proof. To the best of our knowledge, no public correction or counterexample to arXiv:2602.20416 was found in the literature checked for this record.

This note does not attempt a new complete characterization of all independent non-identical sequences whose record indicators are independent. Existing Nevzorov-type characterization results already cover important versions of that question. A later revision or independently circulated correction of the 2026 preprint could reduce the originality of this correction without affecting the counterexample itself.

## Reproducibility

`artifacts/verify_exact.py` uses exact rational arithmetic to reproduce the displayed rational examples and to verify the sign preservation of the product construction for several rational scale parameters and dimensions. Its recorded output is in `artifacts/VERIFICATION.txt`. The general formulas above are proved by direct integration and do not rely on the computation.

## References

1. G. S. Lo and E. H. Babou, *Independence of the indicator functions of record values for Multivariate independent data*, arXiv:2602.20416 (2026). https://arxiv.org/abs/2602.20416
2. V. B. Nevzorov, *Record and interrecord times for sequences of nonidentically distributed random variables*, Journal of Soviet Mathematics 36 (1987), 510–516. https://doi.org/10.1007/BF01663462
3. V. B. Nevzorov, *Two characterizations using records*, Lecture Notes in Mathematics 1233 (1986), 79–85. https://doi.org/10.1007/BFb0072713
4. D. Pfeifer, *Some remarks on Nevzorov's record model*, Advances in Applied Probability 23 (1991), 823–834. https://doi.org/10.2307/1427678
5. G. Barlevy and H. N. Nagaraja, *Characterizations in a random record model with a non-identically distributed initial record*, Federal Reserve Bank of Chicago Working Paper 2005-05. https://www.chicagofed.org/publications/working-papers/2005/2005-05
6. P. He and K. A. Borovkov, *Limit Theorems for Record Indicators in Threshold \(F^\alpha\)-Schemes*, Theory of Probability & Its Applications 65 (2020), 405–417. https://doi.org/10.1137/S0040585X97T990034

**Same-model review: passed. Independent audit: not yet performed.**
