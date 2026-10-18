# Nine-element nondegenerate Jordan Diophantine sets for two infinite congruence families

## Finding

Write \((a,b,d)=\begin{pmatrix}a&b\\0&d\end{pmatrix}\in U=UT_2(\mathbb Z)\), and set \(A\circ B=(AB+BA)/2\). A nondegenerate Jordan \(D(N)\)-set is a set of pairwise distinct nonzero matrices for which every distinct pair satisfies both \(A\circ B\neq0\) and \(A\circ B+N=K^2\) for some \(K\in U\). Let \(M(N)\) be its maximum cardinality.

**Theorem.** For each \(t\in\mathbb Z\setminus\{0\}\),
\[
M((1,6t,1))=M((1,10t,1))=M((4,12t,4))=M((4,20t,4))=9.
\]
Consequently, the upper alternative in Proposition 4.4 of Franušić and Pejković occurs for at least \(7/15\) of the admissible nonzero off-diagonal parameters in each of the two families addressed there (relative natural density, including negative parameters symmetrically).

## Assumptions and scope

All triples and square roots denote \(2\times2\) upper-triangular **integer** matrices. The Jordan product is computed over \(\mathbb Q\) but all pairwise products below have integer entries. Parameters \(t\) are nonzero integers, including negative values. No assertion is made for admissible parameters not divisible by the indicated numbers, or for nonsingular-only sets (our sets contain singular matrices).

## Proof

For \(Q=\{1,3,8,120\}\), \(b>0\), and an even integer \(r\), form the nine matrices
\[
\mathcal A_b=\{(a,2b,0):a\in Q\}\cup\{(0,2b,a):a\in Q\}\cup\{(0,2b,0)\}.
\]
They are pairwise distinct and nonzero. We give two explicit choices of \((b,r)\):
\[
(b,r)=(18,6),\qquad (b,r)=(10,10).
\]
For \(a<c\) in \(Q\), let \(h=\sqrt{ac+1}\). The six relevant pairs and the integer divisibility witnesses are:

| \((a,c)\) | \(h\) | \(u=18(a+c)+6\) | divisor \(h+\epsilon\) | \(u=10(a+c)+10\) | divisor \(h+\epsilon\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| \((1,3)\) | 2 | 78 | 3 | 50 | 1 |
| \((1,8)\) | 3 | 168 | 4 | 100 | 4 |
| \((1,120)\) | 11 | 2184 | 12 | 1220 | 10 |
| \((3,8)\) | 5 | 204 | 6 | 120 | 6 |
| \((3,120)\) | 19 | 2220 | 20 | 1240 | 20 |
| \((8,120)\) | 31 | 2310 | 30 | 1290 | 30 |

In each row \(\epsilon\in\{-1,1\}\) is uniquely specified by the displayed divisor; it divides the corresponding \(u\). In particular, \(ac+1=h^2\) for all six pairs. For two members \((a,2b,0)\) and \((c,2b,0)\), their Jordan product plus \(N=(1,r,1)\) equals \((h^2,u,1)\), which is exactly
\[
\left(h,\frac{u}{h+\epsilon},\epsilon\right)^2.
\]
For two members \((0,2b,a)\), \((0,2b,c)\), swap the diagonal coordinates of this square root. If the selected members lie in different four-element wings, their Jordan product plus \(N\) is
\[
(1,b(a+c)+r,1)=\left(1,\frac{b(a+c)+r}{2},1\right)^2;
\]
if one member is the central matrix \((0,2b,0)\), it is
\[
(1,ba+r,1)=\left(1,\frac{ba+r}{2},1\right)^2.
\]
All off-diagonal square-root entries are integers because both \(b\) and \(r\) are even. Hence all \(\binom92=36\) pairs have the required integral squares. For every pair, the nonzero Jordan product is immediate: within a wing one diagonal product is positive, and across wings or involving the center the upper-right coordinate is respectively \(b(a+c)>0\) or \(ba>0\).

For any nonzero integer \(t\), the map \((a,b,d)\mapsto(a,tb,d)\) is injective and preserves Jordan products and squares, and it sends \((1,r,1)\) to \((1,tr,1)\). The map \((a,b,d)\mapsto(2a,tb,2d)\) similarly preserves the requisite identities up to diagonal factor four and off-diagonal factor \(2t\), sending \((1,r,1)\) to \((4,2tr,4)\). Both preserve nonzero Jordan products. They therefore give nine-element nondegenerate sets for the four families in the theorem. The **upper bound nine** for all these parameters is Theorem 4.2 of Franušić and Pejković [1], completing the equalities.

Finally, among nonzero even integers \(r=2k\), membership in \(6\mathbb Z\cup10\mathbb Z\) is equivalent to \(3\mid k\) or \(5\mid k\), a union of density \(1/3+1/5-1/15=7/15\). Likewise for nonzero \(r=4k\) and \(12\mathbb Z\cup20\mathbb Z\).

## Verification

Run `python3 artifacts/verify.py` using the files embedded with this report. The verifier computes all \(36\) products for both seed choices with exact integer arithmetic, constructs an integral square root for each, checks pairwise distinctness and nonzero Jordan products, tests positive and negative scalar lifts, and independently prints the six divisibility witnesses in the table. The code checks 1080 pair identities across 30 instantiated sets. The infinite scope follows from the symbolic formulas and the published upper bound, not from finite tests.

## Relationship to prior work

Franušić and Pejković [1, Theorem 4.2] prove an upper bound of nine; [1, Proposition 4.4] establishes eight examples for nonzero even \(r\) in \((1,r,1)\), and for nonzero \(r\) divisible by four in \((4,r,4)\), explicitly leaving the eight-or-nine decision open for each parameter. The nine-tuple for \(N=I\) in [1, Proposition 4.3] already uses the diagonal quadruple \(Q\); that diagonal quadruple and the \(N=I\) construction are not claimed as new here. The present integral divisibility choices \((b,r)=(18,6),(10,10)\) give nine with **nonzero** upper-right coordinate of \(N\), and scaling produces infinite positive-density subfamilies of the open cases. Dujella and Franušić [2] introduced the setting and studied quadruples rather than these specific extremal nine-tuples. A manuscript by Wildner [3], cited in [1] for infinite-set constructions, is a residual source-coverage risk; no equivalence of its stated infinite families to these fixed-diagonal nondegenerate finite cases is established here.

## Limitations

The maximal cardinalities for the remaining admissible parameter classes, notably those with \(r/2\) or \(r/4\) coprime to \(15\), are not determined. These constructions are singular and do not address nonsingular-only maximal sizes. The external literature comparison cannot rule out an unindexed identical construction. The named source [1] supplies the upper bound, so the proof is not independent of that published theorem. No independent mathematical audit has been performed.

## References

[1] Z. Franušić and T. Pejković, *Cardinalities of Jordan Diophantine sets of upper triangular integer matrices*, arXiv:2610.10773v1, public October 7, 2026. https://arxiv.org/html/2610.10773v1 (especially Theorem 4.2, Propositions 4.3–4.4).

[2] A. Dujella and Z. Franušić, *\(D(N)\)-quadruples in upper-triangular \(2\times2\) integer matrices*, arXiv:2608.29968v1, August 30, 2026. https://arxiv.org/abs/2608.29968

[3] N. Wildner, *Jordan Diophantine tuples in \(2\times2\) integer matrix rings*, author manuscript (August 30, 2026), referenced in [1, bibliography item 9].
