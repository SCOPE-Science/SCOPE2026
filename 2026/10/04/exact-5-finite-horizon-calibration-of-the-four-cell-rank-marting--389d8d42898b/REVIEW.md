# Independent mathematical audit

## correctness

PASS

From the original four-cell martingale, each length-n null path has probability 4^(-n) and its value depends only on occupancy multiplicities. Independently rebuilt a symmetry-compressed integer DP: transitions from a sorted occupancy state increment a value-v cell with multiplier equal to its count multiplicity, retaining only paths with M_n<T. Reproduced the two exact horizon-128 crossing probabilities: 0.050092095656419… at T-=33554432/2297295 and 0.049902691907131… at T*=10384593717069655257060992658440192/710974957562660933407217865583125. Independently scanned all 550,967 four-part occupancy partitions through n=128 and found no attainable support between T- and T*. Threshold is minimal only within the stipulated attained-support convention, not among all real T.

## originality

PASS

Henzi–Law give the martingale and discuss simulation-based finite-horizon calibration of a different Sinkhorn variant; they do not give this exact fixed-grid four-cell N=128 support threshold. The independent 128-step exact path count and exhaustive support-gap certificate are not implied by a generic Ville bound.

## value

PASS

Finite-horizon Ville calibration is directly relevant to sequential testing. A certified 5% cutoff at a realistic horizon and exact null size replaces an otherwise conservative 20 cutoff; the exact support convention prevents ambiguity and the orbit-compressed recurrence is useful for related discrete null martingales.

The dated certificate retains the supplied scientific assessment, sources and limitations.
