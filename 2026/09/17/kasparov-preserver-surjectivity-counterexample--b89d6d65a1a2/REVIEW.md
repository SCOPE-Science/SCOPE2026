# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The counterexample is internal to the classical Hilbert-space case. Under a unitary
identification \(H\cong H\oplus H\), the amplification \(T\mapsto T\oplus T\) is a
unital *-monomorphism, preserves compactness in both directions, and therefore
induces an injective unital *-endomorphism of the Calkin algebra. Injectivity gives
bidirectional preservation of unitaries, hence of Kasparov cycles, and unital
C*-monomorphisms preserve spectra. Properness is witnessed without any structural
classification of Calkin endomorphisms: the range commutes with the nontrivial
block projection modulo compacts, whereas the block flip does not.

The printed definition in arXiv:2609.18619v1 was checked in the PDF itself. Its
condition is automatic by choosing the existential variable equal to the image of
the universally quantified one. The standard target-surjectivity convention was
cross-checked against earlier Hilbert-module/operator-preserver literature and a
publisher-hosted 2023 paper.

The repair of the Kasparov-cycle theorem was checked independently of the source's
kernel computation. Once standard quotient-surjectivity is assumed, the induced
quotient map is surjective; bidirectional unitary preservation yields a bounded
Jordan *-homomorphism. If an element lies in its kernel, both \(1+a\) and \(1-a\)
are forced to be unitary, which gives \(a=0\). Thus the quotient map is a Jordan
*-automorphism before the prime-algebra dichotomy is invoked.

The Hamel-complement example was checked separately: it induces the identity map on
the Calkin algebra and hence preserves essential spectra, satisfies standard
quotient-surjectivity, but annihilates all compact operators. It therefore disproves
the equality conclusion in Lemma 2.6 while leaving the weaker inclusion intact.

## Originality

To the best of our knowledge, the specific defect and counterexamples have not been
published elsewhere. Searches used the exact preprint title and arXiv identifier,
"surjective up to compact operators," Kasparov-cycle preserver terminology,
essential-spectrum preservers, and amplification/Calkin-endomorphism terminology.
No correction, erratum, revised arXiv version, or equivalent counterexample was
located. The source was only recently posted, so index coverage can lag and a later
revision may supersede this observation.

The underlying amplification construction and the standard definition of
surjectivity modulo compacts are classical; originality is claimed only for applying
them to isolate this defect and for the combined repair/counterexample statement.

## Value

The issue affects the hypotheses and conclusions of the preprint's principal
Kasparov-cycle and essential-spectrum characterization theorems. The counterexample
is explicit and lives in \(B(H)\), so it does not depend on exotic Hilbert modules.
The result also identifies the standard corrected hypothesis and supplies a short
repair of the Kasparov-cycle theorem, while separating an additional overclaim about
the image of the compact ideal.

## Source-access limitations

The complete v1 source preprint was inspected, including the displayed definition
and Theorems 2.5, 2.9, 2.10. The 2023 Yu--Cao article was available from the publisher
and states the standard target-surjectivity convention explicitly. The 2012
Hejazian--Aghasizadeh article was inspected through a full-text mirror that states
the same convention. The 2009 JMAA article cited by the source was located by DOI
and abstract, but its complete publisher text was not inspected. That access gap
has low risk for the counterexample because the defect is determined by the literal
2026 v1 definition and the standard convention is independently documented by the
2012 and 2023 sources.
