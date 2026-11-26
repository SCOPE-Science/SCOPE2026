# Independent mathematical audit

## correctness

PASS

With unit norm, the 16 Hermitian Pauli expectations have squared magnitudes w with w(0)=1, w<=1 and sum 4. Expanding the rank-one density matrix in this basis proves H w=4 w via tr(rho P_u rho P_u)=tr(rho P_u)^2. I independently restricted H-4I to every support containing zero, using exact integer elimination and rational back-substitution. The numbers of strictly positive supports at sizes 4, 5, 6 are 15, 0, 45; at size six each successful kernel is exactly the span of two intersecting isotropic-plane indicators. Normalization gives w(u)=1 at their shared nonzero point and hence a Pauli eigenstate. A Clifford sends the eigenoperator and eigenvalue to the Z⊗I,+1 sector; the remaining pure qubit has exactly two nonzero Bloch coordinates. Signed permutations of these coordinates give the stated real normal form, excluding axis endpoints. For the converse all intersecting pairs are equivalent: quotient the perpendicular of their common line by that line and map the two distinct directions in the resulting symplectic plane to a fixed pair, extending to a symplectic basis. Clifford realization and the product expectations give every support. The 15 planes each meet six others in a line and each union is counted once as an unordered pair. Independent replay: python /workspace/branches/independent-discrete.py (STFT block). The Walsh condition alone was used for necessity, not as a general purity test.

## originality

PASS

The prior minimum-support results are correctly excluded. A later indexed theorem contains the support-five exclusion but expressly leaves size six unclassified. No earlier implication-equivalent source for this small gap plus the complete first nonminimal support geometry and Clifford normal form was established in the inspected literature and records.

## value

PASS

The smallest noncyclic phase space is a natural first test of what lies immediately above the known uncertainty minimum. Finding the first gap is useful, but the substantive gain is determining every next-minimal support and proving the presence of one exact Pauli eigenconstraint on every such signal. The result supplies an exact small reference class for Fourier sparsity and two-qubit Pauli geometry, not a claim about larger groups or noisy support.

The dated certificate retains the supplied scientific assessment, sources and limitations.
