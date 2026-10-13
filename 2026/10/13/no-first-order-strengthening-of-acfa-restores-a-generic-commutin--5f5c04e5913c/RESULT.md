# No first-order strengthening of ACFA restores a generic commuting automorphism
## Finding

Let \(L_\sigma\) be the language of difference fields and let \(R\) be any consistent \(L_\sigma\)-theory satisfying
\[
\mathrm{ACFA}\subseteq R.
\]
No completeness assumption on \(R\) is required.

Let \(R_\tau\) denote the theory obtained by adjoining a new automorphism \(\tau\) of the \(L_\sigma\)-structure. Since \(\tau\) must preserve the distinguished automorphism, this says
\[
\tau\sigma=\sigma\tau.
\]

Then
\[
R_\tau\text{ has no model companion.}
\]

Consequently, adding arbitrary consistent first-order axioms in the original difference-field language cannot restore a model companion for a second commuting automorphism once ACFA is present.

## Assumptions and scope

The extension \(R\supseteq\mathrm{ACFA}\) is taken in the same language \(L_\sigma\). The theorem concerns arbitrary consistent first-order strengthenings, including incomplete ones.

The notation \(R_\tau\) follows the standard generic-automorphism convention: models of \(R\) are expanded by an automorphism \(\tau\) of the whole \(L_\sigma\)-structure. For a difference field this is exactly a field automorphism commuting with \(\sigma\).

The conclusion is nonexistence of a model companion. It does not assert nonexistence of existentially closed expansions as individual structures, nor does it concern arbitrary language expansions that add new nondefinitional structure before \(\tau\).

## Proof

ACFA is a model companion, hence is model-complete. Model-completeness is inherited by extensions in the same language: if
\[
\mathrm{ACFA}\subseteq R
\]
and \(M\hookrightarrow N\) is an embedding between models of \(R\), then \(M\) and \(N\) are models of ACFA, so the embedding is elementary. Therefore \(R\) is model-complete.

Because \(R\) is consistent, choose any complete consistent theory \(R'\) extending \(R\). Then
\[
\mathrm{ACFA}\subseteq R',
\]
so \(R'\) is a completion of ACFA.

Beyarslan and Kowalski prove in their Theorem 1.2 that for every completion \(T\) of ACFA, in arbitrary characteristic, the theory obtained by adjoining a second commuting automorphism has no model companion. Applying this to \(R'\) gives
\[
(R')_\tau\text{ has no model companion.}
\]

Their Corollary 6.2 gives the transfer in the opposite direction: if a model-complete theory \(S\) has \(S_\tau\) with a model companion, then for every completion \(S'\) of \(S\), the theory \((S')_\tau\) has a model companion.

Apply that transfer with \(S=R\). If \(R_\tau\) had a model companion, then \((R')_\tau\) would have a model companion, contradicting Theorem 1.2. Hence
\[
R_\tau\text{ has no model companion.}
\]

Since \(R\) was an arbitrary consistent same-language extension of ACFA, the obstruction survives every such first-order strengthening.

## Verification

The recent source was inspected at Theorem 1.2 and at the model-complete-reduct transfer statement in Corollary 6.2. Theorem 1.2 quantifies over every completion of ACFA. Corollary 6.2 quantifies over every completion of a model-complete reduct whenever the automorphism expansion of that reduct has a model companion.

The only additional logical step is the elementary inheritance fact used above: any same-language extension of a model-complete theory is model-complete. This follows immediately because embeddings between models of the stronger theory are, in particular, embeddings between models of the weaker model-complete theory.

No computation, finite experiment, or unverified infinitary argument is used.

## Relationship to prior work

Beyarslan--Kowalski explicitly prove the nonexistence theorem for every completion of ACFA, and they separately develop a transfer theorem from a model-complete theory to all of its completions. Their introduction also explains why older arguments did not settle every completion in every characteristic.

The checked source does not state the present closure consequence for arbitrary, possibly incomplete, consistent extensions \(R\supseteq\mathrm{ACFA}\). Combining its two results with upward inheritance of model-completeness removes the completeness hypothesis entirely.

This differs from earlier general obstruction theorems for theories with automorphisms, such as results assuming the strict order property or amalgamation hypotheses. The conclusion here uses the new all-completions ACFA theorem and applies uniformly to every same-language strengthening of ACFA, without imposing those extra hypotheses on \(R\).

## Limitations

The result is specific to same-language first-order extensions of ACFA. It does not say that every expansion of ACFA by additional predicates, functions, sorts, or other structure has the same obstruction.

The proof establishes nonexistence of a model companion, not a classification of existentially closed \(R_\tau\)-models in a non-elementary framework.

The claim is a structural corollary of two results in one recent paper plus the standard inheritance of model-completeness. Its mathematical value is the removal of all completeness restrictions on the base theory, rather than a new construction of the underlying obstruction.

## References

[1] Özlem Beyarslan and Piotr Kowalski, “PAC fields and difference fields with generic automorphisms,” arXiv:2609.40251v1, first posted 30 September 2026. See Theorem 1.2 and Corollary 6.2.

[2] Hirotaka Kikyo, “Model companions of theories with an automorphism,” *Journal of Symbolic Logic* 65 (2000), 1215–1222.

[3] Tapani Hyttinen and Kaisa Kangas, “An AEC framework for fields with commuting automorphisms,” arXiv:1904.10828; *Annals of Pure and Applied Logic* 174 (2023), 103191.
