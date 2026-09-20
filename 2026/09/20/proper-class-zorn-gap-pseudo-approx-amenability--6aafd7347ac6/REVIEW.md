# Same-model review

## Verdict

Same-model review: passed. Cross-model review: not yet performed.

The finding is accepted as a proof-audit result. The Zorn step in arXiv:2609.17428v1 is not valid for the unrestricted counterexample collection used there, because the paper's own c0-sum and cardinal-enlargement construction makes that collection proper-class-sized whenever it is nonempty.

## Correctness

The source fixes a bound d, forms the non-approximately-amenable pseudo-amenable classes with bounded approximate identity bound at most d, states closure under c0-direct sums, orders the counterexample types by adjoining c0-summands subject to a reverse-absorption condition, constructs upper bounds for chains, invokes Zorn's lemma, and then adjoins c0(I) with cardinality larger than the alleged maximal algebra.

The last enlargement can be applied to every counterexample, before any maximality argument. If A is a counterexample and |I|>|A|, the source's own closure facts give B=A+_0 c0(I) as another counterexample. The injection i -> e_i gives |c0(I)|>=|I|, hence |B|>|A|. This also rules out any reverse decomposition A isomorphic to B+_0 J', so [A] is strictly below [B] for the source order.

Choosing I above an arbitrary prescribed cardinal produces counterexamples of unbounded cardinality. Therefore no set of Banach algebras can contain one representative of every counterexample isomorphism type. The source's direct-sum construction supplies upper bounds only for set-indexed chains. Ordinary Zorn's lemma does not turn that property into a maximal element for a proper-class collection; the class of all ordinals is the standard comparison.

Checks were also made that the argument does not require the exact cardinality of c0(I), that isometric isomorphism preserves underlying cardinality, and that a fixed-universe reinterpretation would require a new verification of the chain-upper-bound property inside the restricted universe.

No claim is made that the amenability implication itself is false.

## Originality

Originality is assessed to the best of our knowledge. Searches by the exact preprint identifier and title, together with Zorn, proper class, cardinality, error, correction, gap, pseudo-amenability, approximate amenability, and bounded approximate identity did not locate a public correction or prior statement of this specific obstruction.

The set/class distinction, Cantor cardinal enlargement, Zorn's lemma, and the ordinal comparison are standard prior art. The potentially new contribution is their application to the exact c0(I)-closure mechanism of arXiv:2609.17428v1.

The main residual risk is a very recent or poorly indexed author comment, revision, or discussion identifying the same issue.

## Value

The source presents Proposition 1 as closing a gap in a 2007 theorem and restates the claimed equivalence as its main theorem. The obstruction therefore bears directly on the central contribution of a current functional-analysis preprint. The same size mechanism is reusable in maximality arguments over Banach-algebra classes closed under arbitrarily large c0-sums.

## Limitations

- The implication pseudo-amenable plus bounded approximate identity => approximately amenable is not decided here.
- No counterexample to that implication is constructed.
- The review concerns arXiv:2609.17428v1; an unrelated proof could exist.
- No particular alternative universe or class-theoretic reformulation is ruled out without additional closure checks.
- Very recent or poorly indexed comments or revisions may not have been found.
