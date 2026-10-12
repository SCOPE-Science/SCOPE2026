# Self-review

## Correctness — PASS

The statement quantifies over every countable nonempty equivalence frame with specified class-size hypotheses and every set-coded atomic assignment. In the exact-size case, search for the known \(k\) class elements terminates by hypothesis; a modal clause becomes a finite conjunction and uniform formula evaluation is computable in the existing relation and assignment, as \(\mathrm{RCA}_0\) requires. In the mixed-size case, \(\mathrm{ACA}_0\) forms the arithmetical set of worlds with a distinct class partner. Once that set is supplied, successor lists of at most two elements can be computed and the same recursive evaluation applies. Conversely, given any injection, pairing odd input-worlds with even output-worlds and adding loops produces an equivalence relation whose classes are one- or two-element. The parity assignment to \(p_0\) then makes \(\Box p_0\) on output-worlds exactly recognize nonmembership in the injection's range; the full valuation produces the range set and hence \(\mathrm{ACA}_0\). Each quantifier, class-size boundary, and modal truth clause is checked explicitly in the proof.

The embedded verifier passed all 119 labeled partitions into singleton/pair classes on up to six worlds, 5,898 one-variable assignments, 375,078 direct-versus-mate formula/world comparisons, and 30 finite range checks. The infinite theorem is proved symbolically, not by those tests.

## Originality — PASS

The closest primary source is Y. Takeda, *Frame definability in second-order arithmetic* (arXiv:2608.22822), especially Theorem 2.27: all image-finite frames have valuation extension exactly at \(\mathrm{ACA}_0\), and its reverse uses directed, generally non-reflexive partial-function frames. This already supplies the upper bound for the proposed restricted class, and the underlying idea of an injection-coded one-successor lower bound; these are not claimed as new. Y. Takeda and K. Yokoyama (arXiv:2607.01970, Proposition 2.4) use unrestricted complete relations for a weaker earlier reversal. H. M. Friedman's 2017 *Basic Emulation Theory*, Section 2, already builds singleton/pair equivalence relations to recover an injection range for an unrelated maximal-emulator principle, so the matching encoding itself is not new. None of the inspected results establishes the **S5 valuation-extension reversal for mixed singleton/pair classes together with its contrast to uniformly known exact-size classes**. These are different statements and neither reverse implication follows from the prior image-finite equivalence alone. Targeted searches identified no equivalent valuation theorem. Older terminology and unpublished work remain residual risks.

## Value — PASS

This is a natural exact comparison inside the simplest equivalence semantics for modal logic: any uniformly known finite number of worlds per information cell permits complete evaluation in \(\mathrm{RCA}_0\), while allowing unmarked singleton and pair cells demands exactly \(\mathrm{ACA}_0\). The obstruction survives with only two possible class sizes and one depth-one modal formula. Thus the result distinguishes availability of a class-size certificate from bounded size itself, a genuine foundational gap left by the recently developed image-finite valuation-extension analysis. The classification does not rest solely on a numerical example or on finite code checks.

## Residual limitations

The proof is a conventional mathematical proof, not a mechanized formal derivation. The computational checks apply only to finite frames. Closely related range-coding methods are older, and a differently named equivalent modal-valuation theorem may exist. No claim is made about arbitrary infinitely branching frames, quantified modal logic, or independently validated publication status.

Self-review: passed. Independent audit: not yet performed.
