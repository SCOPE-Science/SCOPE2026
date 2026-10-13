# Minimal smooth exchangeable counterexample to order-statistic Kendall concordance

## Finding

There is an exchangeable triple \((X_1,X_2,X_3)\) of positive, atomless lifetimes whose joint density is \(C^\infty\) and **strictly positive at every point of \((0,\infty)^3\)**, but whose first two order statistics satisfy
\[
\tau(X_{1:3},X_{2:3})<\tau(X_1,X_2).
\]
Here \(\tau(U,V)=\mathbb E[\operatorname{sgn}(U-U')\operatorname{sgn}(V-V')]\), with \((U',V')\) an independent copy. The construction gives the explicit certified strict gap
\[
\tau(X_1,X_2)-\tau(X_{1:3},X_{2:3})\ge\frac{3209}{22500}>0.
\]
This counterexample first occurs at sample size three: for **every** bivariate probability law, with ties allowed,
\[
\tau(\min\{X_1,X_2\},\max\{X_1,X_2\})\ge\tau(X_1,X_2).
\]
Therefore the broader conjectural extension of a known concordance comparison from time-transformed exponential models to arbitrary exchangeable lifetimes is false, even under smooth full-support densities, and three is the minimal counterexample dimension.

## Assumptions and scope

All lifetimes are positive, and \(X_{1:3}\le X_{2:3}\le X_{3:3}\) denote their ordered values. All samples used to compute Kendall's tau are independent copies of the **whole triple**, so within-triple coordinates may be dependent. In the counterexample they have identical marginal laws by exchangeability. No conditional independence, infinite extendibility, or time-transformed exponential representation is assumed. The inequality that is refuted was proved for a special class of exchangeable lifetime models; its validity in that class is not challenged.

For completeness an explicit distribution is supplied. Set \(\varepsilon=1/10\) and let \(U_1,U_2,U_3\) be independent with the compactly supported smooth density
\[
\psi(u)=C\exp\!\left(-\frac1{u(\varepsilon-u)}\right)\mathbf1_{(0,\varepsilon)}(u),
\]
where \(C>0\) is the normalizing constant. Independently choose \(G\in\{A,B\}\), each with probability \(1/2\), and a coordinate \(J\) uniformly in \(\{1,2,3\}\). For \(G=A\), let \(a_J=0\) and the other two \(a_i=10\); for \(G=B\), let \(a_J=1\) and the other two \(a_i=2\). Set \(Z_i=a_i+U_i\). Thus \(Z\) is an exchangeable, nonnegative, absolutely continuous triple. Let \(E=(E_1,E_2,E_3)\) have independent rate-one exponential coordinates and put
\[
P=\frac{99}{100}\operatorname{Law}(Z)+\frac1{100}\operatorname{Law}(E).
\]
The counterexample is \(X\sim P\), which is exchangeable with a smooth density \(f_P(z)\ge 100^{-1}\exp(-z_1-z_2-z_3)>0\) for all \(z_i>0\).

## Proof

