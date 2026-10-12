# Review of the isolated-chord/crossing-count theorem

**Correctness (PASS).** All quantifiers concern integer \(n\ge2\) uniform perfect matchings of circularly labeled endpoints. The root-arc split is an exact equivalence for a chord to be degree zero; conditional independence of the two matchings yields the crossing mean. Rotational rooting counts each chord exactly once after the factor \(n\). The resulting positive-summand formula proves strict negativity, and the first nonsimple layer together with the geometric ratio bound proves the nonzero correction limit. The standalone rational checker enumerates every matching through seven chords and verifies all conditional split cases. The asymptotic tail uses a genuine bound; finite enumeration alone is not used as an infinite proof.

**Originality (PASS with residual risk).** The most relevant inspected literature consists of Flajolet–Noy [1] on marginal components/crossings, Acan [2] on degrees, isolation and monoliths, and Paguyo [3] on separate simple-chord and crossing limit laws. The connected-crossing enumeration [4] does not tabulate this two-variable quantity. In particular, the exact simple-chord/crossing law does not cover *all* isolated chords: the difference has a proven nonzero asymptotic covariance \(-1/3\). Classical joint generating functions outside the searched corpus remain a material risk; a failed search alone does not establish originality.

**Value (PASS).** Degree-zero vertices and edge count are basic characteristics of a random intersection graph. The result supplies their exact finite dependence and resolves an asymptotically delicate distinction between simple chords and globally isolated chords. An event class with vanishing mean \(\sim 1/(2n)\) retains a nonvanishing covariance correction, relevant to second-order finite-size dependence rather than merely restating a marginal enumeration.

**Scientific limits.** Uniform labeled-circle matchings only. Classical inaccessible or unindexed mixed-statistic treatments may exist; no claim of an independent audit or a full asymptotic series.

Self-review: passed. Independent audit: not yet performed.

[1] Flajolet and Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA RR3914, https://algo.inria.fr/flajolet/Publications/FlNo00.pdf .
[2] Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, https://arxiv.org/html/1501.01489v1 .
[3] Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, https://arxiv.org/html/2104.01134v2 .
[4] OEIS A322456, https://oeis.org/A322456 .
