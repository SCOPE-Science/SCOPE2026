# Independent mathematical audit

## correctness

PASS

The flip energy divided by two is the local spin times its field. Flipping all spins in row two conjugates negative K to q=|K| and preserves both markings. For q=0 a nonconstant row has a wall-adjacent spin with nonpositive flip cost, so only the four pairs of constant rows remain. For q>0 each spin of any unsatisfied rung must agree with both its horizontal neighbors. The unsatisfied rung therefore forces adjacent rungs of the same orientation, and propagation gives only the two opposite constant rows, strict iff q<2J. All other strict configurations have aligned rungs. Their common binary word is unconstrained when q>2J and has no singleton run when 0<q≤2J: a singleton flip is neutral at equality and is not counted. Counting nonconstant cyclic words with k even marked runs of length at least two gives 2n/k times the number of compositions, binomial(n−k−1,k−1); unrestricted even wall sets give 2 binomial(n,k). The wall-marked matrix has trace S_n(z) and characteristic polynomial (t²−t)²−z². Its primitive Perron root is (1+√(1+4z))/2 for z>0, with subleading roots −φ⁻¹ and exp(±iπ/3) at z=1. Exponential moments at z=e^t give limiting per-rung log mgfs by subtracting their t=0 values; the positive spectral gap and differentiability yield concentration at their slopes (5−√5)/10 and 1/2. There are no walls at q=0. The strict threshold and the exact polynomials were separately checked in 36 small-size/coupling cases by comparing total Hamiltonians after every flip. The opening 'two discontinuities' describes the size-growing landscape: the exact all-n theorem has no count increase out of q=0 for the n=3 exception (4 versus 4). The 0<q<2J, q=2J and above-threshold polynomials distinguish the isolated count drop of two at equality.

## originality

PASS

Credit is limited to the complete anisotropic strictly blocked ladder classification across the two coupling thresholds, including the exact unsatisfied-rung sectors and strict equality case. The aligned no-singleton branch, its combinatorial word space and its unmarked count are covered by inspected prior or indexed comparators; neither their rederivation nor the use of transfer matrices is the originality claim. None of the inspected comparators gives the full rung-coupling classification.

## value

PASS

The simplest periodic ladder with separately variable rung and leg bonds gives a natural comparison of strict trapping landscapes. A local field zero at q=0 or 2J changes the allowed domain structure, and only the exact all-state classification explains both the exponential complexity jumps and the isolated loss of the antiparallel sectors at equality. This is useful as a deterministic benchmark for blocked-state counting and distinguishes entropic proliferation from equilibrium phase behavior; the already-known intermediate word family is not in itself a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
