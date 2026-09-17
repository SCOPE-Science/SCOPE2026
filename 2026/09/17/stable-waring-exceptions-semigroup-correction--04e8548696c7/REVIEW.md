# same-model review

## Verdict

PASS on correctness, originality-to-the-best-of-our-knowledge, and value. This is a same-model review, not independent validation or peer review.

## Correctness audit

### 1. The p=3 counterexample is internal to the primary source

The current arXiv PDF is v2 dated 31 March 2025. On p. 10, Table 2 states `|B^2| = 7`. Theorem 10.7 on the same page states, for every odd prime p, `|B^(p-1)| >= p^(p-1)(p-1)/2`. Substituting p=3 gives 9, contradicting the table. This alone proves the theorem is false as stated.

The record also gives an independent derivation: `S_2=<3,8,15,...>`, while `<3,8>` has gaps `{1,2,4,5,7,10,13}` and conductor 14; every later generator is at least 15. Thus the permanent offset set has exactly seven elements.

### 2. Offset/semigroup equivalence was checked in both directions

A representation `j+c=sum x_i^k` subtracts exactly j copies of 1 and gives `c=sum(x_i^k-1)`. Conversely, a factorization of c into t generators gives a representation for every j>=t by padding with ones. This avoids the main conceptual danger in the source proof: counting absolute non-representable integers n can inadvertently include small n that are excluded when one studies stable offsets n-j.

The gcd/cofiniteness step is also sound: a common prime divisor of all `a^k-1` would in particular divide `ell^k-1` for `a=ell`, impossible modulo ell. Hence a finite subset has gcd 1 and generates a numerical semigroup contained in `S_k`.

### 3. Prime-power hypotheses were stress-tested

The proof needs two different facts and states both hypotheses explicitly:

- `lambda(p^e) | k` makes every unit a satisfy `a^k = 1 mod p^e`;
- `k >= e` makes every p-divisible a satisfy `a^k = 0 mod p^e`.

Without either condition, the residue dichotomy `0` versus `-1` for generators can fail.

For residue `-r mod q`, if u generators come from p-divisible bases, then `u = r mod q`, hence `u>=r`. Each such generator is at least `p^k-1`, so a representable c must satisfy `c>=r(p^k-1)`. Writing `c=qt-r` gives the strict condition `t<r p^k/q`; therefore the certified count is `rM-1`, not `rM`. Summation gives `p^k(q-1)/2-(q-1)`. The strict endpoint was specifically checked because it is the off-by-one mechanism relevant to the source theorem.

### 4. The repair for p>=5 was checked separately at the exceptional small prime

For p>=7, `p(p-1)<2^(p-1)-1`; hence `p,2p,...,(p-1)p` lie below the smallest positive generator and add exactly p-1 residue-zero gaps, restoring the source theorem's numerical bound.

The inequality is true at 7 (42<63) and propagates for all larger integers by doubling: if `2^(n-1)>n(n-1)+1`, then `2^n>n(n+1)+1` because `2n(n-1)+2-[n(n+1)+1]=n(n-3)+1>0`.

At p=5 the generic small-multiple criterion fails, so the proof treats it directly. The generators of `S_4` begin 15 and 80. The four numbers 5, 10, 20, 25 are gaps and are disjoint from the nonzero-residue modular family, raising 1246 to 1250.

At p=3 no analogous supplementation exists: the exact genus is 7, so the source bound 9 really fails.

### 5. Computational cross-check

`artifacts/verify_waring_semigroup.py` independently reproduced the primary source's exact `(genus, Frobenius number)` pairs for k=2,4,6,8:

- k=2: (7, 13)
- k=4: (1321, 2641)
- k=6: (355825, 711649)
- k=8: (945121, 1890241)

It then verified the explicit modular families as subsets of these gap sets for `(k,q)=(2,3),(4,5),(4,8),(6,7),(8,5)`, checked the p=5 and p=7 supplementation, and checked the p=11 number `129687123005`. The script certifies a conductor by observing `2^k-1` consecutive reachable values after the claimed final gap; because `2^k-1` itself is a generator, all subsequent values are then reachable.

