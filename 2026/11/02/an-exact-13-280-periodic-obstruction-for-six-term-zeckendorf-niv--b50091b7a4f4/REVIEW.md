# Independent mathematical audit

## correctness

PASS

For G>=9 and the two fixed offsets only, start from the canonical expansions at G=8,9. For a negative offset w, adjoining F_(G+1) to the decomposition of F_G-w is nonadjacent and gives F_(G+2)-w, raising the weight by one. The positive offsets 1,3,5,7 concatenate canonically, with weights 1,1,1,2. Thus r=floor((G-3)/2) gives the three repaired profiles, including equal first two weights r in the even minus-five case. There r>=3 cannot divide both V-5 and V-3, where V=F_G. In both shapes the fixed weight-two terms require V odd; the minus-three shape requires V=2 mod 3. When G=2r+4 is even in the minus-three shape, r=1 mod 3 makes G a multiple of 3, and r=0 or 2 mod 3 requires V=0 or 1 mod 3, respectively. Hence every survivor for cutoffs >=3 is odd. When G=2r+3, the mod-3 constraints and Fibonacci residues at odd indices modulo 8 give exactly {5,11} mod 24 for minus-three and {1,5,7,11} mod 24 for minus-five. The Fibonacci pair recurrence gives periods 3,8,20,16 and the other tests have periods dividing 2p, giving a common period 1680. The independently authored repair verifier was executed with Python and exhausts indices 9..1688. The rows (minus-three, minus-five, intersection, union) are (140,280,140,280), (112,224,112,224), (80,144,72,152). Thus 19/210 is the exact union fraction at cutoff 7, with nonempty overlap. No structural premise about all possible roots and no existence claim are needed.

## originality

PASS

For the narrowed result, the distinct claim is the exact small-prime, common-period screen for the two candidate families, including overlaps and odds-only classes. It does not claim the two-shape reduction, the first observations on progression length, or priority over a full text that was not obtained.

## value

PASS

The two candidate shapes are singled out by the original six-term progression question and yield coupled, index-dependent divisors. The prime-three calculation eliminates every even index for both shapes and gives explicit odd classes, while the through-seven table quantifies and resolves the overlap of the surviving types across an unlimited range of indices. It gives a reusable preliminary screen for these two families, not a larger finite search or a claim to resolve the length gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
