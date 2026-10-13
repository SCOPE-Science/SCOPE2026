# Two generic quotient strata in the multiplicity-two boundary locus
## Finding
Let \(\mathcal C=\mathcal C(-1,1,1,2)\subset\mathcal M(-1,3,7)\) be the multiplicity-two boundary locus introduced by Almeida--Jardim--Oliveira. Thus a point \([E]\in\mathcal C\) has
\[
F=E^{\vee\vee}\in\mathcal R(-1,1,1),\qquad Q=F/E
\]
with \(Q\) pure one-dimensional of multiplicity \(2\) and Hilbert polynomial \(P_Q(t)=2t\).

There are two natural irreducible constructible families in \(\mathcal C\), reflecting the two irreducible components of the degree-two rank-zero-instanton moduli \(\mathcal T(2)\).

The **conic family** has dimension \(12\). Generically \(Q\) is the unique line bundle of ordinary degree \(-1\) on a smooth plane conic \(C\simeq\mathbf P^1\), the singular point \(p\) of \(F\) lies off the plane of \(C\), and the kernels are parametrized by
\[
\mathbf P\operatorname{Hom}(F,Q)\cong\mathbf P^1.
\]

The **skew-line family** has dimension \(11\). Generically
\[
Q\cong\mathcal O_{L_1}(-1)\oplus\mathcal O_{L_2}(-1)
\]
for two skew lines \(L_1,L_2\), with \(p\notin L_1\cup L_2\). For fixed \((F,L_1,L_2)\), all epimorphisms \(F\twoheadrightarrow Q\) have the same kernel up to isomorphism, so there is no additional quotient parameter.

## Assumptions and scope
The base field is \(\mathbf C\). The notation \(\mathcal M(-1,3,7)\), \(\mathcal R(-1,1,1)\), and \(\mathcal C(-1,1,1,2)\) follows arXiv:2609.32668v1. That paper proves that every \(F\in\mathcal R(-1,1,1)\) has a resolution
\[
0\longrightarrow\mathcal O_{\mathbf P^3}(-2)
\xrightarrow{(\ell_1,\ell_2,\ell_3)}
\mathcal O_{\mathbf P^3}(-1)^{\oplus3}
\longrightarrow F\longrightarrow0,
\]
where the three linear forms are independent. Their common zero is a point \(p\in\mathbf P^3\), the singular point of \(F\). It also records \(\dim\mathcal R(-1,1,1)=3\).

Jardim--Maican--Tikhomirov prove that the moduli \(\mathcal T(2)\) of semistable one-dimensional sheaves with Hilbert polynomial \(2t\) has exactly two irreducible components, each of dimension \(8\): the planar component \(\mathcal P_2\), whose generic member is supported on a smooth conic, and the component \(\mathcal T_{1,1}\), whose generic member is a direct sum of degree-one stable sheaves with disjoint supports.

The claim concerns only the two generic quotient types just described. It does not assert that these are all irreducible components of \(\mathcal C\), nor that \(\mathcal C\) is pure-dimensional.

## Proof
For the conic family, choose a smooth conic \(C\subset H\simeq\mathbf P^2\) and a point \(p\notin H\). Let \(F=F_p\in\mathcal R(-1,1,1)\) be represented by three independent linear forms vanishing at \(p\). Since \(p\notin H\), their restrictions to \(H\), hence to \(C\), span \(H^0(C,\mathcal O_C(1))\). Writing \(C\simeq\mathbf P^1\) with \(\mathcal O_C(1)\simeq\mathcal O_{\mathbf P^1}(2)\), restriction of the resolution gives
\[
0\longrightarrow\mathcal O_{\mathbf P^1}(-4)
\longrightarrow\mathcal O_{\mathbf P^1}(-2)^{\oplus3}
\longrightarrow F|_C\longrightarrow0.
\]
The induced three quadrics form a basis of \(H^0(\mathbf P^1,\mathcal O(2))\). Dualizing the standard evaluation sequence, or equivalently using \(H^0(F|_C)=0\) and the splitting theorem on \(\mathbf P^1\), gives
\[
F|_C\simeq\mathcal O_{\mathbf P^1}(-1)^{\oplus2}.
\]
Let \(Q_C\) be the unique degree-\(-1\) line bundle on \(C\simeq\mathbf P^1\). Its Hilbert polynomial with respect to the conic embedding is \(2t\). Therefore
\[
\operatorname{Hom}(F,Q_C)
=\operatorname{Hom}(F|_C,Q_C)\cong\mathbf C^2,
\]
and every nonzero map is surjective. Modulo the scalar automorphisms of \(F\) and \(Q_C\), the kernels for fixed \((F,C)\) are parametrized by \(\mathbf P^1\).

Smooth plane conics form an irreducible \(8\)-dimensional family: \(3\) parameters for the plane and \(5\) for the conic in that plane. The condition \(p\notin H\) is open. Since \(\mathcal R(-1,1,1)\) has dimension \(3\), the total conic family therefore has dimension
\[
3+8+1=12.
\]
The kernel determines its double dual \(F\), its quotient \(Q_C\), and the projective quotient map, so the induced map to \(\mathcal M(-1,3,7)\) is generically injective. Hence its image is an irreducible constructible set of dimension \(12\).

