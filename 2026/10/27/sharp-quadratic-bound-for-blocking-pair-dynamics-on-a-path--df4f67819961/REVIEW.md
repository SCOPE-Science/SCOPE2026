# Scientific review

## Correctness — PASS

The auxiliary path orientation is acyclic. Ancestor sets of distinct incoming neighbors are disjoint, proving the weight recurrence; every newly selected blocking edge replaces only immediately incoming neighbors, so the weighted matching potential rises by at least one. The selected-to-selected reachability injection into *missing* unselected-to-selected reachability pairs proves \(\Phi\le k(n-k)\le\lfloor n^2/4\rfloor\) for arbitrary matchings. A separate all-left preference construction realizes the sum of odd or even successive phase lengths, exactly \(\lfloor n^2/4\rfloor\). Exact enumeration checks all profiles for \(2\le n\le11\), and the constructive histories for \(2\le n\le80\). The finite checks are supplemental rather than a substitute for the quantified proof.

## Originality — PASS, subject to priority risks

The closest primary work, Fanelli–Moscardelli, proves forest convergence and an \(n^3/8\) total-move bound (Theorem 4), with a quadratic participation example for one agent on a branching tree (Theorem 5). It does **not** state or imply directly the sharp all-sequence \(\lfloor n^2/4\rfloor\) *total*-move law on paths. Garg–Hu's \(O(n^2)\) result addresses the existence of a favorable sequence in stable-marriage markets, not the worst adversarial path sequence. Relevant publicly indexed results about stable matching, roommate rankings, and path matching were compared by their claims rather than title resemblance, and accessible prior claims were excluded for overlap. An unseen equivalent result, including a specialized dynamic-matching paper not recovered in the searched indices, remains a priority risk.

## Value — PASS

The distinction between a *chosen* improving sequence, a per-agent participation bound, and a worst-case bound across **all** sequences is substantive. The result improves the known forest-derived cubic estimate to a tight quadratic total count on the canonical local-communication topology and supplies a reusable combinatorial potential with an exact extremal history. It quantifies the worst possible number of renegotiations without assuming a coordinator chooses advantageous blocking pairs.

## Scope and remaining limitations

Strict fixed preferences, unit-capacity partners, the path acceptability graph, and sequential blocking moves are essential assumptions. We do not claim arbitrary-tree behavior or independent mathematical certification. The publisher lists the motivating article under ECAI 2025 but gives August 25, 2026 as the first verified online release; earlier distribution remains possible. The original proof and tests are included for independent checking.

Self-review: passed. Independent audit: not yet performed.
