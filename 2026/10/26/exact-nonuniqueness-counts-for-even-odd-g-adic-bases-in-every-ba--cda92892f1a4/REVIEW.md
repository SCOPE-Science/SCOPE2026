# Scientific review

## Correctness — PASS
The proof separates cross-parity, even–even and odd–odd representations; its digit-carry model uses the exact bound \(2(g-1)\) and accounts for the final forbidden carry beyond \(g^{2k}\). The intersection count \(2^{2k-1}-2^{k-1}-2^k+1\) requires \(g\ge3\), while the pure-digit multiplicity threshold \(\lfloor g/2\rfloor\ge2\) requires \(g\ge4\). All pure unique and unrepresented cases are classified before combining the counts. The symbolic identity was independently checked by direct unordered summand-pair enumeration for every \(4\le g\le10\), \(1\le k\le3\). No step infers an infinite theorem from these finite tests.

## Originality — PASS, subject to residual bibliographic risk
Ling–Tang (2015), Theorem 1.1 and pp. 375–378, treats exactly this parity-partition basis in every base, but proves density-one uniqueness and strong minimality, not the finite cutoff count. Tang (2026), Theorem 1.1 and Corollary 1.3, extends qualitative uniqueness and minimality to arbitrary infinite partitions for \(g>h\) without the exact count. Tang–Ling (2018) addresses minimality hypotheses, not the exceptional-set spectrum. A previously known base-three count does not imply the stated base-\(g\ge4\) classification: isolated power representations change multiplicity at four. Targeted semantic-result and ordinary literature searches did not locate a stronger equivalent statement. This is not a uniqueness proof; an older derivation may remain undiscovered.

## Mathematical value — PASS
The exceptional-set size in a classical thin, strongly minimal additive basis is a natural invariant: density-one uniqueness leaves its growth undetermined. The formula supplies an exact count at every complete digit-block cutoff for all \(g\ge4\), an explicit leading constant, and the sharp exponent \(\log_{g^2}(2g-1)\). The shift from the small-base behavior is structural (the number of carry splittings changes), not merely notation. There is no claim of a general theorem for arbitrary partitions.

## Closest literature and limitations
The most direct comparison is Ling–Tang (2015), because it uses the identical object and weaker conclusion. Tang (2026) is the recent motivating source. Tang–Ling (2018) supplies earlier digit-basis context. See `RESULT.md` for precise statement, proof, and scientific limits. Independent literature verification and independent mathematical audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
