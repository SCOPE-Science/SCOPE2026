# Exact finite-field census of perfect idempotent-free binary commutative algebras

## Finding
Let \(q\) be any odd prime power and let \(V=\mathbb F_q^2\) with an ordered basis. Consider all symmetric bilinear multiplications \(m:V\times V\to V\), without an associativity requirement, such that \(V^2=V\) (equivalently, the linear map \(\operatorname{Sym}^2V\to V\) has rank two). Exactly
\[
N_q=\frac{q^2(q-1)(q^3-q)}3+\frac{q(q^2-1)(q^2-q)}2+(q-1)(q^2-1)
\]
of these labeled perfect commutative algebras have no nonzero idempotent \(x^2=x\). The three summands count, respectively, (I) algebras with an irreducible cubic projective eigenline equation; (II) algebras whose eigenline cubic has one rational simple factor and an irreducible quadratic, with its unique rational eigenline square-zero; and (III) algebras with a triple rational eigenline, also square-zero. There are \((q^3-1)(q^3-q)\) labeled perfect commutative algebras altogether; consequently their idempotent-free proportion tends to \(1/3\) as \(q\to\infty\) through odd prime powers. At \(q=3,5\), the respective exact counts are \(232\) and \(5296\).

These counts refer to structures on one *fixed ordered vector-space basis*, not to isomorphism classes. The three strata are intrinsic: the factorization type of the projective eigenline cubic is invariant under change of basis.

## Assumptions and scope
The base field is the finite field \(F=\mathbb F_q\), \(q\) odd. A commutative algebra here is a vector space with a bilinear symmetric operation; it need not be associative, unital, power-associative, or an evolution algebra. For any multiplication \(m\), define \(Q_m(x)=m(x,x)\), and call \(m\) *perfect* when the span of all products is \(V\). A nonzero \(x\) with \(x^2=x\) is an idempotent. The count ranges over all six-tuples \((a,b,c,d,e,f)\in F^6\) defining
\[
e_1^2=ae_1+be_2,\qquad e_1e_2=ce_1+de_2,\qquad e_2^2=ee_1+fe_2.
\]
Do not conflate lack of \(F\)-rational idempotents with lack of idempotents after extending scalars to an algebraic closure.

## Proof
**1. Eigenline cubic and fiber size.** For \(x=se_1+te_2\), consider the homogeneous cubic
\[
D_m(s,t)=\det\bigl(x,Q_m(x)\bigr)
=b s^3+(2d-a)s^2t+(f-2c)st^2-e t^3.
\]
The linear map \(m\mapsto D_m\) from the six-dimensional space of symmetric bilinear multiplications onto the four-dimensional space of binary cubics is surjective. Its kernel consists exactly of the multiplications with \(Q_m(x)=\ell(x)x\), \(\ell\in V^*\); polarization gives \(m(x,y)=[\ell(x)y+\ell(y)x]/2\). Thus every cubic \(D\) has exactly \(q^2\) preimages. When \(D\equiv0\), all products are radial; if \(\ell\ne0\), then \(x/\ell(x)\) is a nonzero idempotent whenever \(\ell(x)\ne0\), while \(\ell=0\) gives zero multiplication, which is not perfect. Hence the zero cubic contributes nothing.

**2. Rational roots and square-zero directions.** Let \(D_m\ne0\). A rational projective zero \([u]\in\mathbb P^1(F)\) of \(D_m\) satisfies \(Q_m(u)=\lambda u\). If \(\lambda\ne0\), \(u/\lambda\) is a nonzero idempotent, and conversely every nonzero idempotent yields such a root. Consequently an idempotent-free multiplication has \(Q_m(u)=0\) at *every* rational projective root. A perfect binary commutative multiplication cannot have two independent square-zero vectors: their basis squares vanish, and all products then lie in the one-dimensional span of their mutual product. Thus a perfect idempotent-free algebra with nonzero cubic has at most one rational projective root.

**3. The irreducible-cubic stratum.** A nonzero binary cubic with no rational projective root is irreducible over \(F\). There are \((q^3-q)/3\) monic irreducible cubics over \(F\); each has nonzero highest coefficient in its homogenization, so rescaling gives \((q-1)(q^3-q)/3\) such binary cubics. All \(q^2\) multiplications over each are perfect: were the image of multiplication at most one-dimensional, one would have \(Q_m(x)=h(x)w\) for a quadratic scalar form \(h\) and a fixed vector \(w\), forcing the factorization \(D_m(x)=h(x)\det(x,w)\) with a rational linear factor. None of these algebras has a nonzero idempotent. Their count is the first summand.

**4. The unique-rational-root strata.** A nonzero binary cubic with exactly one distinct rational projective root has one of exactly two factorization types: (II) a rational linear factor times an irreducible homogeneous quadratic, or (III) a cube of a rational linear factor. The numbers of such cubics are
\[
B_q=(q+1)(q-1)\frac{q^2-q}{2},\qquad C_q=(q+1)(q-1).
\]
Indeed there are \(q+1\) rational projective lines, \((q^2-q)/2\) monic irreducible quadratics, and \(q-1\) possible overall nonzero scalars. Both factorizations have unique forms in the indicated normalization.

