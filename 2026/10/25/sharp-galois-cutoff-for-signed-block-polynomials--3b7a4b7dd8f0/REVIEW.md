# Review: sharp Galois cutoff for signed-block polynomials

**Correctness: PASS.** The new boundary \(n=8\) consists of two reciprocal representatives. The reductions modulo \(7\) and \(3\) are irreducible, proving transitivity in prime degree \(7\); the two discriminants have odd prime factors appearing once, giving transpositions, and hence \(S_7\). The lower-degree table's modular irreducibility, cycle, and discriminant certificates are replayable. The infinite \(n\ge9\) step is explicitly sourced to Garmi; it is not extrapolated from experiments. The two exceptional cubics have distinct quadratic discriminants and linearly disjoint \(S_3\) splitting fields.

**Originality: PASS, with residual risk.** Garmi's public v1 theorem and proof require \(n>8\) for the coefficient-two family. The new contribution is the sharp cutoff obtained by resolving \(n=8\), not the older large-degree result or previously catalogued \(n=7\) factors. Searches did not reveal a dominating degree-seven endpoint computation; such a computation might nevertheless be implicit in earlier literature.

**Value: PASS.** The least uniform threshold is mathematically natural for an explicit bounded-coefficient family previously treated only above an effective cutoff. Its exact determination includes both missing degree-seven Galois groups and a counterexample at the immediately preceding degree. This is a sharp boundary classification and not a claim of a new proof for all large degrees.

**Limitations.** Coprime exponents only. No independent audit. The full earlier literature on specific degree-seven polynomials has not been exhaustively indexed. Complete proof details and a runnable exact certificate are in RESULT.md and verify.py.

Self-review: passed. Independent audit: not yet performed.
