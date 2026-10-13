# Thirty-five pairwise inequivalent modalities in crisp Gödel S4
## Finding
Let a modality word be a finite word over \(\neg\), \(\Box\), and \(\Diamond\), acting on a formula from right to left in the usual way.  Two words are equivalent in \(\mathsf{GS4^c}\) when their applications to every formula are equivalent in that logic.

There are at least \(35\) pairwise inequivalent \(\{\neg,\Box,\Diamond\}\)-modalities in \(\mathsf{GS4^c}\).  The certificate uses the following machine encoding: `N` means negation, `B` means box, `D` means diamond, and the empty word means the identity.  The certified representatives are

`'', 'NN', 'D', 'NND', 'B', 'NNB', 'NDN', 'BD', 'DBD', 'NNBD', 'NDNDBD', 'NNDBD', 'NDND', 'NBDND', 'DB', 'BDB', 'NNDB', 'NNBDB', 'NDNDB', 'NBDN', 'NDBDN', 'N', 'ND', 'NB', 'DN', 'NBD', 'DNDBD', 'NDBD', 'DND', 'BDND', 'NDB', 'NBDB', 'DNDB', 'BDN', 'DBDN'`.

Thus, if \(N_{\mathsf{GS4^c}}\) denotes the number of equivalence classes of full modalities, then
\[
35\leq N_{\mathsf{GS4^c}}.
\]
Pacheco's normal-form argument gives \(N_{\mathsf{GS4^c}}\leq105\), so the presently certified interval is
\[
35\leq N_{\mathsf{GS4^c}}\leq105.
\]

## Assumptions and scope
A birelational \(\mathsf{GS4^c}\)-frame is taken in the standard crisp Gödel-S4 sense: \(W\) is finite here, \(\preceq\) is a locally linear preorder, the modal relation \(R\) is a preorder, and \(R\) is forward, backward, and downward confluent with \(\preceq\).  The models are infallible, and the atomic valuation is a \(\preceq\)-upset.

For an infallible model and a truth set \(S\subseteq W\), the certificate evaluates
\[
\neg S=\{w:\text{ no }v\succeq w\text{ lies in }S\},
\]
\[
\Diamond S=\{w:\exists v\,(wRv\ \text{and}\ v\in S)\},
\]
and
\[
\Box S=\{w:\forall u,v\,(w\preceq u\land uRv\Rightarrow v\in S)\}.
\]
These are exactly the clauses used by the verifier.  A lower bound needs only valid countermodels separating the proposed words; it does not require an exhaustive enumeration of all \(\mathsf{GS4^c}\)-models.

## Proof
The file `witnesses.json` contains eight finite models.  For each model, `verify.py` first checks reflexivity and transitivity of both relations, local linearity of \(\preceq\), all three confluence conditions, and monotonicity of the atomic valuation.  Hence every listed structure is a finite birelational \(\mathsf{GS4^c}\)-model.

For each of the \(35\) modality words, the verifier then computes its truth set on the distinguished atom in each of the eight models.  This gives an eight-component fingerprint, each component itself being an exact subset of the corresponding finite world set.  The verifier checks that all \(35\) fingerprints are distinct, and additionally checks all
\[
\binom{35}{2}=595
\]
pairs explicitly.  Therefore, for every two listed modality words there is a certified \(\mathsf{GS4^c}\)-model on which their truth sets differ.  No two listed words can consequently be equivalent in \(\mathsf{GS4^c}\), proving the lower bound.

## Verification
Running `python3 verify.py` beside `witnesses.json` returns

`VERIFY_OK modalities=35 models=8 pairs=595`.

A second implementation using ordinary Python sets rather than bit masks independently replayed the same frame conditions, semantic clauses, and fingerprint distinctness.  The proof obligation is finite and exact: no random sampling, floating-point arithmetic, timeout inference, or unproved extrapolation is used.

## Relationship to prior work
Pacheco's 2026 paper studies the number of modalities in non-classical variants of \(\mathsf{S4}\).  For \(\mathsf{GS4^c}\), its full-modality finiteness proof reduces arbitrary modality words to at most \(105\) candidate forms; it does not identify an exact count or supply the present \(35\)-class lower certificate.  The older finite-model and birelational semantics papers establish the frame conditions and completeness background used here, but do not provide this quantitative lower bound.

The present result is therefore a statement-level quantitative refinement: it rules out every total count below \(35\) while leaving the source upper bound intact.

## Limitations
The exact value of \(N_{\mathsf{GS4^c}}\) is not proved.  The certificate establishes only a lower bound, and the remaining interval \([35,105]\) may contain further identifications or further inequivalent modalities.  The eight models are witnesses, not an exhaustive model census.  No claim is made about the corresponding exact counts for \(\mathsf{CS4}\), \(\mathsf{IS4}\), or \(\mathsf{GS4}\).

## References
1. Leonardo Pacheco, *Modalities in non-classical variations of S4*, arXiv:2609.00736, first submitted 2026-09-01.
2. Martín Diéguez and David Fernández-Duque, *Decidability for S4 Gödel Modal Logics*, DOI:10.1007/978-3-031-07707-4_1.
3. Philippe Balbiani, Martín Diéguez, and David Fernández-Duque, *Some constructive variants of S4 with the finite model property*, arXiv:2104.15053.
