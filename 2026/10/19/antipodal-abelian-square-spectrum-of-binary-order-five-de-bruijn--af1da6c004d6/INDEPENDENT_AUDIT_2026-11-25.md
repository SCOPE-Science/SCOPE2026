# Independent mathematical audit

## correctness

PASS

All 32 possible length-five factors occur once, so there are 16 ones in a period. If f_i is the length-16 window weight minus eight, then f_(i+16)=−f_i and adjacent f values differ by at most one. This proves a nonzero even count of starts, with no assumption of reversal or complement identification. Each rotation class corresponds to one Euler tour of the order-four graph starting at its unique zero edge; the frozen local successor permutations and unused-edge traversal both cover it. For an independent exhaustive check, enumerate all 32,768 choices of outgoing-edge orders at the nonzero vertices, fixing the order 0 then 1 at vertex zero. Each anchored tour induces exactly one accepted choice of orders and each choice that exhausts the graph yields one anchored tour. Verify all cyclic factors and full weight, compute H by sliding the length-16 sum, and normalize orbits by lexicographically smallest rotations. This reproduces the eleven frequencies 300,316,436,256,294,182,120,70,34,32,8, all per-row orbit columns, the 528 group orbits, and mean 1985/256 and variance 1278079/65536. The only nontrivial transformation fixing a rotation class is reversal followed by complement (64 fixed classes); this independently explains the observed 32 size-two orbits. Complement and reversal preserve the balanced-start count by reindexing or replacing the weight by 16 minus the weight.

## originality

PASS

The rotation-class population, total balance, enumeration method, and unconditioned symmetry orbit counts are prior. The surviving exact result is the H-conditioned histogram with its symmetry refinement and derived moments, not the de Bruijn census or the standard Abelian-square definition.

## value

PASS

A full-cycle square and its equal-length antipodal partition are canonical in a cyclic order-five word: the length is the whole period, not an arbitrarily chosen short-factor cutoff. The exact distribution, attainable range and symmetry-conditioned census answer how often a global balance guarantee appears as balance at individual antipodal cuts. They are useful as an exhaustive small-order reference, independently of the already known total class and orbit counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
