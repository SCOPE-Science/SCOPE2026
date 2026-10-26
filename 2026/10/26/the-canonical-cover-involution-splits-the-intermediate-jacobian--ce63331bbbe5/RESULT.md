# The canonical-cover involution splits the intermediate Jacobian in dimensions six and eight

## Finding

Let \(V\subset\mathbf P^6_{\mathbf C}\) be a smooth complete intersection of three quadrics, and let \(\sigma\) be the canonical-cover involution in Sarikyan's Fano--Enriques construction, with exactly eight isolated fixed points. Then \(\sigma^*\) has eigenspace dimensions \(12\) and \(16\) on \(H^3(V,\mathbf Q)\), and dimensions \(6\) and \(8\) on \(H^{2,1}(V)\). Consequently, the intermediate Jacobian \(J(V)\) is isogenous to invariant and anti-invariant abelian subvarieties of dimensions \(6\) and \(8\).

## Assumptions and scope

Work over \(\mathbf C\). The threefold is smooth, cut out by three quadrics in \(\mathbf P^6\), and the holomorphic involution has exactly eight isolated fixed points. The fixed-point count is a premise from the cited canonical-cover construction, not a claim about arbitrary intersections of three quadrics. The result determines dimensions and an isogeny decomposition only; it does not determine the factors' isomorphism classes, polarizations, endomorphism rings, or simplicity.

## Proof

Write \(H=c_1(\mathcal O_V(1))\). The normal bundle sequence gives
\[
c(T_V)=\frac{(1+H)^7}{(1+2H)^3},\qquad c_3(T_V)=-3H^3.
\]
Since \(\int_V H^3=2^3=8\), the topological Euler characteristic is \(\chi(V)=-24\). Weak Lefschetz gives \(b_0=b_2=b_4=b_6=1\) and \(b_1=b_5=0\), so \(b_3=4-\chi(V)=28\).

At an isolated fixed point of a holomorphic involution, the real local fixed-point index is \(+1\): the derivative has no eigenvalue \(1\), and each complex eigenvalue contributes a positive real determinant to \(\det_{\mathbf R}(I-d\sigma)\). The topological Lefschetz formula therefore gives
\[
\sum_i(-1)^i\operatorname{tr}(\sigma^*|H^i(V,\mathbf Q))=8.
\]
The involution fixes \(H^0,H^2,H^4,H^6\), each with trace \(1\), because it preserves constants, the ample hyperplane class, and the complex orientation. Thus \(4-\operatorname{tr}(\sigma^*|H^3)=8\), so the trace on \(H^3\) is \(-4\). If \(m_+,m_-\) are the \(+1,-1\) multiplicities, then \(m_++m_-=28\) and \(m_+-m_-=-4\), hence \((m_+,m_-)=(12,16)\).

As \(V\) is Fano, \(H^{3,0}=0\), and \(h^{2,1}=h^{1,2}=14\). Complex conjugation pairs the eigenspaces in \(H^{2,1}\) and \(H^{1,2}\), so each has trace \(-2\). Solving \(r_++r_-=14\), \(r_+-r_-=-2\) gives \((r_+,r_-)=(6,8)\) on \(H^{2,1}\). The induced involution on \(J(V)\) therefore has invariant and anti-invariant tangent spaces of dimensions \(6\) and \(8\); the images of \(1+\sigma\) and \(1-\sigma\) give abelian subvarieties whose addition map is an isogeny.

## Verification

The accompanying `verify.py` checks the Chern-class coefficient, Euler characteristic, Betti number, Lefschetz trace, and eigenspace equations using exact integer arithmetic. The script does not certify the geometric inputs: smoothness, weak Lefschetz, the local index, and the topological Lefschetz theorem are used in their standard forms. The eight-fixed-point hypothesis comes from the cited construction.

## Relationship to prior work

Sarikyan's paper constructs the canonical cover as a smooth intersection of three quadrics in \(\mathbf P^6\) with an involution fixing eight points, and studies birational properties of the quotient. The present claim is limited to the evaluated \(H^3\) representation and intermediate-Jacobian eigenspace dimensions. It is a specialization of standard Chern-class and Lefschetz tools, not a new general fixed-point theorem. published-finding corpus and accessible own-ledger searches for this family, fixed-point count, trace, and equivalent eigenspace formulations found no matching record; absence of a search hit is not proof of priority.

## Limitations

The claim requires the smooth canonical cover and exactly eight isolated fixed points. It does not determine the factors' polarization types, simplicity, endomorphism rings, or isomorphism classes, and it makes no claim about the quotient's rationality.

## References

1. A. Sarikyan, *On the Rationality of Fano-Enriques Threefolds*, arXiv:2208.09296v1, first public 2022-08-19, especially the canonical-cover construction in §2.2: https://arxiv.org/abs/2208.09296.
2. The normal bundle formula for smooth complete intersections, weak Lefschetz, and the topological Lefschetz fixed-point formula are used in their standard forms.
