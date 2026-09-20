# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The cubic argument is closed under explicit 4-decimations. The identities
\[
t_3(4n+2)=8t_3(n-1),\qquad t_3(4n+3)=8t_3(n)
\]
are direct consequences of the standard two-scale coefficient recurrence, and the remaining classes \(4n,4n+1\) are odd by the established cubic arithmetic. After adjoining the backward-shifted odd-part sequence, all four decimations return either one of the two target sequences or fixed decimations of \(t_3\bmod2^s\). This yields a finite 4-kernel and hence 2-automaticity.

For \(m=5\), substituting \(q+1=2^r u\) into the published recurrence and dividing by the published exact valuation gives
\[
Y_r=5Y_{r-2}-4Y_{r-4}.
\]
The powers of its companion matrix are eventually periodic modulo every \(2^s\). For \(m=9\), the same normalization of the published eighth-step block recurrence gives
\[
Y_r=205Y_{r-2}-8274Y_{r-4}+68224Y_{r-6}-65536Y_{r-8}.
\]
All divisions are justified by the exact valuation theorems, so the normalized quantities are integers. On each parity class, both are fixed finite-order recurrences. Their finitely many initial slices are automatic modulo \(2^s\) because \(t_m\) is 2-regular and only fixed additional 2-adic precision is required. The standard odd-part and valuation substitutions then preserve automaticity.

Adversarial checks focused on index alignment, signs, the coordinate reversal in the ninth-power block, and whether eventual periodicity requires an invertible companion matrix. It does not: powers in any finite matrix monoid are eventually periodic. The coordinate alignment is exact: the vector \(X_{2^{r+2}u}\) consists of the block \(t_9(8q),\ldots,t_9(8q+7)\) in reverse order when \(q+1=2^r u\).

Exact finite computation independently reproduced the coefficient recurrences, valuation formulas on substantial ranges, and both normalized recurrences through coefficient index 200000.

## Originality

**PASS, to the best of our knowledge.**

The September 2026 Shen paper explicitly states as Conjecture 6.1 that odd parts modulo every fixed power of two should be 2-automatic for all positive exponents. Its proved cases are \(m=2^r\), \(m=3\cdot2^r\) with \(r\ge2\), and \(m=6\). It specifically discusses \(m=3\) only to note that the zero set is automatic; the full cubic odd-part sequence remains under the conjecture.

The June 2026 Shen–Wang paper proves the fifth- and ninth-power valuation formulas and supplies the exact matrix recurrences used here, but its accessible full text does not state automaticity of the normalized odd parts. The 2018 Gawron–Miska–Ulas paper supplies the cubic recurrences and zero/valuation structure, not this automaticity conclusion.

Searches using the recent arXiv identifiers, the source titles, "automatic odd parts", "2-automatic", the notation \(t_5,t_9\), and equivalent Thue–Morse power terminology did not locate prior statements of the three conclusions or the normalized recurrence mechanism.

The most relevant source not fully inspected is Xinping Wang's May 2026 undergraduate thesis, *Research on the Properties of Coefficients of Integer Powers of Generating Functions for Thue-Morse and Rudin-Shapiro Sequences*. It matters because the June Shen–Wang paper cites it in connection with the fifth-power valuation work. A complete thesis text was not located in the material inspected. The accessible June paper based on that line of work states valuation results rather than odd-part automaticity, so the thesis is a residual originality risk rather than evidence of coverage. The September conjecture paper is also very recent, leaving the usual risk of unindexed concurrent work.

## Value

**PASS.**

The result settles three previously uncovered cases of a newly stated all-exponent conjecture. The cases are structurally nontrivial: \(m=3\) contains zeros, while \(m=5\) and \(m=9\) have unbounded valuations depending on \(\nu_2(n+1)\). The proof also isolates a reusable mechanism: after exact valuation normalization, a finite recurrence in the valuation depth reduces odd-part automaticity to eventual periodicity of finite companion-matrix powers. Together with the previously proved cases, this leaves only \(m=7\) unresolved among exponents at most 9.

## Limitations

The argument does not settle arbitrary odd exponents or construct minimal automata. It relies on published exact valuation formulas for \(m=5\) and \(m=9\). The verification artifact is supportive rather than a substitute for proof, and no independent validation or formal proof-assistant verification is asserted.
