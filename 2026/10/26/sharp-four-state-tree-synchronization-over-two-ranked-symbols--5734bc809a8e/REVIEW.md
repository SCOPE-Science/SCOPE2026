# Independent mathematical audit

## correctness

PASS

Exact subset-image dynamic closure recomputed independently from the displayed complete unary map and 4x4 binary table: first masks 15,13,7,11,14,12,5,3,10,9,6,4 (heights 0..11) with no singleton before height 11; recurrence enumerates ALL 15 nonempty masks. The universal 11 bound follows strict new-nonsingleton growth; a one-symbol operator image I has |I|<=3 if it can ever synchronize, and only 4 nonsingleton subsets of I, yielding threshold at most 5. The witness term has 12 independent leaves and height 11. Original verify.py was read and the same calculation independently implemented.

## originality

PASS

A sharp four-state unary-plus-binary witness is narrower than, and not implied by, the general 2^n-n-1 upper bound; recent two-symbol constructions target n>=5. Searches did not reveal the same n=4 extremizer, but unavailable full text and unindexed small-state examples are genuine priority risks.

## value

PASS

Attaining a universal strong tree-reset bound with the smallest nontrivial ranked alphabet resolves a natural alphabet-economy extremal problem at four states; the exact minimum alphabet size and reset height are meaningful finite invariants beyond a one-off witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
