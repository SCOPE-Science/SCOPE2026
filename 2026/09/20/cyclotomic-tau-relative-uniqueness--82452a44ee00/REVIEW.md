# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The argument was checked step by step.

- `Phi_{2 p^k}(n)` is odd for every integer `n`, so divisibility by `tau(n)` forces every prime-factor exponent of `n` to be even.
- Because `Phi_{2 p^k}(0)=1`, any common prime divisor of `n` and `tau(n)` would contradict the assumed divisibility.
- Modulo `p`, `Phi_{2 p^k}(x)` reduces to a positive power of `x+1`; if `p | tau(n)` this forces `n=-1 mod p`, contradicting that `n` is a nonzero square when `p=3 mod 4`.
- For every remaining prime `ell | tau(n)`, the cyclotomic quotient identity and the value at `n^{p^{k-1}}=-1` show that `ord_ell(n)=2 p^k` exactly.
- The order formula for a power, `ord(u^m)=ord(u)/gcd(ord(u),m)`, makes the divisibility of all prime-factor exponents bootstrap from `(2p^k)^r` to `(2p^k)^{r+1}`. Infinite divisibility of a fixed positive exponent is impossible.

The proof also correctly extends to positive powers of the cyclotomic polynomial because prime support, rather than valuation size, drives the order argument. A finite exact-integer check over seven `(p,k)` cases and all `n <= 10^6` found no nontrivial solution; it is supporting evidence rather than part of the proof.

## Originality

PASS, to the best of our knowledge, with an explicit residual risk.

The primary 2021 paper was inspected at the theorem/open-problem level. It proves infinitude when `|Q(0)Q(1)| != 1`, gives prime-power-index cyclotomic polynomials as examples on that side, and reports only a computation through `10^8` for `x^2-x+1` and several other type-II polynomials. It does not state the theorem proved here. The 2023 University of Tartu thesis continues the type-II problem and likewise describes the general `|Q(0)Q(1)|=1` case as unresolved.

Exact and synonymous searches were made for relative tau-numbers, divisor-count divisibility by `n^2-n+1`, cyclotomic formulations, and the 2021 authors. The current SCOPE archive was also searched for tau-polynomial/cyclotomic and `x^2-x+1` formulations; no overlap was found.

The largest originality uncertainty comes from a footnote in the 2023 thesis saying that an article was then in preparation describing an unspecified class of polynomials for which 1 is the only relative tau-number. The footnote provides no title, author list, identifier, or description of the class. Current searches and the publicly indexed later publications of the 2021 first author did not identify that article. It could nevertheless contain overlapping coverage, so originality is not claimed beyond the documented search.

## Value

PASS. The result converts a concrete computationally unresolved example from the 2021 paper into a theorem and simultaneously supplies an infinite family of nonconstant type-II polynomials with a unique relative tau-number. It also complements the same paper's positive cyclotomic result for `Phi_{p^k}` with a negative family for `Phi_{2p^k}` when `p=3 mod 4`. The proof gives a reusable order-bootstrap mechanism rather than a finite search.

## Limitations

The congruence class `p = 3 mod 4` is essential to the present proof. No classification is claimed for `p = 1 mod 4`. The unspecified in-preparation article mentioned in the 2023 thesis remains the principal literature uncertainty.
