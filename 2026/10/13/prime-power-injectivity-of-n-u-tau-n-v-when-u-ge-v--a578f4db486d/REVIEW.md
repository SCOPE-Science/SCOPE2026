# Review of Prime-power injectivity of \(n^u\tau(n)^v\) when \(u\ge v\)

## Correctness
**PASS.** On a prime power, \(\tau(p^a)=a+1\), so equality becomes \(p^{au}(a+1)^v=q^{bu}(b+1)^v\). If the prime bases differ, prime-adic valuation gives \(p^a\mid b+1\) and \(q^b\mid a+1\) because \(u\ge v\). Hence \(p^a q^b\le(a+1)(b+1)\), while \(p^a\ge a+1\) and \(q^b\ge b+1\). Equality would force both prime powers to be \(2^1\), contradicting distinct bases. Equal bases are handled by strict monotonicity in the exponent. The counter-ray is exact: \(F_{t,3t}(2^6)=F_{t,3t}(7^3)=21952^t\) for every \(t\ge1\).

## Originality
**PASS.** Gabdullin--Iudelevich--Luca (arXiv:2201.09287v1, 2022) analyze the image of \(k\mapsto k\tau(k)\) and record its noninjectivity, but do not state prime-power injectivity. The focal 2023 paper proves squarefree injectivity for \(n^u\tau(n)^v\), but prime powers of exponent greater than one fall outside that theorem. Its section on \(D(n)=n\tau(n)\) studies global collisions and leaves primitive collisions open, without a prime-power classification. OEIS A338382 catalogs collision values but does not state prime-power injectivity. Exact-form, alias, and implication searches in the published published-finding corpus corpus and the open web returned no equivalent statement. The closest published published-finding corpus records concern Jordan-totient products or compositions with divisor-function iterates, so neither implies this claim. Residual risk remains that an older source states the elementary prime-power lemma under different terminology.

## Value
**PASS.** Prime powers are the canonical non-squarefree local strata for multiplicative arithmetic functions. The result complements the published squarefree theorem on an infinite family of repeated-prime inputs and does so uniformly over the two-parameter range \(u\ge v\). The infinite counter-ray \(v=3u\) demonstrates that parameter balance matters rather than being cosmetic.

Self-review: passed. Independent audit: not yet performed.
