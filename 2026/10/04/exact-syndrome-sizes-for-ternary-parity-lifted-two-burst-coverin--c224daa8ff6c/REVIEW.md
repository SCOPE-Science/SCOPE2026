# Same-model review

## Correctness
PASS. The weighted-lift reduction, syndrome-parity identity, rotation increment, prime-orbit uniformity, and signed/unsigned residue sums jointly derive the four cardinality formulas. `verify.py` checks those identities and formulas at \(p=3,5,7,11\), and directly checks the covering property at \(p=3,5,7\). The all-prime covering premise is Theorem VI.4 of Xie--Sun--Ge.

## Originality
PASS. The closest source proves the nonbinary two-burst covering construction and only a pigeonhole size guarantee. The closest exact-cardinality work computes direct \(q\)-ary differential-VT class sizes, which are not the same objects as ternary parity preimages. Searches under the exact formula, parity-lift terminology, two-burst covering terminology, and DVT aliases did not locate the four-level distribution. Residual risk remains from unindexed or inaccessible literature.

## Value
PASS. The finding replaces an existential parameter choice in a new explicit ternary covering construction by a complete exact distribution and identifies every minimizing syndrome at all odd prime lengths. Its contribution is structural and infinite-family, not merely a small computational table.

## Closest literature and limitations
The source construction is Chengfei Xie, Yubo Sun, and Gennian Ge, arXiv:2606.15379v1. Nithish Suresh Babu, Adi Krishnamoorthy, Ron M. Roth, and Paul H. Siegel study exact sizes of direct differential-VT codes at ISIT 2025. The result does not claim global optimality among all ternary covering codes, and composite lengths are outside its proved scope.

Same-model review: passed. Independent audit: not yet performed.
