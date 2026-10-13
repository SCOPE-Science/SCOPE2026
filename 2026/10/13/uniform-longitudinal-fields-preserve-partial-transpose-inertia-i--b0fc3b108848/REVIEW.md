# Review

## Correctness

PASS. Since the uniform-field generator \(M=Q_A\otimes I+I\otimes Q_B\) commutes with \(H_0\), the Gibbs exponential factors exactly and can be split symmetrically into the positive local filters \(K_A\otimes K_B\) on the two sides of the zero-field Gibbs operator. Partial transpose converts this into an invertible Hermitian congruence by \(K_A\otimes K_B^{\mathsf T}\). Sylvester's law of inertia therefore preserves all positive, negative, and zero partial-transpose eigenvalue counts. The spin-one XXZ plus single-ion Hamiltonian satisfies the commutator hypothesis because its exchange term is \(\frac12(S_1^+S_2^-+S_1^-S_2^+)\). The exact packaged checker verifies the spin-one charge-conservation transitions and the partial-transpose/filter identity.

## Originality

PASS, with explicit partial prior coverage. The 2021 spin-one negativity paper already reports magnetic-field-independent threshold temperature for selected anisotropy values and attributes a kink to a partial-transpose eigenvalue crossing zero. An own prior finding proves field-independent threshold behavior for a different pure-biquadratic spin-one dimer. Standard local-filter theory also predates both. Those statements are not claimed as new. The surviving claim is the general observation that every positive-temperature Gibbs state in a finite uniform field coupled to a conserved additive charge lies on one invertible local-filter orbit of the zero-field state; this yields field independence of the complete partial-transpose inertia and of every zero-crossing temperature for all allowed couplings, not only the plotted or special-case thresholds. Focused published-finding corpus and literature searches did not locate that full statement.

## Value

PASS. The theorem replaces parameter-by-parameter diagonalization of a field-dependent partial transpose by a structural invariant. In the spin-one dimer it upgrades a selected-parameter numerical observation to the full anisotropic parameter space and also fixes all sign-change/kink temperatures. It explains how a field can strongly change the size of negativity and even select a product ground state while being unable, at any finite positive temperature, to change the PPT/NPT sign pattern. This is a reusable diagnostic for thermal dimer calculations rather than a new value of a known table.

## Closest literature and limitations

The closest application source is DOI:10.3390/molecules26113420, which computes the spin-one negativity, states field-independent threshold behavior for selected values, and discusses a kink from an eigenvalue sign change. The archive-era model source is arXiv:cond-mat/0505636. Invertible local filtering is standard theory, for example arXiv:quant-ph/0105090. The closest own prior item is `03f67142-630f-4201-afe7-411cd0af32f8`, a pure-biquadratic special case with an explicit threshold formula. The present result excludes transverse/nonuniform fields and does not equate PPT with separability in \(3\times3\).

Self-review: passed. Independent audit: not yet performed.
