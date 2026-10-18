# A sharp universal resolution-loss bound for Pianka niche overlap

## Finding

For any integer \(m\ge 3\), let \(p,q\in[0,\infty)^m\) be nonzero resource-utilization vectors. Let \(T\) merge any two distinct resource classes by summing their entries and leave every other class unchanged. Define Pianka's pairwise niche-overlap coefficient by
\[
O(p,q)=\frac{\sum_{i=1}^m p_iq_i}{\bigl(\sum_{i=1}^m p_i^2\bigr)^{1/2}\bigl(\sum_{i=1}^m q_i^2\bigr)^{1/2}}.
\]
Then the exact greatest possible **downward** change after one category merger is
\[
\boxed{\sup_{p,q}\bigl[O(p,q)-O(Tp,Tq)\bigr]=K=\bigl(1-2^{-1/3}\bigr)\sqrt{2-2^{2/3}}=0.1325141267187\ldots.}
\]
The supremum is attained for vectors with structural zeros; under strict positivity it is the sharp supremum approached by positive vectors. It is already attained with exactly three resource classes. In the other direction an upward change of \(1\) is possible, so there is no analogous nontrivial upper-increase restriction. For the Schoener/Czekanowski overlap \(S(p,q)=\sum_i\min(\widehat p_i,\widehat q_i)\), where hats denote normalization to unit sums, every such merger satisfies \(S(Tp,Tq)\ge S(p,q)\). Thus the two standard niche-overlap indices have categorically different resolution behavior.

## Assumptions and scope

The resource categories are discrete; utilization vectors are nonnegative, nonzero, and may include zero-use categories. The two profiles are measured on the same fixed categorization before merger. One, and only one, pair of classes is pooled by addition, without reweighting category sizes or imputing missing use. Homogeneity of \(O\) permits profiles to be normalized to probability distributions without changing the theorem. There is no stochastic sampling assumption, inference of competition strength, claim about category availability, or dynamic ecological model.

The sharpness example, in three resource classes with the first two pooled, is
\[
\begin{aligned}
A&=2^{1/3},\qquad s=\frac{2-A^2}{A^2-1}>0,\qquad h=\sqrt{2s},\\
p&=(0,0,1),\qquad q=(1,1,h).
\end{aligned}
\]
Using unit-sum versions of \(p,q\) gives identical values. Here \(O(p,q)=h/\sqrt{2+h^2}\), while \(O(Tp,Tq)=h/\sqrt{4+h^2}\), and their difference equals \(K\). Additional categories may be appended with zero entries. If one insists on positive use in every category, replace the zeros by a common positive \(\varepsilon\), renormalize, and let \(\varepsilon\downarrow0\).

For a two-class table, merging both classes yields overlap \(1\), so a downward change is impossible. Three classes are therefore the minimum size for the downward phenomenon. For an upward change of \(1\), use \(p=(1,0,0)\), \(q=(0,1,0)\) and merge the first two classes: the before/after overlaps are respectively \(0\) and \(1\).

## Proof

By symmetry, merge positions \(1\) and \(2\). Write
\[
\begin{array}{lll}
a=(p_1^2+p_2^2)^{1/2}, & r=(\sum_{i=3}^m p_i^2)^{1/2}, & U=p_1+p_2,\\
b=(q_1^2+q_2^2)^{1/2}, & s=(\sum_{i=3}^m q_i^2)^{1/2}, & W=q_1+q_2,
\end{array}
\]
and let \(d=p_1q_1+p_2q_2\), \(e=\sum_{i=3}^m p_iq_i\). By nonnegativity and Cauchy–Schwarz, \(d\le ab\), \(e\le rs\), and
\[
a\le U\le\sqrt2a,\qquad b\le W\le\sqrt2b.
\]
Introduce \(L_p=\sqrt{a^2+r^2}\), \(L_q=\sqrt{b^2+s^2}\), \(M_p=\sqrt{U^2+r^2}\), \(M_q=\sqrt{W^2+s^2}\). Both \(M_p\ge L_p>0\) and \(M_q\ge L_q>0\). The decrease is
\[
\frac{d+e}{L_pL_q}-\frac{UW+e}{M_pM_q}.
\]
Its coefficient of \(e\) is nonnegative. Consequently, substituting \(e\le rs\), and then \(d\le ab\), gives the valid upper bound
\[
O(p,q)-O(Tp,Tq)\le
\frac{ab+rs}{L_pL_q}-\frac{UW+rs}{M_pM_q}.\tag{1}
\]
This step is important: it means any number of untouched categories can be replaced, for purposes of an upper bound, by a single perfectly aligned outside component. It does not assume their uses were originally aligned.

