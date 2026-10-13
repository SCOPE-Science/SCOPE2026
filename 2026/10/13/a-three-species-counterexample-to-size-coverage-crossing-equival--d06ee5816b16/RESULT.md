# A three-species counterexample to size–coverage crossing equivalence in richness rarefaction

## Finding

**Theorem (explicit counterexample).** Consider the two three-species probability vectors
\[
 P=(15/20,4/20,1/20),\qquad Q=(12/20,7/20,1/20).
\]
For every real \(m\ge 1\), define expected species richness and expected sample coverage by
\[
 R_p(m)=\sum_{i=1}^{3}\bigl(1-(1-p_i)^m\bigr),
 \qquad C_p(m)=1-\sum_{i=1}^{3}p_i(1-p_i)^m.
\]
The size-based expected-richness curves satisfy \(R_P(m)<R_Q(m)\) at **every** \(m>1\). Nevertheless, when each expected richness is plotted against its *own* expected sample coverage, the ordering reverses: community \(Q\) is richer at equal coverage \(c_0=C_P(2)=39/50\), while community \(P\) is richer at equal coverage
\[
 c_1=C_P(11)=\frac{1954570132251121}{2048000000000000}.
\]
Consequently the coverage-based curves cross for some \(c\in(c_0,c_1)\), although the size-based curves have no crossing at all beyond the single-individual base point. Both chosen coverages exceed the expected coverage after one individual for **both** communities. The reversal holds for analytic real-effort curves and for continuous piecewise-linear interpolation of their integer-effort points.

This directly contradicts the unrestricted implication in Theorem G1 of Chao and Jost (2012), Appendix G, that noncrossing expected size-based curves guarantee noncrossing expected coverage-based curves. It also contradicts the asserted crossing-count equivalence in that appendix when applied to the same theoretical model.

## Assumptions and scope

An individual is sampled independently with replacement, with species-selection probabilities given by \(p=(p_1,p_2,p_3)\). All six stated probabilities are strictly between zero and one, and each vector sums to one. There is no detection error, abundance estimation, or finite-population correction. For an integer \(m\ge1\), richness is the number of distinct species in \(m\) sampled individuals, and coverage is the total population frequency of species detected at least once. Linearity of expectation gives the formulas above. Their analytic extensions to real \(m\ge1\) are convenient continuous parametrizations, **not** fractional-individual sampling experiments. Independently, connect consecutive integer-effort points by straight line segments to obtain the polygonal curves discussed below.

For a common coverage \(c\) attained by both communities, the coverage-standardized expected richness of community \(p\) is \(H_p(c)=R_p(C_p^{-1}(c))\), where the inverse exists on the relevant coverage interval because \(C_p\) is strictly increasing. For polygonal interpolation, replace \(C_p^{-1}\) and \(R_p\) with the corresponding linearly interpolated functions.

## Proof

**1. No size-based crossing.** In descending order the vectors satisfy
\[
 15/20>12/20,\qquad (15+4)/20=(12+7)/20=19/20,
\]
so \(P\) strictly majorizes \(Q\). For any real \(m>1\), the map \(t\mapsto (1-t)^m\) is strictly convex on \((0,1)\), since its second derivative is \(m(m-1)(1-t)^{m-2}>0\). Strict Karamata therefore yields
\[
 \sum_i(1-P_i)^m>\sum_i(1-Q_i)^m,
 \qquad R_P(m)<R_Q(m).
\]
At \(m=1\), both curves begin at expected richness one. Thus there is no size-based crossing at any real \(m>1\). At integer efforts, linear interpolation also maintains strict order on every open segment after the common base point.

**2. Strict monotonicity.** Every component \(p_i\) lies in \((0,1)\). For all real \(m\ge1\), each \((1-p_i)^m\) decreases strictly as \(m\) increases. It follows directly that both \(C_p(m)\) and \(R_p(m)\) increase strictly, continuously, and tend respectively to \(1\) and \(3\). Thus equal-coverage comparisons are well-defined on the common coverage domain above the larger of the two one-individual base coverages.

**3. First certified ordering.** Exact rational substitution at integer efforts yields
\[
 C_P(2)=39/50,\quad C_Q(2)=711/1000,
 \quad C_Q(3)=65809/80000,
\]
with positive margins
\[
 C_P(2)-C_Q(2)=69/1000,\quad
 C_Q(3)-C_P(2)=3409/80000.
\]
Therefore, at coverage \(c_0=C_P(2)\), the unique effort \(m_Q\) needed by community \(Q\) lies strictly between \(2\) and \(3\). Also
\[
 R_P(2)=279/200,\qquad R_Q(2)=303/200,
 \quad R_Q(2)-R_P(2)=3/25>0.
\]
Since \(R_Q\) increases strictly, \(H_Q(c_0)>R_Q(2)>R_P(2)=H_P(c_0)\).

