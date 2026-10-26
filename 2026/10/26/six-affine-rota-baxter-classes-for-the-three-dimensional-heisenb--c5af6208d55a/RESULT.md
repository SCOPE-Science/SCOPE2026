# Six affine Rota–Baxter classes for the three-dimensional Heisenberg Lie affgebra

## Finding

Let \(K\) be any field of characteristic different from \(2\), and let \(\mathfrak h=KX\oplus KY\oplus KZ\) be the Heisenberg Lie algebra with \([X,Y]=Z\) and central \(Z\). Equip its underlying affine space with the **canonical Lie affgebra** bracket \(\{u,v\}=[u,v]+v\). Define affine Rota–Baxter operators in the weight-minus-one convention by
\[
P(\{P(u),v\}-\{u,v\}+\{u,P(v)\})=\{P(u),P(v)\}
\quad(u,v\in\mathfrak h).
\]
Two operators are equivalent if conjugate by an automorphism of this canonical Lie affgebra.

**Theorem.** There are exactly **six** equivalence classes, with the following representatives. Write \(u=xX+yY+zZ\):

| Rank of the linear part | Operator \(P(u)\) | Number of classes |
| --- | --- | --- |
| \(0\) | \(0\), or \(X\) (constant maps) | \(2\) |
| \(1\) | \(xX\) | \(1\) |
| \(2\) | \(xX+zZ\), or \(xX+zZ+Y\) | \(2\) |
| \(3\) | \(u\) | \(1\) |

Over each finite field \(K=\mathbb F_q\) of odd cardinality, these six classes have respective sizes
\[
q,\quad q^3-q,\quad q^3(q+1),\quad q^2(q+1),\quad q^2(q^2-1),\quad 1,
\]
where the order is the two rank-zero classes, rank one, the two rank-two classes, and rank three. In particular the exact number of affine Rota–Baxter operators on this canonical Lie affgebra is
\[
\boxed{q^3(2q+3)+1}.
\]
The orbit result and the count hold for **all odd prime powers**, not just prime fields. They refer to affine Lie affgebra automorphisms, not arbitrary affine maps or ordinary weight-one Rota–Baxter operators on the Lie algebra.

## Assumptions and scope

The affine space is the underlying set of the Lie algebra, its heap expression uses \(a-b+c\), and its bracket is fixed as \(\{u,v\}=[u,v]+v\). The weight-minus-one descendant is the displayed three-term affine expression; replacing it by another Rota–Baxter convention changes the problem. The field may be finite or infinite, need not be algebraically closed, and has characteristic distinct from two. The rank refers to the tangent linear part \(R\) of \(P(u)=R(u)+p\). Equivalence is precisely conjugacy under bijections \(\varphi(u)=\psi(u)+t\) preserving the canonical affgebra bracket.

## Proof

**1. Direct characterization of the operator identity.** Substitute \(P(u)=R(u)+p\) and \(\{u,v\}=[u,v]+v\) in the defining identity. Expanding its two sides yields
\[
R([Ru,v]+[u,Rv]-[u,v]+[p,v]+[u,p])+R^2v+Rp+p
=[Ru,Rv]+[p,Rv]+[Ru,p]+Rv+p.
\]
The constant term gives \(Rp=0\). Comparing terms linear only in \(u\) gives \(R[u,p]=[Ru,p]\). Using this identity in the coefficient linear only in \(v\) forces \(R^2=R\). The remaining bilinear part is
\[
R([Ru,v]+[u,Rv]-[u,v])=[Ru,Rv].
\]
For a projection \(R\), this last condition is equivalent to its image \(A=\operatorname{im}R\) and kernel \(B=\ker R\) being Lie subalgebras: on writing \(u=a+b\) and \(v=c+d\) with \(a,c\in A\), \(b,d\in B\), its argument is \([a,c]-[b,d]\). Finally the condition \(R[u,p]=[Ru,p]\), combined with \(p\in B\) and \([B,B]\subseteq B\), is equivalent to \([p,A]\subseteq A\). Thus **exactly** the admissible triples are
\[
\mathfrak h=A\oplus B,\qquad [A,A]\subseteq A,\quad[B,B]\subseteq B,\quad p\in B,\quad[p,A]\subseteq A,
\]
with \(P(a+b)=a+p\). This derivation is valid in all stated characteristics and independently establishes the necessary algebraic premise.

**2. Subalgebra and automorphism geometry.** Every line of \(\mathfrak h\) is a Lie subalgebra. A two-dimensional subspace is a Lie subalgebra **exactly** when it contains \(KZ\). Indeed, a plane missing \(KZ\) projects isomorphically onto the two-dimensional abelian quotient \(\mathfrak h/KZ\), so the bracket of two lifts of a quotient basis is a nonzero multiple of \(Z\), violating closure. Conversely, a plane containing \(Z\) is closed because all brackets lie in \(KZ\).

