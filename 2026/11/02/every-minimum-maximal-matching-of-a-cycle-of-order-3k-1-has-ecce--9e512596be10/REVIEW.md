# Scientific review of the cycle matching eccentricity theorem

## Correctness — PASS

The claim is quantified for every integer \(k\ge2\) and every minimum maximal matching in the labelled cycle \(C_{3k+1}\). The original edge problem is reduced to the already established bracelet graph and then to two separated particles by the invertible map \(j\mapsto-kj\pmod {3k+1}\). The upper-bound proof divides every pair of configurations into the shared-point, alternating-four-point and grouped-four-point cases, with constructive paths of at most \(\lfloor(3k+1)/2\rfloor\) steps. The lower-bound proof gives, from every pair, a feasible target whose minimum unrestricted assignment transportation cost already equals that bound. Both Python programs were executed against the exact scientific statements, including all source states in their indicated finite ranges. The general proof does not depend on the finite tests.

## Originality — PASS, qualified

The 2022 thesis of Teshima and the 2023 article of Brewster, Mynhardt and Teshima establish the full bracelet graph, its vertices and allowed exchanges. Those predecessors therefore cover the coordinate description and preclude claiming the graph identification, degrees, or counts as new. The cycle sections of both full texts were inspected; the former's Section 4.4–4.5 and the latter's Section 3 discuss graph structure and Hamiltonicity rather than the exact common eccentricity. The 2010 paper on independent-set token reconfiguration and the 2014 paper on dominating-set reconfiguration motivate the exact metric question but do not give this formula. Mathematical-record comparisons did not identify an equivalent all-vertex sharp distance theorem. This is best-knowledge originality, not proof of absolute uniqueness; an unindexed equivalent particle metric remains a risk.

## Value — PASS

Distances measure the minimum number of feasibility-preserving changes among optimal configurations, a central reconfiguration invariant. It is not implied by knowing only the counts, local degrees, or connectivity. The result gives an exact infinite-family metric bound attained from *every* starting configuration, despite distinct degree-two and degree-four classes, and makes the obstruction constructive rather than merely asymptotic. The scope is narrow but natural: all optimal edge-dominating matchings on labelled cycles of one residue class. No broader graph-family result is asserted.

## Sources and residual risks

Primary inspected sources: Kamiński–Medvedev–Milanič (arXiv:1008.4563, introduction and independent-set model); Suzuki–Mouawad–Nishimura (arXiv:1401.5714, introduction and distance motivation); Teshima (hdl:1828/14602, thesis Chapter 4 sections 4.3–4.5, especially Lemma 4.11 and Theorem 4.12); Brewster–Mynhardt–Teshima (arXiv:2303.08190, full relevant cycle/bracelet sections and Hamiltonicity). The principal residual originality risk is a differently named historical graph-metric calculation; the theorem is not externally validated. The pairwise assignment-distance equality supported experimentally by the second checker is not included among the proved findings.

Self-review: passed. Independent audit: not yet performed.
