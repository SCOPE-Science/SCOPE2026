# Exact minimal cycle and cut projections on clique-prism graphs

## Finding

Let \(m\ge3\) be an integer and let \(G_m=K_m\square K_2\) be the unweighted Cartesian-product graph consisting of two copies of the complete graph \(K_m\), with corresponding vertices joined by a perfect matching. Equip its \(m^2\)-dimensional real oriented-edge space with the standard \(\ell_1\) norm. Write \(Z_m\) for its real cycle space (incidence kernel) and \(B_m\) for the real cut space (Euclidean orthogonal complement of \(Z_m\)). Their exact relative projection constants are

\[
\boxed{\lambda(Z_m,\ell_1^{m^2})=\frac{16(m-1)^2}{m(5m-2)},\qquad
\lambda(B_m,\ell_1^{m^2})=\frac{2(m^2-m+1)}{m^2-m+2}.}
\]

Explicit norm-minimizing projections appear below. Their symmetrizations are unique, although non-invariant minimizing projections need not be unique. The Euclidean orthogonal cycle projection is norm-minimizing exactly when \(m=4\); the Euclidean orthogonal cut projection is never norm-minimizing for any integer \(m\ge3\). For the triangular prism \(m=3\), the constants are \(64/39\) and \(7/4\), respectively.

## Assumptions and scope

All spaces, operators and projection norms are **real**; the edge norm is the unweighted \(\ell_1\) norm, not an \(\ell_2\) norm. Projection constant means the infimum of induced operator norms over **all** linear idempotents with the prescribed range, without symmetry imposed initially. The graph is simple and undirected, with one reference orientation chosen for each edge; changing orientations conjugates the matrices by coordinate sign changes and preserves the constants. The statement covers every integer \(m\ge3\), with no restriction to a finite enumeration.

Put \(r=\binom m2\). Orient each clique edge from its smaller to its larger vertex and each matching edge from the first to the second clique, so the edge space is \(\mathbb R^r\oplus\mathbb R^r\oplus\mathbb R^m\), with elements \((a,b,c)\). Let \(D:\mathbb R^r\to\mathbb R^m\) be the signed incidence matrix of \(K_m\), with \(-1\) at the smaller vertex and \(+1\) at the larger vertex. Let \(\mathbf1\) be the all-ones vector and put

\[
R=I_m-\frac{\mathbf1\mathbf1^{\mathsf T}}m,\qquad T=I_r-\frac{D^{\mathsf T}D}{m}.
\]

The graph incidence of \(G_m\) sends \((a,b,c)\) to \((Da-c,Db+c)\). Thus \(Z_m=\{(a,b,c):Da=c,\ Db=-c\}\) and \(B_m=Z_m^{\perp}\). Define, for each \(x=(a,b,c)\),

\[
u_0(x)=\frac{D(a-b)+mRc}{m+2},\qquad
u_H(x)=\frac{D(a-b)-2Rc}{2(m+2)},
\]
\[
P_0x=\left(Ta+\frac{D^{\mathsf T}u_0(x)}m,\ Tb-\frac{D^{\mathsf T}u_0(x)}m,\ u_0(x)\right),
\]
\[
Hx=\left(\frac{D^{\mathsf T}u_H(x)}m,\ -\frac{D^{\mathsf T}u_H(x)}m,\ u_H(x)\right).
\]

Here \(P_0\) is the Euclidean orthogonal projection onto \(Z_m\), and \(H\) is a nonzero map from \(B_m\) into \(Z_m\) vanishing on \(Z_m\). Write \(H^{\mathsf T}\) for its Euclidean transpose, and set

\[
t_m=\frac{(m-2)(m-4)}{5m-2},\qquad
s_m=\frac{(m-2)^2}{m^2-m+2}.
\]

The following projections attain the two stated constants:

\[
\boxed{P_Z=P_0+t_mH,\qquad P_B=I-P_0+s_mH^{\mathsf T}.}
\]

In particular, the second formula is a genuine projection **onto \(B_m\)**, not the generally different complementary operator \(I-P_Z\).

