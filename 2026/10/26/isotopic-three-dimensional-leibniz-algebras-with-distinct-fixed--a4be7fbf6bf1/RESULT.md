# Isotopic three-dimensional Leibniz algebras with distinct fixed-point-free automorphism densities

## Finding

For every odd prime power \(q\), let \(L_+(q)\) and \(L_-(q)\) be the three-dimensional two-step nilpotent non-Lie Leibniz algebras \(V\oplus\mathbb F_q z\), with \(\dim V=2\), \([v+az,w+bz]=B_\pm(v,w)z\), where \(B_+\) is a split and \(B_-\) an anisotropic nondegenerate symmetric bilinear form. The two algebras are isotopic but not isomorphic. Their automorphism groups have orders \(2q^2(q-1)^2\) and \(2q^2(q^2-1)\), and the numbers of automorphisms fixing only zero are, respectively, \(2q^2(q-2)^2\) and \(2q^2(q+1)(q-2)\). Thus their fixed-point-free automorphism densities are \(((q-2)/(q-1))^2\) and \((q-2)/(q-1)\), unequal over every odd finite field. In particular, fixed-point-free automorphism density is not an isotopism invariant even among three-dimensional two-step nilpotent non-Lie Leibniz algebras with one-dimensional derived ideal.

## Assumptions and scope

A Leibniz algebra means a left Leibniz algebra over \(\mathbb F_q\), with the identity \([x,[y,w]]=[[x,y],w]+[y,[x,w]]\). Our brackets have central values, so every double bracket vanishes, and satisfy both left and right Leibniz identities. The algebras are non-Lie because a nondegenerate symmetric bilinear form in odd characteristic cannot satisfy \(B(v,v)=0\) for every \(v\). Here \(q\) is an odd prime power, and the center and derived ideal are exactly \(\mathbb F_q z\). A split form has a nonzero isotropic vector; an anisotropic form has none. The \(\mathbb F_q\)-linear automorphism of \(L\) is fixed-point-free if its only fixed vector is zero. An isotopism is a triple of invertible linear maps \((F,G,H)\) satisfying \([Fx,Gy]_- = H([x,y]_+)\) for all \(x,y\).

## Proof

**1. Automorphism normal form.** The derived ideal is \(\mathbb F_q z\), preserved by every algebra automorphism. Hence every automorphism has a unique block form
\[
\Phi(v+tz)=Av+(\ell(v)+ct)z,
\quad A\in\operatorname{GL}(V),\quad \ell\in V^*,\quad c\in\mathbb F_q^\times.
\]
Bracket preservation is equivalent to \(B(Av,Aw)=cB(v,w)\) for all \(v,w\), so \(A\) belongs to the general orthogonal similitude group \(\operatorname{GO}(V,B)\), and \(c=\mu(A)\) is its multiplier. Conversely every such pair \((A,\ell)\) yields an automorphism. The block determinant of \(\Phi-I\) is \((c-1)\det(A-I)\). Therefore \(\Phi\) fixes only zero if and only if \(\mu(A)\ne1\) and \(\det(A-I)\ne0\). For each admissible \(A\), all \(q^2\) choices of \(\ell\) work.

**2. Split plane.** Choose an isotropic basis \(u,v\) with \(B_+(u,v)=1\); its Gram matrix is \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\). In odd characteristic the isotropic lines are precisely \(\mathbb F_q u\) and \(\mathbb F_q v\). Every similitude must permute them, hence is either diagonal \(\operatorname{diag}(a,b)\) or anti-diagonal \(\begin{pmatrix}0&a\\b&0\end{pmatrix}\), with \(a,b\in\mathbb F_q^\times\) and multiplier \(ab\). There are \(2(q-1)^2\) such matrices. In the diagonal family the fixed-point-free condition reads \(a\ne1,b\ne1,ab\ne1\); there are \((q-2)^2-(q-2)=(q-2)(q-3)\) choices, since among nonunit \(a\) the equation \(b=a^{-1}\) has exactly one solution other than one. In the anti-diagonal family \(\det(A-I)=1-ab\), so exactly \((q-1)(q-2)\) choices satisfy both requirements. The total is \(2(q-2)^2\), yielding \(|\operatorname{Aut}L_+|=2q^2(q-1)^2\) and exactly \(2q^2(q-2)^2\) fixed-point-free automorphisms.

