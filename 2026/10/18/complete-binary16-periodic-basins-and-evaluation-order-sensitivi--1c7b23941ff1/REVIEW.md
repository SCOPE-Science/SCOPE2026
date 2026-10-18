# Review of the binary16 quadratic map census

## Correctness — PASS

All states and rounding operations are unambiguously defined. A complete enumeration of every distinct numerical binary16 value in \([-2,2]\) produces \(32{,}769\) vertices, and exact integer comparison constructs the complete two deterministic successor arrays with correct nearest-ties-even selection. The indegree-peeling algorithm finds all cycles and assigns every transient state to its unique basin. The packaged verifier checks every successor with a separately implemented binary16 conversion path, verifies graph labels and depths for all inputs, checks full basin sums, and rederives all exact fractions and displayed orbit invariants. The almost-everywhere real mean is separately justified by standard real conjugacy to the ergodic full logistic map. The finite graph proof does not claim universal arithmetic-format generality.

## Originality — PASS, with priority risk

The 2022 Wu–Fu–He–Wang source introduces this exact quadratic family, gives the \(a=1,b=2\) chaotic regime and discusses numerical and analogue realizations, but its inspected full text does not present these exact binary16 transition, periodic-basin, evaluation-order or mean results. Finite-precision logistic studies [2,3] concern other numerical maps or rounding mechanisms; the affine real conjugacy does not intertwine the discrete alphabets and rounded transitions. Directly related published mathematical-record searches and the accessible prior-census records did not expose the identical claim. Neither failed searches nor the difference in wording proves absolute novelty; an independent reproduction of the same exhaustive table could exist elsewhere.

## Mathematical value — PASS

The 2022 source's physical motivation is the possibility that digital quantization compromises chaotic dynamics. The complete binary16 global census gives the exact digital long-term alternative: six versus five attractor cycles under a single operation-order choice, an extreme 94-versus-44 period switch, complete basin-size distributions, and explicit nonzero long-run average bias where the underlying real invariant law has mean zero. Unlike a parameter-free exercise or a short simulated orbit, the finite result is a natural, exhaustively evaluated numerical invariant of an explicitly published chaotic dynamical map and exposes a concrete source of reproducibility sensitivity.

## Source inspection and limitations

The originating 2022 open-access article's complete model, simulations, circuitry and conclusion were compared against the mathematical claim. The 2017 finite-precision logistic article and 2023 low-precision periodic-orbit article were inspected for rounding and periodic-basin coverage. Related mathematical-record entries on Chebyshev two-cycles and quantized affine maps differ in both object and conclusion. An equivalent unindexed finite-state census remains a priority risk. All computations are restricted to the stated format and exact two rounding protocols, not the actual analogue circuit. The verification uses same-project code and a distinct local half-conversion oracle, not an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
