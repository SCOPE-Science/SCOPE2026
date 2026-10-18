# Scientific review: exact four-coordinate channel capacity

## Correctness (PASS)
The claim is about arbitrary finite alphabets, not just tested small values. The permitted radius-one permutations of four positions are exactly the identity, each of three single adjacent swaps, and the disjoint double swap. The action preserves symbol multiplicities. A complete five-partition classification gives the ball-size profiles and exact packings; the only delicate upper bound is the three-codeword ceiling in the repeated-twice pattern \((2,1,1)\): four balls could fit by size only if all four centers had ball size three, but two of those four balls overlap. Every bound is met by explicit disjoint balls. Counting the components proves \(A_q(4;1)=q^2(q+1)(q+2)/6\). Standalone exhaustive verification confirms the finite canonical cases and the constructions for alphabet sizes two through six; computations do not substitute for the all-\(q\) proof.

## Originality (PASS, with residual risk)
The closest 2017 primary article defines the same channel and lists the binary four-coordinate optimum as eight in Table II; that special case is prior work, not a new claim. Its general-alphabet exact construction concerns length three and its other results concern code bounds and rate constructions. The full 2025 adjacent-transposition paper gives asymptotic bounds and block-code constructions; the full 2026 extinction-depth paper gives finite-horizon criteria, explicit rates, and length-six/longer covering bounds. Neither establishes the five exact length-four composition capacities or their all-alphabet summation. Equivalent-model searches and scientific record searches did not identify dominating exact coverage. Unindexed older finite-dimensional work, or an implicit exact formula not recognized as such in other coding tables, is a residual risk. Originality has not been independently audited.

## Value (PASS)
The next natural exact finite-length parameter after the known three-coordinate case is an operational quantity: how many distinct messages can be sent in four channel uses and decoded against all simultaneous disjoint swaps. The proof gives the optimum for every alphabet size and completely explains which symbol multiplicities limit it. In particular, at \(q\ge3\), the strict gap \(qA_q(3;1)-A_q(4;1)=q^2(q-1)(q-2)/6\) quantifies the nontrivial penalty from an additional unprotected coordinate, something neither rate asymptotics nor the known binary table alone resolves.

## Sources and limits
Primary scientific sources are Langberg–Schwartz–Yaakobi (2017), Kovačević–Kiah–Goyal (arXiv:2509.06692), and Ben Shimon–Lev Zabokritskiy (arXiv:2607.19566); specific URLs are in RESULT.md. The exact original binary parameter is credited. The result makes no longer-length or successive-error claim. Scientific independence and exhaustive historical novelty cannot be established from this review.

Self-review: passed. Independent audit: not yet performed.
