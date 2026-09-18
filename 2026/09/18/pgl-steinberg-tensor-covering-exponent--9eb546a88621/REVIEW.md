# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

PASS.

The proof separates the only two inputs needed from arXiv:2609.17319v1: every nonlinear center-trivial irreducible of GL_n(q) occurs in the Steinberg square, and (outside GL_2(2)) the center-trivial linear characters form a cyclic group of order d=gcd(n,q-1). The trivial character occurs in the square by self-duality. A nontrivial center-trivial determinant character lambda cannot occur because lambda St is an irreducible distinct from St; a semisimple diagonal element on which lambda is nontrivial has nonzero Steinberg value and witnesses the distinction.

For the cube, if chi were absent then chi St would have to be supported entirely on the d-1 missing linear characters. Each such linear constituent has multiplicity at most one because its Steinberg twist is irreducible. This would force chi(1)St(1)<=d-1, contradicting St(1)=q^{n(n-1)/2}>=q>d-1. The exceptional group PGL_2(2)=S_3 is checked directly. The induction from the full cube to all higher powers is immediate from tensor reciprocity and positivity of multiplicities.

The twisted-GL corollary is an exact character twist of the full center-trivial support of St^r for r>=3.

## Originality

PASS, to the best of our knowledge.

The full text of Monteiro--Stasinski, arXiv:2609.17319v1, was inspected. It proves that St^2 contains every nonlinear center-trivial irreducible and explicitly notes that linear characters can be missing; its main construction replaces St by another irreducible sigma whose square has full center-trivial support. It does not state a Steinberg-cube theorem or an exact fixed-Steinberg covering exponent.

Heide--Saxl--Tiep--Zalesski (2013) prove full Steinberg-square support for finite simple groups of Lie type outside their unitary exceptions. This covers the simple d=1 side but not the nonsimple PGL_n(q) cases with d>1. Arad--Chillag--Herzog's character-covering number is a different group-wide invariant requiring a condition for every nontrivial irreducible; Arvind--Panja study the analogous group-wide problem for PSL_2(q). Targeted searches for "PGL_n(q) Steinberg tensor cube", "Steinberg third tensor power", "Steinberg tensor powers PGL", and equivalent covering terminology did not locate the theorem proved here.

Residual risk: the cube argument is short once the new square-support theorem is known, and an older result may encode the same conclusion under different terminology. The source preprint is also very recent, so a concurrent or subsequent author observation may supersede the novelty claim. No inaccessible source gave concrete evidence of prior coverage.

## Value

PASS.

The result turns the new qualitative square-support theorem into an exact tensor-power classification for the full adjoint family PGL_n(q). It identifies precisely why the Steinberg square fails in the nonsimple cases, proves that one additional factor always suffices, and gives the sharp dichotomy c_St=2 or 3. The twisted-Steinberg corollary simultaneously fills every compatible central-character fiber in GL_n(q) from the third power onward.

## Verification status

No independent validation, formal verification, or peer review is asserted.
