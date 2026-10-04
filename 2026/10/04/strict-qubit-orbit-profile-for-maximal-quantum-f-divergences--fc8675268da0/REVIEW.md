# Review

## Correctness
PASS. For qubits, \(A=\sigma_U^{-1/2}\rho\sigma_U^{-1/2}\) has orbit-independent determinant \(\delta\) and trace \(t\) affine in the eigenbasis transition probability. Cayley--Hamilton gives an exact resolvent identity, which reduces every kernel in the operator-convex representation to the displayed scalar function. Its derivative is strictly positive for every non-affine operator-convex generator. The finite checker corroborates exact identities on representative rational data but is not used as an infinite proof.

## Originality
PASS. The closest source, arXiv:2601.08268, proves the minimum, maximum, and closed-interval image of the orbit. Those statements do not imply injectivity or monotonicity through the interior. Claim- and alias-specific searches found no prior statement of the strict qubit overlap profile, its level-set rigidity, or the explicit quadratic stability coefficient. Earlier unitary-orbit work treats particular divergences, and the mixed-unitary follow-up optimizes over a different feasible set.

## Value
PASS. The result converts an endpoint theorem into a complete qubit optimization landscape. It gives an exact observable coordinate for every orbit level and a quantitative local curvature coefficient at the optimum, which are directly useful for robustness and inverse-level questions.

## Closest literature and limitations
The nearest literature is Nguyen--Nguyen--Le, arXiv:2601.08268, together with earlier fidelity/relative-entropy unitary-orbit results of Zhang--Fei and a later mixed-unitary extension. The theorem is restricted to faithful, nondegenerate qubits and non-affine operator-convex generators of the maximal commutant-Radon--Nikodym divergence. An equivalent older formulation under specialized terminology remains a residual literature risk.

Same-model review: passed. Independent audit: not yet performed.
