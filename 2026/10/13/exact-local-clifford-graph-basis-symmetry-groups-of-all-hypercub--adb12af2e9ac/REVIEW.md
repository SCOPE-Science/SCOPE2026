# Scientific review — exact local-Clifford hypercube graph-basis symmetries

## Correctness — PASS

The statement classifies tensor products of one-qubit Cliffords that permute the **rays** of the graph basis of a fixed hypercube \(Q_d\), modulo local Paulis and global phase. In Pauli binary symplectic coordinates, the condition for an operation to stabilize the unsigned graph-state Pauli subspace is necessary and sufficient, because all graph-basis rays are the joint eigenvectors of that Pauli subspace. For a hypercube, the adjacency-square codegree relation forces the local symplectic coefficients to be constant on each parity class. Its diagonal equation gives \(c\); its adjacent-vertex equation determines \(a,e\); its distance-two equation determines \(b\). Imposing the determinant-one condition yields exactly four matrices for even \(d\), six for odd \(d\). The local group law and affine label action are established explicitly. The proof includes \(d=1\) and does not rely on a finite enumeration to establish the all-dimensional claim.

An exact binary linear-system verifier independently solves the complete \(4\cdot2^d\)-variable system for \(1\le d\le5\); a separate complex statevector computation checks all graph-basis vectors for \(d=1,2,3\), totaling 1,624 basis-permutation tests. Both programs run with only Python 3's standard library. The limits of the finite experiments are stated.

## Originality — PASS, with identified residual risk

The closest paper is Wang–Avis–Goodenough–Krastanov (arXiv:2606.23809v1), especially its Section III.C treatment of the exceptional cube \(Q_3\) and its statement that exceptional graph-preserving symmetries remain to be systematically classified. The paper characterizes a restricted **two-copy** graph-preserving gate family, not the full tensor-product Clifford stabilizer of the fixed one-copy hypercube graph basis. Claudet (arXiv:2511.22271, Section 2.5) and earlier graph-state local-symplectic literature provide the general binary constraints; their general solvability conditions and generic algorithms do not evaluate the exact all-hypercube group, its parity jump, or the faithful action on basis labels. Galgano–Holweck give a general local-Clifford orbit formalism. Nation et al. give an algorithm for symmetries of Pauli Hamiltonians, not this fixed graph-basis automorphism group.

The conclusion is not that the general symplectic equation is new; rather, the evaluated closed classification for an infinite natural graph family and its label action is not stated in these inspected sources. A previously unindexed specialized group calculation, or a code-theoretic derivation implicitly equivalent to the present result, remains a genuine originality risk. Searches and similarity retrieval do not prove priority.

## Value — PASS

The parity-dependent six-versus-four cosets give an exact natural structural invariant for a family of highly symmetric entangled graph states, extending the motivating paper's isolated exceptional-cube example to **all** hypercube dimensions. The result exhausts *every* local Clifford pattern rather than presenting an isolated admissible gate. Its explicit \(\mathbb F_2\) representation gives the complete group action on graph-basis labels and a closed, size-independent enumeration rule for the full local graph-basis symmetry search. The result does not claim a noise-tolerance improvement or optimal distillation protocol. The finite computation is verification of an all-dimensional theorem, not the source of its value.

## Limitations and priority comparison

All results are for simple, fixed, labelled hypercube graphs and tensor products of one-qubit Clifford gates. Qubit permutations, graph changes, entangling gates, and general local unitaries are excluded. A broader general algorithm can evaluate arbitrary graphs and would in principle evaluate hypercubes; that capability does not itself give the explicit parameterization or parity-dependent closed formula established here. The stated priority assessment remains provisional pending independent literature review.

Self-review: passed. Independent audit: not yet performed.