Fix one such cubic \(D\), and choose \(0\ne u\in V\) on its sole rational projective root. Every lift \(m\) satisfies \(Q_m(u)=\lambda_m u\). Changing \(m\) by a radial multiplication associated with \(\ell\in V^*\) changes \(\lambda_m\) by \(\ell(u)\). Since evaluation \(V^*\to F\), \(\ell\mapsto\ell(u)\), is onto, exactly \(q\) of the \(q^2\) lifts satisfy \(Q_m(u)=0\), and exactly those lifts have no rational nonzero idempotent.

In type (II) every such lift is perfect. If a lift had rank one, writing \(Q_m(x)=h(x)w\) would force the rational root \([w]\) to coincide with \([u]\), and the quadratic factor \(h\) to be irreducible. Then \(h(u)\ne0\), contradicting \(Q_m(u)=0\). This gives \(q B_q\) algebras. In type (III) exactly one of the \(q\) lifts with \(Q_m(u)=0\) has rank one: fix \(u\), let \(r(x)=\det(x,u)\), and write \(D=\kappa r^3\); the unique rank-one lift is \(Q_m(x)=\kappa r(x)^2u\). Every other such lift is perfect, giving \((q-1)C_q\) algebras. Adding the three disjoint contributions proves the formula.

**5. Denominator and asymptotic.** The multiplication rank is that of a linear map from a three-dimensional space to a two-dimensional one. Counting surjective \(2\)-by-\(3\) matrices gives \((q^3-1)(q^3-q)\) perfect structures. The first numerator summand has leading term \(q^6/3\), while the other two have degree at most five. Therefore \(N_q/[(q^3-1)(q^3-q)]\to1/3\).

## Verification
Run `python3 verify.py` from the directory containing this report and the standalone verifier. It exhaustively lists the \(3^6\) and \(5^6\) symmetric binary structure tables, retains rank-two tables, searches every rational projective line for nonzero idempotents, computes the eigenline cubic, and independently verifies all three predicted counts. For \(q=3\), the three contributions are \(144,72,16\), summing to \(232\) among \(624\) perfect tables. For \(q=5\), they are \(4000,1200,96\), summing to \(5296\) among \(14880\). All checks returned `VERIFY_OK`. These finite tests are consistency checks, not the proof for general prime powers.

## Relationship to prior work
Hu and Wen (2026) investigate idempotent-free nonsolvable evolution algebras and the behavior of their stable derived subalgebras, motivating quantitative study of small commutative algebras without idempotents. Ahmed, Bekbaev, and Rakhimov (2019/2020, Proposition 4.1) explicitly describe the idempotents of a given two-dimensional algebra via rational roots of a cubic, but do not enumerate *all rank-two symmetric multiplication tables over every odd finite field* and their three factorization strata. Kaygorodov and Volkov (2018/2019, Theorem 3.3) classify two-dimensional algebras over algebraically closed fields, not the finite-field labeled census or the rational Frobenius-stratified distribution. Petersson and Scherer (2004) count *isomorphism classes* of general two-dimensional algebras over finite fields, a different enumerand. Verhulst (2020) gives general orbit-counting methods for finite-dimensional algebras, including an example over \(\mathbb F_2\), not this idempotent-free rank-two count. The new contribution is the closed all-odd-\(q\) labeled census and its three constructive geometric strata; the projective cubic itself and earlier classifications are not claimed as new.

## Limitations
The result is limited to commutative two-dimensional algebras and odd characteristic. It does not count isomorphism types, higher dimensions, characteristic two, or algebras without idempotents over an algebraic closure. Its literature comparison does not establish that no equivalent count exists in unpublished or unindexed work. No independent validation has been performed.

## References
1. X.-Y. Hu and R. Wen, *Idempotent-Free Non-Solvable Evolution Algebras over C* (2026), first posted September 1, 2026: https://www.preprints.org/manuscript/202609.0078 ; arXiv:2609.25023.
2. H. Ahmed, U. Bekbaev, and I. Rakhimov, *Subalgebras, Idempotents, Ideals and Quasi-Units of Two-Dimensional Algebras*, arXiv:1810.06780, Proposition 4.1 (2019; journal 2020).
3. I. Kaygorodov and Y. Volkov, *The Variety of Two-Dimensional Algebras over an Algebraically Closed Field*, Canadian Journal of Mathematics (2019), Theorem 3.3; https://doi.org/10.4153/S0008414X18000056.
4. H. P. Petersson and M. Scherer, *The Number of Nonisomorphic Two-Dimensional Algebras over a Finite Field*, Results in Mathematics (2004), https://doi.org/10.1007/BF03323003.
5. N. D. Verhulst, *Counting Finite-Dimensional Algebras Over Finite Field*, Results in Mathematics (2020), https://doi.org/10.1007/s00025-020-01281-6.
6. C. Costoya, A. Fernández Ouaridi, and A. Viruel, *Commutative algebras are ideals of evolution algebras*, arXiv:2609.32784 (2026).
