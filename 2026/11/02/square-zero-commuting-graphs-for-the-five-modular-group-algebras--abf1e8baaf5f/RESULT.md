# Square-zero commuting graphs for the five modular group algebras of order eight

## Finding

Let \(k=\mathbb F_q\) with \(q=2^f\), \(f\ge1\), and let \(R=kD_8\), where \(D_8=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle\). For conjugation by \(R^\times\), every noncentral square-zero element of \(R\) has orbit size \(q^2\). There are \(2(q-1)q^2\) such orbits and \(q^4\) central singleton orbits. This concerns individual elements of the group algebra, not conjugation by the original group \(D_8\) or a count by regular-multiplication rank.

## Square-zero loci and their commuting graphs (context)

For \(D_8\) and \(Q_8\), let \(z\) denote the central group involution and put \(t=1+z\). The ideal \(t kG\) has dimension four: multiply the four representatives of \(G/\langle z\rangle\cong C_2^2\) by \(t\) to obtain a basis. The quotient by this ideal is commutative, and \(t^2=0\); hence \(t kG\) is central and square-zero. Every algebra element is uniquely \(A+tB\), with \(A,B\) in the span of the representatives, and \((A+tB)^2=A^2\).

For \(D_8\), take representatives \(1,r,s,rs\). If \(A=a_0+a_1r+a_2s+a_3rs\) and \(S=a_0+a_1+a_2+a_3\), expansion gives
\[
 A^2=S^2+t(a_1^2+a_1a_2rs+a_1a_3s+a_2a_3r).
\]
Reducing first modulo \(tR\), then comparing the four independent coefficients inside \(tR\), gives \(S=0\), \(a_1=0\), \(a_2a_3=0\). This is the same square equation available from the coefficient formula in Creedon–Gildea [1, proof of Proposition 2.1], upon writing a normalized involutory unit as \(1+x\) with \(x^2=0\), including \(1\) for \(x=0\). The square-zero locus is
\[
 Z_{D_8}=\bigl(tR+k(1+s)\bigr)\cup\bigl(tR+k(1+rs)\bigr).
\]
Their intersection is \(tR\). Each family is commuting because the ideal is central and the added direction is one-dimensional. Across their complements the commutator is a nonzero scalar multiple of \([1+s,1+rs]=r^{-1}-r=tr\), so no cross-pair commutes. In particular the central square-zero elements are exactly \(tR\). The graph (with distinct commuting elements adjacent) is therefore two \(q^5\)-vertex cliques glued along a \(q^4\)-vertex clique. It has \((2q-1)q^4\) vertices, clique number \(q^5\), \((2q^2-1)q^8\) ordered commuting pairs including equal pairs, and \(2(q-1)^2q^8\) ordered noncommuting pairs. The complement induced on the noncentral vertices is \(K_{(q-1)q^4,(q-1)q^4}\).

For \(Q_8\), take representatives \(1,u,v,uv\) with \(u^2=v^2=(uv)^2=z\). Once the sum of coefficients vanishes, the four independent conditions are \(a_1^2+a_2^2+a_3^2=0\) and \(a_1a_2=a_1a_3=a_2a_3=0\). Thus the square-zero set is the central ideal \(t kQ_8\), as in [2], and the graph is \(K_{q^4}\). For the abelian groups \(C_8,C_4\times C_2,C_2^3\), use the truncated polynomial presentations with respective truncation exponents \((8),(4,2),(2,2,2)\). Squaring kills exactly the monomials whose doubled exponent reaches some truncation bound, and the other squared monomials are distinct. Thus the square-zero dimensions are respectively \(4,6,7\) and the graphs are complete of the corresponding sizes. These graph computations are elementary consequences of the coefficient and locus information, rather than separate novelty claims.

## Proof of the unit-orbit census

Central summands do not affect the adjoint map \(y\mapsto[x,y]\). For a noncentral square-zero \(x=c+a(1+s)\) with \(c\in tR\), \(a\ne0\), that map acts on the representatives \(1,r,s,rs\), up to the factor \(a\), with nonzero outputs \([s,r]=trs\) and \([s,rs]=tr\). For \(x=c+a(1+rs)\), its two nonzero outputs, up to \(a\), are \([rs,r]=ts\) and \([rs,s]=tr\). It vanishes on \(tR\) in both cases. Thus the adjoint rank is exactly two in either branch, and the algebra centralizer has dimension six.

A finite \(2\)-group algebra in characteristic two is local and its units are exactly the elements of nonzero augmentation. Here this also follows from the map to \(k[C_2^2]\): its kernel \(tR\) is square-zero, and in the abelian quotient squaring gives the augmentation squared, so every class of nonzero augmentation is invertible and lifts to a unit. Augmentation restricted to the centralizer is surjective since the centralizer contains \(1\). Consequently the unit centralizer has size \((q-1)q^5\), and \(|R^\times|=(q-1)q^7\). The orbit size is \(q^2\). There are \(2(q-1)q^4\) noncentral square-zero elements, so division by the common orbit size gives \(2(q-1)q^2\) noncentral orbits. All elements of \(tR\) have singleton orbits.

## Verification and scope

The supplied `verify.py` evaluates the square-zero predicate from explicit multiplication tables for the five groups over \(\mathbb F_2,\mathbb F_4\), checks ordered commuting-pair counts for \(D_8,Q_8\) over \(\mathbb F_2\), and exhausts the \(\mathbb F_2D_8\) square-zero conjugacy partition. For the latter check it expects 16 singletons and eight orbits of size four. The expected final marker is `ORDER8_GROUP_ALGEBRA_SQZERO_OK`. These finite tests supplement, but do not replace, the centralizer proof over arbitrary \(\mathbb F_{2^f}\). The structural loci and commuting families also make sense over infinite characteristic-two fields; the numerical orbit census is only asserted for finite fields. Nothing is asserted for larger groups or higher nilpotency indices.

## Relationship to prior work

The same-algebra unit group structure and relevant square coefficients occur in [1]. The quaternion collapse is specifically covered by [2]. A later-dated catalogue treatment of algebra retractions [3] uses the same dihedral and quaternion square-zero loci. The contribution retained here is the uniform orbit-size census on the dihedral square-zero locus: it needs the element-centralizer ranks in the full algebra. It is not a claim of novelty for the total square-zero counts or their immediate implications for commuting graphs. Historical priority of the orbit-size statement is assessed only against the sources inspected.

## References

1. L. Creedon and J. Gildea, *The Structure of the Unit Group of the Group Algebra \(\mathbb F_{2^k}D_8\)*, Canadian Mathematical Bulletin 54 (2011), 237–243, Proposition 2.1 and Theorem 2.6. https://doi.org/10.4153/CMB-2010-098-5
2. *Quaternionic square-zero collapse and rank spectra of odd-index dicyclic group algebras*, Resultary `930d5916e28e`, Finding and proof §2. https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-quaternionic-square-zero-collapse-and-rank-spectra-of-odd-index--930d5916e28e
3. *Algebra-retraction rank rigidity distinguishes the modular dihedral and quaternion group algebras of order eight*, Resultary `4bf856f96cbb`, Finding and Step 1. https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-algebra-retraction-rank-rigidity-distinguishes-the-modular-dihed--4bf856f96cbb
