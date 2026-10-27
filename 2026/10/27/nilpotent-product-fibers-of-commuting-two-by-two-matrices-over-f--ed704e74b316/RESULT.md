# Nilpotent-product fibers of commuting two-by-two matrices over finite fields

## Finding

Let \(q\ge 2\) be any prime power, \(k=\mathbb F_q\), and \(R=M_2(k)\). For each \(C\in R\), write
\[
F(C)=\#\{(A,B)\in R\times R:AB=BA=C\}.
\]
For nilpotent \(C\), the complete fiber profile is
\[
F(C)=\begin{cases}
q^2(3q^2-2),&C=0,\\
2q(q-1),&C\ne0\text{ and }C^2=0.
\end{cases}
\]
There are exactly \(q^2-1\) nonzero nilpotent products. Consequently
\[
N_q:=\#\{(A,B):AB=BA,\ AB\text{ nilpotent}\}
=5q^4-2q^3-4q^2+2q.
\]
The number of all commuting ordered pairs is \(q^6+q^5-q^3\), so
\[
\Pr(AB\text{ nilpotent}\mid AB=BA)
=\frac{5q^3-2q^2-4q+2}{q^2(q^3+q^2-1)}.
\]
Its difference from the nilpotent-product probability \(2q^{-2}-q^{-4}\) for unrestricted pairs is exactly
\[
\frac{(q-1)^2(q+1)(3q^2-q-1)}{q^4(q^3+q^2-1)}>0.
\]
For fixed matrix dimension two and \(q\to\infty\), this conditional probability is asymptotic to \(5q^{-2}\), versus \(2q^{-2}\) without conditioning.

## Assumptions and scope

All pairs are ordered and sampled uniformly from the specified finite sets; no invertibility or trace restrictions are imposed on the factors. The field \(k\) may have arbitrary prime-power size or characteristic, including characteristic two. Every nilpotent \(2\times2\) matrix has square zero. A commuting pair determines a two-dimensional representation of \(k[u,v]\) by \(u\mapsto A\), \(v\mapsto B\); its product is nilpotent exactly when that representation factors through \(k[u,v]/((uv)^2)\). The smaller locus \(AB=BA=0\) corresponds to \(k[u,v]/(uv)\).

## Proof

**The zero product.** If \(A=0\), any of the \(q^4\) matrices \(B\) works. If \(A\) has rank one, then \(A\) is nonscalar and has two-dimensional polynomial centralizer \(k[I,A]\). Its Cayley–Hamilton identity is \(A^2=\operatorname{tr}(A)A\). Thus a commuting \(B=aI+bA\) satisfies \(AB=0\) exactly when \(a+b\operatorname{tr}(A)=0\), leaving \(q\) choices. The number of rank-one matrices is \((q-1)(q+1)^2\), because nonzero outer products of a column and row have \((q^2-1)^2/(q-1)\) distinct values. Finally, if \(A\) is invertible then \(B=0\) is forced. The number of invertible matrices is \((q^2-1)(q^2-q)\). Adding gives
\[
F(0)=q^4+q(q-1)(q+1)^2+(q^2-1)(q^2-q)=q^2(3q^2-2).
\]
This zero-product enumeration is included to make the profile self-contained; such mutually annihilating pairs have been studied previously.

**Each nonzero nilpotent product.** Every nonzero nilpotent \(2\times2\) matrix is similar to \(J=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)\), whose centralizer is \(k[I,J]\), the dual-number algebra. If \(AB=BA=J\), both factors commute with \(J\), so necessarily \(A=aI+bJ\) and \(B=cI+dJ\). The equation \(AB=J\) is precisely
\[
ac=0,\qquad ad+bc=1.
\]
For \(a\ne0\), these equations force \(c=0,d=a^{-1}\) while \(b\) is arbitrary: \(q(q-1)\) solutions. For \(c\ne0\), they force \(a=0,b=c^{-1}\) while \(d\) is arbitrary: another \(q(q-1)\) solutions. Neither \(a\) nor \(c\) can both vanish; the cases are disjoint and exhaustive. Consequently \(F(J)=2q(q-1)\), and simultaneous conjugacy makes \(F(C)\) identical for each nonzero nilpotent \(C\).

