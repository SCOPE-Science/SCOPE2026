# Independent mathematical audit

## correctness

PASS

At a degree-three vertex with its own spin included in the four-bit minority rule and ties retained, a flip occurs iff >=2 of three neighbors share the old spin. Each flip decreases monochromatic edge count m by 2s-3>=1. At most 3n flips are possible; each state-changing event occurs after geometric waiting time of conditional mean <=2n, giving E[T]<=6n². Stability iff each vertex has <=1 same-color neighbor. If any rung is monochromatic, both its horizontal neighbors must differ in both layers and so are monochromatic opposites; induction gives exactly two coherent-rung alternating configurations for even n, each energy n. Otherwise all rungs bichromatic. Equality of upper adjacent spins on cycle edges must form an independent set Z; cycle consistency requires |Z|≡n mod2. Each k-independent set yields two bit lifts, energy2k, and count n/(n-k) binom(n-k,k). Lucas cycle independent-set generating polynomial gives totals and parity correction; minimum k gives stated ground states. Fresh independent brute force inspected every 2^(2n) labelled configuration for n=3..8 and reproduced energy histogram and total. The source script covers n<=9 but finite checks are not substituted for proof for all n.

## originality

PASS

Rouquier–Regnault–Thierry 2010 develops the same asynchronous minority class and the general energy-descent/absorption principle; it is explicitly NOT original here. Regnault–Schabanel–Thierry 2007 considers square tori with different neighborhoods, and Wacław–Burda 2008 random-coupling Ising spin glasses, not uniform closed-neighborhood prisms. The narrow new-looking claim is the exact all-n energy-resolved absorbing-state polynomial, parity correction and ground-state multiplicities for circular prisms. The proof supplies a rung dichotomy and independent-cycle-set census not located as a displayed table in inspected previous work.

## value

PASS

Circular prisms are canonical regular degree-three graphs, and metastable absorbing configurations of an asynchronous spin rule are natural finite statistical-mechanics invariants. The exact energy polynomial gives the complete labelled metastable population at every n, beyond general convergence facts, with nontrivial parity- and mod-six effects. The hitting-time bound is useful but routine from prior energy descent and is not the sole claimed contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
