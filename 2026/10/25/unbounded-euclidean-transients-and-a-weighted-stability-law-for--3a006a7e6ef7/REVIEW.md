# Self-review

## Correctness — PASS

The published PartRosExp2 tableau and the entire-matrix identity \(\varphi_1(Y)Y=e^Y-I\) yield \(LML^{-1}=e^YC\) without commutativity between the split matrices. Symmetric dissipation makes both factors Euclidean contractions; equality characterization yields the exact common-kernel spectral boundary. The fixed-exponential two-state family gives an exact matrix and an endpoint gain proportional to \(t/8\), even though \(A_t+B\prec0\). The published reverse-order tableau separately yields the uniform inequality \(\|N\|_2\le3+h\|B\|_2\). Standalone SymPy symbolic checks and 450 random-matrix trials corroborate, but do not establish, the universal claim.

## Originality — PASS, qualified by priority risk

Dallerit et al. (DOI `10.1007/s11075-023-01698-4`) introduce both methods, but §4 treats simultaneous diagonalizability and does not derive the noncommuting weighted similarity or unbounded endpoint counterexample. The preprint (DOI `10.21203/rs.3.rs-3101972/v1`) has a PartRosExp2 tableau expression different from the final published version; the theorem unambiguously uses the latter. Achleitner–Arnold–Mehrmann (DOI `10.13001/ela.2023.7531`) supply broader dissipative matrix context, not this method-specific contrast. Comparable time-integrator transients for other schemes do not imply this exact endpoint claim. Targeted mathematical searches did not uncover a dominating formulation. Specialized splitting/operator-product work could contain an equivalent result, so independent publication-priority verification remains necessary.

## Mathematical value — PASS

The exact stability distinction is germane to selecting second-order partitioned integrators for noncommuting dissipative stiff processes: scalar A-stability coexists with arbitrarily large physical norm amplification for one operator order, but not for the other when the exponential block is held fixed. This supplies both an all-dimensional structural explanation and a sharp two-dimensional obstruction. No nonlinear or finite-precision stability claim is made.

## Limitations and closest literature

Proofs apply only to finite real symmetric negative-semidefinite constant split matrices and exact stage operations. The reverse-order method is only shown uniformly bounded in the stiffness direction, not contractive. Key literature: Dallerit et al. 2023 preprint/published 2023–2024 and Achleitner et al. 2023. Part of the argument uses standard contraction and similarity facts. The new theorem remains a self-review without external expert validation.

Self-review: passed. Independent audit: not yet performed.
