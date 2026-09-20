# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The metric statement was checked first. For \(a\ge1\),
\(|t-s|^{1/a}\) is a snowflake metric, and \(d_{p,a}\) is its
\(\ell^p\)-product with the Euclidean metric. The dilation
\((x,t)\mapsto(rx,r^at)\) gives exact one-homogeneity and ball-volume exponent
\(n+a\).

For \(p\ge a\ge2\), write \(q=p/a\ge1\). The positive proof was checked
against the three metric-specific lemmas in arXiv:2609.15560v1.

For the large-\(x\), large-\(t\), nearly parallel case, the source's spatial
estimate is unchanged because it depends only on the Euclidean \(x\)-term and
\(p\ge2\). Replacing the time exponent \(p/2\) by \(q\) yields
\[
c_p|x_j|^{p-1}|x_{j+1}|
\le |t_{j+1}-t_j|^q-(t_j-1)^q.
\]
Positivity forces \(t_{j+1}\ge(3/2)t_j\). The first inequality gives
\(t_2^{1/a}\ge(4/5)|x_2|\), uniformly for \(p\ge2\). After a number of steps
depending only on \(a\), the ratio \(t_j^{1/a}/|x_j|\) is large enough that
the reverse center-exclusion inequality would imply
\[
(7/5)^q\le (1/2)^q+(17/20)^q,
\]
contradicting
\[
(7/5)^q>(27/20)^q\ge(1/2)^q+(17/20)^q.
\]
This gives a cardinality bound depending only on \(a\), uniformly in
\(p\ge a\).

For bounded \(x\) and very large \(t\), choosing
\(T_a=20^a+2\) makes the convex-power lower bound
\((T_a-1)^q\) exceed the possible spatial error \(20^p\). For bounded \(t\)
and large nearly parallel \(x\), the source's contradiction remains valid
because \(q=p/a\le p/2\). The negative-time versions follow by reflection.

The standard part of the covering proof uses only homogeneity, finite
directional partitioning, a within-scale packing estimate, and the three
geometric bounds. Lebesgue measure scales as \(r^{n+a}\), so the packing step
carries over with homogeneous dimension \(n+a\). The thresholds can all be
chosen from \(n,a\) alone, which verifies the asserted uniformity in
\(p\ge a\).

For \(p<a\), the infinite family was checked directly. With \(q=p/a<1\),
the chosen radii and centers satisfy the common-origin inequality by
concavity of \(u^q\). Rapid growth of \(t_j\) makes the spatial separation
dominate the concavity deficit. The inequality
\((1-u)^q>1-u\) then gives
\[
d(c_i,c_j)^p>r_j^p\qquad(i<j),
\]
and since \(r_i<r_j\), both center-exclusion directions follow. Hence an
infinite Besicovitch family exists and w-BCP fails.

No numerical computation is needed.

## Originality

**PASS, to the best of our knowledge.**

The primary motivating source, Dobronravov arXiv:2609.15560v1, was inspected
through its theorem statements and the full proofs of the three geometric
lemmas, the standard packing argument, and the negative construction. It
treats exactly the anisotropy \(2\):
\[
(|x-y|^p+|t-s|^{p/2})^{1/p},
\]
and proves the threshold \(p=2\). No higher-anisotropy statement appears
there.

Le Donne--Rigot arXiv:1512.04936 was checked because it is the strongest
general structural prior art located. It classifies which graded groups admit
some homogeneous (quasi-)distance satisfying BCP, rather than which specific
homogeneous metrics do. The paper itself stresses the sensitivity of BCP to
the metric and does not imply the classification of the family
\(d_{p,a}\). Its explicit positive constructions are different homogeneous
distances.

Itoh's 2018 theorem concerns the standard max-type parabolic metric with time
snowflake exponent \(1/2\), not the finite-\(p\) family with arbitrary
anisotropy.

Searches covered exact and synonymous formulations involving higher-order or
anisotropic parabolic metrics, snowflake products, homogeneous distances on
Abelian graded groups, and weak/strong Besicovitch covering properties. The
current SCOPE archive was searched by source identifier, parabolic/Besicovitch
terminology, anisotropic terminology, and equivalent claim wording. No
accepted overlap or external theorem covering the stated two-parameter phase
diagram was found.

Residual risk remains because arXiv:2609.15560 is recent and the extension,
once the correct uniform constants are isolated, is relatively concise. An
unindexed contemporaneous observation is possible. No inaccessible paper was
identified whose available metadata or theorem description gave concrete
evidence of coverage.

## Value

**PASS.**

The result turns the single parabolic threshold \(p=2\) into an exact
higher-anisotropy phase diagram: for every \(a\ge2\), the transition occurs
precisely at \(p=a\). The positive constants are uniform over the entire
half-line \(p\ge a\), while below the threshold even the weakest covering
property fails. This shows that the threshold tracks the anisotropic dilation
weight itself, not a peculiarity of the quadratic parabolic case.

The theorem does not settle \(1<a<2\), does not include \(p=\infty\), and
does not claim optimal covering constants.
