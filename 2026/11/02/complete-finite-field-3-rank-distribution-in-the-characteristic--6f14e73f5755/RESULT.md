# Complete finite-field \(3\)-rank distribution in the characteristic-three Ciani family

## Finding

Let \(k=\overline{\mathbb F}_3\) and consider the normalized Ciani plane quartic
\[
C_{a,b,c}:\quad X^4+Y^4+Z^4+aX^2Y^2+bX^2Z^2+cY^2Z^2=0.
\]
Write \(U\subset\mathbb A^3_k\) for the parameters giving smooth curves. The three elliptic quotient supersingularity divisors in this *marked coefficient space* are exactly
\[
D_1:ab+c=0,\qquad D_2:ac+b=0,\qquad D_3:bc+a=0.
\]
They are individually smooth surfaces on \(U\), every pair meets transversely along a punctured coordinate axis, and the three meet transversely only at \((a,b,c)=(0,0,0)\), the Fermat quartic.

If \(r\) of these equations hold, the geometric Jacobian has \(3\)-rank \(3-r\), \(a\)-number \(r\), and Newton slopes \(0^{3-r},(1/2)^{2r},1^{3-r}\). Every value \(r\in\{0,1,2,3\}\) occurs over the algebraic closure. Thus all \(3\)-rank strata, not just the superspecial locus, are explicitly determined.

