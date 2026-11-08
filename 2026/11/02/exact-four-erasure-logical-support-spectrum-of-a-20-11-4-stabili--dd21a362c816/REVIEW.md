# Independent mathematical audit

## correctness

PASS

The nine explicit 20-symbol Pauli generators have independent rank 9 and commute; all 512 stabilizers have nonzero weight at least 12. For |E|=4 the local logical quotient has dimension 8-rank(H_E). Fresh Python independently formed the 40-bit symplectic rows, enumerated all 4845 four-subsets and computed the exact dimension counts 3840, 970, 35; all 35 rank-six local subspaces are isotropic. Four-erasure failure count is 1005; <=3 are correctable by distance 4, >=5 are uncorrectable since 2|E|>=10 exceeds nine commutation constraints and no stabilizer fits in a five-set. Thus P_succ(p)=sum_{j=0}^{3} binom(20,j)p^j(1-p)^(20-j)+3840 p^4(1-p)^16, 0<=p<=1.

## originality

PASS

The source paper gives the specific stabilizer and 1075 individual weight-4 logicals but not the distribution of distinct four-coordinate support multiplicities; the 970/35 refinement and erasure-reliability polynomial are additional exact data.

## value

PASS

The precise erasure-support geometry of a newly tabulated 20-qubit distance-four code is a natural decoding invariant. Its distinction between one- and two-logical failure sets controls exact recovery probability under independent known erasures and is not a routine restatement of a weight enumerator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
