# Review of the isolated-gap classification

## Correctness (C): PASS

The claimed set follows from an explicit Apéry representative in each residue \(2j\pmod a\), namely \(w_j=a\lceil j/2\rceil+2j\). The adjacent-residue calculation is exhaustive: no gap with \(j\le s\) has its predecessor in the semigroup, whereas for \(s+1\le j\le2s\) both neighbors belong precisely when \(u\ge\lceil(j-s)/2\rceil-1\). Together with the gap constraint \(u\le\lceil j/2\rceil-1\), this proves the exact set for every odd \(a\ge3\). Distinct residues permit direct summation; the genus and Frobenius formulas follow from the same minima. The accompanying checker independently compared exact sets for 150 odd multiplicities, covering 1,158,925 gaps and 579,425 isolated gaps. These finite tests are not used as an infinite proof.

## Originality (O): PASS, with residual bibliographic risk

Singh–Ram (arXiv:2406.09848v1, 2024), read in its accessible full-text form, classifies isolated gaps only for embedding dimension two. Smith (2022) supplies general Apéry observations and two-generator results; only the abstract and its detailed discussion in Singh–Ram were accessible. Moreno-Frías–Rosales (2020), whose original eight-page article was inspected, classifies zero isolated gaps for embedding dimension three, not the positive isolated-gap set or its cardinality in this arithmetic progression. Çelik (2023) studies \(\langle a,a+2\rangle\) and halves of two-generator semigroups; its inspected original article does not imply the present three-generator formula. A later article on multiplicity-three semigroups intersects the case \(a=3\), not the full odd-parameter family. Searches of relevant mathematical records, bibliographic sources, and accessible related claims found no equivalent statement, but unindexed or implicit deductions remain possible. A search failure is not a novelty proof.

## Mathematical value (V): PASS

The 2024 explicit enumeration for two generators motivates a natural next test case: the smallest nonconsecutive three-term arithmetic progression with coprime generators. Here the entire isolated-gap set has a structured triangular-strip description; the striking exact relation \(|I(S_a)|=\lfloor g(S_a)/2\rfloor\) explains its quadratic growth and shows that roughly half the gaps are isolated, unlike the bounded isolated-gap behavior of the consecutive-step progression. The same proof locates both extreme isolated gaps. This is a complete natural-family classification of an arithmetic semigroup invariant, not an arbitrary finite census, a table recomputation, or a claim about all three-generated semigroups.

## Limitations and closest sources

The statement applies only to odd \(a\ge3\) and step size two; finite verification covers just the displayed range. Smith's full text and some later related full texts were not accessible, and the novelty assessment cannot rule out every implicit consequence of older general algorithms. No independent scientific audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
