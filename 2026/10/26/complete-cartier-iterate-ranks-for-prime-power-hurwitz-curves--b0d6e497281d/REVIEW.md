# Scientific review: complete Cartier-iterate ranks for prime-power Hurwitz curves

## Correctness — PASS
The curve is smooth because the Hurwitz smoothness modulus \(q^2+q+1\) is coprime to \(p\). On the canonical-adjoint basis the Cartier operator is an injective partial monomial permutation. Every nonzero transition deletes one low base-\(p\) digit pair, replaces it by a forced no-carry high pair, and has a nonzero multinomial coefficient. The successive rank formula follows by exact digit counts, not by finite extrapolation. The standalone coefficient-expansion verifier independently reconstructed the matrix and iterated ranks for representative primes and exponents and returned `VERIFY_OK`.

## Originality — PASS, with residual risk
Montanucci–Speziali (2016), §4, established the \(a\)-number and first-step rank for the identical \(n=sp+1\) Hurwitz family. That special case is acknowledged and excluded from the new contribution. Their statement does not supply the ranks of higher Cartier powers, stable image or nilpotent multiplicities. The inspected Dawson et al. supersingularity theorem and Borges–Gonçalves Fermat-type \(p\)-rank formulas do not settle the full Cartier filtration on this Hurwitz quotient. Search covered exact equations, equivalent twisted Hasse–Witt products, stable-rank and nilpotent block descriptions, published research records, and accessible earlier mathematical entries. No dominating statement was located. Uninspected specialized work may contain an equivalent result.

## Mathematical value — PASS
The formula gives the complete rank profile of the Cartier operator on a classical infinite family of smooth curves. In particular, it identifies the previously undetermined stable \(p\)-rank and the lengths and multiplicities of nonordinary nilpotent strings; for \(e\ge3\) these are strictly finer than the published \(a\)-number. This is useful information about the \(p\)-torsion cohomology of the Jacobian, not a minor numeric increment.

## Scope and limitations
The theorem does not assert a full Newton polygon, polarization or Ekedahl–Oort type. The \(e=1\) ordinary case and previously known single-step Cartier rank are not claimed as original. Finite computational checks are only supplementary to the general proof. Unlocated equivalent specialized literature is a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
