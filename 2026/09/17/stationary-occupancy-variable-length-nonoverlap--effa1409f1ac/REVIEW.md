# Review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**PASS.** For each codeword and each possible offset at which one of its
occurrences can cover a fixed coordinate, the proof defines the corresponding
stationary cylinder event.  Any two distinct such events would give either a
proper prefix--suffix overlap or strict containment of one codeword in another.
Both are excluded by the definition of a variable-length non-overlapping code.
The events are therefore pairwise disjoint, and stationarity makes the
probability of each offset event equal to the fixed cylinder probability of the
codeword.  Summing the disjoint event probabilities proves the main inequality.

The uniform-source, iid-source and mean-length corollaries were checked
algebraically.  In particular,
\[
a_k-2a_{k+1}+a_{k+2}
=\frac{(q-1)(k(q-1)-2)}{q^{k+2}}\ge0
\]
for every \(q\ge2\) and integer \(k\ge2\), so the interpolation used in the
all-alphabet Jensen argument is convex.  For \(q\ge3\),
\(xq^{-x}\) is continuously convex on \([2,\infty)\), giving the sharper
\(q^L\ge |S|L\) form.  The stated fixed-alphabet asymptotics follow by solving
\(L-\log_q L\) at first order.

## Originality

**PASS, to the best of our knowledge, with a material residual risk from older
terminology.** The directly relevant modern sources inspected include Bilotta's
variable-length construction paper, Wang and Wang's generating-function paper,
Wang and Wang's paper on maximum size and minimum average length, Qin and Luo's
2025 generalized construction, and Shen--Shangguan--Lin--Ge's constrained-coding
upper bound.  Searches also used the synonymous terms comma-free,
self-synchronizing, cross-bifix-free, mutually uncorrelated, solid code, Kraft
inequality, Bernoulli measure and stationary measure.

Wang and Wang explicitly study minimum average codeword length but use the
prefix-code entropy route.  Their earlier avoidance generating function has a
denominator of the form \(1-qx+\sum_i a_i x^i\); together with its positive-root
properties, it can yield the uniform weighted inequality by a short additional
convexity argument.  Accordingly, this review does **not** treat the mere
existence of (2) as an isolated deep novelty.  The originality claim is limited
to the explicit stationary-source formulation, its iid source-sensitive family,
and the derived fixed-alphabet mean-length consequences, including the
\(\log_q\log_q |S|\) term.

The principal unresolved literature risk is older variable-length comma-free
work.  J. A. Llewellyn's 1983 *Finite State Models in the Study of Comma-Free
Codes* (The Computer Journal 26, 303--311, DOI 10.1093/comjnl/26.4.303) and 1985
*The Construction of Variable-length Comma-Free Codes* (The Computer Journal
28, 379--390, DOI 10.1093/comjnl/28.4.379) were identifiable and their abstracts
were inspected, but their full text was not available through the inspected
sources.  Their abstracts emphasize finite-state construction, maximality and
examples rather than probability-measure or mean-length inequalities.  An
unseen equivalent theorem in those papers, or in older formal-language
literature under another name, cannot be excluded.

## Value

**PASS.** A recent paper asks directly about minimum average codeword length for
this code class.  The stationary occupancy theorem gives a compact structural
reason for additional length overhead beyond ordinary prefix coding.  For every
fixed alphabet it implies an extra \(\log\log |S|\) term up to an alphabet-
dependent bounded-order correction, and for \(q\ge3\) gives the precise
\(\log_q |S|+\log_q\log_q |S|+o(1)\) lower bound.  The stationary form also
produces a family of composition- and source-sensitive inequalities rather than
only a uniform-cardinality estimate.

## Source inspection and limitations

The modern primary-source statements defining variable-length non-overlapping
codes and discussing average length were inspected.  The 2024/2025
Goulden--Jackson work was inspected for stronger maximum-cardinality coverage;
it does not make the present average-length claim in the inspected material.
The 2025 generalized-construction work was checked for the same object and
subsequent coverage.

No claim is made that the result improves the best bound on maximum cardinality
for a prescribed maximum length.  The fixed-length specialization is weaker
than the best known non-overlapping-code cardinality bounds.  No independent
validation is asserted.
