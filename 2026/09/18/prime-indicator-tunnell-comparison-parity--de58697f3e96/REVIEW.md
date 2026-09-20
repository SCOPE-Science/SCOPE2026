# Review

## Scientific claim

For every coefficient-comparison row used in Section 7 of Im--Shin, arXiv:2609.19085v1, the normalized ternary comparison coefficient has parity equal to the prime indicator on odd square-free indices in that row. Via the source paper's Proposition 7.1, the same statement holds modulo \(1+i\) for the normalized weight-\(3/2\) Fourier coefficient.

The consequence is a method-level obstruction: the exact mod-\((1+i)\) comparison proving the source paper's prime theorem becomes zero on every square-free composite in the same progressions, so that comparison alone cannot extend the nonvanishing argument to composites.

## Correctness

**PASS.**

For the \(x^2+y^2+z^2\) rows, Gauss's three-square formula and genus theory give
\[
2^{\omega(n)-1}\mid r_3(n)/8
\]
for odd square-free \(n\equiv3,5\pmod8\). Thus every composite has even normalized comparison coefficient, while Im--Shin Lemma 7.2 supplies oddness for primes.

For \(x^2+3y^2+5z^2\), the parity reduction
\[
r_{135}(n)/4\equiv A(n)+B(n)\pmod2
\]
follows from the sign-orbit decomposition for every \(n\equiv7\pmod8\), not just primes. The required composite evenness is then proved by an ideal-counting lemma for the discriminants \(-12\) and \(-60\): for square-free arguments coprime to \(30\), every represented proper class has either zero or \(2^{\omega(m)-1}\) positive representations. The exceptional possibility \(3\mid n\) in the modulus-40 row is reduced to the forms \(x^2+3y^2\) and \(x^2+15y^2\); the remaining two-prime case is resolved by the row's mod-5 condition.

The argument was stress-tested against the tempting but false global extension: \(r_{135}(39)/4=3\) and \(r_{135}(111)/4=7\), and both indices lie outside the comparison sets. This confirms that the residue hypotheses used in the proof are substantive.

A standalone exact-integer verifier enumerates both ternary representation functions through 100000 and checks all twelve published comparison rows. It performs 29,548 square-free row-membership checks with no failure and separately verifies the two outside-row counterexamples. This computation supports but does not replace the proof.

## Originality

**PASS, to the best of our knowledge.**

The full relevant portions of Im--Shin v1 were inspected. Proposition 7.1 establishes the normalized coefficient congruences for all positive integers in the comparison residue sets. Lemmas 7.2 and 7.3 then analyze the comparator parity only for prime indices, and Theorem 7.4 uses that prime parity to prove non-\(\theta\)-congruence for primes. The paper does not state that the normalized comparator parity equals the prime indicator on all odd square-free indices in those rows, nor the resulting one-extra-\((1+i)\) divisibility for every square-free composite.

The three-square class-number formula, genus theory, and the binary quadratic-form facts for discriminants \(-12\) and \(-60\) are classical ingredients and are not claimed as new. The new contribution is their uniform synthesis across all twelve Section-7 comparison rows and the resulting obstruction to a composite extension by the same first-layer congruence.

Searches included exact and synonymous formulations involving the Im--Shin preprint, Tunnell comparison coefficients, square-free composite parity, \(r_3(n)/8\), \(r_{135}(n)/4\), and prime-indicator congruences. No equivalent or stronger statement was located. Earlier work on composite non-\(\theta\)-congruent numbers uses different angles and/or descent and does not provide this comparison-row parity law.

No inaccessible source was identified whose available metadata specifically suggests the same theorem. The principal residual originality risk is that arXiv:2609.19085v1 is extremely recent, so contemporaneous follow-up work may not yet be indexed.

## Value

**PASS.**

The theorem identifies exactly what information the source paper's mod-\((1+i)\) Sturm comparisons contain beyond the prime case: on square-free inputs in all published prime progressions, the first residue layer is precisely a primality detector. This is useful negative structure. It prevents a natural but futile attempt to obtain composite nonvanishing from the same parity comparison and points directly to the missing information: higher \((1+i)\)-adic terms, a new comparator, or direct Fourier-coefficient analysis.

The result is not merely the observation that genus theory gives more powers of two. The nontrivial part is that the \(x^2+3y^2+5z^2\) rows require a row-sensitive binary-form analysis, including the \(3m\) branch in the modulus-40 progression; outside the published rows the asserted composite parity is false.

## Limitations

The theorem is confined to the comparison rows of Im--Shin Tables 8 and 9. It does not give a global square-free parity theorem for \(r_{135}\); the explicit values at 39 and 111 show such a statement would be false.

The additional \((1+i)\)-divisibility for composite indices does not imply that the Fourier coefficient vanishes. Consequently this record does not by itself produce new composite non-\(\theta\)-congruent or \(\theta\)-congruent families.

The motivating preprint is very recent, so unindexed contemporaneous work remains a residual originality risk. No independent validation or formal proof-assistant verification is asserted.

**Same-model review: passed. Independent audit: not yet performed.**
