# Review

## Correctness
PASS. In an induced one-point extension, every new block has the form \(\{x,u,v\}\). The old pair \(uv\) must lie in the leave, and two such pairs cannot share a vertex because that would repeat a pair \(\{x,u\}\). Conversely any matching in the leave gives a legal extension. This is an exact size-preserving bijection. The transformation \(\mu_G(t)=t^nE_A(-t^{-2})\), together with Heilmann-Lieb real-rootedness of the matching polynomial, forces every zero of \(E_A\) to be negative real. Newton's inequalities then give the stated ultra-log-concavity. The extremal bound follows from monotonicity of matching counts under edge addition and is strict for any nonempty block set.

The verifier exhaustively checks all \(5902\) labelled partial Steiner triple systems through seven points using matching recurrence, and independently directly enumerates candidate one-point blocks for all \(35\) systems through five points. It returns `VERIFY_OK`.

## Originality
PASS with material folklore risk. Matchings in leaves of partial Steiner triple systems are classical and are explicitly excluded from the novelty claim. Andersen-Hilton-Mendelsohn use the missing-edge graph in embedding theory, and a 1997 paper is specifically titled *Matchings in the Leave of Equitable Partial Steiner Triple Systems*. The web and published-finding corpus searches did not locate the rank-refined extension generating polynomial \(E_A(z)\), its identification as the entire matching generating polynomial, or the resulting negative-real-root and ultra-log-concavity statement for one-point extension strata. The exact claim therefore appears new as a polynomial-level synthesis, but because the bijection is short, undocumented folklore remains a realistic risk.

## Value
PASS. The result turns the one-new-point finite-diagram problem for relational partial Steiner systems into a standard graph polynomial. That imports the full matching-polynomial toolkit immediately: real-root geometry, Newton inequalities, unimodality, recurrences, and efficient graph algorithms. It also gives the sharp global extension maximum \(I_n\) with a unique maximizer. Barbina-Casanovas use partial Steiner systems explicitly in the model-completion construction, so the polynomial gives a compact quantitative invariant for exactly the finite diagrams underlying that framework.

Same-model review: passed. Independent audit: not yet performed.
