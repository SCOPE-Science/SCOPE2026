# Review: Universal nine-column four-request all-symbol batch code in dimension four

## Correctness: PASS

The nine integer columns contain an identity block, so the rank is four over any field. `certificates.json` supplies signed coefficient expansions with supports disjoint across all four requests for each of the nine repeated-symbol cases and all 36 repeated-pair cases. `verify.py` reproduced all 45 bundles directly over the integers, then constructed and checked all 495 possible four-request multisets. The proof shows why these 45 primitive cases suffice: multiplicities \(3+1\) and \(2+1+1\) are handled by avoiding at most two singleton coordinates among four disjoint PIR sets, and four distinct requests use singletons. Specializing exact integer identities proves the upper bound over every field. The lower bound nine follows from Proposition 18's exact three-request optimum eight at dimension four and Proposition 10(iii)'s strict monotonicity, both in Boruchovsky et al., arXiv:2601.04041v2. No enumeration is extrapolated to an infinite field family.

## Originality: PASS, subject to stated residual risk

The full HTML of arXiv:2601.04041v2 was inspected, especially Propositions 10, 18, 24, Theorem 23, Remark 25, and Examples 26–27. Theorem 23 gives only the interval \(9\) to \(10\) for odd-field dimension-four four-request all-symbol codes, and Proposition 24 proves nine in characteristic two. The source's nine-column single-parity construction is, up to elementary equivalence, the very generator matrix used here; its construction is therefore not claimed as original. The new fact is that its specific dimension-four four-cycle instance admits *all* four-request all-symbol batch recovery identities over the integers, including odd characteristic. The source's dimension-five characteristic-three example is not an all-odd-field dimension-four result. A published mathematical record on dimension-three four-request codes concerns different rank-three objects and does not imply the rank-four theorem. Searches also considered the exact equality, all-odd-field aliases, 4x9 generator matrix, the four-cycle parity construction, and orthogonal-repair equivalences. No stronger covering result was found. A previous unindexed calculation remains possible; absence from searches is not a uniqueness proof.

## Value: PASS

The motivating 2026 paper explicitly asks for exact small-parameter all-symbol batch lengths and leaves a one-column gap for odd characteristic at dimension four. The result closes that entire prime-power family rather than a single finite-field numerical instance. It also resolves whether the smallest characteristic-two nine-column construction can retain four-request batch functionality in odd characteristic. This is a natural complete optimal-length determination with directly applicable disjoint-recovery witnesses; no downstream theorem is required to motivate this precise invariant.

## Limitations and literature

The theorem covers four requests among nine stored symbols, not arbitrary functional requests, higher dimensions, uniqueness, or all matrices realizing equality. The proof uses a published lower bound and explicit self-contained upper-bound certificates. Published coverage could be incomplete for unindexed notes or manuscripts. The abstract of the related dimension-three record was accessible, not its whole mathematical proof; the parameter mismatch is decisive for the comparison made here. See the references in `RESULT.md` and the structured comparisons in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
