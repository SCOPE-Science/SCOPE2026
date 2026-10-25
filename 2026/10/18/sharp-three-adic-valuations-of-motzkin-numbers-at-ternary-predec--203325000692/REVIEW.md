# Independent mathematical audit

## correctness

PASS

Start with the exact Motzkin generating function F(z)=(1-z-sqrt((1-3z)(1+z)))/(2z²). For q=3^r the extraction coefficient at z^(q-3) is -1/2 sum_{j=0}^{q-1}(-3)^j binom(1/2,j)binom(1/2,q-1-j). The half-binomial is an integral Catalan factor divided by a power of two. All j>=r terms vanish modulo 3^r, and the j=0 term equals 2^(-2(q-1))C_(q-2) because q-1 is even. For 1<=j<r let m=q-j-2 and t=ceil(log_3(j+2)): high ternary digits 2 in m force >=r-t Kummer carries upon doubling, so ν3(C_m)>=r-t-ν3(j+1). Check j=1, j=2 (special ternary digits 2,1,2,...,2 and exactly r carries), and j=3 directly, then j>=4 using t<=floor(j/2) and ν3(j+1)<=floor(j/2), to obtain j+ν3(C_m)>=r. Therefore every j>=1 vanishes and the asserted congruence holds. Finally q-2 in base3 has digits 1,2,...,2, generating exactly r-1 carries on doubling; q-1 is a 3-unit, hence ν3(C_(q-2))=r-1 and the congruence determines ν3(M_(q-3)) exactly. r=1 gives M0=1. An independent integer-recurrence calculation for all 1<=r<=7 reproduced indices 0,6,24,78,240,726,2184, valuations 0,1,2,3,4,5,6 and all congruences; finite checks are not the infinite proof.

## originality

PASS

Best-of-knowledge original explicit unbounded exact 3-adic valuation family. The origin Rowland–Yassawi paper directly asks in Open Question 3.15 whether ν3(M_n) is unbounded, and its 2026-rendered primary arXiv text still states that question. Straub (2022) determines all primes below 200 with Motzkin valuations bounded by one versus having a valuation at least two, and gives the full 2-adic valuation; this does not entail unbounded growth along 3^r-3. The submission answers the unboundedness half and does not claim to resolve 3-regularity.

## value

PASS

An exact infinite family ν3(M_(3^r-3))=r-1 proves unboundedness and directly settles one of the two halves of a prominently stated open question in Motzkin arithmetic. It is more than a finite residue test or computed table, and the elementary generating-function/Kummer proof supplies a natural transparent mechanism. No complete valuation classification or 3-regularity claim is required for this self-contained sharp fact to have mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
