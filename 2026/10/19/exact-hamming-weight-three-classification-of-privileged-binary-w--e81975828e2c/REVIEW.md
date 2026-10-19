# Scientific review

## Correctness — PASS

An explicit border-case proof starts from the definition of complete returns, derives all possible privileged words with zero, one, or two occurrences of \(1\), then classifies every three-one word by its number of ones in a privileged return border. The only nonpalindromic possibility is \(0^a1 0^b1 0^c1 0^a\) with \(a\ge1\), \(0\le b,c<a\), and \(b\ne c\). A disjoint constructive converse verifies all qualifying families. Geometric-series summations give the generating functions; exact pole analysis yields minimal quasipolynomial period twelve and quadratic leading term \(n^2/24\). The standard-library verification script checks the recursive definition against the independently implemented gap criterion for every three-one binary word of lengths 3 through 37, plus coefficient comparisons through 256. Finite checks support but do not replace the all-length proof.

## Originality — PASS, with residual risk

The closest full-text sources inspected were Gabrić, *Asymptotic bounds for the number of closed and privileged words* (arXiv:2206.14273, public 2022-06-28), and Schaeffer–Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences* (DOI:10.37236/5752), especially its logical characterization of privilege. The former develops unrestricted asymptotic bounds rather than weight-three enumerations. The latter supplies a broad decision/definability framework, not this explicit gap-family classification or length distribution. OEIS A231208 and A235609 give unrestricted counts and examples, not a weight-three formula. A preview of Forsyth et al., *Remarks on Privileged Words* (DOI:10.1142/S0129054116500088), was also inspected; its full text was not accessible, leaving priority risk. Searches for equivalent formulations and stronger results did not reveal the claimed classification. Search failure is not proof of novelty, and no independently certified priority claim is made.

## Mathematical value — PASS

Privileged words form a natural hierarchy defined by iterated complete returns. The theorem pinpoints the first weight permitting nonpalindromic privileged binary words, classifies *every* word in that stratum, gives its complete palindromic/nonpalindromic generating functions, and shows nonpalindromes have density one within it. This is a structural boundary rather than a computational table, generic rationality statement, or arbitrary length cutoff. It does not establish formulas for all fixed weights.

## Limitations

The proof treats exactly three occurrences of \(1\) and provides no infinite-weight result. Some general logical results may provide an alternate route to derive the enumeration, and unindexed analyses or inaccessible relevant full text could contain equivalent formulas. No independent audit or external validation has been performed.

Self-review: passed. Independent audit: not yet performed.
