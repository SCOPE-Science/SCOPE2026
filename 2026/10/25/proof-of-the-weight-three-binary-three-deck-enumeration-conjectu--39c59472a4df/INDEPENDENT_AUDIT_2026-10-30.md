# Independent mathematical audit

## correctness

PASS

Represent n-length binary words of weight three by four nonnegative zero gaps x0..x3 with sum N=n-3. All eight length-three scattered subsequence multiplicities are determined by N, A=T011=3x0+x1, B=T110=x2+3x3, and F=T001=sum_i binom(p_i,2) with prefix-zero counts p1=x0,p2=x0+x1,p3=x0+x1+x2. Equal N,A,B implies xprime=x+t(1,-3,3,-1). The exact F difference is t(x2-x1+3t), so distinct equal-deck partners have unique t=(x1-x2)/3 nonzero and the unique gap involution. Orient t>=1 and write the pair as (r,s+3t,s,t+u) and (r+t,s,s+3t,u), r,s,u>=0. Every nonsingleton class is therefore a pair, with generating function z^7/[(1-z)^2(1-z^2)(1-z^4)]. Subtraction from binom(n,3) yields the published-conjectured generating function for D_3,3(n); exact pole order gives 3/4 limiting uniquely-decked proportion and 7n^3/48 distinct decks. Independently grouped every binary three-one word of lengths 3..16 from direct scattered-triple counts and verified all pair involutions/counts; finite checks supplement the all-length algebra.

## originality

PASS

The exact rational generating function was explicitly CONJECTURED by Chrisnata, Kiah, Karingula, Vardy, Yaakobi and Yao in 2021 (journal 2023), after checking 20 coefficients, and is therefore not new as a proposal. Their Section 5.3 derived the same zero-gap nullspace and a comparison lemma, but explicitly left D_3,3(n) unknown. The audited original increment is the complete proof for every n and exact two-element fibre involution. Targeted searches did not find an intervening proof, with unindexed/alternate-language priority risk preserved. A 2026 paper on unrestricted k-deck degrees of freedom is broader in a different direction and its accessible abstract alone cannot establish noncoverage, so it is listed as residual risk.

## value

PASS

An all-length proof of a published exact enumeration conjecture and full classification of its ambiguity fibres is a substantive, naturally motivated reconstruction problem, not a recomputation of known finite coefficients. The strict at-most-two ambiguity and limiting 3/4 unique reconstruction fraction are new structural consequences, while the previously conjectured generating function is credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
