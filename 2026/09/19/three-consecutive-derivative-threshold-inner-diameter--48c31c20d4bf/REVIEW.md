# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The positive direction reduces to two established facts plus a direct integration argument:
finite interior-path diameter makes boundedness of a higher derivative propagate downward, and
MacMahon's Corollary 1.5 supplies simultaneous divergence of an unbounded holomorphic function and
its first two derivatives. Applying that result to \(f^{(a)}\) proves every set contained in
\(\{a,a+1,a+2\}\).

The negative direction was checked at the level of the explicit real-variable construction. On each
tile the central profile is quadratic, so every derivative of order at least three vanishes there;
all cutoff variation is confined to collars where the profile itself is uniformly small. The amplitude
\(A_j=j^{a+1}\) is sufficient to keep the \(a\)-fold primitive unbounded because the weighted
contribution of each middle half is bounded below by a positive constant up to a factor tending to
one. Whitney's finite-order analytic approximation theorem applies through the required finite order
\(b\). Shrinking the holomorphic continuation to a variable-width cusp preserves the two-derivative
alternative and gives a simply connected domain with uniformly bounded interior-path diameter.

Adversarial checks included the cases \(a=0\), singleton derivative sets, nonconsecutive sets of span
two, arbitrarily large gaps, and infinite index sets. For an infinite set not contained in three
consecutive integers, one pair of indices with gap at least three is enough to defeat simultaneous
divergence of the whole set.

## Originality

**PASS, to the best of our knowledge.** MacMahon's arXiv:2609.20607 is the closest source. It proves
the finite-inner-diameter characterization through derivative order two and gives a \(\{0,3\}\)
counterexample, while its final section asks for derivative-set versions of the theory. The present
result gives an exact universal classification for arbitrary nonempty derivative index sets and a
pairwise obstruction at every gap of at least three.

Targeted searches used the source title and identifier; Rubel-domain terminology; strongly unbounded
analytic functions; selected, finite, and consecutive derivative formulations; and the older work of
Rubel, Gordon, and Hinchliffe. No equivalent arbitrary-index-set classification or arbitrary-gap cusp
construction was located. Hinchliffe's 2003 abstract concerns strong unboundedness on quasidiscs and
does not by itself cover the present cusp classification.

Residual risk remains. The full text of L. A. Rubel, *Unbounded analytic functions and their
derivatives on plane domains*, Bull. Inst. Math. Acad. Sinica 12 (1984), 363-377, was not independently
inspected and is the older paper most plausibly capable of containing a selected-derivative variant.
MacMahon's preprint is also very recent, so an unindexed contemporaneous observation cannot be ruled
out.

## Value

**PASS.** The result turns the first strict Rubel-order separation into a complete threshold theorem
for all derivative index sets under the newly identified finite-inner-diameter geometry. It isolates
the exact mechanism: three consecutive derivative orders are forced, while every gap of three or more
can be destroyed. The theorem directly sharpens the geometric derivative-set question raised by the
recent source without claiming a classification for arbitrary fixed domains.

## Limitations

The result is a universal classification over simply connected finite-inner-diameter domains, not a
geometric characterization of \(\mathcal R(S)\) for every individual domain. It does not optimize cusp
regularity or quantitative divergence rates. No independent validation, formal proof-assistant
verification, or independent audit is asserted.
