# Independent audit — Exact canonical-size census for layered torus-knot triangulations

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/exact-canonical-torus-knot-triangulation-census--831655b0b665`
**Audited tree:** `2281dd93f4d847eaef4a25be618dacc148d3e562`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

The binary-tree proof and all closed counts are correct. A positive determinant-one split matrix has componentwise comparable columns except at the stated boundary forms; subtracting the smaller column preserves positivity and determinant one and decrements both row subtraction-Euclidean lengths. The two inverse column additions are the unique binary children. This gives exactly 2^u matrices at ordered length pair (u,v), and the torus-knot parameter swap identifies the unordered knot types correctly. Independent enumeration through size 19 gives the exact sequence 1,1,3,3,...,1023 and cumulative counts 1515 and 3049.

### Independent checks

- Reproved the dominance implication q>p => s>r (and its reverse) from ps-qr=1, including the equality boundary forms.
- Checked the simultaneous subtraction parent and two column-addition children preserve determinant one and shift both row Euclidean lengths by exactly one.
- Independently enumerated the binary trees through total size 19: a_n is 1,1,3,3,7,7,...,511,511,1023; A_17=1515 and A_19=3049.
- Checked that gcd(p+q,r+s)=1 follows from the determinant and that T(P,Q)=T(Q,P) acts freely for nontrivial coprime P,Q.
- Inspected the Lin--Spreer public notebook: it contains recursive cutoff counters and the 3049/1515 assertions but not the submitted closed all-size/refined multiplicity theorem.

## Originality

PASS to the best of current searchable knowledge. Lin--Spreer arXiv:2609.14200 gives the canonical split/size construction and reports the cutoff count 3049, while its public companion notebook recursively computes cutoff counts (including 1515 and 3049) by Stern--Brocot traversal. Independent inspection of that notebook found no all-size formula a_n=2^{ceil(n/2)}-1 or refined 2^u component-size theorem. The underlying free binary monoid of nonnegative unimodular matrices is classical; originality is the simultaneous Euclidean-row-length census in this torus-knot setting.

### Literature checked

- https://arxiv.org/abs/2609.14200 — Lin–Spreer, Torus knots as loop-edges in three-sphere triangulations; source for the canonical split, size relation, cutoff census and minimality conjecture.
- https://github.com/HimalayanRainstorm/TorusKnots — Public companion notebook independently inspected; it recursively computes canonical cutoffs and Figure 6 data rather than stating the submitted all-size closed form.
- https://doi.org/10.1016/j.dam.2015.07.011 — Nathanson, classical free-monoid/Stern–Brocot background for nonnegative unimodular matrices.

## Scientific value

The result turns an isolated finite computational census into an exact theorem for every canonical size, refines it by the two component sizes, and yields a closed exponential growth law. It also gives an unconditional lower bound for actual torus-knot triangulation-complexity counts, while correctly keeping exact complexity conditional on the Lin--Spreer conjecture.

## Limitations

- The theorem counts canonical Lin--Spreer construction size, not proven minimal triangulation complexity.
- Mirrors are not counted separately, matching the positive-parameter convention.
- The binary unimodular tree is classical; the originality claim is limited to its row-length grading and torus-knot census consequence.

## Publication guard

This audit is scoped to the exact source-tree SHA above. The guarded change-set adds this independent-audit evidence pair and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
