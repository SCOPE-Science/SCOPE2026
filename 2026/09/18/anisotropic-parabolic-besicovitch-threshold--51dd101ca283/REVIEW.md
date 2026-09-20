# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The metric property is immediate from the representation as the \(\ell_p\)-product of \(|x-y|\) and the snowflake metric \(|t-s|^{1/\kappa}\), valid for \(p,\kappa\ge1\). The dilation \((x,t)\mapsto(rx,r^\kappa t)\) scales distances by \(r\) and Lebesgue volume by \(r^{n+\kappa}\).

For \(p<\kappa\), writing \(\sigma=p/\kappa<1\), the explicit centers
\[
x_j=a_je_1,\qquad a_j^p=\sigma(t_j+1)^{\sigma-1},
\]
and radii \(r_j=(t_j+1)^{1/\kappa}\) give a genuine infinite Besicovitch family after choosing \(t_j\) sufficiently rapidly. Concavity of \(u^\sigma\) puts the origin in every ball, while the strict inequality \((1-u)^\sigma>1-u\) and the recursive separation of the \(a_j\) put every center outside every other ball. This proves failure of w-BCP, not merely failure of the stronger form.

For \(p\ge\kappa\), the critical exponent is \(\sigma=p/\kappa\ge1\). The proof replaces the \(p/2\)-specific spatial convexity step in Dobronravov's Lemma 2.3 by the direct near-ray estimate
\[
(|x|-1)^p-|x-y|^p\ge2^{-(p+2)}|x|^{p-1}|y|
\]
whenever \(|x|\ge|y|\ge8\) and the two spatial directions have cosine at least \(0.99\). This estimate is valid for every \(p\ge1\). It yields a finite mixed large-coordinate family by forcing geometric growth of the time coordinates and then contradicting the reverse exclusion inequality. Convexity of \(u^\sigma\) gives the vertical exclusion lemma, and the same near-ray estimate gives the horizontal exclusion lemma.

The rest of the covering proof uses only translation/dilation homogeneity, disjointness of uniformly shrunken selected balls, fixed-scale packing, a finite angular partition, and greedy coloring. Replacing the homogeneous dimension \(n+2\) in the known parabolic proof by the ball-volume exponent \(n+\kappa\) is the only change in the packing calculation. The bounded-center remainder cannot occupy arbitrarily large radius buckets because the normalized target center is outside every earlier selected ball.

Boundary and consistency checks were made at \(p=\kappa\), where \(\sigma=1\) and all positive-side inequalities remain valid; at \(\kappa=2\), where the theorem reduces to Dobronravov's classification; and at \(\kappa=1\), where the metric is norm-like and the positive conclusion agrees with the classical finite-dimensional Besicovitch theorem.

## Originality

**PASS, to the best of our knowledge.**

The most relevant sources were checked against the exact metric family and equivalent formulations:

- Dobronravov, arXiv:2609.15560v1 (submitted 14 September 2026), was inspected at the theorem and proof level. It fixes the parabolic anisotropy at \(\kappa=2\) and proves the threshold \(p=2\); it does not introduce a variable anisotropy exponent or state the threshold \(p=\kappa\).
- Itoh, Hiroshima Math. J. 48 (2018), was inspected in full-text form at the theorem and introductory comparison level. It treats the max parabolic metric with the fixed square-root time scaling.
- Aimar--Forzani, Real Analysis Exchange 27 (2001/02), was checked through its explicit theorem statement, also restated by Itoh. Its balls have one common power \(q\) across coordinates with anisotropic radius exponents \(a_i\). This is a different family from \(|x-y|^p+|t-s|^{p/\kappa}\le r^p\) when \(\kappa\ne1\), so its threshold does not imply the present theorem.
- Le Donne--Rigot, J. Reine Angew. Math. 750 (2019), was checked at the relevant main theorem and graded-Abelian examples. It classifies which graded groups admit some homogeneous (quasi-)distance satisfying BCP; it does not classify this explicit mixed-power distance. Their structural result is therefore compatible with both sides of the present metric-specific dichotomy.

Exact and synonymous searches included Besicovitch covering/property, generalized or anisotropic parabolic metric/balls, mixed powers, snowflake products, homogeneous distances, and the source identifier arXiv:2609.15560. No prior statement of the \(p\ge\kappa\) classification for this metric family was located. The current SCOPE archive was also checked by source identifier, object, and claim family, with no matching record.

No source identified as highly likely to contain the same explicit classification was inaccessible at the theorem-statement level. The main residual originality risk is recency: the source preprint is only days old, so a simultaneous generalization may not yet be indexed.

The originality claim excludes the \(\kappa=2\) theorem and proof architecture of Dobronravov, Itoh's max-metric theorem, Aimar--Forzani's distinct common-power quasi-ball family, and the structural existence theory of Le Donne--Rigot. It is specifically the arbitrary-\(\kappa\) sharp classification and its mixed-power positive/negative mechanism.

## Value

**PASS.**

The theorem turns the isolated threshold \(p=2\) for the standard parabolic anisotropy into a sharp law: the Besicovitch transition occurs exactly when the temporal power \(p/\kappa\) crosses one. This identifies the analytic mechanism behind the recent parabolic result, distinguishes metric-specific BCP from structural existence of some good homogeneous metric, and supplies an explicit failure family throughout the concave regime.

## Limitations

The theorem treats a single anisotropic coordinate and finite \(p\). It does not give optimal covering constants and makes no claim for \(p=\infty\), several independently weighted anisotropic coordinates, \(p<1\), or \(\kappa<1\).

No independent validation is asserted.
