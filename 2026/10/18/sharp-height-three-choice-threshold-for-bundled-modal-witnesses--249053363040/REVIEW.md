# Scientific review: sharp height-three choice threshold

## Correctness — PASS
The proposition has precise ZF quantifiers over all sets, valuations and one fixed \(\Box\Diamond(+)\) term on rooted partial orders of height at most three. The generated-neighborhood definition exactly creates one choice of a diamond witness for each successor of the root; compatibility is equivalent to a selector \(f:W\to P\) with \(u\le f(u)\). Semantics requires only \(\forall u\,\exists v\in P\,(u\le v)\). The three-level root/middle/leaf construction produces these separate existential witnesses from any family of nonempty sets without using choice, while a simultaneous generated certificate extracts a choice function. Conversely AC directly supplies the selector. The depth-one case is discharged by deterministic first-compatible-entry selection from a finite syntactic list; the height-two case explicitly chooses the root witness and uses each other world's self-loop. Check the term definitions against Ding–Yang [1, Definitions 2.3–2.4, 3.1].

The reproducible standard-library checker reports `FINITE_VERIFY_OK rooted_orders=51 valuations=1414 height_two_positive=9`. This is a finite consistency check and does not prove the ZF statement; the unrestricted reasoning is the written proof.

## Originality — PASS, with residual risk
Ding and Yang [1, Proposition 3.2] use AC for the general semantic-to-certificate implication and explicitly say AC is indispensable for their proof. No inspected statement proves the **reverse equivalence to full AC for a single fixed unary-depth-two bundle**, much less locates the exact height-two/height-three cut. This is a stronger mathematical assertion than an observation about a particular proof. Searches of published mathematical records for alternate selector formulations and comparison with accessible neighborhood background did not find an equivalent earlier theorem. The result can still coincide with a different older formulation in the mathematical logic of selection principles, so this is not a guarantee of worldwide uniqueness.

## Value — PASS
The source's central generated-neighborhood representation raises a genuine foundational question: is its reliance on choice a removable artifact or an intrinsic demand? The theorem supplies a complete sharp answer in a sparse structural class, and gives two explicit choice-free boundaries. The exact minimal frame height, fixed two-modal term, and arbitrary-family reduction matter to understanding when the representation can be used in constructive or choice-free foundations. It is not merely a finite test or a renaming of the axiom of choice; the nontrivial frame/term restrictions are essential.

## Limitations and sources
[1] Y. Ding and Y. Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268 (first posted 27 March 2026), especially v2, Definitions 2.3–2.4, 3.1, Proposition 3.2 and its proof, Section 6 and relevant appendices. https://arxiv.org/html/2603.26268v2

[2] H. H. Hansen, C. Kupke, E. Pacuit, *Neighbourhood Structures: Bisimilarity and Basic Model Theory*, arXiv:0901.4430 (2009), introductory and semantics material checked as background, not assumed to exhaust all equivalence results. https://arxiv.org/abs/0901.4430

[3] *Does DC Imply AC-omega, Uniformly?*, Journal of Symbolic Logic 90(4), 2025, consulted for the logical distinction among choice principles, not as a source for the bundle theorem. https://doi.org/10.1017/jsl.2024.33

Residual originality risk: a logically equivalent result may be available under a strategy, family-selector or semantic representation formulation that does not use the same bundle terminology. The finite checker cannot discharge such a literature gap.

Self-review: passed. Independent audit: not yet performed.
