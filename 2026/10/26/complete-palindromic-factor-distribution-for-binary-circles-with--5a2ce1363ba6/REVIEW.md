# Scientific review

## Correctness — PASS

The claim fixes oriented binary necklaces with exactly three ones, excludes the empty palindrome, and restricts cyclic-factor lengths to the circumference. The proof enumerates every palindrome by its number of ones, handles repeated gaps without double counting, and derives the four disjoint formulas. The rational generating function is obtained by exhaustive cases on the ordering/equalities of three nonnegative gaps, including the correct rotational orbit weights. The distributional limit follows from a uniform-simplex Riemann sum and three-event inclusion-exclusion. Direct palindrome-set checks, bivariate-coefficient checks, and independent rotation-class enumeration from `checker.py` all passed. The all-length proof, rather than finite sampling, supports the theorem.

## Originality — PASS, conditional on available-source comparison

The global upper bound and near-sharp examples belong to Simpson (2014); the universal maxima tabulated in OEIS A247000 are known and explicitly credited. Neither the accessible abstract nor the fully inspected OEIS record states the fixed-composition, two-statistic distribution or its rational generating function; those broader global assertions do not imply this distribution. Searches of research records by three-one sparse-circle and palindrome-inventory aliases showed no covering public statement. A relevant 2014 paper remains inaccessible in full, including its near-extremal construction section, so equivalence under another formulation remains a priority risk; originality here is assessed under that explicit limitation.

## Value — PASS

The three-one family is a natural sparse binary family that already supports near-extremal circular palindrome counts, making the shape of its full palindrome inventory a motivated question. The result determines every individual inventory, every fixed-composition count for all lengths, and a nondegenerate limiting distribution with exact mean. It describes the entire spectrum rather than incrementing a known extremal table; correctness or novelty of isolated coefficients is not the value argument.

## Closest literature and remaining limitations

Jamie Simpson, *Palindromes in circular words*, Theoretical Computer Science 550 (2014), 66–78, DOI: 10.1016/j.tcs.2014.07.012. OEIS A247000, initial record September 15, 2014, https://oeis.org/A247000. Both concern the same circular-palindrome statistic; published general maxima and examples must not be presented as discoveries here. The inaccessible primary full text limits historical-priority confidence. The scope is exactly three ones and factors no longer than the circle, and no independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
