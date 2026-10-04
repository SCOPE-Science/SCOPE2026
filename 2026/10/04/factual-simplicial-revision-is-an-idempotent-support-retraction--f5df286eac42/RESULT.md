# Factual simplicial revision is an idempotent support retraction
## Finding

Sink defines two perspective-based belief-revision operations on simplicial belief models. The first revises every belief facet ruled out by a factual announcement; the second, Grove-style variant revises only when the relevant perspective becomes isolated.

Fix a factual formula \(\varphi\), meaning a formula with no modal operators, and let
\[
F_\varphi
\]
be the set of facets satisfying \(\varphi\). Let
\[
R_\varphi
\]
denote either of Sink's two revision transformations, Definition 5.1 or Definition 5.2.

Then the following hold.

First, revision has **support success**: every facet in every updated belief subcomplex lies in
\[
F_\varphi.
\]

Second, the fixed points are exact. A simplicial belief model \(M\) satisfies
\[
R_\varphi(M)=M
\]
if and only if every belief facet of every agent already satisfies \(\varphi\).

Therefore each factual revision is idempotent:
\[
R_\varphi(R_\varphi(M))=R_\varphi(M).
\]

There is also an entailment-absorption law. If \(\psi\) is factual and
\[
F_\psi\subseteq F_\varphi,
\]
then
\[
R_\varphi(R_\psi(M))=R_\psi(M).
\]
In particular, this holds whenever the propositional implication
\[
\psi\to\varphi
\]
is valid.

Thus both revision mechanisms are retractions onto the class of belief models supported on the announced factual content. The repeated-revision oscillations discussed in the source require changing announcement content; repeating the same factual announcement cannot generate a nontrivial cycle.

## Assumptions and scope

A simplicial belief model has a fixed node set, coloring, literal assignment, and one belief subcomplex \(S_a\) for each agent \(a\). Every facet is uniquely colored.

Sink's revision definitions leave the node set, coloring, and literal assignment unchanged. Hence, for a factual formula \(\varphi\), the set \(F_\varphi\) of satisfying facets is the same before and after revision.

Definition 5.1 uses a nearness map
\[
\mathcal R_a(F,\varphi)\subseteq F_\varphi
\]
that chooses nearest \(\varphi\)-facets preserving the \(a\)-perspective. The source explicitly notes that if
\[
G\in F_\varphi,
\]
then
\[
\mathcal R_a(G,\varphi)=\{G\}.
\]

Definition 5.2 uses a Grove-style map \(\mathcal R_{a,G}\). If an already-believed \(\varphi\)-facet with the same \(a\)-perspective exists, the update selects such existing facets; otherwise it falls back to the nearness map from Definition 5.1. In either case its values lie in \(F_\varphi\).

The theorem concerns these two basic revision definitions. It does not claim the same statement for the later memory-enriched variants, whose state description is modified to record announcements.

## Proof

Fix an agent \(a\).

For Definition 5.1, the updated belief-facet set is
\[
\bigcup_{F\in F(S_a)}\mathcal R_a(F,\varphi).
\]
By definition,
\[
\mathcal R_a(F,\varphi)\subseteq F_\varphi,
\]
so every output facet satisfies \(\varphi\).

Suppose now that every facet of \(S_a\) satisfies \(\varphi\). For each
\[
F\in F(S_a),
\]
the source's self-selection property gives
\[
\mathcal R_a(F,\varphi)=\{F\}.
\]
Hence the union of all selected facets is exactly the original belief-facet set. Conversely, if some original belief facet \(F\) fails \(\varphi\), then \(F\notin F_\varphi\), while every output facet belongs to \(F_\varphi\). Therefore \(F\) disappears and the updated belief-facet set cannot equal the original one.

Thus Definition 5.1 fixes exactly the \(\varphi\)-supported belief subcomplexes.

For Definition 5.2, every selected facet again belongs to \(F_\varphi\), so support success holds.

