# Independent mathematical audit

## correctness

PASS

PASS: The permitted weights are distinct products of exactly seven distinct rational primes. Independent enumeration of squarefree integers with omega(n)=7 recovered the first weight 510510 and c_3100=19111638, c_3101=19114095; an independently written exact 40,000,001-bit 0/1 subset-sum dynamic program with exactly those first 3100 weights proved 19027139 unreachable while every integer from 19027140 through 40000000 reachable. Unused weights exceed the alleged gap, so non-representability persists. For each c_j, replace its largest prime by the next prime q<2p by Bertrand: a valid 7-prime product is strictly between c_j and 2c_j, forcing c_(j+1)<2c_j. The starting interval width 20972861 exceeds c_3101, and two translated intervals concatenate inductively with growing width >= c_(j+2). This proves the infinite tail; the finite DP is exact, not sampling. The separate checked source C++ and alternative Python implementations show independent algorithm designs; own independent third implementation corroborated the exact finite certificate.

## originality

PASS

PASS best of knowledge: Butler–Erdős–Graham introduced the exact conductors a(k), asked for further values, and listed a(1) through a(6) only. Their original full article was inspected and its page-eight question read. An unrelated 2026 result on distinct semiprime unit fractions solves a different reciprocal-denominator problem, not integer subset sums of squarefree 7-almost-primes. No matching previously published seventh conductor located after statement/number searches; possible prior computational table outside indexed sources remains a risk.

## value

PASS

PASS: The seventh case of an explicitly posed arithmetic conductor sequence is an independently meaningful exact sharp invariant. Determining both the final missing integer and proving all integers thereafter represented requires a nontrivial exhaustive 0/1 finite certificate plus a rigorous infinite propagation lemma; neither is a trivial parameter substitution of the six published cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
