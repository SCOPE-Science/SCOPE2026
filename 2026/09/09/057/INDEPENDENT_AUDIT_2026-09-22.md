# Independent audit — 2026/09/09/057

## Correctness — PASS

I wrote a fresh beta-number Murnaghan–Nakayama recursion using bead moves and signs counted by intervening beads, then enumerated all 3,718 partitions of 28 and the class weights 28!/z. The exact integer character inner products give g(ρ7,(14,14),(16,8,4))=0, g(ρ7,(14,14),(17,8,3))=0, and g(ρ7,(14,14),(13,8,4,3))=9, each with zero remainder on division by 28!. I independently enumerated all 80 partitions of 28 with at most three rows and computed every one of their coefficients as zero. This corroborates the central row-vanishing claim without trusting the supplied logs. The k=1,2 padded-ray counts and full 3,718-entry multiplicity row were not independently recalculated here, so those finite secondary claims have narrower audit coverage.

## Originality — PASS, narrow computational result

The checked Briand–Orellana–Rosas formulas require two two-row inputs, and Ikenmeyer's Saxl work concerns a staircase square. This mixed product's 80-entry exact zero family and local counterexample to the nominated positive are specific new finite data in the checked literature, though not a general vanishing theorem. A search cannot prove exhaustive first discovery.

## Scientific value — PASS, limited

The exact zero row constrains conjectures about mixed staircase/two-row support and offers a reproducible small test case. Its significance remains local to n=28 and the one second factor; the record supplies no mechanism or asymptotic family.

## Sources

- Original RESULT.md, METADATA.json; independent character computation described above.
- Briand–Orellana–Rosas, https://arxiv.org/abs/0812.0861 .
- Ikenmeyer, https://arxiv.org/abs/1410.6549 .
- Rosas, https://arxiv.org/abs/math/0001084 .
