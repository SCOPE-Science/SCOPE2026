# Self-review

**Correctness — PASS.** The claim quantifies over all ternary Newman polynomials, without a degree cutoff. Multiplication with carry forces a finite 0–144 state space. An explicit 32-state reachable closure partitions into 20 live states and 12 traps; traps cannot return to zero. Every live edge preserves the five-digit carry history and outputs exactly the corresponding coefficient of the claimed multiplier polynomial. The terminal zero-history condition handles polynomial tails. The independent-from-enumeration finite certificate is replayable in `verify.py`; a nontrivial example is checked. No computation is substituted for an unbounded argument.

**Originality — PASS on accessible evidence, with residual risk.** The 2023 primary preprint [1] explicitly leaves the *local* entry for multiplier 289 undecided in its Section 4 table. Its carry-transducer construction does not supply the present 20-live/12-trap invariant or the forced polynomial quotient. The paper's established families and worked cases do not settle its marked question. Searches for equivalent polynomial identities, reversed divisibility, ternary binary-digit multipliers, 289, and the original table identified no covering published theorem. A related digraph manuscript is described as in preparation in public author information, but no citable completed text was available for comparison; an unpublished resolution remains possible.

**Mathematical value — PASS.** This is not an arbitrary small numerical example: 289 is the sole explicitly unresolved local/universal cell in the source's table through 364, and the present result supplies an exhaustive degree-independent answer. The 20-live-state certificate explains why the usual local carry anomalies cannot be completed and identifies a unique quotient polynomial for *every* admissible representation. It closes a concrete motivating classification gap without purporting to solve the global problem.

**Scientific limitations.** The result is multiplier-specific; there is no claim of a general classification or of independent validation. The sole significant novelty risk is unpublished or unindexed work, especially the announced further study of the same digraph family.

Self-review: passed. Independent audit: not yet performed.

Reference: [1] Anders, Dawsey, Reznick and Sisneros-Thiry, arXiv:2308.07252v1 (14 August 2023), especially Sections 1, 4 and 5.
