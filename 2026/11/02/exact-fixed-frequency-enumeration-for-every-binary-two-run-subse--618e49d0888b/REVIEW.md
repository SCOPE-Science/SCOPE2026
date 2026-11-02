# Scientific review

## Correctness — PASS

Fix a binary word with a positive number of scattered occurrences of \(0^a1^b\). The \(a\)-th zero is canonical. Label its following ones, record the first \(q-b+1\) preceding-zero counts, and classify occurrences by their first selected one. This proves the weighted binomial profile equation, not just an upper bound. Its positive summands imply \(\binom{q}{b}\le k\) and \(\binom{t_r}{a}\le k\), establishing termination of the profile enumeration. A word of fixed profile is recovered uniquely from \(a+b\) free nonnegative gap variables and has baseline length \(q+t_r\), proving the rational generating function. Its numerator has positive value at \(z=1\) when a profile exists, proving exact polynomial degree \(a+b-1\); otherwise no word has that positive occurrence frequency.

The standalone checker separately computed subsequence multiplicities on binary words and matched the formula in 3,168 exact parameter/length comparisons, including the five-occurrence example through length 39. These finite checks are corroboration; the all-parameter proof is combinatorial and independent of them.

## Originality — PASS, with specified residual risks

Bruda, *Enumerating binary words restricted by subsequence frequency*, arXiv:2607.02578v1, states the general eventual polynomial upper-degree bound and explicitly asks for complete sharpness criteria; it mentions the pattern \(0011\) at frequency five as a pre-existing exceptional example. The present result does not claim that exception as a discovery. It supplies instead a finite canonical profile set, an exact positive-numerator generating function for every fixed positive frequency of every binary two-run pattern, and a complete if-and-only-if degree criterion in that subclass. Bruda's eventual upper bound alone cannot determine the exact numerator or positivity.

Menon–Singh, arXiv:2306.07870v1, gives small-frequency formulas and extremal occurrence results, not the all-frequency two-run classification. Tian, arXiv:2507.03205v1, develops general occurrence and primitive-word methods but does not state this specific canonical profile formula or its degree-sharpness consequence in the inspected sections. Targeted searches of closely related research records and web literature did not yield an equivalent statement. A more general algorithm could be specialized to obtain some counts with additional work; an overlooked earlier equivalent formula remains a priority risk. A match between a special case's numerical coefficients and the classical tetrahedral sequence is not coverage of its word-counting interpretation or the two-run theorem.

## Value — PASS

The source paper identifies the failure of its known sufficient sharpness conditions and proposes determining when the general upper degree is attained. The answer for **all** two-run binary patterns and **every positive frequency** is a natural, nontrivial complete subfamily of that problem. The explicit finite numerator also supports exact length-by-length enumerations, not only eventual growth, and separates unattainable frequencies from all attainable ones.

## Scope and limitations

The claim excludes zero frequency, three-or-more-run patterns, and alphabets beyond two letters. The decidability criterion uses a finite but potentially expensive arithmetic enumeration. No unperformed independent verification, publication-priority guarantee, or broader classification is asserted.

Self-review: passed. Independent audit: not yet performed.
