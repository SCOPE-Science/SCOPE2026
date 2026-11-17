# Independent mathematical audit

## correctness

PASS

The six distinct 3x3 permutation matrices span the stochastic affine space with one linear dependence: choosing c0=t solves c=(t,d01−d22+t,d02−d11+t,d00−t,d22−t,d11−t). Nonnegativity iff max(0,d22−d01,d11−d02)<=t<=min(d00,d11,d22); Birkhoff existence supplies nonempty interval. All six coordinates are strictly positive for L<t<U and at least one vanishes at each endpoint, so minimum support is min(endpoint supports) and at most two optima. If all D entries lie in (1/Q)Z, both t endpoints and six weights do too. Sharp five-term 1/13 matrix has five positive terms at both ends. Independent enumerator checked all 839 matrices for Q<=6 and exactly reconstructed every endpoint; finite checks are not an all-real proof.

## originality

PASS

Standard Birkhoff six vertices, affine parity relation and general extreme-point optimality are old. Czégel 2026 treats finite precision general-dimensional scheduling and Dufossé et al 2018 treat heuristic minimum decompositions and extreme points, but inspected relevant primary full text does not give this complete all-input 3x3 two-endpoint length and no-grid-penalty classification. It is a natural special case requiring a full exact derivation, with residual risk that older 3x3 Birkhoff polytope sources imply the result as a routine corollary.

## value

PASS

Dimension 3 is smallest with nonunique Birkhoff coefficients. A complete exact minimum-support classification for every 3x3 doubly stochastic matrix, sharp worst-case bound and guarantee that input precision causes no extra terms provide a natural reproducible benchmark. No claim for higher dimension, NP-hard general problem or floating point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
