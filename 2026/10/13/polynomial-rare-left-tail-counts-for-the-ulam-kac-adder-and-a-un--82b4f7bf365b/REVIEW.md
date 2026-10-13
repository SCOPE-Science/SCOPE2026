# Scientific review: polynomial rare-left-tail Ulam–Kac counts

## Correctness — PASS
The recurrence \(e_{t+1}=e_t+U_t+e_{U_t}\) follows exactly from the adder definition. Conditioning on the first \(r\) index choices freezes every subsequent index that can occur on a path with final surplus \(r\). The resulting finite generating polynomials yield an exact nonnegative-integer binomial-basis polynomial, for every integer \(n\ge r\ge0\). Comparing its highest three coefficients to the classical inversion-code distribution gives the leading deficit \((r-2)\binom{n-r}{r-2}\) for each fixed \(r\ge3\), and division by the Mahonian leading term gives the inverse-square limit. Exceptional \(r=0,1,2\) cases are excluded from the deficit assertion. The standalone Python verifier completed 164 exact checks, including all index histories to length nine, as finite corroboration only.

## Originality — PASS, with residual risk
Ben-Naim and Krapivsky (2002, arXiv:cond-mat/0208072v1, pp. 1–2) give only the first two smallest-value probabilities, not a polynomiality result for every fixed surplus. Bonner (2023, arXiv:2303.03606v1, Sections 1–4 and 6) studies moments and first-passage questions rather than the fixed-surplus point-mass law; the related 2025 dissertation Chapter 3 similarly focuses on moments. Mahonian inversion counts and traditional Brauer-chain endpoint counts are prior, but do not imply the claimed fixed-length adder enumeration. Targeted record/literature searches and available previous claims did not reveal covering results. These searches are not proof of priority; older addition-chain literature could contain an equivalent identity.

## Value — PASS
The problem is a natural left-tail enumeration for the Ulam–Kac adder, a standard history-dependent probabilistic model. All fixed surpluses are handled by one constructive finite-prefix formula rather than isolated endpoint checks. The exact inverse-square discrepancy quantifies the first nontrivial effect of history feedback compared with the classical independent-index/Mahonian distribution; its coefficient varies meaningfully with the surplus. This does not solve typical-value or first-passage problems.

## Closest literature and limitations
G. Bonner, *On the moments of the Ulam-Kac adder*, arXiv:2303.03606v1 (2023); E. Ben-Naim and P. L. Krapivsky, *Growth and Structure of Stochastic Sequences*, arXiv:cond-mat/0208072v1 (2002); Bonner's 2025 dissertation Chapter 3; OEIS A008302 and A008927. The argument is for fixed surplus and finite discrete time; its asymptotic does not cover growing surplus.

Self-review: passed. Independent audit: not yet performed.
