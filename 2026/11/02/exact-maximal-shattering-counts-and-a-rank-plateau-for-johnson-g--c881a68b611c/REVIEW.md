# Scientific review: exact maximal shattering on Johnson graphs

## Correctness — PASS

For every \(n\ge2\), \(1\le k<n\), the theorem proves an exact VC dimension and counts all extremal shattered vertex supports. The proof first derives the Boolean-interval representation of Johnson-graph geodesically convex families by a shortest-path exchange argument. A private-coordinate criterion, previously available for general Boolean boxes, is restricted to the uniform layer. The size upper bound partitions distinct coordinate witnesses into private-present and private-absent types; constructions attain it. Equality conditions force the claimed canonical three-part partition in the interior regime, with separate pure cases at ranks three and coranks three. The extremal-count formula includes the exceptional \(J(4,2)\) case.

The separately implemented finite checker reconstructs small graph-geodesic convex sets, verifies trace shattering, counts every maximum support through \(n=7\), and confirms larger explicit constructions. The proof—not the finite computation—establishes the all-parameter result. The self-review identifies no unresolved lemma preventing the conclusion.

## Originality — PASS subject to documented historical-priority risk

The previously known general Hamming/Boolean-box private-coordinate criterion already implies the preparatory support characterization after restricting to the uniform layer. **That criterion is not the original contribution.** The assessed claim is the exact rank-dependent VC dimension, the full maximum-support count, and the uniqueness/classification of all mixed and pure maximum supports.

Adler–Benediktsson–Macpherson (arXiv:2007.16042v1, 2020) study the open-neighborhood edge relation on Johnson graphs, which has universally bounded VC dimension, whereas convex-set VC dimension here grows with graph order. Chepoi (arXiv:2405.07512v1, 2024) studies the separation properties of geodesically convex halfspaces in partial Johnson graphs, not counts of maximum supports. These primary full texts were compared by claim, not merely by title. The 2022 online-learning paper of Thiessen–Gärtner could be read only at abstract level; its full theorem coverage is an unresolved risk. Search of the available mathematical research records and the checked earlier Boolean-box result uncovered no exact formula dominating this new extremal count. This is not a certificate of global novelty.

## Mathematical value — PASS

The number of maximum shattered supports is a natural finite invariant of a geometric concept class. The theorem gives all ranks and orders, a three-regime dimension plateau, explicit canonical extremizers, precise exceptional low-rank counts and a closed multinomial interior formula. These counts are not supplied by the unrestricted Hamming-box VC dimension or by the preparatory private-witness test alone; sharp analysis on the constant-weight slice is required. Such exact extremal descriptions can inform sample-support enumeration and comparisons among graph-convexity classes, without claiming any currently unproved downstream theorem.

## Limits and closest literature

The exact adaptive dimension is not proved. One relevant paper was available only via abstract. The finite verifier cannot settle unrestricted historical priority or substitute for the structural proof. See the references and comparison details in RESULT.md and AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
