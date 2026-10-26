# Review of the exact binary cutoff-three composition profile theorem

**Correctness — PASS.** The run-count and endpoint-singularity identities determine every length-one-to-three composition count, and the observation conversely determines all six signature invariants. Exhaustive endpoint conditions are enumerated by eleven generating-series terms (including one inclusion-exclusion subtraction). The all-length rational identity is checked by an exact polynomial certificate in `verify_profiles.py`; finite brute-force and independent DP replay supplement it. The result is restricted to linear binary words with multiplicities and all substring lengths up to three.

**Originality — PASS, with residual risk.** Ye–Elishco (2022), Section VIII, defines the model and studies Lyndon-based codes with cutoff proportional to block length; it explicitly raises the constant-cutoff problem. The closest public exact binary result treats cutoff two, with no length-three singleton-run/endpoint phenomena. An ordered adjacent-pair multispectrum result and full-spectrum reconstruction have different observations and do not imply the exact truncated-cutoff-three quotient count. Searches may miss unindexed equivalents, and the full 2015 source was not read.

**Mathematical value — PASS.** The theorem exactly enumerates all possible length-three-limited observations for every block length, including a nontrivial period-four quartic, giving the maximum size of noiseless fixed-length reconstruction codes and sharp fourth-degree growth. The object and invariant are defined by a motivated molecular-composition reconstruction model, rather than an arbitrary parameter slice.

**Limits.** No efficient canonical encoder/decoder, error correction, higher cutoff, nonbinary generalization, or individual ambiguity-class formula is established. All claims use proved all-length generating-function identities rather than finite experimentation alone.

Self-review: passed. Independent audit: not yet performed.
