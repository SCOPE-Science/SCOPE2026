# same-model review

**Overall: PASS, as a documented same-model assessment under TBOK-v1.** This is not independent validation, peer review, or a guarantee of first discovery.

## Claim audited

The computer-assisted theorem in RESULT.md completes the eventual edge-count spectrum of simple 3-uniform Berge-K_{1,5}-saturated hypergraphs for n not divisible by five. With s(n)=ceil(4n/3)-3, the spectra are [s(n),2n-4] union {2n-2} for residue 1, [s(n),2n-4] for residues 2 and 4, and [s(n),2n-5] for residue 3. The residue-zero row is explicitly prior work. The threshold is existential and inherits the threshold of [B, Theorem 3.1].

## Correctness: PASS

The proof separates the known eventual lower interval from an exact, finite-assisted upper-boundary argument. The following checks address its main failure modes.

- Berge-star containment is tested by distinct representatives for link edges. This uses incidence matching, not ordinary graph matching. The tree-component identity and augmenting-path matching agree for every local mask in the complete enumeration through order six.
- Claims 5.5-5.7 of [B] were read with their proofs. Their arguments use local neighborhoods, degree bounds, and saturation, but do not use 5 dividing the total order. The divisibility condition enters the later proof of Proposition 5.1. The reduction to at most nine residual vertices is justified in RESULT.md.
- Every non-K_5 component costs at least six deficiency. This prevents an omitted collection of small components from invalidating the residual reduction. Isolated vertices are retained and handled explicitly.
- The forbidden residual instances are (n,d)=(6,3),(7,3),(8,3),(9,3),(8,4). In each the average degree is greater than four, so fixing a maximum-degree five- or six-vertex link loses no isomorphism type. Both canonical link forms are searched.
- The original vertex-link enumeration and the independent edge-branching enumeration agree on all exclusions. The latter builds allowed links directly by matching and does not remove K_5 components. Each of its pruning rules preserves all compatible completions. Positive controls reproduce 3/3 witnesses at (6,4) and 6/0 at (9,5) in the maximum-degree-five/six branches.
- Complete enumeration of all 1,048,576 labelled six-vertex hypergraphs gives exactly the histogram {6:90,7:8400,8:1290,10:6}. It finds no nine-edge saturated graph. All smaller-order saturated examples are complete hypergraphs.
- All 40 stored seeds, including the 28 required positive certificates, passed a separately implemented subset-DP test of freeness and saturation for every missing triple. This verifier imports neither the matching checker nor the structural link characterization. It checks distinct, in-range triples as well as the claimed edge counts, residues, deficits, and rank-four flags.
- Disjoint union is used only with saturated rank-four padding components. The proof explicitly handles crossing triples. It does not assume that arbitrary saturated hypergraphs can be combined.
- The computed lantern has (order,edges,deficit)=(15,23,7), matching [B]'s formula 2+3*(binom(4,3)+binom(3,2))=23. The sun has (6,8,4). Both have all Berge degrees equal to four. The separate verifier actually performed these comparisons.
- The seed order bound and padding arithmetic give all deficits 5<=d<=n/3 for n>=56. The verifier additionally checked 31,387 construction counts. The symbolic bound proves the unlimited range; these finite arithmetic checks alone would not do so.
- The exact saturation minimum from [A, Section 3] simplifies to ceil(4n/3)-3. The minimum was also compared numerically for 296 orders. The lower interval ending at floor(5n/3) and upper interval starting at ceil(5n/3) leave no integer gap.

Residual limitations: this is a computer-assisted proof with readable finite enumerators, not a formally verified proof or a handwritten classification of every small core. The source lower-range theorem is used as a mathematical input. No explicit universal threshold or uniqueness of extremal hypergraphs is claimed. The introductory display of [B, Theorem 1.4] is inconsistent with its body; the proof here instead uses its body Theorem 3.1, Proposition 5.1 and Theorem 5.13, and the independently inspected formula in [A].

## Originality: PASS within documented scope

### Equivalent forms and containing classes

The audited claim was rewritten as the edge-count spectrum of inclusion-maximal Berge-K_{1,5}-free 3-graphs, equivalently inclusion-maximal 3-graphs of maximum Berge degree at most four. The auxiliary parameter was eliminated using Delta=6n-3m and d=2n-m. The extremal consequence was rewritten in the standard complete-block form 10*floor(n/5)+binom(n mod 5,3). These reformulations expose both the equality cases at 2n and the positive-deficiency near-extremal cases.

Searches covered saturation/edge spectra, maximal Berge-star-free hypergraphs, exact Berge-star extremal numbers, remainder and divisibility conditions, and Berge-degree terminology. Older star-forest results and recent generalizations were followed for possible stronger coverage. A source on general stars or forests was not treated as covering the target merely because the objects were related.

### Closest coverage and actual residual

**Closest spectrum result:** [B, Section 5, pp. 21-32]. Its Proposition 5.1 and Theorem 5.13 settle only the residue-zero upper boundary; Theorem 3.1 supplies the lower interval for all orders. Specializing those statements does not give the four nonzero residues. Following their proofs supplies the local deficiency machinery and the lantern construction, both credited as prior work. It still leaves the small-core exclusion cases and residue-specific seed existence. Those are the additional mathematical/computational steps performed here.

**Closest stronger structural result:** [K, Theorem 16 and proof, pp. 15-18 of arXiv:2001.05631v1]. At k=1, ell=5, uniformity 3, its uniqueness statement is for 5 dividing n and attaining the divisible bound. Its proof begins with at least the corresponding extremal number of edges and drives all relevant degrees to equality. It does not classify saturated graphs of positive deficiency. Its nondivisible ceiling bound is weaker than 2n, and the remark after the proof suggests extending the extremal construction to nondivisible orders rather than establishing it. This was a concrete coverage question, resolved by reading the statement, proof and remark. The present extremal formula is consistent with that suggestion; the spectrum claim additionally rules out and fills values below the maximum.

