# Scientific review: cubic generalized-Mersenne family

## Correctness — PASS

The nonstandard ingredient is the exact minimum of the weighted \(\{1,b,c\}\) coin-change problem. Three local exchanges prove its greedy optimum for every nonnegative input, with an explicit terminating potential; the divisibility assumption \(a=mc\) then makes Apéry minimization exact. The two endpoint maxima give the Frobenius formula, summing all greedy weights gives the genus, and a generator-by-generator maximal-Apéry argument yields precisely two pseudo-Frobenius numbers. The unrestricted scope is \(h\ge3\), \(m,d\ge1\), and \(\gcd(m(h^3-h+1),d)=1\). Independent Dijkstra and dynamic-programming computations over finite parameters agree with every stated invariant. No finite computation is used to prove the unrestricted result.

## Originality — PASS within inspected evidence

The closest primary work is Liu, Xin, Ye and Yin, arXiv:2306.03459 (2023), which proves formulas for the binary family and in Section 6 notes that the higher-base greedy-weight monotonicity fails; it does not give this divisible cubic Apéry and pseudo-Frobenius classification. Their arXiv:2306.10738 uses ordinary repunit offsets \((h^i-1)/(h-1)\), which differ from \(h^i-h+1\) for \(h\ge3\). Their arXiv:2304.09039 treats a constant coefficient of the first generator, not the successive powers here. Branco–Colaço–Ojeda (2022) studies repunit-start families with geometric increments and does not state this exact generator pattern. Search of publicly indexed mathematical literature and semantic records yielded no equivalent complete result. Bibliographic completeness cannot be guaranteed; an implicit specialization of a broader theorem remains possible. The binary boundary and general computational principles are expressly excluded from the novelty claim.

## Value — PASS

A published higher-base extension identifies loss of the monotonicity that solves the binary case. The theorem identifies a natural unbounded subfamily where the complete Apéry set is nevertheless computable, and extracts three standard invariants plus an exact, parameter-controlled pseudo-Frobenius spacing. This is an infinite classification across \(h,m,d\), not a single computed datum, a normalization check, or a mere rephrasing of the binary formulas. The restriction to cubic length and divisible first generator remains substantial and is stated openly.

## Limits and closest prior literature

The higher-base problem for arbitrary first generators or longer lists is unresolved here. Available searches do not prove uniqueness in the mathematical literature. The proof and checker are subject to independent mathematical review.

Self-review: passed. Independent audit: not yet performed.
