# Quadratic-factor decomposition removes two spurious complex additions from a three-dimensional associative-algebra list
## Finding
Let \(k\) be a field of characteristic different from \(2\). Consider the algebra \(A_t\) with basis \(e_1,e_2,e_3\) and products
\[
e_1e_i=e_ie_1=e_i,\qquad e_2^2=e_1,\qquad e_2e_3=e_3e_2=e_3,\qquad e_3^2=t(e_1+e_2)+e_3.
\]
This is exactly the family denoted \(As_{1,1}^{8}(3)(t)\) in arXiv:2508.04104v6. Define
\[
p=\frac{e_1+e_2}{2},\qquad q=\frac{e_1-e_2}{2}.
\]
Then
\[
A_t\cong k\times k[z]/(z^2-z-2t)\cong k\times k[w]/(w^2-(1+8t)).
\]
Thus the family is controlled completely by the quadratic factor with discriminant \(1+8t\).

Over an algebraically closed field there are exactly two types. If \(1+8t\ne0\), then \(A_t\cong k^3\). If \(1+8t=0\), then \(A_t\cong k\times k[\varepsilon]/(\varepsilon^2)\). In the notation for the 2021 complex classification reproduced in arXiv:2508.04104v6, these are \(U_2^3\) and \(U_3^3\), respectively. Therefore the two members \(As_{1,1}^{8}(3)(0)\) and \(As_{1,1}^{8}(3)(-1/8)\), which the recent paper lists among complex unital algebras to be added to that classification, are not new classes: they duplicate \(U_2^3\) and \(U_3^3\).

For every finite field \(\mathbb F_q\) of odd characteristic, the family has exactly three isomorphism types, according as \(1+8t\) is a nonzero square, zero, or a nonsquare:
\[
\mathbb F_q^3,\qquad \mathbb F_q\times\mathbb F_q[\varepsilon]/(\varepsilon^2),\qquad \mathbb F_q\times\mathbb F_{q^2}.
\]
Their automorphism-group orders are \(6\), \(q-1\), and \(2\), respectively.

## Assumptions and scope
The decomposition only requires \(2\) to be invertible. The motivating classification assumes characteristic different from \(2\) and \(3\); the algebraic calculation above remains valid in characteristic \(3\) as well. The literature correction asserted here concerns the complex comparison in the current version of arXiv:2508.04104, not the entirety of that paper's arbitrary-field classification.

## Proof
From the displayed structure matrix in arXiv:2508.04104v6 and its stated ordering of structure constants, the multiplication is exactly the one written above. Direct calculation gives
\[
p^2=p,\quad q^2=q,\quad pq=0,\quad pe_3=e_3,\quad qe_3=0.
\]
Hence \(kq\) is a one-dimensional ideal and \(pA_t\) is a two-dimensional ideal with identity \(p\). Inside \(pA_t\), the generator \(e_3\) satisfies
\[
e_3^2-e_3-2tp=0.
\]
Since \(p,e_3\) are a basis of \(pA_t\), this gives
\[
pA_t\cong k[z]/(z^2-z-2t),
\]
and therefore the first product decomposition. Setting \(w=2z-1\) gives \(w^2=1+8t\), yielding the second form.

For \(t=0\), the three elements
\[
q,\qquad e_3,\qquad p-e_3
\]
are pairwise orthogonal idempotents summing to \(e_1\). They therefore identify \(A_0\) with \(k^3\), which is the multiplication table denoted \(U_2^3\) in the reproduced 2021 list.

For \(t=-1/8\), put
\[
\varepsilon=e_3-\frac12p.
\]
Then \(\varepsilon^2=0\), \(p\varepsilon=\varepsilon\), and \(q\) annihilates both \(p\) and \(\varepsilon\). Thus the basis \(q,p,\varepsilon\) has precisely the multiplication table of \(k\times k[\varepsilon]/(\varepsilon^2)\), reproduced there as \(U_3^3\).

Over \(\mathbb F_q\) with \(q\) odd, the map \(t\mapsto1+8t\) is a bijection. A nonzero square gives a split quadratic factor \(\mathbb F_q\times\mathbb F_q\); zero gives the dual numbers; and a nonsquare gives the unique quadratic field \(\mathbb F_{q^2}\). These three algebras are distinguished respectively by being reduced split, nonreduced, and containing a degree-two field factor. Their automorphisms preserve the direct-product factors except in the completely split case. Hence the automorphism groups are \(S_3\), \(\mathbb F_q^\times\) acting by scaling \(\varepsilon\), and \(\operatorname{Gal}(\mathbb F_{q^2}/\mathbb F_q)\), with orders \(6\), \(q-1\), and \(2\).

## Verification
The included `artifacts/verify.py` checks the idempotent decomposition over exact rational arithmetic, verifies explicitly that the two exceptional complex representatives have the \(U_2^3\) and \(U_3^3\) multiplication tables, and exhaustively enumerates all algebra automorphisms for every parameter \(t\in\mathbb F_5\). The resulting automorphism counts are \(6,6,2,4,2\) for \(t=0,1,2,3,4\), matching the three predicted discriminant types; the script ends with `CHECK_OK`.

The finite-field enumeration is a regression check, not the proof for arbitrary \(q\). The general statements follow from the displayed direct-product decomposition and the elementary classification of quadratic \(\mathbb F_q\)-algebras.

## Relationship to prior work
Bekbaev and Rakhimov give the family \(As_{1,1}^{8}(3)(t)\), an isomorphism condition on its parameter, and correctly observe that over \(\mathbb C\) it yields two mutually non-isomorphic members. Their conclusion nevertheless places both \(As_{1,1}^{8}(3)(0)\) and \(As_{1,1}^{8}(3)(-1/8)\) among the unital algebras to be added to the 2021 complex classification. The same paper reproduces the older tables \(U_2^3\) and \(U_3^3\). The explicit bases above show that the two proposed additions are exactly those two older classes.

The 2021 Kobayashi--Shirayanagi--Tsukada--Takahasi paper is the classification being compared against. Its full article text was not available from the lawful sources inspected here; however, the recent paper reproduces the relevant \(U_2^3\) and \(U_3^3\) multiplication tables explicitly, so the two isomorphisms do not depend on an unseen statement from the older article. Fialowski--Penkava independently give a complete complex three-dimensional associative-algebra classification in a different notation; its existence reinforces that any claimed extra complex class must be checked for duplication, but no identification from that paper is used in the proof.

## Limitations
This result isolates one parametric family and one concrete redundancy in the recent complex comparison. It does not re-audit the remaining families in arXiv:2508.04104v6, nor does it claim that the paper's other listed additions are duplicates. The arbitrary-field square-class description assumes characteristic different from \(2\); no characteristic-two analogue is asserted.

## References
1. U. Bekbaev and I. Rakhimov, *On three-dimensional associative algebras*, arXiv:2508.04104v6, first posted 2025-08-06. Primary MSC 16H99.
2. Y. Kobayashi, K. Shirayanagi, M. Tsukada, and S.-E. Takahasi, *A complete classification of three-dimensional algebras over R and C — visiting old, learn new*, Asian-European Journal of Mathematics 14 (2021), 2150131, DOI:10.1142/S179355712150131X.
3. A. Fialowski and M. Penkava, *The Moduli Space of 3-Dimensional Associative Algebras*, arXiv:0807.3178; Communications in Algebra 37 (2009), 3666–3685.