## Proof

**1. Orthogonal decomposition.** The clique incidence satisfies \(DD^{\mathsf T}=mR\). Hence \(T\) is the orthogonal projection of the clique edge space onto \(\ker D\). Each vector in \(Z_m\) has the unique orthogonal decomposition

\[
(a,b,c)= (k_a,0,0)+(0,k_b,0)
+\left(\frac{D^{\mathsf T}c}{m},-\frac{D^{\mathsf T}c}{m},c\right),
\qquad k_a,k_b\in\ker D,\quad Rc=c.
\]

The last map \(z(c)\) has squared Euclidean norm \((m+2)\|c\|_2^2/m\). Orthogonal projection onto these three summands yields exactly the displayed formula for \(P_0\). On the cut-space summand associated to antisymmetric mean-zero vertex potentials \((v,-v)\), the edge vector is

\[
b(v)=(D^{\mathsf T}v,-D^{\mathsf T}v,-2v),\qquad Rv=v,
\]

with \(\|b(v)\|_2^2=2(m+2)\|v\|_2^2\). Therefore the orthogonal extraction of this component is \(u_H(x)\), and \(H:z(v)\leftarrow b(v)\) is the stated map. In particular, \(P_0^2=P_0\), \(H^2=0\), \(P_0H=H\), and \(HP_0=0\). Every \(P_t=P_0+tH\) consequently projects onto \(Z_m\); by transposition every \(Q_s=I-P_0+sH^{\mathsf T}\) projects onto \(B_m\).

**2. Why one parameter suffices globally.** All graph automorphisms act by signed permutations on edges, hence as isometries of \(\ell_1^{m^2}\). The automorphism group contains \(S_m\times C_2\), acting by simultaneous clique permutations and interchange of the layers. Averaging any projection onto \(Z_m\) or \(B_m\) over this finite group leaves its range and its action on that range unchanged, and cannot increase its operator norm. It therefore suffices to minimize among equivariant projections.

Here is an elementary dimension count, with no global irreducibility assertion needed. Under layer interchange, the clique edge module splits into its even and odd copies of the signed edge module \(E=\mathbb R^{\binom m2}\); the matching edges give the odd copy of the permutation module \(U=\mathbb R^m\). The cut module has an even mean-zero copy of \(U_0=R U\) and an odd full copy of \(U\). The cycle module has an even and an odd copy of \(\ker D\), together with an odd copy of \(U_0\). Any \(S_m\)-equivariant map \(U\to E\) is a scalar multiple of \(D^{\mathsf T}\): the image of a vertex basis vector must be fixed by its \(S_{m-1}\) stabilizer, whose signed-edge fixed subspace is exactly the line spanned by the corresponding oriented star. Since \(\operatorname{ran}D^{\mathsf T}\perp\ker D\), no nonzero equivariant map from \(U\) or \(U_0\) into \(\ker D\) exists. The only shared summand for maps from cut to cycle is the odd \(U_0\); equivariant endomorphisms of \(U_0\) are scalars (a commuting permutation matrix on \(U\) has the form \(\alpha I+\beta\mathbf1\mathbf1^{\mathsf T}\)). Thus the space of equivariant maps \(B_m\to Z_m\) is one-dimensional, spanned by \(H\). Its reverse space is one-dimensional, spanned by \(H^{\mathsf T}\). Every equivariant cycle projection is \(P_t\), and every equivariant cut projection is \(Q_s\).

**3. Two column orbits.** Each of the signed edge actions has precisely two edge orbits: the \(m(m-1)\) clique edges and the \(m\) matching edges. The induced \(\ell_1\) operator norm is the largest absolute column sum. Write \(A_Z(t)\), \(U_Z(t)\) for the clique and matching column sums of \(P_t\), and \(A_B(s)\), \(U_B(s)\) for those of \(Q_s\). Using that \(D^{\mathsf T}(e_j-e_i)\) has one coefficient of magnitude two and \(2(m-2)\) coefficients of magnitude one, and that \(D^{\mathsf T}e_i\) has \(m-1\) coefficients of magnitude one, direct expansion yields, whenever \(-2\le t\le m\),

