# Independent mathematical audit

## correctness

PASS

Ordinary insertion/deletion/substitution distance was recomputed independently by a length-5 Levenshtein dynamic program for all 32 words. The 211-edge compatibility graph has exactly 28 four-vertex cliques and no five-vertex cliques (all C(32,5) tested), so optimum is four. For every extremizer, subtracting a codeword yields a four-element XOR-closed subspace: all 28 are affine binary 2-flats. There are 14 directions and 2 eligible cosets per direction exchanged by complement; the six mutual edit distances split as 18 with five 3s and one 4, and 10 with four 3s and two 4s. A separate networkx GraphMatcher isomorphism enumeration of the EXACT 32-vertex graph finds precisely four automorphisms, which agree with reversal and global bit complement, inducing eight maximum-code orbits of sizes 2,2,4,4,4,4,4,4. This is a provably exhaustive finite proof, not extrapolation.

## originality

PASS

Houghten–Ashlock–Lenarz already tabulated E_2(5,3)=4 and proved global alphabet-permutation/reversal edit-space isometries. Neither the inspected report nor the maintained parameter table enumerates all 28 maxima, their affine structure, eligible cosets, finite compatibility-graph automorphisms, or its eight equality-case orbits; only these latter data are evaluated as new. An obscure archived equality-case census is a residual priority risk.

## value

PASS

A complete, symmetry-resolved equality census for a classical fixed-length edit-code optimum clarifies the geometry of all optimal four-word codes, independently reusable to compare code constructions and automorphism reduction. The known value 4 alone cannot provide its 28 labeled solutions, 14 directions, or eight orbits; this is a natural finite classification, not a selected arbitrary tuple.

The dated certificate retains the supplied scientific assessment, sources and limitations.