For every finite extension \(\mathbb F_q/\mathbb F_3\), \(q=3^m\), \(m\ge1\), the **exact number of smooth labeled coefficient triples** of each \(3\)-rank is
\[
\begin{array}{c|cccc}
\text{geometric }3\text{-rank}&0&1&2&3\\\hline
\#(a,b,c)\in U(\mathbb F_q)&1&3(q-3)&3(q-3)(q-5)&(q-3)(q^2-7q+18).
\end{array}
\]
The total number of smooth coefficient triples is
\[
\boxed{\#U(\mathbb F_q)=(q-2)^3-(q-3)^2.}
\]
The unique superspecial normalized coefficient triple over \(k\) is \((0,0,0)\); this uniqueness statement pertains to the chosen normalization, not to all possible equations for that geometric curve.

## Assumptions and scope

The characteristic is exactly three. The quartic coefficient normalization fixes the three pure fourth-power coefficients equal to one. All geometric statements are over \(k\). The smooth locus is explicitly
\[
U=\big\{(a,b,c):\Delta(a,b,c)\ne0\big\},\quad
\Delta=(a^2-1)(b^2-1)(c^2-1)(a^2+b^2+c^2-abc-1).
\]
The numerical formulas count **coefficient triples in this affine family**, not distinct geometric or arithmetic isomorphism classes, twists, or points of a coarse moduli space. The family is of smooth nonhyperelliptic curves of genus three.

## Proof

**1. Smoothness and elliptic factors.** The smoothness criterion is the specialization to characteristic three of the standard Ciani discriminant, which is proved directly by the Jacobian criterion. Indeed, if all three projective coordinates are nonzero, the vanishing of the three partial derivatives forces a nonzero kernel of the symmetric matrix
\[
\begin{pmatrix}1&-a&-b\\-a&1&-c\\-b&-c&1\end{pmatrix},
\]
whose determinant is the negative of the last factor of \(\Delta\); if one coordinate vanishes, one of \(a^2-1,b^2-1,c^2-1\) vanishes. Conversely, these conditions produce geometric singularities. Thus \(\Delta\ne0\) is equivalent to smoothness.

The three sign-change involutions of \(C_{a,b,c}\) generate a Klein four-group in projective space. The quotient by each nontrivial involution has genus one. The three quotient Jacobians induce an isogeny from their product onto \(\operatorname{Jac}(C_{a,b,c})\) whose kernel is killed by a power of two (as follows from the character idempotents of the Klein four-group). Because \(3\) is coprime to this degree, the induced map on \(3\)-divisible groups is an isomorphism. Consequently \(3\)-rank, \(a\)-number, and Newton slopes are the additive data of the three elliptic factors. This is stronger than a bare isogeny statement for the \(a\)-number.

**2. The three Hasse surfaces.** Quotient by the sign change in \(X\), putting \(u=X^2\) and completing the square, gives a genus-one double cover
\[
w^2=(a^2-4)Y^4+(2ab-4c)Y^2Z^2+(b^2-4)Z^4.
\]
For a smooth elliptic quartic \(w^2=A t^4+B t^2+C\) in characteristic three the Hasse invariant is the coefficient of \(t^{2}\) in the quartic, namely \(B\). Thus that quotient is supersingular precisely when \(ab+c=0\). Cycling the coordinates gives the other two conditions. Their common zero set is analyzed on the smooth parameter space as follows. On \(D_1\cap D_2\), substitute \(c=-ab\) into \(ac+b=0\) to obtain \(b(1-a^2)=0\). Since \(a^2\ne1\) on \(U\), we have \(b=c=0\). Therefore
\[
D_1\cap D_2=\{(a,0,0):a^2\ne1\},
\]
and cyclic permutation gives the other two coordinate axes. Their common intersection is the origin. Pairwise gradients along these axes are independent because the relevant determinant equals \(1-a^2\), which is nonzero there. The three gradients at the origin are coordinate vectors, giving transverse triple intersection. Each \(D_i\) is itself smooth, as it is the graph of one coefficient in terms of the other two. Hence these are the complete geometric strata.

**3. The full finite-field count.** Fix \(q=3^m\) and let \(T=\mathbb F_q\setminus\{1,-1\}\), so \(\#T=q-2\). For \(a,b\in T\), the final factor of \(\Delta\), regarded as a quadratic in \(c\), is
\[
P(c)=c^2-abc+a^2+b^2-1.
\]
Its discriminant in characteristic three is
\[
\operatorname{disc}_c P=(a^2-1)(b^2-1),
\]
which is nonzero for \(a,b\in T\). Write \(\chi\) for the quadratic character of \(\mathbb F_q\), with \(\chi(0)=0\). The number of roots \(c\in\mathbb F_q\) is \(1+\chi((a^2-1)(b^2-1))\). On restricting to \(c\in T\), subtract the two disjoint cases \(c=1\) and \(c=-1\), where respectively \(a=-b\) and \(a=b\). There are \(q-2\) pairs in each case. The standard quadratic-character identity
\[
\sum_{a\in T}\chi(a^2-1)=-1
\]
follows by counting solutions of \((y-a)(y+a)=-1\), which has \(q-1\) nonzero-factor solutions. It follows that the number of parameter triples with all three coefficients in \(T\) and \(P(c)=0\) equals
\[
(q-2)^2+(-1)^2-2(q-2)=(q-3)^2.
\]
Thus \(\#U(\mathbb F_q)=(q-2)^3-(q-3)^2\).

On \(D_1\) one has \(c=-ab\). The remaining smoothness conditions reduce to \(a,b\ne\pm1\) and \(ab\ne\pm1\); hence
\[
\#D_1(\mathbb F_q)=(q-2)^2-2(q-3)=q^2-6q+10,
\]
and similarly for the other divisors. Each pair intersection is a coordinate axis with \(q-2\) points; their common intersection has one point. Therefore the number with exactly \(r=3\) supersingular factors is one, with exactly \(r=2\) it is \(3(q-3)\), and with exactly \(r=1\) it is
\[
3(q^2-6q+10)-2\cdot3(q-3)-3=3(q-3)(q-5).
\]
Subtracting these from \(\#U(\mathbb F_q)\) gives the stated \(r=0\) count \((q-3)(q^2-7q+18)\). As \(3\)-rank is \(3-r\), the displayed table follows for every \(m\ge1\). Every geometric stratum is nonempty: the open complement of the three proper divisors is nonempty, each divisor has a two-dimensional open part, the punctured axes are nonempty over \(k\), and their triple point is smooth.

## Verification

The accompanying standalone `verify_ciani3.py` uses only Python standard-library arithmetic. It exhaustively enumerates the complete coefficient fields \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\), independently testing the discriminant criterion and the three Hasse equations, then compares all four stratum counts and the smooth total with the exact polynomials. Its `ciani3_output.txt` ends in `VERIFY_OK`. The infinite sequence of extension-field counts is established by the character-sum proof above, not extrapolated from these finite checks.

## Relationship to prior work

The three-involution Ciani family and its moduli parametrization are classical; Lercier–Ritzenthaler–Rovetta–Sijsling describe the family and its parameter redundancies. Ohashi's study of Ciani curves in all odd characteristics explicitly gives the smoothness discriminant and elliptic quotient models, and focuses on superspecial maximality; Brock's earlier superspecial classifications are acknowledged there. These established facts are background. The assessed contribution is the *complete characteristic-three geometric rank-stratum incidence together with all-extension exact polynomial counts of normalized smooth coefficient triples for every rank*, which are not stated in the inspected primary results. In particular, these are not moduli-class enumeration results.

## Limitations

The formulas refer to one affine normalization with many equations representing isomorphic curves; no division by parameter symmetries or enumeration of arithmetic twists is asserted. The result applies only in characteristic three, and the six pure or mixed coefficient normalizations are held fixed as displayed. The full priority comparison is qualified by the possibility of older tables implicit in the general Ciani literature. No independent scientific audit has been performed.

## References

1. R. Lercier, C. Ritzenthaler, F. Rovetta and J. Sijsling, “Parametrizing the moduli space of curves and applications to smooth plane quartics over finite fields,” arXiv:1403.0562, first public 3 March 2014; see §3.2 for the Ciani family and parameter equivalences. https://arxiv.org/html/1403.0562v4
2. R. Ohashi, “On the maximality of genus-3 nonhyperelliptic curves of Ciani type,” arXiv:2201.12996v1, 31 January 2022; see Lemma 2.1, §3 and Theorem 1.1. https://arxiv.org/abs/2201.12996