**4. Second certified, reversed ordering.** Further exact rational substitution gives
\[
 C_P(11)=\frac{1954570132251121}{2048000000000000},
\]
\[
 C_Q(7)=\frac{12120861409}{12800000000},\qquad
 C_Q(8)=\frac{12227624883}{12800000000}.
\]
Both bracketing inequalities are strict; their exact positive differences are
\[
 C_P(11)-C_Q(7)=\frac{15232306811121}{2048000000000000},
\]
\[
 C_Q(8)-C_P(11)=\frac{1849849028879}{2048000000000000}.
\]
Hence the unique \(Q\)-effort at coverage \(c_1=C_P(11)\) lies strictly between \(7\) and \(8\). Meanwhile,
\[
 R_P(11)=\frac{12007937655731}{5120000000000},\qquad
 R_Q(8)=\frac{29491964511}{12800000000},
\]
\[
 R_P(11)-R_Q(8)=\frac{211151851331}{5120000000000}>0.
\]
By strict monotonicity of \(R_Q\),
\[
 H_Q(c_1)<R_Q(8)<R_P(11)=H_P(c_1).
\]

**5. Crossing and interpolation independence.** The two functions \(H_P\) and \(H_Q\) are continuous on the interval \([c_0,c_1]\). The strict inequalities in Steps 3 and 4 and the intermediate-value theorem force at least one crossing in \((c_0,c_1)\). Their one-individual coverages are \(C_P(1)=121/200\) and \(C_Q(1)=97/200\), both strictly below \(c_0=39/50\); thus the crossing is beyond both base points.

The same comparison remains valid if only integer efforts are treated as sampling experiments, and the resulting points \((C_p(m),R_p(m))\) are joined by straight line segments: the polygonal \(Q\)-ordinate at \(c_0\) lies between \(R_Q(2)\) and \(R_Q(3)\), and the one at \(c_1\) between \(R_Q(7)\) and \(R_Q(8)\). The \(P\)-ordinates at these levels remain exactly \(R_P(2)\) and \(R_P(11)\). Strict inequalities and continuous crossing follow identically. Therefore the counterexample is not an artifact of noninteger individual effort.

## Verification

The accompanying standard-library script `verify.py` performs exact rational evaluation of the six decisive strict margins, checks the one-individual coverages and majorization inequalities, and independently derives integer-effort formulas through exhaustive sampling-sequence enumeration at efforts one, two, and three. It prints `VERIFY_OK` only if every check passes. Reproducibility command: `python3 verify.py`. This independent finite calculation corroborates the rational certificates; the proof of noncrossing at *all* real efforts uses strict convexity and majorization rather than a finite search. The existence of a crossing uses continuity, not a numerical root finder.

## Relationship to prior work

Chao and Jost (2012) define the expected size-based and coverage-based species accumulation curves for independent individual sampling. Their main text explicitly asserts equivalence of crossing behavior, and Appendix G, Theorem G1, states the noncrossing equivalence; Theorem G3 asserts equality of crossing counts. The theorem here supplies a concrete counterexample *inside those stated theoretical definitions*: the original claims have no additional restriction excluding equal three-species richness or majorization of abundance vectors. Appendix H supplies further discussion of the theoretical coverage-based parametrization, not a remedy for this counterexample.

Lande, DeVries, and Walla (2000) discuss crossings and rankings for size-based accumulation curves; that historical context does not already provide the same comparison under expected-coverage standardization. A distinct previously indexed result concerns covariance of consecutive species discoveries, not this crossing equivalence. The novelty here is the refutation of a precise universal implication using two rational three-species communities; the standard expectation identities and majorization inequality themselves are not claimed as new.

## Limitations

The conclusion is a counterexample, not a full classification of all abundance pairs, nor a theorem on the minimum number of species permitting reversal. It concerns **expected** richness plotted against **expected** sample coverage under independent sampling with replacement; it makes no assertion about variance, confidence intervals, coverage estimation from finite reference samples, or actual significance in field surveys. The crossing point is proved to exist in a strict rationally bracketed interval, but its exact coordinate and the total number of coverage-curve crossings are not determined. The result does not invalidate all uses of coverage standardization, only a specific universal ranking/crossing implication. An independently indexed correction or equivalent counterexample in less accessible literature remains possible.

## References

1. Chao, A. and Jost, L. (2012). *Coverage-based rarefaction and extrapolation: standardizing samples by completeness rather than size*. Ecology 93, 2533–2547. DOI: 10.1890/11-1952.1. First published 2012-12-01. https://esajournals.onlinelibrary.wiley.com/doi/10.1890/11-1952.1
2. Chao, A. and Jost, L. (2012). Appendix G: *Comparisons of size- and coverage-based species accumulation curves*, especially Theorems G1 and G3. https://esapubs.org/archive/ecol/E093/238/appendix-G.pdf
3. Chao, A. and Jost, L. (2012). Appendix H: *Some basic theoretical properties of coverage-based species accumulation curves*. https://esapubs.org/archive/ecol/E093/238/appendix-H.pdf
4. Lande, R., DeVries, P. J., and Walla, T. R. (2000). *When species accumulation curves intersect: implications for ranking diversity using small samples*. Oikos 89, 601–605. DOI: 10.1034/j.1600-0706.2000.890320.x.
