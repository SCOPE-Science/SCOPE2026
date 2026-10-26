# Mathematical review

**Correctness: PASS.** The urn transition is computed from the full initial inventory, including its original white ball. The killed first moment satisfies \(A_{n+1}=A_n+u_n\); this in combination with the monotone coupling and the summable-coefficient bootstrap establishes \(u_n=O(n^{-3/2})\) and finite mean. Eighty exact-rational finite checks match the formulas. Finite tests are not used as a substitute for the infinite proof.

**Originality: PASS, with residual risk.** Section 5 of Balaji and Mahmoud explicitly poses the finite expected first return as a conjecture. Bertoin's standard elephant-walk analysis includes related initial-condition and persistence results; his \(p=0\) standard first return is deterministic at time two, so is not the same boundary event. General arbitrary-level elephant hitting theorems could potentially subsume the finding, and this remains an originality risk.

**Value: PASS.** The claim resolves a specific published first-return integrability conjecture and supplies a nontrivial survival-tail exponent upper bound using a reusable killed-moment and random-walk-comparison argument.

**Closest literature:** Balaji and Mahmoud, *Urn-driven random walks* (2026), Sections 4–5; Bertoin, *Counting the zeros of an elephant random walk* (2022). The proof does not establish exact asymptotic constants, does not treat two dimensions, and does not construct a stationary distribution of a time-homogeneous position process.

Self-review: passed. Independent audit: not yet performed.
