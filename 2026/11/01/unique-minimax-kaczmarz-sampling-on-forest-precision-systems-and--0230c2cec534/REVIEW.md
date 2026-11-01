# Scientific review

## Correctness

**PASS.** The exact one-step Kaczmarz objective follows from orthogonal row projection. An invertible congruence identifies its semidefinite constraint with a diagonal majorant of inverse row Gram. The forest's acyclic signed graph supplies a sign vector simultaneously saturating every off-diagonal term, proving an upper bound for every probability vector. An explicit signed-edge sum-of-squares factorization reaches that bound; PSD zero-form rigidity proves global uniqueness. Tree Gaussian factorization supplies the stated precision entries, and summing weighted degrees gives the topology-invariant rate. Exact rational checks of 51,565 assertions verify implementation-level identities without being used as the infinite proof. There are no omitted boundary cases for zero correlations, disconnected precision support or vanishing coupling.

## Originality

**PASS, with residual literature risk.** The general randomized Kaczmarz E-optimal probability semidefinite formulations are known in Dai--Soltanalian--Pelckmans (2014) and Gower--Richtárik (2015); their inspected optimization sections do not present the closed-form forest-precision global optimizer or the shape-independent Gaussian-tree rate. Strohmer--Vershynin (2007) gives norm-weighted sampling, a distinct criterion. The published Agaskar--Wang--Lu (2014) study addresses long-horizon MSE exponents and probability tuning, but full text was inaccessible; only its abstract was checked. Previously known star-tree and three-dimensional instances are special cases: the contribution is not those instances, but the complete arbitrary forest and heterogeneous tree theorem with independent proof and rate invariance. Searches of related research records and bibliographic variants found no equivalent statement, but that absence is not proof of global novelty. Relevant historical graphical-model, diagonal-majorant and Kaczmarz literature may still overlap.

## Mathematical value

**PASS.** The result solves a natural exact minimax probability-selection problem on a large nonsymmetric family without an SDP, yields an efficient local edge formula, proves uniqueness over unconstrained node probabilities, handles arbitrary signs and heterogeneity, and establishes a counterintuitive topology-invariant sharp rate for all equal-magnitude Gaussian Markov trees. The structural tree/forest restriction is mathematically motivated by conditional independence and exact sign balancing; this is neither a single arbitrary numerical example nor a restatement of the general SDP.

## Limitations

This is the one-step worst-direction guarantee, not exact multi-step MSE optimization. The signed-edge certificate need not extend to precision graphs with frustrated cycles. The specialized historical literature has not been exhaustively searched, especially the complete text of Agaskar--Wang--Lu 2014. Exact finite rational assertions are not an infinite proof. Independent review is outstanding.

Self-review: passed. Independent audit: not yet performed.