**Number of nilpotent products.** The centralizer of \(J\) in \(\mathrm{GL}_2(k)\) consists of \(aI+bJ\) with \(a\ne0\), of size \(q(q-1)\). The group has size \((q^2-1)(q^2-q)\), so its orbit of \(J\), which is exactly the set of nonzero nilpotent matrices, has size \(q^2-1\). The total is therefore
\[
F(0)+(q^2-1)F(J)=q^2(3q^2-2)+2q(q-1)(q^2-1)
=5q^4-2q^3-4q^2+2q.
\]

**Conditioning and comparison.** There are \(q\) scalar matrices, each centralizing all \(q^4\) matrices. Each of the other \(q^4-q\) matrices has a \(q^2\)-element centralizer by its degree-two minimal polynomial. Thus the number of commuting pairs is
\[
q\,q^4+(q^4-q)q^2=q^6+q^5-q^3.
\]
For unrestricted independent factors, split the first matrix by rank: \(q^4\) products arise from \(A=0\); each of the \((q-1)(q+1)^2\) rank-one matrices permits exactly \(q^3\) matrices \(B\) with \(AB\) nilpotent, because \(\operatorname{tr}(AB)=0\) is one nonzero linear condition; and each invertible \(A\) permits exactly \(q^2\) matrices \(B\), since there are \(q^2\) nilpotent \(2\times2\) matrices and multiplication by \(A\) is bijective. The total \(q^4+q^3(q-1)(q+1)^2+q^2(q^2-1)(q^2-q)=q^4(2q^2-1)\), divided by \(q^8\), gives \(2q^{-2}-q^{-4}\). Subtracting this from the conditional probability and factoring gives the displayed positive difference. Since \(q\ge2\), every factor in its numerator and denominator is positive. This proves the assertion.

## Verification

The standalone script `check.py` constructs all \(2\times2\) matrices, computes both products and individually counts fibers over all nilpotent matrices. It exhaustively checks \(q=2,3,5\) and the nonprime field \(\mathbb F_4\), using the irreducible polynomial \(X^2+X+1\). All four tests confirmed both fiber values, the number of nilpotent products, the total number of commuting pairs, and the conditional probability. This is a finite independent consistency check, not a substitute for the arbitrary-prime-power proof above.

## Relationship to prior work

Sarma and Subedi introduced nilpotent-product probability for finite rings and studied general bounds, commutative rings, and triangular subrings; their October 2026 paper motivates examining an interaction with the separate commuting condition. Huang previously enumerated mutually annihilating matrix pairs \(AB=BA=0\), identifying the module-counting significance of the nodal algebra \(k[u,v]/(uv)\); hence the zero fiber is not asserted to be novel. Feit–Fine and Fulman–Guralnick count all commuting matrix pairs, and Fulman–Guralnick also count commuting pairs in which both factors are nilpotent. These statements do not supply the nonzero nilpotent-product fibers of the first nodal thickening or the conditional formula without an additional calculation. The claimed contribution is exactly that nonzero-product stratum and its complete combination with known components.

## Limitations

The fiber classification is proved only for \(2\times2\) matrices, not arbitrary dimension; no generating function across dimensions, geometric smoothness statement, or independent external audit is claimed. Earlier results on centralizers, mutually annihilating matrices, and commuting varieties may permit the new formula as a short specialization even where the exact formula is not explicitly printed. This is the principal residual originality risk.

## References

1. D. Sarma and T. Subedi, *Nilpotent product probability of finite rings*, arXiv:2610.07892v1 (first posted 2026-10-06), https://arxiv.org/html/2610.07892v1.
2. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566, https://arxiv.org/html/2110.15566v3.
3. J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499, https://arxiv.org/abs/1611.05499.
