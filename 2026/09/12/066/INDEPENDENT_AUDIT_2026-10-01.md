# Independent audit — 2026-10-01

## Final claim assessed

After repairing the notation, the claim is that the displayed sets \(S_{16}\) and \(S_{20}\subset C_9^2\) have the stated extension-maximal zero-sum properties, with exactly 1832 pairwise-intersecting 9-sums in \(S_{20}\), giving \(g(C_9^2)\ge17\) and \(h_2(C_9^2)\ge21\).

## Correctness — PASS

An independent exhaustive computation reproduced 0 nine-sums in \(S_{16}\), 1832 in \(S_{20}\), no disjoint pair among them, and zero bad one-point extensions for either extremal predicate. The general upper-bound lemma follows immediately by deleting one exponent-sized zero-sum and applying the ordinary Harborth definition to the remainder.

## Originality — PASS

Searches of Harborth and prescribed-length zero-sum literature did not locate these exact \(C_9^2\) witnesses, the 1832-sum pairwise-intersection census, or the disjoint-pair lower bound. Lemos–Moriya–Moura–Silva use \(g^k(G)\) for a different invariant: one zero-sum subset of size \(k\). Their notation therefore does not cover the disjoint-pair claim.

## Scientific value — PASS

The disjoint-pair threshold is a natural packing refinement of the Harborth problem, and the explicit extension-maximal witness plus complete 1832-sum intersection census is a reusable finite structural datum.

## Repair

The public files now use \(h_2(G)\) for the disjoint-pair invariant, avoiding a collision with established \(g^k(G)\) notation, and the reproducibility paths point to the actual `artifacts/` files. The mathematical witness claims are unchanged.

## Outcome

The repaired final claim passes correctness, originality, and scientific value.
