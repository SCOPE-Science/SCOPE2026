# Independent mathematical audit

## correctness

PASS

Intra-side gates are local to the cut. After dropping them, the reduced state has matrix entries 2^(-n) on pairs of bit strings whose difference is in ker(B'^T), and zero otherwise, so the spectrum has 2^rank(B') equal nonzero eigenvalues. The pristine operator is P^(-2)(I+P)^3 and (I+P)^4=I+P^4; under 4|n its left and right kernels are the three-dimensional even-parity four-periodic space. Projecting the deletion equation to the cokernel, distinct deleted-row residues force both column evaluations to vanish; these have rank 1 or 2 according to whether their residues agree. Transposing handles equal row residues with different column residues. In the remaining case d=4k and t=u, x=sum_{j=0}^{k-1}(e_{4j+1}+e_{4j+2}) satisfies Bx=e_0+e_d by telescoping. The common coefficient of the two updates must obey (x_t+x_{d+t}) times that coefficient = 0; x_t+x_{d+t} is 1 exactly for t=-2,1. The other scalar constraint has rank one because evaluation at d+t is nonzero on the pristine kernel. Thus the nullity is 2 or 3 as stated. Same actual column, wraparound, and n=4 are included; same even endpoint is not. An independent GF(2) elimination replay (branches/84af81fa-226f-4828-8fe3-16b101bfd97b/independent_rank_check.py, output independent_rank_check_output.txt) matched all 8,448 configurations at multiples of 4 through 64, with gain counts 240/3312/4896 for 0/1/2. That bounded replay supports, but does not replace, the argument.

## originality

PASS

The supported distinct claim is the placement trichotomy for two omitted cross-cut edges with different even endpoints in the specified cyclic-power family. Neither graph-state cut rank, undamaged consecutive-ones circulant rank, nor cancellation in another graph family is credited as new.

## value

PASS

Checkerboard cut rank is a natural exact entanglement observable for a local ring, and two absent gates are the first case in which the effects of separate omissions can cancel. The law distinguishes zero, one and two bits of gain from geometric placement, including offsets of distance one versus three when the rows and columns have the same residue pattern. It can predict whether a specified defect pair preserves or changes the Schmidt spectrum without simulating the state; it does not claim a statement about coherent noise or arbitrary cuts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
