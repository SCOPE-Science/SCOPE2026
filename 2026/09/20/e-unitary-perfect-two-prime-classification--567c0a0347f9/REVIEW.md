# Review: two-prime e-unitary perfect classification

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The argument was checked from the defining multiplicative formula
\[
\sigma^{(e)*}(2^a q^b)=\left(\sum_{d\mid^*a}2^d\right)\left(\sum_{e\mid^*b}q^e\right).
\]
The key factor split is valid: after dividing by \(2q\), the first normalized factor is odd, while the second is congruent to 1 modulo \(q\). Therefore no prime other than \(q\) can divide the first factor, and no positive power of \(q\) can divide the second; this forces the exact identities \(A=q^{b-1}\) and \(B=2^a\).

The subsequent normalized-product argument was checked separately. The bound
\[
R_b<1+1/(q-1)\le3/2
\]
is strict and yields \(S_a>4/3\). Every proper divisor of \(a\) is at most \(a/2\), so replacing the proper unitary divisors by all integers through \(\lfloor a/2\rfloor\) gives a valid upper bound. For odd \(a\ge3\) this upper bound is at most \(5/4\); for even \(a\ge6\) it is at most \(39/32\). The two remaining cases \(a=2,4\) are resolved exactly, with only \(a=b=2,q=3\) surviving.

The edge cases \(a=1\) and one-prime support were explicitly checked. The example \(36\) satisfies \(\sigma^{(e)*}(36)=72\). A standalone exact-integer computation over a broad finite box finds no contradictory example. The computation is supportive rather than part of the proof.

No hidden hypothesis such as squarefullness is used in the new proof: exponents equal to 1 are covered by the normalized identities and inequalities.

## Originality

The originality claim is **to the best of our knowledge**.

The following coverage was checked:

- The indexed text of Subbarao--Suryanarayana (1971) already defines exponentially unitary perfect numbers and states the no-odd theorem. The visible indexed abstract does not state a two-prime classification.
- Minculete--Tóth (2011) was inspected in full at the relevant definition, theorem, and open-problem section. It proves there are no odd e-unitary perfect numbers and asks whether an e-unitary perfect number not e-perfect exists; no two-prime classification appears there.
- Hanumanthachari--Subrahmanya Sastri--Srinivasan (1978) is known to prove the analogous e-perfect theorem: 36 is the only e-perfect number with two distinct prime factors. This was checked in the standard 2004 handbook summary. That theorem does not by itself cover e-unitary perfect numbers because the implication from e-unitary perfect to e-perfect is open in general.
- Current OEIS entries A391281 and A322858 were checked. They record known e-unitary perfect examples and the unresolved relation to e-perfect numbers, without citing a two-prime e-unitary classification.
- Kalita--Saikia (2025) was inspected at its e-unitary definitions and results; it studies e-unitary Zumkeller numbers and does not supply the claimed classification.
- Searches using “e-unitary perfect”, “exponential unitary perfect”, “exponentially unitary perfect”, “unitary e-perfect”, and combinations with “two prime factors”, “two distinct prime factors”, “classification”, “theorem”, and “36” did not locate prior coverage.
- The current SCOPE archive was searched by the same object and synonymous terminology; no overlapping finding was found.

### Residual originality risk

The most important unresolved source-access risk is the 1971 Notices item: indexed text was available, but the full issue itself was not directly inspectable. Because it is an abstract and the indexed text exposes its principal theorem statements, the remaining risk appears limited but nonzero. The full 1978 *Math. Student* article was not directly inspected; however, it concerns e-perfect rather than e-unitary perfect numbers, and its relevant two-prime conclusion is explicitly reported in a standard handbook. Older literature sometimes varies between “exponential unitary,” “unitary exponential,” and “exponentially unitary” terminology, so an unindexed equivalent statement is the main residual risk.

## Value

The result closes the complete two-prime-support case for e-unitary perfect numbers with a short structural proof. Its main conceptual consequence is a new necessary condition for any counterexample to the longstanding question whether an e-unitary perfect number can fail to be e-perfect: such a counterexample must have at least three distinct prime factors. It also matches, by an independent argument, the classical two-prime classification for e-perfect numbers.

## Limitations

The theorem gives no classification for three or more prime supports and no existence or nonexistence result for an e-unitary-perfect-but-not-e-perfect integer. The originality statement is literature-bounded rather than exhaustive, and there is no formal proof-assistant verification.
