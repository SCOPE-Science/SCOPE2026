# Review status

Fresh independent audit: **PASSED**.

Independent audit passed. The capped histogram is an exact finite sufficient state for the cited q-decimal model and yields the autoregressive bounded-halting/ultimate-periodicity dichotomy.

- Correctness: **PASS** — The finite summary is sufficient under the stated Qiao finite-precision semantics on well-defined prefixes. Realized RoPE phases are periodic and hidden vectors range over a finite set. At a new causal position, old keys/values of the same layer, RoPE phase, and hidden type contribute identically. Capping a type count at \(10^{2q}+1\) is exact: any finite positive rounded exponential is at least \(10^{-q}\), so a saturated positive type forces the rounded denominator beyond \(10^q\) and hence to Inf, making the well-defined head output zero under the source convention; otherwise every positive multiplicity is stored exactly. Thus the prefix update and readout are deterministic functions of a finite state. The eventual-periodicity and bounded-halting conclusions then follow by pigeonhole on the deterministic orbit.
- Originality: **PASS** — The motivating Qiao paper proves a narrower non-memorization result using finite-precision RoPE periodicity and softmax saturation, not a global streaming state for every prefix or an ultimate-periodicity theorem for iterative decoding. Jerad--Svete--Li--Cotterell characterize a related fully uniform periodic-RoPE recognizer class as a regular temporal-logic class, but their model and claim concern one-pass language recognition, not this explicit capped-histogram state and the uniform autoregressive-generation dichotomy in Qiao's q-decimal overflow semantics.
- Scientific value: **PASS** — The theorem turns a model-specific incompleteness mechanism into a complete dynamical restriction on every deterministic autoregressive continuation: halting serial work is uniformly bounded and nonhalting continuations eventually cycle. That is a motivated structural boundary for finite-precision chain-of-thought models, not merely a one-input experiment.

Full evidence, source comparisons, limitations, and residual risks are recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.

The historical same-model assessment remains preserved in `AUDIT.json` and is not treated as independent validation.
