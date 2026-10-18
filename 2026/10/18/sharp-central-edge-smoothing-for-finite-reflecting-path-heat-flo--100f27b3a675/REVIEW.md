# Scientific review

## Correctness — PASS

The edge incidence matrix intertwines the reflecting vertex generator with the Dirichlet edge generator. The key nonstandard lemma—unimodality of every Dirichlet heat-kernel row—is proved by ordered-minor preservation for products of adjacent two-state stochastic heat kernels, together with the Lie–Trotter limit; it is not inferred from mere positivity. Cauchy–Schwarz reduces the maximum to a diagonal, and the cycle-image difference system proves its strict center location. The finite sine series, strict comparison with the infinite-lattice return probability, the uniquely maximized Bessel time factor, and the diffusive limit then follow with the stated normalizations. The standalone checker passed 4,029 finite test assertions. The proof is analytical for all path lengths and times; the numerical tests alone would not establish the universal statements.

## Originality — PASS within examined sources

Dowker's discrete Neumann/Dirichlet image and eigenfunction formulas are antecedent inputs, not claimed as new. Wang–Yan's continuous-domain Neumann estimate uses a different input norm and does not give optimized discrete-path constants. Münch–Wojciechowski's graph gradient contraction assumes Lipschitz input, whereas the present sharp norm permits arbitrary bounded input. Abadias–de León-Contreras provide nonsharp infinite-lattice derivative-kernel estimates, and De Ponti–Stefani derive consequences of an assumed bounded-to-Lipschitz estimate without the finite-path constant. The closest accessible published mathematical results likewise concern distinct heat-envelope, sensor-determinant, or temporal-derivative invariants. No inspected stronger theorem implies the exact spatial path norm together with its central-edge rigidity and sharp global time constant. Older birth–death-chain total-variation or monotone-coupling literature could still contain an equivalent restatement; originality remains subject to independent priority checking.

## Value — PASS

The sharp bounded-input smoothing constant measures worst-case amplification of graph-edge variation for finite diffusion, a natural stability quantity not specified by generic curvature or kernel bounds. Its exact formula works for every path size and time, identifies the unique geometrically worst location, proves the finite-size boundary deficit, and determines the optimal all-size time-weighted estimate. The diffusive limit supplies a separate continuum-scaling benchmark. These are structural, parameter-uniform conclusions, not an arbitrary numerical slice of an existing table.

## Limits

The result does not extend to all graphs, weighted edges, or alternative rate normalizations without additional arguments. The principal literature risk is an older path/birth–death gradient coefficient expressed via variation of neighboring Markov transition laws. No independent scientific audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
