# Full projective symmetry of Płoski's moustache curve
## Finding
## Finding
For every integer \\(m\\ge 2\\), set
\\[
q_j=y^2+xz+jx^2,\\qquad Q_m=\\prod_{{j=1}}^m q_j,\\qquad C_m=V(Q_m)\\subset\\mathbb P^2_{\\mathbb C}.
\\]
Then the full projective stabilizer of \\(C_m\\) is
\\[
\\operatorname{{Aut}}_{{\\mathbb P^2}}(C_m)\\cong\\mathbb G_a\\rtimes\\mu_4.
\\]
Explicitly, define
\\[
U_t[x:y:z]=[x:y+tx:z-2ty-t^2x],\\qquad t\\in\\mathbb C,
\\]
and
\\[
R_m[x:y:z]=[x:iy:-(m+1)x-z].
\\]
Every element of \\(\\operatorname{{Aut}}_{{\\mathbb P^2}}(C_m)\\) is uniquely \\(U_tR_m^k\\) with \\(k\\in\\{{0,1,2,3\\}}\\), and
\\[
R_mU_tR_m^{{-1}}=U_{{it}}.
\\]
Thus \\(\\mu_4\\) acts on \\(\\mathbb G_a\\) through multiplication by \\(i\\). On the set of the \\(m\\) conic components, \\(U_t\\) acts trivially and \\(R_m\\) induces the reflection \\(j\\mapsto m+1-j\\).

The infinitesimal generator of the additive subgroup is \\(x\\partial_y-2y\\partial_z\\). It annihilates every \\(q_j\\), hence
\\[
x(Q_m)_y-2y(Q_m)_z=0.
\\]
This identifies an explicit geometric source for the linear Jacobian syzygy behind the known value \\(\\operatorname{{mdr}}(Q_m)=1\\).

## Assumptions and scope
The ground field is \\(\\mathbb C\\), and \\(m\\ge2\\). The statement concerns the full stabilizer inside \\(\\operatorname{{PGL}}_3(\\mathbb C)\\) of the reduced curve \\(C_m\\) in the displayed normal form. Each \\(q_j\\) is a smooth irreducible conic: the symmetric matrix of \\(y^2+xz+\\lambda x^2\\) has determinant \\(-1/4\\) for every finite \\(\\lambda\\).

The claim does not classify projective stabilizers of all even Płoski curves in arbitrary normal forms or with arbitrary choices of conics. It is specific to the named arithmetic-parameter moustache family used in the source.

## Proof
Because \\(m\\ge2\\), any projective transformation preserving the reduced union \\(C_m\\) permutes its irreducible conic components and therefore preserves their two-dimensional span
\\[
W=\\langle y^2+xz,\\ x^2\\rangle.
\\]
In the pencil \\(W\\), every finite member \\(y^2+xz+\\lambda x^2\\) is nonsingular, since its determinant is \\(-1/4\\). Hence \\([x^2]\\) is the unique singular, indeed rank-one, member of the projective pencil. Consequently a stabilizing projective transformation \\(T\\) must satisfy \\(x\\circ T=a x\\) for some \\(a\\ne0\\).

Write
\\[
x'=ax,\\qquad y'=bx+cy,\\qquad z'=ex+fy+gz.
\\]
There can be no \\(z\\)-term in \\(y'\\), because otherwise the pullback of \\(y^2+xz\\) would have a nonzero \\(z^2\\)-term and would leave \\(W\\). Requiring \\(y'^2+x'z'\\in W\\) gives
\\[
c^2=ag,\\qquad af+2bc=0.
\\]
Therefore
\\[
q_\\lambda\\circ T
=c^2\\left(y^2+xz+\\phi(\\lambda)x^2\\right),\\qquad
\\phi(\\lambda)=\\frac{{b^2+ae+a^2\\lambda}}{{c^2}}.
\\]
Thus \\(T\\) induces an affine transformation \\(\\phi(\\lambda)=u\\lambda+v\\) that permutes the finite set \\(S=\\{{1,\\ldots,m\\}}\\).