For the skew-line family, choose two disjoint lines \(L_1,L_2\subset\mathbf P^3\) and \(p\notin L_1\cup L_2\). On a line \(L\) avoiding \(p\), the three restricted linear forms span \(H^0(L,\mathcal O_L(1))\). After changing bases, the restricted presentation is
\[
0\longrightarrow\mathcal O_L(-2)
\xrightarrow{(x,y,0)}
\mathcal O_L(-1)^{\oplus3}
\longrightarrow F|_L\longrightarrow0,
\]
so
\[
F|_L\simeq\mathcal O_L\oplus\mathcal O_L(-1).
\]
Consequently
\[
\dim\operatorname{Hom}\!\left(F,\mathcal O_L(-1)\right)=1,
\]
and every nonzero map is surjective. Put
\[
Q=\mathcal O_{L_1}(-1)\oplus\mathcal O_{L_2}(-1).
\]
Because the supports are disjoint, \(\operatorname{Aut}(Q)\cong(\mathbf C^\ast)^2\). Each of the two component homomorphism spaces is one-dimensional, so all epimorphisms \(F\twoheadrightarrow Q\) differ by an automorphism of \(Q\) and have the same kernel. Thus there is no additional map parameter. The open family of unordered pairs of skew lines has dimension \(8\), and the choice of \(F\) contributes \(3\), giving exact dimension
\[
3+8=11.
\]
Again the kernel recovers \(F=E^{\vee\vee}\) and \(Q=F/E\), so the induced family in the moduli space is generically injective and irreducible.

In both constructions the kernel \(E\subset F\) has the same rank and first Chern class as the slope-stable sheaf \(F\). Any positive-rank proper subsheaf of \(E\) is therefore a subsheaf of \(F\), so \(E\) is slope-stable. Since \(P_Q(t)=2t\), Riemann--Roch gives
\[
\operatorname{ch}(Q)=2H^2-4H^3.
\]
For \(F\) with Chern classes \((-1,1,1)\),
\[
\operatorname{ch}(F)=2-H-\frac12H^2+\frac56H^3.
\]
Thus the kernel has
\[
(c_1,c_2,c_3)(E)=(-1,3,7).
\]
Moreover \(E^{\vee\vee}=F\) and \(F/E=Q\) is pure of multiplicity \(2\), so every constructed kernel belongs to \(\mathcal C(-1,1,1,2)\).

## Verification
The geometric premises were checked in the full text of arXiv:2609.32668v1: Theorem 2.16 gives \(\dim\mathcal R(-1,1,1)=3\); Definition 5.7 and Proposition 5.8 identify \(\mathcal C(-1,1,1,2)\), prove \(P_Q(t)=2t\), and give the three-linear-form resolution of \(F\). The paper explicitly says that further study of \(\mathcal C(-1,1,1,2)\) would be interesting.

The degree-two quotient classification was checked in the full text of arXiv:1702.06553v1. Its Proposition 18 proves that \(\mathcal T(2)\) has exactly two irreducible \(8\)-dimensional components, the planar component and the \((1,1)\)-component. The generic members used above are respectively a degree-\(-1\) line bundle on a smooth conic and the direct sum of \(\mathcal O_L(-1)\) on two disjoint lines.

The restriction calculations are exact applications of the displayed resolution of \(F\) and the splitting theorem on \(\mathbf P^1\). No finite computation is used as a substitute for proof.

## Relationship to prior work
Almeida--Jardim--Oliveira prove that every point of \(\mathcal C(-1,1,1,2)\) is a smooth point of \(\mathcal M(-1,3,7)\), but they do not determine the dimension, irreducible structure, or generic quotient strata of \(\mathcal C\); they explicitly leave this locus for further study.

Jardim--Maican--Tikhomirov classify the two irreducible components of \(\mathcal T(2)\), but do not combine that classification with the \(\mathcal R(-1,1,1)\) hulls in \(\mathcal M(-1,3,7)\). The two dimension counts above arise from that combination together with the exact restriction splittings of the hull.

Published-finding searches under the exact locus notation, the smooth-conic quotient formulation, the skew-line quotient formulation, and the equivalent kernel formulation found no statement implying these two exact strata.

## Limitations
The result does not claim a complete irreducible decomposition of \(\mathcal C(-1,1,1,2)\). Special incidence loci where the singular point \(p\) meets the support or its plane may have different homomorphism dimensions, and degenerations inside the two quotient components are not classified here. No assertion is made that the \(11\)-dimensional skew-line family is an irreducible component of \(\mathcal C\).

## References
C. Almeida, M. Jardim, and L. Oliveira, “The moduli space of torsion-free sheaves with quasi-maximal third Chern class,” arXiv:2609.32668v1, first public 2026-09-26; especially Theorem 2.16, Definition 5.7, Proposition 5.8, and Proposition 5.9.

M. Jardim, M. Maican, and A. S. Tikhomirov, “Moduli spaces of rank 2 instanton sheaves on the projective space,” arXiv:1702.06553v1; especially Section 4.1 and Proposition 18.