\[
A_Z(t)=3-\frac4m+\frac tm,\qquad
U_Z(t)=\frac{4(m-1)(m-t)}{m(m+2)}.
\]

The same affine expressions are **global lower bounds** for the corresponding absolute column sums at arbitrary real \(t\): fix the coefficient signs at any interior point of this interval and use \(|x|\ge\sigma x\) for each \(\sigma\in\{-1,1\}\). The two lines have opposite slopes, and cross exactly at \(t=t_m\). One verifies \(-2<t_m<m\) for every \(m\ge3\). At this point all the required signs are valid and both displayed equalities hold. Thus

\[
\inf_{t\in\mathbb R}\|P_t\|_{1\to1}
=\frac{16(m-1)^2}{m(5m-2)}.
\]

Similarly, for \(0\le s\le2\), the two column sums of \(Q_s\) are

\[
A_B(s)=2-\frac4{m(m+2)}+\frac{2s}{m(m+2)},\qquad
U_B(s)=\frac{3m-(m-1)s}{m+2}.
\]

Their affine expressions, obtained from the signs of the entries, also globally minorize the absolute sums for all real \(s\). They have opposite slopes and cross at \(s=s_m\). Since \(0<s_m<2\), the formulas hold with equality there, giving

\[
\inf_{s\in\mathbb R}\|Q_s\|_{1\to1}
=\frac{2(m^2-m+1)}{m^2-m+2}.
\]

Group averaging from step 2 makes both bounds global over **all** projections, not merely equivariant ones. The two increasing/decreasing-line intersections also make \(t_m,s_m\) the unique optimal parameters among equivariant projections.

**4. Orthogonal-projection transition.** \(P_0\) is optimal precisely when \(t_m=0\), or \(m=4\) for the stated integers. The orthogonal cut projector corresponds to \(s=0\), whereas \(s_m>0\) always, so it is never optimal. The parameter \(t_m\) is negative at \(m=3\) and positive at every \(m\ge5\).

## Verification

The accompanying standalone Python 3 program `verify_prism.py` uses only standard-library exact rational arithmetic. It constructs the projected columns without numerical pseudoinverses. It verified the two formulas for \(m=3,4,5,6,7,8\), and checked idempotence, range identities, the canonical decomposition, and equivariance under generating graph automorphisms for \(m=3,4,5\). The program reported **868 passed exact-rational assertions**. These finite checks are corroboration; the all-integer conclusion and minimization follow from the preceding algebra and symmetrization argument.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii (2023) develop invariant minimal cycle-space projections, including detailed calculations on equal-side discrete tori and homogeneous Hamming graphs. Their arXiv manuscript, sections 2.4–2.7, does not provide these two clique-prism constants or the accompanying one-parameter optimization; the present family has two unequal Cartesian factors \(K_m\) and \(K_2\) and two edge orbits. Their earlier 2018 manuscript develops transportation-cost/cycle-space representations and the group-averaging approach for diamond and Laakso graph families. Those broad methods motivate, but do not numerically entail, the formulas above without the present decomposition and optimization.

## Limitations

This result covers the **real unweighted** edge-space norms of the stated clique-prism family. It does not determine constants for weighted prisms, complex coefficients, ambient \(\ell_p\) exponents other than \(p=1\), or all Cartesian products of unequal complete graphs. It proves uniqueness only in the equivariant class, not uniqueness among arbitrary optimal projections. The originality assessment rests on identifiable sources and substantive comparisons, not a proof of global bibliographic uniqueness; unindexed or differently formulated prior results remain a possibility. Independent validation has not been performed.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1, first public 2023-05-21, especially Sections 1.1 and 2.1–2.7. https://arxiv.org/abs/2305.12582
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1, first public 2018-07-10, especially Sections 1.1–1.3 and 4–6. https://arxiv.org/abs/1807.03814