The affine stabilizer of \\(S\\) has exactly two elements. Indeed its centroid is \\(c_0=(m+1)/2\\), and
\\[
\\sum_{{j=1}}^m(j-c_0)^2=\\frac{{m(m^2-1)}}{{12}}\\ne0.
\\]
An affine permutation \\(\\lambda\\mapsto u\\lambda+v\\) fixes the centroid and preserves this centered second moment, so \\(u^2=1\\). Hence either \\(u=1,v=0\\), or \\(u=-1,v=m+1\\).

Scale the matrix of \\(T\\) projectively so that \\(a=1\\). In the identity case, \\(c^2=1\\), and the two choices \\(c=1,-1\\) give respectively
\\[
T=U_b,\\qquad T=U_bR_m^2.
\\]
In the reflection case, \\(c^2=-1\\), and \\(c=i,-i\\) give respectively
\\[
T=U_bR_m,\\qquad T=U_bR_m^3.
\\]
This exhausts the stabilizer and proves the unique normal form \\(U_tR_m^k\\).

Direct substitution gives \\(q_j\\circ U_t=q_j\\) and
\\[
q_j\\circ R_m=-q_{{m+1-j}}.
\\]
Moreover \\(R_m^2[x:y:z]=[x:-y:z]\\), \\(R_m^4=1\\), and matrix multiplication gives \\(R_mU_tR_m^{{-1}}=U_{{it}}\\). Hence the group is the asserted semidirect product.

Finally, differentiating \\(U_t\\) at \\(t=0\\) gives the vector field \\(x\\partial_y-2y\\partial_z\\). Since it kills every \\(q_j\\), it kills their product \\(Q_m\\), proving the displayed linear Jacobian syzygy.

## Verification
The accompanying `verify.py` performs exact symbolic checks of the following identities: invariance under \\(U_t\\); reflection under \\(R_m\\); the order-four and conjugation relations; nonsingularity of every finite pencil member; the coefficient identities yielding the induced affine map; the centered second-moment formula; the four matrix normal forms; and the infinitesimal Jacobian syzygy. It also exhaustively confirms for \\(2\\le m\\le8\\) that the affine stabilizer of \\(\\{{1,\\ldots,m\\}}\\) is only the identity and reflection. The finite checks illustrate the general moment argument and are not used as a substitute for it.

Running `python verify.py` returns `VERIFY_OK`.

## Relationship to prior work
Pokora's Example 4.2 uses exactly \\(Q_m=\\prod_{{j=1}}^m(xz+jx^2+y^2)\\), recalls that this Płoski moustache curve has one singular point, and states that \\(\\operatorname{{mdr}}(Q_m)=1\\), hence the curve is free. The source does not state the full projective stabilizer, the additive one-parameter subgroup, the order-four extension, or the induced reflection on the components.

Cheltsov treats even Płoski curves in the broader extremal-singularity and GIT setting and records that even Płoski curves are GIT-semistable. That literature motivates asking for the actual isotropy of an explicit representative, but the inspected discussion does not give the stabilizer computed here.

Targeted searches for Płoski/moustache automorphism groups, projective stabilizers, additive symmetries, conic-pencil stabilizers, and the Jacobian-syzygy interpretation did not identify a source whose statement implies the theorem above. The closest located projective-stabilizer results concern different plane curves or different conic arrangements.

## Limitations
The theorem is over \\(\\mathbb C\\) and is tied to the arithmetic parameter set \\(\\{{1,\\ldots,m\\}}\\). Replacing that set by an arbitrary finite subset of the same conic pencil changes the finite component of the stabilizer to the affine stabilizer of the chosen parameter set. No assertion is made here about abstract automorphisms of the singular curve that are not induced by \\(\\operatorname{{PGL}}_3\\), nor about arbitrary even Płoski curves outside this displayed family.

## References
1. P. Pokora, *On free and nearly free arrangements of conics admitting certain ADE singularities*, arXiv:2303.08584v1 (15 March 2023); Ann. Univ. Ferrara 70 (2024), 593–606, DOI:10.1007/s11565-023-00481-6. Example 4.2.
2. I. Cheltsov, *Worst Singularities of Plane Curves of Given Degree*, J. Geom. Anal. 27 (2017), 2302–2338, DOI:10.1007/s12220-017-9762-y. Definition 1.7, Example 1.14, Theorem 1.15.
