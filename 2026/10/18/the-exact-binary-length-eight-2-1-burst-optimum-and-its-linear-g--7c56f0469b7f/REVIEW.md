# Review of the binary length-eight \((2,1)\)-burst optimum

**Correctness — PASS.** The channel is exactly one adjacent two-to-one replacement in an eight-bit word. The standard-library C++17 verifier constructs all \(256\) error balls, independently confirmed via string slicing, checks the explicit \(14\)-word code and an \(8\)-word binary linear code, and exhaustively rules out any compatible clique of size \(15\). Its greedy-color partition bounds every branch and its exhaustive include/exclude recursion checks all possibilities. The independent string-incidence integer optimization corroborates the optimum, but its solver output is not the proof certificate. An upper bound of \(14\) immediately limits binary linear sizes to at most \(8\), which the exhibited span attains.

**Originality — PASS against inspected statements.** Lu and Zhang's general bound permits \(16\), not \(14\). Schoeny and collaborators provide relevant \((2,1)\)-burst constructions but do not settle the sharp length-eight maximum. The closest examined published finite results concern three-to-one bursts, unrestricted bounded substring edits, and deletion followed by arbitrary substitution; their channel semantics do not imply the stated bound or its linear counterpart. Direct and alias-based searches found no exact duplication. A differently indexed table or unindexed thesis is an acknowledged residual risk.

**Value — PASS.** A standard synchronization channel has a sharp finite optimum that is below the sphere-packing estimate, while nonlinear codes accommodate six more codewords than any linear code at the same blocklength. The result provides an exact, reproducible natural benchmark rather than an artificial parameter slice or an extrapolated sequence.

Scope: binary length eight only; the proof is finite exhaustive computation and does not claim all-length behavior. The two channel implementations, witness vectors, exhaustive graph search, and independent numerical check are supplied. No outside independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
