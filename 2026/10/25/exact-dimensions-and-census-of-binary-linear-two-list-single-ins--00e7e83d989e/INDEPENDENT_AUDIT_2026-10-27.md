# Independent mathematical audit

## correctness

PASS

For each n=1..9 and binary linear k-plane C, received y in F2^(n+1) has distinct parents D(y) exactly the set of length-n words produced by one-coordinate deletions. The list-at-most-2 criterion is all_y |D(y) intersect C|<=2. Each k-subspace has unique RREF with pivot columns and freely chosen entries strictly to the right in nonpivot columns; exhaustive independent RREF generation (checked count against Gaussian binomial [n choose k]_2) enumerated every candidate, not just sampled codes. It confirmed optimum K(1..9)=(1,1,2,2,3,4,4,5,6), optimal labeled-subspace counts (1,3,4,29,49,17,3238,5534,1786), and zero valid (K(n)+1)-subspaces for each n where upper exists. In particular exactly 1786 of all 788035 [9,6] planes valid and none of the 43435 [9,7] planes valid. Containment of subspaces implies absence of larger valid dimensions. RREF canonicality and exhaustive code+received-bitmask check prove finite theorem; independent enumeration finished, not a timed-out partial census. The stated length-nine [9,6] generator and 432/480/112 parent histogram in RESULT.md are consistent with the proof and provide a witness.

## originality

PASS

Finite exact census for a natural linear code/list-two/single-insertion setting, not equivalent to asymptotic list-decoding capacity or pairwise insdel-distance bounds. The relevant recent Kiah-Wei-Zeng paper is an important possible priority comparison but inaccessible in full through authorized routes; strongest inspected accessible claims concern general rate bounds. Best-of-knowledge PASS explicitly qualified, not categorical full-paper noncoverage.

## value

PASS

Small-block linear insertion list-decoding is a canonical constrained coding question where exact attainable dimensions and numbers of optimal labeled codes are useful benchmarks. The length-nine transition to six information bits, complete rank-seven impossibility and counts of all optimal rank-six planes are meaningful finite cutoffs, not an arbitrarily chosen single small code example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