Assume every facet of \(S_a\) satisfies \(\varphi\). For each input facet \(F\), the source's set
\[
T_a(F,\varphi)
\]
of already-believed \(\varphi\)-facets with the same \(a\)-perspective is nonempty because it contains \(F\). The Grove-style rule therefore selects \(T_a(F,\varphi)\), not a new external replacement. Each such set is contained in the original facet set \(F(S_a)\), while each input facet belongs to its own \(T_a(F,\varphi)\). Taking the union over all \(F\) gives exactly \(F(S_a)\).

Conversely, if an original facet fails \(\varphi\), it cannot occur in the output because every output facet lies in \(F_\varphi\). Hence Definition 5.2 has the same fixed-point class.

Applying either transformation once therefore produces a model in its own fixed-point class, which proves
\[
R_\varphi^2=R_\varphi.
\]

Finally, suppose
\[
F_\psi\subseteq F_\varphi.
\]
After revision by \(\psi\), every belief facet lies in \(F_\psi\), hence also in \(F_\varphi\). The fixed-point characterization for \(\varphi\) then gives
\[
R_\varphi(R_\psi(M))=R_\psi(M).
\]

Because factual truth is evaluated on the unchanged node assignment, any propositionally valid implication
\[
\psi\to\varphi
\]
implies the required inclusion of satisfying facets.

## Verification

The proof uses only three structural facts from the published definitions:

1. both revision maps output only \(\varphi\)-facets;
2. Definition 5.1 maps a \(\varphi\)-facet to itself alone;
3. Definition 5.2, when all currently believed facets satisfy \(\varphi\), selects only currently believed same-perspective facets and includes each input facet itself.

The bundled checker independently implements the nearest-facet and Grove-style rules on finite uniquely colored facet systems. It exhaustively enumerates all two-agent binary-perspective facet universes, every factual truth set, and every pair of agent belief-facet sets. It verifies support success, the exact fixed-point characterization, idempotence, and entailment absorption.

It also checks sampled three-agent binary-perspective systems. These computations corroborate the symbolic proof but are not needed for the general result.

## Relationship to prior work

Sink's August 2026 paper introduces the two revision rules and then studies iterated revision examples. It explicitly reports that changing announcements can make agents move back and forth over which worlds they consider possible, motivating later memory-enriched variants. The paper does not state the exact fixed-point class of either basic revision operator, their idempotence, or the entailment-absorption law.

The paper also identifies a systematic comparison with AGM belief revision as future work. Repeated-input stability is familiar at the belief-set level in AGM-style settings, but that background does not imply equality of the full agent-indexed simplicial belief subcomplexes produced by these new model transformations. The present statement is a direct theorem about Sink's concrete simplicial operators.

A later August 2026 preprint by Sink develops simplicial action models and incorporates belief revision into that broader framework. Its abstract and accessible summaries do not state the support-retraction law proved here; a complete comparison with every later action-model variant remains a residual literature risk.

## Limitations

The theorem is restricted to factual formulas. This matters because the revision definitions keep the underlying node assignment fixed, so factual truth sets remain stable. A modal formula can depend on the belief subcomplexes themselves and need not have a revision-invariant truth set.

Idempotence does not imply that two different factual revisions commute. Nor does it rule out the alternating behavior documented in the source when the announced information changes.

The result concerns Definitions 5.1 and 5.2, not the later memory-enriched Definitions 5.3 and 5.4.

## References

[1] Philip Sink, “Simplicial Semantics for Belief Revision,” arXiv:2608.13763, first posted 13 August 2026.

[2] Philip Sink, “Simplicial Actions for Distributed Protocols,” arXiv:2608.16881, first posted 17 August 2026.

[3] Carlos E. Alchourrón, Peter Gärdenfors, and David Makinson, “On the Logic of Theory Change: Partial Meet Contraction and Revision Functions,” *Journal of Symbolic Logic* 50(2) (1985), 510–530.
