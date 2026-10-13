# Scientific assessment of the Lucas-number two-rank formula

## Correctness — PASS

The claim applies to every odd integer \(r\ge3\) over any algebraically closed field of characteristic \(2\). Coprimality of \(2^r-1\) with \(3\) establishes the three full Kummer ramification indices. The quotient involution and Deuring–Shafarevich identity are established in Timpanella, Proposition 4.6. The submitted proof independently computes a complete differential basis by valuations and genus; it then evaluates Cartier on every basis vector by exact characteristic-two identities. The stable nonzero cycles of that partial-permutation operator correspond precisely to cyclic binary words containing no \(00\), counted by the Lucas transfer matrix after deleting the all-ones word. The standalone program tests the valuations, transitions, orbit criterion and numerical formula through \(r=15\), returning `VERIFY_OK`. Finite tests do not replace the infinite proof.

## Originality — PASS, with bibliographic uncertainty

Timpanella's 2026 paper treats the exact same cyclic-dihedral family and supplies the genus, quotient equation and a general upper bound; its Proposition 4.6 does not evaluate the quotient's \(2\)-rank at \(k=2^r-1\). Borges–Gonçalves develop explicit \(p\)-rank formulas for Fermat-type covers and related examples, but the inspected text does not state the present three-point Kummer quotient's Lucas-number evaluation. Bouw's earlier general work on ramified cyclic covers is a relevant potential route to an implicit formula; only its publisher abstract and indexed excerpts were available, so this is a documented unresolved bibliographic risk, not asserted whole-document noncoverage. The new assertion is the all-parameter *closed numerical evaluation* \(2(L_r-1)\), not the previously established Kummer model, Cartier identities or quotient relation. Focused semantic-index, exact-phrase and source searches did not identify an equivalent published evaluation; absence of search results is not a proof of novelty.

## Value — PASS

The family arises naturally from the large-symmetry classification of characteristic-two curves, and its \(2\)-rank governs the etale part of the Jacobian's \(2\)-torsion. The previously known inequality leaves the exact value undetermined for an infinite family with rapidly growing genus. The Lucas expression reveals an unexpected binary-necklace law and gives exact ranks at every admissible Mersenne exponent, rather than another numerical bound or isolated example. The precise Mersenne condition is intrinsic to the periodic action of Frobenius modulo \(2^r-1\).

## Closest literature and limitations

The closest primary source is Marco Timpanella, arXiv:2609.34709v1 (2026-09-28), especially Theorem 1.2 and Proposition 4.6; a broader methods source is Borges–Gonçalves, arXiv:2212.03987v3, especially its Fermat-type rank formulas and Section 6. Bouw, *The p-rank of ramified covers of curves* (2001), is an incompletely inspected plausible source of an equivalent general cyclic-cover derivation. No assertion is made about Newton polygons, \(a\)-numbers, even exponents, or all cyclic-dihedral parameters. The assessment is not an independent audit.

Self-review: passed. Independent audit: not yet performed.