**Step 1: an exact discrete-category Kendall comparison.** For any pair of independent copies of \(Z\), the small noises break ties smoothly but preserve all comparisons between the separated baseline levels. Condition on two independently selected groups \(G,G'\).

Within either common group, the low coordinate in each copy is uniformly chosen from three positions. For the first two labelled coordinates, when their low positions are different and both lie in \(\{1,2\}\), the coordinate comparison signs are opposite; this has probability \(2/9\). In all remaining cases at least one of the coordinate comparisons is between identically distributed independent noises, so the expected product is zero. Hence
\[
\mathbb E[\operatorname{sgn}(Z_1-Z'_1)\operatorname{sgn}(Z_2-Z'_2)\mid G=G'=A]
=\mathbb E[\cdots\mid G=G'=B]=-\frac29.
\]

Between groups \(A\) and \(B\), an \(A\)-coordinate is smaller than any \(B\)-coordinate precisely when its baseline is zero. Thus the product of signs for the first two labelled coordinates is \(+1\) if the unique low \(A\) coordinate is position three (probability \(1/3\)), and \(-1\) otherwise (probability \(2/3\)). It follows that the cross-group expected product is \(-1/3\), regardless of the orientation of the two groups. Weighting common-group cases by \(1/4\) each and cross-group cases by \(1/2\),
\[
\tau(Z_1,Z_2)=\frac14\left(-\frac29\right)+\frac14\left(-\frac29\right)+\frac12\left(-\frac13\right)=-\frac5{18}.
\]

Within group \(A\), the first ordered lifetime is \(U_J\) and the second is \(10+\min_{i\ne J}U_i\); these variables are independent because they depend on disjoint independent noise coordinates, and their conditional distributions do not depend on \(J\). Thus their conditional Kendall tau is zero. The same argument applies to group \(B\), whose first two order statistics are \(1+U_J\) and \(2+\min_{i\ne J}U_i\). Between an \(A\)-triple and a \(B\)-triple, the first order statistic is **smaller** in \(A\) (near zero versus near one) but the second is **larger** in \(A\) (near ten versus near two). The cross-group Kendall product is therefore exactly \(-1\). Consequently
\[
\tau(Z_{1:3},Z_{2:3})=\frac14(0)+\frac14(0)+\frac12(-1)=-\frac12
\quad\text{and}\quad
D(\operatorname{Law}(Z)):=\tau(Z_1,Z_2)-\tau(Z_{1:3},Z_{2:3})=\frac29.
\]

**Step 2: a quantitative full-support smoothing.** Write \(D(Q)\) for the difference of the two Kendall statistics under any law \(Q\) on triples. It is the expectation of a difference of two sign-product kernels, each in \([-1,1]\). Couple two independent \(P\)-draws with two independent \(\operatorname{Law}(Z)\)-draws by replacing each complete triple with an independent \(E\)-triple at probability \(\eta=1/100\). The coupled pair changes with probability at most \(2\eta-\eta^2\). The difference of the two kernels lies in \([-2,2]\), so the difference of its values under the coupling has absolute value at most four. Hence
\[
\bigl|D(P)-D(\operatorname{Law}(Z))\bigr|\le4(2\eta-\eta^2)
\quad\Longrightarrow\quad
D(P)\ge\frac29-4\left(\frac2{100}-\frac1{10000}\right)=\frac{3209}{22500}>0.
\]
Smoothness follows from the usual \(C^\infty\) extension by zero of \(\psi\) at both endpoints, translated products thereof, and the smooth exponential mixture. The strict positive lower bound on the density was displayed in the definition of \(P\).

**Step 3: dimension two cannot give a reversal.** For any two real pairs \((a_1,a_2)\) and \((b_1,b_2)\), let \(a_-\le a_+\) and \(b_-\le b_+\) be their rearrangements. The pointwise rearrangement inequality is
\[
\operatorname{sgn}(a_--b_-)\operatorname{sgn}(a_+-b_+)
\ge
\operatorname{sgn}(a_1-b_1)\operatorname{sgn}(a_2-b_2).
\]
If the left product equals \(+1\), the inequality is immediate. If it equals \(-1\), one interval \([a_-,a_+]\) strictly contains the other; under either original matching one endpoint comparison is positive and the other negative, so the right product is also \(-1\). If the left product equals zero, an endpoint equality forces the right product to be zero or negative (never positive). This exhausts all possibilities, including ties. Taking expectations for independent copies of \((X_1,X_2)\) proves the universal two-dimensional inequality. Since the preceding construction violates it at three dimensions, three is the smallest possible dimension.

## Verification

Run `python3 artifacts/verify.py` with Python 3 and no external packages. The verifier enumerates the nine pairs of low-coordinate locations for each group pairing using exact rational arithmetic. It reconstructs the within-group and across-group conditional Kendall expectations, the aggregate values \(-5/18\) and \(-1/2\), and the certified smooth-density lower bound \(3209/22500\). It also runs a finite-grid diagnostic for the two-dimensional pointwise lemma; the lemma itself is proved above for arbitrary real inputs, not inferred from the diagnostic. The compactly supported smooth bump and the positive exponential mixture are analytic, rather than numerical, parts of the proof.

## Relationship to prior work

Kochar and Spizzichino (2023) prove that the dependence of the first two order statistics is stronger than the dependence of two original coordinates in the time-transformed exponential class, using a more-stochastic-increasing dependence order that implies concordance comparisons. They expressly raise the extension to other exchangeable models. The present example answers the **unrestricted** extension in the negative, and does not contradict their conditional positive theorem. The quantitative smooth full-support result and exact dimension-two boundary distinguish it from simply observing that a discrete exchangeable vector need not be positively associated.

Fuchs and Schmidt (2021) investigate Kendall's tau for order statistics, providing directly relevant two-order-statistic context. The universal sample-size-two boundary is proved here without reliance on that article. Published results on pairwise-independent labelled ordering probabilities, or Pearson correlations of iid sample minima and maxima, concern different hypotheses and statistics and do not imply a three-dimensional exchangeable Kendall reversal.

## Limitations

The counterexample is finitely exchangeable, not asserted infinitely extendible or conditionally iid. It does not contradict concordance preservation in Schur-constant, time-transformed exponential, or other restricted positive-dependence subclasses. It establishes an explicit **lower** bound on the constructed strict gap, not an optimal gap over all exchangeable distributions. The interior density is smooth and everywhere positive, but no uniform upper/lower density bounds or parametric copula representation are claimed. Independent novelty or correctness certification has not been performed; an earlier equivalent construction could exist under alternative dependence terminology. The full text of Fuchs and Schmidt (2021) was inaccessible at this review and remains a bibliographic risk, not evidence of a covering claim.

## References

1. S. Kochar and F. L. Spizzichino, “Dependence among order statistics for time-transformed exponential models,” *Probability in the Engineering and Informational Sciences* (first public preprint archived by September 12, 2023; journal article online October 5, 2023). DOI: https://doi.org/10.1017/S0269964823000190. Accessible preprint: https://pdxscholar.library.pdx.edu/mth_fac/378/.
2. M. Fuchs and K. D. Schmidt, “On order statistics and Kendall’s tau,” *Statistics & Probability Letters* (2021). DOI: https://doi.org/10.1016/j.spl.2020.108972.
3. “Complete ordering polytope for three pairwise-independent continuous observations,” public mathematical research record, September 20, 2026.
4. “Sharp min-max correlation over three-point probability weights,” public mathematical research record, September 20, 2026.
