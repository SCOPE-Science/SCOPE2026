# Independent mathematical audit

## correctness

PASS

The Petersen graph is KG(5,2), with 10 vertices/15 edges, and the weight-three reduced Świątkowski model has chain ranks (680,2400,2700,960), which I independently verified by its basis formula. I read the entire supplied verification code: it constructs oriented integer boundaries, checks both ∂² identities, and calculates ranks (679,1715,960) modulo 3,5,7 and (679,1714,960) modulo 2. Modular ranks are only lower bounds for rational rank. The proof supplies upper bounds for ∂1 by augmentation, ∂3 by its 960-column dimension, and ∂2 from the equivariant total-motion map onto H1(P;Q) of dimension 6: two parked particles permit representatives of twelve Petersen five-cycles, whose graph cycles span rank 6. Hence the rational ranks are exact. Signed chain Lefschetz traces for all seven S5 classes, cross-checked against the independent orbit-product formula, give H2 character (25,-3,1,-2,0,1,0). Murnaghan–Nakayama inner products produce the claimed Specht multiplicities; averaging rational chains under the finite group proves the quotient-homology assertion. This is not an inference of integral torsion from finite fields. The code was inspected but complete large matrix ranks were not independently re-executed.

## originality

PASS

The related published Petersen two-particle S5 module refers to B2(P), not B3(P); separate graph cut complexes are different functors. Ko–Park characterize graph braid H1, not this three-particle H2 symmetry character. Maciążek–Sawicki 2019 gives nonequivariant Petersen-family homology and higher graph configurations but not the seven-class S5 character for B3(P) in the inspected article sections/table. Betti numbers alone are not claimed as new. Exact three-particle rational degree-two S5 decomposition and absence of invariants remain a motivated, best-of-knowledge symmetry refinement.

## value

PASS

The full automorphism action on three-particle Petersen configuration homology is a natural equivariant invariant with a clear application to B3(P)/S5; the 25-dimensional H2 symmetry decomposes into four Specht types and has zero invariants. The distinct particle number makes this nontrivial beyond known two-particle and graph-H1 calculations; it provides a concrete test case for equivariant graph-configuration theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