Computation is corroborative only; the general theorem has a direct proof.

## Originality audit

### Primary-source status

The current source located is arXiv:2404.08193v2, dated 31 March 2025. Searches for the exact title together with `erratum`, `correction`, `Theorem 10.7`, `Corollary 10.8`, and the numerical bound `129687123005` did not locate a correction. The current v2 still contains both the universal odd-prime theorem and the contradictory `|B^2|=7` table entry.

The source PDF contains no occurrence of the word `semigroup`; its stable B-sets are developed through representation/partition arguments rather than identified explicitly with the gap set of `<a^k-1>`.

### Equivalent-form and surrounding-literature searches

Searches included combinations of:

- `a^k-1`, `n^k-1`, `x^k-1` with `numerical semigroup`, `Frobenius`, and `Waring`;
- `sum of exactly j positive kth powers` with `numerical semigroup` and offset terminology;
- the exact source title plus `numerical semigroup`, `correction`, and theorem numbering;
- the prime-power/Carmichael modular formula and close paraphrases.

Nearby numerical-semigroup literature was found, including Gu (2022) on a different structured family, generalized repunit semigroups, geometric numerical semigroups, and Tuenter (2006). None of the inspected statements used the generator family `<a^k-1 : a>=2>` to identify these stable generalized-Waring exceptions, nor did they provide the prime-power modular bound in this record.

Tuenter's 2006 title includes "sums of powers of integers", but its abstract concerns power sums *over the gaps of a two-generator Frobenius problem*, not semigroups generated by power-minus-one values; it does not cover this result.

### Older generalized-Waring sources and residual access risk

The most relevant older source is A. A. Zenkin, *The generalized Waring problem: A new property of positive integers*, Mathematical Notes 58 (1995), DOI 10.1007/BF02304770. Its accessible abstract was inspected: it studies representations by a variable number of positive powers and the associated exceptional sets. The full text was not inspected in this cycle. It is the source most plausibly capable of containing an equivalent permanent-offset observation, so this remains the main residual originality risk for the semigroup reformulation.

Two related Zenkin works cited by Benfield--Lippard were also identified: *Waring's problem: g(1,4)=21 for fourth powers of positive integers* (Computers & Mathematics with Applications 17(11), 1989, pp. 1503--1506) and *Waring's problem from the standpoint of the cognitive interactive computer graphics* (Mathematical and Computer Modelling 13(11), 1990, DOI 10.1016/0895-7177(90)90060-Z). Only metadata/secondary descriptions were inspected here. These works predate the 2025 Theorem 10.7 and therefore cannot already contain a correction of that theorem, but they could reduce novelty of the semigroup viewpoint.

The prime-power Carmichael extension and the explicit repair of the 2025 theorem were not found in the searched sources. Originality is therefore PASS to the best of our knowledge, with the older-Zenkin full-text caveat explicitly retained.

## Internal SCOPE overlap audit

The current SCOPE repository protocols were read before research. Repository searches for `Waring`, `Benfield`, `numerical semigroup`, `2404.08193`, `129687123005`, `positive powers`, and the exact paper title returned no matching successful record. Recent repository changes and the default-branch head were also checked directly. This does not prove absence, so the check is repeated immediately before publication.

## Value audit

PASS. The contribution is not a routine parameter increment:

1. it identifies a concrete false theorem in the current version of a recent number-theory preprint by an internal p=3 contradiction;
2. it supplies a corrected proof that preserves the theorem's intended bound for every odd prime p>=5, including the published p=11 corollary;
3. it gives a structural explanation through a numerical semigroup whose gaps are exactly the permanent offsets;
4. it extends the modular mechanism from `k=p-1, q=p` to prime-power moduli controlled by the Carmichael exponent and to exponents that are arbitrary suitable multiples.

The result does **not** claim an exact formula for the genus of these semigroups, a best possible lower bound, or a complete classification of stable generalized-Waring exceptions.
