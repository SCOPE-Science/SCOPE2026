# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The local criterion rests on the exact identity
\(\mathcal Q(R)=J(R)\) for a local ring: an element outside the Jacobson
radical is a unit, and its inverse witnesses failure of quasinilpotence.
This makes generalized quasi \(t\)-fineness equivalent to surjectivity of
torsion-unit reduction onto \((R/J(R))^\times\).

For a commutative Henselian local ring with locally finite residue field,
every nonzero residue element has finite order prime to the residue
characteristic. It is therefore a simple root of \(X^n-1\) and lifts by
Hensel's lemma to a root of unity. The converse follows from torsion-unit
surjectivity. The \(\mathbb Z_{(p)}\) classification follows because the
only rational roots of unity are \(\pm1\); the \(\mathbb Z_p\) statement
follows from completeness and Henselianity.

The matrix obstruction was checked separately. Quasinilpotence over the
commutative local base forces nilpotent reduction. If
\(aI_n=U+Q\), the reduction of the finite-order rational matrix \(U\) has
characteristic polynomial \((X-\bar a)^n\). A finite-order rational matrix
has cyclotomic characteristic factors, and reduction of
\(\Phi_{dp^s}\), \((d,p)=1\), has the primitive \(d\)-th roots as its
distinct roots. A single distinct residue root therefore forces
\(\varphi(d)=1\), hence the residue root is \(\pm1\), contradicting the
chosen scalar for \(p\ge5\).

## Originality

**PASS, to the best of our knowledge.** The primary source
arXiv:2609.19882v1 was inspected in full, especially Section 3. It introduces
generalized quasi \(t\)-fine rings, records the commutative identity
\(\mathcal Q(R)=J(R)\), gives \(F[[x]]\) for finite \(F\) and
\(\mathbb Z_{(2)}\) as examples, proves center-locality, and gives matrix and
group-ring results. It does not state the local torsion-lifting criterion,
a Henselian characterization, the \(\mathbb Z_{(p)}\) classification, the
completion contrast, or the all-size mixed-characteristic matrix
obstruction.

Targeted searches for the new terminology together with Henselian rings,
residue fields, roots of unity, \(p\)-adic integers, localizations
\(\mathbb Z_{(p)}\), and matrix rings located the source preprint but no
prior statement of these results. Older literature on Hensel lifting and
periodic division rings supplies standard ingredients rather than the new
generalized quasi \(t\)-fine conclusions.

No inaccessible paper was identified as especially likely to contain the
same theorem. The main residual originality risk is contemporaneous work or
a later revision of the very recent source preprint, and older ring-theory
literature expressing the torsion-lifting mechanism without the new
terminology.

## Value

**PASS.** The source explicitly notes difficulty in characterizing the new
generalized quasi \(t\)-fine class. The result gives a complete criterion for
local rings and a residue-field-only classification for commutative
Henselian local rings. It also separates localization from completion
sharply: \(\mathbb Z_{(p)}\) fails for every \(p\ge5\), while \(\mathbb Z_p\)
always succeeds. The matrix obstruction shows that the source's
positive-characteristic matrix permanence cannot be extended naively to
mixed characteristic, even over the simplest localizations of \(\mathbb Z\).

## Scope and limitations

The result does not classify generalized quasi \(t\)-fine matrix rings over
arbitrary Henselian bases and does not assert that the property is Morita
invariant. The periodic-division-ring conclusion and all Henselian lifting
facts are treated as prior art. No independent validation is asserted.
