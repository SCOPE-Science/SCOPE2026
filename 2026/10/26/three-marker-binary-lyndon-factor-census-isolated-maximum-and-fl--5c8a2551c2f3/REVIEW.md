# Scientific review

## Correctness: PASS

The theorem has a complete all-length symbolic proof. Every non-letter binary Lyndon factor must start in \(0\) and end in \(1\). With exactly three marked ones there are only the one-, two-, and three-one cases. The two-one criterion is a strictly longer first zero run; the three-one criterion is a unique longest first run or the precisely resolved tie \(i=b>c\). Distinctness between the two possible two-one families has been checked explicitly, including equal internal gaps. The all-one boundary \(111\) contributes exactly one letter.

The generating function is derived termwise from four elementary rational gap sums, with the \(m=0\) correction. Case splitting into the dominant first, second, and third zero gaps proves the unique maximum and the sharp three-unit gap to all other configurations for \(m\ge4\). A Dirichlet simplex limit with an explicit six-region integral proves the rational mean and variance coefficients. The bounded indicator term does not affect leading asymptotic orders. The stated \(O(1)\) mean and \(O(m)\) variance remainders follow from Lipschitz Riemann-sum approximation on the simplex.

Reproducible standard-library code passed all 5,985 direct length-3–20 word checks, all 23,751 four-gap configurations through zero mass 25, the rational generating-function coefficients and sharp extremal statements, and exact simplex moment arithmetic. Finite checks are supporting evidence; the all-length proof is mathematical, not experimental.

## Originality: PASS, with residual historical-priority risk

The first public source used as the archive-era research anchor is K. Saari, *Lyndon Words and Fibonacci Numbers*, arXiv:1207.4233 (2012-07-17). The accessible full paper develops Lyndon-factor bounds and Fibonacci/recurrent-word characterizations, not a full conditional census of arbitrary finite binary words of weight three. A stronger and more directly relevant later comparison is A. Glen, J. Simpson and W. F. Smyth, *Counting Lyndon Factors*, arXiv:1701.00928 and *Electronic Journal of Combinatorics* 24(3) (2017), P3.28. Its Section 4, equation (6) gives the expected number of distinct Lyndon factors for **uniform unrestricted alphabet words**. Its Sections 2 and 5 address unrestricted maxima and Christoffel-word counts. These do not imply the exact fixed-weight-three zero-gap formula, the isolated extremum, the conditional rational generating function, or the stated conditional limiting moments merely by changing a parameter. The full accessible primary texts were inspected by section and by their relevant theorems/equations.

Targeted searches also considered weight-three Lyndon factors, aliases involving Hamming weight and zero runs, generating functions for Lyndon-substring counts, OEIS sequences of Lyndon words, and published mathematical research records. No equivalent or stronger covering statement was identified. OEIS fixed-content Lyndon **word** enumeration is not an enumeration of distinct Lyndon **factors of source words**. The nearest indexed results on special factor statistics or general string complexity have different invariants and sampling laws. Failure to find a record does not prove historical uniqueness; a prior unpublished, unindexed, or differently phrased derivation remains possible.

## Value: PASS

Lyndon factors are lexicographically minimal primitive rotations and central building blocks for string factorization, de Bruijn-sequence methods, and word complexity. Fixing the number of marked symbols is a natural conditioning that the unrestricted results do not resolve. This result gives a complete explicit classification for the first sparse family with three internal marker-to-marker comparisons, an exact rational aggregate series for all lengths, a genuinely isolated extremal word, and a nondegenerate conditional limiting distribution with rational variance coefficient. The sharp gap and fluctuation law provide structure beyond a routine count of one constructed word. The claim is mathematical and self-contained; it does not require a proposed downstream application to be meaningful.

## Closest literature and limitations

The strongest possible overlap risk is the 2017 unrestricted-expectation analysis of Glen–Simpson–Smyth; the difference between unconditional and conditioned sampling is explicit, and the older paper's tables cannot recover the complete individual zero-gap census. Saari's lower bound pertains to source words that are themselves Lyndon, a different quantified domain. Exact sequence searches showed no identified matching table. The present classification applies only to linear words over \(0<1\) with exactly three ones. Priority remains provisional pending wider independent scholarly verification. The checker is finite and the scientific review is not independent validation.

Self-review: passed. Independent audit: not yet performed.
