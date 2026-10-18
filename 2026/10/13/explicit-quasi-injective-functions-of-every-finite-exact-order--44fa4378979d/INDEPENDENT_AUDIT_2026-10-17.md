# Independent mathematical audit

## correctness

PASS

For each integer m≥2, source defines g_m on exponents with two disjoint length-(m−1) chains terminating at 0; for e≥L=2m−1, g(e)=1 on squares and m otherwise, and f_m(2^e u)=2^{g_m(e)}u with u odd. Then on the tail g_m^k(e)=k for square and m+k−1 otherwise for every 1≤k<m, while g_m^m(e)=0 identically. Suppose f_m^k(an)=f_m^k(bn) for all n; choose n=2^e to force equal odd parts A=B and eventually equal shifted exponent responses g_m^k(e+r)=g_m^k(e+s). If r≠s, arbitrarily large squares t² have t²+|r−s| nonsquare, since fixed difference of two squares admits finitely many solutions; so the two responses differ, contradiction. Thus all k<m quasi-injective. At k=m, choosing multipliers 2^L and 2^(L+1) gives identical odd parts for every n, proving first failure. Independently checked explicit chain/collapse and tail distinctions for every m=2..13 and e across 500 tested tail exponents, supplementary to all-m proof.

## originality

PASS

PASS best-of-knowledge: Pongsriiam 2021 Question 17 explicitly asks whether functions of each finite exact quasi-injectivity order exist. Inspected primary paper proves quasi-injectivity for divisor-counting/Jordan totient iterates and asks the existence question, but does not itself produce these arbitrary-order collapse functions. Nearby Resultary October 4 paper concerns preservation under RIGHT composition by divisor function and addresses a different Question 18. Targeted searches did not identify a dominating general construction; potential unpublished solutions remain a real risk.

## value

PASS

PASS: resolves an explicit published existence question uniformly for every finite m, with fully constructive computable examples and a transparent sharp iterate collapse. Nonmultiplicative examples are permitted by the question; the result clarifies possible depth of an arithmetic-function injectivity property, not a merely arbitrary numerical experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
