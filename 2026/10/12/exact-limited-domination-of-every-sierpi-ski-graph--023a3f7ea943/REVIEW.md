# Scientific review: exact limited domination of Sierpiński graphs

## Correctness — PASS

The proof verifies the full parameter range \(n\ge1\), \(m\ge2\), \(1\le k\le m-1\). It handles a subtle case excluded by a naive per-clique argument: an entire base row may be empty. For each two-level block, two empty rows would leave an off-diagonal vertex undominated, and one empty row forces all other rows to exceed their minimum occupancy by one. This proves at least \(m(m-k)\) selected vertices per block. A symmetric row-regular relation with constant diagonal produces a matching upper-bound construction; its last-symbol selection is preserved along every linking edge. The complete-graph base case is checked separately. Finite checks (69 constructions; 36 exact small minima) corroborate the analytic proof.

## Originality — PASS

The closest paper is Božović, *On \(k\)-limited domination: complexity and Sierpiński graphs*, arXiv:2610.01584v1. Its Section 5 proves the \(k=1\) and \(m=3,k=2\) instances and its Section 6 states the general formula verbatim as Conjecture 12. The present proof does not assume that conjecture and covers all its remaining cases. Earlier general work on \(k\)-limited domination and its equivalent \((0,k)\)-pitchfork terminology supplies definitions/bounds but not the inspected exact result. Search-index incompleteness and lack of full-text access to one more general graph-product paper leave an explicit residual literature risk.

## Value — PASS

The theorem answers an explicit, newly stated conjecture for an entire recursively defined graph family. The two-level lower-bound mechanism is substantive because blank row cliques can be dominated from outside; the proof identifies and compensates those configurations instead of assuming each row contains selected vertices. The construction is valid uniformly, with no exceptional congruence classes. Only the claimed minimum and one family of extremizers are established, not a full census.

Self-review: passed. Independent audit: not yet performed.
