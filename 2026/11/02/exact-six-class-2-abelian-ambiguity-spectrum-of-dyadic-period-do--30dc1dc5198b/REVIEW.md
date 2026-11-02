# Scientific review: dyadic period-doubling 2-Abelian ambiguity spectrum

## Correctness — PASS
The factor parity identity supplies every factor, and disjointness is proved from the absence of `11` in the fixed point. Endpoint-count matrices transform by an exact two-parameter recurrence, giving a parity-separated closed table. Three distinguishable digram signatures per zero-content stratum have sizes \(a+b,a+b,2b\); the two strata yield the six formulas. The proof handles all \(k\ge3\), does not extrapolate finite tests, and lists the smaller scales only as excluded boundaries. The standalone checker constructs genuine finite prefixes, directly enumerates all distinct factors through length \(2^{10}\), recomputes full 2-Abelian signatures, and cross-checks an independently implemented factor desubstitution.

## Originality — PASS (historical priority qualified)
Parreau, Rigo, Rowland and Vandomme (arXiv:1405.3532, Section 5, Propositions 34–35 and Corollary 41) studied 2-Abelian *complexity* of the same period-doubling word, determining signatures and regularity but not the exact sizes of each signature class. Karhumäki, Saarela and Zamboni (arXiv:1302.3783, Section 4) computed its 1-Abelian complexity and studied 2-Abelian complexity of a different sequence. The proposed six-class size multiset strengthens a class-count invariant by resolving every class fiber. Searches for dyadic 2-Abelian factor multiplicities, equivalence aliases and broader period-doubling classifications found no covering claim. The strongest primary work was read at the relevant section's full-text level; priority remains uncertain outside the sources accessed. The structured comparison in AUDIT.json lists exact scope and residual risks.

## Value — PASS
The result quantifies information loss under digram-statistical observation of a canonical morphic word. Its exact two-scale ambiguity profile, including linear minimum and maximum fiber sizes, is a complete infinite-family structural invariant not supplied by known 2-Abelian complexity. The desubstitution and endpoint proof provides a reusable mechanism for studying higher local-observation spectra.

## Verification limits
The checker's finite direct enumeration is a reproducibility test, not an infinite proof; the induction is presented in RESULT.md. The theorem is restricted to distinct dyadic factors with \(k\ge3\), with no claim about positional frequencies, non-dyadic lengths, or higher-order Abelian equivalence. Independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
