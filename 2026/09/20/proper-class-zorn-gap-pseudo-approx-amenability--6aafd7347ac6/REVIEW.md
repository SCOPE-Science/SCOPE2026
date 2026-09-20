# Same-model review

## Verdict

**Same-model review: passed. Cross-model review: not yet performed.**

The finding is accepted as a proof-audit result: the Zorn step in arXiv:2609.17428v1 is not valid for the unrestricted collection used in the paper, because the paper's own closure and cardinal-enlargement construction makes that collection proper-class-sized whenever it is nonempty.

## Correctness review

The argument was checked against the full HTML text of arXiv:2609.17428v1.

The source fixes a bounded-approximate-identity constant \(d\), forms the pseudo-amenable class and its non-approximately-amenable subclass, states closure under \(c_0\)-direct sums, defines its order by one-sided \(c_0\)-summand extension plus a non-absorption condition, constructs upper bounds for chains by a \(c_0\)-sum, invokes Zorn's lemma, and then adjoins a \(c_0(I)\) of cardinality \(2^{|A|}\) to contradict maximality.

The review isolates that final enlargement before the Zorn step. If \(A\) is a counterexample and \(|I|>|A|\), then the same source facts give
\[
B=A\oplus^0c_0(I)
\]
as another counterexample. Since \(c_0(I)\) contains \(|I|\) distinct coordinate vectors, \(|B|>|A|\). This simultaneously makes \([A]\prec[B]\) for the paper's order and rules out a reverse decomposition \(A\cong B\oplus^0J'\) by cardinality. Thus every counterexample has a strict successor.

Allowing \(I\) above an arbitrary prescribed cardinal gives counterexamples of unbounded cardinality. Hence no set of representatives can contain all counterexample isomorphism types. Ordinary Zorn's lemma applies to set-valued partially ordered sets; the paper's set-indexed direct-sum argument supplies upper bounds only for set-sized chains. A proper-class analogue does not follow: the class of ordinals is the standard comparison example.

Adversarial checks included the following points.

- The conclusion does not rely on estimating the exact cardinality of \(c_0(I)\); the injection \(I\to c_0(I)\), \(i\mapsto e_i\), is enough.
- Isometric isomorphism preserves underlying cardinality.
- The reverse-decomposition clause in the source order is genuinely excluded by \(|B|>|A|\).
- Restricting to isomorphism types does not bound cardinality, and a set-sized skeleton would itself have a bounded set of underlying cardinalities.
- A fixed-universe reinterpretation is not an automatic repair, because the chain-upper-bound property must then be reverified for all chains of the restricted poset, including chains whose direct sum may leave the universe.

No claim is made that the source theorem is false.

## Originality review

Originality is assessed **to the best of our knowledge**.

The exact arXiv identifier and title were searched together with `Zorn`, `proper class`, `cardinality`, `error`, `correction`, and `gap`. Searches were also made for equivalent formulations involving pseudo-amenability, approximate amenability, bounded approximate identities, and maximality. No public correction or prior statement of this specific proper-class obstruction was located.

The source is very recent. The 2023 paper by Zhang is the cited diagnosis of the older proof gap. A 2026 University of Manitoba thesis, written before the new preprint, still records the bounded-approximate-identity implication as open. Those sources support the scientific significance of auditing the new claimed resolution, but they do not establish originality of the present set-theoretic observation by themselves.

No novelty is claimed for Zorn's lemma, the distinction between sets and proper classes, Cantor cardinal enlargement, or the general fact that the class of ordinals has no maximal element. The potentially new contribution is the application of these standard facts to the exact \(c_0(I)\)-closure mechanism of arXiv:2609.17428v1 and the resulting proof that its contradiction hypothesis itself forces a proper class of counterexample types.

The main residual originality risk is an unindexed or very recent author comment, revision, MathOverflow-style discussion, or private communication identifying the same issue.

## Value review

The source preprint explicitly presents Proposition 1 as closing a gap in a 2007 theorem and restates the claimed equivalence as its main theorem. The obstruction therefore bears directly on the central contribution of a current functional-analysis preprint.

The finding is also reusable: whenever a Banach-algebra counterexample class is stable under adjoining arbitrarily large \(c_0(I)\) summands, a global maximality argument over all isomorphism types must confront the same size obstruction.

## Limitations

- The implication “pseudo-amenable + bounded approximate identity \(\Rightarrow\) approximately amenable” is not decided here.
- No counterexample to that implication is constructed.
- The review concerns the proof in arXiv:2609.17428v1, not every possible proof of the theorem.
- No specific alternative universe/class-theoretic formalization is proved impossible; any such reformulation requires its own closure checks.
- The literature search cannot exclude very recent or poorly indexed comments and revisions.
