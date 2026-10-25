# Scientific review

## Correctness — PASS

The claimed domain is the 27-point ternary three-cube under inclusive Hamming threshold two. Exact complete face enumeration yields 5,949 nonempty simplices. Bitset elimination computes all eight mod-two boundary ranks, thereby bounding rational homology; the Euler characteristic fixes the sole rational Betti rank 46 in degree three. The 1,296 automorphism actions are enumerated and checked for 22 wreath classes. A vertex-orbit inclusion sum and independently signed simplex Lefschetz traces agree on each class representative. Induced rational wreath-character inner products are exact integers and give the seven stated constituents with multiplicity one, dimensions totaling 46; zero multiplicities for all other irreducibles. Reproducibility is supplied by `verify.py`.

## Originality — PASS (qualified)

Two closest full-text published results determine the **same** ternary complex's 46-sphere nonequivariant homotopy type and ordinary persistence, not its symmetry module. Antolín Camarena–Carnero Bravo formulate the relevant categorical-product question. Goyal–Shukla–Singh address other products, while Galetto–Montaño–Wellner's broader equivariant decomposition addresses binary hypercubes, not this ternary metric space. Targeted searches by the identical complex, the categorical-product alias, the full group, the 46-dimensional character, and the 22 classes did not reveal equivalent coverage. Residual novelty risk: unindexed equivalent character tables or theorem.

## Mathematical value — PASS

This is the complete rational automorphism action, not merely a restatement of a known rank. The multiplicity-free seven-irreducible decomposition detects two distinct one-dimensional sign constituents, a base-invariant line with nontrivial coordinate action, and absence of full-group invariants. A classification of all 22 class traces for a natural 27-point complex is a reusable benchmark for equivariant persistent topology and related graph-product complexes. The result is finite and exact, with no claim for larger parameters.

## Limitations

There is no integral equivariant lattice classification, infinite-parameter theorem, or independent mathematical audit. Exhaustive code is an exact certificate contingent on standard Python/integer execution. An unindexed equivalent source could affect novelty.

Self-review: passed. Independent audit: not yet performed.
