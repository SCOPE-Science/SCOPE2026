# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The construction was checked at the level of the defining cell recurrence rather
than by importing the closed two-parameter formula from the planar source.

The key identities are internally consistent:

- the recursive rule is equivalent to
  \(m_{\mathbf r}=\theta S_{\mathbf r}\) away from the origin;
- increasing one coordinate introduces at most
  \(\prod_{j\ne i}(r_j+1)\) new cells, giving the uniform \(4/3\) growth bound
  from the choice \(\theta(D+1)^{n-1}\le1/4\);
- the anchored \(A_p\) calculation reduces to a convergent product-geometric
  series with ratio \(2^{-p}(4/3)^{p-1}<1\);
- the two-cell rectangle \(R_{e_1}\) supplies the matching
  \(\theta^{1-p}\) lower characteristic;
- the identity
  \(S_{\mathbf r}=1+\theta\sum_{0<\mathbf u\le\mathbf r}S_{\mathbf u}\)
  yields \(S_{\mathbf r}\le2\) throughout the stated hyperbolic region;
- a dyadic divisor count in the truncated box
  \(1\le r_i\le D\), with \(D\asymp\theta^{-1/(n-1)}\), gives
  \(\#\mathcal H_\theta\gtrsim\theta^{-1}\log^{n-1}(1/\theta)\);
- the test \(f=\sigma\mathbf1_Q\) has exact unit \(L^p(w)\) norm and every
  hyperbolic output cell contributes
  \(\gtrsim\theta^{1-p}\);
- the coordinatewise averaging and reflection lemmas use comparison intervals
  depending only on the geometric interval, so the same anchored/reflected
  rectangle works simultaneously for \(w\) and its dual.

The resulting lower norm is
\[
\theta^{-1}\log^{(n-1)/p}(1/\theta),
\]
and \([w]_{A_p^{\rm str}}\asymp\theta^{1-p}\), giving the stated formulation in
terms of the weight characteristic.

Stress checks against limiting cases were also performed. For \(n=2,p=2\) the
construction reproduces Lerner's scale
\(A\sqrt{\log A}\). The proof remains valid for all fixed \(p>1\): the only
geometric-series ratio is strictly below one throughout that range. The theorem
is compatible with the recent Ombrosi--Rey upper power bounds, which remain
strictly above the endpoint power \(1/(p-1)\).

No computer-assisted argument is needed for the proof.

## Originality

**PASS, to the best of our knowledge.**

The closest source is Lerner, arXiv:2609.14008v1. Its theorem is stated for the
strong maximal operator on \(\mathbb R^2\) at \(p=2\), and the introduction says
that the note concentrates on that case for simplicity. The proof contains the
two-parameter mass recurrence, anchored averaging lemma, and reflection device
used as inputs here, but it does not state the all-\(p\), all-dimensional lower
bound or the exponent \((n-1)/p\).

Ombrosi--Rey, arXiv:2609.17246v1, submitted three days later, treats every
\(1<p<\infty\) and every dimension in the *upper-bound* direction. Its
introduction explicitly cites Lerner's \(\mathbb R^2,p=2\) logarithmic lower
bound as the recent lower-bound result before presenting improved upper power
exponents. This is strong evidence that an all-\(p\), all-dimensional
logarithmic lower bound was not already part of the immediately surrounding
literature at that date.

Searches were made for combinations and synonymous formulations involving
"strong maximal operator/function", "rectangular \(A_p\)", logarithmic lower
bounds, endpoint power \(1/(p-1)\), arbitrary \(p\), higher dimensions, and the
source identifier 2609.14008. Searches through the newest available material
did not identify the theorem stated here. Older nearby literature concerns
membership/characterization of strong \(A_p\), reverse Hölder properties,
upper bounds, endpoint unweighted Orlicz behavior, or weighted weak-type
inequalities rather than this quantitative lower construction.

The current SCOPE archive was searched by the source paper, object, claim family,
and equivalent terminology; no overlapping accepted record was found before
publication.

Residual risk remains because both motivating preprints are very recent and an
unindexed contemporaneous extension could exist. The extension is conceptually
natural once Lerner's recurrence is available, so the originality claim is
deliberately limited to "to the best of our knowledge." No inaccessible paper
was found whose available title/abstract supplied concrete evidence of prior
coverage.

## Value

**PASS.**

The theorem turns a single planar Hilbert-space counterexample into a uniform
structural obstruction for the full strong-maximal \(A_p\) scale. In addition,
the direct \(n\)-parameter recurrence gives a dimension-dependent logarithmic
gain \((\log A)^{(n-1)/p}\), exposing the same \(n-1\) multiparameter complexity
that appears in divisor-type and strong-maximal endpoint phenomena. This is
stronger information than merely propagating failure from one exponent or
embedding a two-dimensional example into higher dimension.

The result does not settle the optimal power exponent, and no such claim is made.