**3. Anisotropic plane.** Identify \(V\) with the quadratic extension \(E=\mathbb F_{q^2}\), equipped with the symmetric polar form of the norm \(N(x)=x^{q+1}\): \(B_-(x,y)=(N(x+y)-N(x)-N(y))/2\). This is anisotropic and nondegenerate. Its full similitude group consists of the \(2(q^2-1)\) maps \(x\mapsto tx\) and \(x\mapsto tx^q\), with \(t\in E^\times\) and multiplier \(N(t)\). To see completeness, normalize a similitude by a multiplication to make it fix \(1\). Polarization shows that an isometry fixing \(1\) fixes the \(\mathbb F_q\)-coefficient of every \(x\) in the basis \(1,s\) with \(\operatorname{Tr}_{E/\mathbb F_q}(s)=0\), and then either fixes \(s\) or sends \(s\) to \(-s=s^q\). These are exactly the identity and conjugation. If \(N(t)\ne1\), multiplication by \(t\) cannot fix any nonzero \(x\) (which would force \(t=1\)); likewise \(tx^q=x\) for nonzero \(x\) would imply \(N(t)=1\) by taking norms. Thus every similitude with multiplier different from one automatically has \(\det(A-I)\ne0\). The norm map has \(q+1\) elements in each fiber, so each family contributes \((q^2-1)-(q+1)=(q+1)(q-2)\) suitable maps. This gives \(|\operatorname{Aut}L_-|=2q^2(q^2-1)\) and \(2q^2(q+1)(q-2)\) fixed-point-free automorphisms.

**4. Same isotopism type, different density.** For any Gram matrices \(M_+\) and \(M_-\) of the two forms, set \(F|_V=I\), \(G|_V=M_-^{-1}M_+\), and \(H|_V=I\), and let all three maps fix \(z\). Then
\[
B_-(Fv,Gw)=v^\mathsf{T}M_-M_-^{-1}M_+w=B_+(v,w),
\]
so \((F,G,H)\) is an isotopism. An isomorphism would induce a similitude between the forms and hence preserve existence of nonzero isotropic vectors. This is impossible for a split and an anisotropic plane; therefore the two algebras are not isomorphic. Dividing the fixed-point-free counts by the automorphism orders yields the two distinct stated densities. Their ratio is \((q-2)/(q-1)\), strictly below one for all odd \(q\). Thus the density is not an isotopism invariant, as claimed.

## Verification

The standalone script `verify_leibniz_fixfree.py` directly enumerates all invertible \(2\times2\) matrices over the prime fields \(\mathbb F_3,\mathbb F_5,\mathbb F_7\), checks their Gram-matrix similitude equations and multipliers, and counts those for which \(\Phi-I\) is invertible. The enumerations return (split GO size, split qualifying; anisotropic GO size, anisotropic qualifying) equal to \((8,2;16,8)\), \((32,18;48,36)\), and \((72,50;96,80)\), respectively. Multiplying by \(q^2\) recovers the automorphism counts. These finite checks are diagnostic only; the exact proof for every odd prime power is above.

## Relationship to prior work

La Rosa, Mancini, and Nagy classify isotopism types for two-step nilpotent Leibniz algebras with one-dimensional derived ideal and provide the bilinear-form framework. La Rosa and Mancini classify related two-step nilpotent Leibniz algebras by Kronecker modules. Those classification results do not, in the inspected sections, assert preservation or failure of fixed-point-free automorphism densities. A published finite-field computation for the three-dimensional Heisenberg **Lie** algebra counts fixed-point-free automorphisms, but its bracket is alternating, not symmetric; neither the split/non-split non-Lie distinction nor the isotopism noninvariance follows from that computation. The two orders of the general orthogonal similitude groups in dimension two are classical; novelty is not claimed for these group orders, but for the explicit density comparison and its isotopism consequence.

## Limitations

The finding addresses dimension three and odd characteristic only. It does not describe arbitrary bilinear forms, characteristic two, higher-dimensional Leibniz algebras, or nonlinear maps. The distinction involves ordinary (same-map) algebra automorphisms; isotopisms may have different maps on their two bracket arguments. The formulas use only the standard two-dimensional orthogonal similitude classification and are susceptible to an equivalent formulation in older finite classical-group literature; full historical priority is not independently certified.

## References

1. G. La Rosa, M. Mancini, and G. P. Nagy, “Isotopisms of nilpotent Leibniz algebras and Lie racks,” first arXiv posting 16 February 2023, arXiv:2302.08306; *Communications in Algebra* 52 (2024), 3812–3825.
2. G. La Rosa and M. Mancini, “Two-step nilpotent Leibniz algebras,” *Linear Algebra and its Applications* 637 (2022), 119–137; accessible manuscript listed by UCLouvain institutional repository.
3. A previously published exact finite-field fixed-point-free automorphism count for the three-dimensional Heisenberg Lie algebra (alternating central bracket); unlike the present result, no isotopism comparison is made.
