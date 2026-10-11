# One-dimensional characters of the generic once-punctured-torus PGL2 skein algebra
## Finding
Let \(q\in\mathbb C^*\) satisfy \(q^4\neq1\) and \(q^6\neq1\). For the once-punctured-torus \(\mathrm{PGL}_2\) skein algebra in Theorem 32 of Ellison--Higgins--Sandey--Sylvester, every unital one-dimensional representation \(\chi:\mathcal S_q^Y(\Sigma_{1,1})\to\mathbb C\) is obtained as follows. Put \(\alpha=2-q-q^{-1}\), \(\beta=2-q^2-q^{-2}\), \(\gamma=2-q^4-q^{-4}\), and \(\nu=2+q+q^{-1}\). Then \( (\chi(a),\chi(b),\chi(c))\) is either \( (s,s,s)\) with \(s\in\{0,\alpha,\gamma,\nu\}\), or a permutation of \( (0,\beta,\beta)\), or a permutation of \( (\gamma,\beta,\beta)\). In every case \(\chi(h)=\frac{q}{q^2+1}\bigl(\chi(a)\chi(c)+(q^2-1)(\chi(a)-\chi(b)+\chi(c))\bigr)\). These listed assignments satisfy all defining relations, and no other one-dimensional representations occur under the stated hypotheses.

Thus the character set of this noncommutative skein algebra is finite for every parameter in the stated generic range. The displayed list is a set-theoretic classification; at isolated additional parameter values some displayed points can coincide, so no assertion of ten distinct characters is made without further exclusions.

## Assumptions and scope
The parameter is a nonzero complex number \(q\) with \(q^4\neq1\) and \(q^6\neq1\). The algebra is the once-punctured-torus \(\mathrm{{PGL}}_2\) skein algebra \(\mathcal S_q^Y(\Sigma_{{1,1}})\) with generators \(a,b,c,h\) and the relations of Theorem 32 in arXiv:2610.01075v1. A one-dimensional representation means a unital complex-algebra homomorphism to \(\mathbb C\). The standard deformed-commutator convention is \([x,y]_r=rxy-r^{{-1}}yx\).

## Proof
Write the scalar images again as \(a,b,c,h\). Because scalars commute, the third \(q^2\)-deformed commutator relation reduces, after cancelling factors nonzero under \(q^4\neq1\), to
\[
(q^2+1)h=q\bigl(ac+(q^2-1)(a-b+c)\bigr). 
\]
Hence \(h\) is forced by \(a,b,c\).

Substituting this expression into the difference of the first two deformed-commutator relations gives
\[
(a-c)\bigl(q^2b+(q^2-1)^2\bigr)=0.
\]
Set \(\beta=-(q^2-1)^2/q^2=2-q^2-q^{{-2}}\).

First suppose \(a=c\). The first deformed-commutator relation factors as
\[
(a-b)\bigl(q^2a+(q^2-1)^2\bigr)=0.
\]
If \(a=b=c=s\), the cubic defining relation factors, up to a nonzero scalar, as
\[
s\bigl(-sq+(q+1)^2\bigr)\bigl(sq+(q-1)^2\bigr)\bigl(sq^4+(q^4-1)^2\bigr)=0,
\]
so \(s\in\{0,\nu,\alpha,\gamma\}\). If instead \(a=c=\beta\), the cubic relation factors, again up to a nonzero scalar, as
\[
b(q^2-q+1)(q^2+q+1)\bigl(bq^4+(q^4-1)^2\bigr)=0.
\]
The assumption \(q^6\neq1\) makes the two cyclotomic factors nonzero, leaving \(b=0\) or \(b=\gamma\).

Now suppose the other factor of the first branching identity vanishes, so \(b=\beta\). The first deformed-commutator relation becomes, up to a nonzero scalar,
\[
\bigl(q^2a+(q^2-1)^2\bigr)\bigl(q^2c+(q^2-1)^2\bigr)=0.
\]
Thus \(a=\beta\) or \(c=\beta\). In the first case the cubic relation factors, up to a nonzero scalar, as \(c(q^2-q+1)(q^2+q+1)(cq^4+(q^4-1)^2)\), so \(c\in\{0,\gamma\}\); the second case is symmetric and gives \(a\in\{0,\gamma\}\). These are exactly the six permutations of \((0,\beta,\beta)\) and \((\gamma,\beta,\beta)\).

The symbolic verifier substitutes every listed point into all seven scalarized defining relations and separately checks each factorization used in the completeness argument.

## Verification
Run `python artifacts/verify.py`. The expected terminal line is `VERIFY_OK candidates=10 scalar_relations=7 completeness_branches=6`. The script performs exact symbolic simplification over rational functions in \(q\); it does not infer an infinite statement from numerical sampling.

## Relationship to prior work
Ellison, Higgins, Sandey and Sylvester give the finite presentation, prove it is an isomorphism, and describe bases, multiplication on the closed torus, centers, and puncture-filling kernels. Their stated results do not classify one-dimensional representations of the once-punctured-torus algebra. Targeted searches for one-dimensional representations, characters, abelianization, the exact source identifier, and the displayed parameter expressions found no covering statement. Work relating the ordinary Kauffman-bracket skein algebra of the punctured torus to DAHA concerns a different algebra and does not imply the above finite list for the new \(\mathrm{{PGL}}_2\) presentation without this calculation.

## Limitations
The classification deliberately excludes \(q^4=1\), where the source presentation hypothesis fails, and \(q^6=1\), where the completeness factorization has extra cyclotomic branches. It does not classify higher-dimensional simple modules, determine the primitive spectrum, or claim that all ten displayed formula-points are pairwise distinct for every allowed \(q\).

## References
1. C. Ellison, V. Higgins, M. Sandey, E. Sylvester, “PGL2 skein algebras of small surfaces,” arXiv:2610.01075v1, first public 2026-10-01, Theorem 32 and Section 4.3. https://arxiv.org/abs/2610.01075
2. K. Hikami, “DAHA and skein algebra on surface: double-torus knots,” arXiv:1901.02743, for surrounding once-punctured-torus Kauffman-bracket/DAHA context. https://arxiv.org/abs/1901.02743
