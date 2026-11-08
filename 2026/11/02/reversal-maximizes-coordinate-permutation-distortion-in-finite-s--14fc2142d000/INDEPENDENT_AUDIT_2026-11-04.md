# Independent mathematical audit

## correctness

PASS

Let m=floor((N+1)/2). Any admissible Schreier output set has <=m points since a k-set has greatest element >=2k-1. Compress an arbitrary k-point preimage to first k ordered indices; Schreier admissibility is preserved because the jth chosen coordinate a_j>=j, giving total p-mass <=C_k<=C_m. Reversal maps the first m coordinates onto terminal admissible block, hence attains C_m^(1/p). It is self-inverse, so product optimum C_m^(2/p). The dyadic partition upper bound J+1 and nonincreasing dyadic weight lower bound J+(m-2^J+1)/2^J establish asymptotic (log2 N)^(1/p), including m=1 and real/complex scalar. Independent SciPy LP reproduced C_m for m=1..8 as 1,2,2,5/2,8/3,3,3,13/4; computation supports but does not establish all-N proof.

## originality

PASS

Best-of-knowledge PASS. Infinite-order Schreier isometries and combinatorial Banach-space automorphisms are established prior theory, but a non-isometric finite coordinate permutation extremum, its exact prefix LP reduction, and the reversal maximizer are not implied by isometry classifications. A broader symmetry-constant treatment could give the same theorem under alternate terminology.

## value

PASS

Finite Schreier geometry is a canonical non-symmetric normed sequence-space model. Quantifying its maximal coordinate rearrangement distortion, including sharp reversal extremal and logarithmic growth, is a natural quantitative complement to qualitative basis-isometry rigidity; no closed-form C_m is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
