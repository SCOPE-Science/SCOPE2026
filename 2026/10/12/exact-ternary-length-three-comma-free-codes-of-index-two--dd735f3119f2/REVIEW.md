# Independent mathematical audit

## correctness

PASS

For every ordered x,y from the 27 ternary length-three words, construct the two nontrivial splices and forbid each z at Hamming distance 0 or 1 from either splice. I independently rebuilt the 27x27 forbidden-bit-mask table directly from this quantified definition. Exhaustion of all 80,730 five-subsets finds none valid; by heredity no larger code is valid. Exhaustion of all 17,550 four-subsets gives exactly nine labeled maxima; independent construction of C_{j,b} (fix one position to b, prohibit b elsewhere) matches all nine. Simultaneous alphabet permutations (S3) and reversal (C2) give two orbits of sizes 3 and 6, stabilizers 4 and 2; source census.json explicitly lists all nine and its cardinality/first rows were inspected. This is a complete finite proof, not a sample or extrapolation.

## originality

PASS

The 1963 original provides the index-two lower-bound construction but neither the matching upper bound nor a census of equality cases at ternary length three; later general comma-free count work treats index one / circularity, not the stronger Hamming-separated splices.

## value

PASS

Completes the original index-two synchronization-with-errors construction at its smallest genuinely ternary case, including the entire rigid family of maximizers rather than a bare maximum. This natural finite classification supplies a meaningful exact base case and distinguishes symmetry types; it does not purport to solve general alphabets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
