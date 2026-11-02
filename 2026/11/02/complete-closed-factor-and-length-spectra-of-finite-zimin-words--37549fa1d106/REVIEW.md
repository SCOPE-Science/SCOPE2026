# Scientific assessment: complete closed-factor spectra of finite Zimin words

## Correctness — PASS

The claimed classification holds for every literal finite Zimin word of rank at least one. Every factor has a unique occurrence of its highest letter and hence a unique pair of left and right extension lengths. The proof of sufficiency constructs a border by shifting across two equal low-rank ruler blocks and proves that its highest letter has exactly two appearances. The necessity argument shows that any border extending into unequal dyadic-length shells has an additional occurrence entirely on its longer side, so it cannot establish closedness. Summing square shell cardinalities gives the total formula and counting pair sums gives the exact triangular length distribution. The boundary cases with zero extensions and rank one are handled explicitly. Independent direct software enumeration matches the full predicted set, each length, and each highest-letter count at ranks 1–8. This is a finite diagnostic, not the infinite proof.

## Originality — PASS with residual priority risk

Badkobeh, Fici, and Lipták (arXiv:1305.6395, first public 2013-05-28) develop general closed-factor criteria, lower bounds, binary examples, and extremal tables; their general statements and constructions do not imply the dyadic-shell iff classification or the exact Zimin length spectrum. Schaeffer and Shallit (arXiv:1508.02074) use automatic-sequence predicates and analyze five named infinite words, not finite Zimin words. Wojcik's 2019 presentation does give the unique-highest-letter factor representation of the infinite Zimin word, a fact used and credited here; it does not state a closed-factor classification in the material inspected. Parshina and Puzynina (arXiv:2111.00863) give a general quadratic extremal asymptotic, not the rank-and-length-specific formula.

The known per-marker numerical sequence is also OEIS A047849, but there it is interpreted as closed walks and other structures, not closed Zimin factors. OEIS A375453 agrees accidentally with the first six total counts but differs at the seventh rank. Neither numerical hit constitutes claim-level prior coverage. Relevant research-record search hits on binary closed-rich maxima address global binary extrema at short lengths, not literal finite Zimin words. A full bibliographic priority search and independent review remain pending.

## Value — PASS

The result is a complete classification, not an arbitrary finite census: it identifies the exact two-sided-extension rule underlying closed factors, provides the complete length spectrum with systematic holes at powers of two, and evaluates its rank total for an exponentially long classical ruler word. For length \(N=2^n-1\), the count has nonzero quadratic density \(C_n/N^2\to1/9\), a natural benchmark relative to known extremal closed-factor estimates. It identifies a reusable 2-adic mechanism for complete first returns in structured finite words. The theorem is restricted to literal finite Zimin words; it does not establish extremality or apply to arbitrary morphic images.

## Remaining verification limits

The mathematical proof is internally reviewed only, the checker covers ranks 1–8, and historical priority is not exhaustively established. The 2019 Zimin presentation is not a substitute for inspecting all related unpublished theses, so undiscovered related coverage is possible.

Self-review: passed. Independent audit: not yet performed.