For \(x\in[0,\pi/2]\), define \(f(x)=\arctan(\tan x/\sqrt2)\), extended continuously at \(\pi/2\). Define angles \(\alpha,\beta\in[0,\pi/2]\) through \(\cos\alpha=a/L_p\), \(\sin\alpha=r/L_p\), and \(\cos\beta=b/L_q\), \(\sin\beta=s/L_q\). Set \(\alpha'=\arctan(r/U)\), \(\beta'=\arctan(s/W)\), with the continuous limiting interpretation if a denominator vanishes. Then
\[
f(\alpha)\le\alpha'\le\alpha,\qquad f(\beta)\le\beta'\le\beta.
\]
The right side of (1) is \(\cos(\alpha-\beta)-\cos(\alpha'-\beta')\). Interchange the profiles if necessary so that \(\alpha\ge\beta\). Since \(f\) is increasing,
\[
|\alpha'-\beta'|\le\alpha-f(\beta).
\]
Indeed, \(\alpha'-\beta'\le\alpha-f(\beta)\), while \(\beta'-\alpha'\le\beta-f(\alpha)\le\alpha-f(\beta)\). As all these absolute differences lie in \([0,\pi/2]\),
\[
O(p,q)-O(Tp,Tq)
\le \cos(\alpha-\beta)-\cos(\alpha-f(\beta)).\tag{2}
\]
For fixed \(\beta\), the right side of (2) increases with \(\alpha\in[\beta,\pi/2]\): its derivative is \(\sin(\alpha-f(\beta))-\sin(\alpha-\beta)\ge0\). Thus
\[
O(p,q)-O(Tp,Tq)\le \sin\beta-\sin f(\beta)
=\frac{t}{\sqrt{1+t^2}}-\frac{t}{\sqrt{2+t^2}}=:g(t),\qquad t=\tan\beta\ge0.
\]
The endpoints \(t=0,\infty\) have \(g=0\), and
\[
g'(t)=(1+t^2)^{-3/2}-2(2+t^2)^{-3/2}.
\]
The unique positive stationary point satisfies \((2+t^2)/(1+t^2)=2^{2/3}\), hence \(t^2=(2-2^{2/3})/(2^{2/3}-1)\). This is the global maximum, and direct substitution gives \(g(t)=\bigl(1-2^{-1/3}\bigr)\sqrt{2-2^{2/3}}=K\). In the displayed sharpness example \(\alpha=\pi/2\) and the nonzero merged entries of \(q\) are equal, so every inequality in this proof attains equality. This completes the universal bound and its sharpness.

For Schoener overlap, normalize the original vectors to sums one; merging preserves these sums. Using \(S(p,q)=1-\frac12\sum_i|p_i-q_i|\), the triangle inequality
\[
|(p_1+p_2)-(q_1+q_2)|\le|p_1-q_1|+|p_2-q_2|
\]
proves its claimed nondecrease. The upward Pianka example and the two-category statement follow immediately from the definitions.

## Verification

Run `python verification/check.py` from the package root. It checks the closed-form constant and equality witness at high numerical precision, validates the one-dimensional derivative equation symbolically when SymPy is available, and performs deterministic rational grid and pseudorandom nonnegative-vector stress checks of the bound and the Schoener contrast. These finite checks are diagnostics, not proof of the quantified theorem; the proof above is analytic. The program has no network access, external datasets, or missing artifacts.

## Relationship to prior work

Pianka (1973) introduced the symmetric cosine-normalized resource overlap, with the original formula displayed in equation (5) on page 59. The measure's mathematical definition is prior art. Ecological assessments have long warned that niche metrics depend on the representation of resources: Hurlbert (1978) and Abrams (1980) dispute interpreting raw overlap as competitive strength; Slobodchikoff and Schulz (1980) analyze overlap constructions; Geange and colleagues (2010, first online) instead use intersection-of-distributions overlap for categorical data; Pierotti and colleagues (2016, first online) study compositional alternatives and explicitly discuss the problem of amalgamating categories. Their alternative index's subcomposition results concern restriction and renormalization, not the pooling map proved here. Existing software (EcoSimR) calculates Pianka and Czekanowski pairwise scores but does not supply a sharp pooling-decrement constant in its exposed mathematical definitions. The finding adds the sharp universal, one-merger, one-sided robustness bound and the matching extremal construction for the original Pianka statistic. It does not claim that sensitivity to resolution was previously unknown.

## Limitations

The sharp constant concerns merging exactly two resource classes in one step. It is not a bound for arbitrarily many simultaneous mergers, splitting classes under arbitrary allocation, data sampling error, or interspecific competition coefficients. If all entries are strictly positive, the same constant is a supremum rather than necessarily attained. The proof uses nonnegativity crucially; signed vectors or nonadditive category transformations are not covered. Bibliographic coverage of older, occasionally paywalled treatments is incomplete, and independent literature review has not been performed.

## References

1. Pianka, E. R. (1973), *The Structure of Lizard Communities*, Annual Review of Ecology and Systematics 4, 53–74. DOI: 10.1146/annurev.es.04.110173.000413. An author-hosted full-text scan supplies equation (5) on p. 59.
2. Hurlbert, S. H. (1978), *The Measurement of Niche Overlap and Some Relatives*, Ecology 59, 67–77. DOI: 10.2307/1936632.
3. Abrams, P. (1980), *Some Comments on Measuring Niche Overlap*, Ecology 61, 44–49. DOI: 10.2307/1937153.
4. Slobodchikoff, C. N. and Schulz, W. C. (1980), *Measures of Niche Overlap*, Ecology 61, 1051–1055. DOI: 10.2307/1936823.
5. Geange, S. W., Pledger, S., Burns, K. C. and Shima, J. S. (2011), *A unified analysis of niche overlap incorporating data of different types*, Methods in Ecology and Evolution 2, 175–184, first online 21 October 2010. DOI: 10.1111/j.2041-210X.2010.00070.x.
6. Pierotti, M. E. R., Martín-Fernández, J. A. and Barceló-Vidal, C. (2017), *The peril of proportions: robust niche indices for categorical data*, Methods in Ecology and Evolution, first online 8 September 2016. DOI: 10.1111/2041-210X.12656.
7. GotelliLab, EcoSimR, documented R routines `pianka` and `czekanowski`, https://github.com/GotelliLab/EcoSimR/blob/master/R/metrics.R (consulted for formula and index comparison only).