**General bounds:** [G, Theorem 12 and its proof via Theorem 7] gives ex<=2n, sharp at divisible orders. It does not yield the positive-deficiency exclusions by parameter substitution. [A, Section 3, Theorem 3.1 and proof] determines the minimum, not the upper spectrum. [Z, Theorems 1.10-1.11, pp. 3-4] require at least two forbidden star components and give forest bounds. [F, Section 2.1 and the inspected proof of Theorem 2.1] likewise concerns multiple components; Corollary 2.8 recovers the same divisibility-dependent star upper bound. Their inspected statements and arguments supply no stronger result settling the target.

The result is not presented as novel merely because searches missed a title. It has a definite residual beyond the closest proofs: classify feasibility at deficiency at most twelve for the nonzero residues, and provide verified upper-range seeds for every residue modulo five and deficit modulo seven. The proof framework remains substantially that of [B]. No originality is claimed for the lower interval, the minimum formula, lanterns, suns, complete-block padding, or any individual seed already present in prior work.

### Documented search and inspection record

Discovery and initial screening were completed before active research in the continuing session. Their retained search identifiers are `acba88242e9549da98fde21d66c19e8e` (discovery), `6129c70c8fbb4d069b8110c9d2af8442` (spectrum and nondivisible orders), and `69509c5dbafd4e3eb08ff0470e4d3da2` (maximal Berge stars and exact extremal/spectrum developments). The completed problem was stated before those candidate-originality searches; the exact final claim was restated before this final audit.

The final search records include:

- `dc0870ee3298481c9c28d79d473209c5`: "Berge" "saturation spectrum" stars; "Berge" "stars" "extremal" "exact" remainder. This identified the recent Berge-forest paper [F], which was acquired and inspected.
- `16b734840d984c2c943700e3e1462e0d`: the exact title of [K], plus "maximal" "Berge" "star" "spectrum". This resolved [K]'s correct DOI and identified the more general [Z], which was acquired.
- `0ac05ef478c749a690f80c0805651327`: spectrum/divisibility, extremal/remainder, and non-divisible Berge-star formulations. Many returned items were irrelevant; their presence or absence was not used as mathematical evidence.
- `504d3ea80d73490d906bd277547f8a4f`: maximal Berge-star saturation, exact divisibility results, and Berge-degree spectra. This again led to the same closest spectrum source. Minimum-saturation and linear-host results were not confused with the requested spectrum in arbitrary simple hosts.

Primary-source jobs and precise locations appear in RESULT.md's references. Particularly relevant final reads were [B] offsets 46500-69500 (local claims and upper constructions), 36700-39800 (lower-interval statement/proof), [A] 20500-28100 (saturation proof), [G] 12500-19000 and 21000-23100 (general bound and star theorem), [K] 22500-42800 (link lemma, extremal theorem and equality classification), [Z] 0-17000 (main hypotheses), and [F] 0-16000 plus its references. Excerpts were not described as whole-paper inspections.

Two timed-out search operations supplied no usable evidence. A mistaken preliminary DOI ending `2021.103506` was corrected using bibliographic search to `2022.103506`; failure of the former was not treated as source inaccessibility or novelty evidence.

### Originality scope and inaccessible sources

To the best of our knowledge, within the documented search scope and accessible literature, no equivalent or stronger prior result was found. This is not an exhaustive guarantee of novelty.

No plausible novelty-threatening work remained entirely inaccessible after alternate available acquisition routes. The publisher text of **Omid Khormali and Cory Palmer, Turan numbers for hypergraph star forests (2022), DOI:10.1016/j.ejc.2022.103506**, was not obtained through available channels: job `1e9ad3b72ada0c903e18f69615ea1523` discovered an arXiv link but returned acquisition unavailable. This work was a serious possible coverage source because of its extremal classification. Its arXiv:2001.05631v1 full text was then successfully obtained as job `cc569caf5721875c5e46984022bca5a2`; the relevant statement, proof and post-proof remark were inspected. The covering question is resolved for that accessible version, while publisher-version differences remain unverified. This is a version access limitation, not a claim that the publisher text cannot differ.

[B] and [F] were also obtained as arXiv v1 mirrors, not guaranteed latest publisher revisions. No specific evidence of a covering revision was found. There is no remaining concrete unresolved covering clue in the documented evidence. No unrelated inaccessible titles are added to a threat list. Later evidence of an equivalent or stronger prior theorem would require revising this PASS.

## Value: PASS

This completes the first nontrivial Berge-star spectrum case across all order residues, replacing an eventual result with an unresolved constant-sized upper boundary by an exact eventual spectrum. It identifies a genuine one-edge gap below the maximum for residue one, whereas residues two, three and four have complete integer spectra from the minimum to the maximum. It also determines the exact nondivisible extremal values.

The novelty is focused rather than broad: it extends an existing approach and relies on a small finite classification plus reusable seed certificates. It is more than an arbitrary computation or cosmetic change of parameters because the exclusions control every sufficiently large order, the witnesses realize entire infinite intervals, and the divisibility restriction in the established theorem is removed. The known local lemmas alone stop before the excluded residual orders, and the existing spectrum theorem alone does not establish the new boundary.

## Conclusion

Correctness, originality within the documented accessible scope, and substantive value each pass this same-model review. The finite computational dependencies and source-version limitations are explicit. The success marker records this same-model assessment only.