Every Lie automorphism is determined by an arbitrary \(M\in\operatorname{GL}_2(K)\) on \(\mathfrak h/KZ\) and two arbitrary central shears; the induced action on \(Z\) is multiplication by \(\det M\). A direct comparison of the affine brackets shows that **all** canonical Lie affgebra automorphisms are
\[
\varphi(u)=\psi(u)+tZ,\qquad \psi\in\operatorname{Aut}_{\rm Lie}(\mathfrak h),\quad t\in K.
\]
Their conjugation action on \(P=R+p\) is
\[
R'=\psi R\psi^{-1},\qquad p'=\psi(p)+(I-R')(tZ).
\]
In ranks one and two, a decomposition has one plane containing \(Z\) and one line outside it. Any two such ordered decompositions are conjugate by a Lie automorphism: choose generators of the line and the noncentral direction in the plane, and extend the resulting basis map using their nonzero bracket. Hence for each of the two ranks the image/kernel pair has just one orbit.

**3. Translation orbits.** For rank zero, \(P\) is constant. The affine automorphism group is transitive on central values (central translations remove them), and separately transitive on noncentral values (the quotient \(\operatorname{GL}_2(K)\) action is transitive on nonzero vectors and central translation removes the last component). Center/noncenter is invariant, so there are two classes represented by \(0\) and \(X\). Rank three gives only the identity.

For rank one, take \(A=KX\), \(B=KY\oplus KZ\). If \(p=bY+cZ\), then \([p,X]=-bZ\) lies in \(A\) exactly when \(b=0\). The remaining \(cZ\) is removed by a central translation since \(RZ=0\). There is one class, represented by \(P(u)=xX\).

For rank two, take \(A=KX\oplus KZ\), \(B=KY\). Every \(p=bY\) satisfies \([p,A]\subseteq KZ\subseteq A\). All nonzero coefficients \(b\) are conjugate because the stabilizer of the ordered subalgebras can rescale \(Y\) arbitrarily. They cannot be conjugate to \(b=0\): central translations are annihilated by \(I-R\), since \(Z\in A\), and a Lie automorphism cannot carry a nonzero vector to zero. Thus there are exactly two rank-two classes. Rank invariance proves that the six classes listed are mutually inequivalent.

**4. Exact finite-field orbit sizes.** For odd \(q\), the projective space of lines in \(\mathbb F_q^3\) has \(q^2+q+1\) members. There are \(q+1\) planes through \(KZ\), each with exactly \(q^2\) lines outside it. Hence there are exactly \(q^2(q+1)\) ordered complementary subalgebra pairs in **each** of ranks one and two. For each pair there are \(q\) permitted translations (central translations in rank one and scalar multiples of the complementary line in rank two).

For constants, exactly \(q\) values are central and \(q^3-q\) are noncentral. The rank-one orbit therefore has \(q^3(q+1)\) members; in rank two, zero translation gives \(q^2(q+1)\) and nonzero translation gives \(q^2(q+1)(q-1)\). Rank three contributes one identity. Adding these six disjoint orbit sizes yields \(q^3(2q+3)+1\). As each affine operator uniquely determines its linear projection and its translation at the origin, no object is counted twice.

## Verification

Run \(\texttt{python verify.py}\) using Python 3 and no external dependencies. The checker constructs all admissible projections and translations over \(\mathbb F_3\) and \(\mathbb F_5\), directly verifies the defining affine operator identity for every one of the \(244\) operators and all \(729\) ordered input pairs over \(\mathbb F_3\), and exhausts all \(1296\) canonical affine automorphisms to recover exactly six orbits of sizes \(1,3,24,36,72,108\). Over \(\mathbb F_5\) it builds \(1626\) operators and tests \(25\) selected input pairs for each; it does not enumerate all pairs or all affine conjugacies in that larger field. The general theorem rests on the proof above, not on finite-field testing.

## Relationship to prior work

Han, Khudoyberdiyev, Xie and Zhang (arXiv:2610.14838, first public October 10, 2026), Theorem 4.4 and Proposition 4.5, develop the general decomposition-and-translation characterization and the equivalence criterion for canonical Lie affgebras. Their explicit equivalence classification stops at dimension two; the six-orbit Heisenberg classification and finite-field orbit sizes are not stated there. The present proof independently expands the required operator identity and then resolves the dimension-three ordered-subalgebra geometry and affine translation orbits.

Ji and Hua (2018), and Rathee (arXiv:2402.15428, Sections 2 and 4), classify **ordinary linear** Rota–Baxter operators of the Heisenberg Lie algebra. Their operator spaces are broader in the linear part but do not classify affine translation parameters under the restricted, center-translation affgebra automorphism group. The earlier linear classification may imply some ingredients when combined with the 2026 characterization; those ingredients are not claimed as new. Ma, Zhang and Liu (arXiv:2606.22954) study affine group schemes and skew braces, a different affine Rota–Baxter structure.

## Limitations

This is the canonical bracket \(\{u,v\}=[u,v]+v\), not a classification of all Lie affgebra brackets on the underlying affine space. The classification excludes characteristic two. The finite-field formula assumes an odd prime power and is not a statement about arbitrary nonlinear or weight-one operators. The supporting finite checks prove no infinite-field claim by themselves. The novelty comparison does not exclude every implicit historical reformulation of this specialized orbit classification, particularly a reduction hidden in an earlier complete linear-operator classification. Independent mathematical verification has not been performed.

## References

1. J. Han, A. Khudoyberdiyev, Y. Xie and Y. Zhang, *Rota-Baxter operators and factorization of Lie affgebras*, arXiv:2610.14838 (first public 2026-10-10), especially Sections 4.2–4.3. https://arxiv.org/abs/2610.14838
2. N. Rathee, *Rota–Baxter operators and skew left brace structures over Heisenberg Group*, arXiv:2402.15428 (2024), especially Sections 2.2 and 4. https://arxiv.org/abs/2402.15428
3. G. Ji and X. Hua, *Rota-Baxter operators of 3-dimensional Heisenberg Lie algebra*, Korean J. Math. 26 (2018), 53–60. https://doi.org/10.11568/kjm.2018.26.1.53
4. J. Ma, B. Zhang and J. Liu, *Affine Rota-Baxter groups and affine skew braces*, arXiv:2606.22954 (2026). https://arxiv.org/abs/2606.22954
