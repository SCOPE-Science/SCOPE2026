# Scientific review

## Correctness — PASS

The statement covers every odd prime and all positive exponent pairs, not merely a finite search. The exact formula for \(s(2^ip^j)\) follows from the divisor-sum identity. The sorted-subset-sum lemma is necessary and sufficient, and the five positive base certificates and excluded small cases have been regenerated with exact integers. The key infinite step is the explicit two-axis margin monotonicity calculation in `RESULT.md`; its formulas were re-derived and independently checked against direct finite differences. The inequalities are strict throughout the full stated domains. The proof states the scope of the computation separately from its unbounded argument. Residual correctness risk: human readers should independently inspect the algebra in the two \(b\)-difference formulas and monotonicity reductions.

## Originality — PASS, with stated uncertainty

Schwab and Thompson's relevant Section 6 proves prime-generated infinitude and zero density, without a two-prime-support characterization. Aidun and Thompson examine distributional properties of the same divisor-sum aggregate, not subset-sum completeness. OEIS A393492 lists finite instances but not the infinite classification. The closest published classification for ordinary distinct divisors of \(2^ap^b\) tests a different multiset, while the Carmichael \(\lambda^*\)-practical classification uses different divisor weights, so neither logically implies the theorem. Exact-term and alias searches found no matching published theorem; this is evidence of noncoverage by inspected results, not proof of absolute priority. The full text of Reuijl's relevant 2026 thesis was inaccessible, and possible coverage there or in unindexed work is a residual originality risk.

## Value — PASS

The theorem is a natural exact two-prime-support classification in a recently tabulated nonmultiplicative practical-number family. It identifies all five minimal exponent generators, proves the unexpected exclusion of every odd prime beyond \(5\), and produces explicit infinite classes of composite examples. This is more informative than extending a short table or merely checking isolated examples; it supplies a structural row-and-column closure argument specific to proper-divisor-sum weights. It does not settle the full counting problem.

Self-review: passed. Independent audit: not yet performed.
