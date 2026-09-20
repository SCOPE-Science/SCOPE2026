# Same-model scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was rederived from the defining divisibilities. The key points were checked separately: normalized shifted factors are pairwise coprime; their least common multiple is therefore 2abc; the quotient (n+1)/(2abc) is a positive integer strictly below 4; and each of its three possible values leads to the stated finite case analysis. The surviving triple (5,13,31) was checked directly against the Lucas-Carmichael criterion.

A supporting exact-integer program independently enumerates the three-prime Lucas-Carmichael triples with smallest prime below 100 and finds 190 triples, with (5,13,31) the unique shifted-gcd-2 case. The proof does not depend on this finite search.

## Correction note

The published proof was rechecked after upload. Its pairwise-coprimality step now explicitly works modulo \(2d\), not merely modulo \(d\): if \(d\mid a,b\), then \(2d\mid p+1,q+1\), so \(2d\mid qr-1\) forces \(d\mid c\). This corrects a missing factor of two in the first posted wording; the theorem and all subsequent arguments are unchanged.

## Originality

Originality is assessed to the best of our knowledge. Wright's infinitude paper was inspected for the defining Korselt-like condition and global construction context. The relevant sections of Tamilvanan--Muthukrishnan were inspected, including Proposition 3.3 and Theorem 4.2: they give factor bounds and the decomposition (2hr1-1)(2hr2-1)(2hr3-1) with pairwise coprime normalized factors, but no classification of h=1 was located. The three-prime Lucas-Carmichael section of Einsele--Paterson was also inspected; it uses a normalized common-gcd decomposition for counting bounds, but no g=2 uniqueness statement or occurrence of 2015 was located. OEIS A006972 and exact/synonymous web searches likewise did not locate the theorem.

The strongest residual risk is not a known competing theorem but possible coverage in older problem literature, theses, or material indexed under a different terminology. No inaccessible source identified during this review supplied concrete evidence of prior coverage.

## Value

The result gives a complete, cutoff-free classification of the smallest-common-gcd stratum in the natural three-prime structural decomposition. It isolates 2015 as the unique primitive instance and complements existing infinitude, structural-form, and counting results.
