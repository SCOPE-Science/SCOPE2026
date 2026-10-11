# Review of the cyclic-monomial resonance threshold theorem

## Correctness — PASS
The proof first uses the Jordan decomposition and the generalized eigenspaces of a polynomial in an inner derivation to locate all nonzero entries of the invertible matrix. A nonzero determinant summand provides a cycle cover; coprimality forces every cycle length to be a multiple of the sharp ambient dimension. This proves that the cover is one cycle and that its vertex spectrum is simple. Residues modulo that dimension force every other permissible matrix entry to vanish. The normalized spectral shape is then recoverable from its unique outgoing transition; primitive word counting and the determinant/power identities are exact. No numerical truncation is used as an infinite proof.

## Originality — PASS, with stated residual risk
The nearest dated literature is H. Stanković, *Spectral Rigidity of Commutators: Dynamics, Resonance, and Nilpotency*, arXiv:2608.29574v1 (2026-08-30). Its accessible abstract establishes the sharp nilpotency-versus-invertibility dimension dichotomy and gives a cyclic construction. Those claims alone do not classify **all** invertible threshold solutions or prove the exhaustive necklace classification and exact power identities. Targeted semantic searches of published mathematical findings for quadratic inner derivations, cyclic resonances, minimal dimensions, necklace spectral types, and stronger covering results did not identify a decisive implication. Full manuscript and appendices could not be accessed; they may nonetheless contain equivalent classification, so originality is provisional and should be independently compared against full text.

## Value — PASS
A construction demonstrating sharpness of an operator-theoretic dimension threshold leaves open whether more complicated invertible extremizers exist. The theorem resolves that natural equality-case question: all extremizers are cyclic monomial, their semisimple spectra are forced, their distinct spectral forms have an exact necklace count, and the operators obey concrete scalar-power rigidity. This is a structural classification of every extremizer rather than a routine parameter substitution or a finite-table enumeration.

## Evidence and limitations
The proof is self-contained except for standard Jordan decomposition and determinant expansion. The enclosed standard-library checker exhaustively verifies 19 small coprime parameter pairs, but does not replace the general proof. The source manuscript could not be read in full, so the comparison is based on publicly accessible metadata and abstract, not a negative claim about its whole contents. Larger matrices, singular solutions, and detailed classification of continuous weight parameters remain outside scope.

Same-model review: passed. Independent audit: not yet performed.
