# Independent mathematical audit

## correctness

PASS

Pauli conjugation gives the stated three nontrivial transfer eigenvalues with modulus strictly less than one, normalized right fixed point I/2, and left fixed point I. For each block length at least one, one nonzero Pauli index padded with zero indices gives representatives of the four matrix units' span, proving full column rank of the boundary-to-physical map. Expanding the canonical trace in auxiliary indices gives the output-first Choi operator of E^L on the middle two legs, tensoring I and I/2 on the outer legs, precisely in the two block groupings of the record. Local congruences and their left inverses preserve separability of the positive cone and PPT in both directions (partial transpose conjugates the map on the C side); the outer factors can be added or traced out locally. For a direct check of the threshold, with t_i=λ_i^L the normalized Choi operator is (I+sum_i t_i σ_i⊗σ_i^T)/4. On Bell eigenvectors the three Pauli terms have sign product +1, whereas after partial transpose they have sign product −1. The minimum across both spectra is (1−sum_i |t_i|)/4, so Choi positivity makes the criterion exactly equivalent to PPT. When the sum is at most one, the Choi operator is a mixture of I/4 and the separable equal/unequal Pauli-eigenbasis correlation states (I+sign(t_i) σ_i⊗σ_i^T)/4. This includes equality. Monotone decaying absolute powers make the threshold finite; 3s^L≤1 gives the ceiling and logarithmic asymptotic. Canonical contractions for each fixed finite region converge to all-zero physical support as the nonidentity tensors vanish, at a noninjective endpoint not covered by the strict-positivity theorem. The frozen numerical checks were inspected, not executed; they do not justify the equality case or the all-block quantifier.

## originality

PASS

The exact transfer-channel criterion and index are already covered by Ruskai and Lami–Giovannetti, including the isotropic numerical ceiling as a direct substitution. The distinct supported claim is the necessity as well as sufficiency of that channel threshold for each actual pair of nonempty Pauli-MPS blocks. The closest MPS source gives a general forward transfer contraction and sufficient separability length, but does not supply the inverse physical-to-virtual recovery of the Choi entanglement or its PPT status. Known tensor injectivity is an ingredient, not a claim of invention. No matching physical theorem was established in the inspected sources.

## value

PASS

Exact necessity on arbitrary nonempty blocks distinguishes a physical entanglement range from a sufficient decay bound. The all-block equivalence supplies explicit NPT below the threshold even where merely seeing a non-EB transfer map would not prove physical entanglement, and the product-state limit shows the exact physical length is not locally bounded near this noninjective boundary. These are statements about actual chain marginals, not just a recatalogue of the channel index or a uniform-gap claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
