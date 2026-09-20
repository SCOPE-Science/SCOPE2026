# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof was checked against the primary source arXiv:2609.19493 at the points where binary symbols enter. The q-ary extension preserves the source proof's required invariants:

1. Pairwise equality of two prescribed length-k windows has probability q^{-k}, including overlapping windows, so the k-unique family retains constant density.
2. The simple-path spectrum and shared-source lemmas use positions and equality only, not binary complementation.
3. In a q-ary run edit, the two neighboring run-boundary symbols need only be unequal to the edited symbol. Those two inequalities are exactly what the source proof uses to exclude internal intersections between the two local de Bruijn paths.
4. A separated t-deletion/t-insertion alignment therefore still yields a rule of 2t vertex-disjoint bubbles with signed entries in {-1,0,1}.
5. The random torus hash and rational-independence lemma are unchanged.
6. Exceptional alignments gain only a factor q^d from their inserted symbols, a constant for fixed q,t.
7. In the witness-description lemma, the edited symbol and any one-symbol transfer extension have q choices instead of two. These are fixed-alphabet constant factors and are absorbed by the existing polynomial description term.
8. Retaining the binary choice k=2 ceil(log_2 n)+2 preserves the source proof's n<=2^R estimate when R>L, so no hidden base-of-log change is needed.

The final selection gives |C| >= c_{q,t} q^n/[n^{2t-1} polylog(n)], which is exactly the claimed q-ary redundancy. Finite checks in `artifacts/verify_qary_local.py` independently exercise the overlapping-window count and the q-ary local endpoint contradiction for representative small alphabets and lengths.

## Originality

PASS, to the best of our knowledge.

The strongest evidence is the motivating primary source itself: after proving the binary theorem, Section 8 explicitly identifies fixed larger alphabets as an open extension and asks whether coefficient 2t-1 holds. Searches were also made using q-ary/nonbinary deletion codes, multiple deletions, fixed alphabet, 2t-1 redundancy, substring counts/spectra, and linear hashing. The current SCOPE archive was searched by the source title/arXiv identifier and by q-ary deletion terminology; no overlapping record was found.

Relevant older q-ary literature found in the search either treats explicit constructions with larger redundancy (for example Song--Cai, arXiv:2210.14006) or the different burst-deletion model. No source found states the fixed-q existential (2t-1)-coefficient theorem.

Residual risk is non-negligible because arXiv:2609.19493 is extremely recent. A near-simultaneous note, an unindexed observation, or a subsequent source revision could cover the same extension. No inaccessible paper produced concrete evidence of such coverage. The older general Levenshtein bounds were inspected only through later literature summaries rather than a complete primary-source text; this does not threaten the new claim because those bounds give the classical 2t-scale upper bound, not the 2t-1 extension.

## Value

PASS.

The result answers one of the motivating paper's explicit further questions and shows that the factor-n gain in the new existential deletion-code method is not a binary artifact. It moves every fixed q-ary alphabet from the classical leading coefficient 2t to 2t-1, while keeping the proof mechanism and lower-order scale intact.

## Scope of the claim

No novelty is claimed for the binary theorem, repeat-free-word estimates, de Bruijn spectrum reconstruction, torus linear hashing, or the bounded-witness method. The new claim is specifically the fixed-q extension and the proof that the binary-specific local-run and finite-description steps remain valid over arbitrary fixed alphabets.
