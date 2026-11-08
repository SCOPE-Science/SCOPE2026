# Independent mathematical audit

## correctness

PASS

For C_r from 1->101,0->000, m=3^r, and V_r=C_r0^m, the cutwise shortest proper border equals 2m at cuts 0,m, equals 1 at zero-padding or equal-neighbor cuts, and otherwise equals 2*3^{v3(i)}. The structural recurrence C_{r+1}=C_r0^mC_r, palindrome and no-adjacent-ones properties, plus the 0101/1010 block pattern at nontrivial triadic transitions show a 2*3^j border that is itself unbordered (0^{3^j}C_j or reverse), proving minimality; counting transitions establishes multiplicities 2^{r-j}. Longer factors of C_{r+1} have border length length-2m from the 2m periodicity. Independent naive conjugate-prefix/suffix checks for r=0..4 confirm exact spectrum and boundary r=0; source checker.py independently covers r up to 6. Finite cases merely corroborate the unbounded block argument.

## originality

PASS

Holub–Müller Fully bordered words supplies the cyclic local-period notion and qualitative two-unbordered-conjugate framework but not the inspected pointwise 3-adic Cantor array. Goč–Mousavi–Shallit treat enumerations of unbordered factors for other automatic sequences, including period doubling; their theorem does not imply this explicit position-by-position array. Unindexed Cantor local-period computations remain a priority risk.

## value

PASS

The complete cyclic local-period spectrum is a natural word-combinatorial invariant tied precisely to triadic substitutions, with nontrivial multiplicity counts and an extremal unbordered-factor consequence. The pointwise law goes beyond the qualitative existence of exactly two unbordered rotations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
