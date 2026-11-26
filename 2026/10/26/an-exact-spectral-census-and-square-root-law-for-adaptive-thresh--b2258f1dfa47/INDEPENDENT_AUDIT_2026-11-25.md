# Independent mathematical audit

## correctness

PASS

A parallel fixed extended state has every bit unchanged; for sequential permutations each vertex is updated only once, so return of the extended state likewise requires no bit switch and hence no threshold change. The local test with i and j active sites gives j+1 and b+1−j allowed thresholds on the A side, and i+1 and a+1−i on the B side. These sum to b+2 and a+2, which fixes the normalization. After dividing out (b+2)^a(a+2)^b the double sum is exactly the diagonal sum of the composed conditional binomials. On the polynomial functions of j of degree ≤b the operator preserves the degree filtration, and binomial factorial moments give its kth graded eigenvalue (a)_k(b)_k/[(a+2)(b+2)]^k, zero if a<k≤b. Thus the claimed zeros have algebraic multiplicity max(0,b−a) on the stated (b+1)-point space. For h=ab/(a+b), use a,b≥h and expand each log[1−(r+2)/(a+2)] and its b analogue at k=⌊t√h⌋ to obtain −t²/2+o(1) with no aspect-ratio assumption. The uniform bound exp(−k²/(4h)) follows from log(1−u)≤−u; the associated step functions are integrably dominated, giving √(πh/2) for the spectral sum. At a=b=n divide by [2(n+1)]^(2n) and use ((n+2)/(n+1))^(2n)→e² to get the stated fraction. The audit's own exact characteristic-polynomial checks on eight graphs and full extended-state updates on six graphs, including sequential orders in both directions and all three schemes, ran via python3 /workspace/branches/independent_reproduction.py bipartite. They gave counts 10, 42, 162, 324, 2128, 2128 in the enumerated cases and confirm asymmetric zero multiplicities in the finite matrix test. The uploaded script was read, not run; the proof establishes the full quantifiers.

## originality

PASS

Pass the specific spectral census of labelled adaptive-threshold fixed extended states on general K_{a,b}. Common fixed-point conditions and path, cycle and star cases are covered; neither the binomial diagonalization technique nor the joint Gaussian asymptotic mechanism warrants a standalone originality claim. In particular, the closely matching unshifted chip-firing asymptotic transfers to the shifted sum by an O(1) comparison once the new enumeration is known. The inspected chip-firing theorem does not enumerate the shifted adaptive fixed points themselves.

## value

PASS

The exact number of extended-state equilibria is a motivated invariant of the specified adaptive system. The two-variable spectral sum replaces exponential enumeration and identifies the finite spectrum of the enumeration kernel. It also quantifies how rare fixed states are even when both shores grow at very different rates, rather than only for stars, cycles, or balanced sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
