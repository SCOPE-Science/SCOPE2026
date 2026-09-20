# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

Write `m=a+1`, `c=b+1`, `A=(2^(km)-1)/(2^k-1)`, and `B=(p^(kc)-1)/(p^k-1)`. The assumed `k`-harmonic divisibility implies `AB | 2^(ak) p^(bk) m c`.

For `B`, Bang--Zsigmondy always supplies a primitive prime divisor `s`: here the exponent `kc>=4`, the base `p` is odd, and neither exceptional case applies. Its order is exactly `kc`, so `s>=kc+1>c`. Since `s|B` and `s` is neither `2` nor `p`, the divisibility forces `s|m`, giving `m>=kc+1`.

For `A`, except when `km=6`, Bang--Zsigmondy supplies a primitive prime divisor `r` with `r>=km+1>m>c`. The same divisibility then forces `r=p`, hence `m|p-1`. But `s|m` gives `p=1 (mod s)`, contradicting `ord_s(p)=kc`. If `km=6`, the two possibilities `(k,m)=(2,3)` and `(3,2)` already contradict `m>=kc+1` for `c>=2`. The proof therefore covers every `k>=2`, `a,b>=1`, and odd prime `p`.

The exceptional cases of Bang--Zsigmondy were checked explicitly in the proof. No empirical assumption enters the theorem. A separate exact-integer enumeration over 42112 finite parameter choices produced zero counterexamples.

## Originality

PASS, to the best of our knowledge, with a stated residual risk.

Cohen--Deng (1998) introduced `k`-harmonic numbers. The accessible bibliographic record does not provide the full text. A detailed standard secondary source, Sándor--Crstici (2004), attributes to Cohen--Deng only necessary conditions for a hypothetical even two-prime proper `k`-harmonic number `2^a p^b`: `b=7 mod 8` for even `k`, and `b` odd with `(p+1)(b+1)=0 mod 16` for odd `k`. That summary is materially weaker than complete nonexistence.

Searches for the exact object, synonymous `power-harmonic` terminology, two-prime-factor statements, and Zsigmondy/primitive-divisor formulations did not locate the theorem proved here. Searches of the current SCOPE archive under `k-harmonic` and `power-harmonic` also found no overlap.

The main residual originality risk is the unavailable full text of Cohen--Deng, MR1680101 (Nieuw Arch. Wisk. (4) 16 (1998), 161--172). Because that paper studies the exact object and derives the weaker displayed restrictions quoted by the handbook, it is the source most capable of containing an equivalent unindexed argument. No concrete evidence of such coverage was found.

## Value

PASS.

No proper `k`-harmonic number with `k>=2` is currently known in the checked literature. Earlier work left a detailed congruence-restricted search space for even numbers with two prime factors. The present theorem removes that entire support pattern uniformly in all exponents and all `k>=2`. It follows that every even proper power-harmonic number must have at least three distinct prime factors, a structural reduction that is independent of computational bounds.

## Limitations

The theorem does not treat odd integers with exactly two distinct prime factors, and it does not address even integers with three or more distinct prime factors. The originality assessment is qualified because the complete 1998 primary paper was not directly inspected.
