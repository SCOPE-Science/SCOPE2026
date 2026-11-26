# Independent mathematical audit

## correctness

PASS

In the specified Pauli convention, the three rows and first two columns of the Peres–Mermin square multiply to +II, while XX·YY·ZZ=-II. In every context the first two distinct nonidentity Paulis commute and have product epsilon times the third. Each assigned sign occurs twice over the six triples, so at least one triple must have sign product -epsilon. Its positive joint (-r_P,-r_Q) projector has trace one (P,Q and PQ are traceless); its expansion on II,P,Q,R gives signed expectations -r_P,-r_Q,-r_R and zero for all other Paulis. The Pauli expansion of a flat state then gives the projector expectation (1-3 gamma)/4 >= 0. The argument covers every sign assignment and gamma=0 separately has the maximally mixed state. At gamma=1/3 the all-positive signed sum is A⊗I+I⊗A+A⊗A with A eigenvalues ±sqrt(3), so the density has eigenvalues (3±sqrt(3))/6 and two zeros in the local product eigenbasis. The spectrum gives the rank, purity 2/3 and separability; mixing with I/4 preserves separability and scales every Pauli expectation to gamma. The stabilizer witness follows because each pure two-qubit stabilizer state has exactly three unit-modulus nonidentity expectations, so the all-positive witness is at most 3 and equals 15 gamma on the constructed family. The Finding states nonmembership above 1/5; to check the phrase 'exact interval' in the literature comparison, five positive commuting triples partition all 15 strings: (XI,IY,XY),(YI,IX,YX),(ZI,IZ,ZZ),(XX,YZ,ZY),(XZ,YY,ZX). The equal mixture of their joint +1 projectors gives the all-positive gamma=1/5 state and mixing down with I/4 establishes membership for gamma<=1/5. The independent symbolic Pauli replay `python3 /workspace/branches/frozen_math_checks.py` verifies the six context signs, all 512 effective assignments of the nine square signs (the remaining six signs are unused), and the five positive triples. The symbolic and analytic arguments, not a search over density operators, establish the result.

## originality

PASS

Pass for the distinct all-sign ceiling and sharp separable all-positive construction. Cieśliński v1 already gave exact feasibility at contrast 1/3, the corresponding endpoint purity and the general sign-aligned witness giving gamma>1/5 for two qubits. The witness and threshold must be credited as prior; their application to this separable family follows from the new construction and is not an independent novelty claim. The inspected prior example is entangled, and the best-found table and optimization formulation do not furnish the rigorous universal ceiling or the separable endpoint.

## value

PASS

The exact allowed interval resolves the two-qubit mixed-state full-spectrum problem beyond the prior best-found value. The contextuality bound and explicitly separable maximizer show that entanglement is unnecessary even for maximally flat states outside the stabilizer polytope. The value here is the sharp obstruction plus separable attainment, not the known cutoff alone or any unproved operational quantum advantage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
