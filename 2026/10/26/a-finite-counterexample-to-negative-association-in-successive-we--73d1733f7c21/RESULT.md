# A finite counterexample to negative association in successive weighted sampling

## Finding

For five items with positive worth vector \(w=(1,34,37,1,1)\), draw a full Plackett–Luce ranking by successive probability-proportional-to-remaining-worth selection. Let \(I_i\) indicate that item \(i\) occurs among the first three positions. Then

\[
\operatorname{Cov}(I_2,I_3)=\frac{2941}{1230359520}>0.
\]

Therefore the top-three inclusion indicators are not negatively associated. This is a counterexample for this specific positive worth vector and sample size; it is not a classification of all Plackett–Luce designs.

## Assumptions and scope

There are five distinct items with worths \(w_i>0\). At each draw, an unselected item \(i\) is chosen with probability \(w_i\) divided by the sum of the worths of all remaining items. The sample consists of the first three selected items, with order discarded only when defining the inclusion indicators. Negative association would require nonpositive covariance for every pair of distinct increasing indicator functions, so one positive pairwise covariance is sufficient to disprove it.

## Proof

For an ordered top-three sequence \((i_1,i_2,i_3)\) of distinct labels, its probability is

\[
\frac{w_{i_1}}{W}\,\frac{w_{i_2}}{W-w_{i_1}}\,\frac{w_{i_3}}{W-w_{i_1}-w_{i_2}},\qquad W=\sum_{i=1}^5w_i=74.
\]

Summing this expression over all \(5\cdot4\cdot3=60\) ordered sequences gives total probability \(1\). Exact rational enumeration gives

\[
\Pr(I_2=1)=\frac{10761}{10804},\qquad
\Pr(I_3=1)=\frac{113507}{113880},
\]

and

\[
\Pr(I_2=I_3=1)=\frac{2091527}{2106780}.
\]

Consequently

\[
\begin{aligned}
\operatorname{Cov}(I_2,I_3)
&=\Pr(I_2=I_3=1)-\Pr(I_2=1)\Pr(I_3=1)\\
&=\frac{2941}{1230359520}>0.
\end{aligned}
\]

The included verification script independently enumerates all 60 ordered sequences using exact rational arithmetic, checks normalization, and asserts each fraction above. No asymptotic or simulation inference is used.

## Verification

Reproducibility: run `python verify_plackett_luce.py` with Python 3. The script uses only the standard library (`fractions` and `itertools`) and verifies the exact rational probabilities and strict positive sign. The conclusion follows directly from the definition of negative association by choosing the two coordinate functions \(f(I_2)=I_2\) and \(g(I_3)=I_3\).

## Relationship to prior work

Joag-Dev and Proschan (1983) define negative association and discuss examples including multivariate hypergeometric sampling without replacement. Yu (2010) studies first-order inclusion probabilities for successive and rejective sampling and compares their majorization behavior. These sources motivate the question but do not imply negative association for the Plackett–Luce successive-sampling top-three indicators: the first concerns different sampling laws, and the second's stated results concern marginal inclusion probabilities rather than pairwise dependence. This is a finite counterexample, not a general dependence theorem.

## Limitations

Only the specified worth vector and top-three sample are established here. The covariance is small in magnitude but strictly positive, which is enough to refute negative association. The result does not determine the sign for other worth vectors or sample sizes, and no claim is made about stronger forms of positive dependence.

## References

1. K. Joag-Dev and F. Proschan, “Negative Association of Random Variables with Applications,” *The Annals of Statistics* 11(1) (1983), 286–295. DOI: 10.1214/aos/1176346079.
2. Y. Yu, “On the inclusion probabilities in some unequal probability sampling plans without replacement,” *Bernoulli* 18(1) (2012), 282–304; first public preprint 22 May 2010. arXiv:1005.4107. DOI: 10.3150/10-BEJ337.
