# Self-review

**Correctness — PASS.** The proof treats every exponent partition through \(\Omega(n)=4\); its only nontrivial last case reduces to \((q-3)(r-3)=16\). The inequalities excluding \(p^3q\) and \(p^2q^2\) hold for every prime, without finite bounds. Direct checks at \(12,18,220\), and the next-layer witness \(396\), agree with the independent recurrence-and-sieve computation.

**Originality — PASS, subject to publication-risk caveat.** OEIS A211991 describes the exact signed difference and A212127 lists its zeros, but the inspected material contains no unlimited exclusion theorem for \(\Omega(n)\le4\). Ufnarovski–Åhlander (2003) establishes derivative fundamentals. The nearest published arithmetic-derivative gap record compares with the cototient rather than with the aliquot sum; its statement does not imply this result. Undiscovered or unindexed proofs remain a risk.

**Value — PASS.** It determines a natural entire prime-factor-multiplicity layer of a previously tabulated equality, including the unique multiplicity-four and three-support composite \(220\). The next-layer solution \(396\) marks the genuine limit of this first classification and motivates extensions beyond it.

**Limits and sources.** This is not an unbounded classification of all solutions. Finite verification through \(500000\) corroborates but does not prove the theorem. Closest scientific sources: OEIS A211991, OEIS A212127, Ufnarovski–Åhlander (2003), and the published arithmetic-derivative cototient-gap study (different second function). No independent audit is asserted.

Self-review: passed. Independent audit: not yet performed.
