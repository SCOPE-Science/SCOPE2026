# Independent mathematical audit

## correctness

PASS

Each of the 2^k length-k circular windows is the unique occurrence of a distinct factor, and a selected position hits exactly k such windows. When k divides 2^k and the capacity bound is attained, no window may contain two chosen positions. Thus consecutive cyclic gaps are at least k, and their sum makes every gap k: all equality cases are residue sets modulo k. Every longer occurrence contains a length-k window already hit by such a set. Independently I enumerated every binary tail following the unique rotationally anchored 0^k for k=1,2,4, and intersected sets of factors with the covered occurrences. The respective necklace counts are 1,1,16, and the valid-residue histograms are {1:1}, {2:1}, {2:4,3:8,4:4}. Each frozen order-eight word has 256 distinct length-eight windows. I checked all eight obstruction rows for V against both starts and residue-disjointness, found that residue seven misses only 1011011, and checked coverage by the advertised 32- and 33-position sets at every length 1–256, including wrapping occurrences. This yields the exact separation and the first power-of-two order, not a comparison over all orders less than eight or a statement about a worst cycle.

## originality

PASS

The supported distinct statement is exact 32-versus-33 optimality for two circular order-eight cycles, with uniform optima at the smaller power-of-two orders. The most relevant inspected comparison reporting 33 is an experimental linear attractor size, not an exact circular optimum. The inspected same-invariant catalog result is at order five only. Prime-order results for particular linear unfoldings do not determine the composite order-eight cyclic case. Mantaci et al. Proposition 41 was not accessible in full text, a specific unresolved literature risk rather than evidence for or against priority.

## value

PASS

The natural counting bound from unique length-k windows predicts a common optimum in the smaller cases. At the first relevant power-of-two order the two exact certificates show that the circular optimum depends on the choice of cycle and that shorter factors can alone force a strict increase despite complete length-k coverage. This answers a specific extremal question and provides concrete benchmarks for circular factor coverage without mistaking a greedy set for an optimum or claiming an asymptotic separation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
