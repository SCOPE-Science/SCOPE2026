# Independent mathematical audit

## correctness

PASS

For the finite group square the group block K is a nonempty subsemigroup, hence a subgroup by positive powers, and contains the diagonal. Put N={g:(g,e)∈K}; diagonal conjugation makes it normal, and right multiplication by (h^−1,h^−1) proves (g,h)∈K iff gh^−1∈N. Separately each oriented cross-section is product-closed and, if nonempty, is a subgroup by finiteness. Multiplying by (e,e) proves each lies in N. Conversely both cross-sections may be chosen independently: same-orientation products use their subgroup closures, opposite-orientation products land in N×N, and mixed products with the group block retain equal G/N images in both coordinates. The new identity pair does not constrain them. The sections and N can be recovered by projection or restriction, proving uniqueness and coordinatewise inclusion. Reversing exchanges the sections, so symmetry requires equality. For a common nonempty subgroup the chain *~e~n for each n∈N forces the full N as the section; the resulting class N∪{*}, or the singleton {*} when both sections are empty, gives exactly the two congruences per N. Counting yields D,T,C. For nontrivial G at least the term N=G exceeds 4 in D and none is smaller; for trivial G, C/D=1/2. In the cyclic p-power case N=C_(p^j) has j+1 subgroups and the sum of (j+2)² grows as r³/3, giving 6/r². Both idempotents are central and all elements lie in subgroups, so these are finite Clifford monoids with the same two-element semilattice. The infimum is zero but is not attained in a finite example. Independent replay: python3 /workspace/review-evidence/check_frozen_math.py 1 directly enumerates all reflexive compatible relations for C1,C4,V4,S3,Q8 by generation from the diagonal and closure under product, without parametrizing them. Every closed relation is reachable by successive addition of its own elements; thus this independently exhausts S3 and Q8 as well. The observed (D,T,C) were (4,2,2),(29,9,6),(67,17,10),(62,12,6),(110,24,12), respectively. The frozen script's S3 check only verifies predicted forms; the independent finite computation does not substitute for the general proof.

## originality

PASS

Barber–Ruškuc already construct a one-sided subgroup cross-section on exactly the same fresh-identity example, on the full G×G block; neither the example nor the group-square theorem is new. The supported distinct result is the exhaustive two-section parametrization at every N, its exact count/order/cyclic density consequences, and its vanishing sequence within fresh-identity monoids. A separate indexed product family also exhibits fixed-semilattice vanishing, so that qualitative phenomenon by itself is not the basis for the pass. The bounded comparison does not establish priority.

## value

PASS

The theorem resolves the concrete elementary Clifford example used to show incompleteness of an existing bound. It determines the entire labeled relation order in terms of tractable group data, distinguishes symmetry and congruence, and quantifies a vanishing density in the fixed fresh-identity family. This structural payoff is not mere recomputation of isolated group counts, and the proof does not presume the finite argument extends to infinite groups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
