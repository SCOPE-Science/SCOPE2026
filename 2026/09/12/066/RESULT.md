# Certified extremal witnesses for the Harborth and two-fold Harborth problems on C_9^2

## Context
Let G = C_9 x C_9, exp(G) = 9. A squarefree sequence is a set (distinct elements).
A 9-sum is a 9-element subset summing to (0,0). The Harborth constant g(G) is
the smallest l such that every l-subset of G contains a 9-sum; the two-fold
constant g^2(G) is the smallest l such that every l-subset contains two
disjoint 9-sums. Kemnitz's elementary bound (n-1)2^{d-1}+1 <= g(C_n^d) gives
g(C_9^2) >= 17 as a bare number; Reiher/Gao prime-square theorems do not apply
to the composite group C_9^2, and no prior work treats two disjoint 9-sums in
C_9^2. This record certifies the first explicit extension-maximal extremal
witnesses S16 (one-fold) and S20 (two-fold) for this group.

## Definitions
- G = {(x,y) : x,y in Z/9Z}, |G| = 81.
- S16 = {(0,1),(0,2),(1,0),(1,1),(2,7),(3,4),(3,5),(4,2),(4,3),(5,0),(5,8),(6,7),(6,8),(7,5),(8,3),(8,4)}, |S16| = 16.
- S20 = S16 union {(0,3),(5,1),(6,5),(7,2)}, |S20| = 20.
- Extension-maximal (chain-maximal): every one-point extension S union {g},
  g in G \ S, breaks freeness; this is maximality along chains, not a claim
  of global cardinality optimality.

## Result
(A) S16 contains no 9-term zero-sum (count 0 over all C(16,9)=11440 subsets),
and each of its 65 one-point extensions contains a 9-sum; hence any future
exact value satisfies the witness form g(C_9^2) >= 17 with explicit maximal
example. The bare number 17 is also the Kemnitz elementary value and novelty
is not claimed for the number alone.
(B) S20 contains exactly 1832 nine-term zero-sums, no two of which are
disjoint, and each of its 61 one-point extensions contains two disjoint
9-sums; hence g^2(C_9^2) >= 21, materially above the trivial bound 18.
The 1832 zero-sums form a pairwise-intersecting family, a structural fact of
independent combinatorial interest.
(C) General lemma: for any finite abelian group H, g^2(H) <= g(H) + exp(H),
by two-step deletion: from |S| = g(H)+exp(H) extract a first exp(H)-sum,
leaving g(H) points which contain a second. For C_9^2 this frames the exact
problem as 21 <= g^2(C_9^2) <= g(C_9^2)+9.

## Proof / evidence
Deterministic stdlib-only certificate output/artifacts/certify.py, reproduced
by the auditor: T1 enumerates all C(16,9) subsets of S16, 0 zero-sums;
T2 checks all 65 extensions, each contains a 9-sum; T3 enumerates all
C(20,9)=167960 subsets of S20, exactly 1832 zero-sums, pairwise-intersection
test confirms no two disjoint; T4 checks all 61 extensions for two disjoint
9-sums. T4 is sound because T3 certifies that all pre-existing zero-sums of
S20 pairwise intersect, so any disjoint pair in S20 union {g} must use a new
zero-sum through g; the script exhaustively enumerates all 8-subsets of S20
summing to -g and tests disjointness against old masks. Lemma C is proved
analytically. Verification log: T1=0, T2=0 bad, T3=1832 disjoint=False,
T4=0 bad.

## Limitations
One-sided bounds only: exact values of g(C_9^2) and g^2(C_9^2) are not
established; global optimality of S16/S20 is not proved (annealing hints of
tightness are heuristic and excluded). No result for p>=5, no all-p formula,
no automorphism classification, no Chevalley-Warning certificate. Enumeration
covers only the listed sets and their one-point extensions.

## Reproducibility
Run `python3 output/artifacts/certify.py` (no dependencies, deterministic);
compare with output/artifacts/verification.log. Do not modify S16/S20
coordinates when reusing the certificate.

## References
- Kemnitz, On a lattice point problem, Ars Combin. 16B (1983); Thesis (1982).
- Harborth, Ein Extremalproblem fuer Gitterpunkte, J. Reine Angew. Math. 1973.
- Reiher, Kemnitz conjecture proof; Gao-Thangadurai, variant of Kemnitz (2004).
- Marchan-Ordaz-Ramos-Schmid, Harborth constants, Arch. Math. 101 (2013).
- Guillot et al., Harborth constant of C3+C3p, JTNB 31 (2020): g(C3+C9)=13.
- Lemos-Moriya-Moura-Silva, A Variant of Harborth Constant, arXiv:2209.14784
  (k-term g^k over Cp/Cn/C2^r; different predicate from disjoint-pair g^2).
